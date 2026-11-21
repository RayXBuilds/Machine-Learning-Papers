---
id: seq2seq
primary_topic: nlp
type: paper
added: 2026-10-25
verified: 2026-10-25
source: https://arxiv.org/abs/1409.3215
status: summary
tags: ["sequence-modeling", "machine-translation"]
catalog_year: 2014
subtopic: "序列建模与预训练"
updated: 2026-11-21
---

# Sequence to Sequence Learning with Neural Networks

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 常用名称：Seq2Seq。
- 作者：Ilya Sutskever、Oriol Vinyals、Quoc V. Le。
- 年份与版本：2014 · NeurIPS（当时名为 NIPS）。
- 原始来源：[原文](https://arxiv.org/abs/1409.3215)。
- 官方代码：原导读未单独核实，本次编排未新增代码可用性声明。

- 仓库内 PDF：[打开全文](../../pdfs/nlp/2014-seq2seq.pdf)（arXiv 1409.3215v3）。

## 解决的问题

如何用编码器与解码器处理变长序列？

## 主要方法

理解 LSTM 编码器与解码器如何处理变长输入、输出序列。

## 贡献与局限

本条提供方法入门线索；具体实验收益与适用条件仍需结合原文核对。阅读时重点辨析：固定长度编码给长序列带来了什么限制？

## 前置知识与阅读重点

建议前置：RNN、LSTM、条件概率。

阅读顺序：先看方法定义，再结合上方阅读问题核查原文中的假设和实验条件。

## 收录理由

作为本主题的基础阅读入口，可与[学习路线](../../docs/reading-paths.md)中的相关方法对照阅读。

## 相关主题与版本

年份与版本口径沿用上述书目信息。

[主题目录](README.md) · [原经典索引](../../docs/classics.md#seq2seq) · [年份导航](../../docs/years/README.md)

> 本次仅重组已有书目与阅读提示，未新增实验结论，也未重新核验原文；原 verified 日期保持不变。导读不代表全文精读或实验复现。
