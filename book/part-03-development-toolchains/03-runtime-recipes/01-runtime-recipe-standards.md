# Runtime recipe standards

Runtime recipes document developer-facing language runtimes managed by `mise` inside WSL. Each recipe must identify the supported version, configuration scope, backend or source, executable location, version-selection behavior, verification, upgrade, and rollback.

Keep runtime installation separate from dependency-management practices. For example, a PHP runtime recipe belongs here, while Composer dependency policy remains in Part V.

Add a runtime-specific chapter only when its commands and supported versions have been verified against primary documentation.
