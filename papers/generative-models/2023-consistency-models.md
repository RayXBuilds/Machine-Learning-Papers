---
id: consistency-models
primary_topic: generative-models
tags: [diffusion, distillation]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://proceedings.mlr.press/v202/song23a.html
status: summary
---

# Consistency Models

- 作者：Yang Song、Prafulla Dhariwal、Mark Chen、Ilya Sutskever。
- 年份与版本：ICML 2023。arXiv 首版提交于 2023-03-02。
- 原始来源：[ICML 2023 书目](https://proceedings.mlr.press/v202/song23a.html) · [arXiv 版本记录](https://arxiv.org/abs/2303.01469)。
- 官方代码：已核对[作者项目仓库](https://github.com/openai/consistency_models)。

## 解决的问题

扩散采样反复求解去噪轨迹，能否一步就预测同一条轨迹的终点？

## 主要方法

学习把概率流 ODE 轨迹上不同时刻的状态映射到同一个低噪声端点。作者分别研究从扩散教师蒸馏和直接用数据训练的路线。

## 贡献与局限

同一模型支持单步及少步生成。论文的 FID 对应明确的数据集、分辨率与训练路线，横向比较需匹配这些条件。

## 前置知识与阅读重点

先掌握扩散与概率流 ODE，再看一致性约束怎样配合端点边界条件，避免常数解。

## 收录理由

为比较扩散蒸馏与直接训练的快速采样方法提供起点。

## 相关主题与版本

arXiv:2303.01469。本导读依据原始书目与摘要整理，未复现实验。
