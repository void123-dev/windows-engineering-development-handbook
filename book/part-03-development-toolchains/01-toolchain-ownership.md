# Development toolchain ownership

Developer-facing runtimes and command-line tools run inside WSL. Use `mise` to manage their versions when the tool is part of the project toolchain.

The toolchain includes:

- Git
- PHP
- Composer
- Node.js LTS
- npm or pnpm
- WP-CLI
- `wp-env`
- Laravel Installer
- Codex CLI

Use the WSL distribution package manager for OS libraries and low-level dependencies. Use Docker for persistent or networked services, not as the default provider for interactive developer CLIs. If a tool must exist in more than one layer, document the authoritative executable and verify its path.

The following `mise` Usage section explains configuration, supported tool recipes, environment management, tasks, team use, and recovery. Version-sensitive installation commands must be verified against the official `mise` documentation before publication.
