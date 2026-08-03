<div align="center">
    <a href="https://pypi.python.org/pypi/ChatWord">
        <img src="https://img.shields.io/pypi/v/ChatWord.svg" alt="PyPI version" />
    </a>
    <a href="https://github.com/ChatArch/ChatWord/actions/workflows/ci.yml">
        <img src="https://github.com/ChatArch/ChatWord/actions/workflows/ci.yml/badge.svg" alt="Tests" />
    </a>
    <a href="https://arch.gh.wzhecnu.cn/ChatWord/">
        <img src="https://img.shields.io/badge/docs-mkdocs-blue.svg" alt="Documentation" />
    </a>
</div>

<div align="center">

**English** | [中文说明](README.md)
</div>

# ChatWord

ChatWord: Word document workflows for ChatArch.

[Documentation](https://arch.gh.wzhecnu.cn/ChatWord/) · [Quick Start](https://arch.gh.wzhecnu.cn/ChatWord/en/quickstart/) · [CLI Tree](https://arch.gh.wzhecnu.cn/ChatWord/en/cli-tree/) · [Capability Map](https://arch.gh.wzhecnu.cn/ChatWord/en/capability-map/)

## Quick Start

```bash
pip install -e ".[dev,word,pdf]"
chatword hello ChatArch
chatword inspect ./example.docx
chatword extract ./example.pdf -o ./example.txt
python -m pytest -q
python -m build
```

## Word/PDF Dependencies

The base install keeps only the CLI runtime. Document parsers are optional extras:

```bash
pip install "ChatWord[word]"   # python-docx, mammoth
pip install "ChatWord[pdf]"    # pypdf, pdfplumber
pip install "ChatWord[ocr]"    # pdf2image, pytesseract; requires system OCR tools
pip install "ChatWord[all]"    # common Word/PDF/OCR stack
```

## Task-Oriented CLI

- `chatword inspect FILE [--json]`: detect document type, size, parser availability, and lightweight metadata.
- `chatword extract FILE [-o OUTPUT] [--force]`: extract plain text from `.docx` or `.pdf`; existing outputs require `--force`, and the input document is never overwritten.
- See the [CLI Tree](https://arch.gh.wzhecnu.cn/ChatWord/en/cli-tree/) for the complete command surface and [CLI Design](https://arch.gh.wzhecnu.cn/ChatWord/en/cli-design/) for Python API mapping.

## CLI Contract

This template depends on `chatstyle>=0.1.0` and `chatenv>=0.1.1`. New commands should prefer:

- `CommandSchema` / `CommandField` for inputs.
- `add_interactive_option()` for the shared `-i/-I` switch.
- `resolve_command_inputs()` for missing args, defaults, TTY behavior, and validation.

## Layout

- `src/`: package source code
- `tests/`: CLI, parser, error-contract, and output-safety tests
- `docs/`: bilingual MkDocs sources maintained through `.en.md` mirrors

## Development Notes

See `DEVELOP.md` and `AGENTS.md` before expanding the scaffold.
