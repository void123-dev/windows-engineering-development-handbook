# Safe Refactoring Plan for v1.0

## Objective

Transform Draft v0.2 into the target v1.0 documentation architecture without losing content, history, navigability, or a usable `main` branch. The migration inserts Part III Development Toolchains, moves existing Parts III–VI to Parts IV–VII, and establishes `mise` as the WSL toolchain manager while Docker remains the service/infrastructure boundary.

## Safety constraints

- Do all implementation in a dedicated branch and pull request.
- Never overwrite root files without reviewing a three-way comparison: current file, proposed file, intended policy.
- Do not combine bulk moves with large prose rewrites.
- Do not delete historical or apparently duplicated content until references and semantic equivalence are verified.
- Keep Markdown canonical; generated documents are disposable build outputs.
- Create a recoverable checkpoint before every structural batch.

## Phase 0 — Prepare and protect

1. Confirm the correct remote and default branch.
2. Fetch remote state and verify the local working tree is clean. Preserve any user work before continuing.
3. Record the starting commit SHA and create an annotated local safety tag or a backup branch according to repository policy.
4. Create `refactor/v1-information-architecture` from the latest reviewed `main`.
5. Disable no checks and rewrite no shared history.
6. Open a tracking issue or draft pull request containing scope, exclusions, migration map, and acceptance criteria.

**Checkpoint:** the branch points to the recorded baseline and can be abandoned without affecting `main`.

## Phase 1 — Inventory the current repository

1. List every tracked Markdown file, image, template, script, workflow, and generated artifact.
2. Parse `SUMMARY.md` and confirm each target exists.
3. Identify canonical chapters missing from `SUMMARY.md`, duplicated entries, duplicate H1 headings, and case mismatches.
4. Search all Markdown and scripts for current part paths and titles.
5. Capture internal-link, image, anchor, external-link, Markdown-lint, secret-scan, and build results.
6. Record supported Windows, WSL distribution, Docker Desktop, Pandoc, and relevant tool versions.
7. Store the findings in the pull request or a temporary migration report; do not “fix while inventorying.”

**Checkpoint:** baseline failures are distinguished from migration regressions.

## Phase 2 — Establish governance

1. Compare the proposed root documents with current versions line by line.
2. Merge the intent of `README.md`, `CONTRIBUTING.md`, and `ROADMAP.md`; preserve accurate project-specific information.
3. Add `AGENTS.md`, `BOOK_CONTEXT.md`, and `STYLE_GUIDE.md`.
4. Add this refactoring plan for the migration lifetime; decide after v1.0 whether to retain or archive it.
5. Ensure the documents cross-link correctly and do not contradict `SUMMARY.md`.
6. Commit governance separately, for example: `docs(governance): define v1 handbook architecture`.

**Checkpoint:** maintainers and agents have one consistent set of rules before any moves.

## Phase 3 — Add validation before moving content

Introduce or document deterministic checks for:

- Markdown syntax/style;
- internal file links, anchors, and image paths;
- external links with an allowlist/retry policy for unreliable sites;
- `SUMMARY.md` missing paths, duplicates, and orphan chapters;
- one H1 per file and valid code-fence language identifiers;
- whitespace and line endings;
- secret/private-data patterns;
- supported document builds.

Run the checks locally in WSL and in GitHub Actions. Pin tool versions through the chosen toolchain configuration. If checks reveal legacy failures, either fix them in a dedicated commit or record a narrow, temporary baseline; do not create a blanket ignore.

**Checkpoint:** a known-good structural change can be distinguished automatically from a broken one.

## Phase 4 — Approve the move map

Start with this directory map and refine it after inventory:

| Current path | Target path |
|---|---|
| `book/part-03-technology-profiles/` | `book/part-04-technology-profiles/` |
| `book/part-04-engineering-practices/` | `book/part-05-engineering-practices/` |
| `book/part-05-infrastructure/` | `book/part-06-infrastructure/` |
| `book/part-06-new-machine-checklist/` | `book/part-07-new-machine-checklist/` |
| new | `book/part-03-development-toolchains/` |

Decide separately whether overlapping chapters such as Linux Development Toolchain, Composer, Docker, Quality Tools, and Remote Development stay, move, split, or become index chapters. Do not decide by filename alone; assign one clear responsibility and replace duplication with cross-links.

**Checkpoint:** every current chapter has a target disposition: move, split, merge, retain, archive, or remove with justification.

## Phase 5 — Perform mechanical moves

Move one part at a time with tracked moves. Recommended order:

1. New Machine Checklist: VI → VII.
2. Infrastructure: V → VI.
3. Engineering Practices: IV → V.
4. Technology Profiles: III → IV.
5. Create the empty Part III Development Toolchains entry point.

For each batch:

1. move files without rewriting their prose;
2. update `SUMMARY.md` paths and part title;
3. update every inbound/outbound relative link, image path, script input, and workflow reference;
4. search for the old path and old part name;
5. run all structural/link checks and a build;
6. inspect Git's rename detection and rendered navigation;
7. commit the batch separately.

**Checkpoint:** every commit leaves the book buildable and navigable.

## Phase 6 — Design Part III Development Toolchains

Create focused chapters following this hierarchy:

1. toolchain ownership and Docker/`mise` decision matrix;
2. install and activate `mise` in WSL;
3. configuration files, precedence, and trust;
4. runtimes and developer CLI recipes;
5. environment variables and secret boundaries;
6. `mise` tasks and repository automation;
7. team onboarding and CI;
8. security, updates, rollback, and troubleshooting.

During drafting:

- verify volatile commands against current official `mise` documentation;
- state tested versions and shells;
- demonstrate global default, committed project pin, and ignored local override;
- verify which executable is selected and where it was installed;
- never put service containers under `mise` ownership;
- keep secret values outside committed examples.

**Checkpoint:** a clean WSL user can reproduce at least one representative toolchain and explain its ownership.

## Phase 7 — Reconcile overlapping content

1. Review Part I's Linux Development Toolchain chapter. Keep OS prerequisites and the architecture overview there; move detailed `mise` workflows to Part III.
2. Review Composer. Keep dependency-management practice in Engineering Practices; keep PHP runtime/tool installation in Part III.
3. Review Docker chapters. Keep host integration in Part I, development workflow in Engineering Practices, and service-specific operation in Infrastructure.
4. Review Remote Development duplicates. Assign IDE connectivity to Part II and scenario/profile guidance to Part IV, or merge with explicit redirects.
5. Replace copied explanations with concise cross-links.
6. Update the New Machine Checklist only after final chapter paths stabilize.

**Checkpoint:** repository-wide searches reveal no contradictory tool ownership or unexplained duplicate chapters.

## Phase 8 — Content hardening

For every chapter:

1. confirm outcome, prerequisites, platform/shell context, and ownership;
2. verify commands in a supported disposable environment;
3. add expected results and independent verification;
4. add security, rollback, and troubleshooting where risk warrants;
5. replace secondary or stale claims with primary references;
6. mark version-sensitive and untested material;
7. remove personal paths, secrets, and machine-specific assumptions;
8. review accessibility and terminology.

Use separate content commits or pull requests when the change is not necessary to complete the structural migration.

## Phase 9 — Full validation and release candidate

Run from a clean clone of the branch:

- repository status and diff checks;
- Markdown lint;
- `SUMMARY.md` existence, uniqueness, and orphan checks;
- internal links, anchors, images, and case-sensitive path checks;
- external link check with failures reviewed manually;
- secret and private-data scan, including history for newly exposed data;
- syntax checks for representative shell/config examples where available;
- every supported DOCX/PDF/HTML/EPUB build;
- visual inspection of headings, tables, code blocks, page breaks, images, and navigation;
- clean WSL workstation walkthrough or a documented representative subset.

Repeat validation on GitHub Actions. Record exact tool versions, commands, date, results, waived failures, and justification in the pull request.

## Phase 10 — Pull request and review workflow

The pull request description should include:

- baseline and target commit;
- purpose, scope, and explicit non-goals;
- final old-path → new-path map;
- commit-by-commit review guide;
- validation matrix with local and CI results;
- rendered artifact links or attached previews;
- known limitations and follow-up issues;
- rollback plan.

Request at least one technical review for WSL/Docker/`mise` correctness and one editorial/structure review. Resolve review threads with additional focused commits; do not force-push after review unless team policy explicitly expects it.

## Phase 11 — Merge and release

1. Rebase or update the branch according to repository policy and rerun the complete suite.
2. Ensure `main` has not acquired conflicting path changes.
3. Merge only when required checks and approvals pass.
4. Verify the GitHub rendering and build from merged `main`.
5. Update version markers and release notes in a reviewed release commit if not already included.
6. Create the `v1.0.0` tag and GitHub release only with explicit maintainer authorization.
7. Keep the branch until post-merge verification succeeds, then remove it according to policy.

## Rollback strategy

- Before merge: close the pull request or revert individual migration commits on the branch.
- After merge but before release: use a normal revert pull request; do not rewrite `main`.
- After release: publish a corrective patch or revert release with clear notes and preserve the original tag.
- Generated artifacts may be regenerated; canonical Markdown and Git history must be preserved.

## v1.0 acceptance checklist

- [ ] Governance documents are present, consistent, and linked.
- [ ] Target Parts I–VII and appendices are represented in `SUMMARY.md`.
- [ ] Part III contains the complete agreed `mise` hierarchy.
- [ ] All moved paths are accounted for in the migration map.
- [ ] No stale internal references to old part paths remain.
- [ ] Every navigation entry resolves exactly once; no unintended chapter is orphaned.
- [ ] Markdown, links, anchors, images, secrets, and builds pass required checks.
- [ ] Critical procedures were tested in a clean supported environment.
- [ ] Windows, WSL, Docker, and `mise` ownership is consistent across chapters.
- [ ] Supported exports are reproducible and visually reviewed.
- [ ] Licensing, attribution, version scope, and known limitations are documented.
- [ ] Pull request approvals and required CI checks pass.
- [ ] Post-merge verification on `main` succeeds before tagging v1.0.0.

## Suggested commit sequence

```text
docs(governance): define v1 handbook architecture
build(markdown): add documentation validation
docs(structure): move new machine checklist to part VII
docs(structure): move infrastructure to part VI
docs(structure): move engineering practices to part V
docs(structure): move technology profiles to part IV
docs(toolchains): introduce part III development toolchains
docs(mise): add configuration and workflow chapters
fix(links): remove legacy part references
docs(release): prepare v1 release candidate
```
