---
id: segment-anything
primary_topic: computer-vision
tags: [segmentation, prompting]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://openaccess.thecvf.com/content/ICCV2023/html/Kirillov_Segment_Anything_ICCV_2023_paper.html
status: summary
catalog_year: 2023
subtopic: "检测、分割与人体理解"
updated: 2026-11-21
---

# Segment Anything

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Alexander Kirillov、Eric Mintun、Nikhila Ravi 等（完整署名见原文）。
- 年份与版本：ICCV 2023。arXiv 首版提交于 2023-04-05。
- 原始来源：[ICCV 2023 书目](https://openaccess.thecvf.com/content/ICCV2023/html/Kirillov_Segment_Anything_ICCV_2023_paper.html) · [arXiv 版本记录](https://arxiv.org/abs/2304.02643)。
- 官方代码：已核对[作者项目仓库](https://github.com/facebookresearch/segment-anything)。

- 仓库内 PDF：[打开全文](../../pdfs/computer-vision/2023-segment-anything.pdf)（CVF 会议论文集版）。

## 解决的问题

同一张图里，一个点可能落在衣袖、衣服或人身上。分割模型如何响应含义不唯一的提示？

## 主要方法

图像编码器先计算可复用的特征，提示编码器接收点或框，轻量解码器产生候选掩码。作者把模型嵌入标注流程，逐轮扩充 SA-1B。

## 贡献与局限

论文把提示式分割变成可跨数据集测试的任务。掩码覆盖目标区域并不等于识别其类别，比较结果还取决于提示如何生成。

## 前置知识与阅读重点

熟悉像素级分割与 IoU 后，比较单点提示下的多个输出，留意评估时如何选掩码。

## 收录理由

用一个具体任务区分交互提示、类别识别与掩码质量。

## 相关主题与版本

arXiv:2304.02643。[正式 DOI 10.1109/ICCV51070.2023.00371](https://doi.org/10.1109/ICCV51070.2023.00371)。本导读依据原始书目与摘要整理，未复现实验。
