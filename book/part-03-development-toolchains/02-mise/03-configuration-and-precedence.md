# Configuration and precedence

Use `mise` configuration to separate shared project requirements from personal machine state. A project should commit the configuration needed to reproduce its supported toolchain. Personal overrides remain uncommitted, and secrets remain outside committed configuration.

The documented configuration model must make precedence explicit for:

- global defaults;
- committed project configuration;
- ignored local overrides;
- environment-specific configuration;
- trusted configuration and directory activation.

Verify exact filenames and precedence against the supported `mise` version before publication. Trust and configuration security are covered separately in [Trust and security](04-trust-and-security.md).
