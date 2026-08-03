# CLI Tree

The tree lists only implemented commands. Planned capabilities are not presented as callable interfaces.

```text
chatword
|-- --help
|-- --version
|-- hello [NAME] [-i | -I]
|-- inspect [PATH] [--json] [-i | -I]
`-- extract [PATH] [-o OUTPUT] [--force] [-i | -I]
```

## Top-level entries

| Entry | Status | Purpose |
| --- | --- | --- |
| `--help` | Implemented | Show commands and options |
| `--version` | Implemented | Show the package version |
| `hello` | Implemented | Preserve the minimal ChatStyle input example |

## Document commands

<div class="grid cards" markdown>

-   **`inspect`**

    ---

    Inspect `.docx`, `.pdf`, legacy `.doc`, or unknown extensions. Supports human-readable output and `--json`.

-   **`extract`**

    ---

    Extract text from `.docx` or `.pdf`. Supports stdout, `-o` file output, and explicit `--force`.

</div>

## Input contract

- A missing `PATH` is recoverable: `-i` may prompt when a TTY is available.
- `-I` disables prompting for agents, CI, and shell automation.
- `inspect --json` is the machine-readable metadata surface; `extract` uses stdout or an explicit file.

## Update rule

When commands change, update CLI help tests, this tree, the capability map, and the README command summary together.
