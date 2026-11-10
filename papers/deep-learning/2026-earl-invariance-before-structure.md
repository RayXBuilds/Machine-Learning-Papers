---
id: earl-invariance-before-structure
primary_topic: deep-learning
tags: [representation-learning, information-theory, reservoir-computing, evaluation]
type: paper
added: 2026-11-10
verified: 2026-11-10
source: https://arxiv.org/abs/2611.07952
status: summary
---

# Invariance before structure: two modes of emergent compression in representation learning

- 作者为 Hardik Rajpal、Dan Goodman。
- 年份采用预印本 v1 的 2026 年，首次提交于 2026-11-05（UTC）。当前核对版本为 v1，书目备注为 NeurIPS 2026 UniReps workshop 扩展摘要，正式接收状态待核实。[书目页](https://arxiv.org/abs/2611.07952)
- 原始正文给出 EARL 框架、指标和对照实验。本次核对的书目页及正文未列出官方代码链接，代码可用性待核实。[正文](https://arxiv.org/html/2611.07952v1)

## 解决的问题

不同参数的网络为何学到相似表征，这种一致性如何随任务学习形成？论文将表征对底层参数的不变性与其时间预测结构分别研究。[摘要](https://arxiv.org/abs/2611.07952)

## 主要方法

EARL 用互信息指标衡量状态空间压缩和参数空间压缩。在固定随机循环储备池上训练瓶颈，通过参数集成与时间打乱等对照观察学习轨迹。[方法与实验](https://arxiv.org/html/2611.07952v1)

## 贡献与局限

作者观察到参数不变性先于任务相关预测结构增强。证据来自储备池与合成吸引子设置。状态指标全程为负，解释依赖相对变化及时间采样；参数指标需要任务相关潜变量，衡量跨模型一致性。推广到其他架构仍需验证。[结果与讨论](https://arxiv.org/html/2611.07952v1)

## 前置知识与阅读重点

建议先了解互信息、信息瓶颈与储备池计算。重点核对公式 1、2 的测量对象，并结合打乱目标对照理解早期变化。[正文](https://arxiv.org/html/2611.07952v1)

## 收录理由

补充深度表征主题中的训练动态与指标解释。编者建议将“相似表征如何形成”作为阅读问题，与现有 SimCLR 条目联系阅读。

## 相关主题与版本

主主题为[深度学习与表征学习](README.md)，相关主题为[评估与实验方法](../evaluation/README.md)。唯一标识为 arXiv:2611.07952，页面列出的 DOI 为 `10.48550/arXiv.2611.07952`，当前标记待注册。已核对书目、方法及讨论，状态为导读，实验复现待开展。
