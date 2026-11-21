---
id: word2vec
primary_topic: nlp
type: paper
added: 2026-10-25
verified: 2026-10-25
source: https://arxiv.org/abs/1301.3781
status: summary
tags: ["word-embeddings", "language-modeling"]
catalog_year: 2013
subtopic: "词表示与主题模型"
updated: 2026-11-21
---

# Efficient Estimation of Word Representations in Vector Space

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 常用名称：Word2Vec。
- 作者：Tomas Mikolov、Kai Chen、Greg Corrado、Jeffrey Dean。
- 年份与版本：2013 · arXiv 预印本。
- 原始来源：[原文](https://arxiv.org/abs/1301.3781)。
- 官方代码：原导读未单独核实，本次编排未新增代码可用性声明。

## 解决的问题

如何通过词预测任务学习分布式词表示？

## 主要方法

学习 CBOW 与 Skip-gram 的基本目标，理解分布式词表示和预测任务的联系。

## 贡献与局限

本条提供方法入门线索；具体实验收益与适用条件仍需结合原文核对。阅读时重点辨析：预测中心词与预测上下文分别学习什么信息？

## 前置知识与阅读重点

建议前置：语言模型、向量表示。

阅读顺序：先看方法定义，再结合上方阅读问题核查原文中的假设和实验条件。

## 收录理由

作为本主题的基础阅读入口，可与[学习路线](../../docs/reading-paths.md)中的相关方法对照阅读。

## 相关主题与版本

本条对应早期 CBOW / Skip-gram 论文；负采样等后续细节不能全部归到这一篇。

[主题目录](README.md) · [原经典索引](../../docs/classics.md#word2vec) · [年份导航](../../docs/years/README.md)

> 本次仅重组已有书目与阅读提示，未新增实验结论，也未重新核验原文；原 verified 日期保持不变。导读不代表全文精读或实验复现。
