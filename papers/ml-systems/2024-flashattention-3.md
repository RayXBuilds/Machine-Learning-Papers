---
id: flashattention-3
primary_topic: ml-systems
tags: [attention, gpu]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://proceedings.neurips.cc/paper/2024/hash/7ede97c3e082c6df10a8d6103a2eebd2-Abstract-Conference.html
status: summary
catalog_year: 2024
subtopic: "推理与硬件效率"
updated: 2026-11-21
---

# FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Jay Shah、Ganesh Bikshandi、Ying Zhang、Vijay Thakkar、Pradeep Ramani、Tri Dao。
- 年份与版本：NeurIPS 2024。arXiv 首版提交于 2024-07-11。
- 原始来源：[NeurIPS 2024 书目](https://proceedings.neurips.cc/paper/2024/hash/7ede97c3e082c6df10a8d6103a2eebd2-Abstract-Conference.html) · [arXiv 版本记录](https://arxiv.org/abs/2407.08608)。
- 官方代码：已核对[作者项目仓库](https://github.com/Dao-AILab/flash-attention)。

## 解决的问题

当访存已做分块优化，Hopper 上的注意力核还有哪些空闲周期？

## 主要方法

用不同 warp 角色重叠数据传输与张量核计算，并交错矩阵乘法与 softmax；另行研究 FP8 分块量化的误差。

## 贡献与局限

作者在 H100 上测量速度和精度。硬件代际、矩阵形状及数据类型都会改变瓶颈，核函数结果不能直接代表整模型吞吐。

## 前置知识与阅读重点

理解分块注意力与在线 softmax 后，沿时间线观察搬运、乘法和归约哪些阶段能重叠。

## 收录理由

解释同一注意力公式如何因硬件调度而出现不同性能。

## 相关主题与版本

arXiv:2407.08608。[正式 DOI 10.52202/079017-2193](https://doi.org/10.52202/079017-2193)。可先读[初代 FlashAttention](2022-flashattention.md)，比较两代内核优化的数据移动环节。本导读依据原始书目与摘要整理，未复现实验。
