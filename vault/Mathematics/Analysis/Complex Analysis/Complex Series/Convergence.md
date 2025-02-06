---
title: Convergence of Complex Series
tags:
    - convergence
    - complex-series
    - complex-analysis
    - mathematics
---

# Convergence

Since a [complex series](./index.md) $\displaystyle \sum_{n \in \mathcal{D}} a_n$ is just a [complex sequence](../Complex%20Sequences/index.md), the definitions and terminology for convergence of series is the same as those used for [convergence](../Complex%20Sequences/Convergence.md) of sequences. What is different, however, is the notation used.

>[!NOTATION] Notation: Convergence of Complex Series
>
>If $\displaystyle \sum_{n \in \mathcal{D}} a_n$ [converges](../Complex%20Sequences/Convergence.md) to $L$, we write
>
>$$
>\sum_{n \in \mathcal{D}} a_n = L
>$$
>
>Instead of calling $L$ the limit of $\displaystyle \sum_{n \in \mathcal{D}} a_n$, we usually say it is its **value**.
>

## Absolute Convergence

>[!DEFINITION] Definition: Absolute Convergence of Complex Series
>
>A [complex series](./index.md) $\displaystyle \sum_{n \in \mathcal{D}} a_n$ **converges absolutely** to $L$ iff the [real series](../../Real%20Analysis/Real%20Series/index.md) $\displaystyle \sum_{n \in \mathcal{D}} |a_n|$ [converges](../../Real%20Analysis/Real%20Series/Convergence.md) to $L$.
>

>[!THEOREM] Theorem: Absolute Convergence $\implies$ Convergence
>
>If a [complex series](./index.md) is [absolutely convergent](Convergence.md#absolute%20convergence) towards $L \in \mathbb{C}$, then it is also [convergent](Convergence.md) towards $L$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Conditional Convergence

>[!DEFINITION] Definition: Conditional Convergence
>
>A [complex series](./index.md) is **conditionally convergent** iff it is [convergent](Convergence.md) but not [absolutely convergent](Convergence.md#absolute%20convergence).
>

# Criteria for Convergence and Divergence

>[!THEOREM] Theorem: Test for Divergence
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n$ be a [complex series](./index.md).
>
>If the [sequence](../Complex%20Sequences/index.md) $(a_n)_{n \in \mathcal{D}}$ [diverges](../Complex%20Sequences/Convergence.md) or its [limit](../Complex%20Sequences/Convergence.md) is not zero, then $\displaystyle \sum_{n \in \mathcal{D}} a_n$ [diverges](../Complex%20Sequences/Convergence.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>