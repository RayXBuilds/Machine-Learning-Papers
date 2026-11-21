---
id: local-probability-computations
primary_topic: foundations
tags: [graphical-models, exact-inference]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://doi.org/10.1111/j.2517-6161.1988.tb01721.x
status: summary
catalog_year: 1988
subtopic: "概率推断与图模型"
updated: 2026-11-21
---

# Local Computations with Probabilities on Graphical Structures and Their Application to Expert Systems

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：S. L. Lauritzen、D. J. Spiegelhalter
- 年份与版本：1988 年，Journal of the Royal Statistical Society, Series B 50(2), 157–224（含讨论）。
- 原始来源：[原文](https://doi.org/10.1111/j.2517-6161.1988.tb01721.x) · [期刊原文影印](https://www.eecis.udel.edu/~shatkay/Course/papers/Lauritzen1988.pdf)
- 官方代码：核对的原始资料中未确认论文配套实现。

## 解决的问题

已知一些变量的取值后，怎样在含条件依赖的系统中更新其他变量的概率？

## 主要方法

利用图的分解结构组织局部概率表，在团之间经共享变量传递边缘信息，使局部更新与整体模型一致。

## 贡献与局限

推断可以复用局部计算。构图和三角化决定团的大小，大团的联合状态空间仍会迅速膨胀。

## 前置知识与阅读重点

先理解条件独立与边缘化，再追踪一条新证据怎样跨过两个团的交集。

## 收录理由

为理解概率图模型的精确推断建立参照，也能解释后来为何需要近似推断。

## 相关主题与版本

[DOI 10.1111/j.2517-6161.1988.tb01721.x](https://doi.org/10.1111/j.2517-6161.1988.tb01721.x)。延伸阅读见[LDA 的变分近似](../nlp/2003-lda.md)。

核对范围为书目信息与方法概要，未做实验复现。
