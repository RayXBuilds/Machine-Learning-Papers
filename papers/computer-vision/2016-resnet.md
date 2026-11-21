---
id: resnet
primary_topic: computer-vision
type: paper
added: 2026-10-25
verified: 2026-10-25
source: https://arxiv.org/abs/1512.03385
status: summary
tags: ["residual-learning", "image-classification"]
catalog_year: 2016
subtopic: "分类与视觉表征"
updated: 2026-11-21
---

# Deep Residual Learning for Image Recognition

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 常用名称：ResNet。
- 作者：Kaiming He、Xiangyu Zhang、Shaoqing Ren、Jian Sun。
- 年份与版本：2016 · CVPR；预印本首发 2015。
- 原始来源：[原文](https://arxiv.org/abs/1512.03385)。
- 官方代码：原导读未单独核实，本次编排未新增代码可用性声明。

- 仓库内 PDF：[打开全文](../../pdfs/computer-vision/2016-resnet.pdf)（arXiv 1512.03385v1）。

## 解决的问题

如何改善深层网络优化中的退化问题？

## 主要方法

学习残差连接如何改变深层网络的优化问题，区分退化问题与过拟合。

## 贡献与局限

本条提供方法入门线索；具体实验收益与适用条件仍需结合原文核对。阅读时重点辨析：为什么拟合残差与直接拟合目标映射的优化行为不同？

## 前置知识与阅读重点

建议前置：CNN、反向传播。

阅读顺序：先看方法定义，再结合上方阅读问题核查原文中的假设和实验条件。

## 收录理由

作为本主题的基础阅读入口，可与[学习路线](../../docs/reading-paths.md)中的相关方法对照阅读。

## 相关主题与版本

年份与版本口径沿用上述书目信息。

[主题目录](README.md) · [原经典索引](../../docs/classics.md#resnet) · [年份导航](../../docs/years/README.md)

> 本次仅重组已有书目与阅读提示，未新增实验结论，也未重新核验原文；原 verified 日期保持不变。导读不代表全文精读或实验复现。
