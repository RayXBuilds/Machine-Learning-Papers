---
id: caelum
primary_topic: evaluation
tags: [conformal-prediction, uncertainty, semantic-coverage, nlp]
type: paper
added: 2026-11-12
verified: 2026-11-12
source: https://arxiv.org/abs/2611.10738
status: summary
---

# Matchability-Aware Conformal Prediction for Open-Ended Language Model Generation

- 作者为 Ilia Azizi。
- 年份采用 2026 年，arXiv v1 首次提交于 2026-11-07（UTC）。本次核对版本为 v1，作者书目备注注明已被 NeurIPS 2026 接收，正式会议出版页待核实。[书目页](https://arxiv.org/abs/2611.10738)
- 官方项目页介绍 CAELUM 的语义预测集与覆盖界，并链接代码。[项目页](https://unco3892.github.io/caelum/)
- 官方仓库包含生成、匹配、校准和缓存分析入口。已核对 README，运行验证待开展。[作者代码](https://github.com/Unco3892/caelum)

## 解决的问题

开放式生成的候选回答可能完全遗漏参考答案，导致语义预测集的实际覆盖受到候选支持集限制。论文研究这一限制如何进入共形预测保证。[摘要](https://arxiv.org/abs/2611.10738)

## 主要方法

CAELUM 在多种澄清提示下采样回答并做语义聚类，用核 von Neumann 熵构造不确定性分量与加权分数，再做分割共形校准。另用问题特征预测参考答案可匹配性，建立含误判惩罚的分层覆盖界。[方法](https://arxiv.org/html/2611.10738v1)

## 贡献与局限

贡献在于明确候选支持集对覆盖率的上限及分层保证条件。保证依赖可交换性和预先固定的评分、分类及匹配流程。澄清间差异与真实歧义的关联较弱，权重选择可能不稳定，预测集大小与基线相近。实验集中于短答案问答，多次生成也带来计算开销。[讨论与局限](https://arxiv.org/html/2611.10738v1)

## 前置知识与阅读重点

先了解分割共形预测、语义熵与校准数据划分。重点核对分层覆盖所对应的人群、选择比例和可匹配性误判率，并将语义覆盖与含拒答的覆盖指标分别阅读。[覆盖界说明](https://unco3892.github.io/caelum/)

## 收录理由

补充评估主题中的生成式模型不确定性与覆盖保证。编者建议围绕“参考答案能否出现在候选集中”审视校准指标，并联系已有概率校准导读阅读。

## 相关主题与版本

主主题为[评估与实验方法](README.md)，相关主题为[自然语言处理与大语言模型](../nlp/README.md)。唯一标识为 arXiv:2611.10738，书目页列出 DOI `10.48550/arXiv.2611.10738`，当前标记待注册。已核对书目、方法、讨论及官方代码说明，状态为导读，实验复现待开展。
