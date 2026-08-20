# Tasks

Use `mise` tasks for repeatable project commands such as validation, builds, tests, and onboarding checks. Task definitions should remain small, discoverable, and independently executable where practical.

Document each task's execution context, prerequisites, inputs, outputs, dependencies, and failure behavior. Avoid embedding secrets or machine-specific absolute paths. A task that starts or modifies a persistent service must preserve the Docker service boundary.

Team documentation should provide a command that lists the available tasks and an independent way to verify the result of important operations.
