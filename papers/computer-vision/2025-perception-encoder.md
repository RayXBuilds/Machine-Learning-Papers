---
id: perception-encoder
primary_topic: computer-vision
tags: [visual-representation, multimodal]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://proceedings.neurips.cc/paper_files/paper/2025/hash/57bc0a850255e2041341bf74c7e2b9fa-Abstract-Conference.html
status: summary
catalog_year: 2025
subtopic: "分类与视觉表征"
updated: 2026-11-21
---

# Perception Encoder: The best visual embeddings are not at the output of the network

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Daniel Bolya、Po-Yao Huang、Peize Sun 等（完整署名见原文）。
- 年份与版本：NeurIPS 2025。arXiv 首版提交于 2025-04-17。
- 原始来源：[NeurIPS 2025 书目](https://proceedings.neurips.cc/paper_files/paper/2025/hash/57bc0a850255e2041341bf74c7e2b9fa-Abstract-Conference.html) · [arXiv 版本记录](https://arxiv.org/abs/2504.13181)。
- 官方代码：已核对[作者项目仓库](https://github.com/facebookresearch/perception_models)。

## 解决的问题

同一视觉编码器里，最适合全局检索和局部定位的特征是否来自同一层？

## 主要方法

扩展图文对比预训练并加入视频数据，逐层分析表示，再分别以语言对齐和空间对齐适配多模态问答与稠密预测。

## 贡献与局限

作者在分类检索、问答和空间任务上展示不同层的价值。比较时需同时考虑特征层、对齐训练和下游解码器。

## 前置知识与阅读重点

熟悉视觉 Transformer 和线性探测即可。先看冻结特征的逐层曲线，再看加入对齐训练后的结果。

## 收录理由

提醒使用预训练编码器时把层选择本身列为实验变量。

## 相关主题与版本

arXiv:2504.13181。[正式 DOI 10.52202/085713-2036](https://doi.org/10.52202/085713-2036)。本导读依据原始书目与摘要整理，未复现实验。
