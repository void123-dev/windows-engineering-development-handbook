# Configuration hierarchy and trust

Use `mise` configuration to separate shared project requirements from personal machine state. A project should commit the configuration needed to reproduce its supported toolchain. Personal overrides remain uncommitted, and secrets remain outside committed configuration.

The documented configuration model must make precedence explicit for:

- global defaults;
- committed project configuration;
- ignored local overrides;
- environment-specific configuration;
- trusted configuration and directory activation.

Treat configuration from an unfamiliar repository as untrusted until it has been reviewed. Verify exact filenames, precedence, and trust commands against the supported `mise` version before publication.
