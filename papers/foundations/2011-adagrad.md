---
id: adagrad
primary_topic: foundations
tags: [online-learning, optimization]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://jmlr.org/papers/v12/duchi11a.html
status: summary
catalog_year: 2011
subtopic: "正则化、优化与学习理论"
updated: 2026-11-21
---

# Adaptive Subgradient Methods for Online Learning and Stochastic Optimization

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：John Duchi、Elad Hazan、Yoram Singer
- 年份与版本：JMLR 12，2011 年；本文采用期刊版。
- 原始来源：[论文入口](https://jmlr.org/papers/v12/duchi11a.html)
- 官方代码：在本次核对的一手来源中未确认论文配套实现。

- 仓库内 PDF：[打开全文](../../pdfs/foundations/2011-adagrad.pdf)（JMLR 期刊版）。

## 解决的问题

在线更新中，不同坐标的出现频率与梯度尺度相差很大，统一步长可能淹没稀有特征。

## 主要方法

用历史次梯度构造随时间变化的近端几何。对角形式累计各坐标的梯度平方，用其平方根缩放新一步更新。

## 贡献与局限

原文给出依赖观测梯度的遗憾界。对角形式忽略坐标间相关性，凸优化分析也有明确的损失函数条件。

## 前置知识与阅读重点

先理解在线凸优化和遗憾。对照全矩阵与对角版本的更新式，再跟踪长期为零的坐标第一次出现时的有效步长。

## 收录理由

帮助区分 AdaGrad 的历史累积和 Adam 的指数滑动平均。

## 相关主题与版本

[主主题：数学、学习理论与概率模型](README.md) · [延伸主题：深度学习与表征学习](../deep-learning/README.md)

本条依据原始书目和论文内容整理，未复现实验。
