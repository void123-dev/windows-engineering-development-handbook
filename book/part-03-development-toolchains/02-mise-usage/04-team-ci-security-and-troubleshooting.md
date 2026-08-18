# Team use, CI, security, and troubleshooting

Team and CI workflows should consume the same committed tool versions. Onboarding instructions must explain how to install the toolchain, trust reviewed configuration, install pinned tools, and verify executable ownership.

CI documentation should record:

- the configuration used as the source of truth;
- caching boundaries;
- deterministic validation commands;
- behavior when `mise` or a required backend is unavailable.

Review the provenance of installation sources, backends, and plugins. Do not trust repository configuration automatically or expose tokens through configuration, task output, or logs.

Troubleshooting should begin by checking the active shell, `PATH`, selected executable, configuration precedence, and trust state. Recovery instructions must avoid deleting unrelated tool installations or user configuration.
