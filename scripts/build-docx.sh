#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="$ROOT_DIR/build"
mkdir -p "$OUTPUT_DIR"

mapfile -t CHAPTERS < <(find "$ROOT_DIR/book" -type f -name '*.md' | sort)
pandoc "$ROOT_DIR/README.md" "${CHAPTERS[@]}" \
  --from=gfm \
  --toc \
  --output="$OUTPUT_DIR/windows-engineering-development-handbook.docx"

echo "Created: $OUTPUT_DIR/windows-engineering-development-handbook.docx"
