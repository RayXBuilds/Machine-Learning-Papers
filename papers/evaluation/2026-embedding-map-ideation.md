---
id: embedding-map-ideation
primary_topic: evaluation
tags: [ideation, embeddings, temporal-evaluation]
type: paper
added: 2026-11-22
verified: 2026-11-22
updated: 2026-11-22
source: https://arxiv.org/abs/2611.21408v1
status: summary
catalog_year: 2026
subtopic: "实验设计与数据有效性"
---

# Do Embedding-Map Distances Guide LLM Ideation? Four Tests Against What Came Next

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Javier Aguilar Martín
- 年份与版本：arXiv v1 于 2026-11-16 提交，按预印本年份归档。
- 原始来源：[论文页面](https://arxiv.org/abs/2611.21408v1)
- 仓库内 PDF：[打开全文](../../pdfs/evaluation/2026-embedding-map-ideation.pdf)（arXiv 2611.21408v1，48 页）。
- 官方代码：[作者的实验仓库](https://github.com/JaviMaligno/latent-gap-ideas)。本次核对仓库说明，未运行实验。

## 解决的问题

把已有研究映射为向量后，离已知工作较远的区域是否值得探索？要把这个想法用作选题依据，至少需要证明两件事：模型能写出落在目标区域的文本，而且该区域能预示后续发展。

## 主要方法

作者用较早的资料建立嵌入空间，再用较晚出现的条目检验预测。他分别考察指定坐标能否解码成文本、稀疏区域是否增长更快、模型生成的后续研究与真实引用论文相距多远，以及参考材料的距离如何影响生成结果。

## 贡献与局限

作者报告，在 Steam 和 arXiv 数据上，把区域的稀疏程度加入已有增长趋势后，没有获得额外的增长预测能力。即使能写出靠近某些内部空隙的文本，也仍需单独验证其研究价值。专利数据上的结果尚不明确，部分后续检验是在主结果出来后设计的。

## 前置知识与阅读重点

先了解余弦相似度、聚类和时间切分。读第一个实验时关注文本是否命中目标坐标；读第二个实验时关注区域原有的增长趋势。两处成功的判据不同。

## 收录理由

为评估科研选题工具提供了一个可操作的基线：用当时确实可见的资料建图，再检查模型能否预测后来发生的变化。

## 相关主题与版本

可与[科研新颖性评估](2026-claimnov.md)对读。后者关注模型能否识别已有工作，本篇关注距离指标的预测效力。
