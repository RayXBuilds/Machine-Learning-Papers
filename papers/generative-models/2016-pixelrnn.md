---
id: pixelrnn
primary_topic: generative-models
tags: [autoregression, image-modeling]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://proceedings.mlr.press/v48/oord16.html
status: summary
---

# Pixel Recurrent Neural Networks

- 作者：Aäron van den Oord、Nal Kalchbrenner、Koray Kavukcuoglu
- 年份与版本：ICML 2016；arXiv 首版同年。
- 原始来源：[论文入口](https://proceedings.mlr.press/v48/oord16.html)
- 官方代码：在本次核对的一手来源中未确认论文配套实现。

## 解决的问题

怎样为整幅图像写出可直接计算的概率，同时利用远处像素与颜色通道之间的依赖？

## 主要方法

按给定顺序把联合分布分解为离散像素条件分布，用行 LSTM 或对角双向 LSTM 扩大可见上下文，并遮蔽未来输入。

## 贡献与局限

模型可直接优化对数似然。按条件分布逐像素采样仍需串行推进，训练时的并行度不能直接转化为生成速度。

## 前置知识与阅读重点

先了解概率链式法则与循环网络。画出一个目标像素可见的上下文，再检查掩码如何阻止读取待预测通道。

## 收录理由

在 VAE 和 GAN 之外补上以精确似然为目标的图像生成方法。

## 相关主题与版本

[主主题：生成模型](README.md) · [延伸主题：计算机视觉](../computer-vision/README.md) · [arXiv:1601.06759](https://arxiv.org/abs/1601.06759)

本条依据原始书目和论文内容整理，未复现实验。
