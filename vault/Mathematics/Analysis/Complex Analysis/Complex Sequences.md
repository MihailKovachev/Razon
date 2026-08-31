---
title: Complex Sequences
tags:
  - complex-sequences
  - complex-analysis
  - mathematics
---

# Complex Sequences

>[!DEFINITION] Definition: Complex Sequence
>
>A **complex sequence** is a [sequence](../Functional%20Analysis/Sequences/Sequences.md) of [complex numbers](../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md).
>

>[!THEOREM] Theorem: Equality of Complex Sequences
>
>Let $(a_n)_{n \in \mathcal{D}}$ and $(b_n)_{n \in \mathcal{D}}$ be [infinite](../Functional%20Analysis/Sequences/Sequences.md) [complex sequences](./Complex%20Sequences.md).
>
>If there exist [complex power series](./Complex%20Power%20Series.md) $\sum_{n \in \mathcal{D}} a_n (x - c)^n$ and $\sum_{n \in \mathcal{D}} b_n (x - c)^n$ which have the same center $c \in \mathbb{C}$ and for which there is some $r \gt 0$ such that both series [converge](./Complex%20Power%20Series.md#Convergence) to the same number, i.e.
>
>$$
>\sum_{n \in \mathcal{D}} a_n (x - c)^n = \sum_{n \in \mathcal{D}} b_n (x - c)^n,
>$$
>
>when when $|x - c| \lt r$, then $a_n = b_n$ for all $n \in \mathcal{D}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Convergence

>[!DEFINITION] Definition: Convergence
>
>
>A [complex sequence](./Complex%20Sequences.md) $(z_n)_{n \in \mathcal{D}}$ [converges](../Functional%20Analysis/Sequences/Convergence%20(Sequences.md) to the [limit](../Functional%20Analysis/Sequences/Convergence%20(Sequences.md) $L \in \mathbb{C}$ if and only if for each $\varepsilon \gt 0$, there exists some $N \in \mathcal{D}$ such that
>
>$$
>|z_n - L| \lt \varepsilon \qquad \forall n \ge N.
>$$
>
>>[!NOTATION]
>>
>>The most common notation is
>>
>>$$
>>\lim_{n \to \infty} z_n = L
>>$$
>>
>>In text, one also writes "$z_n \to L$ as $n \to \infty$" or just "$z_n \to L$". Sometimes, one might also encounter $z_n \underset{n \to \infty}{\longrightarrow} L$ and $z_n \overset{n \to \infty}{\longrightarrow} L$.
>>
>
>>[!THEOREM] Theorem: Uniqueness of the Limit
>>
>>The [limit](#Convergence) of a [convergent](#Convergence) [complex sequence](./Complex%20Sequences.md) is unique - if $\{z_n\}$ [converges](#Convergence) to both $L$ and $M$, then $L = M$.
>>
>>>[!PROOF]-
>>>
>>>Pick some arbitrary $\varepsilon \gt 0$.
>>>
>>>Since $\{a_n\} \to L$, by definition, there exists some integer $N_L$ such that
>>>
>>>$$
>>>|a_n - L| \lt \varepsilon \qquad \forall n \ge N_L.
>>>$$
>>>
>>>Similarly, since $\{a_n\} \to M$, there exists some integer $N_M$ such that
>>>
>>>$$
>>>|a_n - M| \lt \varepsilon \qquad \forall n \ge N_M.
>>>$$
>>>
>>>Now, let $N = \max\{N_L, N_M\}$. For all $n \ge N$, both of the aforementioned inequalities hold. Therefore, for all $n \ge N$, we have
>>>
>>>$$
>>>|L - M| = |L - a_n + a_n - M| \le |L - a_n| + |a_n - M| \lt \varepsilon + \varepsilon = 2\varepsilon.
>>>$$
>>>
>>>Therefore,
>>>
>>>$$
>>>\frac{1}{2}|L - M| \lt \varepsilon
>>>$$
>>>
>>>So far, the argument does not actually depend on the particular choice of $\varepsilon$ and is thus true for every $\varepsilon \gt 0$. This means that $\frac{1}{2}|L - M|$ is smaller that every positive real number. This is only possible if $\frac{1}{2}|L - M|$ is zero which is in turn only possible if $|L - M| = 0$. Therefore, $L = M$.
>>>
>>
>

>[!THEOREM] Theorem: Complex Convergence via Real Convergence
>
>A [complex sequence](./Complex%20Sequences.md) $(z_n)_{n \in \mathcal{D}}$ [converges](#Convergence) to $L \in \mathbb{C}$ the [sequence](../Real%20Analysis/Real%20Sequences.md) $|z_n - L|$ [converges](../Real%20Analysis/Real%20Sequences.md#Convergence) to $0$:
>
>$$
>\lim_{n \to \infty} z_n = L \iff \lim_{n \to \infty} |z_n - L| = 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: $z_n = \frac{1}{2n} + \frac{n}{n+1}\mathrm{i}$
>>
>>We examine the following [complex sequence](./Complex%20Sequences.md) $(z_n)_{n \in \mathbb{N}}$:
>>
>>$$
>>z_n = \frac{1}{2n} + \frac{n}{n+1}\mathrm{i}
>>$$
>>
>>Since $\frac{1}{2n} \to 0$ and $\frac{n}{n+1} \to 1$, we see that $(z_n)$ probably [converges](#Convergence) to $\mathrm{i}$. To show this, we examine $z_n - \mathrm{i}$:
>>
>>$$
>>z_n - \mathrm{i} = \frac{1}{2n} + \left(\frac{n}{n+1} -1\right)\mathrm{i} = \frac{1}{2n} + \frac{-1}{n+1}\mathrm{i}
>>$$
>>
>>We now examine the [limit](#Convergence) of the [absolute values](../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md):
>>
>>$$
>>\lim_{n\to\infty} |z_n - \mathrm{i}| = \sqrt{\frac{1}{4n^2}+\frac{1}{(n+1)}} = 0
>>$$
>>
>>Therefore, $(z_n)$ [converges](#Convergence) to $\mathrm{i}$.
>>
>

>[!THEOREM] Theorem: Component-Wise Convergence
>
>A [complex sequence](./Complex%20Sequences.md) $(z_n)_{n \in \mathcal{D}}$ [converges](#Convergence) to $L \in \mathbb{C}$ if and only if the [sequences](../Real%20Analysis/Real%20Sequences.md) of its [real part](../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md) and its [imaginary part](../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md) [converge](../Real%20Analysis/Real%20Sequences.md#Convergence) to the [real part](../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md) and [imaginary part](../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md) of $L$, respectively.
>
>$$
>\lim_{n \to \infty} z_n = L \iff \lim_{n \to \infty} \operatorname{Re}(z_n) = \operatorname{Re}(L) \qquad \text{and} \qquad \lim_{n \to \infty} \operatorname{Im}(z_n) = \operatorname{Im}(L)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: $z_n = \left(1 - \frac{3}{n}\right)^n + \mathrm{i}\frac{2n^2+3n+5}{n^2+1}$
>>
>>We examine the following [complex sequence](./Complex%20Sequences.md) $(z_n)_{n\in\mathbb{N}}$:
>>
>>$$
>>z_n = \left(1 - \frac{3}{n}\right)^n + \mathrm{i}\frac{2n^2+3n+5}{n^2+1}
>>$$
>>
>>Since $\lim_{n\to\infty} \left(1 - \frac{3}{n}\right)^n = \mathrm{e}^{-3}$ and $\lim_{n\to\infty} \frac{2n^2+3n+5}{n^2+1} = 2$, we know that $(z_n)_{n\to\mathcal{N}}$ [converges](#Convergence) to $\mathrm{e}^{-3} + 2\mathrm{i}$:
>>
>>$$
>>\lim_{n \to \infty} = \left(1 - \frac{3}{n}\right)^n + \mathrm{i}\frac{2n^2+3n+5}{n^2+1} = \mathrm{e}^{-3}+2\mathrm{i}
>>$$
>>
>
>>[!EXAMPLE]- Example: $z_n = \frac{5}{n} + (-1)^n\mathrm{i}$
>>
>>We examine the following [complex sequence](./Complex%20Sequences.md) $(z_n)_{n\in\mathbb{N}}$:
>>
>>$$
>>z_n = \frac{5}{n} +(-1)^n \mathrm{i}
>>$$
>>
>>Since $\Im(z_n) = (-1)^n$ [diverges](../Real%20Analysis/Real%20Sequences.md#Convergence), we know that $(z_n)_{n \to\mathbb{N}}$ must also [diverge](#Convergence).
>>
>

>[!THEOREM] Theorem: Cauchy Sequences
>
>A [complex sequence](./Complex%20Sequences.md) $(z_n)_{n \in \mathcal{D}}$ is [convergent](#Convergence) if and only if for each $\varepsilon \gt 0$ there exists some $N \in \mathcal{D}$ such that
>
>$$
>\lim_{n \to \infty} |z_n - z_m| = 0 \qquad \forall n,m \ge N 
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!NOTE]
>>
>>Sequences for which the above holds, i.e. convergent sequences, are also known as **Cauchy sequences**.
>>
>

>[!THEOREM] Theorem: Boundedness of Convergent Sequences
>
>Every [convergent](#Convergence) [complex sequence](./Complex%20Sequences.md) is [bounded](./Boundedness%20of%20Complex%20Functions.md).
>
>>[!PROOF]-
>>
>>Suppose that $\{a_n\}$ [converges](#Convergence) to some $L \in \mathbb{C}$. Then, by definition, for each $\varepsilon \gt 0$, there exists some integer $N$ such that
>>
>>$$
>>|a_n - L| \lt \varepsilon \qquad \forall n \ge N.
>>$$
>>
>>Choose $\varepsilon = 1$. The actual choice is irrelevant, it will just result in a different bound. Then,
>>
>>$$
>>|a_n - L| \lt 1 \qquad \forall n \ge N.
>>$$
>>
>>Let's look at the absolute value of $a_n$:
>>
>>$$
>>|a_n| = |a_n - L + L|
>>$$
>>
>>Using the triangle inequality, we get
>>
>>$$
>>|a_n| = |a_n - L + L| \le |a_n - L| + |L|.
>>$$
>>
>>For all $n \ge N$,
>>
>>$$
>>|a_n - L| + |L| \lt 1 + |L|
>>$$
>>
>>and so $|a_n| \lt 1 + |L|$ for all $n \ge N$. This means that the modulus of all sequence terms from the $N$-th one onwards is less than $1 + |L|$. Amongst the first $N-1$ terms of the sequence, choose the one whose modulus $M$ is greatest. The moduli of the first $N-1$ terms are thus all less than or equal to $M$. Essentially, we have
>>
>>- $|a_n| \le M$ for every $n \lt N$;
>>- $|a_n| \lt 1 + |L|$ for every $n \ge N$.
>>
>>Let $B = \max\{M, 1 + |L|\}$. Therefore, $|a_n| \le B$ for every integer $n$ and so $a_n$ is [bounded](./Boundedness%20of%20Complex%20Functions.md).
>>
>

>[!THEOREM] Theorem: Convergence to Zero
>
>A [complex sequence](./Complex%20Sequences.md) $(z_n)_{n \in \mathcal{D}}$ [converges](#Convergence) to $0$ if and only if the [real sequence](../Real%20Analysis/Real%20Sequences.md) $(|z_n|)_{n \in \mathcal{D}}$ of its [absolute values](../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md) [converges](../Real%20Analysis/Real%20Sequences.md#Convergence) to $0$.
>
>$$
>\lim_{n \to \infty} z_n = 0 \iff \lim_{n \to \infty} |z_n| = 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem
>
>Let $\{a_n\}$ and $\{b_n\}$ be [complex sequences](./Complex%20Sequences.md).
>
>If $\{a_n\}$ [converges](#Convergence) to zero and there exists some integer $N$ such that $|b_n| \le |a_n|$ for all $n \ge N$, then $\{b_n\}$ also [converges](#Convergence) to zero.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Limit Arithmetic
>
>If $(a_n)_{n\in\mathcal{D}}$ and $(b_n)_{n\in\mathcal{D}}$ are both [convergent](#Convergence) [complex sequences](./Complex%20Sequences.md), then
>
>$$\begin{aligned}& \lim_{n \to \infty} (\alpha a_n + \beta b_n) = \alpha \lim_{n \to \infty} a_n + \beta \lim_{n \to \infty} b_n \qquad \forall \alpha, \beta \in \mathbb{C} \\ & \lim_{n \to \infty} (a_n \cdot b_n) = \lim_{n \to \infty} a_n \cdot \lim_{n \to \infty} b_n \\ & \lim_{n \to \infty} \frac{a_n}{b_n} = \frac{\displaystyle \lim_{n \to \infty} a_n}{\displaystyle \lim_{n \to \infty} b_n}, \qquad \lim_{n \to \infty} b_n \ne 0 \\ & \lim_{n \to \infty} \overline{a_n} = \overline{\lim_{n \to \infty} a_n} \\ & \lim_{n \to \infty} |a_n| = \left|\lim_{n \to \infty} a_n\right|\end{aligned}$$
>
>>[!PROOF]-
>>
>>Let $A = \displaystyle \lim_{n \to \infty} a_n$ and $B = \displaystyle \lim_{n \to \infty} b_n$.
>>
>>**Proof of (1):**
>>
>>We have to prove that for each $\varepsilon \gt 0$, there exists some integer $N$ such that
>>
>>$$
>>|\alpha a_n + \beta b_n - (\alpha A + \beta B)| \lt \varepsilon \qquad \forall n \ge N.
>>$$
>>
>>The case of $\alpha = \beta = 0$ is trivial, since then $|\alpha a_n + \beta b_n - (\alpha A + \beta B)|$ is always zero and is thus smaller than all $\varepsilon \gt 0$. As for the existence of $N$ - not only does such an integer $N$ exist, but there are actually infinitely many such integers, since the inequality holds irrespective of $N$.
>>
>>If $\alpha$ and $\beta$ are not zero, choose some arbitrary $\varepsilon' \gt 0$. Since $a_n \to A$ and $b_n \to B$, there exist integers $N_A$ and $N_B$ such that
>>
>>$$
>>\begin{aligned}
>>
>>|a_n - A| \lt \varepsilon' \qquad \forall n \ge N_A \\
>>
>>|b_n - B| \lt \varepsilon' \qquad \forall n \ge N_B
>>
>>\end{aligned}
>>$$
>>
>>Let $N = \max \{N_A, N_B\}$. Then both inequalities hold for every $n \ge N$. Now, we look at
>>
>>$$
>>|\alpha a_n + \beta b_n - (\alpha A + \beta B)| = |\alpha (a_n - A) + \beta (b_n - B)|.
>>$$
>>
>>By the triangle inequality, we obtain
>>
>>$$
>>|\alpha (a_n - A) + \beta (b_n - B)| \le |\alpha (a_n - A)| + |\beta (b_n - B)| = |\alpha| |a_n - A| + |\beta| |b_n - B|.
>>$$
>>
>>For every $n \ge N$, we know that $|a_n - A| \lt \varepsilon'$ and $|b_n - B| \lt \varepsilon'$ and so we get
>>
>>$$
>>|\alpha| |a_n - A| + |\beta| |b_n - B| \lt |\alpha| \varepsilon' + |\beta| \varepsilon'.
>>$$
>>
>>Since $|\alpha (a_n - A) + \beta (b_n - B)| \le |\alpha| |a_n - A| + |\beta| |b_n - B|$ and $|\alpha a_n + \beta b_n - (\alpha A + \beta B)| = |\alpha (a_n - A) + \beta (b_n - B)|$, we get
>>
>>$$
>>|\alpha a_n + \beta b_n - (\alpha A + \beta B)| \lt |\alpha| \varepsilon' + |\beta| \varepsilon' \qquad \forall n \ge N
>>$$
>>
>>So far, the argument does not depend on the choice of $\varepsilon'$ which means that it must be true for all $\varepsilon' \gt 0$. Thus, we have proven that for each $\varepsilon = |\alpha| \varepsilon' + |\beta| \varepsilon'$, there exists some integer, namely $N$, such that
>>
>>$$
>>|\alpha a_n + \beta b_n - (\alpha A + \beta B)| \lt \varepsilon \qquad \forall n \ge N,
>>$$
>>
>>which is what we set out to prove.
>>
>>**Proof of (2):**
>>
>>We have to prove that for each $\varepsilon \gt 0$, there exists some integer $N$ such that
>>
>>$$
>>|a_n \cdot b_n - A \cdot B| \lt \varepsilon \qquad \forall n \ge N.
>>$$
>>
>>Choose some arbitrary $\varepsilon' \gt 0$. Since $a_n \to A$ and $b_n \to B$, there exist integers $N_A$ and $N_B$ such that
>>
>>$$
>>\begin{aligned}
>>
>>&|a_n - A| \lt \varepsilon' \qquad \forall n \ge N_A \\
>>
>>&|b_n - B| \lt \varepsilon' \qquad \forall n \ge N_B.
>>
>>\end{aligned}
>>$$
>>
>>Let $N = \max \{N_A, N_B\}$. Then both inequalities hold for all $n \ge N$. We transform the expression $|a_n \cdot b_n - A \cdot B|$ a bit:
>>
>>$$
>>|a_n \cdot b_n - A \cdot B| = |a_n \cdot b_n - A \cdot b_n + A \cdot b_n - A \cdot B|.
>>$$
>>
>>Using the triangle inequality, we obtain
>>
>>$$
>>|a_n \cdot b_n - A \cdot b_n + A \cdot b_n - A \cdot B| \le |a_n \cdot b_n - A \cdot b_n| + |A \cdot b_n - A \cdot B|,
>>$$
>>
>>which is equivalent to
>>
>>$$
>>|a_n \cdot b_n - A \cdot B| \le |b_n| \cdot |a_n - A| + |A| \cdot |b_n - B|.
>>$$
>>
>>For all $n \ge N$,
>>
>>$$
>>|b_n| \cdot |a_n - A| + |A| \cdot |b_n - B| \lt |b_n| \cdot \varepsilon' + |A| \cdot \varepsilon',
>>$$
>>
>>which in turn means that, for all $n \ge N$,
>>
>>$$
>>|a_n \cdot b_n - A \cdot B| \lt |b_n| \cdot \varepsilon' + |A| \cdot \varepsilon'
>>$$
>>
>>Recall that every convergent sequence is bounded. This means that there exists some $B \gt 0$ and some integer $\mathcal{N}$ such that $|b_n| \le B$ for all $n \ge \mathcal{N}$. Therefore,
>>
>>$$
>>|a_n \cdot b_n - A \cdot B| \lt B \cdot \varepsilon' + |A| \cdot \varepsilon' \qquad \forall n \ge \mathcal{N}.
>>$$
>>
>>Set $\varepsilon = B \cdot \varepsilon' + |A| \cdot \varepsilon'$. Therefore,
>>
>>$$
>>|a_n \cdot b_n - A \cdot B| \lt \varepsilon \qquad \forall n \ge \mathcal{N}.
>>$$
>>
>>It is obvious that $\varepsilon$ can be any positive real number. Moreover, since the argument so far does not depend on any particular choice of $\varepsilon$, we know the argument holds for all $\varepsilon \gt 0$. We have thus proven that for each $\varepsilon \gt 0$, there exists some integer, namely $\mathcal{N}$, such that
>>
>>$$
>>|a_n \cdot b_n - A \cdot B| \lt \varepsilon \qquad \forall n \ge \mathcal{N},
>>$$
>>
>>which is what we set out to show.
>>
>>**Proof of (3):**
>>
>>TODO
>>
>>**Proof of (4):**
>>
>>TODO
>>
>>**Proof of (5):**
>>
>>TODO
>>
>