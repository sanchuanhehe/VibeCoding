# 对比总表（摘要）

```{warning}
本页只保留摘要。每个工具的详细评价、功能清单、证据链接请在对应单页维护。
```

## 完整对比表

```{raw} latex
\begin{landscape}
```

```{list-table}
:header-rows: 1
:widths: 10 13 13 26 18 20

* - 工具
  - 主要定位
  - 典型入口
  - 亮点能力
  - 适合场景
  - 主要限制/注意点
* - [GitHub Copilot](../tools/github-copilot.md)
  - 通用 AI coding + agent + review
  - GitHub / IDE / Terminal
  - Agent mode、代码审查、多模型、AGENT HQ；与 vscode 深度融合；订阅可用于 Claude Code 和 Codex
  - 已深度使用 GitHub 生态的团队
  - 价格与配额受套餐影响；企业能力需管理员配置
* - [Claude Code](../tools/claude-code.md)
  - Agentic coding（终端/IDE/桌面/Web）
  - Terminal / VS Code / JetBrains / Desktop / Web
  - 代码库级操作、命令执行、MCP 连接、GitHub Actions/GitLab CI 自动化；提出 skills/subagent 行业标准
  - 需要多端一致体验的团队
  - 高级能力依赖订阅；不同端能力细节有差异
* - [Codex CLI](../tools/codex-cli.md)
  - 终端编码 Agent（开源 CLI）
  - Terminal (macOS/Linux)
  - 本地读写代码、执行命令、非交互模式、MCP/多 Agent/SDK/CI 集成
  - 终端优先、自动化需求强的团队
  - 对命令行有要求；能力边界受环境权限影响
* - [Cline](../tools/cline.md)
  - IDE/CLI Agent（开源）
  - VS Code 扩展 + CLI
  - Plan/Act 工作流、MCP 扩展、支持多模型与多 Provider
  - 需要可定制 Agent 工作流的开发者
  - 配置项较多，上手门槛较高
* - [Aider](../tools/aider.md)
  - 终端 AI Pair Programming（开源）
  - CLI（可配 IDE）
  - Repo map、Git 自动提交、Lint/Test 联动、支持多模型
  - 终端优先、重视 Git 流程
  - 体验偏 CLI 心智
* - [Tabby](../tools/tabby.md)
  - 自托管 AI coding assistant（开源）
  - 自建服务 + IDE 插件
  - 开源、on-prem、OpenAPI、支持消费级 GPU
  - 强隐私/私有化部署团队
  - 需要自建与运维成本
* - [JetBrains AI Assistant](../tools/jetbrains-ai-assistant.md)
  - JetBrains 生态 AI 助手
  - JetBrains IDE / VS Code 扩展
  - Chat、补全、重构、测试生成、VCS 场景、MCP/ACP
  - JetBrains 重度用户团队
  - 以 JetBrains 生态为主
* - [Trae](../tools/trae.md)
  - AI IDE + SOLO Agent
  - Trae IDE / SOLO 模式
  - IDE 与 SOLO 双模式、Agent 生态、MCP、规则化工作流
  - 倾向 AI 主导任务的个人或小团队
  - 生态快速变化
* - [CodeBuddy](../tools/codebuddy.md)
  - 全流程 AI 编程平台
  - CodeBuddy IDE / IDE 插件 / CLI
  - 需求到部署链路、代码补全与审查、Plan/Subagents/Skills/Hooks、企业版 SSO
  - 国内团队、腾讯云生态
  - 产品线多，落地时需统一工作模式
* - [Qwen Code](../tools/qwen-code.md)
  - 开源终端 Agent（Qwen 生态）
  - CLI + IDE 集成
  - 终端优先、MCP、子智能体、可接多种 AI 端点
  - 开源与国内模型生态、CI 自动化团队
  - 需一定 CLI 与配置能力
* - [Qoder](../tools/qoder.md)
  - Agentic 编码平台
  - IDE / JetBrains 插件 / CLI
  - 上下文工程+智能体、Quest Mode、Repo Wiki、MCP、团队版 SSO
  - 兼顾 IDE 体验与 Agent 深度能力的团队
  - 生态更新较快
* - [OpenCode](../tools/opencode.md)
  - 开源 coding agent（终端优先）
  - CLI/TUI + Desktop (Beta)
  - 100% 开源、终端优先、内置 build/plan agent、Provider-agnostic
  - 开源终端工作流、避免绑定单一模型的团队
  - 企业治理需结合外部平台
* - [Cursor](../tools/cursor.md)
  - AI 编辑器 + 编码 Agent
  - Cursor IDE / CLI / Cloud Agent
  - Agent、MCP、Rules、Subagents、企业治理与合规，支持多模型
  - IDE + Agent + 企业策略一体化团队
  - 功能与计费策略迭代频繁
* - [Windsurf](../tools/windsurf.md)
  - 下一代 AI IDE
  - Windsurf IDE（含 Cascade）
  - Cascade 智能体、MCP、Memories/Rules、Workflows、App Deploys
  - 快速切换到 AI 原生 IDE 的团队
  - 平台演进快
* - [Sourcegraph Cody](../tools/sourcegraph-cody.md)
  - 企业代码库上下文 coding assistant
  - VS Code / JetBrains / Web / CLI
  - Sourcegraph Search API 结合本地+远程仓库上下文，支持 Chat/Auto-edit/Prompts
  - 大型代码库、跨仓库上下文高需求团队
  - 高级能力与 Sourcegraph 平台绑定
* - [Amazon Q Developer](../tools/amazon-q-developer.md)
  - AWS 生成式 AI 开发助手
  - IDE 插件 / CLI / AWS 控制台
  - 代码补全、安全扫描、重构升级、AWS 架构辅助
  - AWS 生态开发与运维一体化团队
  - 非 AWS 场景能力优势下降
* - [Google Antigravity](../tools/google-antigravity.md)
  - AI-first IDE + 跨表面 Agent
  - Antigravity 客户端
  - next-generation IDE、跨 editor/terminal/browser agent 工作流，支持多模型
  - Google 生态团队
  - Public preview，文档可能滞后
* - [Continue](../tools/continue.md)
  - AI checks / PR 审查（开源）
  - CLI + CI
  - .continue/checks 规则即代码、PR 通过/失败、可接受建议修复
  - 审查流程化的团队
  - 初期需配置 checks 规则
* - [CodeRabbit](../tools/coderabbit.md)
  - AI 代码审查与规划平台
  - Git 平台 + IDE 扩展 + CLI
  - 上下文感知 PR 审查、Issue Planner、支持 GitHub/GitLab/Azure/Bitbucket
  - 以 PR 审查效率为核心的团队
  - 深度能力与组织流程绑定
```

```{raw} latex
\end{landscape}
```
