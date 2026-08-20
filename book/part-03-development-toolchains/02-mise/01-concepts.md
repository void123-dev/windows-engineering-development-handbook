# `mise` concepts

`mise` is the handbook's toolchain layer inside WSL. It selects developer-facing runtime and CLI versions, activates project configuration, and exposes repeatable tasks. It does not replace Docker services or the WSL distribution package manager.

Use `mise` when a runtime or CLI must be reproducible for a developer or project. Use Docker for persistent or networked services, and use the distribution package manager for OS libraries and low-level dependencies.

Configuration may define global defaults, committed project requirements, environment-specific behavior, or ignored personal overrides. The following chapters define how those scopes are installed, trusted, activated, verified, and recovered.
