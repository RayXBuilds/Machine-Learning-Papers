---
id: isolation-forest
primary_topic: data-mining
tags: [anomaly-detection, random-trees]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://research.monash.edu/en/publications/isolation-forest/
status: summary
catalog_year: 2008
subtopic: "异常检测"
updated: 2026-11-21
---

# Isolation Forest

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Fei Tony Liu、Kai Ming Ting、Zhi-Hua Zhou
- 年份与版本：2008 年，IEEE International Conference on Data Mining（ICDM 2008）, 413–422。
- 原始来源：[原文](https://research.monash.edu/en/publications/isolation-forest/)
- 官方代码：核对的原始资料中未确认论文配套实现。

- 仓库内 PDF：[打开全文](../../pdfs/data-mining/2008-isolation-forest.pdf)（作者机构公开稿（ICDM 2008））。

## 解决的问题

在缺少异常标签时，能否直接判断一个点有多容易被隔离？

## 主要方法

在子样本上随机选择特征与切分值生成树，对一个点在多棵树中的隔离路径长度取平均并归一化。

## 贡献与局限

稀少且取值特殊的点常经较少切分就被隔离。若异常只体现在复杂的特征组合上，单轴切分未必产生短路径。

## 前置知识与阅读重点

了解二叉树后，画一个稠密点团和一个远点，比较随机阈值隔离它们所需的切分次数。

## 收录理由

阐明同样使用随机树，异常打分与监督分类为何采用不同的训练和输出方式。

## 相关主题与版本

[DOI 10.1109/ICDM.2008.17](https://doi.org/10.1109/ICDM.2008.17)。延伸阅读见[随机森林](../classical-ml/2001-random-forests.md)。

核对范围为书目信息与方法概要，未做实验复现。
