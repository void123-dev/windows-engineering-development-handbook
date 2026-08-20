# Tools, environment, and tasks

Use `mise` for project-facing runtimes and CLIs that need reproducible versions inside WSL. Keep service containers under Docker ownership and OS libraries under the WSL distribution package manager.

Tool recipes should state:

- the supported and pinned version;
- whether the setting is global, project-local, or personal;
- where the executable is installed;
- how to verify which executable is selected;
- backend or plugin caveats;
- upgrade and rollback behavior.

Non-secret environment values may be documented in committed configuration when appropriate. Secrets belong in an approved secret store or ignored local file. Never commit real credentials.

Use tasks for repeatable repository commands such as validation and document builds. Task definitions should remain small, discoverable, and independently executable where practical.
