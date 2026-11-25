---
id: graph-aware-diffusion
primary_topic: graph-learning
catalog_year: 2026
subtopic: "图神经网络"
updated: 2026-11-25
tags: [graph-signals, diffusion-models, spectral-methods, imputation]
type: paper
added: 2026-11-25
verified: 2026-11-25
source: https://arxiv.org/abs/2611.27826v1
status: summary
---

# Graph Signal Generation via Graph-Aware Diffusion Models

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Vimal K B、Sergio Rozada、Antonio G. Marques、Elvin Isufi、Hadi J. Rad
- 年份与版本：按 arXiv v1 的提交日 2026-11-20 归档。作者注明稿件正由 IEEE TPAMI 审稿。
- 原始来源：[arXiv 书目与版本记录](https://arxiv.org/abs/2611.27826v1)
- 仓库内 PDF：[打开全文](../../pdfs/graph-learning/2026-graph-aware-diffusion.pdf)（v1，19 页）。
- 官方代码：[作者在论文页链接的 SpectralAnalysisGAD 仓库](https://github.com/vimalkb7/SpectralAnalysisGAD)。本次核对入口，未运行实验。

## 解决的问题

两处相邻的道路传感器有时会同时记录到拥堵，有时读数又会明显分开。要补全缺测值，模型既要学会相邻节点的共同变化，也要保留局部差异。若用图上的热扩散逐步破坏训练信号，局部差异会比平滑趋势更早消失。去噪模型还能从训练样本中学到两者吗？

## 主要方法

作者把图拉普拉斯矩阵的特征向量作为坐标轴。在这些坐标上，节点间变化平缓的模式对应低频，邻接节点间起伏较大的模式对应高频。论文的 MASS 方法为各个图频率分别设置扩散速率，使它们在同一扩散时刻具有相同的信噪比。逆向生成时，模型再利用观测值补全缺失部分。

## 贡献与局限

对满足图平稳性假设的信号，作者证明最优线性去噪器在各频率上的归一化误差可以均衡。实验则考察了推荐、交通缺测补全和预测。阅读结果时要分别看理论和实验：频率间误差均衡有明确的模型假设，某个缺测节点的预测是否更准，仍取决于任务数据和图的连接方式。

## 前置知识与阅读重点

建议先了解图拉普拉斯矩阵、图傅里叶变换和扩散模型的前向加噪过程。读到噪声调度时，可选一个低频模式和一个高频模式，先画出共享速率下二者的衰减，再对比 MASS 如何改变这两条曲线。这里的频率描述相邻节点间的变化，并非一天中车流的周期。

## 收录理由

把图结构放进前向加噪过程，让读者能具体比较两种设计：图如何决定训练信号被破坏的方式，以及去噪网络如何从中恢复节点值。可与库中的[图卷积网络](2017-gcn.md)对读。

## 相关主题与版本

作者在引言中将[较早的工作](https://arxiv.org/abs/2510.05036)列为初步版本。早期方法使用共享扩散速率，本稿进一步提出按频率调度的 MASS，补充了谱分析和实验。本条收录 2026 年扩展稿。
