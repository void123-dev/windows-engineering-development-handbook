# Team and CI use

Team and CI workflows should consume the same committed tool versions. Onboarding instructions must explain how to install the toolchain, trust reviewed configuration, install pinned tools, and verify executable ownership.

CI documentation should record:

- the configuration used as the source of truth;
- caching boundaries;
- deterministic validation commands;
- behavior when `mise` or a required backend is unavailable.

CI output must not expose tokens through configuration, task output, or logs. Security and recovery guidance are maintained in the adjacent trust and troubleshooting chapters.
