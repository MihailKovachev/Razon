---
title: Geometric Series
tags:
    - real-series
    - real-analysis
    - mathematics
---

# Geometric Series

>[!DEFINITION] Definition: Geometric Series
>
>A **geometric series** is a [real series](Real%20Series.md) $\sum_{n = 1}^{\infty} a_n$ such that the [sequence](../Real%20Sequences/Real%20Sequences.md) $(a_n)_{n \in \mathbb{N}}$ can be specified as
>
>$$
>a_n = q^{n-1}a
>$$
>
>for some [real numbers](../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) $a$ and $q$ with $q \ne 0$.
>

## Properties

>[!THEOREM]- Theorem: Product of Members of Geometric Series
>
>If $a_p$ and $a_m$ are members of a [geometric series](Geometric%20Series.md), then for all $k \in \mathbb{N}$ with $k \lt m$, we have
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Partial Sums of Geometric Series
>
>The $n$-th [partial sum](Real%20Series.md#Partial%20Sums) $S_n$ of a [geometric series](Geometric%20Series.md) $a_n$ with ratio $q$ is given by
>
>$$
>S_n = \frac{1 - q^n}{1 - q}a_1
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Convergence of Geometric Series
>
>A [geometric series](Geometric%20Series.md) $(a_n)_{n \in \mathbb{N}}$ with ratio $q$ [converges absolutely](Convergence.md) if and only if $|q| \lt 1$ and [diverges otherwise](Convergence.md). If $(a_n)_{n \in \mathbb{N}}$ [converges](Convergence.md), then
>
>$$
>\sum_{n = 1}^{\infty} a_n = \frac{a_1}{1 - q}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>