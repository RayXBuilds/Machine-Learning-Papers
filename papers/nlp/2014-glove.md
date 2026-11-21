---
id: glove
primary_topic: nlp
tags: [word-embeddings, cooccurrence]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://aclanthology.org/D14-1162/
status: summary
---

# GloVe: Global Vectors for Word Representation

- 作者：Jeffrey Pennington、Richard Socher、Christopher D. Manning
- 年份与版本：EMNLP 2014。
- 原始来源：[论文入口](https://aclanthology.org/D14-1162/)
- 官方代码：[作者项目](https://github.com/stanfordnlp/GloVe)

## 解决的问题

怎样把全语料的共现关系编码进低维向量，同时控制极常见词对对目标函数的影响？

## 主要方法

从上下文概率比的例子出发，对非零词对的对数共现次数做加权最小二乘拟合，内积和偏置共同给出预测。

## 贡献与局限

论文用类比与词相似度任务检查表示。每个词型共享静态向量，阅读结果时应考虑多义词和语料域的限制。

## 前置知识与阅读重点

先了解滑动窗口与内积。观察权重函数怎样区别低频和高频词对，再与 Skip-gram 的局部训练样本比较。

## 收录理由

补上词嵌入中从全局统计出发的一条路线。

## 相关主题与版本

[主主题：自然语言处理与大语言模型](README.md) · [延伸主题：深度学习与表征学习](../deep-learning/README.md) · [DOI 10.3115/v1/D14-1162](https://doi.org/10.3115/v1/D14-1162)

本条依据原始书目和论文内容整理，未复现实验。
