# ChatWord

ChatWord 为 ChatArch 提供可组合的 Word/PDF 文档检查与纯文本抽取能力，既可以直接从 CLI 使用，也可以作为 Python API 接入自动化流程。

<div class="grid cards" markdown>

-   **快速处理文档**

    ---

    选择 Word 或 PDF extra，完成安装、检查和文本抽取。

    [进入快速开始](quickstart.md)

-   **查看真实命令面**

    ---

    通过 CLI 树确认已实现命令、参数和交互约定。

    [查看 CLI 树](cli-tree.md)

-   **判断能力边界**

    ---

    区分已实现、可选依赖、规划能力与明确不负责的范围。

    [查看能力地图](capability-map.md)

-   **接入自动化流程**

    ---

    对照 CLI 与 Python API，统一错误和输出安全契约。

    [查看 CLI 设计](cli-design.md)

</div>

## 按场景选择

| 目标 | 推荐入口 | 关键行为 |
| --- | --- | --- |
| 先判断文件能否处理 | `chatword inspect FILE` | 输出类型、大小、解析器与轻量元数据 |
| 给 Agent 或索引器提供正文 | `chatword extract FILE` | 输出 UTF-8 纯文本到 stdout |
| 将正文写入文件 | `chatword extract FILE -o OUTPUT` | 默认拒绝覆盖已有文件 |
| 在脚本中稳定调用 | `chatword ... -I` | 禁止缺参交互，错误以非零状态返回 |
| 直接嵌入 Python | `inspect_document()` / `extract_text()` | 复用与 CLI 一致的解析和错误边界 |

## 安全默认值

- 输入文档永远不能作为抽取输出路径。
- 已存在的输出文件只有在显式传入 `--force` 时才会被替换。
- 缺失、损坏或加密文档统一收敛为 ChatWord 错误，不向 CLI 泄漏第三方 parser traceback。
- OCR 只是可选依赖准备；当前 CLI 不把 OCR 命令伪装成已实现能力。
