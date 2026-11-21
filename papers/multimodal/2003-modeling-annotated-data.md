---
id: modeling-annotated-data
primary_topic: multimodal
tags: [topic-models, image-annotation]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://www.cs.columbia.edu/~blei/papers/BleiJordan2003.pdf
status: summary
catalog_year: 2003
subtopic: "图文建模与生成描述"
updated: 2026-11-21
---

# Modeling Annotated Data

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：David M. Blei、Michael I. Jordan
- 年份与版本：2003 年，SIGIR 2003, 127–134。
- 原始来源：[原文](https://www.cs.columbia.edu/~blei/papers/BleiJordan2003.pdf)
- 官方代码：核对的原始资料中未确认论文配套实现。

- 仓库内 PDF：[打开全文](../../pdfs/multimodal/2003-modeling-annotated-data.pdf)（Blei 与 Jordan，SIGIR 2003 论文）。

## 解决的问题

一张图像配有一组说明词，却缺少逐词对应的区域标签，怎样学习图文关系？

## 主要方法

论文比较三种生成模型。对应 LDA 先为图像区域生成潜在主题，再让说明词引用某个区域的主题，从生成过程中引入跨模态对应。

## 贡献与局限

模型可以利用图像和文字的弱配对做标注或检索。词与区域间的局部对应假设较难表达整幅场景的抽象含义。

## 前置知识与阅读重点

先读 LDA 的文档混合模型，再比较三个模型中的条件依赖，重点看新增的区域索引。

## 收录理由

在 CLIP 之前补入一个以隐变量解释图文对应的参照模型。

## 相关主题与版本

[DOI 10.1145/860435.860460](https://doi.org/10.1145/860435.860460)。延伸阅读见[LDA](../nlp/2003-lda.md)。

核对范围为书目信息与方法概要，未做实验复现。
