---
id: dump-retrieval-prefix-tokens
primary_topic: nlp
tags: [retrieval, embedding, attention-sink, representation-learning]
type: paper
added: 2026-11-10
verified: 2026-11-10
source: https://arxiv.org/abs/2611.07298
status: summary
---

# Reducing Representational Interference in Retrieval Embeddings with Trainable Prefix Tokens

- 作者为 Seongtae Hong、Youngjoon Jang、Jungseob Lee、Chanjun Park、Heuiseok Lim。
- 年份为 2026。arXiv v1 首次提交于 2026-11-05（UTC），书目备注为 CIKM 2026，作者正文列出会议日期 11 月 7–11 日。[书目页](https://arxiv.org/abs/2611.07298)
- 正文列出出版 DOI `10.1145/3799682.3840002`。本次出版商页面访问失败，会议信息据作者原文记录。[作者正文](https://arxiv.org/html/2611.07298v1) · [出版入口](https://doi.org/10.1145/3799682.3840002)
- 本次核对的原始页面未找到官方代码链接，代码可用性待核实。

## 解决的问题

文本压缩为检索向量时，低信息 token 的激活与注意力可能干扰语义匹配。论文研究可训练前缀对这种干扰的影响。[摘要](https://arxiv.org/abs/2611.07298)

## 主要方法

向查询和文档添加 [DUMP] 前缀，新增词嵌入与模型参数通过对比检索目标联合训练。推理沿用前缀编码，前缀通过自注意力参与表征形成。[方法](https://arxiv.org/html/2611.07298v1)

## 贡献与局限

六种模型的平均检索表现有所改善，实验包含长上下文场景。个别数据集分数下降，最佳前缀数量随模型变化。机制分析基于特定模型及数据集，编者认为其因果解释仍需进一步对照验证。[实验与分析](https://arxiv.org/html/2611.07298v1)

## 前置知识与阅读重点

先了解双塔检索、InfoNCE、池化与 attention sink。重点查看训练和推理的编码一致性，并逐数据集检查 nDCG@10 及前缀数量消融。[正文](https://arxiv.org/html/2611.07298v1)

## 收录理由

补充 NLP 主题中检索向量的训练方法，与 RAG 条目的检索环节衔接。编者建议关注表示质量与部署编码配置的关系。

## 相关主题与版本

主主题为[自然语言处理与大语言模型](README.md)，相关主题为[深度学习与表征学习](../deep-learning/README.md)。唯一标识为 arXiv:2611.07298，出版 DOI 见上。arXiv DOI 为 `10.48550/arXiv.2611.07298`，页面标记待注册。已核对书目、方法与实验，状态为导读，实验复现待开展。
