---
id: perceptron
primary_topic: classical-ml
tags: [online-learning, neural-networks]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://www.cs.cmu.edu/~epxing/Class/10715/reading/Rosenblatt.perceptron.pdf
status: summary
catalog_year: 1958
subtopic: "分类与集成"
updated: 2026-11-21
---

# The perceptron: A probabilistic model for information storage and organization in the brain

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Frank Rosenblatt
- 年份与版本：1958 年，Psychological Review 65(6), 386–408。
- 原始来源：[原文](https://www.cs.cmu.edu/~epxing/Class/10715/reading/Rosenblatt.perceptron.pdf)
- 官方代码：核对的原始资料中未确认论文配套实现。

## 解决的问题

经验怎样改变一个识别系统对相似刺激的反应？

## 主要方法

把感知、联结和响应划分为不同单元，让刺激激活部分通路，再用强化改变通路对响应的影响。

## 贡献与局限

随机连接与可调连接承担不同角色，使学习规则可以接受数学分析。论文中的神经元是建模假设，生物真实性需要独立证据。

## 前置知识与阅读重点

先了解阈值函数，再沿一条刺激通路辨认哪些连接在学习时改变。

## 收录理由

从原始模型看懂感知机里的可训练参数，也能理解固定特征给分类边界施加的约束。

## 相关主题与版本

[DOI 10.1037/h0042519](https://doi.org/10.1037/h0042519)。延伸阅读见[反向传播](../deep-learning/1986-backpropagation.md)。

核对范围为书目信息与方法概要，未做实验复现。
