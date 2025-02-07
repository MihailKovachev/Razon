---
title: Convergence of Complex Power Series
tags:
    - convergence
    - complex-power-series
    - complex-analysis
    - mathematics
---

# Convergence

>[!DEFINITION] Definition: Convergence and Divergence of Power Series
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n (x-c)^n$ be [complex power series](./index.md) and let $x^{\ast} \in \mathbb{R}$.
>
>We say that $\displaystyle \sum_{n \in \mathcal{D}} a_n (x-c)^n$
>- **is convergent** or **converges** for $x^{\ast}$ if the resultant [complex series](../Complex%20Series/index.md) $\sum_{n \in \mathcal{D}} a_n (x^{\ast} - c)^n$ is [convergent](../Complex%20Series/Convergence.md);
>- **is absolutely convergent** or **converges absolutely** for $x^{\ast}$ if the resultant [complex series](../Complex%20Series/index.md) $\sum_{n \in \mathcal{D}} a_n (x^{\ast} - c)^n$ is [absolutely convergent](../Complex%20Series/Convergence.md#absolute%20convergence);
>- **is divergent** or **diverges** for $x^{\ast}$ if the resultant [complex series](../Complex%20Series/index.md) $\sum_{n \in \mathcal{D}} a_n (x^{\ast} - c)^n$ is [divergent](../Complex%20Series/Convergence.md).
>

## Radius of Convergence

>[!THEOREM] Theorem: Radius of Convergence
>
>There are only three possibilities for the [convergence](Convergence.md) of every [complex power series](./index.md) $\displaystyle \sum_{n \in \mathcal{D}} a_n (x - c)^n$:
>- The power series [converges](Convergence.md) only for $x = c$.
>- The power series [converges](Convergence.md) for all $x \in \mathbb{C}$.
>- There exists some $r \gt 0$ such that the power series [converges](Convergence.md) if $|x - c| \lt r$ and [diverges](Convergence.md) if $|x - c| \gt r$. If $|x - c| = r$, then the power series may or may not converge and it might do so only for some points but not for others.
>
>![](res/Radius%20of%20Convergence.drawio.svg) 
>
>>[!PROOF]-
>>
>>TODO
>
>>[!DEFINITION] Definition: Radius of Convergence
>>
>>If $r$ exists, then we call it the **radius of convergence**. Furthermore, if the power series converges only for $x = c$, we usually say that the radius of convergence is zero. If the power series converges for all $x \in \mathbb{C}$, then we say that the radius of convergence if infinite.
>>
>

### Determining the Radius of Convergence

>[!ALGORITHM] Algorithm: Determining the Radius of Convergence
>
>We are given a [real power series](./index.md) $\displaystyle \sum_{n \in \mathcal{D}} a_n (x-c)^n$ and want to determine its [radius of convergence](Convergence.md).
>
>1. Evaluate either one of the [limits](../../Real%20Analysis/Real%20Sequences/Convergence.md) $\lim_{n \to \infty} \left| \frac{a_n}{a_{n+1}}\right|$ and $\lim_{n\to \infty} \frac{1}{\sqrt[n]{|a_n|}}$. Choose whichever one is easier to calculate.
>
>2. If the limit is zero, then the power series [converges](Convergence.md) only for $x = c$.
> 
>3. If the limit is $+\infty$, then the power series [converges](Convergence.md) for every $x \in \mathbb{R}$.
>
>4. If the limit is some nonzero real number, then it is the radius of convergence.
>