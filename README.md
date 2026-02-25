# VibeCoding Docs

基于 Sphinx + MyST 的文档项目，使用 Markdown 作为主写作语言，依赖由 `uv` 管理。

## 环境要求

- Python 3.12+
- uv

## 初始化

```bash
uv sync --dev
```

## 本地构建文档

```bash
uv run sphinx-build -W --keep-going -b html docs docs/_build/html
```

构建产物输出在 `docs/_build/html`。

## Esbonio

已提供工作区配置文件 `.vscode/settings.json`，打开本仓库后 Esbonio 将自动识别 `docs/conf.py`。
