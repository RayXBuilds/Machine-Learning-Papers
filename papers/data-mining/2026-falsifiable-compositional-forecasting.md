---
id: falsifiable-compositional-forecasting
primary_topic: data-mining
catalog_year: 2026
subtopic: "时序预测与验证"
updated: 2026-11-24
tags: [time-series, time-series-validation, distribution-shift]
type: paper
added: 2026-11-24
verified: 2026-11-24
source: https://arxiv.org/abs/2611.25388v1
status: summary
---

# Falsifiable Compositional Reasoning in Time Series Forecasting

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Hao Xue
- 年份与版本：arXiv v1 于 2026-11-19 提交，按预印本年份归档。正式发表状态未核实。
- 原始来源：[arXiv 书目和版本记录](https://arxiv.org/abs/2611.25388v1)
- 仓库内 PDF：[打开原文](../../pdfs/data-mining/2026-falsifiable-compositional-forecasting.pdf)（v1，10 页）。
- 官方代码：本次从论文及其书目页未核实作者发布的代码链接。

## 解决的问题

若两个影响价格的因素在整段历史中总是一起变化，模型即使通过按时间切分的验证，也可能无法区分哪个因素在起作用。等到两者分开变化，原本得分最好的模型还可靠吗？

## 主要方法

作者把预测拆成若干基本成分及其组合关系，并要求提前写明关系在什么条件下成立、哪些观测足以推翻它。检验阈值用训练期数据校准。实验用可控制成分相关性的合成序列和德国日前电价，对照端到端预测、规则搜索，以及有无失效检验的组合模型。

## 贡献与局限

作者报告，在所研究的分布转变中，扩大候选模型的搜索范围没有改善新环境下的准确度；单纯拆分成分也可能失效。读这些结果要区分两类证据：合成数据允许研究者指定哪种关系改变了，真实电价的数据切分只能检验该次转变上的表现。

## 前置知识与阅读重点

熟悉按时间顺序留出验证集和分布偏移即可。读实验图时，先找阈值是在哪段数据上确定的，再比较转变前后的触发率和预测误差。若看到测试结果后才决定什么算失效，便无法用同一段测试验证这条规则。

## 收录理由

这篇文章为回测设计补上一道检查：除了报告历史误差，还可以在预测前写下模型依赖的关系，以及承认这条关系失效所需的证据。

## 相关主题与版本

[配套阅读：已知事件如何改变预测](2026-loki-event-effects.md) · [跨序列验证](2026-series-wise-cross-validation.md)。本导读依据上述 v1 整理，未复现实验。
