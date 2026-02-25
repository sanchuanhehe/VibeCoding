# 对比总表（摘要）

```{warning}
本页只保留摘要。每个工具的详细评价、功能清单、证据链接请在对应单页维护。
```

## 完整对比表（原始内容保留）

```{important}
以下表格按你提供的版本完整保留，作为“基线主表”。后续如有改动，建议先在单工具页更新，再回填本表。
```

| 工具 | 主要定位 | 典型入口 | 亮点能力 | 适合场景 | 主要限制/注意点 |
| --- | --- | --- | --- | --- | --- |
| GitHub Copilot | 通用 AI coding + agent + review | GitHub / IDE / Terminal | Agent mode、Copilot coding agent、Copilot code review、多模型、企业治理能力、AGENT HQ 企业级工具里的开源开放派(能使用国外所有的模型,且代码开源) 依托vscode上游,与vscode深度融合 功能齐全 发布节奏快 订阅覆盖面最广 且其订阅现在能够在claude code和codex工具使用,官方提供转换的方法 | 已深度使用 GitHub 生态的团队 | 价格与配额受套餐影响(额度按次计费,还算便宜,但是有最大限额)；企业能力需管理员配置 |
| Claude Code | Agentic coding（终端/IDE/桌面/Web） | Terminal / VS Code / JetBrains / Desktop / Web | 代码库级操作、命令执行、MCP 连接、可用 GitHub Actions/GitLab CI 做自动化 提出了很多领先的理念,例如skills mcp 插件,已经成为ai coding届的事实标准 | 需要“一套引擎多端一致体验”的团队 | 高级能力常依赖订阅与账号体系；不同端能力细节有差异 |
| Codex CLI | 终端编码 Agent（开源 CLI） | Terminal（macOS/Linux，Windows 实验） | 本地读写代码、执行命令、非交互模式、MCP/多 Agent/SDK/CI 集成路径完整 | 终端优先、自动化和脚本化需求强的团队 | 对命令行工作流有要求；能力边界受审批模式和环境权限影响 |
| Cline | IDE/CLI Agent（开源） | VS Code 扩展 + CLI | Plan/Act 工作流、MCP 扩展、支持多模型与多 Provider、可接 VS Code LM API | 需要可定制 Agent 工作流的开发者 | 配置项较多，上手门槛高于“开箱即用”产品 |
| Aider | 终端 AI Pair Programming（开源） | CLI（可配 IDE） | Repo map、Git 自动提交、Lint/Test 联动、支持云端与本地多模型 | 终端优先、重视可控改码与 Git 流程 | 体验偏 CLI 心智，对纯 IDE 用户不一定友好 |
| Tabby | 自托管 AI coding assistant（开源） | 自建服务 + IDE 插件 | 开源、on-prem、OpenAPI、支持消费级 GPU、企业集成能力 | 强隐私/私有化部署团队 | 需要自建与运维成本 |
| JetBrains AI Assistant | JetBrains 生态 AI 助手 | JetBrains IDE / VS Code 扩展 | Chat、补全、重构、测试生成、VCS 场景、MCP/ACP 与项目规则 | JetBrains 重度用户团队 | 以 JetBrains 生态为主，跨工具统一治理需额外设计 |
| Trae | AI IDE + SOLO Agent | Trae IDE / SOLO 模式 | IDE 与 SOLO 双模式、Agent 生态、MCP、规则化工作流、强调本地优先与区域化部署说明 | 倾向“AI 主导推进任务”的个人或小团队 | 生态仍在快速变化，企业治理与第三方流程细节需逐项验证 |
| CodeBuddy（含 CodeBuddy Code） | 全流程 AI 编程平台（IDE/插件/CLI） | CodeBuddy IDE / IDE 插件 / CLI | 从需求到部署链路、代码补全与审查、规则/记忆/MCP、Plan/Subagents/Skills/Hooks、企业版能力（SSO/管理/网络） | 国内团队、腾讯云生态、需要企业管理能力的组织 | 产品线较多（IDE/插件/CLI），落地时需先统一团队工作模式；“Flow”命名在公开文档以模式能力呈现为主 |
| Qwen Code（Qwen CLI） | 开源终端 Agent（Qwen 生态） | CLI（`qwen`）+ IDE 集成 | 终端优先、交互/无头模式、MCP、子智能体、可接 OpenAI/Anthropic/Gemini 兼容端点 + Qwen OAuth | 偏好开源+国内模型生态、CI 自动化需求团队 | 需要一定 CLI 与配置能力；企业级治理能力依赖外围平台与自建规范 |
| Qoder | Agentic 编码平台（IDE/JetBrains/CLI） | AI-Native IDE / JetBrains 插件 / CLI | 强调上下文工程+智能体，多文件修改、Quest Mode、Repo Wiki、MCP 扩展，支持团队版（含 SSO/集中管理） | 希望兼顾 IDE 体验与 Agent 深度能力，并需要团队治理能力的团队 | 生态更新较快，部分企业能力仍在持续迭代；高级模型额度依赖 Credits 体系 |
| OpenCode | 开源 AI coding agent（终端优先） | CLI/TUI + Desktop（Beta） | 100% 开源、终端优先体验、内置 build/plan agent、Provider-agnostic（Claude/OpenAI/Google/本地模型）、可扩展文档与配置体系 | 偏好开源和终端工作流、希望避免绑定单一模型厂商的开发者/团队 | 以终端体验为核心，企业治理与托管能力需结合外部平台；部分图形化体验仍在完善 |
| Cursor | AI 编辑器 + 编码 Agent | Cursor IDE / CLI / Cloud Agent | 官方文档覆盖 Agent、CLI、Cloud Agent、MCP、Rules、Subagents、企业治理与合规章节，支持多模型与团队管理能力 | 需要“IDE + Agent + 企业策略”一体化的团队 | 动态文档更新快，功能与计费策略迭代频繁，落地时需按团队版本复核 |
| Windsurf | 下一代 AI IDE | Windsurf IDE（含 Cascade） | Cascade 智能体、MCP、Memories/Rules、Context Awareness、Workflows、App Deploys；支持从 VS Code/Cursor 导入配置 | 想快速切换到 AI 原生 IDE 并保持上手平滑的团队 | 平台演进快，企业治理细项与第三方集成边界需按当前版本核对 |
| Sourcegraph Cody | AI coding assistant（企业代码库上下文强化） | VS Code / JetBrains / Visual Studio / Web / CLI | 结合 Sourcegraph Search API 获取本地+远程仓库上下文，支持 Chat/Auto-edit/Prompts/Context Filters，强调企业代码理解 | 大型代码库、跨仓库上下文需求高的团队 | 高级能力常与 Sourcegraph 平台能力绑定，部署与采购模型需综合评估 |
| Amazon Q Developer | 生成式 AI 开发助手（AWS 深度集成） | IDE 插件 / CLI / AWS 控制台 / 聊天应用 | 代码聊天与补全、生成与安全扫描、重构升级、AWS 架构与运维辅助、支持 Free/Pro 套餐 | AWS 生态内开发与运维一体化团队 | 最佳价值在 AWS 场景，跨云与非 AWS 工作流下能力优势可能下降 |
| Google Antigravity | AI-first IDE + 跨表面 Agent（Google 生态） | Antigravity 客户端（Editor/Terminal/Browser 协同） | 官网强调 next-generation IDE、跨 editor/terminal/browser 的 agent 工作流；定价页显示可用 Gemini 3.1 Pro / Gemini 3 Flash / Claude Sonnet & Opus 4.6 / gpt-oss-120b，并含 Tab/Command 能力（按套餐与限额） | 想在 Google 账号与 Google One/Workspace/Cloud 体系内使用一体化 AI IDE + Agent 的个人与团队 | 当前处于 Public preview，文档抓取受动态页面影响；与“Gemini CLI（终端优先）”是不同产品线，能力与配额需按各自文档复核 |
| Continue | AI checks / PR 审查（开源 CLI + 平台） | `cn` CLI + GitHub 状态检查 + CI | `.continue/checks` 规则即代码、PR 通过/失败、可接受建议修复、支持本地/CI 运行 | 想把 AI 审查“流程化、可执行化”的团队 | 需要先建设 checks 规则，初期有配置成本 |
| CodeRabbit | AI 代码审查与规划平台 | Git 平台 + IDE 扩展 + CLI | 上下文感知 PR 审查、Issue Planner、支持 GitHub/GitLab/Azure/Bitbucket | 以 PR 审查效率为核心诉求的团队 | 深度能力与组织流程绑定，需团队习惯配合 |

```{list-table} 工具对比（摘要）
:header-rows: 1

* - 工具
  - 主要定位
  - 典型入口
  - 适合场景
* - [GitHub Copilot](../tools/github-copilot.md)
  - 通用 AI coding + review
  - GitHub / IDE / Terminal
  - GitHub 生态团队
* - [Claude Code](../tools/claude-code.md)
  - Agentic coding
  - Terminal / IDE / Desktop / Web
  - 多端一致体验
* - [Codex CLI](../tools/codex-cli.md)
  - 终端编码 Agent
  - CLI
  - 自动化与脚本化
* - [Cline](../tools/cline.md)
  - IDE/CLI Agent
  - VS Code 扩展 + CLI
  - 可定制工作流
* - [Aider](../tools/aider.md)
  - 终端 Pair Programming
  - CLI
  - Git 驱动协作
* - [Tabby](../tools/tabby.md)
  - 自托管 coding assistant
  - 自建服务 + IDE 插件
  - 私有化团队
* - [JetBrains AI Assistant](../tools/jetbrains-ai-assistant.md)
  - JetBrains AI 助手
  - JetBrains IDE
  - JetBrains 用户
* - [Trae](../tools/trae.md)
  - AI IDE + Agent
  - Trae IDE
  - AI 原生 IDE 团队
* - [CodeBuddy](../tools/codebuddy.md)
  - 全流程 AI 编程平台
  - IDE / 插件 / CLI
  - 国内企业协作
* - [Qwen Code](../tools/qwen-code.md)
  - 开源终端 Agent
  - CLI
  - 开源与国内模型生态
* - [Qoder](../tools/qoder.md)
  - Agentic 编码平台
  - IDE / 插件 / CLI
  - 长任务与知识沉淀
* - [OpenCode](../tools/opencode.md)
  - 开源 coding agent
  - CLI / Desktop
  - 开源终端流
* - [Cursor](../tools/cursor.md)
  - AI 编辑器 + Agent
  - IDE / CLI / Cloud Agent
  - 一体化团队策略
* - [Windsurf](../tools/windsurf.md)
  - AI IDE
  - Windsurf IDE
  - 迁移到 AI 原生 IDE
* - [Sourcegraph Cody](../tools/sourcegraph-cody.md)
  - 企业上下文 coding assistant
  - IDE / Web / CLI
  - 大型多仓团队
* - [Amazon Q Developer](../tools/amazon-q-developer.md)
  - AWS 开发助手
  - IDE / CLI / AWS Console
  - AWS 一体化团队
* - [Google Antigravity](../tools/google-antigravity.md)
  - AI-first IDE + 跨表面 Agent
  - Antigravity 客户端
  - Google 生态团队
* - [Continue](../tools/continue.md)
  - AI checks / PR 审查
  - CLI + CI
  - 审查规则流程化
* - [CodeRabbit](../tools/coderabbit.md)
  - PR 审查平台
  - Git 平台 + IDE + CLI
  - 审查效率优先团队
* - [Codeium](../tools/codeium.md)
  - 待补核验
  - 待补核验
  - 待补核验
```
