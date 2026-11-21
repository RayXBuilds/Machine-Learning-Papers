---
id: flashattention
primary_topic: ml-systems
tags: [attention, gpu-memory, io-complexity]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://arxiv.org/abs/2205.14135
status: summary
catalog_year: 2022
subtopic: "推理与硬件效率"
updated: 2026-11-21
---

# FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Tri Dao、Dan Fu、Stefano Ermon、Atri Rudra、Christopher Ré。
- 年份与版本：按 NeurIPS 2022 正式发表年份归档。arXiv 初稿提交于 2022 年 5 月。
- 原始来源：[NeurIPS 会议版](https://proceedings.neurips.cc/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract.html) · [作者预印本](https://arxiv.org/abs/2205.14135)。
- 官方代码：[作者项目](https://github.com/Dao-AILab/flash-attention)（同仓库也包含后续版本）。

## 解决的问题

精确注意力为何常被显存读写拖慢，即使 GPU 还有足够算力？

## 主要方法

分块将查询、键和值载入片上存储，用在线 softmax 累积归一化量与输出；反向时重算部分结果，避免写回完整注意力矩阵。

## 贡献与局限

作者从访存复杂度解释实测加速。稠密注意力的算术量仍随序列长度二次增长，实际速度受形状、硬件与内核实现影响。

## 前置知识与阅读重点

先复习数值稳定的 softmax 与 GPU 存储层次。手算两块分数合并时旧输出的缩放因子，再看显存访问次数。

## 收录理由

把注意力公式与硬件数据移动联系起来，可接续 TVM 阅读。

## 相关主题与版本

arXiv:2205.14135。延伸阅读见 [TRANSFORMER](../nlp/2017-transformer.md)。

本条依据作者摘要、书目及项目说明整理，未复现实验。
