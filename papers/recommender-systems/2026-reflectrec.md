---
id: reflectrec
primary_topic: recommender-systems
tags: [llm, preference-verification, retrieval, temporal-evaluation]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://aclanthology.org/2026.emnlp-main.1591/
status: summary
---

# ReflectRec: Cycle-Consistency Preference Verification for LLM-based Recommendation

- 作者：Dae Kyoo Kim、Heejung Cho、Sungmoo Hong、Eunil Park。
- 年份与版本：2026 按正式会议年份。ACL Anthology 记录为 EMNLP 2026 主会，出版月份为 2026-10，页码 36183–36197；arXiv v1 于 2026-11-18（UTC）提交，不能将其当作首次正式发表日期。
- 原始来源：[会议书目](https://aclanthology.org/2026.emnlp-main.1591/) · [arXiv 书目](https://arxiv.org/abs/2611.23969) · [v1 正文](https://arxiv.org/html/2611.23969v1)。
- 官方代码：本次未核实可用的官方代码仓库。

## 解决的问题

语言模型生成的用户偏好描述能否忠实反映交互历史？论文为推荐流程增加可检查的中间信号，避免直接信任偏好文本。[会议摘要](https://aclanthology.org/2026.emnlp-main.1591/)

## 主要方法

从历史生成偏好，再用偏好从候选池恢复历史物品，以召回率决定是否重新生成及保留哪个版本。排序时还检索训练集中相似历史片段的后续行为，作为协同提示。[方法](https://arxiv.org/html/2611.23969v1)

## 贡献与局限

作者在两个 MovieLens 数据集报告完整流程优于 CoT4Rec-ICL，并在电子产品数据中考察偏好重生成。历史可恢复性不是推荐正确性的保证。主实验没有统一的生产时间截断；严格时间约束下，ML-1M 的后续行为检索收益不显著。电子产品上直接使用后续物品标题会降低表现，阈值也需随模型及候选池重新校准。[实验与局限](https://arxiv.org/html/2611.23969v1)

## 前置知识与阅读重点

建议了解序列推荐、检索增强与 Hit@K。重点审查检索信息在预测时刻是否可用，并区分偏好验证、重生成及协同提示各自的贡献。

## 收录理由

补充推荐系统中的偏好验证案例，同时连接本库的数据泄漏专题。近期 arXiv 提交提供核查入口，并不意味着会议论文首次发表于近七日。

## 相关主题与版本

- 正式 DOI：`10.18653/2026.emnlp-main.1591`；arXiv ID：`2611.23969`，对应 DOI `10.48550/arXiv.2611.23969` 在书目页标记待注册。两个入口合并为本条。
- 主主题：[推荐系统](README.md)；相关方向：[评估与实验方法](../evaluation/README.md)、[自然语言处理](../nlp/README.md)。
- 本次核对会议书目、arXiv 版本、方法及局限；未逐页精读、运行代码或复现实验。
