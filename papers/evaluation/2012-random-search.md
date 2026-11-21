---
id: random-search
primary_topic: evaluation
tags: [hyperparameters, experimental-design]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://jmlr.org/papers/v13/bergstra12a.html
status: summary
catalog_year: 2012
subtopic: "实验设计与数据有效性"
updated: 2026-11-21
---

# Random Search for Hyper-Parameter Optimization

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：James Bergstra、Yoshua Bengio
- 年份与版本：JMLR 13，2012 年。
- 原始来源：[论文入口](https://jmlr.org/papers/v13/bergstra12a.html)
- 官方代码：在本次核对的一手来源中未确认论文配套实现。

- 仓库内 PDF：[打开全文](../../pdfs/evaluation/2012-random-search.pdf)（JMLR 期刊版）。

## 解决的问题

给定固定训练预算，当只有少数超参数强烈影响结果时，网格能试到多少种真正不同的配置？

## 主要方法

在同一搜索空间独立抽样超参数，将预算投影到重要维度上，与规则网格的重复取值比较，并用模型调参实验检验。

## 贡献与局限

论文说明随机搜索应成为比较自适应搜索算法的基线。效率取决于搜索范围与抽样分布，参数的重要性也随数据集变化。

## 前置知识与阅读重点

先理解验证集与对数尺度。画出二维网格以及同样多的随机点，再把两组点分别投影到一个轴。

## 收录理由

为阅读调参论文提供一个成本可对齐的实验基线。

## 相关主题与版本

[主主题：评估与实验方法](README.md) · [延伸主题：传统机器学习](../classical-ml/README.md)

本条依据原始书目和论文内容整理，未复现实验。
