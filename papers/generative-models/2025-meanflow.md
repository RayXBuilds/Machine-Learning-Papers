---
id: meanflow
primary_topic: generative-models
tags: [flow-matching, sampling]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://proceedings.neurips.cc/paper_files/paper/2025/hash/6d13e085b79d454da5910e4ca82a3d9d-Abstract-Conference.html
status: summary
catalog_year: 2025
subtopic: "扩散、流与世界模型"
updated: 2026-11-21
---

# Mean Flows for One-step Generative Modeling

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Zhengyang Geng、Mingyang Deng、Xingjian Bai、J. Zico Kolter、Kaiming He。
- 年份与版本：NeurIPS 2025。arXiv 首版提交于 2025-05-19。
- 原始来源：[NeurIPS 2025 书目](https://proceedings.neurips.cc/paper_files/paper/2025/hash/6d13e085b79d454da5910e4ca82a3d9d-Abstract-Conference.html) · [arXiv 版本记录](https://arxiv.org/abs/2505.13447)。
- 官方代码：已核对[作者项目仓库](https://github.com/Gsunshine/meanflow)。

## 解决的问题

若希望从噪声一步跳到样本，训练时应学局部速度还是一段时间内的平均位移？

## 主要方法

定义区间平均速度，推导它与瞬时速度的恒等关系，并用该关系构造可直接训练的回归目标。

## 贡献与局限

作者展示从头训练且单次函数求值的图像生成结果。一次采样调用衡量推理成本，训练所需导数计算需单独计量。

## 前置知识与阅读重点

需要流匹配与方向导数。先检查时间区间趋零时的关系，再对照跨整个区间的一步采样。

## 收录理由

与一致性模型对读，可比较两种一步生成方法各自约束的量。

## 相关主题与版本

arXiv:2505.13447。[正式 DOI 10.52202/085713-2534](https://doi.org/10.52202/085713-2534)。可对读 [Consistency Models](../generative-models/2023-consistency-models.md)。本导读依据原始书目与摘要整理，未复现实验。
