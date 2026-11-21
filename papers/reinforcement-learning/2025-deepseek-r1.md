---
id: deepseek-r1
primary_topic: reinforcement-learning
tags: [reasoning, reinforcement-learning]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://www.nature.com/articles/s41586-025-09422-z
status: summary
catalog_year: 2025
subtopic: "离线决策与语言推理"
updated: 2026-11-21
---

# DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：DeepSeek-AI 团队（预印本完整署名见原文）。
- 年份与版本：Nature 2025。arXiv 首版提交于 2025-01-22。期刊版标题为 DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning；本条以预印本题名为入口。
- 原始来源：[Nature 2025 书目](https://www.nature.com/articles/s41586-025-09422-z) · [arXiv 版本记录](https://arxiv.org/abs/2501.12948)。
- 官方代码：[团队发布仓库](https://github.com/deepseek-ai/DeepSeek-R1)提供权重入口和使用说明；完整强化学习训练实现未核实。

## 解决的问题

在答案可判定的任务上，只给结果奖励能否塑造更长的推理行为？

## 主要方法

分别研究直接施加强化学习的 R1-Zero 和引入冷启动样本、多阶段训练的 R1，并以生成轨迹蒸馏较小模型。

## 贡献与局限

作者在数学和代码等可验证任务上报告能力提升。可自动判分的奖励条件限制了对开放式推理和事实可靠性的外推。

## 前置知识与阅读重点

熟悉策略梯度、组内相对奖励和蒸馏后，区分两条训练流程，再查看输出长度与正确率的关系。

## 收录理由

提供一个区分可验证奖励、冷启动数据与蒸馏收益的实例。

## 相关主题与版本

arXiv:2501.12948。[正式 DOI 10.1038/s41586-025-09422-z](https://doi.org/10.1038/s41586-025-09422-z)。本导读依据原始书目与摘要整理，未复现实验。
