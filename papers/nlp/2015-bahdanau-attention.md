---
id: bahdanau-attention
primary_topic: nlp
tags: [attention, machine-translation]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://arxiv.org/abs/1409.0473
status: summary
catalog_year: 2015
subtopic: "序列建模与预训练"
updated: 2026-11-21
---

# Neural Machine Translation by Jointly Learning to Align and Translate

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Dzmitry Bahdanau、Kyunghyun Cho、Yoshua Bengio
- 年份与版本：ICLR 2015 口头报告；arXiv 首版为 2014 年。
- 原始来源：[论文入口](https://arxiv.org/abs/1409.0473)
- 官方代码：[作者项目](https://github.com/lisa-groundhog/GroundHog/tree/master/experiments/nmt)

## 解决的问题

把整句压缩成单一向量后，译到句末时解码器如何找回与当前目标词有关的信息？

## 主要方法

编码器保留各源位置的表示。每个解码步对它们打分、归一化后加权求和，生成随目标位置变化的上下文。

## 贡献与局限

原文在英译法实验中比较翻译表现并展示软对齐图。注意力权重由翻译目标间接训练，解读为人工词对齐时需要额外验证。

## 前置知识与阅读重点

先了解循环编码器与自回归解码。逐步写出同一个源词在相邻两个解码步的权重如何变化。

## 收录理由

连接固定向量 Seq2Seq 与后来广泛采用的注意力机制。

## 相关主题与版本

[主主题：自然语言处理与大语言模型](README.md) · [延伸主题：深度学习与表征学习](../deep-learning/README.md) · [arXiv:1409.0473](https://arxiv.org/abs/1409.0473)

本条依据原始书目和论文内容整理，未复现实验。
