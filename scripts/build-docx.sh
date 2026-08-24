#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="$ROOT_DIR/build"
OUTPUT_FILE="$OUTPUT_DIR/windows-engineering-development-handbook-print-preview.docx"
REFERENCE_DOC="$ROOT_DIR/templates/reference.docx"
TABLE_FILTER="$ROOT_DIR/scripts/print-tables.lua"

if ! command -v pandoc >/dev/null 2>&1; then
  echo "Error: pandoc is required to build the DOCX preview." >&2
  exit 1
fi

if [[ ! -f "$REFERENCE_DOC" ]]; then
  echo "Error: missing reference document: $REFERENCE_DOC" >&2
  exit 1
fi

if [[ ! -f "$TABLE_FILTER" ]]; then
  echo "Error: missing print table filter: $TABLE_FILTER" >&2
  exit 1
fi

mkdir -p "$OUTPUT_DIR"

# --print-chapters only emits paths after the complete documentation validation
# succeeds, so a failed validation stops the build before Pandoc runs.
CHAPTER_LIST="$(python3 "$ROOT_DIR/scripts/validate-docs.py" --print-chapters)"
mapfile -t CHAPTER_PATHS <<< "$CHAPTER_LIST"

CHAPTERS=()
for chapter in "${CHAPTER_PATHS[@]}"; do
  CHAPTERS+=("$ROOT_DIR/$chapter")
done

pandoc "$ROOT_DIR/README.md" "${CHAPTERS[@]}" \
  --from=gfm \
  --toc \
  --reference-doc="$REFERENCE_DOC" \
  --lua-filter="$TABLE_FILTER" \
  --output="$OUTPUT_FILE"

echo "Created: $OUTPUT_FILE"
