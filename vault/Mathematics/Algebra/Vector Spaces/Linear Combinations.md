---
tags:
  - linear-algebra
  - algebra
  - mathematics
---

# Linear Combinations

>[!DEFINITION] Definition: Linear Combination
>
>Let $\mathbf{v}_1, \cdots, \mathbf{v}_n$ be [vectors](../../../index.md#Vector%20Spaces) in a [vector space](../../../index.md#Vector%20Spaces) $(V, F, +, \cdot)$.
>
>A **linear combination** of $\mathbf{v}_1, \cdots, \mathbf{v}_n$ is any $\mathbf{v} \in V$ which can be expressed as
>
>$$
>\mathbf{v} = \lambda_1\mathbf{v}_1 + \cdots + \lambda_n \mathbf{v}_n = \sum_{i = 1}^n \lambda_i \mathbf{v}_i
>$$
>
>for some $\lambda_1, \dotsc, \lambda_n \in F$.
>
>>[!EXAMPLE]-
>>
>>We can express every $\mathbf{v} = (v_1, \dotsc, v_n) \in F^n$ as a [linear combination](./Linear%20Combinations.md)
>>
>>$$
>>\mathbf{v} = v_1 \mathbf{e}_1 + \cdots + v_n \mathbf{e}_n
>>$$
>>
>>of
>>
>>$$
>>\begin{aligned}
>>\mathbf{e}_1 &= (1, 0, \dotsc, 0) \\
>>\mathbf{e}_2 &= (0, 1, 0, \dotsc, 0) \\
>>&\vdots \\
>>\mathbf{e}_n &= (0, \dotsc, 0, 1)
>>\end{aligned}
>>$$
>>
>
>>[!EXAMPLE]-
>>
>>The [polynomial](../Fields/The%20Real%20Numbers/Real%20Polynomials.md) $2x^2 + x + 3$ is a [linear combination](./Linear%20Combinations.md) of the [polynomials](../Fields/The%20Real%20Numbers/Real%20Polynomials.md) $x^0, x, x^2$.
>>
>

## Linear Independence

>[!DEFINITION] Definition: Linear Independence
>
>A [subset](../../Set%20Theory/Sets.md) $S \subseteq V$ of a [vector space](./Vector%20Spaces.md) $V$ is **linearly independent** if removing any $\mathbf{v}$ from $S$ results in a [span](./Span.md) different from that of $S$:
>
>$$
>\operatorname{\mathop{span}} (S) \ne \mathop{\operatorname{span}} (S \setminus \{\mathbf{v}\}) \qquad \forall \mathbf{v} \in S
>$$
>
>Let $\mathbf{v}_1, \cdots, \mathbf{v}_n$ be [vectors](./Vector%20Spaces.md) in a [vector space](./Vector%20Spaces.md) $(V, F, +, \cdot)$.
>
>We say that $\mathbf{v}_1, \dotsc, \mathbf{v}_n$ are **linearly independent** if
>
>$$
>\operatorname{\mathop{span}} (\mathbf{v}_1, \cdots, \mathbf{v}_n) \ne \operatorname{\mathop{span}} (\mathbf{v}_1, \dotsc, \mathbf{v}_{k-1}, \mathbf{v}_{k+1}, \dotsc, \mathbf{v}_n)
>$$
>
>for all $k \in \{1, \dotsc, n\}$.
>
>>[!WARNING]
>>
>>Saying that $\mathbf{v}_1, \dotsc, \mathbf{v}_n$ are [linearly independent](#Linear%20Independence) is the same as saying that $\{\mathbf{v}_1, \dotsc, \mathbf{v}_n\}$ [linearly independent](#Linear%20Independence) *only when* $\mathbf{v}_1, \dotsc, \mathbf{v}_n$ *are all different*. 
>>
>>For example, if $\mathbf{v}_1$ and $\mathbf{v}_2$ are [linearly independent](#Linear%20Independence), then $\mathbf{v}_1, \mathbf{v}_1, \mathbf{v}_2$ are *not* [linearly independent](#Linear%20Independence), since $\operatorname{\mathop{span}}(\mathbf{v}_1, \mathbf{v}_1, \mathbf{v}_2) = \operatorname{\mathop{span}}(\mathbf{v}_1, \mathbf{v}_2)$. However, $\{\mathbf{v}_1, \mathbf{v}_1, \mathbf{v}_2\}$ *is* [linearly independent](#Linear%20Independence) because $\{\mathbf{v}_1, \mathbf{v}_1, \mathbf{v}_2\} = \{\mathbf{v}_1, \mathbf{v}_2\}$ and $\operatorname{\mathop{span}}(\{\mathbf{v}_1, \mathbf{v}_1, \mathbf{v}_2\}) \ne \operatorname{\mathop{span}}(\{\mathbf{v}_1, \mathbf{v}_1, \mathbf{v}_2\} \setminus \{\mathbf{v}_1\}) = \operatorname{\mathop{span}}(\{\mathbf{v}_2\})$.
>>
>
>>[!EXAMPLE]-
>>
>>The [vectors](./Vector%20Spaces.md)
>>
>>$$
>>\begin{aligned}
>>\mathbf{e}_1 &= (1, 0, \dotsc, 0) \\
>>\mathbf{e}_2 &= (0, 1, 0, \dotsc, 0) \\
>>&\vdots \\
>>\mathbf{e}_n &= (0, \dotsc, 0, 1)
>>\end{aligned}
>>$$
>>
>>in $F^n$ are [linearly independent](#Linear%20Independence).
>>
>
>>[!EXAMPLE]-
>>
>>For each $t$ we define the [function](../../Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) $f_t: \mathbb{R} \to \mathbb{R}$ in the following way:
>>
>>$$
>>f_t(x) \overset{\text{def}}{=} \begin{cases}1 & \text{if } x = t \\ 0 & \text{otherwise}\end{cases}
>>$$
>>
>>The [set](../../Set%20Theory/Sets.md) $\{f_t: t \in \mathbb{R}\}$ of all $f_t$'s is [linearly independent](#Linear%20Independence) in the [space](./Vector%20Spaces.md) of all [real functions](../../Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md).
>>
>
>
>>[!THEOREM] Theorem: Alternative Definition
>>
>>Let $V$ be a [vector space](./Vector%20Spaces.md).
>>
>>A [subset](../../Set%20Theory/Sets.md) $S \subseteq V$ is [linearly independent](#Linear%20Independence) if and only if there is no $\mathbf{v} \in S$ which can be represented as a [linear combination](#Linear%20Combinations) of [vectors](./Vector%20Spaces.md) from $S \setminus \{\mathbf{v}\}$.
>>
>>>[!PROOF]-
>>>
>>>We need to prove two things:
>>>- (I) If $S$ is [linearly independent](#Linear%20Independence), then there is no $\mathbf{v} \in S$ which can be represented as a [linear combination](#Linear%20Combinations) of [vectors](./Vector%20Spaces.md) from $S \setminus \{\mathbf{v}\}$.
>>>- (II) If there is no $\mathbf{v} \in S$ which can be represented as a [linear combination](#Linear%20Combinations) of [vectors](./Vector%20Spaces.md) from $S \setminus \{\mathbf{v}\}$, then $S$ is [linearly independent](#Linear%20Independence).
>>>
>>>**Proof of (I):**
>>>
>>>Suppose there is some $\mathbf{v} \in S$ which can be expressed as a [linear combination](#Linear%20Combinations) of [vectors](./Vector%20Spaces.md) from $S \setminus \{\mathbf{v}\}$. This means that $\mathbf{v} \in \mathop{\operatorname{span}} (S \setminus \{\mathbf{v}\})$. But this is a contradiction with the definition of [linear independence](#Linear%20Independence), since it means that $\mathop{\operatorname{span}} (S \setminus \{\mathbf{v}\}) = \mathop{\operatorname{span}} (S)$.
>>>
>>
>
>>[!THEOREM] Theorem: Alternative Definition
>>
>>Let $V$ be a [vector space](./Vector%20Spaces.md).
>>
>>A [subset](../../Set%20Theory/Sets.md) $S \subseteq V$ is [linearly independent](#Linear%20Independence) if and only if
>>
>>$$
>>\lambda_1 \mathbf{v}_1 + \cdots + \lambda_n \mathbf{v}_n = 0 \implies \lambda_1 = \cdots = \lambda_n = 0
>>$$
>>
>>for all pairwise-different $\mathbf{v}_1, \dotsc, \mathbf{v}_n \in S$.
>>
>>>[!PROOF]-
>>>
>>>We need to prove two things:
>>>- (I) If $S$ is [linearly independent](#Linear%20Independence), then $\lambda_1 \mathbf{v}_1 + \cdots + \lambda_n \mathbf{v}_n = 0 \implies \lambda_1 = \cdots = \lambda_n = 0$ for all pairwise-different $\mathbf{v}_1, \dotsc, \mathbf{v}_n \in S$.
>>>- (II) If $\lambda_1 \mathbf{v}_1 + \cdots + \lambda_n \mathbf{v}_n = 0 \implies \lambda_1 = \cdots = \lambda_n = 0$ for all pairwise-different $\mathbf{v}_1, \dotsc, \mathbf{v}_n \in S$, then $S$ is [linearly independent](#Linear%20Independence).
>>>
>>>**Proof of (I):** TODO
>>>
>>>**Proof of (II):**
>>>
>>>Suppose that $S$ is *not* [linearly independent](#Linear%20Independence). Then there exists some $\mathbf{v} \in S$ such that $\mathop{\operatorname{span}}(S) = \mathop{\operatorname{span}}(S \setminus \{\mathbf{v}\})$. This means that there is some $N \in \mathbb{N}$, some pairwise different $\mathbf{v}_1,\dotsc,\mathbf{v}_N \ne \mathbf{v}$ and some non-zero $\lambda_1, \dotsc, \lambda_N \in F$ such that
>>>
>>>$$
>>>\mathbf{v} = \lambda_1 \mathbf{v}_1 + \cdots + \lambda_N \mathbf{v}_N.
>>>$$
>>>
>>>This means that 
>>>
>>>$$
>>>\lambda_1 \mathbf{v}_1 + \cdots + \lambda_N \mathbf{v}_N + (-1)\mathbf{v} = \mathbf{0}
>>>$$
>>>
>>>However, this is a contradiction because $\mathbf{v},\mathbf{v}_1, \dotsc, \mathbf{v}_N$ are all pairwise different but $-1 \ne 0$.
>>>
>>
>

>[!THEOREM] Theorem: Size Limit for Linearly Independent Sets
>
>The number of elements in any [set](../../Set%20Theory/Sets.md) $I$ of [linearly independent](./Linear%20Combinations.md) [vectors](./Vector%20Spaces.md) from a [finitely generated](#Span) [vector space](./Vector%20Spaces.md) $(V,F,+,\cdot)$ is always less than or equal to the [dimension](./Hamel%20Bases.md) of $V$.
>
>$$
>|I| \le \dim(V)
>$$
>
>>[!PROOF]-
>>
>>Let $B = \{\mathbf{b}_1, \cdots, \mathbf{b}_n,\}$ be a [Hamel Bases](./Hamel%20Bases.md) of $V$ and let $I = \{\mathbf{v}_1, \cdots, \mathbf{v}_m\}$ be a [set](../../Set%20Theory/Sets.md) of [linearly independent](./Linear%20Combinations.md) [vectors](./Vector%20Spaces.md).
>>
>>According to the [Hamel Bases](./Hamel%20Bases.md) there are $n-m$ [vectors](./Vector%20Spaces.md) in $B$ which form a basis with the vectors from $I$. This means that $n-m$ cannot be negative and thus the proof is complete.
>>
>

>[!DEFINITION] Definition: Maximality
>
>A [linearly independent](#Linear%20Independence) [subset](../../Set%20Theory/Sets.md) $S \subseteq V$ of a [vector space](./Vector%20Spaces.md) $V$ is **maximal** if there is no $\mathbf{v} \in V \setminus S$ such that the [union](../../Set%20Theory/Sets.md#Operations) $S \cup \{ \mathbf{v} \}$ is still [linearly independent](#Linear%20Independence).
>
>>[!TIP]
>>
>>This means that no matter how much we try, we cannot find any vector outside $S$ such that if we add it to $S$, we would still end up with a linearly independent set.
>>
>

## Linear Dependence

>[!DEFINITION] Definition: Linear Dependence
>
>Let $\mathbf{v}_1, \cdots, \mathbf{v}_n$ be [vectors](../../../index.md) in some [index](../../../index.md) $(V,F,+,\cdot$).
>
>We say that $\mathbf{v}_1, \cdots, \mathbf{v}_n$ are **linearly dependent** iff they are not [linearly independent](./Linear%20Combinations.md), i.e. there exist $c_1, \cdots, c_n$ with at least one $c_i \ne 0$ such that
>
>$$
>c_1\mathbf{v}_1 + \cdots + c_n\mathbf{v}_n = \mathbf{0}
>$$
>

>[!THEOREM] Theorem: Linear Dependence $\implies$ Linear Combination
>
>If $\{ \mathbf{v}_1, \cdots, \mathbf{v}_n\} \, (n \ge 2)$ are [linearly dependent](./Linear%20Combinations.md) [vectors](./Vector%20Spaces.md), then there is at least one $\mathbf{v}_i \in \{ \mathbf{v}_1, \cdots, \mathbf{v}_n\}$  which can be expressed as a [linear combination](./Linear%20Combinations.md) of the rest of the [vectors](./Vector%20Spaces.md):
>
>$$
>\mathbf{v}_i = \sum_{\begin{aligned}j &= 1 \\ j &\ne i\end{aligned}}^n c_j \mathbf{v}_j
>$$
>
>>[!PROOF]-
>>
>>According to the definition of linear dependence, there are coefficients $h_1, \cdots, h_n \in F$ with at least one $h_i \ne 0$ such that
>>
>>$$
>>h_1 \mathbf{v}_1 + \cdots + h_i \mathbf{v}_i + \cdots + h_n \mathbf{v}_n = \mathbf{0}
>>$$
>>
>>Let's move everything except $h_i \mathbf{v}_i$ to the other side of the equation:
>>
>>$$
>>h_i \mathbf{v}_i = -h_1\mathbf{v}_1+\cdots -h_{i-1}\mathbf{v}_{i-1}-h_{i+1}\mathbf{v}_{i+1}+\cdots+-h_n\mathbf{v}_n
>>$$
>>
>>Since $h_i \ne 0$, we can divide both sides by it:
>>
>>
>>
>>$$
>>\mathbf{v}_i = c_1\mathbf{v}_1+\cdots + c_{i-1}\mathbf{v}_{i-1}+c_{i+1}\mathbf{v}_{i+1}+\cdots+c_n\mathbf{v}_n
>>$$
>>
>>We have thus obtained $\mathbf{v}_i$ as a linear combination of the other vectors, where $c_j = -\frac{h_j}{h_i}$
>>
>