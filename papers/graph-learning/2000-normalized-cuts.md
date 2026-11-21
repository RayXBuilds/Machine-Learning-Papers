---
id: normalized-cuts
primary_topic: graph-learning
tags: [spectral-clustering, image-segmentation]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://people.eecs.berkeley.edu/~malik/papers/SM-ncut.pdf
status: summary
catalog_year: 2000
subtopic: "图划分与嵌入"
updated: 2026-11-21
---

# Normalized Cuts and Image Segmentation

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Jianbo Shi、Jitendra Malik
- 年份与版本：2000 年，IEEE Transactions on Pattern Analysis and Machine Intelligence 22(8), 888–905。采用扩展期刊版年份。
- 原始来源：[原文](https://people.eecs.berkeley.edu/~malik/papers/SM-ncut.pdf)
- 官方代码：[作者的 MATLAB 分割与聚类程序](https://www.cis.upenn.edu/~jshi/software/)

## 解决的问题

在带权像素图上怎样划分区域，才能减少单纯最小割切出孤立小块的倾向？

## 主要方法

用每一侧的连接总量归一化跨割权重，把离散划分松弛为广义特征值问题，再从连续解取得分割。

## 贡献与局限

归一化让割边代价具有相对尺度。松弛和离散化会产生近似误差，边权的设计也决定哪些差异可见。

## 前置知识与阅读重点

先认识邻接矩阵与度矩阵。用一条弱边连接两个稠密子图，比较切弱边与剥离单点的代价。

## 收录理由

用一个视觉问题把图划分目标、谱方法与聚类联系起来。

## 相关主题与版本

[DOI 10.1109/34.868688](https://doi.org/10.1109/34.868688)。延伸阅读见[Lloyd 量化](../classical-ml/1982-lloyd-quantization.md)。

核对范围为书目信息与方法概要，未做实验复现。
