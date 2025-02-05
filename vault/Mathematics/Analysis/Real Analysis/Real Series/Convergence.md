---
title: Convergence of Real Series
tags:
    - convergence
    - real-series
    - real-analysis
---

# Convergence

Since a [real series](./index.md) $\displaystyle \sum_{n \in \mathcal{D}} a_n$ is just a [real sequence](../Real%20Sequences/index.md), the definitions and terminology for convergence of series is the same as those used for [convergence](../Real%20Sequences/Convergence.md) of sequences. What is different, however, is the notation used.

>[!NOTATION] Notation: Convergence of Real Series
>
>If $\displaystyle \sum_{n \in \mathcal{D}} a_n$ [converges](../Real%20Sequences/Convergence.md) to $L$, we write
>
>$$
>\sum_{n \in \mathcal{D}} a_n = L
>$$
>
>Instead of calling $L$ the limit of $\displaystyle \sum_{n \in \mathcal{D}} a_n$, we usually say it is its **value**.
>

## Absolute Convergence

>[!DEFINITION] Definition: Absolute Convergence of Real Series
>
>A [real series](./index.md) $\displaystyle \sum_{n \in \mathcal{D}} a_n$ **converges absolutely** to $L$ iff the [series](./index.md) $\displaystyle \sum_{n \in \mathcal{D}} |a_n|$ [converges](Convergence.md) to $L$.
>

>[!THEOREM] Theorem: Absolute Convergence $\implies$ Convergence
>
>If a [real series](./index.md) is [absolutely convergent](Convergence.md#absolute%20convergence) towards $L \in \mathbb{C}$, then it is also [convergent](Convergence.md) towards $L$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Conditional Convergence

>[!DEFINITION] Definition: Conditional Convergence
>
>A [real series](./index.md) is **conditionally convergent** iff it is [convergent](Convergence.md) but not [absolutely convergent](Convergence.md#absolute%20convergence).
>

# Criteria for Convergence and Divergence

>[!THEOREM] Theorem: Divergence Test
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n$ be a [real series](./index.md).
>
>If the [sequence](../Real%20Sequences/index.md) $(a_n)_{n \in \mathcal{D}}$ [diverges](../Real%20Sequences/Convergence.md) or its [limit](../Real%20Sequences/Convergence.md) is not zero, then $\displaystyle \sum_{n \in \mathcal{D}} a_n$ [diverges](../Real%20Sequences/Convergence.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Minorant Divergence Test
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n$ be a [real series](./index.md).
>
>If there exists some [divergent](Convergence.md) [real series](./index.md) $\displaystyle \sum_{n \in \mathcal{D}} b_n$ and some integer $N$ such that $0 \le b_n \le a_n$ for all $n \ge N$, then $\displaystyle \sum_{n \in \mathcal{D}} a_n$ also [diverges](Convergence.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Majorant Convergence Test
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n$ be a [real series](./index.md).
>
>If there exists some [convergent](Convergence.md) [real series](./index.md) $\displaystyle \sum_{n \in \mathcal{D}} b_n$ and some integer $N$ such that $|a_n| \le b_n$ for all $n \ge N$, then $\displaystyle \sum_{n \in \mathcal{D}} a_n$ is [absolutely convergent](Convergence.md#absolute%20convergence).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Quotient Criterion
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n$ be a [real series](./index.md).
>
>If the [sequence](../Real%20Sequences/index.md) $\left|\frac{a_{n+1}}{a_n}\right|$ [converges](../Real%20Sequences/Convergence.md), then $\displaystyle \sum_{n \in \mathcal{D}} a_n$ is:
>- [absolutely convergent](Convergence.md#absolute%20convergence) if 
>
>$$
>\displaystyle \lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| \lt 1
>$$
>
>- [divergent](Convergence.md) if 
>
>$$
>\displaystyle \lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| \gt 1
>$$
>
>>[!NOTE] 
>>
>>If $\displaystyle \lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| = 1$, then this theorem is useless.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Square Root Criterion
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n$ be a [real series](./index.md).
>
>If the [sequence](../Real%20Sequences/index.md) $\sqrt[n]{|a_n|}$ [converges](../Real%20Sequences/Convergence.md), then $\displaystyle \sum_{n \in \mathcal{D}} a_n$ is:
>- [absolutely convergent](Convergence.md#absolute%20convergence) if 
>
>$$
>\displaystyle \lim_{n \to \infty} \sqrt[n]{|a_n|} \lt 1
>$$
>
>- [divergent](Convergence.md) if 
>
>$$
>\displaystyle \lim_{n \to \infty} \sqrt[n]{|a_n|} \gt 1
>$$
>
>>[!NOTE] 
>>
>>If $\displaystyle \lim_{n \to \infty} \sqrt[n]{|a_n|} = 1$, then this theorem is useless.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>