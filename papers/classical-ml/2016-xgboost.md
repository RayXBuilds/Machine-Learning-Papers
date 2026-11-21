---
id: xgboost
primary_topic: classical-ml
type: paper
added: 2026-10-25
verified: 2026-10-25
source: https://arxiv.org/abs/1603.02754
status: summary
tags: ["boosting", "decision-trees"]
catalog_year: 2016
subtopic: "分类与集成"
updated: 2026-11-21
---

# XGBoost: A Scalable Tree Boosting System

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 常用名称：XGBoost。
- 作者：Tianqi Chen、Carlos Guestrin。
- 年份与版本：2016 · KDD。
- 原始来源：[原文](https://arxiv.org/abs/1603.02754)。
- 官方代码：原导读未单独核实，本次编排未新增代码可用性声明。

- 仓库内 PDF：[打开全文](../../pdfs/classical-ml/2016-xgboost.pdf)（arXiv 1603.02754v3）。

## 解决的问题

如何把梯度提升树的学习目标与高效系统实现结合？

## 主要方法

把梯度提升树的目标函数与稀疏数据处理、近似分裂和系统优化联系起来。

## 贡献与局限

本条提供方法入门线索；具体实验收益与适用条件仍需结合原文核对。阅读时重点辨析：哪些收益来自学习目标，哪些来自工程实现？

## 前置知识与阅读重点

建议前置：决策树、梯度提升、泰勒展开。

阅读顺序：先看方法定义，再结合上方阅读问题核查原文中的假设和实验条件。

## 收录理由

作为本主题的基础阅读入口，可与[学习路线](../../docs/reading-paths.md)中的相关方法对照阅读。

## 相关主题与版本

年份与版本口径沿用上述书目信息。

[主题目录](README.md) · [原经典索引](../../docs/classics.md#xgboost) · [年份导航](../../docs/years/README.md)

> 本次仅重组已有书目与阅读提示，未新增实验结论，也未重新核验原文；原 verified 日期保持不变。导读不代表全文精读或实验复现。
