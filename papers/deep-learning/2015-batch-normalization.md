---
id: batch-normalization
primary_topic: deep-learning
type: paper
added: 2026-10-25
verified: 2026-10-25
source: https://proceedings.mlr.press/v37/ioffe15.html
status: summary
tags: ["normalization", "optimization"]
catalog_year: 2015
subtopic: "网络训练与优化"
updated: 2026-11-21
---

# Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 常用名称：Batch Normalization。
- 作者：Sergey Ioffe、Christian Szegedy。
- 年份与版本：2015 · ICML。
- 原始来源：[原文](https://proceedings.mlr.press/v37/ioffe15.html)。
- 官方代码：原导读未单独核实，本次编排未新增代码可用性声明。

## 解决的问题

如何在网络中计算和使用批归一化？

## 主要方法

学习批归一化的计算、可学习缩放和平移，以及训练与推理统计量的差别。

## 贡献与局限

本条提供方法入门线索；具体实验收益与适用条件仍需结合原文核对。阅读时重点辨析：小批量统计量和推理时统计量为什么不能混用？

## 前置知识与阅读重点

建议前置：反向传播、均值与方差。

阅读顺序：先看方法定义，再结合上方阅读问题核查原文中的假设和实验条件。

## 收录理由

作为本主题的基础阅读入口，可与[学习路线](../../docs/reading-paths.md)中的相关方法对照阅读。

## 相关主题与版本

标题沿用原论文的解释，不应把标题中的解释当成机制的最终定论。

[主题目录](README.md) · [原经典索引](../../docs/classics.md#batch-normalization) · [年份导航](../../docs/years/README.md)

> 本次仅重组已有书目与阅读提示，未新增实验结论，也未重新核验原文；原 verified 日期保持不变。导读不代表全文精读或实验复现。
