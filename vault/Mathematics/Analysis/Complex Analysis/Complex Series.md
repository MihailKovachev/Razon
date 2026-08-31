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
>Let $\{z_n\}_{n \in \mathcal{D}}$ be a [complex sequence](./Complex%20Sequences.md). 
>
>The $k$-th **partial sum** of $\{z_n\}$ is the sum of its first $k$ numbers:
>
>$$
>\sum_{\begin{aligned}j &\in \mathcal{D} \\ j &\le k \end{aligned}} a_j
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

Given a [complex sequence](./Complex%20Sequences.md) $(z_n)_{n \in \mathcal{D}}$, it is apparent that the [function](./Complex-Valued%20Functions.md) which maps each $k \in \mathcal{D}$ to the $k$-th [partial sum](#Partial%20Sums) of $(z_n)_{n \in \mathcal{D}}$ is itself a [complex sequence](./Complex%20Sequences.md) $(s_n)_{n \in \mathcal{D}}$.

>[!DEFINITION] Definition: Complex Series
>
>A **complex series** is the [complex sequence](./Complex%20Sequences.md) of the [partial sums](#Partial%20Sums) of some other [complex sequence](./Complex%20Sequences.md).
>
>>[!NOTATION]
>>
>>If the sequence is $(z_n)_{n \in \mathcal{D}}$, then we denote the sequence of its partial sums by $\displaystyle \sum_{n \in \mathcal{D}} z_n$. 
>>
>>When $\mathcal{D} = \mathbb{N}_0$ or $\mathcal{D} = \mathbb{N}$, we write $\displaystyle \sum_{n = 0}^{\infty} z_n$ or $\displaystyle \sum_{n = 1}^{\infty} z_n$, respectively.
>>
>>In the case, when $\mathcal{D} = \mathbb{N} \setminus \{0, 1, \dotsc, p - 1\}$ for some integer $p$, we write $\displaystyle \sum_{n = p}^{\infty} z_n$.
>>
>


# Convergence

Since a [complex series](./Complex%20Series.md) $\displaystyle \sum_{n \in \mathcal{D}} z_n$ is just a [complex sequence](./Complex%20Sequences.md), the definitions and terminology for convergence of series is the same as those used for [convergence of sequence](./Complex%20Sequences.md#Convergence),. What is different, however, is the notation used.

>[!NOTATION] Notation: Convergence of Complex Series
>
>If $\displaystyle \sum_{n \in \mathcal{D}} z_n$ [converges](./Complex%20Sequences.md), to $L$ we write
>
>$$
>\sum_{n \in \mathcal{D}} z_n = L
>$$
>
>Instead of calling $L$ the limit of $\displaystyle \sum_{n \in \mathcal{D}} z_n$, we usually say it is its **value**.
>

>[!DEFINITION] Definition: Absolute Convergence of Complex Series
>
>A [complex series](./Complex%20Series.md) $\displaystyle \sum_{n \in \mathcal{D}} z_n$ **converges absolutely** to $L$ iff the [series](../Real%20Analysis/Real%20Series.md) $\displaystyle \sum_{n \in \mathcal{D}} |z_n|$ [converges](../Real%20Analysis/Real%20Series.md#Convergence) to $L$.
>
>>[!EXAMPLE]- Example: $\sum_{n=1}^{\infty} \frac{2}{n^2}-\mathrm{i}\frac{(-1)^n}{n^2}$
>>
>>The [complex series](./Complex%20Series.md) $\sum_{n=1}^{\infty} \frac{2}{n^2}-\mathrm{i}\frac{(-1)^n}{n^2}$ is [absolutely convergent](#Convergence), since
>>
>>$$
>>\sum_{n=1}^{\infty} \left|\frac{2}{n^2}-\mathrm{i}\frac{(-1)^n}{n^2}\right| = \sum_{n=1}^{\infty} \sqrt{\frac{4}{n^4}+\frac{1}{n^4}} = \sum_{n=1}^{\infty}\frac{\sqrt{5}}{n^2},
>>$$
>>
>>which is [convergent](../Real%20Analysis/Real%20Series.md).
>>
>

>[!DEFINITION] Definition: Conditional Convergence
>
>A [complex series](./Complex%20Series.md) is **conditionally convergent** if it is  [convergent](#Convergence) but not [absolutely convergent](#Convergence).
>

>[!THEOREM] Theorem: Absolute Convergence $\implies$ Convergence
>
>If a [complex series](./Complex%20Series.md) is [absolutely convergent](#Convergence) towards $L \in \mathbb{C}$, then it is also [convergent](#Convergence) towards $L$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Convergence $\implies$ Zero Sequence
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} z_n$ be a [complex series](./Complex%20Series.md).
>
>If $\displaystyle \sum_{n \in \mathcal{D}} z_n$ [converges](#Convergence), then $(z_n)_{n \in \mathcal{D}}$ [converges](./Complex%20Sequences.md) to $0$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Arithmetic with Convergent Series
>
>If $\sum_{n\in\mathcal{D}} z_n$ and $\sum_{n \in \mathcal{D}}w_n$ [converge](#Convergence), then
>
>$$
>\sum_{n \in \mathcal{D}} (\lambda z_n + \mu w_n) = \lambda \sum_{n \in \mathcal{D}} z_n + \mu \sum_{n \in \mathcal{D}} w_n
>$$
>
>for all $\lambda, \mu \in \mathbb{C}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Majorant Convergence Test
>
>Let $\sum_{n \in \mathcal{D}} z_n$ be a [complex series](./Complex%20Series.md).
>
>If there exist a [convergent](../Real%20Analysis/Real%20Series.md) [real series](../Real%20Analysis/Real%20Series.md) $\sum_{n \in \mathcal{D}} b_n$ and some $N \in \mathcal{D}$ such that
>
>$$
>|z_n| \le b_n \qquad \forall n \ge N,
>$$
>
>then $\sum_{n = 1}^{\infty} z_n$ is [absolutely convergent](#Convergence).
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: $\sum_{n=1}^{\infty} z_n = \frac{(1+\mathrm{i})^n}{3^n n}$
>>
>>We examine the following [complex series](./Complex%20Series.md):
>>
>>$$
>>\sum_{n=1}^{\infty} z_n = \frac{(1+\mathrm{i})^n}{3^n n}
>>$$
>>
>>We have:
>>
>>$$
>>|z_n| = \frac{|1+\mathrm{i}|^n}{3^n n} = \frac{\sqrt{2}^n}{3^n n} = \left(\frac{\sqrt{2}}{3}\right)^n\frac{1}{n}
>>$$
>>
>>It is obvious that
>>
>>$$
>>|z_n| = \left(\frac{\sqrt{2}}{3}\right)^n\frac{1}{n} \le \left(\frac{\sqrt{2}}{3}\right)^n
>>$$
>>
>>for all $n \in \mathbb{N}$ and since $\sum_{n = 1}^{\infty} \left(\frac{\sqrt{2}}{3}\right)^n$ [converges](../Real%20Analysis/Real%20Series.md) as a [geometric series](../Real%20Analysis/Real%20Series.md) with $q \lt 1$, we know that $\sum_{n=1}^{\infty} z_n$ is [absolutely convergent](#Convergence).
>>
>

>[!THEOREM] Theorem: Ratio Convergence Test
>
>Let $\sum_{n \in \mathcal{D}} z_n$ be a [complex Series](./Complex%20Series.md).
>
>- (I) If there exists some $N \in \mathcal{D}$ and some $q \in (0;1)$ such that $\left\vert \frac{z_{n+1}}{z_n}\right\vert \le q$ for all $n \ge N$, then $\sum_{n \in \mathcal{D}} z_n$ is [absolutely convergent](#Convergence).
>
>- (II) If there exists some $N \in \mathcal{D}$ such that $\left\vert \frac{z_{n+1}}{z_n}\right\vert \ge 1$ for all $n \ge N$, then $\sum_{n \in \mathcal{D}} z_n$ is [divergent](#Convergence).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: $n$-th Root Convergence Test
>
>Let $\sum_{n \in \mathcal{D}} z_n$ be a [complex series](./Complex%20Series.md).
>
>If the [real sequence](../Real%20Analysis/Real%20Sequences.md) $\sqrt[n]{|z_n|}$ [converges](../Real%20Analysis/Real%20Sequences.md#Convergence), then $\sum_{n \in \mathcal{D}} z_n$ is:
>- [absolutely convergent](#Convergence) if 
>
>$$
>\displaystyle \lim_{n \to \infty} \sqrt[n]{|z_n|} \lt 1
>$$
>
>- [divergent](#Convergence) if 
>
>$$
>\displaystyle \lim_{n \to \infty} \sqrt[n]{|z_n|} \gt 1
>$$
>
>
>>[!PROOF]-
>>
>>TODO
>>
>