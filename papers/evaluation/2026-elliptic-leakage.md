---
id: elliptic-leakage
primary_topic: evaluation
tags: [data-leakage, temporal-evaluation, reproducibility, bitcoin-forensics]
type: paper
added: 2026-11-15
verified: 2026-11-15
source: https://arxiv.org/abs/2611.04000
status: summary
catalog_year: 2026
subtopic: "实验设计与数据有效性"
updated: 2026-11-21
---

# Revisiting Elliptic++ for Bitcoin Forensics: Feature Reconstruction and Leakage-Resistant Evaluation

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Runlin Liang、Simon Trimborn、Noud van Giersbergen。
- 年份与版本：2026 按预印本 v1 年份。首次提交于 2026-11-02（UTC），核对时为 v1。未核实会议或期刊接收信息。
- 原始来源：[arXiv 书目](https://arxiv.org/abs/2611.04000) · [v1 正文](https://arxiv.org/html/2611.04000v1)。
- 官方代码：[论文提供的代码仓库](https://github.com/DukHaanYumCha/Leakage-Resistant-Elliptic_pp)，正文注明为评审匿名链接。本库未运行代码。

- 仓库内 PDF：[打开全文](../../pdfs/evaluation/2026-elliptic-leakage.pdf)（arXiv 2611.04000v1）。

## 解决的问题

Elliptic++ 地址分类的高分是否受到未来信息影响？作者检查原有样本划分与特征时间范围，识别可能夸大泛化表现的泄漏。[摘要](https://arxiv.org/abs/2611.04000)

## 主要方法

关联公开账本，恢复 55 项地址特征的定义。按地址首次出现时间划分训练与测试数据，并在截止时点截断训练特征的历史范围。[方法](https://arxiv.org/html/2611.04000v1)

## 贡献与局限

作者报告随机森林的非法类别 F1 从原设置的 0.846 降至新流程的 0.291。该比较同时涉及划分与特征处理，不能把降幅全部归给单一因素。实验保留冗余特征、默认超参数和 0.5 阈值，未充分调优基线，结论限于所测流程。[表 4 与讨论](https://arxiv.org/html/2611.04000v1)

## 前置知识与阅读重点

建议了解时间切分、随机森林、逻辑回归与类别不平衡。重点比较表 4 的三个设置，检查缩放器拟合范围，以及每项特征在预测时是否可得。

## 收录理由

补充维护队列中的数据泄漏专题。虽早于近七日窗口，但提供了从特征来源到评估协议的具体审查案例。

## 相关主题与版本

- arXiv ID：`2611.04000`。书目页列 DOI `10.48550/arXiv.2611.04000`，注明待注册。
- 主文件归入[评估与实验方法](README.md)，相关方向为[领域应用](../applications/README.md)。
- 本条核对书目、方法、实验表与局限，未进行全文精读或实验复现。
