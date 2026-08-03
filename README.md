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

**简体中文** | [英文版](README.en.md)
</div>

# ChatWord

ChatWord 为 ChatArch 提供 Word/PDF 文档检查、纯文本抽取与自动化接口。

[完整文档](https://arch.gh.wzhecnu.cn/ChatWord/) · [快速开始](https://arch.gh.wzhecnu.cn/ChatWord/quickstart/) · [CLI 树](https://arch.gh.wzhecnu.cn/ChatWord/cli-tree/) · [能力地图](https://arch.gh.wzhecnu.cn/ChatWord/capability-map/)

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
- 完整命令面见 [CLI 树](https://arch.gh.wzhecnu.cn/ChatWord/cli-tree/)，设计与 Python API 映射见 [CLI 设计](https://arch.gh.wzhecnu.cn/ChatWord/cli-design/)。

## CLI 规范

这个模板默认依赖 `chatstyle>=0.1.0` 和 `chatenv>=0.1.1`，新的命令应优先使用：

- `CommandSchema` / `CommandField` 描述输入。
- `add_interactive_option()` 提供统一 `-i/-I`。
- `resolve_command_inputs()` 统一缺参补问、默认值、TTY 与校验。

## 目录结构

- `src/`：包源码
- `tests/`：CLI、parser、错误契约和输出安全测试
- `docs/`：按 `.en.md` 镜像维护的中英文 MkDocs 文档

## 开发说明

扩展脚手架前，先阅读 `DEVELOP.md` 和 `AGENTS.md`。
