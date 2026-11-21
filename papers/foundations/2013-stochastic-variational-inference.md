---
id: stochastic-variational-inference
primary_topic: foundations
tags: [variational-inference, stochastic-optimization]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://jmlr.org/papers/v14/hoffman13a.html
status: summary
---

# Stochastic Variational Inference

- 作者：Matthew D. Hoffman、David M. Blei、Chong Wang、John Paisley
- 年份与版本：JMLR 14，2013 年；arXiv 首版为 2012 年。
- 原始来源：[论文入口](https://jmlr.org/papers/v14/hoffman13a.html)
- 官方代码：在本次核对的一手来源中未确认论文配套实现。

## 解决的问题

贝叶斯模型的全批量变分更新每轮都要遍历数据，大规模语料上怎样更新全局后验近似？

## 主要方法

抽样小批量观测并求其局部变分参数，放大充分统计量估计，用自然梯度和递减步长更新全局参数。

## 贡献与局限

论文在大规模主题模型上展示可扩展推断。直接套用文中简洁更新需满足模型的条件共轭等结构假设。

## 前置知识与阅读重点

先掌握均值场变分推断与指数族。沿 LDA 的一篇文档追踪哪些变量留在本地，哪些统计量进入全局更新。

## 收录理由

把批量坐标上升与流式小批量推断接到同一条推导线上。

## 相关主题与版本

[主主题：数学、学习理论与概率模型](README.md) · [延伸主题：生成模型](../generative-models/README.md) · [arXiv:1206.7051](https://arxiv.org/abs/1206.7051)

本条依据原始书目和论文内容整理，未复现实验。
