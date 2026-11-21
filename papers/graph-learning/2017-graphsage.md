---
id: graphsage
primary_topic: graph-learning
tags: [inductive-learning, neighborhood-sampling]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://arxiv.org/abs/1706.02216
status: summary
catalog_year: 2017
subtopic: "图神经网络"
updated: 2026-11-21
---

# Inductive Representation Learning on Large Graphs

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Will Hamilton、Zhitao Ying、Jure Leskovec（会议页面署名；预印本列为 William L. Hamilton、Rex Ying、Jure Leskovec）。
- 年份与版本：按 NIPS 2017 正式发表年份归档。arXiv 初稿提交于 2017 年 6 月。
- 原始来源：[NIPS 会议版](https://papers.nips.cc/paper/2017/hash/5dd9db5e033da9c6fb5ba83c7a7ebea9-Abstract.html) · [作者预印本](https://arxiv.org/abs/1706.02216)。
- 官方代码：[作者项目](https://github.com/williamleif/GraphSAGE)。

- 仓库内 PDF：[打开全文](../../pdfs/graph-learning/2017-graphsage.pdf)（arXiv 1706.02216v4）。

## 解决的问题

图中加入新节点时，按节点编号学习的向量无法直接用于预测。

## 主要方法

从目标节点向外采样邻居，再逐层聚合邻域特征。训练得到的聚合函数可以作用于未参与训练的节点。

## 贡献与局限

实验展示了归纳式节点分类。新节点仍需有可用的特征和邻接信息，采样也可能遗漏少数重要邻居。

## 前置知识与阅读重点

先掌握图的邻接表与消息传递。画出两层采样树，区分训练时更新的参数和推理时读取的节点信息。

## 收录理由

承接 GCN，说明图模型如何为新增节点计算表示。

## 相关主题与版本

arXiv:1706.02216。延伸阅读见 [GCN](../graph-learning/2017-gcn.md)。

本条依据作者摘要、书目及项目说明整理，未复现实验。
