---
id: deep-sparse-rectifiers
primary_topic: deep-learning
tags: [rectifiers, sparsity]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://proceedings.mlr.press/v15/glorot11a.html
status: summary
catalog_year: 2011
subtopic: "网络训练与优化"
updated: 2026-11-21
---

# Deep Sparse Rectifier Neural Networks

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Xavier Glorot、Antoine Bordes、Yoshua Bengio
- 年份与版本：AISTATS 2011。
- 原始来源：[论文入口](https://proceedings.mlr.press/v15/glorot11a.html)
- 官方代码：在本次核对的一手来源中未确认论文配套实现。

## 解决的问题

深层监督网络能否直接学到含大量精确零值的表示，并减少对无监督预训练的依赖？

## 主要方法

用整流单元替代饱和的平滑激活，观察输入变化时哪些单元输出零，并比较有无预训练的分类实验。

## 贡献与局限

论文报告整流网络在所测任务上的训练表现以及激活稀疏性。输出为零的单元在该输入下也不传回局部梯度。

## 前置知识与阅读重点

先了解反向传播与逐元素激活。分别看参数是否为零、激活是否为零，检视论文如何测量后者。

## 收录理由

与权重初始化论文并读，可分清激活函数和初始尺度对训练的影响。

## 相关主题与版本

[主主题：深度学习与表征学习](README.md) · [延伸主题：数学、学习理论与概率模型](../foundations/README.md)

本条依据原始书目和论文内容整理，未复现实验。
