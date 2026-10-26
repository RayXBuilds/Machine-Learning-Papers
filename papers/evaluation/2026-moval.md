---
id: moval
primary_topic: evaluation
tags: [calibration, domain-shift, performance-estimation]
type: paper
added: 2026-10-26
verified: 2026-10-26
source: https://arxiv.org/abs/2610.29262
status: summary
---

# Estimating Performance for Safe Deployment of Machine Learning Models

[主题目录](README.md) · [首页](../../README.md)

- 作者：Zeju Li、Konstantinos Kamnitsas、Mobarakol Islam、Melanie Roschewitz、Cheng Ouyang、Chen Chen、Ben Glocker。
- 年份与版本：2026-10-21 · arXiv:2610.29262v1；作者备注已被 Medical Image Analysis 接收，正式卷期与期刊 DOI 本次未独立核实。
- 原始来源：[原文入口](https://arxiv.org/abs/2610.29262)。
- 官方代码：[MOVAL 实现](https://github.com/ZerojumpLine/MOVAL)；论文另列 [实验脚本](https://github.com/ZerojumpLine/moval_scripts)。
- 核对日期：2026-10-26；本条为摘要与指定章节导读，未宣称全文精读。

## 解决的问题

部署数据分布发生变化、目标域没有标签时，如何估计模型表现，且不只关注总体准确率？

## 主要方法

利用有标签的源域验证集做类别级校准，再将多个置信度分数及其集成用于无标签目标域的性能估计，覆盖 F1、AUC 等指标及分割任务。

## 贡献与局限

将类别不平衡、多指标和多粒度估计放进统一框架。无标签指目标域评估阶段，并非完全不需要标签；作者明确其是部署辅助工具，不提供单样本覆盖保证，也不能单独保证部署安全。

## 前置知识与阅读重点

前置：概率校准、类别不平衡、分布偏移。重点读问题设定与结论，区分“估计指标”和“使用真实标签测得指标”。

## 收录理由

近七日提交，补充校准如何服务部署后评估的具体实例。

## 相关主题与版本

作者说明其扩展了 MICCAI 2022 初步工作，本条对应 2026 年稿件。已核对[正文问题设定、结论与代码说明](https://arxiv.org/html/2610.29262v1)，未复现实验。
