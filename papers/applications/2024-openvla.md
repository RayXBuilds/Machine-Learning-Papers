---
id: openvla
primary_topic: applications
tags: [robotics, imitation-learning]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://proceedings.mlr.press/v270/kim25c.html
status: summary
---

# OpenVLA: An Open-Source Vision-Language-Action Model

- 作者：Moo Jin Kim、Karl Pertsch、Siddharth Karamcheti 等（完整署名见原文）。
- 年份与版本：CoRL 2024。arXiv 首版提交于 2024-06-13。采用会议举行年份 2024；PMLR 第 270 卷的书目年份为 2025。
- 原始来源：[CoRL 2024 书目](https://proceedings.mlr.press/v270/kim25c.html) · [arXiv 版本记录](https://arxiv.org/abs/2406.09246)。
- 官方代码：已核对[作者项目仓库](https://github.com/openvla/openvla)。

## 解决的问题

预训练视觉语言模型如何利用多种机器人演示，并适配新的操作任务？

## 主要方法

融合 DINOv2 与 SigLIP 的视觉特征，将语言指令和图像送入语言模型，以离散化动作表示训练策略；再研究低秩微调和量化部署。

## 贡献与局限

作者用约 97 万条演示训练，并在多种平台上比较任务成功率。读跨平台结果时需要核对动作表示、任务及微调数据。

## 前置知识与阅读重点

需要模仿学习和视觉编码器知识。优先对照零样本控制与使用目标环境演示微调的实验。

## 收录理由

为后续连续动作生成策略提供可比较的离散动作基线。

## 相关主题与版本

arXiv:2406.09246。可对读 [SigLIP](../multimodal/2023-siglip.md)。本导读依据原始书目与摘要整理，未复现实验。
