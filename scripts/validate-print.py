#!/usr/bin/env python3
"""Validate detectable geometry problems in the generated 6x9 PDF."""

from __future__ import annotations

import argparse
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    import pymupdf
except ImportError:
    print(
        "PRINT ERROR: PyMuPDF is required; install requirements-print.txt",
        file=sys.stderr,
    )
    raise SystemExit(2)


POINTS_PER_INCH = 72.0
EXPECTED_WIDTH = 6 * POINTS_PER_INCH
EXPECTED_HEIGHT = 9 * POINTS_PER_INCH
PAGE_SIZE_TOLERANCE = 2.0

INSIDE_MARGIN = 22 / 25.4 * POINTS_PER_INCH
OUTSIDE_MARGIN = 17 / 25.4 * POINTS_PER_INCH
TOP_MARGIN = 18 / 25.4 * POINTS_PER_INCH
BOTTOM_MARGIN = 20 / 25.4 * POINTS_PER_INCH
GEOMETRY_TOLERANCE = 6.0
PHYSICAL_TOLERANCE = 0.75
# Header/footer content is allowed in the corresponding configured margin.
# Body objects crossing back into those margins are still caught by their bbox.
HEADER_BAND = TOP_MARGIN
FOOTER_BAND = BOTTOM_MARGIN
WIDE_RULE_FRACTION = 0.40

URL_OR_LONG_TOKEN = re.compile(r"(?:https?://|www\.|\S{48,})", re.IGNORECASE)
MONOSPACE_FONT = re.compile(r"(?:mono|courier|consolas|code)", re.IGNORECASE)


@dataclass(frozen=True)
class Finding:
    page: int
    kind: str
    message: str
    bbox: tuple[float, float, float, float] | None = None

    def render(self) -> str:
        location = ""
        if self.bbox is not None:
            location = " bbox=(" + ", ".join(f"{value:.1f}" for value in self.bbox) + ")"
        return f"PRINT ERROR page {self.page} [{self.kind}]:{location} {self.message}"


def is_finite_rect(rect: pymupdf.Rect) -> bool:
    return all(math.isfinite(value) for value in (rect.x0, rect.y0, rect.x1, rect.y1))


def in_body_vertical_band(rect: pymupdf.Rect, page_height: float) -> bool:
    center = (rect.y0 + rect.y1) / 2
    return HEADER_BAND <= center <= page_height - FOOTER_BAND


def classify_text(font: str, text: str) -> str:
    if MONOSPACE_FONT.search(font):
        return "code-overflow"
    if URL_OR_LONG_TOKEN.search(text):
        return "unbreakable-text-overflow"
    return "text-overflow"


def validate_pdf(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    try:
        document = pymupdf.open(path)
    except Exception as error:
        return [Finding(0, "malformed-pdf", f"cannot open PDF: {error}")]

    if document.page_count == 0:
        return [Finding(0, "malformed-pdf", "PDF contains no pages")]

    for page_index, page in enumerate(document):
        page_number = page_index + 1
        page_rect = page.rect
        width, height = page_rect.width, page_rect.height

        if abs(width - EXPECTED_WIDTH) > PAGE_SIZE_TOLERANCE or abs(height - EXPECTED_HEIGHT) > PAGE_SIZE_TOLERANCE:
            findings.append(
                Finding(
                    page_number,
                    "page-size",
                    f"expected 6x9 inch ({EXPECTED_WIDTH:.1f}x{EXPECTED_HEIGHT:.1f}pt), "
                    f"found {width:.1f}x{height:.1f}pt",
                )
            )

        printable_left = INSIDE_MARGIN
        printable_right = width - OUTSIDE_MARGIN
        printable_top = TOP_MARGIN
        printable_bottom = height - BOTTOM_MARGIN
        meaningful_body_objects = 0

        text = page.get_text("dict")
        for block in text.get("blocks", []):
            block_rect = pymupdf.Rect(block["bbox"])
            if block.get("type") == 1:
                if in_body_vertical_band(block_rect, height):
                    meaningful_body_objects += 1
                if not page_rect.contains(block_rect):
                    findings.append(
                        Finding(page_number, "image-page-overflow", "image extends outside the physical page", tuple(block_rect))
                    )
                continue
            if block.get("type") != 0:
                continue

            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    value = span.get("text", "")
                    if not value.strip():
                        continue
                    rect = pymupdf.Rect(span["bbox"])
                    if not is_finite_rect(rect) or rect.x1 < rect.x0 or rect.y1 < rect.y0:
                        findings.append(
                            Finding(page_number, "abnormal-geometry", "invalid text bounding box", tuple(rect))
                        )
                        continue

                    if in_body_vertical_band(rect, height):
                        meaningful_body_objects += 1

                    if (
                        rect.x0 < -PHYSICAL_TOLERANCE
                        or rect.y0 < -PHYSICAL_TOLERANCE
                        or rect.x1 > width + PHYSICAL_TOLERANCE
                        or rect.y1 > height + PHYSICAL_TOLERANCE
                    ):
                        findings.append(
                            Finding(page_number, "text-page-overflow", "text extends outside the physical page", tuple(rect))
                        )
                        continue

                    if not in_body_vertical_band(rect, height):
                        continue

                    horizontal_overflow = (
                        rect.x0 < printable_left - GEOMETRY_TOLERANCE
                        or rect.x1 > printable_right + GEOMETRY_TOLERANCE
                    )
                    vertical_overflow = (
                        rect.y0 < printable_top - GEOMETRY_TOLERANCE
                        or rect.y1 > printable_bottom + GEOMETRY_TOLERANCE
                    )
                    if horizontal_overflow or vertical_overflow:
                        kind = classify_text(span.get("font", ""), value)
                        findings.append(
                            Finding(
                                page_number,
                                kind,
                                f"text exceeds printable body boundary; printable="
                                f"({printable_left:.1f}, {printable_top:.1f}, {printable_right:.1f}, {printable_bottom:.1f})pt; "
                                f"text={value[:80]!r}",
                                tuple(rect),
                            )
                        )

                    if rect.x1 >= width - PHYSICAL_TOLERANCE and value[-1:].isalnum():
                        findings.append(
                            Finding(page_number, "suspected-clipping", "text terminates at the physical page edge", tuple(rect))
                        )

        for drawing in page.get_drawings():
            rect = pymupdf.Rect(drawing["rect"])
            if not is_finite_rect(rect):
                findings.append(Finding(page_number, "abnormal-geometry", "invalid drawing bounding box", tuple(rect)))
                continue
            if in_body_vertical_band(rect, height):
                meaningful_body_objects += 1
                is_wide_rule = rect.width >= width * WIDE_RULE_FRACTION
                exceeds_printable = (
                    rect.x0 < printable_left - GEOMETRY_TOLERANCE
                    or rect.x1 > printable_right + GEOMETRY_TOLERANCE
                )
                if is_wide_rule and exceeds_printable:
                    findings.append(
                        Finding(
                            page_number,
                            "table-or-rule-overflow",
                            f"wide table/rule geometry exceeds printable width; "
                            f"printable_left={printable_left:.1f}pt, printable_right={printable_right:.1f}pt",
                            tuple(rect),
                        )
                    )

        if meaningful_body_objects == 0:
            findings.append(
                Finding(page_number, "blank-page", "page has no body text, images, or drawings; headers/footers are ignored")
            )

    document.close()
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "pdf",
        nargs="?",
        type=Path,
        default=Path("build/windows-engineering-development-handbook-print-preview.pdf"),
    )
    args = parser.parse_args()

    if not args.pdf.is_file():
        print(f"PRINT ERROR: PDF does not exist: {args.pdf}", file=sys.stderr)
        return 2

    findings = validate_pdf(args.pdf)
    if findings:
        for finding in findings:
            print(finding.render(), file=sys.stderr)
        print(f"Print validation failed: {len(findings)} blocking problem(s).", file=sys.stderr)
        return 1

    with pymupdf.open(args.pdf) as document:
        print(f"Print validation passed: {document.page_count} pages, 6x9 inch geometry.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
