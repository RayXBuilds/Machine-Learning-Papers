---
id: policy-gradient-function-approximation
primary_topic: reinforcement-learning
catalog_year: 1999
subtopic: "策略优化与连续控制"
updated: 2026-11-28
tags: [policy-gradient, actor-critic, function-approximation]
type: paper
added: 2026-11-28
verified: 2026-11-28
source: https://proceedings.neurips.cc/paper_files/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html
status: summary
---

# Policy Gradient Methods for Reinforcement Learning with Function Approximation

[主题目录](README.md) · [年份导航](../../docs/years/README.md)

- 作者：Richard S. Sutton、David A. McAllester、Satinder P. Singh、Yishay Mansour
- 年份与版本：按 NIPS 1999 会议年份归档，收于 *Advances in Neural Information Processing Systems 12*。
- 原始来源：[会议论文页](https://proceedings.neurips.cc/paper_files/paper/1999/hash/464d828b85b0bed98e80ade0a5c43b0f-Abstract.html)
- 仓库内 PDF：[会议论文集全文，7 页](../../pdfs/reinforcement-learning/1999-policy-gradient-function-approximation.pdf)
- 官方代码：会议论文页未列出代码。

## 解决的问题

假设智能体可以向左或向右走。稍微调高向右走的概率，会改变眼前的动作选择，也会改变之后更常到达的状态。要判断这次调整能否提高长期回报，是否还得知道环境如何响应，并对每个状态的访问频率求导？

## 主要方法

策略梯度定理把答案写成一个加权和。在当前策略经常访问的状态，考察参数变化会怎样改变各动作的概率，再用该动作的长期价值给这个变化加权。状态访问分布仍然决定权重，但公式中无需对它显式求导。论文分别处理了平均奖励和从固定起点出发的折扣回报。

## 贡献与局限

真实的动作价值通常未知。作者给出可用近似值替代它的一组充分条件：近似器的参数梯度要与策略对数概率的参数梯度匹配，而且在当前策略的采样权重下，价值拟合的平方误差要达到驻点。满足这些条件，价值估计即使有误差，得到的期望策略梯度仍然正确。文中的收敛结论还涉及步长、光滑性及每轮拟合条件，不能直接推广到用少量样本同时训练两个神经网络的情形。

## 前置知识与阅读重点

先熟悉随机策略、动作价值和条件期望。读定理 1 时，可给同一状态下的两个动作价值同时减去一个常数，观察为何梯度不变：两个动作概率之和恒为 1，它们的导数之和为零。再读定理 2，区分“价值预测准确”和“价值误差在策略更新方向上的加权投影为零”。

## 收录理由

[TRPO](2015-trpo.md) 和 [PPO](2017-ppo.md) 的导读都涉及如何控制策略的更新幅度。这篇论文适合放在它们之前，先弄清楚策略应朝哪个方向更新，以及优势估计在其中起什么作用。

## 相关主题与版本

可与 [Q-learning](1992-q-learning.md) 对读，比较从动作价值选择动作与直接调整动作概率这两种决策方式。本文核对了会议版的书目信息与定理条件，未做实验复现。
