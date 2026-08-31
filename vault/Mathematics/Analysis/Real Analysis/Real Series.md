---
tags:
    - real-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Real Series

>[!DEFINITION] Definition: Partial Sum
>
>Let $(a_n)_{n \in \mathcal{D}}$ be a [real sequence](./Real%20Sequences.md).
>
>The $k$-th **partial sum** of $(a_n)_{n \in \mathcal{D}}$ is the sum of its first $k$ numbers:
>
>$$\sum_{\begin{aligned}j &\in \mathcal{D} \\ j &\le k \end{aligned}} a_j$$
>
>>[!NOTATION]
>>
>>$$s_k$$
>>
>

>[!THEOREM] Theorem: Re-Indexing
>
>$$\sum_{k = l}^u a_k = \sum_{j = l + r}^{u+r} a_{j - r}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

Given a [real sequence](./Real%20Sequences.md) $(a_n)_{n \in \mathcal{D}}$, it is apparent that the [real-valued function](./Real-Valued%20Functions.md) which maps each $k \in \mathcal{D}$ to the $k$-th [partial sum](#partial%20sums) of $(a_n)_{n \in \mathcal{D}}$ is itself a [real sequence](./Real%20Sequences.md) $(s_n)_{n \in \mathcal{D}}$.

>[!DEFINITION] Definition: Real Series
>
>A **real series** is the [sequence](./Real%20Sequences.md) of [partial sums](#partial%20sums) of a [real sequence](./Real%20Sequences.md).
>
>>[!NOTATION]
>>
>>If the sequence is $(a_n)_{n \in \mathcal{D}}$, then we denote the sequence of its partial sums by $\displaystyle \sum_{n \in \mathcal{D}} a_n$. 
>>
>>When $\mathcal{D} = \mathbb{N}_0$ or $\mathcal{D} = \mathbb{N}$, we write $\displaystyle \sum_{n = 0}^{\infty} a_n$ or $\displaystyle \sum_{n = 1}^{\infty} a_n$, respectively.
>>
>>In the case, when $\mathcal{D} = \mathbb{N} \setminus \{0, 1, \dotsc, p - 1\}$ for some integer $p$, we write $\displaystyle \sum_{n = p}^{\infty} a_n$.
>>
>

## Convergence

Since a [real series](./Real%20Series.md) $\displaystyle \sum_{n \in \mathcal{D}} a_n$ is just a [real sequence](./Real%20Sequences.md), the definitions and terminology for convergence of series is the same as those used for [convergence](#Convergence) of sequences. What is different, however, is the notation used.

>[!NOTATION] Notation: Convergence of Real Series
>
>If $\displaystyle \sum_{n \in \mathcal{D}} a_n$ [converges](#Convergence) to $L$, we write
>
>$$
>\sum_{n \in \mathcal{D}} a_n = L
>$$
>
>Instead of calling $L$ the limit of $\displaystyle \sum_{n \in \mathcal{D}} a_n$, we usually say it is its **value**.
>

>[!EXAMPLE]- Example: Geometric Series
>
>A **geometric series** is a [real series](./Real%20Series.md)
>
>$$\sum_{n = s}^{\infty} q^n,$$
>
>where $q$ is some [real number](../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) and $s \in \mathbb{N}_0$.
>
>If $|q| \lt 1$, then the [geometric series](./Real%20Series.md) is [convergent](#Convergence) with
>
>$$\sum_{n = s}^{\infty} q^n = \frac{q^s}{1 - q}.$$
>
>If $|q| \ge 1$, then the [geometric series](./Real%20Series.md) is [divergent](#Convergence).
>

>[!EXAMPLE]- Example: The Harmonic Series
>
>The **harmonic series** is the following [real series](./Real%20Series.md):
>
>$$\sum_{n = 1}^{\infty} \frac{1}{n}$$
>
>It [diverges](#Convergence) towards $+\infty$:
>
>$$\sum_{n = 1}^{\infty} \frac{1}{n} = +\infty$$
>

>[!DEFINITION] Definition: Absolute Convergence of Real Series
>
>A [real series](./Real%20Series.md) $\displaystyle \sum_{n \in \mathcal{D}} a_n$ **converges absolutely** or is **absolutely convergent** if the [series](./Real%20Series.md) $\displaystyle \sum_{n \in \mathcal{D}} |a_n|$ [converges](#Convergence).
>
>>[!THEOREM] Theorem: Alternative Definition
>>
>>A [real series](./Real%20Series.md) $\displaystyle \sum_{n \in \mathcal{D}} a_n$ is [absolutely convergent](#Convergence) if and only if $\displaystyle \sum_{n \in \mathcal{D}} |a_n|$ is [bounded](./Real%20Functions/Boundedness%20of%20Real%20Functions.md).
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>
>>[!THEOREM] Theorem: Absolute Convergence $\implies$ Convergence
>>
>>If $\sum_{n \in \mathcal{D}} |a_n|$ [converges](#Convergence) to $L \in \mathbb{R}$, then $\sum_{n \in \mathcal{D}} a_n$ also [converges](#Convergence) to $L$.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

>[!DEFINITION] Definition: Conditional Convergence
>
>A [real series](./Real%20Series.md) is **conditionally convergent** iff it is [convergent](#Convergence) but not [absolutely convergent](#Convergence).
>

>[!EXAMPLE]- Example: The Alternating Harmonic Series
>
>The **alternating harmonic series** is the following [real series](./Real%20Series.md):
>
>$$\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots$$
>
>It [converges](#Convergence) towards the [natural logarithm](./Real%20Functions/Real%20Logarithms.md#The%20Real%20Natural%20Logarithm) of $2$:
>
>$$\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} = \ln 2$$
>
>However, it is *not*  [absolutely convergent](#Convergence) because $\sum_{n = 1}^{\infty} \left\vert \frac{(-1)^{n+1}}{n}\right\vert = \sum_{n = 1}^{\infty} \frac{1}{n}$. This is the [harmonic series](./Real%20Series.md) and we know that the [harmonic series](./Real%20Series.md) is [divergent](#Convergence). Therefore, $\sum_{n = 1}^{\infty} \frac{(-1)^{n+1}}{n}$ is [conditionally convergent](#Convergence).
>

>[!THEOREM] Theorem: Arithmetic with Real Series
>
>If $\sum_{n \in \mathcal{D}} a_n$ and $\sum_{n \in \mathcal{D}} b_n$ are [convergent](#Convergence) [real series](./Real%20Series.md), then
>
>$$
>\sum_{n \in \mathcal{D}} (\lambda a_n + \mu b_n) = \lambda \sum_{n \in \mathcal{D}} a_n + \mu \sum_{n \in \mathcal{D}} b_n
>$$
>
>for all $\lambda, \mu \in \mathbb{R}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] The Riemann Series Theorem
>
>Let $\sum_{n \in \mathcal{D}} a_n$ be an infinite [real series](./Real%20Series.md).
>
>>[!DEFINITION] Definition: Rearrangement
>>
>>A **rearrangement** of $\sum_{n \in \mathcal{D}} a_n$ is another infinite [real series](./Real%20Series.md) $\sum_{n \in \mathcal{D}} {}_{\sigma}a_n$ such that ${}_{\sigma} a_n$ can be expressed as
>>
>>$$
>>{}_{\sigma}a_{n} = a_{\sigma (n)}
>>$$
>>
>>for some [permutation](../../Combinatorics/Permutations.md) $\sigma$ of $\mathcal{D}$.
>>
>
>If $\sum_{n \in \mathcal{D}} a_n$ is [conditionally convergent](#Convergence), then for each $L \in \mathbb{R}$, there exists a rearrangement of $(a_n)_{n \in \mathcal{D}}$ which [converges](#Convergence) to $L$. There is also a rearrangement which [diverges](#Convergence) to $+\infty$, a rearrangement which [diverges](#Convergence) to $-\infty$ and a rearrangement which simply [diverges](#Convergence).
>
>>[!INTUITION]-
>>
>>The terms of every [conditionally convergent](#Convergence) [real series](./Real%20Series.md) can also be rearranged to produce a sum which is equal to any real number of our choice, or which diverges to infinity or negative infinite or just does not approach any limit, finite or infinite.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Convergent Series $\implies$ Zero Sequence
>
>If an [infinite](../Functional%20Analysis/Sequences/Sequences.md) [real series](./Real%20Series.md) $\sum_{n \in \mathcal{D}} a_n$ is [convergent](#Convergence), then $(a_n)_{n \in \mathcal{D}}$ is a [zero sequence](./Real%20Sequences.md#Convergence).
>
>>[!PROOF]-
>>
>>Since the [real series](./Real%20Series.md) is [convergent](#Convergence), the [Cauchy convergence theorem](#Convergence) tells us that for each $\varepsilon \gt 0$, there exists some $N_{\varepsilon} \in \mathcal{D}$ such that
>>
>>$$
>>\left\vert \sum_{k = m + 1}^n a_k \right\vert \lt \varepsilon
>>$$
>>
>>for all $n,m \in \mathcal{D}$ with $n,m \ge N_{\varepsilon}$ and $n \gt m$.
>>
>>If we set $m = n - 1$, we get
>>
>>$$
>>\left\vert \sum_{k = m + 1}^n a_k \right\vert = \left\vert \sum_{k = n}^n a_k \right \vert = |a_n| = |a_n - 0| \lt \varepsilon.
>>$$
>>
>>This holds for all $n \ge N_{\varepsilon}$, i.e. it is the definition of the [limit](./Real%20Sequences.md) of a [real sequence](./Real%20Sequences.md).
>>
>

>[!THEOREM] Theorem: Minorant Divergence Test
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n$ be a [real series](./Real%20Series.md).
>
>If there exists some [divergent](#Convergence) [real series](./Real%20Series.md) $\displaystyle \sum_{n \in \mathcal{D}} b_n$ and some integer $N$ such that $0 \le b_n \le a_n$ for all $n \ge N$, then $\displaystyle \sum_{n \in \mathcal{D}} a_n$ also [diverges](#Convergence).
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: The Series $\sum_{n = 1}^{\infty} \frac{1}{n^{\alpha}}$
>>
>>If $\alpha \le 1$, then the [real series](./Real%20Series.md) $\sum_{n = 1}^{\infty} \frac{1}{n^{\alpha}}$ [diverges](#Convergence), since
>>
>>$$\frac{1}{n} \le \frac{1}{n^{\alpha}} \qquad \forall n \in \mathbb{N}$$
>>
>>and the [harmonic series](./Real%20Series.md) $\sum_{n = 1}^{\infty} \frac{1}{n}$ [diverges](#Convergence).
>>
>

>[!THEOREM] Theorem: Cauchy Convergence Theorem
>
>A [real series](./Real%20Series.md) $\sum_{n \in \mathcal{D}} a_n$ is [convergent](#Convergence) if and only if for each $\varepsilon \gt 0$, there exists some $N_{\varepsilon} \in \mathcal{D}$ such that
>
>$$\left\vert \sum_{k = m + 1}^n a_k \right\vert \lt \varepsilon$$
>
>for all $m,n \in \mathcal{D}$ with $n \gt m$ and $m,n \ge N_{\varepsilon}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Majorant Convergence Test
>
>Let $\displaystyle \sum_{n \in \mathcal{D}} a_n$ be a [real series](./Real%20Series.md).
>
>If there exists some [convergent](#Convergence) [real series](./Real%20Series.md) $\displaystyle \sum_{n \in \mathcal{D}} b_n$ and some integer $N$ such that $|a_n| \le b_n$ for all $n \ge N$, then $\displaystyle \sum_{n \in \mathcal{D}} a_n$ is [absolutely convergent](#Convergence).
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: The Series $\sum_{n = 1}^{\infty} \frac{1}{n^{\alpha}}$
>>
>>If $\alpha \gt 1$, then the [real series](./Real%20Series.md) $\sum_{n = 1}^{\infty} \frac{1}{n^{\alpha}}$ is [convergent](#Convergence).
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Ratio Test
>
>Let $\sum_{n \in \mathcal{D}} a_n$ be an [infinite](../Functional%20Analysis/Sequences/Sequences.md) [real series](./Real%20Series.md).
>
>- (I) If there exists some $N \in \mathcal{D}$ and some $q \in (0;1)$ such that $\left\vert \frac{a_{n+1}}{a_n}\right\vert \le q$ for all $n \ge N$, then $\sum_{n \in \mathcal{D}} a_n$ is [absolutely convergent](#Convergence).
>
>- (II) If there exists some $N \in \mathcal{D}$ such that $\left\vert \frac{a_{n+1}}{a_n}\right\vert \ge 1$ for all $n \ge N$, then $\sum_{n \in \mathcal{D}} a_n$ is [divergent](#Convergence).
>
>>[!PROOF]-
>>
>>**Proof of (I):**
>>
>>Pick any $q \lt 1$ such that $\left\vert \frac{a_{n+1}}{a_n}\right\vert \le q$ for all $n \ge N$. We notice that
>>
>>$$
>>|a_{n+1}| \le q|a_n| \le q^2 |a_{n-1}| \le \cdots,
>>$$
>>
>>i.e. $|a_n| \le q^{n - N} |a_N|$ for all $n \ge N$. The [series](./Real%20Series.md) $\sum_{n = N}^{\infty} q^{n - N}|a_N|$ is the same as $\sum_{n = 0}^{\infty} q^n |a_N|$, which is [convergent](#Convergent) because $|a_N|$ is just a real number and the [geometric series](./Real%20Series.md) $\sum_{n = 0}^{\infty} q^n$ is [convergent](#Convergence) for $q \lt 1$. Therefore, the [majorant convergence test](#Convergence) tells us that $\sum_{n \in \mathcal{D}} |a_n|$ [converges](#Convergence), i.e. $\sum_{n \in \mathcal{D}} a_n$ is [absolutely convergent](#Convergence).
>>
>>**Proof of (II):**
>>
>>We show that $(a_n)$ is not a [zero sequence](./Real%20Sequences.md#Convergence) and so $\sum_{n \in \mathcal{D}}$ must [diverge](#Convergence).
>>
>>Suppose $(a_n)$ is a [zero sequence](./Real%20Sequences.md#Convergence):
>>
>>$$\lim_{n \to \infty} a_n = 0$$
>>
>>
>>
>
>>[!THEOREM] Theorem: Ratio Test via Limits 
>>
>>If $\left\vert\frac{a_{n+1}}{a_n}\right\vert$ is [convergent](./Real%20Sequences.md#Convergence), then the ratio test can be alternatively stated in the following way:
>>
>>- If $\lim_{n \in \mathcal{D}} \left\vert\frac{a_{n+1}}{a_n}\right\vert \lt 1$, then $\sum_{n \in \mathcal{D}} a_n$ is [absolutely convergent](#Convergence).
>>- If $\lim_{n \in \mathcal{D}} \left\vert\frac{a_{n+1}}{a_n}\right\vert \gt 1$, then $\sum_{n \in \mathcal{D}} a_n$ is [divergent](#Convergence).
>>- If $\lim_{n \in \mathcal{D}} \left\vert\frac{a_{n+1}}{a_n}\right\vert = 1$, then we can't use this [limit](./Real%20Sequences.md#Convergence) to make any statements about $\sum_{n \in \mathcal{D}} a_n$.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>>>[!EXAMPLE]- Example: The Series $\sum_{n = 0}^{\infty} \frac{1}{n!}$
>>>
>>>The [real series](./Real%20Series.md) $\sum_{n = 0}^{\infty} \frac{1}{n!}$ is [absolutely convergent](#Convergence), since
>>>
>>>$$\left\vert\frac{a_{n+1}}{a_n}\right\vert = \frac{n!}{(n+1)!} = \frac{1}{n+1}$$
>>>
>>>and
>>>
>>>$$\lim_{n \to \infty} \frac{1}{n+1} = 0 \lt 1.$$
>>>
>>
>>>[!EXAMPLE]- Example: The Series $\sum_{n=1}^{\infty} \frac{n^2}{3^n}$
>>>
>>>The [real series](./Real%20Series.md) $\sum_{n=1}^{\infty} \frac{n^2}{3^n}$ is [absolutely convergent](#Convergence), since
>>>
>>>$$\left\vert\frac{a_{n+1}}{a_n}\right\vert = \frac{(n+1)^2}{3^{n+1}}\frac{3^n}{n^2} = \frac{1}{3}\frac{n^2 + 2n + 1}{n^2}$$
>>>
>>>and 
>>>
>>>$$\lim_{n \to \infty} \frac{1}{3}\frac{n^2 + 2n + 1}{n^2} = \frac{1}{3} \lt 1.$$
>>>
>>
>

>[!THEOREM] Theorem: $n$-th Root Convergence Test
>
>Let $\sum_{n \in \mathcal{D}} a_n$ be a [real series](./Real%20Series.md).
>
>If the [real sequence](./Real%20Sequences.md) $\sqrt[n]{|a_n|}$ [converges](./Real%20Sequences.md#Convergence), then $\sum_{n \in \mathcal{D}} a_n$ is:
>- [absolutely convergent](#Convergence) if 
>
>$$\displaystyle \lim_{n \to \infty} \sqrt[n]{|a_n|} \lt 1$$
>
>- [divergent](#Convergence) if 
>
>$$\displaystyle \lim_{n \to \infty} \sqrt[n]{|a_n|} \gt 1$$
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
>>[!EXAMPLE]- Example: The Series $\sum_{n=3}^{\infty} \left(1 - \frac{2}{n}\right)^{n^2}$
>>
>>The [real sequence](./Real%20Sequences.md) $\sum_{n=3}^{\infty} \left(1 - \frac{2}{n}\right)^{n^2}$ is  [absolutely convergent](#Convergence), since
>>
>>$$\sqrt[n]{|a_n|} = \left(1 - \frac{2}{n}\right)^n$$
>>
>>and the [sequence](./Real%20Sequences.md)
>>
>>$$\left(1 - \frac{2}{n}\right)^n$$
>>
>>[converges](./Real%20Sequences.md#Convergence) to $\mathrm{e}^{-2}$.
>>
>

>[!THEOREM] Theorem: Leibniz Convergence Test for Alternating Series
>
>Let $\sum_{n \in \mathcal{D}} (-1)^n a_n$ be an [infinite real series](./Real%20Series.md).
>
>If $a_n \ge 0$ for all $n \in \mathcal{D}$ and $(a_n)_{n \in \mathcal{D}}$ is a [decreasing](./Real%20Functions/Monotonicity%20of%20Real%20Functions.md) [zero sequence](./Real%20Sequences.md), then $\sum_{n \in \mathcal{D}} (-1)^n a_n$ [converges](#Convergence).
>
>If $a_n \le 0$ for all $n \in \mathcal{D}$ and $(a_n)_{n \in \mathcal{D}}$ is an [increasing](./Real%20Functions/Monotonicity%20of%20Real%20Functions.md) [zero sequence](./Real%20Sequences.md), then $\sum_{n \in\mathcal{D}} (-1)^n a_n$ [converges](#Convergence).
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: The Series $\sum_{n = 1}^{\infty} \frac{(-1)^n}{n^{\alpha}}$
>>
>>Consider the [real series](./Real%20Series.md)
>>
>>$$\sum_{n = 1}^{\infty} \frac{(-1)^n}{n^{\alpha}},$$
>>
>>where $\alpha \in \mathbb{R}$.
>>
>>If $\alpha \gt 0$, then the [series](./Real%20Series.md) is [convergent](#Convergence) because $\frac{1}{n^{\alpha}}$ is a [decreasing](./Real%20Functions/Monotonicity%20of%20Real%20Functions.md) [sequence](./Real%20Sequences.md) which [converges](./Real%20Sequences.md#Convergence) to $0$.
>>
>

>[!THEOREM] Theorem: The Integral Test
>
>A [real series](./Real%20Series.md)
>
>$$\sum_{n = a}^{\infty} f(n),$$
>
>where $f: [a, +\infty) \subset \mathbb{R} \to \mathbb{R}$ is a non-negative [decreasing](./Real%20Functions/Monotonicity%20of%20Real%20Functions.md) [real function](./Real%20Functions/Real%20Functions.md), is [convergent](#Convergence) if and only if the [improper integral](./Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md#Improper%20Riemann%20Integrals)
>
>$$\int_a^{\infty} f(x) \,\mathrm{d}x$$
>
>is [convergent](./Real%20Functions/Limits%20(Real%20Functions.md).
>
>>[!EXAMPLE]- Example: $\sum_{n=2}^{\infty} \frac{1}{n \ln^{\alpha} n}$
>>
>>We want to see for what values of $\alpha$ the following [real series](./Real%20Series.md) [converges](#Convergence):
>>
>>$$\sum_{n=2}^{\infty} \frac{1}{n \ln^{\alpha} n}$$
>>
>>We examine the corresponding [improper integral](./Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md#Improper%20Riemann%20Integrals):
>>
>>$$\int_2^{\infty} \frac{1}{x \ln^{\alpha}x}\,\mathrm{d}x = \lim_{\beta \to \infty} \int_2^{\beta} \frac{1}{x \ln^{\alpha}x}\,\mathrm{d}x$$
>>
>>Using [integration by substitution](./Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md) with $u = \ln x$:
>>
>>$$\int_2^{\beta} \frac{1}{x \ln^{\alpha}x}\,\mathrm{d}x = \int_{\ln 2}^{\ln \beta} \frac{1}{u^{\alpha}} \,\mathrm{d}u$$
>>
>>We know that
>>
>>$$\lim_{\beta \to \infty} \int_2^{\beta} \frac{1}{u^{\alpha}}\,\mathrm{d}u = \int_2^{\infty} \frac{1}{u^{\alpha}}\,\mathrm{d}u$$
>>
>>[converges](./Real%20Functions/Limits%20(Real%20Functions.md) if and only if $\alpha \gt 1$ and so the original [improper integral](./Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md#Improper%20Riemann%20Integrals):
>>
>>$$\int_2^{\infty} \frac{1}{x \ln^{\alpha}x}\,\mathrm{d}x$$
>>
>>[converges](./Real%20Functions/Limits%20(Real%20Functions.md) if and only if $\alpha \gt 1$.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>
