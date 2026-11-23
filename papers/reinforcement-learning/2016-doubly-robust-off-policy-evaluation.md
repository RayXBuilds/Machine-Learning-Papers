---
id: doubly-robust-off-policy-evaluation
primary_topic: reinforcement-learning
catalog_year: 2016
subtopic: "离线决策与语言推理"
updated: 2026-11-23
tags: [off-policy-evaluation, importance-sampling, value-estimation]
type: paper
added: 2026-11-23
verified: 2026-11-23
source: https://proceedings.mlr.press/v48/jiang16.html
status: summary
---

# Doubly Robust Off-policy Value Evaluation for Reinforcement Learning

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Nan Jiang、Lihong Li
- 年份与版本：按 ICML 2016 正式发表年归档。会议于 2016-06-20 至 06-22 举办，论文刊载于 PMLR 第 48 卷，第 652–661 页。预印本首发于 2015-11-11，v3 更新于 2016-05-26。
- 原始来源：[PMLR 论文页](https://proceedings.mlr.press/v48/jiang16.html)
- 仓库内 PDF：[打开会议原文](../../pdfs/reinforcement-learning/2016-doubly-robust-off-policy-evaluation.pdf)（10 页）。
- 官方代码：[作者论文列表](https://nanjiang.cs.illinois.edu/)列有论文和海报，本次未核实官方实现。

## 解决的问题

只有旧策略产生的轨迹时，怎样估计换用新策略后的平均回报？直接在拟合的环境模型里模拟，模型误差可能累积；按新旧策略选择动作的概率之比给日志加权，又可能让少数轨迹主导估计。

## 主要方法

从轨迹末端向前算。每一步先取模型给出的目标策略状态价值，再计算一次预测误差：实际奖励加上下步的折扣回报估计，减去模型对已执行动作的价值预测。用这一步的新旧策略动作概率比给误差加权，再加回状态价值。若模型已经解释了大部分回报波动，需要用日志校正的部分就较小。

## 贡献与局限

作者把用于单步决策的双重稳健估计扩展到多步轨迹。在行为策略概率已知、目标动作得到覆盖、价值模型与评估样本独立等条件下，即使模型预测有误，估计仍可无偏。方差能降多少取决于预测质量；旧策略极少采取的动作仍会带来大权重。

## 前置知识与阅读重点

先熟悉折扣回报、动作价值与重要性采样。读第 3 节时，可在两步轨迹上把动作价值预测都设为零，观察递推式如何还原逐步重要性采样；再代入较准确的预测，找出哪一项的波动缩小了。

## 收录理由

离线日志既能用于学习策略，也能用于评估给定策略。这篇论文提供了检查评估可信度的具体问题：数据是否覆盖目标动作？哪些误差由模型解释，哪些必须由轨迹校正？

## 相关主题与版本

[arXiv 版本记录](https://arxiv.org/abs/1511.03722) · [离线轨迹上的策略学习：Decision Transformer](2021-decision-transformer.md)。本导读核对了书目、递推方法与理论条件，未复现实验。
