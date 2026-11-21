---
id: tabicl
primary_topic: classical-ml
tags: [tabular-classification, in-context-learning]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://proceedings.mlr.press/v267/qu25d.html
status: summary
catalog_year: 2025
subtopic: "表格学习与迁移"
updated: 2026-11-21
---

# TabICL: A Tabular Foundation Model for In-Context Learning on Large Data

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Jingang Qu、David Holzmüller、Gaël Varoquaux、Marine Le Morvan。
- 年份与版本：ICML 2025。arXiv 首版提交于 2025-02-08。
- 原始来源：[ICML 2025 书目](https://proceedings.mlr.press/v267/qu25d.html) · [arXiv 版本记录](https://arxiv.org/abs/2502.05564)。
- 官方代码：已核对[作者项目仓库](https://github.com/soda-inria/tabicl)。

- 仓库内 PDF：[打开全文](../../pdfs/classical-ml/2025-tabicl.pdf)（arXiv 2502.05564v2）。

## 解决的问题

把已标注样本当上下文预测测试标签时，如何处理样本数较多的表格？

## 主要方法

先在列与行上构建定长行表示，再用上下文学习模块根据训练行预测测试标签；预训练阶段在合成分类任务上学习这种推断。

## 贡献与局限

作者比较多个公开分类数据集，并单列超过一万条样本的任务。分类上的结果需要与回归、极端稀疏特征等设置分开看。

## 前置知识与阅读重点

需要熟悉树模型基线与上下文学习。留意预训练成本、单表推理开销及上下文长度分别怎样统计。

## 收录理由

为传统表格分类基线提供不逐表更新参数的比较对象。

## 相关主题与版本

arXiv:2502.05564。可对读 [XGBoost](../classical-ml/2016-xgboost.md)。本导读依据原始书目与摘要整理，未复现实验。
