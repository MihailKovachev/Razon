---
title: Complex Series
tags:
    - complex-series
    - complex-analysis
    - mathematics
---

# Partial Sums

>[!DEFINITION] Definition: Partial Sum
>
>Let $\{a_n\}_{n \in \mathcal{D}}$ be a [complex sequence](../Complex%20Sequences/index.md). 
>
>The $k$-th **partial sum** of $\{a_n\}$ is the sum of its first $k$ numbers:
>
>$$
>\sum_{\begin{align*}j &\in \mathcal{D} \\ j &\le k \end{align*}} a_j
>$$
>
>>[!NOTATION]-
>>
>>$$
>>s_k
>>$$
>>
>

# Complex Series

Given a [complex sequence](../Complex%20Sequences/index.md) $(a_n)_{n \in \mathcal{D}}$, it is apparent that the [complex-valued function](../Complex-Valued%20Function.md) which maps each $k \in \mathcal{D}$ to the $k$-th [partial sum](./index.md#partial%20sums) of $(a_n)_{n \in \mathcal{D}}$ is itself a [complex sequence](../Complex%20Sequences/index.md) $(s_n)_{n \in \mathcal{D}}$.

>[!DEFINITION] Definition: Complex Series
>
>A **complex series** is the [sequence](../Complex%20Sequences/index.md) of [partial sums](./index.md#partial%20sums) of a [complex sequence](../Complex%20Sequences/index.md).
>
>>[!NOTATION]-
>>
>>If the sequence is $(a_n)_{n \in \mathcal{D}}$, then we denote the sequence of its partial sums by $\displaystyle \sum_{n \in \mathcal{D}} a_n$. 
>>
>>When $\mathcal{D} = \mathbb{N}_0$ or $\mathcal{D} = \mathbb{N}$, we write $\displaystyle \sum_{n = 0}^{\infty} a_n$ or $\displaystyle \sum_{n = 1}^{\infty} a_n$, respectively.
>>
>>In the case, when $\mathcal{D} = \mathbb{N} \setminus \{0, 1, \dotsc, p - 1\}$ for some integer $p$, we write $\displaystyle \sum_{n = p}^{\infty} a_n$.
>>
>
