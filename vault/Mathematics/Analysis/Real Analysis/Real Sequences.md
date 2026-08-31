---
tags:
    - real-analysis
    - analysis
    - mathematics
---

# Real Sequences

>[!DEFINITION] Definition: Real Sequence
>
>A **real sequence** is a [sequence](../Functional%20Analysis/Sequences/Sequences.md) of [real numbers](../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md).
>

## Convergence

>[!DEFINITION] Definition: Convergence of Real Sequences
>
>Let $(a_n)_{n \in \mathcal{D}}$ be a [real sequence](#Real%20Sequence) and let $L \in \mathbb{R}$.
>
>We say that $L$ is the **limit** of $(a_n)_{n \in \mathcal{D}}$ if for each $\varepsilon \gt 0$ there exists some $N \in \mathcal{D}$ such that
>
>$$
>|a_n - L| \lt \varepsilon \qquad \forall n \ge N.
>$$
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

>[!DEFINITION] Definition: Convergence
>
>A [real sequence](./Real%20Sequences.md) is **convergent** if there exists some $L \in \mathbb{R}$ which is its [limit](#Convergence):
>
>$$
>\exists L \in \mathbb{R}: \lim_{n \to \infty} a_n = L
>$$
>
>>[!THEOREM] Theorem: Uniqueness of the Limit
>>
>>If a [real sequence](./Real%20Sequences.md) is [convergent](#Convergence), then it has exactly one [limit](#Convergence).
>>
>>>[!PROOF]-
>>>
>>>We need to prove that if $\lim_{n \to \infty} a_n = L$ and $\lim_{n \to \infty} a_n = M$, then $L = M$.
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
>>>
>>
>

>[!DEFINITION] Definition: Zero Sequence
>
>A **zero sequence** is a [real sequence](./Real%20Sequences.md) whose [limit](#Convergence) is zero.
>

>[!DEFINITION] Definition: Divergence of Real Sequences
>
>A [real sequence](#Real%20Sequences) is **divergent** if it is not [convergent](#Convergence).
>
>>[!DEFINITION] Definition: Divergence towards Positive Infinity
>>
>>A [real sequence](#Real%20Sequences) $(a_n)_{\mathcal{D}}$ **diverges towards positive infinity** if for each $A \in \mathbb{R}$ there is some $N \in \mathcal{D}$ such that
>>
>>$$
>>a_n \gt A \qquad \forall n \ge N
>>$$
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\lim_{n \to \infty} a_n = \infty
>>>$$
>>>
>>
>
>>[!DEFINITION] Definition: Divergence towards Negative Infinity
>>
>>A [real sequence](#Real%20Sequences) $(a_n)_{n \in \mathcal{D}}$ **diverges towards negative infinity** if for each $A \in \mathbb{R}$ there is some integer $N \in \mathcal{D}$ such that
>>
>>$$
>>a_n \lt A \qquad \forall n \ge N
>>$$
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\lim_{n \to \infty} a_n = -\infty
>>>$$
>>>
>>
>
>>[!NOTE]
>>
>>Even though we use limit notation for sequences that diverge towards positive or negative infinity, these sequences are *not* [convergent](#Convergence) and their [limits](#Convergence) do *not* exist. However, we often talk of "infinite limits" because of the notation we have chosen. Just remember that, strictly speaking, the "limits" of [divergent](#Convergence) [real sequences](#Real%20Sequences) *never* exist.
>>
>

>[!THEOREM] Theorem: Approaching Zero
>
>A [real sequence](#Real%20Sequences) $\{a_n\}$ [converges](#Convergence) to $L \in \mathbb{R}$ if and only if
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

>[!THEOREM] Theorem: Cauchy Criterion
>
>A [real sequence](#Real%20Sequences) $\{a_n\}$ is [convergent](#Convergence) if and only if, for each $\varepsilon \gt 0$, there exists some integer $N$ such that
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

>[!THEOREM] Theorem: Boundedness of Convergent Sequences
>
>Every [convergent](#Convergence) [real sequence](#Real%20Sequences) is [bounded](./Real%20Functions/Boundedness%20of%20Real%20Functions.md).
>
>>[!PROOF]-
>>
>>Suppose that $\{a_n\}$ [converges](#Convergence) to some $L \in \mathbb{R}$. Then, by definition, for each $\varepsilon \gt 0$, there exists some integer $N$ such that
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
>>Let $B = \max\{M, 1 + |L|\}$. Therefore, $|a_n| \le B$ for every integer $n$ and so $a_n$ is [bounded](./Real%20Functions/Boundedness%20of%20Real%20Functions.md).
>>
>

>[!THEOREM] Theorem: Limit Inequality
>
>Let $(a_n)_{n \in \mathcal{D}_a}$ and $(b_n)_{n \in \mathcal{D}_b}$ be [convergent](#Convergence) [real sequences](#Real%20Sequences). 
>
>If there exists some $N \in \mathcal{D}_a \cap \mathcal{D}_b$ such that $a_n \le b_n$ for all $n \gt N$, then
>
>$$
>\lim_{n \to \infty} a_n \le \lim_{n \to \infty} b_n
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Convergence to Zero
>
>A [real sequence](#Real%20Sequences) $(a_n)$ [converges](#Convergence) to zero if and only if $(|a_n|)$ converges to zero.
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

>[!THEOREM] The Squeeze Theorem for Sequences
>
>Let $\{a_n\}$, $\{b_n\}$ and $\{c_n\}$ be [real sequences](#Real%20Sequences) such that both $\{a_n\}$ and $\{b_n\}$ [converge](#Convergence) to $L \in \mathbb{R}$.
>
>If there exists an integer $N$ such that $a_n \le c_n \le b_n$ for all $n \ge N$, then $\{c_n\}$ also [converges](#Convergence) to $L$.
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
>>[!EXAMPLE]- Example: Limit of $\frac{n}{2^n}$
>>
>>We look at the following [sequence](./Real%20Sequences.md):
>>
>>$$
>>c_n = \frac{n}{2^n}
>>$$
>>
>>Using [induction](../../Logic/Mathematical%20Induction.md), it is fairly easy to prove that $2^n \ge n^2$ for all $n \ge 4$. We thus have the following:
>>
>>$$
>>\frac{1}{2^n} \le \frac{1}{n^2}
>>$$
>>
>>Multiply both sides by $n$:
>>
>>$$
>>\frac{n}{2^n} \le \frac{1}{n}
>>$$
>>
>>If we choose $a_n = 0$ to be the constant [real sequence](./Real%20Sequences.md) which always gives zero and we choose $b_n = \frac{1}{n}$, then we see that
>>
>>$$
>>\lim_{n \to \infty}{2^n} = 0,
>>$$
>>
>>since $\lim_{n\to \infty} a_n = 0$, $\lim_{n \to \infty} b_n = 0$ and $a_n \le c_n \le b_n$ for all $n \ge 4$.
>>
>>This can be extended to show that
>>
>>$$
>>\lim_{n \to \infty} \frac{n^r}{q^n} = 0 \qquad \text{where } r \in \mathbb{N}, q \gt 1
>>$$
>>
>
>>[!EXAMPLE]- Example: Limit of $\sqrt[n]{n}$
>>
>>We examine the following [real sequence](./Real%20Sequences.md):
>>
>>$$
>>a_n = \sqrt[n]{}
>>$$
>>
>>By looking at a few terms, we may guess that $(a_n)$ [converges](#Convergence) to $1$:
>>
>>$$
>>a_1 = 1 \qquad a_2 \approx 1.41 \qquad a_{10} \approx 1.25 \qquad a_{100} \approx 1.047 \qquad a_{1000} \approx 1.0069
>>$$
>>
>>To prove this, we examine the [real sequence](./Real%20Sequences.md) $b_n = \sqrt[n]{n} - 1$. We immediately see that
>>
>>$$
>>1 + b_n = \sqrt[n]{n}
>>$$
>>
>>and so
>>
>>$$
>>n = (1+b_n)^n.
>>$$
>>
>>Using the [binomial theorem](../../Algebra/Fields/The%20Complex%20Numbers/The%20Binomial%20Theorem.md), we get that
>>
>>$$
>>n = 1 + nb_n + \frac{n(n-1)}{2}b_n^2 + \cdots + b_n^n.
>>$$
>>
>>Therefore,
>>
>>$$
>>\begin{aligned}
>>n &\ge 1 + \frac{n(n-1)}{2}b_n^2 \qquad \forall n \ge 2 \\
>>n - 1 &\ge \frac{n(n-1)}{2}b_n^2 \qquad \forall n \ge 2 \\
>>1 &\ge \frac{n}{2} b_n^2 \qquad \forall n \ge 2 \\
>>b_n^2 &\le \frac{2}{n} \qquad \forall n \ge 2
>>\end{aligned}
>>$$
>>
>>We have
>>
>>$$
>>0 \le b_n^2 \le \frac{2}{n} \qquad \forall n \ge 2
>>$$
>>
>>and we can take the square root:
>>
>>$$
>>\sqrt{0} \le b_n \le \sqrt{\frac{2}{n}}
>>$$
>>
>>Now, we recall the definition of $b_n$ as $b_n = a_n - 1$:
>>
>>$$
>>\begin{aligned}
>>0 &\le a_n - 1 \le \sqrt{\frac{2}{n}} \\
>>1 &\le a_n \le \sqrt{\frac{2}{n}} = 1
>>\end{aligned}
>>$$
>>
>>We have $\lim_{n \to \infty} 1 = 1$ and 
>>
>>$$
>>\begin{aligned}
>>\lim_{n \to \infty} \left(\sqrt{\frac{2}{n}} + 1\right) &= \lim_{n \to \infty} \sqrt{\frac{2}{n}} + \lim_{n \to \infty} 1 \\ &= \sqrt{\lim_{n \to \infty} \frac{2}{n}} + 1 \\ &= \sqrt{0} + 1 = 0 + 1 = 1.
>>\end{aligned}
>>$$
>>
>>Therefore:
>>
>>$$
>>\lim_{n \to \infty} a_n = 1
>>$$
>>
>

>[!THEOREM] Theorem: Limit Arithmetic
>
>If two [real sequences](#Real%20Sequences) $\{a_n\}$ and $\{b_n\}$ are both [convergent](#Convergence), then
>
>$$
>\begin{aligned}
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
>&\lim_{n \to \infty} |a_n| = \left|\lim_{n \to \infty} a_n\right| \\ \\
>
>&\lim_{n \to \infty} \sqrt{a_n} = \sqrt{\lim_{n \to \infty} a_n} \qquad \text{if } \exists N \in \mathcal{D} \text{ such that } a_n \ge 0, \forall n \ge N
>
>\end{aligned}
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
>

>[!THEOREM] Theorem: The Limit of $q^n$
>
>The [real sequence](#Real%20Sequences) $q^n$:
>
>- [converges](#Convergence) to $0$ if and only if $|q| \lt 1$;
>- [converges](#Convergence) to $1$ if and only if $|q| = 1$;
>- [diverges](#Convergence) if and only if $|q| \gt 1$;
>- [diverges](#Convergence) towards $+ \infty$ if and only if $q \gt 1$.
>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: The Limit of $\frac{1}{n^k}$
>
>$$\lim_{n \to \infty} \frac{1}{n^r} = \begin{cases} 0 & \text{if } r > 0 \\ 1 & \text{if } r = 0 \\ \infty & \text{if } r < 0 \end{cases}$$
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

>[!THEOREM] Theorem: Reciprocal Limits
>
>Let $\{a_n\}$ be a [real sequence](#Real%20Sequences).
>
>If $\{a_n\}$ [converges](#Convergence) to $0$ and there exists some integer $N$ such that $a_n \gt 0$ for all $n \ge N$, then $\{\frac{1}{a_n}\}$ [diverges](#Convergence) towards $+\infty$.
>
>$$
>a_n \gt 0 \text{ and } \lim_{n \to \infty} a_n = 0 \implies \lim_{n \to \infty} \frac{1}{a_n} = +\infty
>$$
>
>If $\{a_n\}$ [converges](#Convergence) to $0$ and there exists some integer $N$ such that $a_n \lt 0$ for all $n \ge N$, then $\{\frac{1}{a_n}\}$ [diverges](#Convergence) towards $-\infty$.
>
>$$
>a_n \lt 0 \text{ and } \lim_{n \to \infty} a_n = 0 \implies \lim_{n \to \infty} \frac{1}{a_n} = -\infty
>$$
>
>If $\{a_n\}$ [diverges](#Convergence) towards either $+\infty$ or $-\infty$, then $\{\frac{1}{a_n}\}$ [converges](#Convergence) to $0$.
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

>[!THEOREM] Theorem: Arithmetic with Infinite Limits
>
>Let $\{a_n\}$ and $\{b_n\}$ be [real sequences](#Real%20Sequences). 
>
>If $\{a_n\}$ [converges](#Convergence) but $\{b_n\}$ [diverges](#Convergence) towards $\pm \infty$, then $\{a_n + b_n\}$ also [diverges](#Convergence) towards $\pm \infty$.
>
>$$
>\lim_{n \to \infty} a_n \in \mathbb{R} \text{ and } \lim_{n \to \infty} b_n = \pm \infty \implies \lim_{n\to \infty} (a_n + b_n) = \pm \infty
>$$
>
>If $\{a_n\}$ [converges](#Convergence) towards $L \in \mathbb{R}$ but $\{b_n\}$ [diverges](#Convergence) towards $\pm \infty$, then $\{a_n \cdot b_n\}$ also [diverges](#Convergence) towards $\pm \infty$ when $L \gt 0$ and [diverges](#Convergence) towards $\mp \infty$ when $L \lt 0$.
>
>$$
>\lim_{n \to \infty} a_n = L \in \mathbb{R} \text{ and } \lim_{n \to \infty} b_n = \pm \infty \implies \lim_{n\to \infty} (a_n \cdot b_n) = \begin{cases} \pm \infty \qquad \text{ if } L \gt 0 \\ \mp \infty \qquad \text{ if } L \lt 0\end{cases}
>$$
>
>If $\{a_n\}$ and $\{b_n\}$ both [diverge](#Convergence) towards $\pm \infty$, then $\{a_n + b_n\}$ also [diverges](#Convergence) towards $\pm \infty$ and $\{a_n \cdot b_n\}$ [diverges](#Convergence) towards $+ \infty$.
>
>$$
>\lim_{n \to \infty} a_n = \lim_{n \to \infty} b_n = \pm \infty \implies \lim_{n \to \infty} (a_n + b_n) = \pm \infty \text{ and } \lim_{n \to \infty} (a_n \cdot b_n) = + \infty
>$$
>
>If $\{a_n\}$ [diverges](#Convergence) towards $\pm \infty$ but $\{b_n\}$ [diverges](#Convergence) towards $\mp \infty$, then $\{a_n \cdot b_n\}$ [diverges](#Convergence) towards $- \infty$. However, this information is insufficient to determine $\lim_{n\to \infty} (a_n + b_n)$.
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

>[!THEOREM] Theorem: The Limit of $\left(1 + \frac{1}{n}\right)^n$ and its Variations
>
>The [real sequence](#Real%20Sequences) $a_n = \left(1 + \frac{1}{n}\right)^n$ [converges](#Convergence) towards [Euler's number](./Real%20Functions/Real%20Exponentiation.md) $\mathrm{e}$.
>
>$$
>\lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n = \mathrm{e}
>$$
>
>Similarly, the [limits](#Convergence) of the following [real sequences](#Real%20Sequences) can also be expressed using the [real exponential function](./Real%20Functions/Real%20Exponentiation.md):
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

>[!THEOREM] Theorem: Limits of Recursive Sequences
>
>Let $(a_n)$ be a [real sequence](./Real%20Sequences.md) defined as $a_{n+1} = f(a_n)$ for some [real function](./Real%20Functions/Real%20Functions.md) $f$.
>
>If $f$ is [continuous](./Real%20Functions/Continuity%20(Real%20Functions).md) and $(a_n)$ is [convergent](#Convergence), then
>
>$$
>f\left(\lim_{n \to \infty} a_n \right) = \lim_{n \to \infty} a_n.
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

### Subsequential Limits

>[!DEFINITION] Definition: Subsequential Limit
>
>Let $(a_n)_{n \in \mathcal{D}}$ be a [real sequence](#Real%20Sequence) and let $L \in \mathbb{R}$.
>
>We say that $L$ is a **subsequential limit** of $(a_n)_{n \in \mathcal{D}}$ if $(a_n)_{n \in \mathcal{D}}$ has some [convergent](#Convergence) [subsequence](../Functional%20Analysis/Sequences/Sequences.md) whose [limit](#Convergence) is $L$.
>
>>[!EXAMPLE]-
>>
>>Consider the [sequence](./Real%20Sequences.md) $a_n = (-1)^n$ and consider its [subsequence](../Functional%20Analysis/Sequences/Sequences.md) $a_{2k} = 1^{2k}$. The [sequence](./Real%20Sequences.md) $a_n = (-1)^n$ is [divergent](#Convergence), but $a_{2k} = 1^{2k}$ [converges](#Convergence) to $1$, so $1$ is a [subsequential limit](#Subsequential%20Limits) of $a_n$.
>>
>

>[!THEOREM] Bolzano-Weierstraß Theorem
>
>Every [bounded](./Real%20Functions/Boundedness%20of%20Real%20Functions.md)  [infinite](../Functional%20Analysis/Sequences/Sequences.md) [real sequence](#Real%20Sequence) has at least one [convergent](#Convergence) [subsequence](../Functional%20Analysis/Sequences/Sequences.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Limit $\iff$ Subsequential Limits
>
>The [limit](#Convergence) of an [infinite](../Functional%20Analysis/Sequences/Sequences.md) [real sequence](#Real%20Sequence) $(a_n)_{n \in \mathcal{D}}$ is $L \in \mathbb{R}$ if and only if all of the [subsequences](../Functional%20Analysis/Sequences/Sequences.md) of $(a_n)_{n \in \mathcal{D}}$ [converge](#Convergence) to $L$.
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (I) The [limit](#Convergence) of $(a_n)_{n \in \mathcal{D}}$ is $L \in \mathbb{R}$, then all of the [subsequences](../Functional%20Analysis/Sequences/Sequences.md) of $(a_n)_{n \in \mathcal{D}}$ [converge](#Convergence) to $L$.
>>- (II) If all of the [subsequences](../Functional%20Analysis/Sequences/Sequences.md) of $(a_n)_{n \in \mathcal{D}}$ [converge](#Convergence) to $L \in \mathbb{R}$, then the [limit](#Convergence) of $(a_n)_{n \in \mathcal{D}}$ is $L$.
>>
>>**Proof of (I):**
>>
>>Let $(b_{m})_{m \in f(\mathcal{D})}$ be a [subsequence](../Functional%20Analysis/Sequences/Sequences.md) of $(a_n)_{n \in \mathcal{D}}$. By definition, for each $m$ there exists some $n \in \mathcal{D}$ such that $m = f(n)$ and $b_m = a_m$. Since $(a_n)_{n \in \mathcal{D}}$ [converges](#Convergence) to $L$, we know that for each $\varepsilon \gt 0$ there exists some $N \in \mathcal{D}$ with
>>
>>$$
>>|a_m - L| \lt \varepsilon \qquad \forall m \ge N, 
>>$$
>>
>>i.e.
>>
>>$$
>>|b_m - L| \lt \varepsilon \qquad \forall m \ge N, 
>>$$
>>
>>**Proof of (II):**
>>
>>TODO
>>
>

### Limit Inferior and Limit Superior

>[!THEOREM] Theorem: Limit Inferior
>
>Let $(a_n)_{n \in \mathcal{D}}$ be a [real sequence](#Real%20Sequence).
>
>The [limit inferior](../Functional%20Analysis/Sequences/Convergence%20(Sequences.md#Limit%20Inferior%20and%20Limit%20Superior) of $(a_n)_{n \in \mathcal{D}}$, if it is finite, is equal to the [minimum](../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md#Boundedness) of all the [limits](#Convergence) of $(a_n)_{n \in \mathcal{D}}$'s [convergent](#Convergence) [subsequences](../Functional%20Analysis/Sequences/Sequences.md):
>
>$$
>\liminf_{n \to \infty} a_n = \min \{L \in \mathbb{R} \mid L \text{ is a limit of a convergent subsequence of } (a_n)_{n \in \mathcal{D}}\}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: $a_n = (-1)^n$
>>
>>We examine the following [real sequence](./Real%20Sequences.md) $(a_n)_{n \in \mathcal{D}}$:
>>
>>$$
>>a_n = (-1)^n
>>$$
>>
>>It is obvious that the smallest [limit](#Convergence) which a [subsequence](../Functional%20Analysis/Sequences/Sequences.md) of $(a_n)_{n \in \mathcal{D}}$ could have is $-1$. Therefore:
>>
>>$$
>>\liminf_{n \to \infty} a_n = -1
>>$$
>>
>
>>[!EXAMPLE]-
>>
>>We examine the following [real sequence](./Real%20Sequences.md) $(a_n)_{n \in \mathcal{D}}$:
>>
>>$$
>>a_n = \begin{cases}23 & \text{if } n = 10 \\ -42 & \text{if } n = 13 \\ (-1)^n & \text{otherwise}\end{cases}
>>$$
>>
>>The values $23$ and $-42$ cannot be [limits](#Convergence) of [subsequences](../Functional%20Analysis/Sequences/Sequences.md) of $(a_n)_{n \in \mathcal{D}}$, since they occur only once at a specific index. Therefore, the smallest [limit](#Convergence) which a [subsequence](../Functional%20Analysis/Sequences/Sequences.md) of $(a_n)_{n \in \mathcal{D}}$ could have is still $-1$:
>>
>>$$
>>\liminf_{n \to \infty} a_n = -1
>>$$
>>
>


>[!THEOREM] Theorem: Limit Superior
>
>Let $(a_n)_{n \in \mathcal{D}}$ be a [real sequence](#Real%20Sequence).
>
>The [limit superior](../Functional%20Analysis/Sequences/Convergence%20(Sequences.md#Limit%20Inferior%20and%20Limit%20Superior) of $(a_n)_{n \in \mathcal{D}}$, if it is finite, is equal to the [maximum](../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md#Boundedness) of all the [limits](#Convergence) of $(a_n)_{n \in \mathcal{D}}$'s [convergent](#Convergence) [subsequences](../Functional%20Analysis/Sequences/Sequences.md):
>
>$$
>\limsup_{n \to \infty} a_n = \max \{L \in \mathbb{R} \mid L \text{ is a limit of a convergent subsequence of } (a_n)_{n \in \mathcal{D}}\}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: $a_n = (-1)^n$
>>
>>We examine the following [real sequence](./Real%20Sequences.md) $(a_n)_{n \in \mathcal{D}}$:
>>
>>$$
>>a_n = (-1)^n
>>$$
>>
>>It is obvious that the greatest [limit](#Convergence) which a [subsequence](../Functional%20Analysis/Sequences/Sequences.md) of $(a_n)_{n \in \mathcal{D}}$ could have is $1$. Therefore:
>>
>>$$
>>\liminf_{n \to \infty} a_n = 1
>>$$
>>
>
>>[!EXAMPLE]-
>>
>>We examine the following [real sequence](./Real%20Sequences.md) $(a_n)_{n \in \mathcal{D}}$:
>>
>>$$
>>a_n = \begin{cases}23 & \text{if } n = 10 \\ -42 & \text{if } n = 13 \\ (-1)^n & \text{otherwise}\end{cases}
>>$$
>>
>>The values $23$ and $-42$ cannot be [limits](#Convergence) of [subsequences](../Functional%20Analysis/Sequences/Sequences.md) of $(a_n)_{n \in \mathcal{D}}$, since they occur only once at a specific index. Therefore, the greatest [limit](#Convergence) which a [subsequence](../Functional%20Analysis/Sequences/Sequences.md) of $(a_n)_{n \in \mathcal{D}}$ could have is still $+1$:
>>
>>$$
>>\limsup_{n \to \infty} a_n = +1
>>$$
>>
>
>

## Monotony

>[!THEOREM] Theorem: Difference Criteria for Sequence Monotony
>
>A [real sequence](#Real%20Sequences) $(a_n)$ is
>- [increasing](./Real%20Functions/Monotonicity%20of%20Real%20Functions.md) if $a_{n+1} - a_n \ge 0$ for all $n \in \mathbb{N}$;
>- [strictly increasing](./Real%20Functions/Monotonicity%20of%20Real%20Functions.md) if $a_{n+1} - a_n \gt 0$ for all $n \in \mathbb{N}$;
>- [decreasing](./Real%20Functions/Monotonicity%20of%20Real%20Functions.md) if $a_{n+1} - a_n \le 0$ for all $n \in \mathbb{N}$;
>- [strictly decreasing](./Real%20Functions/Monotonicity%20of%20Real%20Functions.md) if $a_{n+1} - a_n \lt 0$ for all $n \in \mathbb{N}$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: Monotony of $\frac{1}{n}$
>>
>>The [sequence](./Real%20Sequences.md) $(a_n)_{n \in \mathbb{N}}$ defined as $a_n = \frac{1}{n}$ is [strictly decreasing](./Real%20Functions/Monotonicity%20of%20Real%20Functions.md), since
>>
>>$$
>>a_{n+1} - a_n = \frac{1}{n+1} - \frac{1}{n} = -\frac{1}{n(n+1)} \lt 0.
>>$$
>>
>
>>[!EXAMPLE]- Example: Monotony of $\frac{n!}{2^n}$
>>
>>The [sequence](./Real%20Sequences.md) $(a_n)_{n \in \mathbb{N}}$ defined as $a_n = \frac{n!}{2^n}$ is [increasing](./Real%20Functions/Monotonicity%20of%20Real%20Functions.md), since
>>
>>$$
>>\frac{a_{n+1}}{a_n} = \frac{(n+1)!}{2^{n+1}}\div \frac{n!}{2^n} = \frac{(n+1)!}{2^{n+1}}\frac{2^n}{n!} = \frac{n+1}{2} \ge 1 
>>$$
>>
>

>[!THEOREM] Theorem: Quotient Criteria for Sequence Monotony
>
>A [real sequence](#Real%20Sequences) $(a_n)$ with $a_n \gt 0$ for all $n \in \mathbb{N}$ is:
>- [increasing](./Real%20Functions/Monotonicity%20of%20Real%20Functions.md) if $\frac{a_{n+1}}{a_n} \ge 1$ for all $n \in \mathbb{N}$;
>- [strictly increasing](./Real%20Functions/Monotonicity%20of%20Real%20Functions.md) if $\frac{a_{n+1}}{a_n} \gt 1$ for all $n \in \mathbb{N}$;
>- [decreasing](./Real%20Functions/Monotonicity%20of%20Real%20Functions.md) if $\frac{a_{n+1}}{a_n} \le 1$ for all $n \in \mathbb{N}$;
>- [strictly decreasing](./Real%20Functions/Monotonicity%20of%20Real%20Functions.md) if $\frac{a_{n+1}}{a_n} \lt 1$ for all $n \in \mathbb{N}$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Monotone Convergence Theorem
>
>If a [real sequence](#Real%20Sequences) is [increasing](./Real%20Functions/Monotonicity%20of%20Real%20Functions.md) and [bounded above](./Real%20Functions/Boundedness%20of%20Real%20Functions.md), then it is [convergent](#Convergence) and its [limit](#Convergence) is the [supremum](../../Set%20Theory/Boundedness.md) of its [image](../Functions/Functions.md).
>
>If a [real sequence](#Real%20Sequences) is [decreasing](./Real%20Functions/Monotonicity%20of%20Real%20Functions.md) and [bounded below](./Real%20Functions/Boundedness%20of%20Real%20Functions.md), then it is [convergent](#Convergence) and its [limit](#Convergence) is the [infimum](../../Set%20Theory/Boundedness.md) of its [image](../Functions/Functions.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example
>>
>>We want to see if the following, recursively defined [sequence](./Real%20Sequences.md) $(a_n)_{n \in \mathbb{N}}$ is [convergent](#Convergence):
>>
>>$$
>>a_1 = 2 \qquad a_{n+1} = \frac{1}{2}a_n + \frac{1}{a_n}
>>$$
>>
>>We prove two things:
>>- $(a_n)_{n \in \mathbb{N}}$ is [bounded](./Real%20Functions/Boundedness%20of%20Real%20Functions.md) by $\sqrt{2} \le a_n \le 2$;
>>- $(a_n)_{n \in \mathbb{N}}$ is [decreasing](./Real%20Functions/Monotonicity%20of%20Real%20Functions.md).
>>
>>**Proof of (1):**
>>
>>We do this using [induction](../../Logic/Mathematical%20Induction.md):
>>
>>1. Base case: The statement holds for $n = 1$, since $a_1 = 2$ and $\sqrt{2} \le 2 \le 2$.
>>2. Induction step: We assume that there exists some arbitrary, fixed $n \in \mathbb{N}$ such that $\sqrt{2} \le a_n \le 2$. We have
>>
>>$$
>>a_{n+1} = \frac{1}{2}a_n + \frac{1}{a_n} \le \frac{1}{2}
>>$$
>>
>>Since $\sqrt{2} \le a_n$, we know that $\frac{1}{a_n} \le \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}$. We therefore have the following:
>>
>>$$
>>a_{n+1} = \frac{1}{2}a_n + \frac{1}{a_n} \le \frac{1}{2}\cdot 2 + \frac{\sqrt{2}}{2} = \frac{2 + \sqrt{2}}{2} \lt 2
>>$$
>>
>>Furthermore,
>>
>>$$
>>a_{n+1} - \sqrt{2} = \frac{1}{2}a_n + \frac{1}{a_n} - \sqrt{2} = \frac{a_n^2 - 2\sqrt{2}a_n + 2}{2a_n} = \frac{(a_n - \sqrt{2})^2}{2a_n}
>>$$
>>
>>Since $\sqrt{2} \le a_n$, we know that $\frac{(a_n - \sqrt{2})^2}{2a_n} \ge 0$, i.e. $a_{n+1} - \sqrt{2} \ge 0$ and so $a_{n+1} \ge \sqrt{2}$. 
>>
>>Thus we have shown at $(a_n)$ is [bounded](./Real%20Functions/Boundedness%20of%20Real%20Functions.md)
>>
>>**Proof of (2):**
>>
>>We have
>>
>>$$
>>a_{n+1} - a_n = \frac{1}{2}a_n + \frac{1}{a_n} - a_n = \frac{1}{a_n} - \frac{1}{2}a_n = \frac{2 - a_n^2}{2a_n} \le 0,
>>$$
>>
>>since $a_n \ge \sqrt{2}$.
>>
>>Thus, we have shown that $(a_n)$ is [decreasing](./Real%20Functions/Monotonicity%20of%20Real%20Functions.md).
>>
>>Since we showed that $(a_n)$ is both [bounded](./Real%20Functions/Boundedness%20of%20Real%20Functions.md) and [decreasing](./Real%20Functions/Monotonicity%20of%20Real%20Functions.md), we know it is [convergent](#Convergence).
>>
>