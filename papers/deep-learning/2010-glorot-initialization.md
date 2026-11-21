---
id: glorot-initialization
primary_topic: deep-learning
tags: [initialization, gradient-flow]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://proceedings.mlr.press/v9/glorot10a.html
status: summary
catalog_year: 2010
subtopic: "网络训练与优化"
updated: 2026-11-21
---

# Understanding the difficulty of training deep feedforward neural networks

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Xavier Glorot、Yoshua Bengio
- 年份与版本：AISTATS 2010。
- 原始来源：[论文入口](https://proceedings.mlr.press/v9/glorot10a.html)
- 官方代码：在本次核对的一手来源中未确认论文配套实现。

## 解决的问题

随机初始化时，为什么深层网络的部分隐层很快饱和，学习随后陷入长时间停滞？

## 主要方法

逐层观测激活与梯度分布，从前向和反向传播的方差推导兼顾输入、输出宽度的权重尺度。

## 贡献与局限

实验把饱和与训练平台期联系起来。推导依赖初始化时的近似假设，训练中的权重相关性会改变传播条件。

## 前置知识与阅读重点

先复习链式法则与独立随机变量之和的方差。分别写下前向、反向保持方差的条件，观察宽度不同时两者为何冲突。

## 收录理由

为阅读批归一化与残差网络提供可计算的初始化基线。

## 相关主题与版本

[主主题：深度学习与表征学习](README.md) · [延伸主题：数学、学习理论与概率模型](../foundations/README.md)

本条依据原始书目和论文内容整理，未复现实验。
