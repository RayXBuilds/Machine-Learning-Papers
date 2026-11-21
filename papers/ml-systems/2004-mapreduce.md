---
id: mapreduce
primary_topic: ml-systems
tags: [distributed-computing, data-processing]
type: paper
added: 2026-11-21
verified: 2026-11-21
source: https://www.usenix.org/conference/osdi-04/mapreduce-simplified-data-processing-large-clusters
status: summary
catalog_year: 2004
subtopic: "数据处理与编译"
updated: 2026-11-21
---

# MapReduce: Simplified Data Processing on Large Clusters

[主题目录](README.md) · [年份导航](../../docs/years/README.md) · [学习路线](../../docs/reading-paths.md)

- 作者：Jeffrey Dean、Sanjay Ghemawat
- 年份与版本：2004 年，OSDI 2004。
- 原始来源：[原文](https://www.usenix.org/conference/osdi-04/mapreduce-simplified-data-processing-large-clusters)
- 官方代码：核对的原始资料中未确认论文配套实现。

## 解决的问题

怎样让使用者编写集群批处理程序，同时把数据分区、调度和故障恢复交给运行时？

## 主要方法

Map 产生中间键值对，运行时按键分组并传送到 Reduce。调度器利用数据位置并重做失败的任务。

## 贡献与局限

两个用户函数就能表达多种聚合任务。中间数据的跨机传输有成本，多轮依赖会引入额外作业边界。

## 前置知识与阅读重点

熟悉键值对后，沿一个词频统计作业追踪同一单词的中间记录，找出发生网络传输的步骤。

## 收录理由

帮助理解训练之前的大规模特征统计和样本处理为何受数据移动制约。

## 相关主题与版本

OSDI 2004 Dean/Ghemawat。延伸阅读见[机器学习系统目录](README.md)。

核对范围为书目信息与方法概要，未做实验复现。
