---
id: imagenetv2
primary_topic: evaluation
tags: [benchmark, dataset-shift]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://arxiv.org/abs/1902.10811
status: summary
catalog_year: 2019
subtopic: "实验设计与数据有效性"
updated: 2026-11-21
---

# Do ImageNet Classifiers Generalize to ImageNet?

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Benjamin Recht、Rebecca Roelofs、Ludwig Schmidt、Vaishaal Shankar。
- 年份与版本：按 ICML 2019 正式发表年份归档。arXiv 初稿提交于 2019 年 2 月。
- 原始来源：[ICML 会议版](https://proceedings.mlr.press/v97/recht19a) · [作者预印本](https://arxiv.org/abs/1902.10811)。
- 官方代码：[作者项目](https://github.com/modestyachts/ImageNetV2)（ImageNetV2 数据与评估资源）。

- 仓库内 PDF：[打开全文](../../pdfs/evaluation/2019-imagenetv2.pdf)（arXiv 1902.10811v2）。

## 解决的问题

多年反复使用同一测试集后，模型进步能否在重新采集的图像上重现？

## 主要方法

作者尽量沿用原采集流程，为 CIFAR-10 与 ImageNet 构建新测试集，在相同模型上比较原测试集和新测试集准确率。

## 贡献与局限

新测试集上准确率整体下降，而原基准上更好的模型通常仍有优势。仅凭下降无法把选样难度和反复使用测试集的影响分开。

## 前置知识与阅读重点

先理解独立测试集与选择偏差。阅读新样本的筛选标准，再检查不同采样规则下的准确率关系。

## 收录理由

为判断榜单进步和分析数据分布变化提供一次具体的复测。

## 相关主题与版本

arXiv:1902.10811。延伸阅读见 [WILDS](../evaluation/2021-wilds.md)。

本条依据作者摘要、书目及项目说明整理，未复现实验。
