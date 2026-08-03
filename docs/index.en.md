# ChatWord

ChatWord provides composable Word/PDF inspection and plain-text extraction for ChatArch. Use it directly from the CLI or embed the same contracts through the Python API.

<div class="grid cards" markdown>

-   **Process a document**

    ---

    Pick the Word or PDF extra, then install, inspect, and extract text.

    [Open Quick Start](quickstart.md)

-   **See the real command surface**

    ---

    Use the CLI tree to review implemented commands, options, and input behavior.

    [Open CLI Tree](cli-tree.md)

-   **Understand product boundaries**

    ---

    Separate implemented, optional, planned, and explicitly out-of-scope capabilities.

    [Open Capability Map](capability-map.md)

-   **Integrate automation**

    ---

    Match CLI behavior to the Python API, including errors and output safety.

    [Open CLI Design](cli-design.md)

</div>

## Choose by scenario

| Goal | Entry point | Key behavior |
| --- | --- | --- |
| Check whether a file is processable | `chatword inspect FILE` | Reports type, size, parser, and lightweight metadata |
| Feed text to an agent or indexer | `chatword extract FILE` | Emits UTF-8 plain text to stdout |
| Write extracted text to a file | `chatword extract FILE -o OUTPUT` | Refuses to overwrite by default |
| Run deterministically in automation | `chatword ... -I` | Disables missing-input prompts and returns non-zero errors |
| Embed the library | `inspect_document()` / `extract_text()` | Reuses the CLI parsing and error boundaries |

## Safe defaults

- The input document can never be used as the extraction output path.
- Existing outputs require explicit `--force` before replacement.
- Missing, corrupt, or encrypted documents become ChatWord errors instead of leaking parser tracebacks through the CLI.
- OCR is an optional dependency foundation; no OCR command is presented as implemented yet.
