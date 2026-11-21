---
id: show-attend-tell
primary_topic: multimodal
tags: [visual-attention, captioning]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://proceedings.mlr.press/v37/xuc15.html
status: summary
catalog_year: 2015
subtopic: "图文建模与生成描述"
updated: 2026-11-21
---

# Show, Attend and Tell: Neural Image Caption Generation with Visual Attention

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Kelvin Xu、Jimmy Ba、Ryan Kiros、Kyunghyun Cho、Aaron Courville、Ruslan Salakhudinov、Rich Zemel、Yoshua Bengio
- 年份与版本：ICML 2015；arXiv 首版同年。
- 原始来源：[论文入口](https://proceedings.mlr.press/v37/xuc15.html)
- 官方代码：[作者项目](https://github.com/kelvinxu/arctic-captions)

- 仓库内 PDF：[打开全文](../../pdfs/multimodal/2015-show-attend-tell.pdf)（arXiv 1502.03044v3）。

## 解决的问题

生成图像描述时，每个词可能对应不同区域，单一的整图表示怎样提供这种局部信息？

## 主要方法

保留卷积特征的空间网格，在每个解码步根据隐藏状态计算区域权重；比较加权平均的软注意力与抽样位置的硬注意力。

## 贡献与局限

作者同时报告描述质量与可视化。注意力图提供观察窗口，只靠图例无法证明某一区域对词预测有因果作用。

## 前置知识与阅读重点

先掌握条件语言模型与空间特征图。对比两种注意力的训练梯度，以及训练和生成时位置选择的差异。

## 收录理由

用同一个描述任务比较确定性与随机注意力的代价。

## 相关主题与版本

[主主题：多模态学习](README.md) · [延伸主题：计算机视觉](../computer-vision/README.md) · [arXiv:1502.03044](https://arxiv.org/abs/1502.03044)

本条依据原始书目和论文内容整理，未复现实验。
