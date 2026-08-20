# Windows Engineering & Development Handbook

An opinionated, documentation-as-code handbook for building a reproducible Windows engineering workstation with WSL2, Docker, modern development toolchains, IDEs, Git, and AI-assisted workflows.

> **Status:** Draft toward v1.0. The current published structure is v0.2; the target architecture is described in [BOOK_CONTEXT.md](BOOK_CONTEXT.md) and [ROADMAP.md](ROADMAP.md).

## Vision

The handbook treats Windows as the host platform, WSL2 as the primary engineering environment, Docker as the runtime boundary for infrastructure and services, and `mise` as the preferred manager for project toolchains. Markdown is the source of truth; generated DOCX, PDF, HTML, and EPUB files are build artifacts.

The goal is not a collection of installation notes. It is a maintainable engineering system that explains decisions, provides reproducible procedures, and verifies outcomes.

## Core principles

- **WSL-first:** run development shells, Git, language tools, and project automation inside WSL unless a Windows-native tool is required.
- **Clear ownership:** Windows owns desktop integration; WSL owns development; Docker owns infrastructure; `mise` owns user- and project-level toolchain versions.
- **Documentation as code:** review documentation through branches and pull requests, and validate it automatically.
- **Markdown as source of truth:** edit Markdown, never generated exports.
- **Reproducibility:** every setup procedure includes verification and avoids undocumented machine state.
- **Progressive complexity:** begin with a working baseline, then add optimization, security, and alternatives.

## Target book architecture

```text
book/
├── 00-front-matter/
├── part-01-operating-system/
├── part-02-ide-tools/
├── part-03-development-toolchains/
│   ├── toolchain ownership
│   ├── mise/
│   │   ├── concepts
│   │   ├── installation and shell activation
│   │   ├── configuration and precedence
│   │   ├── trust and security
│   │   ├── environment management
│   │   ├── tasks
│   │   ├── team and CI use
│   │   └── troubleshooting and recovery
│   ├── runtime recipes/
│   └── CLI recipes/
├── part-04-technology-profiles/
├── part-05-engineering-practices/
├── part-06-infrastructure/
├── part-07-new-machine-checklist/
└── appendices/
```

Part III is **Development Toolchains**. Technology Profiles, Engineering Practices, Infrastructure, and New Machine Checklist occupy Parts IV–VII. The definitive navigation remains `SUMMARY.md` in the repository.

## Repository layout

```text
book/          Canonical book chapters
assets/        Source images and diagrams
templates/     Reusable, non-secret examples
scripts/       Build and validation automation
archive/       Historical material, not canonical content
SUMMARY.md     Ordered book map
README.md      Project landing page
```

## Responsibility map

| Concern | Primary owner | Examples |
|---|---|---|
| Desktop applications and OS integration | Windows | Windows Terminal, Docker Desktop, browsers |
| Development shell and repository files | WSL2 | Git, SSH, shell automation, source trees |
| Language runtimes and developer CLIs | `mise` in WSL | Node.js, Python, PHP, Terraform, task runners |
| Databases, caches, proxies, app services | Docker | MariaDB, Redis, NGINX |
| Project history and collaboration | Git/GitHub | branches, commits, reviews, releases |

Do not install the same tool in several layers without documenting which executable is authoritative.

## Reading the handbook

Start with the front matter and Part I. Read Part II for editor integration, Part III for toolchain management, and then select the relevant technology profile. Engineering Practices and Infrastructure are cross-cutting reference sections. Use the final checklist to provision or audit a workstation.

## Contributing

Before editing, read [CONTRIBUTING.md](CONTRIBUTING.md), [STYLE_GUIDE.md](STYLE_GUIDE.md), and [BOOK_CONTEXT.md](BOOK_CONTEXT.md). AI coding agents must also follow [AGENTS.md](AGENTS.md).

Typical workflow:

1. Create a focused branch from an up-to-date `main`.
2. Edit Markdown source files and `SUMMARY.md` together.
3. Run Markdown, link, structure, and build checks.
4. Review the rendered diff and generated preview.
5. Open a pull request with scope, validation evidence, and migration notes.

The detailed repository migration sequence is in [REFACTORING_PLAN_V1.md](REFACTORING_PLAN_V1.md).

## Build outputs

The canonical Markdown may be exported to DOCX, PDF, HTML, or EPUB. Generated files must be reproducible and must not become an alternate editable source. The repository currently includes a DOCX build script; v1.0 adds documented and automated validation for all supported targets.

## Release goal

v1.0 is reached when the target structure is complete, navigation and links validate, critical procedures have been tested in a clean WSL environment, tool ownership is unambiguous, supported exports build reproducibly, and the release criteria in [ROADMAP.md](ROADMAP.md) are satisfied.

## License and support

Retain the repository's existing licensing decision. Use GitHub issues for errors, proposals, and reproducibility reports; never publish credentials, private hostnames, or personal configuration values.
