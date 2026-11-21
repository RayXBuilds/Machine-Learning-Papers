---
id: backpropagation
primary_topic: deep-learning
tags: [optimization, representation-learning]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://www.cs.toronto.edu/~hinton/absps/naturebp.pdf
status: summary
catalog_year: 1986
subtopic: "网络训练与优化"
updated: 2026-11-21
---

# Learning representations by back-propagating errors

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：David E. Rumelhart、Geoffrey E. Hinton、Ronald J. Williams
- 年份与版本：1986 年，Nature 323, 533–536。
- 原始来源：[原文](https://www.cs.toronto.edu/~hinton/absps/naturebp.pdf)
- 官方代码：核对的原始资料中未确认论文配套实现。

- 仓库内 PDF：[打开全文](../../pdfs/deep-learning/1986-backpropagation.pdf)（Nature 323 (1986)，论文自扫描首页第 533 页下半页开始）。

## 解决的问题

输出带有监督信号时，隐藏单元应怎样调整才能学到适合任务的表示？

## 主要方法

前向计算各单元活动，再由输出层反向传递误差导数。链式法则把同一隐藏单元经过多条路径的影响合并起来。

## 贡献与局限

作者用小型网络展示了隐藏表示的形成。梯度提供局部下降方向，训练结果仍取决于目标和优化过程。

## 前置知识与阅读重点

先复习复合函数求导。挑一个连到两个输出的隐藏单元，检查它的梯度为何含有两个加项。

## 收录理由

为阅读深层网络的优化论文建立梯度计算的共同起点。

## 相关主题与版本

[DOI 10.1038/323533a0](https://doi.org/10.1038/323533a0)。延伸阅读见[深度自编码器](2006-deep-autoencoder.md)。

核对范围为书目信息与方法概要，未做实验复现。
