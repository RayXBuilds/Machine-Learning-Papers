---
id: siglip
primary_topic: multimodal
tags: [image-text, contrastive-learning]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://openaccess.thecvf.com/content/ICCV2023/html/Zhai_Sigmoid_Loss_for_Language_Image_Pre-Training_ICCV_2023_paper.html
status: summary
catalog_year: 2023
subtopic: "图文对齐"
updated: 2026-11-21
---

# Sigmoid Loss for Language Image Pre-Training

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Xiaohua Zhai、Basil Mustafa、Alexander Kolesnikov、Lucas Beyer。
- 年份与版本：ICCV 2023。arXiv 首版提交于 2023-03-27。
- 原始来源：[ICCV 2023 书目](https://openaccess.thecvf.com/content/ICCV2023/html/Zhai_Sigmoid_Loss_for_Language_Image_Pre-Training_ICCV_2023_paper.html) · [arXiv 版本记录](https://arxiv.org/abs/2303.15343)。
- 官方代码：已核对[作者项目仓库](https://github.com/google-research/big_vision)。

- 仓库内 PDF：[打开全文](../../pdfs/multimodal/2023-siglip.pdf)（arXiv 2303.15343，PDF 制作于 2023-09-27，首页未标修订号）。

## 解决的问题

图文双塔训练通常在整批相似度上归一化，成对匹配是否需要这个全局分母？

## 主要方法

对每个图文对用 sigmoid 损失判断匹配与否，分别累计正例和负例的贡献，从而可以单独考察样本数和正负配对比例。

## 贡献与局限

作者展示小批量下的表现并探索极大批量的收益递减。取消全局归一化之后，负例选择和计算成本仍影响结果。

## 前置知识与阅读重点

先读 CLIP 双向对比目标；固定图像数，写出增加一条文本后两个目标各有哪些项改变。

## 收录理由

提供用配对损失重新理解图文对齐的对照实验。

## 相关主题与版本

arXiv:2303.15343。[正式 DOI 10.1109/iccv51070.2023.01100](https://doi.org/10.1109/iccv51070.2023.01100)。可对读 [CLIP](../multimodal/2021-clip.md)。本导读依据原始书目与摘要整理，未复现实验。
