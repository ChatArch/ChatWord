# 能力地图

## 当前能力

| 能力 | 状态 | 接口 | 边界 |
| --- | --- | --- | --- |
| 文件类型识别 | 已实现 | CLI + Python API | 基于扩展名识别 DOCX、DOC、PDF 和未知类型 |
| DOCX 检查 | 已实现 | CLI + Python API | 需要 `word` extra |
| DOCX 文本抽取 | 已实现 | CLI + Python API | 抽取段落与表格单元格文本 |
| PDF 检查 | 已实现 | CLI + Python API | 需要 `pdf` extra；加密内容只报告状态 |
| PDF 文本抽取 | 已实现 | CLI + Python API | 不执行 OCR；加密文件需要先解密 |
| 输出保护 | 已实现 | CLI | 默认拒绝覆盖；输入路径永远不可覆盖 |
| JSON 元数据 | 已实现 | `inspect --json` | 面向脚本和 Agent |

## 可选依赖

<div class="grid cards" markdown>

-   **`word`**

    `python-docx` 与 `mammoth`，面向 Word 文档。

-   **`pdf`**

    `pypdf` 与 `pdfplumber`，面向 PDF 文档。

-   **`ocr`**

    `pdf2image` 与 `pytesseract`，仅准备 OCR 依赖；当前没有 OCR CLI。

-   **`all`**

    一次安装常见 Word、PDF 与 OCR 依赖。

</div>

## 规划中的能力

- 文档转 PDF、PDF 转图像和 OCR 工作流。
- 面向 Agent 的结构化文本分块与摘要接口。
- 更完整的旧 `.doc` 转换路径。

这些项目属于能力规划，不是当前 CLI 命令。

## 不在当前范围

- 在线文档编辑器或协同编辑服务。
- 后台守护进程、Web API 或文件上传服务。
- 自动破解或绕过加密文档。
