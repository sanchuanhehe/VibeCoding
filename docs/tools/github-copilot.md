# GitHub Copilot

> _本工具是笔者常用的工具,笔者认为github的策略非常开放,只要是能够在保证ai驱动的前提下,无论是谁家的模型,都可以接入_

## 工具定位

- 定位：覆盖 GitHub + IDE + CLI 的全栈 AI coding/agent 平台
- 入口：GitHub.com / IDE / CLI / Terminal / 移动端

## 功能列表

```{list-table}
:header-rows: 1

* - 能力
  - 状态
  - 说明
* - 代码补全
  - ✅
  - IDE 内联补全，支持多 IDE
* - Chat / 问答
  - ✅
  - 支持在 GitHub、IDE、CLI 等入口对话
* - GitHub 内 PR/代码流程
  - ✅
  - 可生成 PR 变更描述、在仓库与 PR 场景提问
* - Coding Agent
  - ✅
  - 可分配任务给 agent，自动产出代码与 PR
* - Agent Management
  - ✅
  - 提供 Agents 视图集中查看会话、日志、中途 steering
* - Agent HQ（Agents 页面）
  - ✅
  - 提供集中控制台，用于统一启动、切换、跟踪多个 agent 会话
* - Skills 支持
  - ✅
  - 支持 `project skills` 与 `personal skills`，采用开放 Agent Skills 规范
* - Custom Agents
  - ✅
  - 通过 agent profile 定义提示词、可用 tools、可用 MCP servers
* - Subagent / 多代理协作
  - ✅
  - 支持第三方 agents 与 custom agents 共同参与任务分派与执行
* - 插件/集成支持
  - ✅
  - 支持与 Teams/Slack/Linear/Azure Boards 集成触发 coding agent
* - MCP 支持
  - ✅
  - 支持连接 MCP server；支持企业/组织级 registry 与 allowlist 策略
* - 模型与选模
  - ✅
  - 支持手动选模与 Auto model selection（受计划与策略约束）
* - 企业治理
  - ✅
  - 支持 seat、策略、配额、模型访问与 MCP 访问控制
```

## 细颗粒度管理（重点）

- Skills 粒度：支持仓库级 `/.github/skills`、`/.claude/skills`，以及个人级 `~/.copilot/skills`、`~/.claude/skills`。
- Agent 粒度：可在 agent session 中实时 steering，并可在 GitHub 与本地（VS Code/CLI）之间切换继续执行。
- Subagent 粒度：可按任务选择 Copilot、第三方 agents 或自定义 agents，形成“主 agent + 专项 agent”协作模式。
- Tool 粒度（产品层）：custom agent profile 可显式限定 `tools`，默认可访问内建与 MCP 工具。
- MCP 粒度（企业层）：可配置 MCP Registry URL，并在 `Allow all` 与 `Registry only` 间切换。
- 模型粒度：管理员策略可排除模型；Auto 模式会在可用模型集合中自动选择。
- 配额粒度：premium requests 按计划计量，支持额外预算控制。

## Agent HQ（重点补充）

- 定义：通常可理解为 GitHub Copilot 的 Agents 中枢页面（Agents page + 仓库内 Agents tab）。
- 入口：仓库内 Agents tab，或全局页面 `https://github.com/copilot/agents`。
- 核心能力：
  - 发起新任务并选择模型/agent（含第三方 agent 与 custom agent）。
  - 查看实时 session 日志与进度，跟踪并发运行任务。
  - 会话中途 steering（不中断任务追加指令）。
  - 将会话转到本地继续（Open in VS Code / Continue in Copilot CLI）。
  - 回到 PR 完成审阅与合并闭环。
- 管理价值：把“任务分派—过程可视—中途干预—结果回收”收敛到一个控制平面，降低多 agent 并行时的管理成本。

## 源码侧补充（vscode-copilot-chat 参考）

- Skills 解析与启用列表：`remoteAgents.ts` 中存在 `ListSkills`、`resolveCopilotSkills`、`getPlatformAgentSkills` 实现。
- MCP 扩展接入：`GitHubMcpContrib` 通过 `registerMcpServerDefinitionProvider('github', ...)` 注册 GitHub MCP provider。
- MCP 安装流：`McpSetupCommands` 提供 `validatePackage`、`setup.flow` 等命令流程（含遥测与校验）。
- 工具治理约束：`languageModelAccess.ts` 对 tool 请求做限制（如工具数量上限、`Required` 模式下单工具约束）。
- 扩展级风控：`BlockedExtensionService` 支持对高频/异常扩展做临时阻断。
- 工具体系设计：`docs/tools.md` 明确 `languageModelTools`、`toolsets`、model-specific tools 与危险工具确认流程。

## 适合场景

- 既要 GitHub 内协作（Issue/PR/Review），又要 IDE/CLI 一体 agent 能力的团队
- 需要企业级策略治理（模型、MCP、席位、配额）的大中型团队

## 主要限制/注意点

- 关键能力受计划影响（Free/Pro/Pro+/Business/Enterprise）。
- Skills、Custom Agents、MCP 与部分 IDE 能力存在预览项，策略与可用性可能调整。
- 第三方集成与插件能力需要额外配置，且可能涉及额外许可证。

## 详细评价

### 优势

- GitHub 原生工作流结合最深（代码、PR、Issue、Agent 会话统一）。
- 能力覆盖广：补全、Chat、Agent、Skills、Custom Agents、MCP、企业治理。
- 工具与策略具备较好的分层管理能力，适合规模化落地。
- 即有cli,也有ide,同时支持agent hq,以及外部模型提供商支持(支持BYOK),最开放且功能全的一款

### 局限

- 不同计划、IDE 与预览阶段能力差异较大，需要按团队版本逐项核对。
- 若团队不在 GitHub 主工作流中，部分优势难以完全发挥。

## 证据链接

- 官方总览：<https://docs.github.com/en/copilot>
- 功能与入口：<https://docs.github.com/en/copilot/get-started/what-is-github-copilot>
- Agent 管理：<https://docs.github.com/en/copilot/concepts/agents/coding-agent/agent-management>
- Agent HQ 页面：<https://github.com/copilot/agents>
- 第三方 Agents：<https://docs.github.com/en/copilot/concepts/agents/about-third-party-agents>
- Skills：<https://docs.github.com/en/copilot/concepts/agents/about-agent-skills>
- Custom Agents：<https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-custom-agents>
- Integrations（插件/集成）：<https://docs.github.com/en/copilot/concepts/tools/about-copilot-integrations>
- MCP 访问控制：<https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-mcp-usage/configure-mcp-server-access>
- Auto model selection：<https://docs.github.com/en/copilot/concepts/auto-model-selection>
- 商业页：<https://github.com/features/copilot>
- 源码（skills）：<https://github.com/microsoft/vscode-copilot-chat/blob/main/src/extension/conversation/vscode-node/remoteAgents.ts>
- 源码（MCP provider）：<https://github.com/microsoft/vscode-copilot-chat/blob/main/src/extension/githubMcp/vscode-node/githubMcp.contribution.ts>
- 源码（MCP setup）：<https://github.com/microsoft/vscode-copilot-chat/blob/main/src/extension/mcp/vscode-node/commands.ts>
- 源码（tools 限制）：<https://github.com/microsoft/vscode-copilot-chat/blob/main/src/extension/conversation/vscode-node/languageModelAccess.ts>
- 源码（扩展阻断）：<https://github.com/microsoft/vscode-copilot-chat/blob/main/src/platform/chat/common/blockedExtensionService.ts>
- 源码（工具体系说明）：<https://github.com/microsoft/vscode-copilot-chat/blob/main/docs/tools.md>
