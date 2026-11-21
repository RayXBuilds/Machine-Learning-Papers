---
id: pagedattention
primary_topic: ml-systems
tags: [inference, memory-management]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://doi.org/10.1145/3600006.3613165
status: summary
---

# Efficient Memory Management for Large Language Model Serving with PagedAttention

- 作者：Woosuk Kwon、Zhuohan Li、Siyuan Zhuang、Ying Sheng、Lianmin Zheng、Cody Hao Yu、Joseph E. Gonzalez、Hao Zhang、Ion Stoica。
- 年份与版本：SOSP 2023。arXiv 首版提交于 2023-09-12。
- 原始来源：[SOSP 2023 书目](https://doi.org/10.1145/3600006.3613165) · [arXiv 版本记录](https://arxiv.org/abs/2309.06180)。
- 官方代码：已核对[作者项目仓库](https://github.com/vllm-project/vllm)。

## 解决的问题

并发请求的输出长度未知，提前留出连续 KV 缓存会损失多少可用显存？

## 主要方法

把每条序列的缓存划成逻辑块，用块表映射到物理显存块。按需分配，分支解码可共享已有块。

## 贡献与局限

作者在给定延迟水平下观察到吞吐提升。结果随请求长度分布、模型规模与解码方式而变，吞吐提升不能直接换算为单请求延迟下降。

## 前置知识与阅读重点

先了解自回归解码的键值缓存，用两条共享前缀的序列追踪块表何时分叉。

## 收录理由

把推理服务的批量大小和缓存碎片联系起来。

## 相关主题与版本

arXiv:2309.06180。[正式 DOI 10.1145/3600006.3613165](https://doi.org/10.1145/3600006.3613165)。本导读依据原始书目与摘要整理，未复现实验。
