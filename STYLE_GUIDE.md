# Style Guide

## Language and voice

- Write in clear technical English unless the repository explicitly adopts another primary language.
- Use an engineering, direct, and calm voice. Explain the reason before long procedures.
- Address the reader as “you” sparingly; prefer imperative steps.
- Distinguish facts, recommendations, alternatives, and personal preferences.
- Avoid marketing claims, unexplained absolutes, and time-relative words such as “currently” without a date or version.

## Markdown rules

- Use GitHub Flavored Markdown and UTF-8.
- Use exactly one H1 per file; begin subsections at H2 and do not skip heading levels.
- Leave blank lines around headings, lists, tables, block quotes, and fenced code blocks.
- Use `-` for unordered lists and `1.` for ordered steps.
- Give fenced code blocks an accurate language identifier (`bash`, `powershell`, `yaml`, `json`, `text`).
- Keep code, commands, paths, filenames, environment variables, and tool names such as `mise` in backticks.
- Use relative repository links. Do not use branch-specific GitHub blob URLs for internal content.
- Use descriptive link text; avoid “click here.”
- Prefer Markdown constructs over embedded HTML.
- Do not add a hand-written table of contents to every chapter; navigation belongs in `SUMMARY.md`.

## File and heading naming

- Book directories use `part-NN-topic`; chapters use `NN-kebab-case.md`.
- Numbering represents reading order, not version.
- Use sentence case for headings.
- Use canonical product spelling: Windows, WSL2, Docker, Docker Desktop, GitHub, PhpStorm, VS Code, NGINX, MariaDB, Redis, and `mise`.
- Avoid renaming published paths casually. Record every rename in the migration map.

## Commands and platform context

Every command block must make its execution context obvious in nearby text:

- **PowerShell on Windows** for host administration.
- **Shell inside WSL** for repository and developer-tool commands.
- **Container shell** only for commands intentionally executed inside a container.

Do not mix prompts into copyable commands. Prefer one safe operation per line. Explain elevated privileges, destructive behavior, network downloads, and persistent changes before the command.

For multi-step procedures, provide:

1. prerequisites;
2. the command or action;
3. expected result;
4. an independent verification command;
5. rollback or recovery guidance when the change is risky.

## Examples and configuration

- Examples must be minimal, syntactically valid, and internally consistent.
- Use placeholders such as `<project-name>` and explain them once.
- Never include real secrets, tokens, emails, private domains, or machine-specific absolute paths.
- Prefer complete short config examples over unexplained fragments.
- State whether a file is committed, generated, ignored, global, project-local, or personal.
- Pin versions where reproducibility requires it; explain deliberate floating versions.

## Links and sources

- Prefer official product documentation, specifications, and primary sources.
- Link to the most stable versioned page available.
- Put references near the claim they support or in a focused “References” section.
- Do not copy long passages from external sources.
- Before merge, validate internal links, image paths, anchors, and external URLs.
- When moving a chapter, update inbound links across the repository and check external/public link impact.

## Images, diagrams, and accessibility

- Store source assets under `assets/` with descriptive kebab-case names.
- Use meaningful alt text that communicates the image's purpose.
- Do not rely on color alone to communicate state.
- Prefer text or Mermaid for maintainable diagrams when rendering targets support it; otherwise retain an editable source beside the export.
- Crop screenshots to relevant UI, remove private information, and record product/version when the UI is volatile.

## Chapter quality template

Use only sections relevant to the topic:

```markdown
## Outcome
## Prerequisites
## Architecture and ownership
## Installation
## Configuration
## Verification
## Daily workflow
## Security considerations
## Troubleshooting
## Alternatives and trade-offs
## References
```

## Terminology

- **Host:** the Windows operating system.
- **WSL:** the Linux environment running under WSL2.
- **Toolchain:** developer-facing runtimes and CLIs used to build or maintain projects.
- **Service:** a networked or persistent runtime component, generally containerized.
- **Source of truth:** the canonical editable representation; for this project, Markdown.
- **Generated artifact:** reproducible output derived from canonical sources.

## Review checklist

- The title, filename, and `SUMMARY.md` entry agree.
- Platform and shell context are explicit.
- Commands are safe, copyable, and verified.
- Versions and assumptions are stated.
- Internal and external links work.
- Examples contain no secrets or personal data.
- The chapter avoids duplicate or conflicting ownership guidance.
- Claims are supported by primary references.
- Spelling, headings, code fences, and line endings pass automated checks.
