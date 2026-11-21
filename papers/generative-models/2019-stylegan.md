---
id: stylegan
primary_topic: generative-models
tags: [gan, style-control]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://arxiv.org/abs/1812.04948
status: summary
catalog_year: 2019
subtopic: "对抗生成"
updated: 2026-11-21
---

# A Style-Based Generator Architecture for Generative Adversarial Networks

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Tero Karras、Samuli Laine、Timo Aila。
- 年份与版本：按 CVPR 2019 正式发表年份归档。arXiv 初稿提交于 2018 年 12 月。
- 原始来源：[CVPR 会议版](https://openaccess.thecvf.com/content_CVPR_2019/html/Karras_A_Style-Based_Generator_Architecture_for_Generative_Adversarial_Networks_CVPR_2019_paper.html) · [作者预印本](https://arxiv.org/abs/1812.04948)。
- 官方代码：[作者项目](https://github.com/NVlabs/stylegan)。

- 仓库内 PDF：[打开全文](../../pdfs/generative-models/2019-stylegan.pdf)（arXiv 1812.04948v3）。

## 解决的问题

能否分别控制合成图像的整体布局和局部随机细节？

## 主要方法

映射网络先将潜变量送入中间空间，逐层用风格参数调制特征，同时为各尺度注入独立噪声。

## 贡献与局限

风格混合和噪声实验展示了分尺度控制。属性分离是训练中的经验现象，不能据此假定每个方向只对应一种语义。

## 前置知识与阅读重点

先了解卷积生成器。对照固定风格换噪声、只替换粗层风格两种实验，观察变化的位置和尺度。

## 收录理由

为阅读后续生成器的风格控制、插值和解耦指标建立参照。

## 相关主题与版本

arXiv:1812.04948；会议 DOI 为 [10.1109/CVPR.2019.00453](https://doi.org/10.1109/CVPR.2019.00453)。延伸阅读见 [GAN](../generative-models/2014-gan.md)。

本条依据作者摘要、书目及项目说明整理，未复现实验。
