# Print QA

The print-preview pipeline runs two independent validation layers:

```text
validate-docs.py -> Pandoc -> DOCX -> LibreOffice -> PDF -> validate-print.py
```

`scripts/validate-docs.py` checks Markdown and repository structure. It does not
inspect pagination or rendered geometry. `scripts/validate-print.py` opens the
generated PDF with PyMuPDF and fails the build when it finds a blocking,
machine-detectable print-layout problem.

## Automated checks

The PDF validator checks:

- that the PDF opens and contains pages;
- that every page is 6x9 inches, with a small renderer tolerance;
- text and image bounding boxes outside the physical page;
- body text extending into the configured printable margins;
- monospaced code and long URL/token overflow;
- wide table/rule geometry extending beyond the printable width;
- text ending at the physical edge, which is a clipping signal;
- invalid or non-finite content geometry;
- pages with no body text, images, or drawings.

Header and footer bands are excluded from printable-body margin checks so page
numbers and future running headers do not produce false positives. Small
geometric tolerances account for glyph bearings and PDF renderer rounding.

Install the print-validation dependency and run the complete pipeline with:

```bash
python3 -m pip install -r requirements-print.txt
./scripts/build-pdf.sh
```

The validator can also be run independently:

```bash
python3 scripts/validate-print.py \
  build/windows-engineering-development-handbook-print-preview.pdf
```

Exit code `0` means validation passed. A non-zero exit code means the PDF is
missing, malformed, or contains at least one blocking geometry problem.

## Limits of automated validation

PDF geometry cannot reliably determine whether a layout is pleasant or easy to
read. Table recognition is heuristic when tables have few or no visible borders.
Font substitution can also change wrapping between environments even when all
bounding boxes remain valid. Passing automation is therefore necessary but not
sufficient for a release.

## Manual and physical proof checklist

- [ ] Tables are readable at normal print distance.
- [ ] Code remains readable and does not wrap in misleading places.
- [ ] Headings are not orphaned at the bottom of a page.
- [ ] Paragraph widows and orphans are acceptable.
- [ ] Page and chapter breaks are intentional and comfortable.
- [ ] Pages do not contain distracting or excessive whitespace.
- [ ] Heading, body, code, note, and table hierarchy is visually clear.
- [ ] Tables do not split awkwardly across pages or repeat partial rows.
- [ ] Images are sharp, correctly scaled, and have sufficient print resolution.
- [ ] Captions stay with their images or tables.
- [ ] Links, inline code, and long commands remain legible.
- [ ] Headers, footers, and page numbers are consistent and inside trim safety.
- [ ] Gutter and outside margins feel balanced in a bound physical proof.
- [ ] Body and code sizes are comfortable during sustained physical reading.
- [ ] No content is lost near trim, binding, or printer non-printable areas.
