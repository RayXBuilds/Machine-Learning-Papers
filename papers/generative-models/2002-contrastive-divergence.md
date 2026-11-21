---
id: contrastive-divergence
primary_topic: generative-models
tags: [energy-based-models, mcmc]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://doi.org/10.1162/089976602760128018
status: summary
catalog_year: 2002
subtopic: "能量模型、变分与自回归"
updated: 2026-11-21
---

# Training Products of Experts by Minimizing Contrastive Divergence

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Geoffrey E. Hinton
- 年份与版本：2002 年，Neural Computation 14(8), 1771–1800。2000 年技术报告为早期版本。
- 原始来源：[原文](https://doi.org/10.1162/089976602760128018) · [作者的早期报告](https://www.cs.toronto.edu/~hinton/absps/tr00-004.html)
- 官方代码：核对的原始资料中未确认论文配套实现。

## 解决的问题

多个专家分布相乘后，归一化常数妨碍直接计算似然梯度，训练怎样继续？

## 主要方法

从真实样本启动短马尔可夫链，用链运行前后的统计量之差近似参数更新所需的正相与负相差异。

## 贡献与局限

缩短采样链降低单次更新的成本。短链通常还未达到平衡，更新方向会带有偏差。

## 前置知识与阅读重点

先理解能量模型与 Gibbs 采样。对照数据分布、一步重构分布和模型平衡分布的作用。

## 收录理由

有助于理解能量模型中推断容易与采样困难为何可以同时发生。

## 相关主题与版本

[DOI 10.1162/089976602760128018](https://doi.org/10.1162/089976602760128018)。延伸阅读见[深度自编码器](../deep-learning/2006-deep-autoencoder.md)。

核对范围为书目信息与方法概要，未做实验复现。
