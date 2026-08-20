#!/usr/bin/env python3
"""Validate handbook navigation, Markdown structure, links, and line endings."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
SUMMARY = ROOT / "SUMMARY.md"
BOOK = ROOT / "book"
LINK_PATTERN = re.compile(r"!?\[([^\]]*)\]\(([^)]+)\)")
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
EXTERNAL_SCHEMES = {"http", "https", "mailto"}


def repository_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def normalize_title(value: str) -> str:
    value = value.replace("`", "")
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def heading_anchors(text: str) -> set[str]:
    anchors: set[str] = set()
    counts: defaultdict[str, int] = defaultdict(int)
    for _, heading in HEADING_PATTERN.findall(text):
        heading = re.sub(r"[`*_~]", "", heading).lower()
        slug = re.sub(r"[^\w\- ]", "", heading, flags=re.UNICODE)
        slug = re.sub(r"\s+", "-", slug.strip())
        number = counts[slug]
        counts[slug] += 1
        anchors.add(slug if number == 0 else f"{slug}-{number}")
    return anchors


def summary_entries() -> list[tuple[str, str]]:
    text = SUMMARY.read_text(encoding="utf-8")
    return [
        (label, target.split("#", 1)[0])
        for label, target in LINK_PATTERN.findall(text)
        if target.startswith("book/") and target.split("#", 1)[0].endswith(".md")
    ]


def active_markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts and "archive" not in path.parts
    )


def controlled_text_files() -> list[Path]:
    suffixes = {".md", ".py", ".sh", ".yaml", ".yml"}
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and "archive" not in path.parts
        and "build" not in path.parts
        and (path.suffix.lower() in suffixes or path.name == ".gitattributes")
    )


def validate() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    notices: list[str] = []
    entries = summary_entries()
    targets = [target for _, target in entries]
    chapters = sorted(repository_path(path) for path in BOOK.rglob("*.md"))

    for target in sorted(set(targets)):
        if targets.count(target) > 1:
            errors.append(f"SUMMARY.md contains duplicate path: {target}")
        if not (ROOT / target).is_file():
            errors.append(f"SUMMARY.md target does not exist: {target}")

    for chapter in sorted(set(chapters) - set(targets)):
        errors.append(f"Active chapter is missing from SUMMARY.md: {chapter}")

    for target in sorted(set(targets) - set(chapters)):
        errors.append(f"SUMMARY.md path is not an active chapter: {target}")

    hashes: defaultdict[str, list[str]] = defaultdict(list)
    for chapter in chapters:
        path = ROOT / chapter
        hashes[hashlib.sha256(path.read_bytes()).hexdigest()].append(chapter)
    for duplicates in hashes.values():
        if len(duplicates) > 1:
            errors.append(f"Duplicate chapter content: {', '.join(duplicates)}")

    for label, target in entries:
        path = ROOT / target
        if not path.is_file():
            continue
        headings = HEADING_PATTERN.findall(path.read_text(encoding="utf-8"))
        h1 = [title for marks, title in headings if len(marks) == 1]
        if len(h1) == 1 and normalize_title(label) != normalize_title(h1[0]):
            errors.append(
                f"Navigation title differs from H1: {target}: {label!r} != {h1[0]!r}"
            )

    for path in controlled_text_files():
        relative = repository_path(path)
        data = path.read_bytes()
        if b"\r" in data:
            errors.append(f"Non-LF line ending: {relative}")
        if data and not data.endswith(b"\n"):
            errors.append(f"Missing final newline: {relative}")

    for path in active_markdown_files():
        relative = repository_path(path)
        data = path.read_bytes()

        text = data.decode("utf-8")
        h1 = [title for marks, title in HEADING_PATTERN.findall(text) if len(marks) == 1]
        if len(h1) != 1:
            errors.append(f"Expected exactly one H1 in {relative}; found {len(h1)}")

        fence_open = False
        for line_number, line in enumerate(text.splitlines(), start=1):
            if line.startswith("```"):
                marker = line[3:].strip()
                if not fence_open and not marker:
                    errors.append(f"Unlabelled code fence: {relative}:{line_number}")
                fence_open = not fence_open
        if fence_open:
            errors.append(f"Unclosed code fence: {relative}")

        for _, raw_target in LINK_PATTERN.findall(text):
            target = raw_target.strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme.lower() in EXTERNAL_SCHEMES:
                continue
            if parsed.scheme:
                continue

            destination = path if not parsed.path else (path.parent / unquote(parsed.path)).resolve()
            if not destination.exists():
                errors.append(f"Broken internal link: {relative} -> {target}")
                continue
            if parsed.fragment and destination.is_file() and destination.suffix.lower() == ".md":
                fragment = unquote(parsed.fragment).lower()
                anchors = heading_anchors(destination.read_text(encoding="utf-8"))
                if fragment not in anchors:
                    errors.append(f"Broken Markdown anchor: {relative} -> {target}")

    notices.append(
        f"Validated {len(chapters)} chapters and {len(targets)} SUMMARY.md entries."
    )
    return errors, notices


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--print-chapters",
        action="store_true",
        help="print chapter paths in SUMMARY.md order after successful validation",
    )
    args = parser.parse_args()

    errors, notices = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    if args.print_chapters:
        for _, target in summary_entries():
            print(target)
    else:
        for notice in notices:
            print(notice)
        print("Documentation validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
