# Contributing

Thank you for improving the Windows Engineering & Development Handbook. Contributions should make the book more correct, reproducible, navigable, and maintainable.

## Before you start

Read:

- [BOOK_CONTEXT.md](BOOK_CONTEXT.md) for scope and architecture;
- [STYLE_GUIDE.md](STYLE_GUIDE.md) for prose and Markdown rules;
- [ROADMAP.md](ROADMAP.md) for release priorities;
- [REFACTORING_PLAN_V1.md](REFACTORING_PLAN_V1.md) for structural migration work.

For large structure changes, open or reference an issue describing the problem, proposed move map, link impact, and acceptance criteria.

## Development environment

Use Git and repository automation inside WSL2. Keep the clone in the Linux filesystem when possible. Use Docker for required service dependencies and `mise` for supported developer toolchains. Do not require contributors to install the same runtime through multiple managers.

## Branches

Create a branch from an up-to-date `main`. Suggested names:

- `docs/<short-topic>` for chapter work;
- `fix/<short-topic>` for corrections;
- `refactor/v1-information-architecture` for the coordinated v1 migration;
- `build/<short-topic>` for validation and export automation.

Do not commit directly to `main`.

## Change workflow

1. Confirm a clean working tree and update local `main` without rewriting shared history.
2. Create a focused branch.
3. Read the affected chapters and search for inbound links and terminology.
4. Make a small coherent change.
5. Update `SUMMARY.md` and cross-links when paths or titles change.
6. Run validation and inspect the rendered Markdown/export.
7. Review the full diff for accidental reformatting or private data.
8. Commit with a scoped message and open a pull request.

## Chapter standard

A procedural chapter should usually cover outcome, prerequisites, architecture/ownership, installation, configuration, verification, daily use, security, troubleshooting, alternatives, and primary references. Omit irrelevant sections rather than filling them with boilerplate.

Every procedure must identify whether commands run in Windows PowerShell, WSL, or a container. Verification must check the result, not merely repeat the installation command.

## Structural changes

- Prepare an old-path → new-path move map.
- Preserve history with tracked moves.
- Separate mechanical moves from substantial rewrites when feasible.
- Update navigation, links, scripts, workflows, and references atomically.
- Search case-sensitively for old paths after the move.
- Document any public-link breakage and migration strategy.
- Do not delete old content until equivalence, references, and history have been reviewed.

## Commits

Use concise imperative subjects with an optional Conventional Commits-style scope:

```text
docs(mise): explain project configuration precedence
docs(structure): move infrastructure to part VI
fix(links): repair references after part renumbering
build(markdown): add internal link validation
```

Each commit should be understandable and reversible. Avoid mixing generated artifacts, content moves, prose rewrites, and unrelated cleanup.

## Pull requests

Include:

- purpose and scope;
- affected chapters and old/new paths;
- architecture decisions or trade-offs;
- validation commands and results;
- preview or screenshots when layout changes;
- known limitations and follow-up work;
- rollback notes for structural changes.

Reviewers should be able to distinguish moves from changed prose. Use GitHub's rendered Markdown view as well as the source diff.

## Required checks

Before requesting review:

- run Markdown linting;
- validate internal links, anchors, and image paths;
- check `SUMMARY.md` paths, duplicates, and orphaned chapters;
- scan for secrets and personal data;
- run `git diff --check`;
- build every supported output or state exactly why a build was not run;
- test changed commands in the declared environment where safe and practical.

Repository automation is the authority for exact command names once those workflows are added.

## Source and licensing policy

Prefer official documentation and primary sources. Paraphrase in the handbook's voice, cite the source, and respect its license. Do not paste copyrighted tutorials, unlicensed diagrams, or AI-generated content that has not been reviewed for accuracy and provenance.

## Security and privacy

Never commit passwords, tokens, private keys, cookies, private domains, corporate configuration, personal addresses, or identifying screenshots. Use obvious placeholders. If a secret is exposed, stop, revoke it, and follow repository security procedures; deleting the latest line is not sufficient remediation.

## Definition of done

A contribution is done when its requested outcome is present, style and architecture rules are met, navigation and links work, tests/builds are recorded, no unrelated changes remain, and reviewers have enough evidence to reproduce the result.
