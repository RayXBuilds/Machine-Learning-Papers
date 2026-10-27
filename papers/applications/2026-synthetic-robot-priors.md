---
id: synthetic-robot-priors
primary_topic: applications
tags: [robotics, synthetic-data, in-context-learning]
type: paper
added: 2026-10-27
verified: 2026-10-27
source: https://arxiv.org/abs/2610.31275
status: summary
---

# Learning Robot Behavior Priors from Non-Robotic Synthetic Data

- 作者：Mateusz Odrowaz-Sypniewski、Michael Amir、Jasmine Bayrooti、Ajay Shankar、Amanda Prorok。
- 年份与版本：2026-10-22 首次提交，arXiv v1；预印本，未核实正式会议或期刊接收信息。
- 原始来源：[arXiv 书目页](https://arxiv.org/abs/2610.31275) · [v1 正文](https://arxiv.org/html/2610.31275v1)。
- 官方代码：正文 VI-D 称接收后发布代码与数据；截至核对日，所核页面未提供已发布代码包。

## 解决的问题

机器人行为数据收集成本高。能否先从不含真实机器人轨迹的程序化数据中学到有助于动作预测的结构？

## 主要方法

构造三类控制问题的数学抽象数据，用于 Transformer 预训练；测试时利用任务上下文预测动作，考察合成先验能否迁移到未见物理任务。[方法与实验](https://arxiv.org/html/2610.31275v1)

## 贡献与局限

作者报告控制相关先验优于通用因果先验，但真实数据基线在其训练数据集上更强。实验主要验证动作预测；开环误差会累积，不能据此宣称已实现可靠的闭环自主控制。模型规模也受计算预算约束。已核对相关正文，未复现实验。

## 前置知识与阅读重点

需要了解状态转移、Transformer 与上下文学习。重点区分预训练数据、测试上下文及动作预测指标，检查合成分布与目标任务的差异。

## 收录理由

补充机器人应用中的低成本预训练思路，适合与真实行为数据驱动的方法对照阅读。

## 相关主题与版本

arXiv ID：`2610.31275`。年份采用首次预印本年份。主主题为领域应用；动作预测结果不直接作为强化学习策略性能证据。
