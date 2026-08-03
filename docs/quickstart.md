# 快速开始

## 选择安装方式

<div class="grid cards" markdown>

-   **Word 文档**

    ---

    ```bash
    pip install "ChatWord[word]"
    ```

    用于 `.docx` 检查和文本抽取。

-   **PDF 文档**

    ---

    ```bash
    pip install "ChatWord[pdf]"
    ```

    用于 PDF 元数据检查和文本抽取。

-   **全部常见能力**

    ---

    ```bash
    pip install "ChatWord[all]"
    ```

    同时准备 Word、PDF 和 OCR 相关依赖。

</div>

## 检查文档

```bash
chatword inspect ./example.docx
chatword inspect ./example.pdf --json
```

人类可读输出适合终端检查；`--json` 适合 Agent、脚本或 CI 消费。

## 抽取文本

```bash
chatword extract ./example.docx
chatword extract ./example.pdf -o ./example.txt
```

如果输出文件已经存在，命令会拒绝覆盖：

```bash
chatword extract ./example.pdf -o ./example.txt --force
```

即使使用 `--force`，输出路径也不能与输入文档相同。

## 交互模式

当路径缺失时，`-i` 允许补问；自动化场景使用 `-I` 禁止补问：

```bash
chatword inspect -i
chatword inspect -I
```

## 开发验证

```bash
pip install -e ".[dev,docs,word,pdf]"
python -m pytest -q
python -m build
mkdocs build --strict
```
