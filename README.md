<div align="center">
    <a href="https://pypi.python.org/pypi/ChatWord">
        <img src="https://img.shields.io/pypi/v/ChatWord.svg" alt="PyPI version" />
    </a>
    <a href="https://github.com/ChatArch/ChatWord/actions/workflows/ci.yml">
        <img src="https://github.com/ChatArch/ChatWord/actions/workflows/ci.yml/badge.svg" alt="Tests" />
    </a>
    <a href="https://ChatArch.github.io/ChatWord">
        <img src="https://img.shields.io/badge/docs-mkdocs-blue.svg" alt="Documentation" />
    </a>
</div>

<div align="center">

[English](README.en.md) | [简体中文](README.md)
</div>

# ChatWord

ChatWord: Word document workflows for ChatArch.

## 快速开始

```bash
pip install -e ".[dev,word,pdf]"
chatword hello ChatArch
chatword inspect ./example.docx
chatword extract ./example.pdf -o ./example.txt
python -m pytest -q
python -m build
```

## Word/PDF 依赖

基础安装只包含 CLI 运行时；文档解析依赖按任务拆成 optional extras：

```bash
pip install "ChatWord[word]"   # python-docx, mammoth
pip install "ChatWord[pdf]"    # pypdf, pdfplumber
pip install "ChatWord[ocr]"    # pdf2image, pytesseract；还需要系统 OCR 工具
pip install "ChatWord[all]"    # 常见 Word/PDF/OCR 栈
```

## 任务导向 CLI

- `chatword inspect FILE [--json]`：识别文档类型、大小、解析器可用性和轻量元数据。
- `chatword extract FILE [-o OUTPUT] [--force]`：从 `.docx` 或 `.pdf` 抽取纯文本；默认拒绝覆盖已有输出，且始终拒绝覆盖输入文档。
- 详细设计见 `docs/cli-design.md`。

## CLI 规范

这个模板默认依赖 `chatstyle>=0.1.0` 和 `chatenv>=0.1.1`，新的命令应优先使用：

- `CommandSchema` / `CommandField` 描述输入。
- `add_interactive_option()` 提供统一 `-i/-I`。
- `resolve_command_inputs()` 统一缺参补问、默认值、TTY 与校验。

## 目录结构

- `src/`：包源码
- `tests/code-tests/`：代码测试和历史测试迁移
- `tests/cli-tests/`：真实 CLI 测试，doc-first
- `tests/mock-cli-tests/`：mock/fake CLI 测试，doc-first
- `docs/`：长期维护文档，由 mkdocs 构建

## 开发说明

扩展脚手架前，先阅读 `DEVELOP.md` 和 `AGENTS.md`。
