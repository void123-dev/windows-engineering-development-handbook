# Trust and security

Treat `mise` configuration from an unfamiliar repository as untrusted until it has been reviewed. Review configuration, tasks, installation sources, backends, and plugins before allowing them to execute in the development environment.

Keep secrets outside committed configuration. Do not place tokens in examples, task definitions, shell history, validation output, or logs. Use placeholders when documentation needs to show a secret-bearing setting.

Document the supported trust workflow only after verifying it against the selected `mise` version. Where an installation source provides integrity or provenance controls, record the required verification without weakening upstream safeguards.
