# Machine-Learning-Papers

**按主题整理的机器学习论文、中文导读与历史资料库。**

[主题目录](papers/README.md) · [经典阅读路线](docs/classics.md) · [每日收录](docs/daily/README.md) · [历史 PDF](library/README.md) · [收录规范](CONTRIBUTING.md)

## 从哪里开始

- 找某个方向的文章：进入下方主题目录，每篇导读有独立文件。
- 系统学习：使用[经典阅读路线](docs/classics.md)，按前置知识逐步阅读。
- 看最近新增：使用[每日收录记录](docs/daily/README.md)，记录链接到主题文章。
- 查找旧文件：使用[旧路径对照表](docs/migration.md)或[2018 年历史索引](docs/legacy-index.md)。

## 主题导航

| 主题 | 内容范围 | 导读 | 历史 PDF |
| --- | --- | ---: | ---: |
| [数学、学习理论与概率模型](papers/foundations/README.md) | 学习理论、优化、概率推断、图模型 | 0 | 9 |
| [传统机器学习](papers/classical-ml/README.md) | 分类、回归、集成、聚类、特征选择、主动/在线/迁移学习 | 2 | 34 |
| [深度学习与表征学习](papers/deep-learning/README.md) | 网络训练、优化、自监督表征、神经网络基础 | 4 | 3 |
| [计算机视觉](papers/computer-vision/README.md) | 图像分类、检测、跟踪、视觉编码器 | 3 | 7 |
| [自然语言处理与大语言模型](papers/nlp/README.md) | 文本、序列、语言模型、检索增强、适配与对齐 | 7 | 15 |
| [生成模型](papers/generative-models/README.md) | VAE、GAN、扩散模型 | 4 | 0 |
| [多模态学习](papers/multimodal/README.md) | 图文对齐与跨模态表示 | 1 | 0 |
| [强化学习与决策](papers/reinforcement-learning/README.md) | 策略/价值学习、Bandit、规划 | 3 | 6 |
| [图学习与网络分析](papers/graph-learning/README.md) | 图神经网络、社区发现、链接挖掘 | 1 | 9 |
| [推荐系统](papers/recommender-systems/README.md) | 协同过滤、矩阵分解、ALS、神经推荐 | 1 | 6 |
| [机器学习系统](papers/ml-systems/README.md) | 分布式训练、计算框架、参数服务器 | 0 | 10 |
| [数据挖掘与数据管理](papers/data-mining/README.md) | 时序、流数据、模式/规则、Web、实体匹配 | 0 | 25 |
| [领域应用](papers/applications/README.md) | 生物信息、金融、可持续发展、业务应用 | 0 | 20 |
| [评估与实验方法](papers/evaluation/README.md) | 实验设计、A/B 测试、验证与指标 | 0 | 3 |

数量为 2026-10-26 整理时快照：26 篇独立导读、147 份历史 PDF。PDF 包含译文与技术资料，不代表 147 篇独立论文。后续收录同步维护目录和数量。

## 存放方式

```text
papers/<主题>/<年份>-<英文短名>.md       每篇论文或文章的唯一导读
library/<主题>/<子主题>/*.pdf           迁移后的历史资料
docs/classics.md                      经典阅读路线（保留原锚点）
docs/daily/YYYY/MM/YYYY-MM-DD.md       每日新增/修订链接
docs/migration.md                     旧文件路径对照
```

每篇文章只存一个主文件；跨主题使用标签或索引链接。日期记录只保留新增摘要和文章入口，完整导读按主题存放。主题名称、归类边界及模板见[收录规范](CONTRIBUTING.md)。

<a id="historical-library"></a>

## 本次目录整理 · 2026-10-26

原来根目录的 36 个分类统一到 14 个主题入口。ALS 并入推荐系统，Ray 等框架资料并入机器学习系统，概率与图模型资料集中到基础理论，策略迭代归入强化学习。147 份历史 PDF 内容不变，26 篇导读拆为独立文件。

旧路径发生变更，完整对照及历史版本入口见[迁移说明](docs/migration.md)。历史索引作为原始资料保留；它不代表已核实的现代书目。

<a id="maintenance"></a>

## 持续维护

每天北京时间 11:00 由 Codex 自动任务检索、核实并精选最多 5 篇机器学习论文或技术文章。新增内容按主题存放，并登记到[每日收录](docs/daily/README.md)。没有合格新增时不生成空记录。此计划由 Codex 任务执行，仓库本身未配置 GitHub Actions 定时器。

后续优先补齐 SVM、Boosting、EM，扩展模型评估、数据泄漏、概率校准与可解释性专题，并逐项核对历史书目与译文来源。导读不等于全文翻译、实验复现或已读记录。

## 资料归属

论文与译文权利归各自权利人。新增内容使用原文链接与原创简短导读，不上传新的论文副本。本库整理不构成对第三方材料的重新授权。欢迎通过 [Issues](https://github.com/RayXBuilds/Machine-Learning-Papers/issues) 推荐文章或纠正信息，并附原始来源。
