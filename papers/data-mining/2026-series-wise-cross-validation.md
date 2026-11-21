---
id: series-wise-cross-validation
primary_topic: data-mining
tags: [time-series, cross-validation, forecasting, model-selection]
type: paper
added: 2026-11-20
verified: 2026-11-20
source: https://arxiv.org/abs/2611.08252
status: summary
catalog_year: 2026
subtopic: "时序预测与验证"
updated: 2026-11-21
---

# Series-wise Cross-validation for Global Time Series Forecasting

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Vitor Cerqueira、Mariana Oliveira、Luis Roque。
- 年份与版本：2026 按预印本 v1 年份，首次提交于 2026-11-05（UTC），核对时为 v1。未核实会议或期刊接收信息。
- 原始来源：[arXiv 书目](https://arxiv.org/abs/2611.08252) · [v1 正文](https://arxiv.org/html/2611.08252v1)。
- 官方代码：[experiments-tscv](https://github.com/vcerqueira/experiments-tscv)，论文提供的实验仓库。本库未运行代码。

- 仓库内 PDF：[打开全文](../../pdfs/data-mining/2026-series-wise-cross-validation.pdf)（arXiv 2611.08252v1）。

## 解决的问题

全局预测模型同时学习多条时间序列。仅沿时间切分，能否反映模型对新序列的泛化能力？论文研究按序列及时间双重划分的交叉验证。[摘要](https://arxiv.org/abs/2611.08252)

## 主要方法

训练使用一组序列的历史，验证使用另一组序列的未来，同时保留时间顺序。作者在 11 个数据集、10 种神经网络架构上比较多种划分方法，分别考察误差估计和模型选择。[基准设计](https://arxiv.org/html/2611.08252v1)

## 贡献与局限

作者报告：测试出现新序列时，按序列划分更有利于下游预测，按时间划分对误差量级估计略优。序列群体固定时，按时间划分也更适合下游准确率。多折方案增加训练成本，嵌套验证内层采用简化的时间划分，更多分布漂移情形尚待检验。[讨论与结论](https://arxiv.org/html/2611.08252v1)

## 前置知识与阅读重点

建议了解全局时序模型、嵌套交叉验证与模型选择。重点检查训练未见序列的比例、时间边界和调参预算，区分估计误差与选出好模型两个目标。

## 收录理由

虽早于近七日窗口，仍可补充时序专题的验证设计案例，帮助按部署场景选择数据划分方式。

## 相关主题与版本

- arXiv ID：`2611.08252`。书目页列 DOI `10.48550/arXiv.2611.08252`，注明待注册。
- 主文件归入[数据挖掘与数据管理](README.md)，相关方向为[评估与实验方法](../evaluation/README.md)。
- 本条核对书目、实验设计、讨论及官方代码入口，未进行全文精读或实验复现。
