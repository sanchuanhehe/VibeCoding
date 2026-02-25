# VibeCoding Docs

基于 Sphinx + MyST 的文档项目，使用 Markdown 作为主写作语言，依赖由 `uv` 管理。

## 环境要求

- Python 3.12+
- uv
- Node.js（用于运行 markdownlint）

## 初始化

```bash
uv sync --dev
```

## 本地构建文档

```bash
uv run sphinx-build -W --keep-going -b html docs docs/_build/html
```

构建产物输出在 `docs/_build/html`。

## Markdown 规范检查

```bash
make lint-md
```

自动修复可由 markdownlint 处理的问题：

```bash
make lint-md-fix
```

默认使用仓库根目录下的 `.markdownlint.jsonc` 和 `.markdownlintignore`。

## Esbonio

已提供工作区配置文件 `.vscode/settings.json`，打开本仓库后 Esbonio 将自动识别 `docs/conf.py`。
