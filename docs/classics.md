# 经典论文精选阅读索引

[返回首页](../README.md) · [历史索引](legacy-index.md)

首批精选 **26 篇**，书目核对日期：**2026-10-25**；2026-10-26 将导读拆为独立文件，本页保留阅读路线和原锚点。选题强调基础方法及后续代表作，不以当期热度排序；这是分批维护的精选集，不是完整的机器学习发展史。

每篇提供英文原题、作者、年份口径、原文入口、中文阅读重点、建议前置知识与一个阅读问题。阅读重点是编者导读，不是全文翻译、复现实验或个人已读记录；原文中的实验结论也不应直接推广到所有数据和任务。

## 年份与来源说明

- 有明确会议或期刊记录时列正式发表年份，跨年预印本另行注明。仅以 arXiv 为书目口径的条目明确标为预印本，并采用 v1 年份，不用后续修订时间冒充发表年份。
- 原文优先链接会议、期刊出版页或作者提交的 arXiv 页面；页面通常提供 PDF 入口。出版页的全文访问取决于其开放状态。
- 本轮核对了书目信息、摘要与主题相关性，没有宣称逐篇精读。后续如新增中文精读或实验，需单独标明作者、来源和验证范围。

## 按目标选择阅读顺序

| 目标 | 建议顺序 |
| --- | --- |
| 传统机器学习 | [Random Forests](#random-forests) → [XGBoost](#xgboost) |
| 深度网络训练与视觉 | [AlexNet](#alexnet) → [Dropout](#dropout) → [Adam](#adam) → [Batch Normalization](#batch-normalization) → [ResNet](#resnet) |
| NLP 与预训练 | [Word2Vec](#word2vec) → [Seq2Seq](#seq2seq) → [Transformer](#transformer) → [BERT](#bert) |
| 生成模型 | [VAE](#vae) → [GAN](#gan) → [DDPM](#ddpm) → [Latent Diffusion](#latent-diffusion) |
| 视觉表征与多模态 | [ResNet](#resnet) → [SimCLR](#simclr) → [CLIP](#clip)；读过 Transformer 后再读 [ViT](#vit) |
| 深度强化学习 | 补齐 MDP 与策略梯度基础，再读 [DQN](#dqn) → [PPO](#ppo) → [SAC](#sac) |
| 图与推荐 | 矩阵分解 → [NCF](#ncf)；图结构与半监督学习 → [GCN](#gcn) |
| 预训练模型扩展 | [Transformer](#transformer) / [BERT](#bert) → [RAG](#rag) / [LoRA](#lora)；读过 PPO 后再读 [InstructGPT](#instructgpt) |

这些顺序是阅读建议，不表示所有论文存在直接的技术继承关系。

## 主题导航

- [树模型与集成学习](#topic-1)
- [深度学习训练基础](#topic-2)
- [视觉模型](#topic-3)
- [词表示与序列建模](#topic-4)
- [生成模型](#topic-5)
- [自监督与多模态](#topic-6)
- [深度强化学习](#topic-7)
- [图学习与推荐系统](#topic-8)
- [预训练模型的知识与适配](#topic-9)

<a id="topic-1"></a>

## 1. 树模型与集成学习

<a id="random-forests"></a>

### [Random Forests](../papers/classical-ml/2001-random-forests.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="xgboost"></a>

### [XGBoost](../papers/classical-ml/2016-xgboost.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="topic-2"></a>

## 2. 深度学习训练基础

<a id="dropout"></a>

### [Dropout](../papers/deep-learning/2014-dropout.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="adam"></a>

### [Adam](../papers/deep-learning/2015-adam.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="batch-normalization"></a>

### [Batch Normalization](../papers/deep-learning/2015-batch-normalization.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="topic-3"></a>

## 3. 视觉模型

<a id="alexnet"></a>

### [AlexNet](../papers/computer-vision/2012-alexnet.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="resnet"></a>

### [ResNet](../papers/computer-vision/2016-resnet.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="vit"></a>

### [Vision Transformer](../papers/computer-vision/2021-vit.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="topic-4"></a>

## 4. 词表示与序列建模

<a id="word2vec"></a>

### [Word2Vec](../papers/nlp/2013-word2vec.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="seq2seq"></a>

### [Seq2Seq](../papers/nlp/2014-seq2seq.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="transformer"></a>

### [Transformer](../papers/nlp/2017-transformer.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="bert"></a>

### [BERT](../papers/nlp/2019-bert.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="topic-5"></a>

## 5. 生成模型

<a id="vae"></a>

### [VAE](../papers/generative-models/2013-vae.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="gan"></a>

### [GAN](../papers/generative-models/2014-gan.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="ddpm"></a>

### [DDPM](../papers/generative-models/2020-ddpm.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="latent-diffusion"></a>

### [Latent Diffusion](../papers/generative-models/2022-latent-diffusion.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="topic-6"></a>

## 6. 自监督与多模态

<a id="simclr"></a>

### [SimCLR](../papers/deep-learning/2020-simclr.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="clip"></a>

### [CLIP](../papers/multimodal/2021-clip.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="topic-7"></a>

## 7. 深度强化学习

<a id="dqn"></a>

### [DQN](../papers/reinforcement-learning/2015-dqn.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="ppo"></a>

### [PPO](../papers/reinforcement-learning/2017-ppo.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="sac"></a>

### [Soft Actor-Critic](../papers/reinforcement-learning/2018-sac.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="topic-8"></a>

## 8. 图学习与推荐系统

<a id="gcn"></a>

### [GCN](../papers/graph-learning/2017-gcn.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="ncf"></a>

### [Neural Collaborative Filtering](../papers/recommender-systems/2017-ncf.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="topic-9"></a>

## 9. 预训练模型的知识与适配

<a id="rag"></a>

### [RAG](../papers/nlp/2020-rag.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="lora"></a>

### [LoRA](../papers/nlp/2021-lora.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


<a id="instructgpt"></a>

### [InstructGPT](../papers/nlp/2022-instructgpt.md)

查看独立条目的原文、作者、年份、阅读重点与前置知识。


## 阅读时注意

- Batch Normalization 的标题沿用原论文的解释；理解该方法不应把标题中的解释当成机制的最终定论。
- Word2Vec 条目对应早期 CBOW / Skip-gram 论文；负采样等后续细节不能全部归到这一篇。
- DQN 条目对应 2015 年 Nature 论文，不与 2013 年的 Playing Atari with Deep Reinforcement Learning 混作同一版本。
- LoRA、RAG 和 InstructGPT 是本精选集中的后续代表作；“经典”是本库的编辑取舍，不代表统一的学术评级。
