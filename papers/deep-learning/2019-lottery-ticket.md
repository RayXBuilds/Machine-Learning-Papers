---
id: lottery-ticket
primary_topic: deep-learning
tags: [model-compression, pruning, initialization]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://arxiv.org/abs/1803.03635
status: summary
catalog_year: 2019
subtopic: "结构与效率"
updated: 2026-11-21
---

# The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Jonathan Frankle、Michael Carbin。
- 年份与版本：按 ICLR 2019 正式发表年份归档。arXiv 初稿提交于 2018 年 3 月。
- 原始来源：[ICLR 会议版](https://openreview.net/forum?id=rJl-b3RcF7) · [作者预印本](https://arxiv.org/abs/1803.03635)。
- 官方代码：[作者项目](https://github.com/google-research/lottery-ticket-hypothesis)（第一作者参与的 MNIST 重实现）。

## 解决的问题

剪枝后的小网络如果从头训练，原来的哪些信息决定了它能否赶上稠密网络？

## 主要方法

先训练稠密网络，再按权重幅度剪枝。保留掩码，把剩余权重重置到原始初始化并重新训练，以随机重置作对照。

## 贡献与局限

实验揭示了掩码与初始化组合的作用。发现子网仍须付出训练和剪枝成本，参数数目减少也不能直接换算成硬件加速。

## 前置知识与阅读重点

先了解随机初始化与非结构化剪枝。固定掩码，比较保留初值和换初值两组曲线。

## 收录理由

把模型压缩与优化问题联系起来，给出可检验的初始化对照。

## 相关主题与版本

arXiv:1803.03635。延伸阅读见 [DROPOUT](../deep-learning/2014-dropout.md)。

本条依据作者摘要、书目及项目说明整理，未复现实验。
