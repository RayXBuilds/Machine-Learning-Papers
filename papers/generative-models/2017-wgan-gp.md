---
id: wgan-gp
primary_topic: generative-models
tags: [gan, gradient-penalty]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://arxiv.org/abs/1704.00028
status: summary
---

# Improved Training of Wasserstein GANs

- 作者：Ishaan Gulrajani、Faruk Ahmed、Martin Arjovsky、Vincent Dumoulin、Aaron C. Courville。
- 年份与版本：按 NIPS 2017 正式发表年份归档。arXiv 初稿提交于 2017 年 4 月。
- 原始来源：[NIPS 会议版](https://papers.nips.cc/paper_files/paper/2017/hash/892c3b1c6dccd52936e27cbd0ff683d6-Abstract.html) · [作者预印本](https://arxiv.org/abs/1704.00028)。
- 官方代码：[作者项目](https://github.com/igul222/improved_wgan_training)。

## 解决的问题

Wasserstein GAN 对评论器权重做截断时，为何仍可能出现梯度和训练问题？

## 主要方法

在真实样本与生成样本之间采样插值点，对评论器输入梯度的范数偏离 1 施加惩罚，替代逐参数截断。

## 贡献与局限

作者在多种架构上展示了训练稳定性。沿采样线段施加软约束不会保证整个输入空间都满足 Lipschitz 条件。

## 前置知识与阅读重点

先理解 Wasserstein 对偶与评论器。注意被求导的变量是输入，并观察惩罚项如何参与评论器参数更新。

## 收录理由

为比较生成模型中的约束方式提供具体目标函数。

## 相关主题与版本

arXiv:1704.00028。延伸阅读见 [GAN](../generative-models/2014-gan.md)。

本条依据作者摘要、书目及项目说明整理，未复现实验。
