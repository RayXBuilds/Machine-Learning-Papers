---
id: deepwalk
primary_topic: graph-learning
tags: [random-walks, embeddings]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://arxiv.org/abs/1403.6652
status: summary
catalog_year: 2014
subtopic: "图划分与嵌入"
updated: 2026-11-21
---

# DeepWalk: Online Learning of Social Representations

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Bryan Perozzi、Rami Al-Rfou、Steven Skiena
- 年份与版本：KDD 2014，arXiv 首版同年。
- 原始来源：[论文入口](https://arxiv.org/abs/1403.6652)
- 官方代码：[作者项目](https://github.com/phanein/deepwalk)

- 仓库内 PDF：[打开全文](../../pdfs/graph-learning/2014-deepwalk.pdf)（arXiv 1403.6652v2）。

## 解决的问题

只有网络连接与少量节点标签时，怎样为分类器提取邻域信息？

## 主要方法

从节点出发采样截断随机游走，把游走视作词序列，用 Skip-gram 从窗口内的共现学习节点向量。

## 贡献与局限

作者在多标签节点分类中检验表示。节点向量与训练节点绑定，游走邻近性的含义也取决于网络连接方式。

## 前置知识与阅读重点

先了解随机游走和 Skip-gram。改变窗口宽度，追踪一对节点在何种路径上会成为正例。

## 收录理由

展示语言建模的上下文目标如何迁移到图上。

## 相关主题与版本

[主主题：图学习与网络分析](README.md) · [延伸主题：自然语言处理与大语言模型](../nlp/README.md) · [arXiv:1403.6652](https://arxiv.org/abs/1403.6652) · [DOI 10.1145/2623330.2623732](https://doi.org/10.1145/2623330.2623732)

本条依据原始书目和论文内容整理，未复现实验。
