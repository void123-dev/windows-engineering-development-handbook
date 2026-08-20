# Book Context

## Purpose

This document records the durable product and architecture decisions for the Windows Engineering & Development Handbook. It explains *why* the book is organized as it is. `SUMMARY.md` defines navigation, `STYLE_GUIDE.md` defines writing rules, and `CONTRIBUTING.md` defines collaboration.

## Audience

- Developers building a professional Windows workstation.
- Platform and DevOps engineers who need reproducible local environments.
- Technical leads standardizing team setup and troubleshooting.
- Experienced users migrating from ad hoc Windows/WSL installations.

Readers are assumed to understand basic terminals and Git, but not the handbook's preferred architecture.

## Problem statement

Windows development guidance often mixes host, WSL, containers, language managers, and IDE integration without declaring boundaries. That produces duplicate installations, path conflicts, permission problems, unreproducible machines, and instructions that age quickly. The handbook must provide both a working path and a decision model.

## Platform model

### Windows host

Windows provides hardware access, desktop applications, corporate controls, Windows Terminal, browser tooling, and Docker Desktop integration. Windows-native installation is appropriate only where host integration or a native GUI is the reason for the tool.

### WSL2 engineering environment

WSL2 is the default location for repositories, shells, Git, SSH, build commands, and automation. Projects should normally live in the Linux filesystem rather than under `/mnt/c` when Linux tooling performance and permissions matter.

### Docker service boundary

Docker runs infrastructure and application services that benefit from isolation, parity, networks, volumes, and disposable state: databases, caches, queues, proxies, and full application stacks. Docker is not the default way to provide every interactive developer CLI.

### `mise` toolchain boundary

`mise` manages developer-facing runtime and CLI versions inside WSL. It provides consistent global defaults, project-local versions, environment activation, and tasks. Projects pin versions in committed configuration; personal overrides remain uncommitted.

### Decision rule

Use this order:

1. Does the tool require Windows UI or host integration? Use Windows.
2. Is it a persistent or networked service? Prefer Docker.
3. Is it an interactive runtime or project CLI? Prefer `mise` in WSL.
4. Is it an OS-level Linux dependency? Use the WSL distribution package manager.
5. If more than one layer is required, document precedence and verification.

## Target information architecture

| Part | Target responsibility |
|---|---|
| Front matter | Scope, principles, conventions, navigation |
| I — Operating System & Development Environment | Windows, WSL2, Docker Desktop, AI environment, project layout |
| II — IDE & Development Tools | PhpStorm, VS Code, quality UI, remote development |
| III — Development Toolchains | Toolchain ownership, `mise`, runtime recipes, CLI recipes, tasks, environment files |
| IV — Technology Profiles | WordPress, Laravel, Docker-first and remote profiles |
| V — Engineering Practices | Git, dependencies, quality, AI, performance, security |
| VI — Infrastructure | NGINX, Redis, MariaDB, Cloudflare, deployment platforms |
| VII — New Machine Checklist | End-to-end provisioning and verification |
| Appendices | Software lists, templates, reference configs, commands |

## `mise` content hierarchy

Part III should teach `mise` progressively rather than placing all material in one oversized chapter:

1. **Role and mental model:** ownership boundaries and comparison with Docker, OS packages, and single-language managers.
2. **Installation in WSL:** prerequisites, shell activation, upgrade, removal, and verification.
3. **Configuration hierarchy:** global, project, local, environment-specific, and trusted configuration; precedence must be explicit.
4. **Tool recipes:** supported runtimes and CLIs, version pinning, shims/path behavior, and per-tool caveats.
5. **Environment management:** non-secret variables, secret boundaries, `.env` policy, and directory activation.
6. **Tasks:** repeatable project commands, composition, dependencies, and discoverability.
7. **Team and CI use:** lock/pin policy, onboarding, caching, deterministic checks, and graceful fallback.
8. **Security and troubleshooting:** configuration trust, plugin/backend provenance, checksums, path diagnosis, and recovery.

Specific command syntax must be verified against current official documentation during implementation.

## Documentation architecture

- Markdown files under `book/` are canonical.
- `SUMMARY.md` is the only ordered navigation source.
- Root governance files describe the project, not book chapters.
- Images and diagrams live in `assets/` and use relative links.
- Reusable examples live in `templates/`; they contain placeholders, never secrets.
- Generated documents are outputs. Do not hand-edit them or use them to overwrite Markdown.
- `archive/` is historical and excluded from navigation, lint scope where appropriate, and canonical search results.

## Chapter contract

A mature procedural chapter should contain, where relevant: purpose, prerequisites, ownership decision, installation, configuration, verification, operational workflow, security notes, troubleshooting, alternatives/trade-offs, and authoritative references. A conceptual chapter may omit installation but must still provide outcomes and cross-links.

## Versioning and compatibility

- Pin commands and screenshots to named versions when behavior is version-sensitive.
- State the tested Windows, WSL distribution, Docker, and tool versions.
- Prefer version-neutral concepts; isolate volatile commands in focused sections.
- Mark content as tested, partially tested, or conceptual when confidence differs.
- Breaking information-architecture changes require redirects or an explicit link-migration table.

## Security model

Examples use placeholders and least privilege. Secrets, tokens, private domains, personal paths, and real IP addresses must not enter the repository. Download instructions should prefer authenticated package sources, signatures, or checksums. AI-generated commands are treated as untrusted until reviewed and tested.

## Non-goals for v1.0

- Supporting every Windows edition, Linux distribution, IDE, or runtime manager.
- Replacing upstream product documentation.
- Treating Docker and `mise` as interchangeable.
- Maintaining parallel canonical DOCX/PDF copies.
- Guaranteeing identical performance across hardware and corporate environments.

## Decision governance

Durable architecture decisions belong here. A change that affects part numbering, ownership boundaries, canonical sources, or supported environments must update this file, `SUMMARY.md`, the roadmap, and relevant migration notes in the same pull request.
