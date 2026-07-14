# Windows Engineering & Development Handbook

A documentation-as-code handbook for building and maintaining a modern Windows engineering workstation with WSL2, Docker, IDE tooling, AI-assisted development, and web infrastructure.

## Status

Draft edition: **0.2**

## Repository layout

```text
book/        Main book sources, split by part and chapter
assets/      Images and diagrams
templates/   Reusable configuration templates
scripts/     Build and validation scripts
archive/     Original source drafts
```

## Editing workflow

1. Create a branch for a chapter or topic.
2. Edit Markdown files under `book/`.
3. Keep one chapter per file.
4. Open a pull request for review.
5. Merge only after links, headings, and code blocks are checked.

## Build targets

The Markdown sources are intended to be exportable with Pandoc to DOCX, PDF, HTML, or EPUB.

```bash
./scripts/build-docx.sh
```

## Book map

See [SUMMARY.md](SUMMARY.md).
