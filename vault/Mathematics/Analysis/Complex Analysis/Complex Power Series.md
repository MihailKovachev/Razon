---
title: Complex Power Series
tags:
  - complex-power-series
  - complex-analysis
  - mathematics
---

# Complex Power Series

>[!DEFINITION] Definition: Complex Power Series
>
>A **complex power series** is an expression of the form
>
>$$
>\sum_{n\in \mathcal{D}} a_n (z-c)^n,
>$$
>
>where $(a_n)_{n \in \mathcal{D}}$ is a [complex sequence](./Complex%20Sequences.md) and $c \in \mathbb{C}$.
>
>>[!INTUITION]
>>
>>By plugging in a concrete value $z_0 \in \mathbb{C}$ for $z$, one obtains the [complex series](./Complex%20Series.md)
>>
>>$$
>>\sum_{n \in \mathcal{D}} a_n (z_0 - c)^n
>>$$
>>
>

# Convergence

>[!DEFINITION] Definition: Convergence and Divergence of Power Series
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n (z-c)^n$ be a [complex power series](./Complex%20Power%20Series.md) and let $z_0 \in \mathbb{C}$.
>
>We say that $\displaystyle \sum_{n \in \mathcal{D}} a_n (z-c)^n$
>- **is convergent** or **converges** for $z_0$ if the resultant [complex series](./Complex%20Series.md) $\sum_{n \in \mathcal{D}} a_n (z_0 - c)^n$ is [convergent](./Complex%20Series.md#Convergence);
>- **is absolutely convergent** or **converges absolutely** for $z_0$ if the resultant [complex series](./Complex%20Series.md) $\sum_{n \in \mathcal{D}} a_n (z_0 - c)^n$ is [absolutely convergent](./Complex%20Series.md#Convergence);
>- **is divergent** or **diverges** for $z_0$ if the resultant [complex series](./Complex%20Series.md) $\sum_{n \in \mathcal{D}} a_n (z_0 - c)^n$ is [divergent](./Complex%20Series.md#Convergence);
>

>[!THEOREM] Theorem: Convergence Disks
>
>If the [complex power series](./Complex%20Power%20Series.md) $\sum_{n \in \mathcal{D}} a_n (z-c)^n$ [converges](#Convergence) for $w \in \mathbb{C}$, then it also [converges](#Convergence) for all $w' \in \mathbb{C}$ with $|w' - c| \lt |w - c|$.
>
>>[!PROOF]-
>>
>>Since the [series](./Complex%20Series.md) $\sum_{n \in \mathcal{D}} a_n (w-c)^n$ [converges](./Complex%20Series.md#Convergence), we know that the [limit](./Complex%20Sequences.md#Convergence) of $a_n (w - c)^n$ must be $0$:
>>
>>$$
>>\lim_{n \to \infty} a_n (w-c)^n = 0
>>$$
>>
>>Since $a_n (w - c)^n$ is [convergent](./Complex%20Sequences.md#Convergence), it must be [bounded](./Boundedness%20of%20Complex%20Functions.md), i.e. there exists $B \in \mathbb{R}_{\gt 0}$ such that
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
>>Since $|w'-c| \lt |{w-c}|$, we know that $q \lt 1$. Therefore, $\sum_{n \in \mathcal{D}} B q^n$ is [convergent](../Real%20Analysis/Real%20Series.md#Convergence) ($\sum_{n\in\mathcal{D}}q^n$ is a [geometric series](../Real%20Analysis/Real%20Series.md#Convergence)). The [convergence](./Complex%20Series.md) of $\sum_{n \in \mathcal{D}} a_n(w'-c)^n$ is thus guaranteed by the [majorant convergence criterion](./Complex%20Series.md#Convergence).
>>
>

>[!THEOREM] Theorem: Radius of Convergence
>
>For each [complex power series](./Complex%20Power%20Series.md) $\displaystyle \sum_{n \in \mathcal{D}} a_n (z - c)^n$, there exists some $r \in \mathbb{R}_{\ge 0} \cup \{\infty\}$ such that:
>- If $r = 0$, then the [power series](./Complex%20Power%20Series.md) [converges](#Convergence) only for $x = c$.
>- If $r \in (0; \infty)$, then the [power series](./Complex%20Power%20Series.md) [converges absolutely](#Convergence) for all $z \in \mathbb{C}$ with $|z - c| \lt r$ and [diverges](#Convergence) for all $z \in \mathbb{C}$ with $|z - c| \gt r$. The behavior for $z \in \mathbb{C}$ with $|z| = r$ must be examined separately.
>- If $r = \infty$, then the [power series](./Complex%20Power%20Series.md) [converges absolutely](#Convergence) for all $z \in \mathbb{C}$.
>
>>[!DEFINITION] Definition: Radius of Convergence
>>
>>We call $r$ the **radius of convergence**.
>>
>>
>>![](./res/Radius%20of%20Convergence.svg)
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Radius of Convergence via Quotient Limit
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n (z - c)^n$ be a [complex power series](./Complex%20Power%20Series.md).
>
>If the [limit](../Real%20Analysis/Real%20Sequences.md) of $\left|\frac{a_n}{a_{n+1}}\right|$ exists or is $\infty$, then it is equal to the [radius of convergence](./Complex%20Power%20Series.md) $r$:
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
>>[!EXAMPLE]- Example: $\sum_{n = 0}^{\infty} z^n$
>>
>>We examine the [complex power series](./Complex%20Power%20Series.md)
>>
>>$$
>>\sum_{n = 0}^{\infty} z^n
>>$$
>>
>>To see that it is indeed a [complex power series](./Complex%20Power%20Series.md), we rewrite it a bit:
>>
>>$$
>>\sum_{n = 0}^{\infty} a_n(z - 0)^n \qquad a_n = 1
>>$$
>>
>>We thus have the following:
>>
>>$$
>>r = \lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| = 1
>>$$
>>
>>Therefore, $\sum_{n = 0}^{\infty} z^n$ is [absolutely convergent](#Convergence) when $|z| \lt 1$ and [divergent](#Convergence) when $|z| \gt 1$. Moreover, we have noticed that $\sum_{n = 0}^{\infty} z^n$ is a [geometric series](./Complex%20Series.md) for each $z \in \mathbb{C}$. Therefore, we know that it is also [divergent](#Convergence) when $|z| = 1$.
>>
>

>[!THEOREM] Cauchy-Hadamard Theorem
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n (z - c)^n$ be a [complex power series](./Complex%20Power%20Series.md).
>
>The [limit superior](../Real%20Analysis/Real%20Sequences.md#Limit%20Inferior%20and%20Limit%20Superior) of the [sequence](../Real%20Analysis/Real%20Sequences.md) $\sqrt[n]{|a_n|}$ can be used to find the [radius of convergence](#Convergence):
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
>>[!EXAMPLE]- Example: $\sum_{k = 0}^{\infty} z^{k^2}$
>>
>>We examine the following [complex power series](./Complex%20Power%20Series.md):
>>
>>$$
>>\sum_{k = 0}^{\infty} z^{k^2} = 1 + z + z^4 + z^9 + z^{16} + \cdots
>>$$
>>
>>To see that this is indeed a [complex power series](./Complex%20Power%20Series.md), we need to rewrite it a bit:
>>
>>$$
>>\sum_{n = 0}^{\infty} a_n(z-0)^{n} \qquad a_n = \begin{cases}1 & \text{if } n = k^2, k \in \mathbb{N}_0 \\ 0 & \text{otherwise}\end{cases}
>>$$
>>
>>Therefore, we have:
>>
>>$$
>>\sqrt[n]{|a_n|} = \begin{cases}1 & \text{if } n = k^2, k \in \mathbb{N}_0 \\ 0 & \text{otherwise}\end{cases}
>>$$
>>
>>The [sequence](../Real%20Analysis/Real%20Sequences.md) $\sqrt[n]{|a_n|}$ is [divergent](../Real%20Analysis/Real%20Sequences.md#Convergence), but its [limit superior](../Real%20Analysis/Real%20Sequences.md#Limit%20Inferior%20and%20Limit%20Superior) is $1$:
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
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n (z - c)^n$ be a [complex power series](./Complex%20Power%20Series.md).
>
>If the [limit](../Real%20Analysis/Real%20Sequences.md) $\lim_{n \to \infty} \sqrt[n]{|a_n|} = L$ exists or is $\infty$, then the [radius of convergence](./Complex%20Power%20Series.md) $r$ is given by:
>
>$$
>r = \begin{cases} 
>0 & \text{if } L = \infty \\
>\infty & \text{if } L = 0 \\
>\frac{1}{L} & \text{otherwise}
>\end{cases}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
