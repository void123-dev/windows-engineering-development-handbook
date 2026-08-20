# Environment management

Use `mise` environment management for non-secret values that belong to the selected development context. State whether each value is global, committed project configuration, environment-specific configuration, or an ignored personal override.

Document:

- configuration precedence;
- directory activation behavior;
- which files are committed or ignored;
- how to verify the active value without exposing sensitive data;
- how to deactivate or roll back the environment safely.

Secrets belong in an approved secret store or ignored local file. Never commit real credentials or print them during verification.
