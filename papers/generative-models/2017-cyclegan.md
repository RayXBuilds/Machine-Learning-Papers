---
id: cyclegan
primary_topic: generative-models
tags: [image-translation, cycle-consistency]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://arxiv.org/abs/1703.10593
status: summary
---

# Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks

- 作者：Jun-Yan Zhu、Taesung Park、Phillip Isola、Alexei A. Efros。
- 年份与版本：按 ICCV 2017 正式发表年份归档。arXiv 初稿提交于 2017 年 3 月。
- 原始来源：[ICCV 会议版](https://openaccess.thecvf.com/content_iccv_2017/html/Zhu_Unpaired_Image-To-Image_Translation_ICCV_2017_paper.html) · [作者预印本](https://arxiv.org/abs/1703.10593)。
- 官方代码：[作者项目](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)。

## 解决的问题

只有两个域各自的图像集合时，怎样学习图像翻译？

## 主要方法

两个生成器分别完成正向和反向映射。判别器检查输出是否像目标域，循环一致性损失检查往返后能否重建输入。

## 贡献与局限

作者在无配对数据上展示了外观迁移。能往返重建的映射可能有多个，尤其要检查形状需要改变的样例。

## 前置知识与阅读重点

先了解 GAN。对同一张输入分别追踪判别损失和循环损失，判断它们各自能发现哪类错误。

## 收录理由

提供无配对监督的实例，可用来讨论约束为何不足以唯一确定语义映射。

## 相关主题与版本

arXiv:1703.10593；会议 DOI 为 [10.1109/ICCV.2017.244](https://doi.org/10.1109/ICCV.2017.244)。延伸阅读见 [GAN](../generative-models/2014-gan.md)。

本条依据作者摘要、书目及项目说明整理，未复现实验。
