# Roadmap to v1.0

## Current baseline

The repository content originated in Draft v0.2. The v1 structural branch now represents Parts I–VII: Part III is Development Toolchains, followed by Technology Profiles, Engineering Practices, Infrastructure, and the New Machine Checklist. Content completion and release validation remain in progress.

## Release principles

- Preserve usable content while changing its organization.
- Land small reviewable stages with a validated book map at each stage.
- Stabilize architecture before broad prose expansion.
- Automate checks before declaring content complete.
- Treat v1.0 as a reproducible handbook release, not merely a renumbering exercise.

## v0.3 — Governance and baseline

- Add `AGENTS.md`, `BOOK_CONTEXT.md`, and `STYLE_GUIDE.md`.
- Expand `README.md`, `CONTRIBUTING.md`, and this roadmap.
- Record repository inventory, broken-link baseline, build behavior, and supported environments.
- Define chapter template, terminology, canonical-source policy, and generated-artifact policy.
- Decide and document Markdown lint, link check, secret scan, and export tools.

**Exit:** governance documents agree; existing content is inventoried; baseline validation is reproducible.

## v0.4 — Information architecture migration

- Maintain Part III Development Toolchains and its nested `mise` Usage section.
- Keep Technology Profiles in Part IV.
- Keep Engineering Practices in Part V.
- Keep Infrastructure in Part VI.
- Keep New Machine Checklist in Part VII.
- Validate `SUMMARY.md`, paths, headings, cross-links, scripts, and build inputs after each structural batch.
- Publish a final old-path → new-path map in the migration pull request.

**Exit:** every canonical chapter appears once in `SUMMARY.md`; no old internal paths remain; history and content are preserved.

## v0.5 — `mise` foundation

- Explain the Windows/WSL/Docker/`mise` ownership model.
- Add WSL installation, shell activation, upgrade, removal, and verification.
- Document configuration hierarchy and trust behavior.
- Define global defaults, committed project pins, and ignored personal overrides.
- Add a Docker-versus-`mise` decision matrix.

**Exit:** a new contributor can install `mise`, activate it, pin a project runtime, and verify executable ownership without ambiguity.

## v0.6 — Toolchain recipes and tasks

- Add reviewed recipes for the handbook's supported languages and CLIs.
- Add environment-variable and secret-boundary guidance.
- Add repeatable `mise` tasks for validation/build workflows where appropriate.
- Document team onboarding and CI usage.
- Add troubleshooting for PATH, shims, trust, backends, network failures, and mixed Windows/WSL installations.

**Exit:** representative projects reproduce pinned toolchains in a clean WSL instance and CI.

## v0.7 — Technology profiles

- Reconcile WordPress, Laravel, Docker-first, and remote-development profiles with the new toolchain model.
- Remove duplicated generic Git, Composer, Docker, and IDE instructions from profiles; replace with cross-links.
- Add profile-specific prerequisites, verification, and troubleshooting.
- Clarify when project services are containerized and when CLIs run through `mise`.

**Exit:** profiles are executable end-to-end and contain no conflicting ownership guidance.

## v0.8 — Engineering practices and infrastructure

- Normalize Git, dependency management, quality, AI-assisted development, performance, and security chapters.
- Normalize NGINX, Redis, MariaDB, Cloudflare, and deployment guidance.
- Add least-privilege, secret, backup, restore, observability, and data-safety guidance where relevant.
- Verify commands against supported versions and primary documentation.

**Exit:** critical procedures are tested and include verification, failure modes, and safe rollback.

## v0.9 — Release candidate

- Complete the new-machine provisioning checklist against the target architecture.
- Resolve all critical link, lint, secret, structure, and build failures.
- Build and visually review supported DOCX/PDF/HTML/EPUB outputs.
- Audit terminology, duplication, accessibility, licensing, and source attribution.
- Test the documented path in a clean or disposable Windows/WSL environment.
- Freeze the information architecture except for release-blocking fixes.

**Exit:** a release-candidate pull request satisfies every automated check and has a documented manual QA report.

## v1.0 — Stable handbook

v1.0 is ready when:

- all target parts and required chapters are present and navigable;
- Markdown is explicitly canonical and exports are reproducible;
- every `SUMMARY.md` entry resolves and no unintended canonical chapter is orphaned;
- internal links, anchors, images, and required external references validate;
- Part III fully implements the agreed `mise` hierarchy;
- WSL-first, Docker service, and `mise` toolchain boundaries are consistent across the book;
- critical setup procedures have been tested in a clean supported environment;
- supported outputs build without release-blocking errors;
- no known secrets, private data, broken critical commands, or unresolved high-severity technical errors remain;
- licensing and attribution are documented;
- the final pull request includes migration map, validation evidence, known limitations, and release notes;
- a `v1.0.0` tag/release is created only after the reviewed release commit is merged.

## After v1.0

- Establish a regular dependency/link review cadence.
- Track version-sensitive procedures by supported release.
- Add new technology profiles only when ownership boundaries and maintenance capacity are clear.
- Improve automated executable-example testing and artifact publishing.
