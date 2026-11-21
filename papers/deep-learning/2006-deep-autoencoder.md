---
id: deep-autoencoder
primary_topic: deep-learning
tags: [dimensionality-reduction, pretraining]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://www.cs.toronto.edu/~hinton/absps/science.pdf
status: summary
catalog_year: 2006
subtopic: "表征与自监督"
updated: 2026-11-21
---

# Reducing the Dimensionality of Data with Neural Networks

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Geoffrey E. Hinton、Ruslan R. Salakhutdinov
- 年份与版本：2006 年，Science 313, 504–507。
- 原始来源：[原文](https://www.cs.toronto.edu/~hinton/absps/science.pdf)
- 官方代码：[作者提供的 MATLAB 训练程序](https://www.cs.toronto.edu/~hinton/MatlabForSciencePaper.html)

- 仓库内 PDF：[打开全文](../../pdfs/deep-learning/2006-deep-autoencoder.pdf)（Science 313，2006 年期刊排印版）。

## 解决的问题

怎样训练具有窄瓶颈的深层网络，使高维输入经压缩后仍可重构？

## 主要方法

逐层训练受限玻尔兹曼机以初始化权重，再展开为编码器与解码器，用反向传播联合优化重构。

## 贡献与局限

论文展示了非线性低维编码在所测数据上的重构优势。保留重构所需变化并不保证保留分类所需信号。

## 前置知识与阅读重点

熟悉 PCA 与反向传播后，区分逐层预训练时每层的目标和展开后整网的目标。

## 收录理由

把早期深层网络的初始化难题与降维任务放在同一实验背景下。

## 相关主题与版本

[DOI 10.1126/science.1127647](https://doi.org/10.1126/science.1127647)。延伸阅读见[反向传播](1986-backpropagation.md)。

核对范围为书目信息与方法概要，未做实验复现。
