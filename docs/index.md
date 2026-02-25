# VibeCoding / AI Coding / AI Review 工具全景对比（持续更新）

本文档用于对比市面上主流的 Vibe Coding、AI Coding、AI Code Review 工具，目标是帮助你：

- 快速选型（个人、团队、企业）
- 明确各工具边界（写码、重构、审查、CI、治理）
- 建立统一评估框架，后续可持续补充

## 使用说明

- 由于产品迭代很快，本文默认以“官方文档/官方仓库信息”为准。
- 本版先覆盖已可核验的核心工具，后续按模板扩展到更多工具。
- “所有工具”在实践上应理解为“主流+有代表性+持续补录”。

## 对比维度（统一口径）

建议所有工具都按以下维度记录，避免只看宣传点：

1. **定位**：AI coding assistant / AI agent / AI review
2. **运行形态**：IDE 插件 / CLI / Web / CI / Git 平台集成
3. **核心能力**：补全、问答、重构、批量改码、PR 审查、自动修复
4. **上下文能力**：仓库索引、跨文件、规则、记忆、MCP/外部工具调用
5. **模型策略**：自带模型、多模型路由、是否支持本地模型
6. **协作与治理**：团队策略、审计、权限、合规、私有化
7. **成本结构**：免费层、个人版、团队版、企业版（按官方价格页）
8. **适配场景**：个人提效、中小团队、强合规企业、私有化环境

## 工具分层地图

### A. 通用 AI Coding（IDE/终端协作）

- GitHub Copilot
- Claude Code
- Codex CLI
- Cline
- Aider
- Tabby（偏自托管）
- JetBrains AI Assistant
- Trae（国内/全球双站）
- CodeBuddy（腾讯云）
- Qwen Code（Qwen CLI）
- Qoder
- OpenCode

### B. AI Review / AI Checks（PR 与 CI）

- Continue
- CodeRabbit
- GitHub Copilot Code Review（作为 Copilot 能力子集）

### C. 待补充（官网动态渲染或本次未完成核验）

- Cursor
- Windsurf / Codeium
- Sourcegraph Cody
- Amazon Q Developer

## 对比表（已核验条目，含新增）

| 工具 | 主要定位 | 典型入口 | 亮点能力 | 适合场景 | 主要限制/注意点 |
|---|---|---|---|---|---|
| GitHub Copilot | 通用 AI coding + agent + review | GitHub / IDE / Terminal | Agent mode、Copilot coding agent、Copilot code review、多模型、企业治理能力 | 已深度使用 GitHub 生态的团队 | 价格与配额受套餐影响；企业能力需管理员配置 |
| Claude Code | Agentic coding（终端/IDE/桌面/Web） | Terminal / VS Code / JetBrains / Desktop / Web | 代码库级操作、命令执行、MCP 连接、可用 GitHub Actions/GitLab CI 做自动化 | 需要“一套引擎多端一致体验”的团队 | 高级能力常依赖订阅与账号体系；不同端能力细节有差异 |
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
| Continue | AI checks / PR 审查（开源 CLI + 平台） | `cn` CLI + GitHub 状态检查 + CI | `.continue/checks` 规则即代码、PR 通过/失败、可接受建议修复、支持本地/CI 运行 | 想把 AI 审查“流程化、可执行化”的团队 | 需要先建设 checks 规则，初期有配置成本 |
| CodeRabbit | AI 代码审查与规划平台 | Git 平台 + IDE 扩展 + CLI | 上下文感知 PR 审查、Issue Planner、支持 GitHub/GitLab/Azure/Bitbucket | 以 PR 审查效率为核心诉求的团队 | 深度能力与组织流程绑定，需团队习惯配合 |

## 国内工具横评（Trae / CodeBuddy / Qwen Code / Qoder）

- **Trae**：更偏“AI IDE + 自主代理”路线，适合希望在 IDE 内直接切到高自动化模式（SOLO）的团队。
- **CodeBuddy**：更偏“产设研到部署的一体化平台”路线，IDE/插件/CLI 形态齐全，企业管理与腾讯云生态整合较强。
- **Qwen Code**：更偏“开源终端 Agent”路线，适合 CLI 驱动、可脚本化、愿意自己做工程规范治理的团队。
- **Qoder**：偏“Agent + IDE 深度融合”路线，Quest Mode 和 Repo Wiki 对复杂长期任务和知识沉淀友好，适合中高频 AI 协作开发团队。

## 快速选型建议（MVP 版本）

- **个人开发者，追求开箱即用**：优先试 GitHub Copilot。
- **终端流 + 可控改码**：优先试 Aider。
- **希望“Agent + MCP + 高可定制”**：优先试 Cline。
- **团队要把审查标准固化到 CI**：优先试 Continue。
- **私有化/内网优先**：优先试 Tabby。
- **JetBrains 重度用户**：优先试 JetBrains AI Assistant。

## 评测模板（后续新增工具直接套用）

### 模板字段

- 工具名：
- 官网/文档：
- 定位：
- 运行形态：
- 核心能力：
- 上下文能力：
- 模型支持：
- 数据与合规：
- 安全与权限控制：
- 协作治理：
- 可观测性与审计：
- 工作流集成深度：
- 可定制能力（规则/Skills/Subagents/MCP）：
- 上下文规模表现（大仓库/跨仓库）：
- 价格与版本：
- 迁移与锁定成本：
- 优势：
- 局限：
- 推荐人群：
- 评测基准结果（可选）：
- 最后核验日期：

> 建议：新增工具时至少填写到「迁移与锁定成本」，否则对企业选型参考价值会明显下降。

## 已收集来源（首版）

- GitHub Copilot: <https://github.com/features/copilot>
- GitHub Copilot Docs: <https://docs.github.com/en/copilot>
- Cline: <https://github.com/cline/cline>
- Aider: <https://github.com/Aider-AI/aider>
- Continue: <https://github.com/continuedev/continue>
- Tabby: <https://github.com/TabbyML/tabby>
- CodeRabbit Docs: <https://docs.coderabbit.ai>
- JetBrains AI Assistant Docs: <https://www.jetbrains.com/help/ai-assistant/about-ai-assistant.html>
- Claude Code Docs: <https://code.claude.com/docs/en>
- Codex Docs: <https://developers.openai.com/codex/cli>
- Trae CN: <https://www.trae.cn/>
- Trae Global: <https://www.trae.ai/>
- CodeBuddy Docs: <https://www.codebuddy.cn/docs/ide/Introduction>
- CodeBuddy Pricing: <https://www.codebuddy.cn/pricing>
- Qwen Code Repo: <https://github.com/QwenLM/qwen-code>
- Qwen Code Docs (ZH): <https://qwenlm.github.io/qwen-code-docs/zh/users/overview/>
- Qoder Docs (ZH): <https://docs.qoder.com/zh/>
- Qoder Pricing: <https://docs.qoder.com/zh/account/pricing>
- OpenCode Repo: <https://github.com/anomalyco/opencode>
- OpenCode Website: <https://opencode.ai/>

## 下一步补充清单

1. 逐个补全 Cursor / Windsurf / Cody / Amazon Q Developer 的官方文档证据。
2. 增加“定价对比表（个人/团队/企业）”。
3. 增加“同一任务基准对比”（例如：修复 bug、跨文件重构、PR 安全审查）。
