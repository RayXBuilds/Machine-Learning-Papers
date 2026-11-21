---
id: transformer
primary_topic: nlp
type: paper
added: 2026-10-25
verified: 2026-10-25
source: https://papers.nips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html
status: summary
tags: ["attention", "sequence-modeling"]
catalog_year: 2017
subtopic: "序列建模与预训练"
updated: 2026-11-21
---

# Attention Is All You Need

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 常用名称：Transformer。
- 作者：Ashish Vaswani 等。
- 年份与版本：2017 · NeurIPS（当时名为 NIPS）。
- 原始来源：[原文](https://papers.nips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)。
- 官方代码：原导读未单独核实，本次编排未新增代码可用性声明。

- 仓库内 PDF：[打开全文](../../pdfs/nlp/2017-transformer.pdf)（会议论文集版（papers.nips.cc））。

## 解决的问题

如何利用注意力进行不依赖递归的序列建模？

## 主要方法

学习缩放点积注意力、多头注意力和位置编码，理解没有递归的序列建模。

## 贡献与局限

本条提供方法入门线索；具体实验收益与适用条件仍需结合原文核对。阅读时重点辨析：并行训练与自回归生成的计算方式有什么不同？

## 前置知识与阅读重点

建议前置：矩阵运算、Seq2Seq、注意力基础。

阅读顺序：先看方法定义，再结合上方阅读问题核查原文中的假设和实验条件。

## 收录理由

作为本主题的基础阅读入口，可与[学习路线](../../docs/reading-paths.md)中的相关方法对照阅读。

## 相关主题与版本

年份与版本口径沿用上述书目信息。

[主题目录](README.md) · [原经典索引](../../docs/classics.md#transformer) · [年份导航](../../docs/years/README.md)

> 本次仅重组已有书目与阅读提示，未新增实验结论，也未重新核验原文；原 verified 日期保持不变。导读不代表全文精读或实验复现。
