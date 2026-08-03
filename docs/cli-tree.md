# CLI 树

下面只列出当前真实实现的命令，不把规划能力写成可调用接口。

```text
chatword
|-- --help
|-- --version
|-- hello [NAME] [-i | -I]
|-- inspect [PATH] [--json] [-i | -I]
`-- extract [PATH] [-o OUTPUT] [--force] [-i | -I]
```

## 顶层入口

| 入口 | 状态 | 用途 |
| --- | --- | --- |
| `--help` | 已实现 | 查看命令和参数 |
| `--version` | 已实现 | 查看当前包版本 |
| `hello` | 已实现 | 保留的最小 ChatStyle 输入示例 |

## 文档命令

<div class="grid cards" markdown>

-   **`inspect`**

    ---

    检查 `.docx`、`.pdf`、旧 `.doc` 或未知扩展。支持人类可读输出和 `--json`。

-   **`extract`**

    ---

    从 `.docx` 或 `.pdf` 抽取纯文本。支持 stdout、`-o` 文件输出和显式 `--force`。

</div>

## 输入契约

- `PATH` 缓存为可恢复的缺失参数：有 TTY 时可通过 `-i` 补问。
- `-I` 禁止交互，适合 Agent、CI 和 shell automation。
- `inspect --json` 是当前机器可读输出；`extract` 的机器接口是 stdout 或显式文件。

## 更新规则

新增或删除命令时，同时更新 CLI help 测试、本页命令树、能力地图和 README 命令摘要。
