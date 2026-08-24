#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="$ROOT_DIR/build"
DOCX_FILE="$OUTPUT_DIR/windows-engineering-development-handbook-print-preview.docx"
PDF_FILE="$OUTPUT_DIR/windows-engineering-development-handbook-print-preview.pdf"

if command -v libreoffice >/dev/null 2>&1; then
  LIBREOFFICE_BIN="$(command -v libreoffice)"
elif command -v soffice >/dev/null 2>&1; then
  LIBREOFFICE_BIN="$(command -v soffice)"
else
  echo "Error: LibreOffice (libreoffice or soffice) is required to build the PDF preview." >&2
  exit 1
fi

"$ROOT_DIR/scripts/build-docx.sh"

PROFILE_DIR="$(mktemp -d)"
trap 'rm -rf "$PROFILE_DIR"' EXIT

"$LIBREOFFICE_BIN" \
  --headless \
  "-env:UserInstallation=file://$PROFILE_DIR" \
  --convert-to pdf \
  --outdir "$OUTPUT_DIR" \
  "$DOCX_FILE"

if [[ ! -f "$PDF_FILE" ]]; then
  echo "Error: LibreOffice did not create the expected PDF: $PDF_FILE" >&2
  exit 1
fi

python3 "$ROOT_DIR/scripts/validate-print.py" "$PDF_FILE"

echo "Created: $PDF_FILE"
