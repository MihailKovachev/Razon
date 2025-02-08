---
title: Convergence of Real Power Series
tags:
    - real-power-series
    - real-analysis
    - mathematics
---

# Convergence
>[!DEFINITION] Definition: Convergence and Divergence of Power Series
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n (x-c)^n$ be [real power series](./index.md) and let $x^{\ast} \in \mathbb{R}$.
>
>We say that $\displaystyle \sum_{n \in \mathcal{D}} a_n (x-c)^n$
>- **is convergent** or **converges** for $x^{\ast}$ if the resultant [real series](../Real%20Series/index.md) $\sum_{n \in \mathcal{D}} a_n (x^{\ast} - c)^n$ is [convergent](../Real%20Series/Convergence.md);
>- **is absolutely convergent** or **converges absolutely** for $x^{\ast}$ if the resultant [real series](../Real%20Series/index.md) $\sum_{n \in \mathcal{D}} a_n (x^{\ast} - c)^n$ is [absolutely convergent](../Real%20Series/Convergence.md#absolute%20convergence);
>- **is divergent** or **diverges** for $x^{\ast}$ if the resultant [real series](../Real%20Series/index.md) $\sum_{n \in \mathcal{D}} a_n (x^{\ast} - c)^n$ is [divergent](../Real%20Series/Convergence.md).
>

## Interval of Convergence

>[!THEOREM] Theorem: Interval of Convergence
>
>There are only three possibilities for the [convergence](Convergence.md) of every [real power series](./index.md) $\displaystyle \sum_{n \in \mathcal{D}} a_n (x - c)^n$:
>- The power series [converges](Convergence.md) only for $x = c$.
>- The power series [converges](Convergence.md) for all $x \in \mathbb{R}$.
>- There exists some $r \gt 0$ such that the power series [converges](Convergence.md) if $x \in (c - r; c + r)$ and [diverges](Convergence.md) if $|x - c| \gt r$. In this case, the power series may or may not [converge](Convergence.md) for $x = c + r$ or $x = c - r$ or both 
>
>>[!PROOF]-
>>
>>TODO
>
>>[!DEFINITION] Definition: Interval of Convergence
>>
>>The [set](../../../Set%20Theory/index.md) of all $x \in \mathbb{R}$ for which a [power series](./index.md) $\displaystyle \sum_{n \in \mathcal{D}} a_n (x-c)^n$ [converges](Convergence.md) is known as its **interval of convergence** and if this interval is finite, then we call half of its length the **radius of convergence**.
>>
>>![](res/Interval%20of%20convergence.drawio.svg)
>>
>

### Determining the Interval of Convergence

>[!ALGORITHM] Algorithm: Determining the Interval of Convergence
>
>We are given a [real power series](./index.md) $\displaystyle \sum_{n \in \mathcal{D}} a_n (x-c)^n$ and want to determine its [interval of convergence](Convergence.md).
>
>1. Evaluate either one of the [limits](../Real%20Sequences/Convergence.md) $\lim_{n \to \infty} \left| \frac{a_n}{a_{n+1}}\right|$ and $\lim_{n\to \infty} \frac{1}{\sqrt[n]{|a_n|}}$. Choose whichever one is easier to calculate.
>
>2. If the limit is zero, then the power series [converges](Convergence.md) only for $x = c$.
> 
>3. If the limit is $+\infty$, then the power series [converges](Convergence.md) for every $x \in \mathbb{R}$.
>
>4. If the limit is equal to some nonzero $r \in \mathbb{R}$, then the power series [converges](Convergence.md) for $x \in (c - r; c + r)$. However, we also need to check whether it converges for $x = c -r$ and $x = c + r$.
>	-  Evaluate the power series at $x = c - r$. If the resultant [series](../Real%20Series/index.md) $\sum_{n \in \mathcal{D}} a_n (-r)^n$ is [convergent](../Real%20Series/Convergence.md), then the power series [converges](Convergence.md) for $x = c - r$ as well.
>	-  Evaluate the power series at $x = c + r$. If the resultant [series](../Real%20Series/index.md) $\sum_{n \in \mathcal{D}} a_n r^n$ is [convergent](../Real%20Series/Convergence.md), then the power series [converges](Convergence.md) for $x = c + r$ as well.
>