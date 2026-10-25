# Machine-Learning-Papers

**机器学习经典论文、综述与阅读路线。**

Machine learning classics, surveys, and curated reading paths.

这里独立维护机器学习文献：保留早期积累的基础资料，逐步补充深度学习、生成模型、强化学习与预训练模型的代表性论文，帮助读者按主题理解方法的发展。

[精选论文与阅读路线](docs/classics.md) · [历史资料目录](#historical-library) · [原始历史索引](docs/legacy-index.md) · [收录与维护约定](#maintenance)

## 本轮更新 · 2026-10-25

新增 **26 篇论文的原文链接与中文导读**，涵盖 **9 个主题**。每篇标注作者、年份与版本、阅读重点、前置知识和阅读问题。新增条目采用原文链接；现有 **36 个目录、147 份 PDF** 保留原路径。

| 主题 | 本轮新增 |
| --- | --- |
| [树模型与集成学习](docs/classics.md#topic-1) | Random Forests、XGBoost |
| [深度学习训练基础](docs/classics.md#topic-2) | Dropout、Adam、Batch Normalization |
| [视觉模型](docs/classics.md#topic-3) | AlexNet、ResNet、Vision Transformer |
| [词表示与序列建模](docs/classics.md#topic-4) | Word2Vec、Seq2Seq、Transformer、BERT |
| [生成模型](docs/classics.md#topic-5) | VAE、GAN、DDPM、Latent Diffusion |
| [自监督与多模态](docs/classics.md#topic-6) | SimCLR、CLIP |
| [深度强化学习](docs/classics.md#topic-7) | DQN、PPO、Soft Actor-Critic |
| [图学习与推荐系统](docs/classics.md#topic-8) | GCN、Neural Collaborative Filtering |
| [预训练模型的知识与适配](docs/classics.md#topic-9) | RAG、LoRA、InstructGPT |

初次阅读可以从 **Random Forests → XGBoost** 或 **AlexNet → ResNet** 开始；有神经网络基础后，选择 **Word2Vec → Seq2Seq → Transformer → BERT**。完整路线与前置知识见 [精选阅读索引](docs/classics.md)。

这是一份持续整理的精选资料库，不是覆盖所有方向的课程。中文导读不等于全文翻译或实验复现；预印本首发年与正式发表年份按条目分别标注。

<a id="historical-library"></a>

## 历史资料目录

以下数量按本轮维护前的实际 PDF 文件统计，包含论文、译文及技术文档，不代表独立论文数量。旧目录名和文件路径保持可访问；2018 年 README 原文保存在 [历史索引](docs/legacy-index.md)，其书目信息仍待逐项校订。

| 目录 | PDF 文件数 |
| --- | ---: |
| [active learning](active%20learning/) | 2 |
| [ALS](ALS/) | 3 |
| [Applications](Applications/) | 6 |
| [Biology](Biology/) | 12 |
| [Classification](Classification/) | 1 |
| [Clustering](Clustering/) | 18 |
| [Computer Vision](Computer%20Vision/) | 7 |
| [Databases](Databases/) | 4 |
| [deep learning](deep%20learning/) | 1 |
| [Dimension Reduction](Dimension%20Reduction/) | 6 |
| [Economics](Economics/) | 3 |
| [Game Theory](Game%20Theory/) | 1 |
| [Graphical Models](Graphical%20Models/) | 1 |
| [kernel methods](kernel%20methods/) | 1 |
| [Learning Theory](Learning%20Theory/) | 1 |
| [Machine Learning](Machine%20Learning/) | 11 |
| [Mathematics](Mathematics/) | 1 |
| [Multi-armed Bandit](Multi-armed%20Bandit/) | 1 |
| [Natural Computing](Natural%20Computing/) | 5 |
| [Natural Language Processing](Natural%20Language%20Processing/) | 16 |
| [Networks](Networks/) | 9 |
| [On-Line Learning](On-Line%20Learning/) | 1 |
| [Others](Others/) | 1 |
| [Planning and Scheduling](Planning%20and%20Scheduling/) | 1 |
| [Probabilistic](Probabilistic/) | 2 |
| [Probabilistic Models](Probabilistic%20Models/) | 1 |
| [Randomized Algorithms](Randomized%20Algorithms/) | 1 |
| [Ray](Ray/) | 10 |
| [Recommender Systems](Recommender%20Systems/) | 3 |
| [Regression](Regression/) | 1 |
| [Reinforcement Learning](Reinforcement%20Learning/) | 2 |
| [Rule Learning](Rule%20Learning/) | 2 |
| [Testing](Testing/) | 1 |
| [Time Series](Time%20Series/) | 3 |
| [Transfer Learning](Transfer%20Learning/) | 1 |
| [Web Mining](Web%20Mining/) | 7 |

<a id="maintenance"></a>

## 收录与维护约定

1. **选题**：优先补齐方法发展中的关键论文、可靠综述和具有教学价值的代表作；新近热门论文需说明收录理由，不自动冠以“经典”。
2. **来源**：提供英文原题、作者、正式发表信息或预印本标记，并链接会议、期刊、作者页面或 arXiv。新增译文必须注明原文、译者和版本。
3. **导读**：至少写明论文解决的问题、建议前置知识及阅读重点。未精读或未复现的条目不标为已完成。
4. **校验**：新增前检查已有目录与索引，避免重复；核对标题、年份、主题分类和链接。链接检查时间与论文发表时间分开记录。
5. **反馈**：欢迎通过 [Issues](https://github.com/RayXBuilds/Machine-Learning-Papers/issues) 推荐论文或纠正书目信息，请附原文来源及推荐理由。

### 后续维护队列

- 补齐传统机器学习的 SVM、Boosting、EM 等基础方法原始论文。
- 扩展模型评估、数据泄漏、概率校准与可解释性专题。
- 逐项校订历史索引中的数字残留、缺失条目、分类及年份。
- 为重点论文增加有署名的中文精读，并明确区分摘要导读、全文翻译与复现实验。

以上是维护方向，不表示已建立自动更新或固定发布日程。

## 资料归属

论文与译文的权利归各自权利人。本轮新增的是书目链接与简短中文导读，不上传新的论文副本；本库的整理不构成对第三方论文、译文或代码的重新授权。历史材料的来源信息将逐步补充。
