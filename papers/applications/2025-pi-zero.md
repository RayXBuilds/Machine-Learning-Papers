---
id: pi-zero
primary_topic: applications
tags: [robotics, flow-matching]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://roboticsproceedings.org/rss21/p010.html
status: summary
catalog_year: 2025
subtopic: "机器人与具身控制"
updated: 2026-11-21
---

# π₀: A Vision-Language-Action Flow Model for General Robot Control

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Kevin Black、Noah Brown、Danny Driess 等（完整署名见原文）。
- 年份与版本：RSS 2025。arXiv 首版提交于 2024-10-31。正式发表在次年；此处讨论初代 π₀。
- 原始来源：[RSS 2025 书目](https://roboticsproceedings.org/rss21/p010.html) · [arXiv 版本记录](https://arxiv.org/abs/2410.24164)。
- 官方代码：已核对[作者项目仓库](https://github.com/Physical-Intelligence/openpi)。

- 仓库内 PDF：[打开全文](../../pdfs/applications/2025-pi-zero.pdf)（arXiv 2410.24164v4）。

## 解决的问题

语言指令对应连续、多步且可能有多种解的机器人动作，怎样由视觉语言表示生成这些动作？

## 主要方法

在预训练视觉语言骨干之上用流匹配学习条件动作块，结合多种机器人平台的数据，再按任务微调。

## 贡献与局限

作者在折叠衣物、清理桌面等任务上评估控制效果。零样本与任务专门微调的数据条件不同，成功率需对应具体实验。

## 前置知识与阅读重点

先了解行为克隆、动作分块和流匹配。观察动作块内部的连续轨迹与控制循环重新读取观测的时点。

## 收录理由

与 OpenVLA 对读，比较离散动作符号和连续动作块的建模取舍。

## 相关主题与版本

arXiv:2410.24164。[正式 DOI 10.15607/RSS.2025.XXI.010](https://doi.org/10.15607/RSS.2025.XXI.010)。可对读 [OpenVLA](../applications/2024-openvla.md)。本导读依据原始书目与摘要整理，未复现实验。
