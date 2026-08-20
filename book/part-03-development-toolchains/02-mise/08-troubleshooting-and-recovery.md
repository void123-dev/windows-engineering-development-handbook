# Troubleshooting and recovery

Begin diagnosis by checking the active shell, `PATH`, selected executable, configuration precedence, directory activation, and trust state. Confirm which layer owns the failing tool before changing Windows, WSL, Docker, or `mise` configuration.

Recovery guidance should preserve project files and unrelated user configuration. Prefer reversible changes, record the previous version or configuration, and verify the selected executable after recovery.

Document version-specific diagnostic and removal commands only after testing them against the supported `mise` release and shell.
