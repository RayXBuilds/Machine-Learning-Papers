---
id: q-learning
primary_topic: reinforcement-learning
tags: [temporal-difference, off-policy]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf
status: summary
catalog_year: 1992
subtopic: "价值学习"
updated: 2026-11-21
---

# Q-learning

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Christopher J. C. H. Watkins、Peter Dayan
- 年份与版本：1992 年，Machine Learning 8, 279–292。本文给出 Q-learning 收敛性分析，算法见 Watkins 的 1989 年早期工作。
- 原始来源：[原文](https://www.gatsby.ucl.ac.uk/~dayan/papers/cjch.pdf)
- 官方代码：核对的原始资料中未确认论文配套实现。

- 仓库内 PDF：[打开全文](../../pdfs/reinforcement-learning/1992-q-learning.pdf)（Machine Learning 1992 期刊版）。

## 解决的问题

智能体只观测实际采取动作的收益和后继状态，能否学出最优动作价值？

## 主要方法

用即时奖励加上折扣后的最大后继动作价值构造目标，对已访问的状态动作对作增量更新。

## 贡献与局限

论文给出离散表示和充分采样等条件下的收敛结果。神经网络近似会改变证明所依赖的条件。

## 前置知识与阅读重点

先掌握贝尔曼最优方程。区分行为策略选出的动作与更新目标中取最大值的动作。

## 收录理由

为 DQN 提供表格情形的基准，便于逐项辨认函数近似引入的变化。

## 相关主题与版本

[DOI 10.1007/BF00992698](https://doi.org/10.1007/BF00992698)。延伸阅读见[DQN](../reinforcement-learning/2015-dqn.md)。

核对范围为书目信息与方法概要，未做实验复现。
