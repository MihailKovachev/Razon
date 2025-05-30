---
title: Convergence of Real Sequences
tags:
    - convergence
    - real-sequences
    - real-analysis
    - mathematics
---

# Convergence and Real Limits

>[!DEFINITION] Definition: Convergence of Real Sequences
>
>Let $\{a_n\}$ be a [real sequence](Real%20Sequences.md).
>
>We say that $\{a_n\}$ **converges** to $L \in \mathbb{R}$ iff for each $\varepsilon \gt 0$, there exists some integer $N$ such that
>
>$$
>|a_n - L| \lt \varepsilon \qquad \forall n \ge N
>$$
>
>The number $L$, if it exists, is called the **limit** of $\{a_n\}$ as $n$ approaches infinity.
>
>>[!NOTATION]
>>
>>The most common notation is
>>
>>$$
>>\lim_{n \to \infty} a_n = L
>>$$
>>
>>In text, one also writes "$a_n \to L$ as $n \to \infty$" or just "$a_n \to L$". Sometimes, one might also encounter $a_n \underset{n \to \infty}{\longrightarrow} L$ and $a_n \overset{n \to \infty}{\longrightarrow} L$.
>>
>
>>[!THEOREM] Theorem: Uniqueness of the Limit
>>
>>The [limit](Convergence%20of%20Real%20Sequences.md) of a [real sequence](Real%20Sequences.md), if it exists, is unique - if $\{a_n\}$ [converges](Convergence%20of%20Real%20Sequences.md) to both $L$ and $M$, then $L = M$.
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

## Characterizations

>[!THEOREM]- Theorem: Approaching Zero
>
>A [real sequence](Real%20Sequences.md) $\{a_n\}$ [converges](Convergence%20of%20Real%20Sequences.md) to $L \in \mathbb{R}$ if and only if
>
>$$
>\lim_{n \to \infty} |a_n - L| = 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Cauchy Sequences
>
>A [real sequence](Real%20Sequences.md) $\{a_n\}$ is [convergent](Convergence%20of%20Real%20Sequences.md) if and only if, for each $\varepsilon \gt 0$, there exists some integer $N$ such that
>
>$$
>\lim_{n \to \infty} |a_n - a_m| = 0 \qquad \forall n,m \ge N 
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

## Properties

>[!THEOREM]- Theorem: Boundedness of Convergent Sequences
>
>Every [convergent](Convergence%20of%20Real%20Sequences.md) [real sequence](Real%20Sequences.md) is [bounded](../Real%20Functions/Bounds%20of%20Real%20Functions.md).
>
>>[!PROOF]-
>>
>>Suppose that $\{a_n\}$ [converges](Convergence%20of%20Real%20Sequences.md) to some $L \in \mathbb{R}$. Then, by definition, for each $\varepsilon \gt 0$, there exists some integer $N$ such that
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
>>Let $B = \max\{M, 1 + |L|\}$. Therefore, $|a_n| \le B$ for every integer $n$ and so $a_n$ is [bounded](../../Complex%20Analysis/Complex%20Sequences/Boundedness.md).
>>
>

>[!THEOREM]- Theorem: Convergence to Zero
>
>A [real sequence](Real%20Sequences.md) $\{a_n\}$ [converges](Convergence%20of%20Real%20Sequences.md) to zero if and only if $\{|a_n|\}$ converges to zero.
>
>$$
>\lim_{n \to \infty} a_n = 0 \iff \lim_{n \to \infty} |a_n| = 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- The Squeeze Theorem for Sequences
>
>Let $\{a_n\}$, $\{b_n\}$ and $\{c_n\}$ be [real sequences](Real%20Sequences.md) such that both $\{a_n\}$ and $\{b_n\}$ [converge](Convergence%20of%20Real%20Sequences.md) to $L \in \mathbb{R}$.
>
>If there exists an integer $N$ such that $a_n \le c_n \le b_n$ for all $n \ge N$, then $\{c_n\}$ also [converges](Convergence%20of%20Real%20Sequences.md) to $L$.
>
>$$
>\lim_{n\to\infty} c_n = \lim_{n\to\infty} a_n = \lim_{n\to\infty} b_n = L
>$$
>
>>[!PROOF]-
>>
>>Let $\varepsilon \gt 0$. Since $(a_n)_{n \in \mathbb{N}}$ and $(b_n)_{n \in \mathbb{N}}$ are convergent, there exist $N_a, N_b \in \mathbb{N}$ such that
>>
>>$$
>>|a_n - L| \lt \varepsilon \qquad \forall n \gt N_a
>>$$
>>
>>$$
>>|b_n - L| \lt \varepsilon \qquad \forall n \gt N_b
>>$$
>>
>>We also assumed that there is an integer $N$ such that
>>
>>$$
>>a_n \le c_n \le b_n \qquad \forall n \gt N
>>$$
>>
>>It follows then
>>
>>$$
>>L - \varepsilon \lt a_n \le c_n \le b_n \lt L + \varepsilon \qquad \forall n \ge \max \{N, N_a, N_b\}
>>$$
>>
>>From this we see that
>>
>>$$
>>L - \varepsilon \le c_n \le L + \varepsilon \qquad \forall n \ge \max \{N, N_a, N_b\}
>>$$
>>
>>This is the same as
>>
>>$$
>>|c_n - L| \lt \varepsilon \qquad n \ge \max \{N, N_a, N_b\}
>>$$
>>
>

>[!THEOREM]- Theorem: Limit Arithmetic
>
>If $\{a_n\}$ and $\{b_n\}$ are both [convergent](Convergence%20of%20Real%20Sequences.md) [real sequences](Real%20Sequences.md), then
>
>$$
>\begin{align*}
>
>&\lim_{n \to \infty} (\alpha a_n + \beta b_n) = \alpha \lim_{n \to \infty} a_n + \beta \lim_{n \to \infty} b_n \qquad \forall \alpha, \beta \in \mathbb{R} \\
>
>\\
>
>&\lim_{n \to \infty} (a_n \cdot b_n) = \lim_{n \to \infty} a_n \cdot \lim_{n \to \infty} b_n \\
>
>\\
>
>&\lim_{n \to \infty} \frac{a_n}{b_n} = \frac{\displaystyle \lim_{n \to \infty} a_n}{\displaystyle \lim_{n \to \infty} b_n}, \qquad \lim_{n \to \infty} b_n \ne 0 \\
>
>\\
>
>&\lim_{n \to \infty} |a_n| = \left|\lim_{n \to \infty} a_n\right|
>
>\end{align*}
>$$
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
>>\begin{align*}
>>
>>|a_n - A| \lt \varepsilon' \qquad \forall n \ge N_A \\
>>
>>|b_n - B| \lt \varepsilon' \qquad \forall n \ge N_B
>>
>>\end{align*}
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
>>\begin{align*}
>>
>>&|a_n - A| \lt \varepsilon' \qquad \forall n \ge N_A \\
>>
>>&|b_n - B| \lt \varepsilon' \qquad \forall n \ge N_B.
>>
>>\end{align*}
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
>

# Divergence and Infinite Limits

>[!DEFINITION] Definition: Divergence of Real Sequences
>
>A [real sequence](Real%20Sequences.md) is **divergent** iff it does not [converge](Convergence%20of%20Real%20Sequences.md) to any $\mathbb{R}$.
>

There are two special types of divergence in which we are often interested. 

>[!DEFINITION] Definition: Divergence towards Positive Infinity
>
>A [real sequence](Real%20Sequences.md) $\{a_n\}$ **diverges towards positive infinity** iff for each $A \in \mathbb{R}$ there is some integer $N$ such that
>
>$$
>a_n \gt A \qquad \forall n \ge N
>$$
>
>>[!NOTATION]
>>
>>$$
>>\lim_{n \to \infty} a_n = \infty
>>$$
>>
>

>[!DEFINITION] Definition: Divergence towards Negative Infinity
>
>A [real sequence](Real%20Sequences.md) $\{a_n\}$ **diverges towards negative infinity** iff for each $A \in \mathbb{R}$ there is some integer $N$ such that
>
>$$
>a_n \lt A \qquad \forall n \ge N
>$$
>
>>[!NOTATION]
>>
>>$$
>>\lim_{n \to \infty} a_n = -\infty
>>$$
>>
>

Even though we use limit notation for sequences that diverge towards positive or negative infinity, these sequences are *not* [convergent](Convergence%20of%20Real%20Sequences.md) and their limits do *not* exist. However, we often talk of "infinite limits" because of the notation we have chosen. Just remember that, strictly speaking, the "limits" of [divergent](Convergence%20of%20Real%20Sequences.md#Divergence%20and%20Infinite%20Limits) [real sequences](Real%20Sequences.md) *never* exist.

## Properties

>[!THEOREM]- Theorem: The Limit of $q^n$
>
>The [real sequence](Real%20Sequences.md) $q^n$:
>- [converges](Convergence%20of%20Real%20Sequences.md#Convergence%20and%20Real%20Limits) to $0$ if and only if $|q| \lt 1$;
>- [converges](Convergence%20of%20Real%20Sequences.md#Convergence%20and%20Real%20Limits) to $1$ if and only if $|q| = 1$;
>- [diverges](Convergence%20of%20Real%20Sequences.md#Divergence%20and%20Infinite%20Limits) if and only if $|q| \gt 1$;
>- [diverges](Convergence%20of%20Real%20Sequences.md#Divergence%20and%20Infinite%20Limits) towards $+ \infty$ if and only if $q \gt 1$.
>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: The Limit of $\frac{1}{n^k}$
>
>For every natural number $k \gt 0$, the [real sequence](Real%20Sequences.md) $\{ \frac{1}{n^k}\}$ [converges](Convergence%20of%20Real%20Sequences.md) to $0$.
>
>$$
>\lim_{n \to \infty} \frac{1}{n^k} = 0
>$$
>
>>[!PROOF]-
>>
>>*The following proof was generated by AI and may contain mistakes.* TODO: Review
>>
>>We want to prove that the sequence $a_n = \frac{1}{n^k}$ converges to $0$ for any fixed natural number $k > 0$.
>>By the definition of convergence, we need to show that for every $\epsilon > 0$, there exists a natural number $N$ such that for all $n > N$, we have $|a_n - 0| < \epsilon$.
>>
>>Let $\epsilon > 0$ be an arbitrary positive real number. We want to find an $N \in \mathbb{N}$ such that for all $n > N$,
>>
>>$$|\frac{1}{n^k} - 0| < \epsilon$$
>>
>>Since $n$ is a natural number, $n \ge 1$. Since $k$ is a natural number $k > 0$, we have $n^k \ge 1^k = 1$. Thus, $n^k$ is always positive.
>>Therefore, the absolute value simplifies to:
>>
>>$$|\frac{1}{n^k} - 0| = |\frac{1}{n^k}| = \frac{1}{n^k}$$
>>
>>So, we need to find $N \in \mathbb{N}$ such that for all $n > N$,
>>
>>$$\frac{1}{n^k} < \epsilon$$
>>
>>Since $\epsilon > 0$ and $n^k > 0$, we can rearrange the inequality:
>>Take the reciprocal of both sides (this reverses the inequality sign):
>>
>>$$n^k > \frac{1}{\epsilon}$$
>>
>>Since $k > 0$, we can take the $k$-th root of both sides. The function $x \mapsto x^{1/k}$ is strictly increasing for positive $x$.
>>
>>$$n > \left(\frac{1}{\epsilon}\right)^{1/k}$$
>>
>>We need to find a natural number $N$ such that for all $n > N$, the condition $n > (\frac{1}{\epsilon})^{1/k}$ holds.
>>By the Archimedean Property of the real numbers, for any positive real number, such as $(\frac{1}{\epsilon})^{1/k}$, there exists a natural number $N$ greater than it.
>>So, we can choose $N$ to be any natural number such that
>>
>>$$N > \left(\frac{1}{\epsilon}\right)^{1/k}$$
>>
>>For example, we can choose $N = \lfloor (\frac{1}{\epsilon})^{1/k} \rfloor + 1$.
>>
>>Now, let's verify this choice of $N$. Suppose $n$ is any natural number such that $n > N$. Since $N > (\frac{1}{\epsilon})^{1/k}$, we have $n > N > (\frac{1}{\epsilon})^{1/k}$. So, $n > (\frac{1}{\epsilon})^{1/k}$. Since $k > 0$, raising both sides to the power of $k$ (which is an increasing function for positive values) preserves the inequality:
>>
>>$$n^k > \left(\left(\frac{1}{\epsilon}\right)^{1/k}\right)^k$$
>>
>>$$n^k > \frac{1}{\epsilon}$$
>>
>>Since $n^k > 0$ and $\epsilon > 0$, we can take the reciprocal of both sides, which reverses the inequality:
>>
>>$$\frac{1}{n^k} < \epsilon$$
>>
>>Since we already established that $|\frac{1}{n^k} - 0| = \frac{1}{n^k}$, we have shown that for any $n > N$,
>>
>>$$|\frac{1}{n^k} - 0| < \epsilon$$
>>
>>Since we found such an $N$ for an arbitrary $\epsilon > 0$, by the definition of convergence, the sequence $\frac{1}{n^k}$ converges to $0$.
>>
>>This completes the proof.
>

>[!THEOREM]- Theorem: Reciprocal Limits
>
>Let $\{a_n\}$ be a [real sequence](Real%20Sequences.md).
>
>If $\{a_n\}$ [converges](Convergence%20of%20Real%20Sequences.md) to $0$ and there exists some integer $N$ such that $a_n \gt 0$ for all $n \ge N$, then $\{\frac{1}{a_n}\}$ [diverges](Convergence%20of%20Real%20Sequences.md#Divergence%20and%20Infinite%20Limits) towards $+\infty$.
>
>$$
>a_n \gt 0 \text{ and } \lim_{n \to \infty} a_n = 0 \implies \lim_{n \to \infty} \frac{1}{a_n} = +\infty
>$$
>
>If $\{a_n\}$ [converges](Convergence%20of%20Real%20Sequences.md) to $0$ and there exists some integer $N$ such that $a_n \lt 0$ for all $n \ge N$, then $\{\frac{1}{a_n}\}$ [diverges](Convergence%20of%20Real%20Sequences.md#Divergence%20and%20Infinite%20Limits) towards $-\infty$.
>
>$$
>a_n \lt 0 \text{ and } \lim_{n \to \infty} a_n = 0 \implies \lim_{n \to \infty} \frac{1}{a_n} = -\infty
>$$
>
>If $\{a_n\}$ [diverges](Convergence%20of%20Real%20Sequences.md#Divergence%20and%20Infinite%20Limits) towards either $+\infty$ or $-\infty$, then $\{\frac{1}{a_n}\}$ [converges](Convergence%20of%20Real%20Sequences.md) to $0$.
>
>$$
>\lim_{n \to \infty} a_n = \pm \infty \implies \lim_{n \to \infty} \frac{1}{a_n} = 0
>$$ 
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Arithmetic with Infinite Limits
>
>Let $\{a_n\}$ and $\{b_n\}$ be [real sequences](Real%20Sequences.md). 
>
>If $\{a_n\}$ [converges](Convergence%20of%20Real%20Sequences.md#Convergence%20and%20Real%20Limits) but $\{b_n\}$ [diverges](Convergence%20of%20Real%20Sequences.md#Divergence%20and%20Infinite%20Limits) towards $\pm \infty$, then $\{a_n + b_n\}$ also [diverges](Convergence%20of%20Real%20Sequences.md#Divergence%20and%20Infinite%20Limits) towards $\pm \infty$.
>
>$$
>\lim_{n \to \infty} a_n \in \mathbb{R} \text{ and } \lim_{n \to \infty} b_n = \pm \infty \implies \lim_{n\to \infty} (a_n + b_n) = \pm \infty
>$$
>
>If $\{a_n\}$ [converges](Convergence%20of%20Real%20Sequences.md#Convergence%20and%20Real%20Limits) towards $L \in \mathbb{R}$ but $\{b_n\}$ [diverges](Convergence%20of%20Real%20Sequences.md#Divergence%20and%20Infinite%20Limits) towards $\pm \infty$, then $\{a_n \cdot b_n\}$ also [diverges](Convergence%20of%20Real%20Sequences.md#Divergence%20and%20Infinite%20Limits) towards $\pm \infty$ when $L \gt 0$ and [diverges](Convergence%20of%20Real%20Sequences.md#Divergence%20and%20Infinite%20Limits) towards $\mp \infty$ when $L \lt 0$.
>
>$$
>\lim_{n \to \infty} a_n = L \in \mathbb{R} \text{ and } \lim_{n \to \infty} b_n = \pm \infty \implies \lim_{n\to \infty} (a_n \cdot b_n) = \begin{cases} \pm \infty \qquad \text{ if } L \gt 0 \\ \mp \infty \qquad \text{ if } L \lt 0\end{cases}
>$$
>
>If $\{a_n\}$ and $\{b_n\}$ both [diverge](Convergence%20of%20Real%20Sequences.md#Divergence%20and%20Infinite%20Limits) towards $\pm \infty$, then $\{a_n + b_n\}$ also [diverges](Convergence%20of%20Real%20Sequences.md#Divergence%20and%20Infinite%20Limits) towards $\pm \infty$ and $\{a_n \cdot b_n\}$ [diverges](Convergence%20of%20Real%20Sequences.md#Divergence%20and%20Infinite%20Limits) towards $+ \infty$.
>
>$$
>\lim_{n \to \infty} a_n = \lim_{n \to \infty} b_n = \pm \infty \implies \lim_{n \to \infty} (a_n + b_n) = \pm \infty \text{ and } \lim_{n \to \infty} (a_n \cdot b_n) = + \infty
>$$
>
>If $\{a_n\}$ [diverges](Convergence%20of%20Real%20Sequences.md#Divergence%20and%20Infinite%20Limits) towards $\pm \infty$ but $\{b_n\}$ [diverges](Convergence%20of%20Real%20Sequences.md#Divergence%20and%20Infinite%20Limits) towards $\mp \infty$, then $\{a_n \cdot b_n\}$ [diverges](Convergence%20of%20Real%20Sequences.md#Divergence%20and%20Infinite%20Limits) towards $- \infty$. However, this information is insufficient to determine $\lim_{n\to \infty} (a_n + b_n)$.
>
>$$
>\lim_{n \to \infty} a_n = \pm \infty \text{ and } \lim_{n \to \infty} b_n = \mp \infty \implies \lim_{n \to \infty} (a_n \cdot b_n) = -\infty
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: The Limit of $\left(1 + \frac{1}{n}\right)^n$ and its Variations
>
>The [real sequence](Real%20Sequences.md) $a_n = \left(1 + \frac{1}{n}\right)^n$ [converges](Convergence%20of%20Real%20Sequences.md#Convergence%20and%20Real%20Limits) towards [Euler's number](../Real%20Functions/The%20Real%20Exponential%20Function.md) $\mathrm{e}$.
>
>$$
>\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = \mathrm{e}
>$$
>
>Similarly, the [limits](Convergence%20of%20Real%20Sequences.md#Convergence%20and%20Real%20Limits) of the following [real sequences](Real%20Sequences.md) can also be expressed using the [real exponential function](../Real%20Functions/The%20Real%20Exponential%20Function.md):
>
>$$
>\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^{n + r} = \mathrm{e} \qquad \forall r \in \mathbb{R}
>$$
>
>$$
>\lim_{n \to \infty} \left(1 + \frac{r}{n}\right)^n = \mathrm{e}^r \qquad \forall r \in \mathbb{R}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>