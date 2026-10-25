# 经典论文精选阅读索引

[返回首页](../README.md) · [历史索引](legacy-index.md)

本批新增 **26 篇**，核对日期：**2026-10-25**。选题强调基础方法及后续代表作，不以当期热度排序；这是分批维护的精选集，不是完整的机器学习发展史。

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

### Random Forests

**[Random Forests](https://link.springer.com/article/10.1023/A:1010933404324)**

- 作者：Leo Breiman。
- 年份与版本：2001 · Machine Learning。
- 阅读重点：理解随机采样、随机特征选择与树集成，以及袋外评估的作用。
- 建议前置：决策树、偏差与方差。
- 带着问题读：单棵树的强度和树之间的相关性如何影响集成误差？

<a id="xgboost"></a>

### XGBoost

**[XGBoost: A Scalable Tree Boosting System](https://arxiv.org/abs/1603.02754)**

- 作者：Tianqi Chen、Carlos Guestrin。
- 年份与版本：2016 · KDD。
- 阅读重点：把梯度提升树的目标函数与稀疏数据处理、近似分裂和系统优化联系起来。
- 建议前置：决策树、梯度提升、泰勒展开。
- 带着问题读：哪些收益来自学习目标，哪些来自工程实现？

<a id="topic-2"></a>

## 2. 深度学习训练基础

<a id="dropout"></a>

### Dropout

**[Dropout: A Simple Way to Prevent Neural Networks from Overfitting](https://jmlr.org/papers/v15/srivastava14a.html)**

- 作者：Nitish Srivastava 等。
- 年份与版本：2014 · JMLR。
- 阅读重点：理解训练时随机丢弃单元的正则化方法，以及训练和推理的差别。
- 建议前置：神经网络、过拟合。
- 带着问题读：训练时的随机网络与推理时的网络如何对应？

<a id="adam"></a>

### Adam

**[Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980)**

- 作者：Diederik P. Kingma、Jimmy Ba。
- 年份与版本：2015 · ICLR；预印本首发 2014。
- 阅读重点：学习梯度一阶、二阶矩估计和偏差修正，理解自适应步长的构造。
- 建议前置：SGD、动量、指数移动平均。
- 带着问题读：为什么初始化为零的矩估计需要偏差修正？

<a id="batch-normalization"></a>

### Batch Normalization

**[Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://proceedings.mlr.press/v37/ioffe15.html)**

- 作者：Sergey Ioffe、Christian Szegedy。
- 年份与版本：2015 · ICML。
- 阅读重点：学习批归一化的计算、可学习缩放和平移，以及训练与推理统计量的差别。
- 建议前置：反向传播、均值与方差。
- 带着问题读：小批量统计量和推理时统计量为什么不能混用？

<a id="topic-3"></a>

## 3. 视觉模型

<a id="alexnet"></a>

### AlexNet

**[ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html)**

- 作者：Alex Krizhevsky、Ilya Sutskever、Geoffrey E. Hinton。
- 年份与版本：2012 · NeurIPS（当时名为 NIPS）。
- 阅读重点：理解卷积网络、GPU 训练、数据增强和正则化如何共同构成图像分类系统。
- 建议前置：卷积、池化、监督分类。
- 带着问题读：模型结构之外，哪些训练选择对结果至关重要？

<a id="resnet"></a>

### ResNet

**[Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)**

- 作者：Kaiming He、Xiangyu Zhang、Shaoqing Ren、Jian Sun。
- 年份与版本：2016 · CVPR；预印本首发 2015。
- 阅读重点：学习残差连接如何改变深层网络的优化问题，区分退化问题与过拟合。
- 建议前置：CNN、反向传播。
- 带着问题读：为什么拟合残差与直接拟合目标映射的优化行为不同？

<a id="vit"></a>

### Vision Transformer

**[An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929)**

- 作者：Alexey Dosovitskiy 等。
- 年份与版本：2021 · ICLR；预印本首发 2020。
- 阅读重点：理解将图像切成 patch 后使用 Transformer 的方法，以及预训练数据规模的影响。
- 建议前置：Transformer、图像分类。
- 带着问题读：减少卷积归纳偏置后，模型需要怎样的数据与训练条件？

<a id="topic-4"></a>

## 4. 词表示与序列建模

<a id="word2vec"></a>

### Word2Vec

**[Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781)**

- 作者：Tomas Mikolov、Kai Chen、Greg Corrado、Jeffrey Dean。
- 年份与版本：2013 · arXiv 预印本。
- 阅读重点：学习 CBOW 与 Skip-gram 的基本目标，理解分布式词表示和预测任务的联系。
- 建议前置：语言模型、向量表示。
- 带着问题读：预测中心词与预测上下文分别学习什么信息？

<a id="seq2seq"></a>

### Seq2Seq

**[Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215)**

- 作者：Ilya Sutskever、Oriol Vinyals、Quoc V. Le。
- 年份与版本：2014 · NeurIPS（当时名为 NIPS）。
- 阅读重点：理解 LSTM 编码器与解码器如何处理变长输入、输出序列。
- 建议前置：RNN、LSTM、条件概率。
- 带着问题读：固定长度编码给长序列带来了什么限制？

<a id="transformer"></a>

### Transformer

**[Attention Is All You Need](https://papers.nips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)**

- 作者：Ashish Vaswani 等。
- 年份与版本：2017 · NeurIPS（当时名为 NIPS）。
- 阅读重点：学习缩放点积注意力、多头注意力和位置编码，理解没有递归的序列建模。
- 建议前置：矩阵运算、Seq2Seq、注意力基础。
- 带着问题读：并行训练与自回归生成的计算方式有什么不同？

<a id="bert"></a>

### BERT

**[BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://aclanthology.org/N19-1423/)**

- 作者：Jacob Devlin、Ming-Wei Chang、Kenton Lee、Kristina Toutanova。
- 年份与版本：2019 · NAACL；预印本首发 2018。
- 阅读重点：理解掩码语言建模、双向表示与预训练后微调的范式。
- 建议前置：Transformer 编码器。
- 带着问题读：双向掩码预训练与从左到右的生成目标有什么差别？

<a id="topic-5"></a>

## 5. 生成模型

<a id="vae"></a>

### VAE

**[Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114)**

- 作者：Diederik P. Kingma、Max Welling。
- 年份与版本：2013 · arXiv 预印本（此处按所链接版本首发年）。
- 阅读重点：学习变分下界与重参数化技巧，理解如何训练带连续隐变量的生成模型。
- 建议前置：概率分布、KL 散度、变分推断。
- 带着问题读：重参数化如何让梯度通过随机采样过程？

<a id="gan"></a>

### GAN

**[Generative Adversarial Networks](https://arxiv.org/abs/1406.2661)**

- 作者：Ian J. Goodfellow 等。
- 年份与版本：2014 · arXiv 预印本；会议版题为 Generative Adversarial Nets。
- 阅读重点：学习生成器与判别器的对抗目标，以及生成分布如何通过博弈被学习。
- 建议前置：概率分布、神经网络、优化。
- 带着问题读：理论上的均衡与实际训练稳定性之间有什么差距？

<a id="ddpm"></a>

### DDPM

**[Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)**

- 作者：Jonathan Ho、Ajay Jain、Pieter Abbeel。
- 年份与版本：2020 · NeurIPS。
- 阅读重点：理解逐步加噪、反向去噪以及噪声预测目标，建立扩散模型的基本认识。
- 建议前置：高斯分布、变分下界、神经网络。
- 带着问题读：训练时预测噪声与采样时逐步去噪如何对应？

<a id="latent-diffusion"></a>

### Latent Diffusion

**[High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752)**

- 作者：Robin Rombach 等。
- 年份与版本：2022 · CVPR；预印本首发 2021。
- 阅读重点：理解在压缩潜空间中进行扩散，以及用交叉注意力引入条件信息。
- 建议前置：自动编码器、DDPM、注意力。
- 带着问题读：潜空间压缩如何在计算成本与细节保真之间取舍？

<a id="topic-6"></a>

## 6. 自监督与多模态

<a id="simclr"></a>

### SimCLR

**[A Simple Framework for Contrastive Learning of Visual Representations](https://proceedings.mlr.press/v119/chen20j.html)**

- 作者：Ting Chen、Simon Kornblith、Mohammad Norouzi、Geoffrey Hinton。
- 年份与版本：2020 · ICML。
- 阅读重点：学习数据增强、投影头和对比目标的配合，理解无标签视觉表征学习。
- 建议前置：CNN、相似度、交叉熵。
- 带着问题读：哪些增强保持语义，哪些增强可能改变任务标签？

<a id="clip"></a>

### CLIP

**[Learning Transferable Visual Models From Natural Language Supervision](https://proceedings.mlr.press/v139/radford21a.html)**

- 作者：Alec Radford 等。
- 年份与版本：2021 · ICML。
- 阅读重点：理解图像与文本的对比预训练，以及通过文本描述构造零样本分类器。
- 建议前置：对比学习、图像与文本编码器。
- 带着问题读：为什么提示文本的写法会改变零样本分类结果？

<a id="topic-7"></a>

## 7. 深度强化学习

<a id="dqn"></a>

### DQN

**[Human-level control through deep reinforcement learning](https://doi.org/10.1038/nature14236)**

- 作者：Volodymyr Mnih 等。
- 年份与版本：2015 · Nature。
- 阅读重点：理解深度 Q 网络、经验回放与目标网络怎样结合来学习控制策略。
- 建议前置：MDP、Bellman 方程、Q-learning。
- 带着问题读：经验回放与目标网络分别缓解什么训练问题？

<a id="ppo"></a>

### PPO

**[Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)**

- 作者：John Schulman 等。
- 年份与版本：2017 · arXiv 预印本。
- 阅读重点：学习裁剪代理目标和多轮小批量更新，理解策略更新幅度的控制。
- 建议前置：策略梯度、优势函数、重要性采样。
- 带着问题读：裁剪目标如何影响过大的策略更新，为什么不等于硬约束？

<a id="sac"></a>

### Soft Actor-Critic

**[Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html)**

- 作者：Tuomas Haarnoja、Aurick Zhou、Pieter Abbeel、Sergey Levine。
- 年份与版本：2018 · ICML。
- 阅读重点：理解最大熵目标、随机策略与离策略训练在连续控制中的结合。
- 建议前置：Actor-Critic、熵、离策略学习。
- 带着问题读：奖励最大化与策略熵之间如何权衡？

<a id="topic-8"></a>

## 8. 图学习与推荐系统

<a id="gcn"></a>

### GCN

**[Semi-Supervised Classification with Graph Convolutional Networks](https://arxiv.org/abs/1609.02907)**

- 作者：Thomas N. Kipf、Max Welling。
- 年份与版本：2017 · ICLR；预印本首发 2016。
- 阅读重点：理解归一化邻接矩阵与邻域信息聚合，建立图神经网络的入门模型。
- 建议前置：图结构、矩阵运算、半监督学习。
- 带着问题读：节点特征和图连接分别提供什么信息？

<a id="ncf"></a>

### Neural Collaborative Filtering

**[Neural Collaborative Filtering](https://arxiv.org/abs/1708.05031)**

- 作者：Xiangnan He 等。
- 年份与版本：2017 · WWW。
- 阅读重点：学习用神经网络建模用户和物品交互，并与矩阵分解的内积形式比较。
- 建议前置：协同过滤、矩阵分解、隐式反馈。
- 带着问题读：负采样、数据划分和基线调参如何影响比较结论？

<a id="topic-9"></a>

## 9. 预训练模型的知识与适配

<a id="rag"></a>

### RAG

**[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)**

- 作者：Patrick Lewis 等。
- 年份与版本：2020 · NeurIPS。
- 阅读重点：理解参数化生成模型与非参数化检索记忆的组合，关注检索和生成如何连接。
- 建议前置：稠密检索、Seq2Seq、Transformer。
- 带着问题读：知识缺失、检索失败和生成错误如何分别识别？

<a id="lora"></a>

### LoRA

**[LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)**

- 作者：Edward J. Hu 等。
- 年份与版本：2021 · arXiv 预印本（此处按所链接版本首发年）。
- 阅读重点：理解冻结原模型、训练低秩增量的适配方式，以及秩对参数量的影响。
- 建议前置：线性代数、Transformer、模型微调。
- 带着问题读：低秩约束减少了哪些训练参数，又限制了哪些更新方向？

<a id="instructgpt"></a>

### InstructGPT

**[Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)**

- 作者：Long Ouyang 等。
- 年份与版本：2022 · arXiv 预印本。
- 阅读重点：理解监督微调、偏好数据、奖励模型与强化学习构成的指令对齐流程。
- 建议前置：语言模型、偏好学习、PPO。
- 带着问题读：人类偏好评分能衡量什么，又不能保证什么？

## 阅读时注意

- Batch Normalization 的标题沿用原论文的解释；理解该方法不应把标题中的解释当成机制的最终定论。
- Word2Vec 条目对应早期 CBOW / Skip-gram 论文；负采样等后续细节不能全部归到这一篇。
- DQN 条目对应 2015 年 Nature 论文，不与 2013 年的 Playing Atari with Deep Reinforcement Learning 混作同一版本。
- LoRA、RAG 和 InstructGPT 是本精选集中的后续代表作；“经典”是本库的编辑取舍，不代表统一的学术评级。
