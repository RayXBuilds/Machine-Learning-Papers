# 内容编排说明 · 2026-11-21

[首页](../README.md) · [全库年份索引](years/README.md) · [学习路线](reading-paths.md)

本次整理基于 135 篇独立导读、14 个主题和 147 份历史 PDF。没有新增论文，没有移动文章主文件，也没有修改历史 PDF 或迁移清单。

## 查找与阅读

- 主题目录：按子方向分组，每组按归档年升序排列，同时展示阅读问题。
- 年份索引：覆盖全部导读，而不只展示历史补录批次；归档年口径以各条目为准。
- 学习路线：提供 12 条跨主题选读路线。它们是编辑建议，不是论文之间的技术继承声明。
- 经典索引：保留首批 26 篇和已有锚点，新路线使用独立页面维护。

## 编辑范围与证据

全库添加归档年、主题内分组、编辑日期和统一导航。26 篇早期导读将原有书目、方法提示、前置知识和阅读问题整理到统一栏目，并补标签与完整原题；原有版本提醒保留。没有追加实验数值、官方代码可用性或精读声明，未更新原 verified 日期。其“贡献与局限”保留待核查的阅读问题，不作为论文实证结论。

这些属于编辑结构变更，故当天日报的新增与实质内容修订数保持原值。原内容在 Git 历史中可追溯。

## 统一格式的 26 篇

- [Random Forests](../papers/classical-ml/2001-random-forests.md)
- [XGBoost: A Scalable Tree Boosting System](../papers/classical-ml/2016-xgboost.md)
- [ImageNet Classification with Deep Convolutional Neural Networks](../papers/computer-vision/2012-alexnet.md)
- [Deep Residual Learning for Image Recognition](../papers/computer-vision/2016-resnet.md)
- [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](../papers/computer-vision/2021-vit.md)
- [Dropout: A Simple Way to Prevent Neural Networks from Overfitting](../papers/deep-learning/2014-dropout.md)
- [Adam: A Method for Stochastic Optimization](../papers/deep-learning/2015-adam.md)
- [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](../papers/deep-learning/2015-batch-normalization.md)
- [A Simple Framework for Contrastive Learning of Visual Representations](../papers/deep-learning/2020-simclr.md)
- [Auto-Encoding Variational Bayes](../papers/generative-models/2013-vae.md)
- [Generative Adversarial Networks](../papers/generative-models/2014-gan.md)
- [Denoising Diffusion Probabilistic Models](../papers/generative-models/2020-ddpm.md)
- [High-Resolution Image Synthesis with Latent Diffusion Models](../papers/generative-models/2022-latent-diffusion.md)
- [Semi-Supervised Classification with Graph Convolutional Networks](../papers/graph-learning/2017-gcn.md)
- [Learning Transferable Visual Models From Natural Language Supervision](../papers/multimodal/2021-clip.md)
- [Efficient Estimation of Word Representations in Vector Space](../papers/nlp/2013-word2vec.md)
- [Sequence to Sequence Learning with Neural Networks](../papers/nlp/2014-seq2seq.md)
- [Attention Is All You Need](../papers/nlp/2017-transformer.md)
- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](../papers/nlp/2019-bert.md)
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](../papers/nlp/2020-rag.md)
- [LoRA: Low-Rank Adaptation of Large Language Models](../papers/nlp/2021-lora.md)
- [Training language models to follow instructions with human feedback](../papers/nlp/2022-instructgpt.md)
- [Neural Collaborative Filtering](../papers/recommender-systems/2017-ncf.md)
- [Human-level control through deep reinforcement learning](../papers/reinforcement-learning/2015-dqn.md)
- [Proximal Policy Optimization Algorithms](../papers/reinforcement-learning/2017-ppo.md)
- [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](../papers/reinforcement-learning/2018-sac.md)

## 后续维护

运行 `python3 scripts/build_catalog.py` 生成目录，运行 `python3 scripts/build_catalog.py --check` 检查是否遗漏生成步骤。文章元数据与两份目录配置是生成输入，生成结果提交到仓库，读者无需安装工具。

归档年不是统一的首次发表年。OpenVLA 等跨会议/出版年份条目已在正文说明；本轮未擅自更改这些年份口径。后续补充内容应优先核实与深化已有导读，再按缺口新增。
