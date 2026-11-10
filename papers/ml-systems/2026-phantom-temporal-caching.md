---
id: phantom-temporal-caching
primary_topic: ml-systems
tags: [diffusion, inference, temporal-caching, hardware-acceleration]
type: paper
added: 2026-11-10
verified: 2026-11-10
source: https://arxiv.org/abs/2611.06019
status: summary
---

# Phantom: Temporal Caching for Diffusion Models

- 作者为 Yuzhe Fu、Cong Guo、Zishan Shao、Bowen Duan、Chiyue Wei、Haoxuan Shan、Ting Jiang、Hancheng Ye、Jonathan Ku、Changchun Zhou、Hai “Helen” Li、Yiran Chen。
- 年份采用预印本 v1 的 2026 年，首次提交于 2026-11-04（UTC）。当前核对版本为 v1，书目页未列出正式会议或期刊。[书目页](https://arxiv.org/abs/2611.06019)
- 本次核对的原始页面未找到 Phantom 官方实现链接，代码可用性待核实。[原始正文](https://arxiv.org/html/2611.06019v1)

## 解决的问题

扩散模型跨时间步反复执行网络，产生大量相似计算。论文研究如何将相邻步的激活相似性转化为硬件执行收益。[摘要](https://arxiv.org/abs/2611.06019)

## 主要方法

Phantom 交替进行完整计算与差分更新，重算变化显著的 token，其余复用时间缓存。检测与缓存单元配合压缩流水线，把稀疏更新映射到脉动阵列计算。[方法](https://arxiv.org/html/2611.06019v1)

## 贡献与局限

论文将缓存策略与加速器共同设计，评估覆盖 SD1.4、DiT 和 SD3.5。硬件结果采用 RTL 综合与周期精确仿真，能耗含建模及工艺缩放。质量和速度取决于更新间隔、保留比例与工作负载，部署收益需按硬件重新验证。[评估](https://arxiv.org/html/2611.06019v1)

## 前置知识与阅读重点

先了解扩散采样、激活缓存和脉动阵列。重点核对完整刷新频率、缓存容量及质量约束，再阅读性能比较中的硬件预算与测量方式。[正文](https://arxiv.org/html/2611.06019v1)

## 收录理由

补充机器学习系统主题中的推理加速方向。编者建议围绕缓存带来的计算节省、存储流量和近似误差进行联合阅读。

## 相关主题与版本

主主题为[机器学习系统](README.md)，相关主题为[生成模型](../generative-models/README.md)。唯一标识为 arXiv:2611.06019，书目页列出 DOI `10.48550/arXiv.2611.06019`，当前标记待注册。已核对书目、方法与评估，状态为导读，实验复现待开展。
