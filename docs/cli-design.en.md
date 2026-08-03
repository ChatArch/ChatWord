# CLI and Python API Design

## Design goal

ChatWord keeps a task-oriented surface: inspect a document first, then extract text. Planned capabilities do not reserve fake CLI commands.

## CLI-to-API mapping

| Task | CLI | Python API |
| --- | --- | --- |
| Detect document kind | `chatword inspect FILE` | `detect_document_kind(path)` |
| Read metadata | `chatword inspect FILE [--json]` | `inspect_document(path)` |
| Extract plain text | `chatword extract FILE` | `extract_text(path)` |
| Write an output file | `chatword extract FILE -o OUTPUT` | The caller writes the returned API text |

## Error boundary

The public API uses the `ChatWordError` family for expected failures:

- `MissingDependencyError`: a Word/PDF optional extra is unavailable.
- `UnsupportedDocumentError`: the document type or operation is unsupported.
- `DocumentParseError`: the file is missing, corrupt, encrypted, or unreadable by the parser.

The CLI converts these errors into concise messages and non-zero exit codes without exposing third-party tracebacks.

## Output safety

- Without `-o`, extracted text goes to stdout.
- With `-o`, existing files are protected by default.
- `--force` may replace another output file but can never target the input document.
- Path protection runs before any output write.

## Interactive contract

`inspect` and `extract` use `CommandSchema`, `add_interactive_option()`, and `resolve_command_inputs()`:

- Complete arguments execute immediately.
- A missing path prompts only when interaction is allowed.
- `-I` always disables prompting for automation.

## Dependency model

The base installation contains only the CLI runtime. Select Word, PDF, and OCR parsers through the `word`, `pdf`, `ocr`, or `all` extras. CI installs `word` and `pdf` so real parser paths remain covered.
