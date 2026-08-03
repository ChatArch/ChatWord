# CLI 设计

ChatWord CLI 应保持任务导向：用户从文档任务出发，而不是从底层解析库名称出发。

## 已实现 MVP

| 任务 | 命令 | 用途 |
| --- | --- | --- |
| 查看文件信息 | `chatword inspect FILE [--json]` | 识别 Word/PDF 类型、文件大小、解析器可用性和轻量元数据。 |
| 抽取正文 | `chatword extract FILE [-o OUTPUT] [--force]` | 从 `.docx` 或 `.pdf` 抽取纯文本，供总结、索引或后续 agent 流程使用。已有输出必须显式 `--force`，输入文档永不覆盖。 |

## 依赖模型

基础安装保持轻量，文档解析器通过 optional extras 安装：

```bash
pip install "ChatWord[word]"   # python-docx, mammoth
pip install "ChatWord[pdf]"    # pypdf, pdfplumber
pip install "ChatWord[ocr]"    # pdf2image, pytesseract；还需要系统 OCR 工具
pip install "ChatWord[all]"    # 常见 Word/PDF/OCR 栈
```

## 下一批任务命令

这些命令围绕常见文档处理任务设计：

| 任务 | 规划命令 | 说明 |
| --- | --- | --- |
| 抽取表格 | `chatword tables FILE --format csv|json` | Word 表格走 `python-docx`，PDF 表格走 `pdfplumber`。 |
| 转 Markdown | `chatword convert FILE -o OUT.md` | `.docx` 优先用 `mammoth` 做语义转换；PDF 先走文本优先。 |
| 生成大纲 | `chatword outline FILE` | 返回标题、页锚点和近似结构，方便 agent 规划。 |
| 扫描件 OCR | `chatword ocr FILE -o OUT.txt` | 作为可选能力，因为依赖 Tesseract、Poppler 等系统组件。 |
| 批量处理 | `chatword batch INPUT_DIR --glob "*.pdf" --task extract` | 用于项目文件夹和 agent pipeline。 |

## 输出规则

- 面向人的输出应简洁、稳定，方便复制粘贴。
- 面向自动化和 agent 的命令应提供 `--json`。
- 缺少 optional dependency 时，应明确提示需要安装哪个 extra。
- 除非参数缺失且任务可恢复，否则命令不应主动交互式提问。
- 文件参数遵循统一 `-i/-I` 交互契约；自动化场景可用 `-I` 禁止补问。
- 解析错误统一收敛为 ChatWord 错误，不向 CLI 泄漏第三方 parser 异常。
