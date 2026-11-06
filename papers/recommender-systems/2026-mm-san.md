---
id: mm-san
primary_topic: recommender-systems
tags: [dataset-recommendation, graph-learning, multimodal, cold-start]
type: paper
added: 2026-11-06
verified: 2026-11-06
source: https://arxiv.org/abs/2611.05071
status: summary
---

# Dataset Recommendation for Heterogeneous and Dynamic Scholarly Graphs via Multimodal Representation Learning

- 作者为 Ornella Irrera、Matteo Lissandrini、Daniele Dell’Aglio、Gianmaria Silvello。
- 年份采用预印本 v1 的 2026 年，首次提交于 2026-11-03。原文首页注明已获 ACM Transactions on Recommender Systems 接收，正式卷期、出版日期及出版 DOI 待核实。当前导读对应 [arXiv v1](https://arxiv.org/abs/2611.05071v1)。
- 原始来源为 [arXiv 书目页](https://arxiv.org/abs/2611.05071)与[正文](https://arxiv.org/html/2611.05071v1)。
- 官方代码为 [OrnellaIrrera/MM-SAN](https://github.com/OrnellaIrrera/MM-SAN)，由原文链接确认。已核对仓库 README，训练、基线及消融运行待开展。

## 解决的问题

给定研究论文，如何在关系稀疏、描述缺失且不断加入新节点的学术知识图谱中推荐可用数据集。观测到的论文与数据集关联并不完整，相关资源可能缺少显式连接。[原文](https://arxiv.org/abs/2611.05071)

## 主要方法

MM-SAN 用实体与主题扩充图，再通过随机游走选取兼顾节点类型的邻居。分组交叉注意力融合文本和拓扑表示，拼接得到节点向量，以向量内积排列候选数据集。这里的两种模态是文本与图结构。[方法第 4 节](https://arxiv.org/html/2611.05071v1#S4)

## 贡献与局限

作者在 MES、PubMed 两个 OpenAIRE 子图上比较传导、半归纳和完全归纳设置，并逐步减少文本元数据。贡献在于把新节点和信息缺失纳入同一推荐评估。局限包括图谱漏边造成的假负例，以及随机移除元数据与实际缺失机制的差异。编者判断，向其他领域迁移仍需独立验证。[实验设置第 5 节](https://arxiv.org/html/2611.05071v1#S5)

## 前置知识与阅读重点

先了解异构图、注意力和 Recall、MRR、nDCG。重点核查测试节点及其关联边怎样从训练图移除，并区分新论文与新数据集同时出现的设置。复现入口已提供数据划分、基线和消融说明，README 要求 Docker 与 GPU。[代码说明](https://github.com/OrnellaIrrera/MM-SAN/blob/main/README.md)

## 收录理由

补充推荐系统主题中面向科研数据发现的案例，连接图学习、冷启动与缺失信息处理。适合与传统协同过滤对照阅读。

## 相关主题与版本

主主题为[推荐系统](README.md)，相关方向为[图学习](../graph-learning/README.md)及[多模态学习](../multimodal/README.md)。标识为 arXiv:2611.05071，页面列出的 DOI 为 `10.48550/arXiv.2611.05071`，当前标记待注册。已核对书目、相关方法、实验设置与代码 README，状态为导读，实验复现待开展。
