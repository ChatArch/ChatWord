# CLI 与 Python API 设计

## 设计目标

ChatWord 的命令面保持任务导向：先检查文档，再抽取文本。文档中的规划能力不会提前占用 CLI 命令。

## 命令与 API 映射

| 任务 | CLI | Python API |
| --- | --- | --- |
| 识别文档类型 | `chatword inspect FILE` | `detect_document_kind(path)` |
| 查看元数据 | `chatword inspect FILE [--json]` | `inspect_document(path)` |
| 抽取纯文本 | `chatword extract FILE` | `extract_text(path)` |
| 写入输出文件 | `chatword extract FILE -o OUTPUT` | 调用方负责写入 API 返回文本 |

## 错误边界

公共 API 使用 `ChatWordError` 家族表达可预期失败：

- `MissingDependencyError`：缺少 Word/PDF optional extra。
- `UnsupportedDocumentError`：当前不支持该文档类型或操作。
- `DocumentParseError`：文件缺失、损坏、加密或 parser 读取失败。

CLI 将这些错误转换为简短错误消息和非零退出码，不显示第三方 traceback。

## 输出安全

- 不指定 `-o` 时，正文写到 stdout。
- 指定 `-o` 时，已有文件默认不覆盖。
- `--force` 只允许替换另一个输出文件，不能把输入文档当作输出。
- 写文件前先完成路径保护检查。

## 交互约定

`inspect` 和 `extract` 使用 `CommandSchema`、`add_interactive_option()` 与 `resolve_command_inputs()`：

- 参数完整时直接执行。
- 缺少路径且允许交互时才补问。
- `-I` 始终关闭交互，适合自动化调用。

## 依赖模型

基础安装只包含 CLI 运行时。Word、PDF 和 OCR parser 通过 `word`、`pdf`、`ocr` 与 `all` extras 选择。CI 安装 `word` 与 `pdf`，确保真实 parser 路径进入测试。
