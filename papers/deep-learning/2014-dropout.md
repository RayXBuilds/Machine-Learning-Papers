---
id: dropout
primary_topic: deep-learning
type: paper
added: 2026-10-25
verified: 2026-10-25
source: https://jmlr.org/papers/v15/srivastava14a.html
status: summary
tags: ["regularization", "neural-networks"]
catalog_year: 2014
subtopic: "网络训练与优化"
updated: 2026-11-21
---

# Dropout: A Simple Way to Prevent Neural Networks from Overfitting

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 常用名称：Dropout。
- 作者：Nitish Srivastava 等。
- 年份与版本：2014 · JMLR。
- 原始来源：[原文](https://jmlr.org/papers/v15/srivastava14a.html)。
- 官方代码：原导读未单独核实，本次编排未新增代码可用性声明。

- 仓库内 PDF：[打开全文](../../pdfs/deep-learning/2014-dropout.pdf)（JMLR 期刊版）。

## 解决的问题

如何在神经网络训练中使用随机丢弃进行正则化？

## 主要方法

理解训练时随机丢弃单元的正则化方法，以及训练和推理的差别。

## 贡献与局限

本条提供方法入门线索；具体实验收益与适用条件仍需结合原文核对。阅读时重点辨析：训练时的随机网络与推理时的网络如何对应？

## 前置知识与阅读重点

建议前置：神经网络、过拟合。

阅读顺序：先看方法定义，再结合上方阅读问题核查原文中的假设和实验条件。

## 收录理由

作为本主题的基础阅读入口，可与[学习路线](../../docs/reading-paths.md)中的相关方法对照阅读。

## 相关主题与版本

年份与版本口径沿用上述书目信息。

[主题目录](README.md) · [原经典索引](../../docs/classics.md#dropout) · [年份导航](../../docs/years/README.md)

> 本次仅重组已有书目与阅读提示，未新增实验结论，也未重新核验原文；原 verified 日期保持不变。导读不代表全文精读或实验复现。
