# CLI recipe standards

CLI recipes document interactive developer tools managed by `mise` inside WSL. Each recipe must state why the tool belongs in the toolchain layer, how its version is pinned, which executable is selected, and how upgrades or rollback affect projects.

Keep service operation outside these recipes. Databases, caches, proxies, queues, and application services remain under Docker and Infrastructure ownership.

Add a CLI-specific chapter only after verifying installation and version behavior against primary documentation.
