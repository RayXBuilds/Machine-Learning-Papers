# Machine-Learning-Papers

[简体中文](README.md) | **English**

**Machine learning papers, Chinese reading guides, and an archival library, organized by topic.**

[Browse by topic](papers/README.md) · [Classic reading paths](docs/classics.md) · [Daily additions](docs/daily/README.md) · [Archived PDFs](library/README.md) · [Contribution guide](CONTRIBUTING.md)

This README provides an English overview. Reading guides, topic indexes, daily records, and contribution instructions are currently written primarily in Chinese; paper links lead to the original sources.

## Where to start

- **Explore a field:** use the topic table below. Each reading guide has its own file.
- **Study systematically:** follow the [classic reading paths](docs/classics.md), with suggested prerequisites and reading order.
- **Find recent additions:** browse the [daily records](docs/daily/README.md), which link to the corresponding topic entries.
- **Locate an older file:** consult the [path migration map](docs/migration.md) or the [original 2018 index](docs/legacy-index.md).

## Topics

| Topic | Scope | Reading guides | Archived PDFs |
| --- | --- | ---: | ---: |
| [Mathematics, Learning Theory & Probabilistic Models](papers/foundations/README.md) | Learning theory, optimization, probabilistic inference, graphical models | 1 | 9 |
| [Classical Machine Learning](papers/classical-ml/README.md) | Classification, regression, ensembles, clustering, feature selection, active/online/transfer learning | 4 | 34 |
| [Deep Learning & Representation Learning](papers/deep-learning/README.md) | Network training, optimization, self-supervised representations, neural network fundamentals | 4 | 3 |
| [Computer Vision](papers/computer-vision/README.md) | Image classification, detection, tracking, human motion, visual encoders | 4 | 7 |
| [Natural Language Processing & Large Language Models](papers/nlp/README.md) | Text, sequences, language models, retrieval augmentation, adaptation, alignment | 8 | 15 |
| [Generative Models](papers/generative-models/README.md) | VAEs, GANs, diffusion models | 4 | 0 |
| [Multimodal Learning](papers/multimodal/README.md) | Image–text alignment and cross-modal representations | 1 | 0 |
| [Reinforcement Learning & Decision-Making](papers/reinforcement-learning/README.md) | Policy and value learning, bandits, planning | 3 | 6 |
| [Graph Learning & Network Analysis](papers/graph-learning/README.md) | Graph neural networks, community detection, link mining | 1 | 9 |
| [Recommender Systems](papers/recommender-systems/README.md) | Collaborative filtering, matrix factorization, ALS, neural recommendation | 1 | 6 |
| [Machine Learning Systems](papers/ml-systems/README.md) | Distributed training, computing frameworks, parameter servers | 1 | 10 |
| [Data Mining & Data Management](papers/data-mining/README.md) | Time series, data streams, patterns and rules, web mining, entity matching | 0 | 25 |
| [Domain Applications](papers/applications/README.md) | Robotics, bioinformatics, finance, sustainability, business applications | 1 | 20 |
| [Evaluation & Experimental Methods](papers/evaluation/README.md) | Experimental design, A/B testing, validation, metrics | 8 | 3 |

As of October 31, 2026: **41 independent reading guides and 147 archived PDFs**. The PDFs include translations and technical documents, so the file count does not represent 147 distinct papers. Indexes and counts are maintained as new entries are added.

## Repository layout

```text
papers/<topic>/<year>-<slug>.md       One canonical reading guide per paper or article
library/<topic>/<subtopic>/*.pdf     Existing archival materials, organized by topic
docs/classics.md                     Classic reading paths, with original anchors preserved
docs/daily/YYYY/MM/YYYY-MM-DD.md      Links to daily additions and revisions
docs/migration.md                    Old-to-new file path mapping
```

Each article has one primary file. Tags and index links connect it to other topics without duplicating its content. Daily records contain brief summaries and links; full reading guides live in the topic directories. See the [contribution guide](CONTRIBUTING.md) for classification rules and the article template.

<a id="historical-library"></a>

## Directory reorganization · October 26, 2026

The original 36 root-level categories were consolidated into 14 topic entry points. ALS materials now belong to recommender systems; Ray and other computing frameworks belong to machine learning systems; probabilistic and graphical models are grouped under foundations; and policy iteration belongs to reinforcement learning. All 147 archived PDFs retain their original contents, and the 26 reading guides now have separate files.

PDF paths have changed. The [migration guide](docs/migration.md) provides a complete mapping and a link to the repository before the move. The historical index is retained as a source record; its bibliographic information has not been fully reverified.

<a id="maintenance"></a>

## Ongoing maintenance

Latest additions: [October 31, 2026 · Statistical evaluation and reinforcement learning frameworks](docs/daily/2026/10/2026-10-31.md) — two new guides: one preprint first submitted and one preprint revised within the past seven days.

A Codex automation runs daily at **11:00 Beijing time (Asia/Shanghai, UTC+8)** to search for, verify, and select up to five machine learning papers or technical articles. New guides are stored by topic and linked from the [daily records](docs/daily/README.md). No empty record is created when there are no suitable additions. Scheduling is handled by the Codex task; this repository does not currently contain a GitHub Actions scheduler.

Original-paper guides for SVMs, EM, and boosting have been added. Priorities include coverage of model evaluation, data leakage, probability calibration, and interpretability; and verification of historical references and translation sources. A reading guide is not a full translation, an experimental reproduction, or a claim that the paper has been read in depth.

## Attribution and rights

Papers and translations remain the property of their respective rights holders. New entries provide original-source links and short, original reading guides rather than additional copies of papers. Organizing this collection does not grant new rights to third-party materials. Suggestions and corrections are welcome through [Issues](https://github.com/RayXBuilds/Machine-Learning-Papers/issues); please include the original source.
