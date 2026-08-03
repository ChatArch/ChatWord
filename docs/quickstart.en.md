# Quick Start

## Choose an installation

<div class="grid cards" markdown>

-   **Word documents**

    ---

    ```bash
    pip install "ChatWord[word]"
    ```

    Enables `.docx` inspection and text extraction.

-   **PDF documents**

    ---

    ```bash
    pip install "ChatWord[pdf]"
    ```

    Enables PDF metadata inspection and text extraction.

-   **Common document stack**

    ---

    ```bash
    pip install "ChatWord[all]"
    ```

    Installs the Word, PDF, and OCR dependency foundations together.

</div>

## Inspect a document

```bash
chatword inspect ./example.docx
chatword inspect ./example.pdf --json
```

Human-readable output is useful in a terminal. `--json` is intended for agents, scripts, and CI.

## Extract text

```bash
chatword extract ./example.docx
chatword extract ./example.pdf -o ./example.txt
```

Existing output files are protected by default:

```bash
chatword extract ./example.pdf -o ./example.txt --force
```

Even with `--force`, the output path cannot be the input document.

## Interactive behavior

Use `-i` to allow a missing-path prompt and `-I` to disable prompting in automation:

```bash
chatword inspect -i
chatword inspect -I
```

## Development verification

```bash
pip install -e ".[dev,docs,word,pdf]"
python -m pytest -q
python -m build
mkdocs build --strict
```
