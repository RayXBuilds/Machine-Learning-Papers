---
id: genie
primary_topic: generative-models
tags: [world-models, latent-actions]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://proceedings.mlr.press/v235/bruce24a.html
status: summary
catalog_year: 2024
subtopic: "扩散、流与世界模型"
updated: 2026-11-21
---

# Genie: Generative Interactive Environments

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Jake Bruce、Michael Dennis、Ashley Edwards 等（完整署名见原文）。
- 年份与版本：ICML 2024。arXiv 首版提交于 2024-02-23。
- 原始来源：[ICML 2024 书目](https://proceedings.mlr.press/v235/bruce24a.html) · [arXiv 版本记录](https://arxiv.org/abs/2402.15391)。
- 官方代码：在已核对的论文与[作者项目页](https://sites.google.com/view/genie-2024/)中未确认公开实现。

- 仓库内 PDF：[打开全文](../../pdfs/generative-models/2024-genie.pdf)（arXiv 2402.15391v1）。

## 解决的问题

没有记录操作者的按键，能否仅凭视频学出可交互环境？

## 主要方法

时空分词器压缩视频，潜在动作模型从帧间变化提取离散动作，动态模型在选定动作条件下逐帧预测后续状态。

## 贡献与局限

作者展示了可逐帧操控的生成环境。潜在动作来自观察关联，语义和长时物理一致性需要另外验证。

## 前置知识与阅读重点

需要视频离散表示和自回归预测知识。比较训练时推断动作所见的帧与生成时用户指定动作所见的信息。

## 收录理由

连接无标签视频建模与可控世界模型。

## 相关主题与版本

arXiv:2402.15391。本导读依据原始书目与摘要整理，未复现实验。
