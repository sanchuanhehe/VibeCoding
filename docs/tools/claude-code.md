---
tool: "Claude Code"
website: "https://claude.ai/code"
docs: "https://code.claude.com/docs/en"
verified_date: ""
verified_by: ""
---

# Claude Code

> ai coding agent，提供多端一致的 agentic coding 体验，支持跨文件、命令执行、MCP 等guo能力。作为业界最先进的领军者,定义着agent工具的形态和终端体验,是目前生态最好,功能最全的agent工具之一

## 工具定位

- 定位：Agentic coding
- 入口：Terminal / VS Code / JetBrains / Desktop / Web

## 功能列表

```{list-table}
:header-rows: 1

* - 能力
  - 状态
  - 说明
* - 代码库级操作
  - ✅
  - 支持跨文件任务执行
* - 命令执行
  - ✅
  - 终端工作流能力
* - MCP
  - ✅
  - 可扩展外部工具,是mcp协议的定义者
* - 自动化集成
  - ✅
  - 可接入 CI 流程、支持与GitHub Actions或GitLab CI/CD集成
* - 自动化常规任务
  - ✅
  - 可自动执行各种重复性任务
* - 构建特性与修复Bug
  - ✅
  - 能够理解代码库内容进行跨文件编辑解决问题
* - 版本控制辅助
  - ✅
  - 能够自动创建 Commits 和 Pull Requests
* - Agent团队与自定义Agent
  - ✅
  - 支持运行Agent团队，并通过 Agent SDK 构建自定义 Agent 工作流
* - 记忆与指令管理
  - ✅
  - 支持通过 CLAUDE.md 文件持久化指令以及自动记忆 (Auto memory)
* - 管道与脚本自动化
  - ✅
  - CLI 支持管道操作(Pipe)与脚本自动化
* - SKILLS
  - ✅
  - 支持技能库管理，包含个人和项目级别,是agent技能库规范的定义者

```

## 核心概念与工作原理

基于官方文档 [How Claude Code works](https://code.claude.com/docs/en/how-claude-code-works)，Claude Code 有以下核心运作机制：

1. **Agentic Loop (代理循环)**
   Claude Code 的核心是通过“模型推理”和“工具调用”组成的循环。每次任务都会经历三个可重叠的阶段：**收集上下文 (gather context)**、**采取行动 (take action)** 和 **验证结果 (verify results)**。用户可以随时中断并纠正它的路线。

2. **核心工具集 (Built-in Tools)**
   Claude Code 依赖五类基础工具来实现代理能力，包括：
   - 文件操作 (File operations)：读写、创建、重命名等。
   - 搜索 (Search)：模式检索、正则搜索、代码库探索。
   - 执行 (Execution)：运行 shell 命令、启动服务、运行测试、使用 git。
   - Web与网络：搜索网页、抓取文档。
   - 代码智能 (Code intelligence)：修改后查看类型错误警告、跳转定义、查找引用等。

3. **访问权限 (What Claude can access)**
   环境在执行时被赋予访问特定上下文的能力，包括：整个项目目录的文件、执行任意终端命令的能力、检测当前 Git 状态、读取 `CLAUDE.md` 获取自定义项目指令，以及利用“自动记忆 (Auto memory)”记录项目模式。

4. **会话与上下文管理 (Sessions & Context)**
   - 每个对话被称为一个 Session（会话），与所在目录绑定。切换 Git 分支后，Claude 虽然看到了新分支的代码，但对话记忆得以保留。
   - 提供 `--fork-session`，使用户可以在历史节点上开辟新的对话分支尝试不同方案。
   - 具有上下文上限管理功能，通过总结旧工具输出来自动清理上下文；也可通过 Subagents 和 Skills 控制上下文成本。

5. **安全与权限控制 (Checkpoints & Permissions)**
   - **Checkpoints**: 文件编辑前自动快照。若代码改坏了，可以通过连按双击 `Esc` 键或告知它 Undo 来回滚修改。
   - **Permissions**: 通过按 `Shift+Tab` 键切换交互模式，涵盖三种权限状态（每次都询问、文件可自动编辑但命令需要询问、纯只读计划模式 Plan mode)；在配置文件中也可以全局信任特定的命令（如 npm test）。

## 拓展生态 (Extension Ecosystem)

> 对于开发者生态来说,拓展是必不可少的一部分,不可拓展的工具证明是生态上的新手,而Claude Code在这方面的设计非常前瞻和全面,提供了从基础的技能库到复杂的Agent团队构建的全方位拓展能力,是目前市面上最成熟和灵活的agent工具生态之一

Claude Code 提供了一套灵活完整的拓展生态层 (Extension Layer) 来定制知识、连接外部服务并自动化工作流：

1. **CLAUDE.md & Auto memory**  
   - 每次对话都会加载的基础项目共识与规则设置。适合存放类似于 "使用 pnpm 而不是 npm" 或 "提交前运行测试" 这类的“常驻”要求。内容加载于会话启动时。

2. **Skills (技能)**  
   - 提供按需加载 (On-demand) 的参考知识与执行工作流。Skills 可以是教导大模型如何做特定事情的规则集合 (例如 API 规范设计指北)，亦或是具体的自动化动作。它既可以通过 `/deploy` 等方式手动触发，也可以由大模型自行判断调用。  

3. **Subagents (子智能体)**  
   - 隔离执行上下文的高级拓展能力。当大模型需要跨百个文件索引关键信息但不想污染当前对话的上下文空间时，它可以孵化一个 Subagent 独立开展工作，只由主对话接收到精华内容的任务总结。

4. **Agent Teams (智能体团队)**
   - 构建并协调平行开展独立工作的多个 Claude Code 会话队伍。例如：并行运行负责代码 Security 审计、性能检查及测试用例审查的各自 Subagents，多节点协作。  

5. **MCP (模型上下文协议 - Model Context Protocol)**  
   - 极其核心的连接层拓展能力。MCP 作为由 Anthropic 推出的规范，支持连接各种外部服务或数据库以丰富模型能力。MCP Server 服务内定义的各项能力，能够在每个 Request 中加载。

6. **Hooks (钩子)**  
   - 在特定事件（如每次文件编辑前后）触发的确定性脚本。在无需大模型介入的环节运行，可自动执行 `ESLint` 或其他本地外部逻辑。

7. **Plugins & Marketplaces (插件与市场)**  
   - 所有以上提到到 Skills、Subagents、MCP 和 Hooks 均可被统一打包 (Packaging Layer) 成为 Plugins（含有专门命名空间例如 `/my-plugin:review` 以避免冲突），并在各个项目之间复用或分享到市场供他人安装使用。

## 适合场景

- 需要“一套引擎多端一致体验”的团队

## 主要限制/注意点

- 高级能力常依赖订阅与账号体系；不同端能力细节有差异

## 详细评价

### 优势

- 多端统一，agent 能力完整。

### 局限

- 订阅与账号体系会影响可用能力。
- 国内很难订阅

## 证据链接

- <https://code.claude.com/docs/en>
