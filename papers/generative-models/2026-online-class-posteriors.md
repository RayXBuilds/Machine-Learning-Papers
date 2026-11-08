---
id: online-class-posteriors
primary_topic: generative-models
tags: [discrete-diffusion, guidance, interpretability, nlp]
type: paper
added: 2026-11-08
verified: 2026-11-08
source: https://arxiv.org/abs/2611.03454
status: summary
---

# Online Class Posteriors for Interpretable and Controllable Discrete Diffusion

- 作者为 Felix Koulischer、Gianni Van De Velde、François Remy、Chris Develder、Thomas Demeester。
- 年份采用预印本 v1 的 2026 年，首次提交于 2026-11-02（UTC）。当前核对版本为 v1，来源注明 ICLR 2027 在审，正式接收信息待核实。[书目页](https://arxiv.org/abs/2611.03454)
- 原始正文提供后验估计、逻辑算子及实验附录。[arXiv HTML](https://arxiv.org/html/2611.03454v1)
- 官方代码由原文附录 H 确认，README 按合成数据、MNIST、文本和抗体序列列出复现入口。已核对 README，权重及实验运行待验证。[作者仓库](https://github.com/Gianni-Van-de-Velde/Online-Class-Posteriors-for-Interpretable-and-Controllable-Discrete-Diffusion)

## 解决的问题

离散扩散逐步生成 token 时，需要跟踪当前样本属于指定类别的概率，以解释生成轨迹，并按多个条件控制生成。[摘要](https://arxiv.org/abs/2611.03454)

## 主要方法

结合条件与无条件模型的转移预测，以对数似然比递推类别后验，再按后验加权组合转移率，实现 AND、OR、NOT 引导。论文分别讨论掩码与均匀噪声，并分析数据分布混合和含噪边缘分布混合对应的 CFG 公式。[方法](https://arxiv.org/html/2611.03454v1)

## 贡献与局限

贡献在于将 token 变化、类别后验和逻辑控制联系起来，实验覆盖解析合成数据、MNIST、文本和抗体序列。精确后验关系依赖转移核及采样假设，实践中的估计还使用校正超参数。后验在状态变化后更新，NOT 引导可能滞后于决定类别的 token。置信度解掩码、分块解码及重新掩码的交互仍待系统分析。[正文与局限附录](https://arxiv.org/html/2611.03454v1)

## 前置知识与阅读重点

先了解贝叶斯更新、连续时间马尔可夫链、离散去噪与 classifier-free guidance。阅读时重点核对路径后验等于当前状态后验的条件，以及理论转移核和实际估计器的差别。复现可从解析合成数据入口开始核查，再比较图像与文本设置。[代码说明](https://github.com/Gianni-Van-de-Velde/Online-Class-Posteriors-for-Interpretable-and-Controllable-Discrete-Diffusion/blob/main/README.md)

## 收录理由

扩展生成模型主题中的离散扩散与可控生成方向，连接可解释性维护队列。编者认为，采样假设和估计滞后是理解该方法适用范围的主要阅读问题。

## 相关主题与版本

主主题为[生成模型](README.md)，相关方向为[NLP 与大语言模型](../nlp/README.md)。唯一标识为 arXiv:2611.03454，页面列出的 DOI 为 `10.48550/arXiv.2611.03454`，当前标记待注册。已核对书目、相关方法、局限和官方代码 README，状态为导读，实验复现待开展。
