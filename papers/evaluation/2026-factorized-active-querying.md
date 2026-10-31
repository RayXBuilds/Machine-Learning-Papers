---
id: factorized-active-querying
primary_topic: evaluation
tags: [active-evaluation, confidence-intervals, language-models]
type: paper
added: 2026-10-31
verified: 2026-10-31
source: https://arxiv.org/abs/2601.20251
status: summary
---

# Efficient Evaluation of LLM Performance with Statistical Guarantees

- 作者：Skyler Wu、Yash Nair、Emmanuel J. Candès。
- 年份与版本：2026-01-28 首次提交，2026-10-29 更新至 arXiv v4；预印本，未核实会议或期刊接收信息。
- 原始来源：[书目与摘要](https://arxiv.org/abs/2601.20251) · [v4 正文](https://arxiv.org/html/2601.20251v4)。
- 官方代码：[skbwu/efficiently-evaluating-llms](https://github.com/skbwu/efficiently-evaluating-llms)；已核对代码与数据入口，未运行。

## 解决的问题

给定固定题库和有限调用预算，如何估计语言模型准确率，并为估计值提供可信的置信区间？

## 主要方法

Factorized Active Querying（FAQ）用贝叶斯因子模型提取历史答题信息，结合方差缩减与主动学习选择下一道题；Pro-Active Inference（PAI）处理自适应抽样下的有限总体推断，在正则条件下保持渐近频率学覆盖率。

## 贡献与局限

作者在两个基准套件及不同历史数据缺失程度下检验查询效率。保证是渐近的，不等于任意小样本下的精确覆盖；调参还需额外验证查询。没有历史、可迁移信息或其他预测线索时，不应期待优于均匀抽样。当前讨论固定题库的二元结果。[讨论与局限](https://arxiv.org/html/2601.20251v4#S6)

已核对方法概述和讨论，未逐项审阅证明或复现实验。

## 前置知识与阅读重点

了解置信区间、有限总体抽样和潜因子模型。重点区分预测模型用于省查询与推断程序用于保证覆盖的职责，并核对正则条件与总查询成本。

## 收录理由

补充低预算评估的统计依据，可与侧重候选筛选的 [EvalAlloc](2026-evalalloc.md) 对照阅读。

## 相关主题与版本

arXiv ID：`2601.20251`；[arXiv DOI](https://doi.org/10.48550/arXiv.2601.20251)。文件年份采用首次预印本年份；近期事件是 v4 修订，本库为首次收录。主文件归评估，以 language-models 标签关联 NLP。
