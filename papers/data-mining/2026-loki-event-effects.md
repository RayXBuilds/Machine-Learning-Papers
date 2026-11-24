---
id: loki-event-effects
primary_topic: data-mining
catalog_year: 2026
subtopic: "时序预测与验证"
updated: 2026-11-24
tags: [time-series, event-aware-forecasting, exogenous-variables]
type: paper
added: 2026-11-24
verified: 2026-11-24
source: https://arxiv.org/abs/2611.27191v1
status: summary
---

# Lift Out, Kick In: Decoupling Event Effects for Time Series Forecasting

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Yunying Zhu、Zichun Cao、Siwei Sun、Xiaocen Guo、Shengsheng Lin、Jing Hu、Enyun Yu、Zhichao Zou
- 年份与版本：arXiv v1 于 2026-11-20 提交，按预印本年份归档。正式发表状态未核实。
- 原始来源：[arXiv 书目和版本记录](https://arxiv.org/abs/2611.27191v1)
- 仓库内 PDF：[打开原文](../../pdfs/data-mining/2026-loki-event-effects.pdf)（v1，39 页）。
- 官方代码：本次从论文及其书目页未核实作者发布的代码链接。

## 解决的问题

节日带来的客流高峰可能落在训练窗口里，也可能落在预测窗口里。若模型把上一次高峰当成持续趋势，或者忽略下一次节日，两种情况下都会预测失准。

## 主要方法

Loki 学习一个共享的事件响应函数。它根据事件类型和相对事件时刻估计序列相对基线的变化，在历史窗口先消去这部分影响，让时序模型外推基线；到预测窗口，再根据当时已知的日程，用同一函数把事件影响施加到基线预测上。

## 贡献与局限

作者报告，Loki 在五个基准的标准化平均绝对误差上均优于所比较的基线。方法依赖两个条件：预测时已掌握事件日程，同类事件的响应有可复用的规律。对首次发生、事前未知的冲击，论文的实验不能给出同样保证。

## 前置知识与阅读重点

先了解外生变量和滚动预测。读消融实验时，分别看只处理历史事件、只处理未来事件、两个窗口各用一套响应函数的结果。这三个对照能区分收益来自事件信息本身，还是来自跨窗口共享参数。

## 收录理由

这项工作把使用节假日等已知信息的方式说得很具体。读者可以据此检查自己的预测流程：历史窗口和未来窗口中的事件是否用同一种方式表示？

## 相关主题与版本

[配套阅读：历史回测何时会选错模型](2026-falsifiable-compositional-forecasting.md) · [跨序列验证](2026-series-wise-cross-validation.md)。本导读依据上述 v1 整理，未复现实验。
