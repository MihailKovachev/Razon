---
title: Real Power Series
tags:
  - real-power-series
  - real-analysis
  - mathematics
---

# Real Power Series

>[!DEFINITION] Definition: Real Power Series
>
>A **real power series** is an [expression](../../Logic/Formal%20Languages.md) of the form
>
>$$
>\sum_{n\in \mathcal{D}} a_n (x-c)^n,
>$$
>
>where $(a_n)_{n \in \mathcal{D}}$ is a [real sequence](./Real%20Sequences.md) and $c \in \mathbb{R}$.
>
>>[!INTUITION]
>>
>>By plugging in a concrete value $x^\ast \in \mathbb{R}$ for $x$, one obtains the [real series](./Real%20Series.md)
>>
>>$$
>>\sum_{n \in \mathcal{D}} a_n (x^{\ast} - c)^n
>>$$
>>
>

# Convergence

>[!DEFINITION] Definition: Convergence and Divergence of Power Series
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n (x-c)^n$ be a [real power series](./Real%20Power%20Series.md) and let $z_0 \in \mathbb{R}$.
>
>We say that $\displaystyle \sum_{n \in \mathcal{D}} a_n (x-c)^n$
>- **is convergent** or **converges** for $z_0$ if the resultant [real series](./Real%20Series.md) $\sum_{n \in \mathcal{D}} a_n (z_0 - c)^n$ is [convergent](./Real%20Series.md#Convergence);
>- **is absolutely convergent** or **converges absolutely** for $z_0$ if the resultant [real series](./Real%20Series.md) $\sum_{n \in \mathcal{D}} a_n (z_0 - c)^n$ is [absolutely convergent](./Real%20Series.md#Convergence);
>- **is divergent** or **diverges** for $z_0$ if the resultant [real series](./Real%20Series.md) $\sum_{n \in \mathcal{D}} a_n (z_0 - c)^n$ is [divergent](./Real%20Series.md#Convergence);
>

>[!THEOREM] Theorem: Convergence Intervals
>
>If the [real power series](./Real%20Power%20Series.md) $\sum_{n \in \mathcal{D}} a_n (x-c)^n$ [converges](#Convergence) for $w \in \mathbb{R}$, then it also [converges](#Convergence) for all $w' \in \mathbb{R}$ with $|w' - c| \lt |w - c|$.
>
>>[!PROOF]-
>>
>>Since the [series](./Real%20Series.md) $\sum_{n \in \mathcal{D}} a_n (w-c)^n$ [converges](./Real%20Series.md#Convergence), we know that the [limit](./Real%20Sequences.md#Convergence) of $a_n (w - c)^n$ must be $0$:
>>
>>$$
>>\lim_{n \to \infty} a_n (w-c)^n = 0
>>$$
>>
>>Since $a_n (w - c)^n$ is [convergent](./Real%20Sequences.md#Convergence), it must be [bounded](./Boundedness%20of%20Real%20Functions.md), i.e. there exists $B \in \mathbb{R}_{\gt 0}$ such that
>>
>>$$
>>|a_n (w-c)^n| \le B
>>$$
>>
>>for all $n \in \mathcal{D}$.
>>
>>For $w'$ we have
>>
>>$$
>>|a_n (w' - c)^n| = \left|a_n(w' - c)^n \frac{(w-c)^n}{(w-c)^n}\right| = \left|a_n(w - c)^n\right|\left| \frac{w'-c}{w-c}\right|^n
>>$$
>>
>>Since $|a_n (w-c)^n| \le B$ for all $n\in\mathcal{D}$, we know that
>>
>>$$
>>|a_n (w' - c)^n| \le B \left| \frac{w'-c}{w-c}\right|^n
>>$$
>>
>>for all $n \in \mathcal{D}$. Let $q = \left| \frac{w'-c}{w-c}\right|$, i.e.
>>
>>$$
>>|a_n (w' - c)^n| \le B q^n
>>$$
>>
>>Since $|w'-c| \lt |{w-c}|$, we know that $q \lt 1$. Therefore, $\sum_{n \in \mathcal{D}} B q^n$ is [convergent](./Real%20Series.md#Convergence) ($\sum_{n\in\mathcal{D}}q^n$ is a [geometric series](./Real%20Series.md#Convergence)). The [convergence](./Real%20Series.md) of $\sum_{n \in \mathcal{D}} a_n(w'-c)^n$ is thus guaranteed by the [majorant convergence criterion](./Real%20Series.md#Convergence).
>>
>

>[!THEOREM] Theorem: Radius of Convergence
>
>For each [real power series](./Real%20Power%20Series.md) $\displaystyle \sum_{n \in \mathcal{D}} a_n (x - c)^n$, there exists some $r \in \mathbb{R}_{\ge 0} \cup \{\infty\}$ such that:
>- If $r = 0$, then the [power series](./Real%20Power%20Series.md) [converges](#Convergence) only for $x = c$.
>- If $r \in (0; \infty)$, then the [power series](./Real%20Power%20Series.md) [converges absolutely](#Convergence) for all $x \in \mathbb{R}$ with $|x - c| \lt r$ and [diverges](#Convergence) for all $x \in \mathbb{R}$ with $|x - c| \gt r$. The behavior for $x \in \mathbb{R}$ with $|x| = r$ must be examined separately.
>- If $r = \infty$, then the [power series](./Real%20Power%20Series.md) [converges absolutely](#Convergence) for all $x \in \mathbb{R}$.
>
>>[!DEFINITION] Definition: Radius of Convergence
>>
>>We call $r$ the **radius of convergence**.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Radius of Convergence via Quotient Limit
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n (x - c)^n$ be a [real power series](./Real%20Power%20Series.md).
>
>If the [limit](./Real%20Sequences.md) of $\left|\frac{a_n}{a_{n+1}}\right|$ exists or is $\infty$, then it is equal to the [radius of convergence](./Real%20Power%20Series.md) $r$:
>
>$$
>r = \lim_{n \to \infty}\left|\frac{a_n}{a_{n+1}}\right| \in \mathbb{R}_{\ge 0} \cup \{\infty\}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: $\sum_{n = 0}^{\infty} x^n$
>>
>>We examine the [real power series](./Real%20Power%20Series.md)
>>
>>$$
>>\sum_{n = 0}^{\infty} x^n
>>$$
>>
>>To see that it is indeed a [real power series](./Real%20Power%20Series.md), we rewrite it a bit:
>>
>>$$
>>\sum_{n = 0}^{\infty} a_n(x - 0)^n \qquad a_n = 1
>>$$
>>
>>We thus have the following:
>>
>>$$
>>r = \lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| = 1
>>$$
>>
>>Therefore, $\sum_{n = 0}^{\infty} x^n$ is [absolutely convergent](#Convergence) when $|x| \lt 1$ and [divergent](#Convergence) when $|x| \gt 1$. Moreover, we have noticed that $\sum_{n = 0}^{\infty} x^n$ is a [geometric series](./Real%20Series.md) for each $x \in \mathbb{R}$. Therefore, we know that it is also [divergent](#Convergence) when $|x| = 1$.
>>
>
>>[!EXAMPLE]- Example: $\sum_{n=1}\frac{1}{n}x^n$
>>
>>We examine the following [real power series](./Real%20Power%20Series.md):
>>
>>$$
>>\sum_{n=1}\frac{1}{n}x^n
>>$$
>>
>>To see that it is indeed a [real power series](./Real%20Power%20Series.md), we can rewrite it a bit:
>>
>>$$
>>\sum_{n = 1}^{\infty}a_n (x - c)^n \qquad a_n = \frac{1}{n}, c = 0
>>$$
>>
>>We therefore have:
>>
>>$$
>>r = \lim_{n \to \infty}\left|\frac{a_n}{a_{n+1}}\right| = \lim_{n \to \infty}\left|\frac{n+1}{n}\right| = 1
>>$$
>>
>>For $x = -1$, we have [convergence](./Real%20Series.md#Convergence) by the [Leibniz convergence criterion](./Real%20Series.md#Convergence). For $x = 1$, we get the [harmonic series](./Real%20Series.md) which is [divergent](./Real%20Series.md#Convergence).
>>
>
>>[!EXAMPLE]- Example: $\sum_{n = 1}^{\infty} \frac{1}{n^2} x^n$
>>
>>We examine the following [real power series](./Real%20Power%20Series.md):
>>
>>$$
>>\sum_{n=1}\frac{1}{n^2}x^n
>>$$
>>
>>To see that it is indeed a [real power series](./Real%20Power%20Series.md), we can rewrite it a bit:
>>
>>$$
>>\sum_{n = 1}^{\infty}a_n (x - c)^n \qquad a_n = \frac{1}{n^2}, c = 0
>>$$
>>
>>We therefore have:
>>
>>$$
>>r = \lim_{n \to \infty}\left|\frac{a_n}{a_{n+1}}\right| = \lim_{n \to \infty}\left|\frac{(n+1)^2}{n^2}\right| = 1
>>$$
>>
>>For $x = \pm 1$, the [power series](./Real%20Power%20Series.md) is [absolutely convergent](./Real%20Power%20Series.md) by the [majorant convergence criterion](./Real%20Series.md), since $\sum_{n = 1}^{\infty} \frac{1}{n^2}$ is [convergent](./Real%20Power%20Series.md).
>>
>

>[!THEOREM] Cauchy-Hadamard Theorem
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n (x - c)^n$ be a [real power series](./Real%20Power%20Series.md).
>
>The [limit superior](./Real%20Sequences.md#Limit%20Inferior%20and%20Limit%20Superior) of the [sequence](./Real%20Sequences.md) $\sqrt[n]{|a_n|}$ can be used to find the [radius of convergence](#Convergence):
>
>- If $\limsup_{n\to \infty} \sqrt[n]{|a_n|} = 0$, then $R = \infty$.
>- If $\limsup_{n\to \infty} \sqrt[n]{|a_n|} \in (0; \infty)$, then $R = \frac{1}{\limsup_{n\to \infty} \sqrt[n]{|a_n|}}$.
>- If $\limsup_{n\to \infty} \sqrt[n]{|a_n|} = \infty$, then $R = 0$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: $\sum_{k = 0}^{\infty} x^{k^2}$
>>
>>We examine the following [real power series](./Real%20Power%20Series.md):
>>
>>$$
>>\sum_{k = 0}^{\infty} x^{k^2} = 1 + x + x^4 + x^9 + x^{16} + \cdots
>>$$
>>
>>To see that this is indeed a [real power series](./Real%20Power%20Series.md), we need to rewrite it a bit:
>>
>>$$
>>\sum_{n = 0}^{\infty} a_n(x-0)^{n} \qquad a_n = \begin{cases}1 & \text{if } n = k^2, k \in \mathbb{N}_0 \\ 0 & \text{otherwise}\end{cases}
>>$$
>>
>>Therefore, we have:
>>
>>$$
>>\sqrt[n]{|a_n|} = \begin{cases}1 & \text{if } n = k^2, k \in \mathbb{N}_0 \\ 0 & \text{otherwise}\end{cases}
>>$$
>>
>>The [sequence](./Real%20Sequences.md) $\sqrt[n]{|a_n|}$ is [divergent](./Real%20Sequences.md#Convergence), but its [limit superior](./Real%20Sequences.md#Limit%20Inferior%20and%20Limit%20Superior) is $1$:
>>
>>$$
>>\limsup_{n\to \infty} \sqrt[n]{|a_n|} = 1
>>$$
>>
>>Therefore, the [radius of convergence](#Convergence) is $1$:
>>
>>$$
>>r = \frac{1}{\limsup_{n\to \infty} \sqrt[n]{|a_n|}} = \frac{1}{1} = 1
>>$$
>>
>

>[!THEOREM] Theorem: Radius of Convergence via $n$-th Root Limit
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n (x - c)^n$ be a [real power series](./Real%20Power%20Series.md).
>
>If the [limit](./Real%20Sequences.md) of $\frac{1}{\sqrt[n]{|a_n|}}$ exists or is $\infty$, then it is equal to the [radius of convergence](./Real%20Power%20Series.md) $r$:
>
>$$
>r = \lim_{n \to \infty}\frac{1}{\sqrt[n]{|a_n|}} \in \mathbb{R}_{\ge 0} \cup \{\infty\}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>