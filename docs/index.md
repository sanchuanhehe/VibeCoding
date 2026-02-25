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
- Cline
- Aider
- Tabby（偏自托管）
- JetBrains AI Assistant

### B. AI Review / AI Checks（PR 与 CI）

- Continue
- CodeRabbit
- GitHub Copilot Code Review（作为 Copilot 能力子集）

### C. 待补充（官网动态渲染，需二次核验）

- Cursor
- Windsurf / Codeium
- Sourcegraph Cody
- Amazon Q Developer

## 首版对比表（已核验条目）

| 工具 | 主要定位 | 典型入口 | 亮点能力 | 适合场景 | 主要限制/注意点 |
|---|---|---|---|---|---|
| GitHub Copilot | 通用 AI coding + agent + review | GitHub / IDE / Terminal | Agent mode、Copilot coding agent、Copilot code review、多模型、企业治理能力 | 已深度使用 GitHub 生态的团队 | 价格与配额受套餐影响；企业能力需管理员配置 |
| Cline | IDE/CLI Agent（开源） | VS Code 扩展 + CLI | Plan/Act 工作流、MCP 扩展、支持多模型与多 Provider、可接 VS Code LM API | 需要可定制 Agent 工作流的开发者 | 配置项较多，上手门槛高于“开箱即用”产品 |
| Aider | 终端 AI Pair Programming（开源） | CLI（可配 IDE） | Repo map、Git 自动提交、Lint/Test 联动、支持云端与本地多模型 | 终端优先、重视可控改码与 Git 流程 | 体验偏 CLI 心智，对纯 IDE 用户不一定友好 |
| Tabby | 自托管 AI coding assistant（开源） | 自建服务 + IDE 插件 | 开源、on-prem、OpenAPI、支持消费级 GPU、企业集成能力 | 强隐私/私有化部署团队 | 需要自建与运维成本 |
| JetBrains AI Assistant | JetBrains 生态 AI 助手 | JetBrains IDE / VS Code 扩展 | Chat、补全、重构、测试生成、VCS 场景、MCP/ACP 与项目规则 | JetBrains 重度用户团队 | 以 JetBrains 生态为主，跨工具统一治理需额外设计 |
| Continue | AI checks / PR 审查（开源 CLI + 平台） | `cn` CLI + GitHub 状态检查 + CI | `.continue/checks` 规则即代码、PR 通过/失败、可接受建议修复、支持本地/CI 运行 | 想把 AI 审查“流程化、可执行化”的团队 | 需要先建设 checks 规则，初期有配置成本 |
| CodeRabbit | AI 代码审查与规划平台 | Git 平台 + IDE 扩展 + CLI | 上下文感知 PR 审查、Issue Planner、支持 GitHub/GitLab/Azure/Bitbucket | 以 PR 审查效率为核心诉求的团队 | 深度能力与组织流程绑定，需团队习惯配合 |

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
- 协作治理：
- 价格与版本：
- 优势：
- 局限：
- 推荐人群：
- 最后核验日期：

## 已收集来源（首版）

- GitHub Copilot: <https://github.com/features/copilot>
- GitHub Copilot Docs: <https://docs.github.com/en/copilot>
- Cline: <https://github.com/cline/cline>
- Aider: <https://github.com/Aider-AI/aider>
- Continue: <https://github.com/continuedev/continue>
- Tabby: <https://github.com/TabbyML/tabby>
- CodeRabbit Docs: <https://docs.coderabbit.ai>
- JetBrains AI Assistant Docs: <https://www.jetbrains.com/help/ai-assistant/about-ai-assistant.html>

## 下一步补充清单

1. 逐个补全 Cursor / Windsurf / Cody / Amazon Q Developer 的官方文档证据。
2. 增加“定价对比表（个人/团队/企业）”。
3. 增加“同一任务基准对比”（例如：修复 bug、跨文件重构、PR 安全审查）。
