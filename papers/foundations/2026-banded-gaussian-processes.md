---
id: banded-gaussian-processes
primary_topic: foundations
tags: [gaussian-processes, bayesian-inference, sparse-approximation, posterior-contraction]
type: paper
added: 2026-11-16
verified: 2026-11-16
source: https://arxiv.org/abs/2611.16482
status: summary
catalog_year: 2026
subtopic: "概率推断与图模型"
updated: 2026-11-21
---

# Posterior contraction rates for banded approximations of Gaussian processes

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Omar Kassi、Bernhard Stankewitz、Botond Szabó。
- 年份与版本：2026 按 arXiv v1 年份，首次提交于 2026-11-12（UTC），核对时为 v1。正文注明已被 NeurIPS 2026 接收，正式会议出版页尚未独立核实。
- 原始来源：[arXiv 书目](https://arxiv.org/abs/2611.16482) · [v1 正文](https://arxiv.org/html/2611.16482v1)。
- 官方代码：未在上述原始来源中找到本论文的官方代码链接。

- 仓库内 PDF：[打开全文](../../pdfs/foundations/2026-banded-gaussian-processes.pdf)（arXiv 2611.16482v1）。

## 解决的问题

高斯过程回归的稠密矩阵计算限制了数据规模。论文研究按空间距离截断协方差后，需要保留多少邻域依赖，才能维持统计估计质量。[摘要](https://arxiv.org/abs/2611.16482)

## 主要方法

分析带状稀疏协方差近似的后验收缩率，给出邻域规模的充分和必要条件，并考察平方指数核与 Matérn 核。[正文](https://arxiv.org/html/2611.16482v1)

## 贡献与局限

作者连接近似规模与统计收敛保证。讨论指出，函数恢复达到最优速率与完整后验的 KL 近似准确性可以要求不同的截断规模。方法依赖核相关性随空间距离衰减，最优半径还依赖未知的函数正则性，自适应选择仍待研究。[第 5 节](https://arxiv.org/html/2611.16482v1)

## 前置知识与阅读重点

建议了解高斯过程回归、核矩阵、后验收缩与 KL 散度。重点核对随机设计和高斯噪声假设，以及核平滑性、真实函数正则性和邻域规模的关系。

## 收录理由

补充概率模型的可扩展推断方向，为理解计算近似何时保留统计保证提供案例。

## 相关主题与版本

- arXiv ID：`2611.16482`。书目页列 DOI `10.48550/arXiv.2611.16482`，注明待注册。
- 主文件归入[数学、学习理论与概率模型](README.md)，相关方向为[传统机器学习](../classical-ml/README.md)。
- 本条核对书目、问题设定与讨论，未独立验证完整证明或复现实验。
