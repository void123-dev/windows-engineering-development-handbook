#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="$ROOT_DIR/build"
mkdir -p "$OUTPUT_DIR"

CHAPTER_LIST="$(python3 "$ROOT_DIR/scripts/validate-docs.py" --print-chapters)"
mapfile -t CHAPTER_PATHS <<< "$CHAPTER_LIST"

CHAPTERS=()
for chapter in "${CHAPTER_PATHS[@]}"; do
  CHAPTERS+=("$ROOT_DIR/$chapter")
done

pandoc "$ROOT_DIR/README.md" "${CHAPTERS[@]}" \
  --from=gfm \
  --toc \
  --output="$OUTPUT_DIR/windows-engineering-development-handbook.docx"

echo "Created: $OUTPUT_DIR/windows-engineering-development-handbook.docx"
