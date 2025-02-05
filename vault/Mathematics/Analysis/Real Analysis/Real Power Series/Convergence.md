---
title: Convergence of Real Power Series
tags:
    - real-power-series
    - real-analysis
    - mathematics
---

>[!DEFINITION] Definition: Convergence of Power Series
>
>We say that a [real power series](Real%20Power%20Series.md) $\sum_{n=0}^\infty c_n (x-a)^n$ **converges for** $x^\ast \in \mathbb{R}$ if the resultant [real series](../Real%20Series/index.md) $\sum_{n=0}^\infty c_n (x^\ast - a)^n$ [converges](../Real%20Series/Convergence.md).
>

>[!THEOREM] Theorem: Interval of Convergence
>
>For a [real power series](Real%20Power%20Series.md) $\displaystyle \sum_{n=0}^\infty c_n (x-a)^n$ and a point $x^\ast \in \mathbb{R}$ there are only three possibilities:
>- The series [converges](Convergence.md) only for $x^\ast = a$.
>- The series converges for all $x^\ast \in \mathbb{R}$.
>- There exists an $r \gt 0$ such that the series converges if $|x^\ast - a| \lt r$ and diverges if $|x^\ast - a| \gt r$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Interval of Convergence
>>
>>The [set](../../../../Set%20Theory/Set.md) of all $x \in \mathbb{R}$ for which a [power series](Real%20Power%20Series.md) $\displaystyle \sum_{n=0}^\infty c_n (x-a)^n$ [converges](Convergence.md) is known as its **interval of convergence** and if this interval is finite, then we call half of its length the **radius of convergence**.
>>
>>^intervalofconvergence
>>
>