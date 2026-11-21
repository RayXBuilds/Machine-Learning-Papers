---
id: unaligned-ordinal-transfer
primary_topic: classical-ml
tags: [transfer-learning, ordinal-regression, high-dimensional-statistics, regularization]
type: paper
added: 2026-11-19
verified: 2026-11-19
source: https://arxiv.org/abs/2611.20411
status: summary
catalog_year: 2026
subtopic: "表格学习与迁移"
updated: 2026-11-21
---

# High-dimensional transfer learning with unaligned ordinal responses

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Ruopei Fu、Ying Yang。
- 年份与版本：2026 按预印本 v1 年份，首次提交于 2026-11-16（UTC），核对时为 v1。未核实会议或期刊接收信息。
- 原始来源：[arXiv 书目](https://arxiv.org/abs/2611.20411) · [v1 正文](https://arxiv.org/pdf/2611.20411v1)。
- 官方代码：未在上述原始来源中找到本论文的官方代码链接。

## 解决的问题

源域和目标域可能采用不同等级数量或定义的有序标签。论文研究这种响应空间不对齐时，如何在高维回归中迁移信息。[摘要](https://arxiv.org/abs/2611.20411)

## 主要方法

分别建立累积链接模型，允许系数、链接与阈值不同。先合并似然做惩罚估计，再以目标数据修正偏差。sample-split 分开使用目标子样本，full-target 在两阶段复用全部目标观测。[方法](https://arxiv.org/pdf/2611.20411v1)

## 贡献与局限

作者给出估计误差及超额风险界，仿真支持 full-target 的有限样本表现。理论依赖系数接近等条件，full-target 的对应最优速率还要求源样本量不超过目标样本量的常数倍。链接形状估计、无序标签迁移及严重源域偏移的自适应处理仍待研究。[第 6 节](https://arxiv.org/pdf/2611.20411v1)

## 前置知识与阅读重点

建议了解有序回归、Lasso 与极小极大速率。重点区分标签不对齐和系数差异，检查修正阶段的数据使用方式，以及新增源样本是否真的有帮助。

## 收录理由

补充传统机器学习中的迁移学习方向，为多套等级标签之间的信息共享提供具体建模案例。

## 相关主题与版本

- arXiv ID：`2611.20411`。书目页列 DOI `10.48550/arXiv.2611.20411`，注明待注册。
- 主文件归入[传统机器学习](README.md)，相关方向为[数学、学习理论与概率模型](../foundations/README.md)。
- 本条核对书目、方法及讨论，未独立验证完整证明或复现实验。
