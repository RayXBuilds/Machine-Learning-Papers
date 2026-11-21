---
id: simclr
primary_topic: deep-learning
type: paper
added: 2026-10-25
verified: 2026-10-25
source: https://proceedings.mlr.press/v119/chen20j.html
status: summary
tags: ["contrastive-learning", "self-supervised-learning"]
catalog_year: 2020
subtopic: "表征与自监督"
updated: 2026-11-21
---

# A Simple Framework for Contrastive Learning of Visual Representations

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 常用名称：SimCLR。
- 作者：Ting Chen、Simon Kornblith、Mohammad Norouzi、Geoffrey Hinton。
- 年份与版本：2020 · ICML。
- 原始来源：[原文](https://proceedings.mlr.press/v119/chen20j.html)。
- 官方代码：原导读未单独核实，本次编排未新增代码可用性声明。

## 解决的问题

如何通过增强视图和对比目标学习无标签视觉表示？

## 主要方法

学习数据增强、投影头和对比目标的配合，理解无标签视觉表征学习。

## 贡献与局限

本条提供方法入门线索；具体实验收益与适用条件仍需结合原文核对。阅读时重点辨析：哪些增强保持语义，哪些增强可能改变任务标签？

## 前置知识与阅读重点

建议前置：CNN、相似度、交叉熵。

阅读顺序：先看方法定义，再结合上方阅读问题核查原文中的假设和实验条件。

## 收录理由

作为本主题的基础阅读入口，可与[学习路线](../../docs/reading-paths.md)中的相关方法对照阅读。

## 相关主题与版本

年份与版本口径沿用上述书目信息。

[主题目录](README.md) · [原经典索引](../../docs/classics.md#simclr) · [年份导航](../../docs/years/README.md)

> 本次仅重组已有书目与阅读提示，未新增实验结论，也未重新核验原文；原 verified 日期保持不变。导读不代表全文精读或实验复现。
