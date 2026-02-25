# VibeCoding / AI Coding / AI Review 工具评测库

```{note}
这份文档已经拆分为“总览 + 方法论 + 工具目录 + 单工具页”。
你可以在每个工具的独立页面里持续维护详细评价与功能列表。
```

```{contents}
:local:
:depth: 2
```

## 导言：AI Coding 市场正在从“工具实验”走向“生产基础设施”

过去两年，AI Coding 已从开发者的“效率插件”快速演进为软件生产链路中的核心能力。结合公开数据看，市场变化主要体现在四个层面：

1. **渗透率快速上升，使用频率显著提高**

- 第三方统计显示，美国开发者中有高比例用户已进入高频使用阶段（如“日用”），全球开发者周级使用也在扩大。
- 在企业端，头部组织已将 AI Coding 纳入常规研发流程，而非仅用于 PoC。

1. **市场规模进入高增长区间，但结构分化明显**

- 第三方统计口径给出的“vibe coding 平台市场”已达十亿美元级，并给出 2027 年前的高增长预测。
- 增长并非均匀分布：企业平台、个人开发者工具、no-code/low-code 三类子市场增长驱动不同，采购逻辑与定价弹性也不同。

1. **“多模型 + 代理化（agentic）”成为主流形态**

- OpenRouter 的大规模平台行为研究显示：真实工作负载正从单轮问答转向更长上下文、更多推理、更多工具调用。
- 该研究还显示编程相关请求占比持续上升，说明 AI Coding 正在从“能写代码”走向“能在真实工程上下文中持续完成任务”。

1. **效率红利与治理成本同步上升**

- 一方面，团队在样板代码、集成类任务、常规开发流程中获得显著效率提升。
- 另一方面，代码质量一致性、安全、版权与可审计性压力上升，组织需要补齐策略、评审、扫描与权限治理能力。

综合来看，AI Coding 市场已进入“规模化落地阶段”：竞争焦点不再只是模型能力本身，而是 **工作流整合能力、代理编排能力、治理与合规能力、以及跨工具生态兼容能力**。

```{note}
数据口径说明（建议阅读时一并参考）：
1. <https://openrouter.ai/state-of-ai> 反映的是 OpenRouter 平台上的真实调用行为（Token/类别/地域/工具调用等），是“平台观察样本”，并非全行业普查。
2. <https://www.secondtalent.com/resources/vibe-coding-statistics/> 为第三方汇编统计，适合用于市场趋势参考；具体数值可能随样本、时间窗口和引用来源更新而变化。
3. 本仓库在对比工具时，优先关注“趋势方向 + 口径一致性”，避免将不同来源的单点数值做直接横向等价比较。
```

## 导言数据来源

- OpenRouter, *State of AI*: <https://openrouter.ai/state-of-ai>
- SecondTalent, *Top Vibe Coding Statistics & Trends [2026]*: <https://www.secondtalent.com/resources/vibe-coding-statistics/>

## 快速入口

```{toctree}
:maxdepth: 2
:caption: 总览

overview/landscape
overview/comparison
overview/china-tools
```

```{toctree}
:maxdepth: 2
:caption: 工具档案

tools/index
```

```{toctree}
:maxdepth: 2
:caption: 评测资产

templates/tool-review-template
research/sources
research/todo
```

## 维护约定

1. 优先引用官方文档、官方仓库与官方价格页。
2. 每个工具结论都沉淀到独立页面，避免主页面无限膨胀。
3. 评测新增内容优先写在“功能列表 + 详细评价 + 证据链接”三块。

```{important}
如果某工具官网是动态渲染，先在“证据链接”中记录可抓取的官方入口，再补充结论。
```
