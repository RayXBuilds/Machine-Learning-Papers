---
id: lightgcn
primary_topic: recommender-systems
tags: [collaborative-filtering, graph-learning]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://arxiv.org/abs/2002.02126
status: summary
---

# LightGCN: Simplifying and Powering Graph Convolution Network for Recommendation

- 作者：Xiangnan He、Kuan Deng、Xiang Wang、Yan Li、Yongdong Zhang、Meng Wang。
- 年份与版本：按 SIGIR 2020 正式发表年份归档。arXiv 初稿提交于 2020 年 2 月。
- 原始来源：[SIGIR 会议版](https://doi.org/10.1145/3397271.3401063) · [作者预印本](https://arxiv.org/abs/2002.02126)。
- 官方代码：[作者项目](https://github.com/kuandeng/LightGCN)。

## 解决的问题

只有用户和物品交互时，图卷积中的特征变换与非线性是否都对推荐有益？

## 主要方法

在用户–物品二部图上传播归一化嵌入，合并不同深度及初始层的表示，再用用户和物品向量内积打分。

## 贡献与局限

消融展示了简化传播在所测协同过滤任务中的效果。方法依赖历史交互，缺少交互的新物品难以靠这些边得到表示。

## 前置知识与阅读重点

先了解隐式反馈和二部图。沿一条两跳路径追踪同类节点的信息，再看最终表示为何保留第零层。

## 收录理由

连接矩阵分解与图传播，说明如何用消融检验推荐模型中的复杂组件。

## 相关主题与版本

arXiv:2002.02126；会议 DOI 为 [10.1145/3397271.3401063](https://doi.org/10.1145/3397271.3401063)。延伸阅读见 [GCN](../graph-learning/2017-gcn.md)。

本条依据作者摘要、书目及项目说明整理，未复现实验。
