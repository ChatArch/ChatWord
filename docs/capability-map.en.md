# Capability Map

## Current capabilities

| Capability | Status | Interface | Boundary |
| --- | --- | --- | --- |
| File-kind detection | Implemented | CLI + Python API | Detects DOCX, DOC, PDF, and unknown types by extension |
| DOCX inspection | Implemented | CLI + Python API | Requires the `word` extra |
| DOCX text extraction | Implemented | CLI + Python API | Extracts paragraphs and table-cell text |
| PDF inspection | Implemented | CLI + Python API | Requires the `pdf` extra; encrypted content reports status only |
| PDF text extraction | Implemented | CLI + Python API | Does not run OCR; encrypted files must be decrypted first |
| Output protection | Implemented | CLI | Refuses overwrite by default and never overwrites the input |
| JSON metadata | Implemented | `inspect --json` | Intended for scripts and agents |

## Optional dependencies

<div class="grid cards" markdown>

-   **`word`**

    `python-docx` and `mammoth` for Word documents.

-   **`pdf`**

    `pypdf` and `pdfplumber` for PDF documents.

-   **`ocr`**

    `pdf2image` and `pytesseract` prepare OCR dependencies; no OCR CLI exists yet.

-   **`all`**

    Installs the common Word, PDF, and OCR dependency stack.

</div>

## Planned capabilities

- Document-to-PDF, PDF-to-image, and OCR workflows.
- Structured chunking and summarization interfaces for agents.
- A fuller conversion path for legacy `.doc` files.

These are capability plans, not current CLI commands.

## Out of scope

- An online document editor or collaborative editing service.
- A background daemon, Web API, or upload service.
- Breaking or bypassing document encryption.
