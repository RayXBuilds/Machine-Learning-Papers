---
id: decision-transformer
primary_topic: reinforcement-learning
tags: [offline-rl, sequence-modeling]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://arxiv.org/abs/2106.01345
status: summary
---

# Decision Transformer: Reinforcement Learning via Sequence Modeling

- 作者：Lili Chen、Kevin Lu、Aravind Rajeswaran、Kimin Lee、Aditya Grover、Misha Laskin、Pieter Abbeel、Aravind Srinivas、Igor Mordatch。
- 年份与版本：按 NeurIPS 2021 正式发表年份归档。arXiv 初稿提交于 2021 年 6 月。
- 原始来源：[NeurIPS 会议版](https://proceedings.neurips.cc/paper/2021/hash/7f489f642a0ddb10272b5c31057f0663-Abstract.html) · [作者预印本](https://arxiv.org/abs/2106.01345)。
- 官方代码：[作者项目](https://github.com/kzl/decision-transformer)。

## 解决的问题

能否只用现成的轨迹，通过指定目标回报让模型生成动作？

## 主要方法

将剩余目标回报、状态和动作按时间排列，以因果注意力预测下一个动作。推理时用实际奖励更新剩余目标。

## 贡献与局限

论文在离线控制等任务中比较了条件序列建模。目标回报只是条件，尤其在数据稀少的高回报区间不能保证达成。

## 前置知识与阅读重点

先理解轨迹回报与自回归建模。写出执行第一步前可见的 token，并追踪收到奖励后下一步的输入。

## 收录理由

提供离线强化学习路线，可与依赖价值目标的 TD3 对比。

## 相关主题与版本

arXiv:2106.01345。延伸阅读见 [TD3](../reinforcement-learning/2018-td3.md)。

本条依据作者摘要、书目及项目说明整理，未复现实验。
