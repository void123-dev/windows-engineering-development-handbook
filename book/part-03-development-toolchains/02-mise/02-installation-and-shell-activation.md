# Installation and shell activation

Install `mise` inside WSL, not on the Windows host, when it manages the handbook's Linux developer toolchain. Keep repositories and project configuration in the WSL filesystem unless Windows-native integration requires otherwise.

Before publishing installation commands, verify them against the current official `mise` documentation. The completed procedure must identify its supported WSL distribution and shell and cover:

- prerequisites and installation source;
- shell activation and a new-shell verification;
- the selected `mise` executable and its location;
- upgrade and removal;
- rollback when shell activation fails.

Do not place credentials in shell startup files or committed examples.
