---
id: discrimination-calibration-ranking
primary_topic: evaluation
tags: [calibration, ranking-metrics, multilabel-learning]
type: paper
added: 2026-11-04
verified: 2026-11-04
source: https://arxiv.org/abs/2611.02215
status: summary
---

# Discrimination, Calibration, and Ranking: A Unified Matrix Framework

- 作者：Ronaldo Cristiano Prati、Farangis Johari。
- 年份与版本：2026-11-01 首次提交，arXiv v1；预印本，未核实会议或期刊接收信息。
- 原始来源：[书目与摘要](https://arxiv.org/abs/2611.02215) · [v1 正文](https://arxiv.org/html/2611.02215v1)。
- 官方代码：[rcprati/discrimination-calibration-ranking](https://github.com/rcprati/discrimination-calibration-ranking)；已读取 README，确认 Lean 证明、实验脚本与结果文件的说明，未运行构建或实验。

## 解决的问题

分类器的区分能力、概率质量和排序表现衡量不同性质。如何用一致的表示比较这些指标，并解释按类别、样本或全局聚合时的差异？

## 主要方法

以标签和预测矩阵为基础，在已有分类指标算子之外，引入偏差算子及依赖排序或切片的算子，沿用 micro、macro、exemplar 三种聚合方式。统一按单元损失平均时，三种 Brier 聚合相等；归一化后的 nDCG 则未必如此。[框架与聚合定义](https://arxiv.org/html/2611.02215v1)

## 贡献与局限

提供连接多类指标的代数视角，帮助区分评分规则与排序规则。两个多标签基准用于展示指标差异，并非对所有任务的效果验证。编者提醒：Brier 同时涉及可靠性与分辨能力，不能把总分直接等同于纯校准误差；聚合等式依赖文中归一化与权重定义。

作者公开了部分结果的 Lean 形式化；仓库明确列出未形式化内容及较窄命题范围，不能视为全文已获机器验证。已核对摘要、相关聚合定义和代码说明，未逐项审阅证明或复现。

## 前置知识与阅读重点

了解混淆矩阵、Brier 分数、AUC、nDCG 及多标签评估。重点追踪分母和聚合轴，区分文中 micro-AUC 与 pooled ROC-AUC，并理解排序不变时概率质量仍可能改变。

## 收录理由

补充概率校准专题的指标基础，适合与 [Temperature Scaling](2017-temperature-scaling.md) 对照，先明确评价对象，再讨论校准方法。

## 相关主题与版本

arXiv ID：`2611.02215`；页面列出的 DOI 为 `10.48550/arXiv.2611.02215`，检索时标注 pending registration，未单独确认注册完成。年份采用首次预印本年份，主文件归评估，通过 ranking-metrics 标签关联排序任务。
