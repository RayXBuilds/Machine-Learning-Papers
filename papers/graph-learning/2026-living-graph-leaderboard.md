---
id: living-graph-leaderboard
primary_topic: graph-learning
tags: [benchmarking, evaluation, reproducibility]
type: paper
added: 2026-11-05
verified: 2026-11-05
source: https://arxiv.org/abs/2611.03433
status: summary
---

# A Living Leaderboard for Graph Machine Learning

- 作者为 Martin Ritzert。
- 年份与版本采用 2026-11-02 首次提交的 arXiv v1，状态为预印本。会议或期刊接收信息待核实。
- 原始来源包含书目页和 v1 正文。[书目与摘要](https://arxiv.org/abs/2611.03433) · [正文](https://arxiv.org/html/2611.03433v1)
- 官方代码仓库及榜单均可访问。本次核对了仓库 README 和站点首页，运行验证与实验复现待开展。[代码](https://github.com/martinalex000/benchmarking_website) · [榜单](https://graphlearningbenchmarks.github.io/)

## 解决的问题

图学习论文使用的数据集、基线及调参方式各异，分散的结果使读者难以判断新模型的优势是否经得起已有强基线的比较。

## 主要方法

通过候选筛选、数据集识别、表格选择和结果提取，将论文报告的成绩按数据集组织。系统记录来源与模型类别，提供筛选表和随时间变化的最佳成绩曲线，并突出 GCN、MLP 等基线。正文描述了任务匹配和特殊评估设置的过滤规则。[方法第 2 节](https://arxiv.org/html/2611.03433v1)

## 贡献与局限

论文将持续维护的结果索引与图学习基准审计结合。作者分析使用截至 2026-10-15 的快照，涵盖 885 篇同行评审论文、111 个数据集及 27,723 条合格提取结果。在线榜单持续更新，引用统计时应保留快照日期。

自动提取可能出错，协议差异也可能导致不可比成绩被合并。统计比较在重复次数缺失时假定四次运行，并采用未经多重比较校正的检验，阅读基线差距结论时需结合这些条件。已核对方法与局限，逐项结果审计和实验复现待开展。[分析与局限](https://arxiv.org/html/2611.03433v1)

## 前置知识与阅读重点

了解 GCN、节点和图级任务、数据划分及均值与标准差。重点核对同名数据集的协议、指标和调参预算，沿来源链接检查表格，并比较简单基线与新架构的表现。

## 收录理由

扩展图学习主题的实验方法内容，为选择基线和核查文献成绩提供入口，可接续 GCN 基础导读阅读。[GCN 导读](2017-gcn.md)

## 相关主题与版本

arXiv ID 为 `2611.03433`，文件年份采用首次预印本年份。来源页列出的 DOI 为 `10.48550/arXiv.2611.03433`，检索时标记 pending registration，注册完成状态待核实。按图学习专用基准归入图学习，以 evaluation 标签关联评估主题。
