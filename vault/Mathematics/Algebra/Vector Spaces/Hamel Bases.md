---
tags:
  - linear-algebra
  - algebra
  - mathematics
---

# Hamel Bases

>[!DEFINITION] Definition: Basis
>
>A **basis** of a [vector space](../../../index.md#Vector%20Spaces) $(V,F,+,\cdot)$ is a [linearly independent](./Linear%20Combinations.md#Linear%20Independence) [spanning set](./Linear%20Combinations.md#Span) for it.
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
>>in $F^n$ are a [basis](./Hamel%20Bases.md) for $F^n$.
>>
>
>>[!EXAMPLE]-
>>
>>The [polynomials](TODO) $1, x, x^2, \dotsc$ are a [basis](./Hamel%20Bases.md) for the [space](./Vector%20Spaces.md) of all [polynomials](TODO) over $F$.
>>
>
>>[!THEOREM] Equivalent Definition
>>
>>A [set](../../Set%20Theory/Sets.md) of [vectors](../../../index.md#Vector%20Spaces) is a [basis](#Bases) for a [vector space](../../../index.md#Vector%20Spaces) $(V,F,+,\cdot)$ if and only if it is a [maximal linearly independent set](./Linear%20Combinations.md#Linear%20Independence).
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>
>>[!THEOREM] Equivalent Definition
>>
>>A [set](../../Set%20Theory/Sets.md) of [vectors](../../../index.md#Vector%20Spaces) is a [basis](#Bases) for a [vector space](../../../index.md#Vector%20Spaces) $(V,F,+,\cdot)$ if and only if it is a [minimal spanning set](./Linear%20Combinations.md#Span).
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

>[!THEOREM] Theorem: Existence of a Basis
>
>Every [vector space](./Vector%20Spaces.md) has at least one [basis](./Hamel%20Bases.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Existence of a Finite Basis
>
>A [vector space](./Vector%20Spaces.md) has a [finite](../../Set%20Theory/Cardinality.md) [basis](./Hamel%20Bases.md) if and only if it is  [finitely generated](./Span.md#Spanning%20Sets).
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Dimension

>[!THEOREM] Theorem: Number of Basis Elements
>
>All [bases](#Bases) of a given [vector space](../../../index.md#Vector%20Spaces) $(V, F, +, \cdot)$ have the same [cardinality](../../Set%20Theory/Cardinality.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Dimension of a Vector
>>
>>If these [bases](./Hamel%20Bases.md) are [finite](../../Set%20Theory/Cardinality.md), then we call $(V, F, +, \cdot)$ **finite-dimensional**. In this case, the [cardinality](../../Set%20Theory/Cardinality.md) of the [bases](#Bases) is known as the **dimension** of $(V, F, +, \cdot)$.
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\dim(V)
>>>$$
>>>
>>
>>If these [bases](./Hamel%20Bases.md) are [infinite](../../Set%20Theory/Cardinality.md), then we call $(V, F, +, \cdot)$ **infinite-dimensional**.
>>
>

>[!THEOREM] Theorem: Dimension Equality
>
>Two [finite dimensional](./Hamel%20Bases.md) [vector spaces](./Vector%20Spaces.md) have the same [dimension](./Hamel%20Bases.md) if and only if there is a [vector space isomorphism](../../Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md) between them.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Basis Representation
>
>Let $(V,F,+,\cdot)$ a [vector space](../../../index.md#Vector%20Spaces).
>
>If $B$ is a [basis](#Bases) of $(V,F,+,\cdot)$, then each [vector](../../../index.md#Vector%20Spaces) of $(V,F,+,\cdot)$ can be uniquely expressed as a [linear combination](./Linear%20Combinations.md#Linear%20Combinations) of elements from $B$.
>
>>[!NOTE] Note: Uniqueness
>>
>>Here, "uniquely" means that no two vectors are expressed as a linear combination which has the exact same coefficients in front of the exact same basis vectors.
>>
>
>>[!PROOF]-
>>
>>Let $\mathbf{v}_1, \dotsc, \mathbf{v}_n \in B$ be pairwise different and let $\mathbf{v} \in V$. Furthermore, suppose that $\mathbf{v}$ has the representations $\sum_{i=1}^n \lambda_i \mathbf{v}_i$ and $\sum_{i=1}^n \mu_i \mathbf{v}_i$, i.e.
>>
>>$$
>>\mathbf{v} = \sum_{i=1}^n \lambda_i \mathbf{v}_i = \sum_{i=1}^n \mu_i \mathbf{v}_i.
>>$$
>>
>>We therefore have the following:
>>
>>$$
>>\sum_{i = 1}^n (\lambda_i - \mu_i)\mathbf{v}_i = \mathbf{0}
>>$$
>>
>>Since $B$ is a [basis](./Hamel%20Bases.md), we know that $\mathbf{v}_1, \dotsc, \mathbf{v}_n$ are [linearly independent](./Linear%20Combinations.md#Linear%20Independence). Therefore, we have $\lambda_i - \mu_i = 0$ for all $i \in \{1, \dotsc, n\}$, i.e. $\lambda_i = mu_i$.
>>
>

>[!THEOREM] Theorem: Basis Criterion
>
>Let $(V,F,+,\cdot)$ be a [finite dimensional](./Hamel%20Bases.md) [vector space](./Vector%20Spaces.md).
>
>Every [linearly independent](./Linear%20Combinations.md#Linear%20Independence) [subset](../../Set%20Theory/Sets.md) whose [cardinality](../../Set%20Theory/Cardinality.md) is equal to the [dimension](#Dimension) $\dim(V)$ is a [basis](./Hamel%20Bases.md) for $(V,F,+,\cdot)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Basis Extension
>
>Let $V$ be a [finite dimensional](./Hamel%20Bases.md) [vector space](./Vector%20Spaces.md) with $\dim V = n$.
>
>If $\mathbf{v}_1, \dotsc, \mathbf{v}_k$ are [linearly independent](./Linear%20Combinations.md#Linear%20Independence), then there exist $\mathbf{v}_{k+1}, \dotsc, \mathbf{v}_n \in V$ such that $\mathbf{v}_1, \dotsc, \mathbf{v}_n$ is a [basis](./Hamel%20Bases.md) of $V$. Moreover, if $B$ is already a [basis](./Hamel%20Bases.md) of $V$, then $\mathbf{v}_{k+1}, \dotsc, \mathbf{v}_n$ can be chosen such that $\mathbf{v}_{k+1}, \dotsc, \mathbf{v}_n \in B$.
>
>>[!PROOF]-
>>
>>Let $\mathbf{w}_1, \dotsc, \mathbf{w}_n \in V$ be arbitrary. 
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Steinitz Exchange Lemma
>
>Let $B = \{\mathbf{v}_1,\cdots,\mathbf{v}_n\}$ be a [basis](#Bases) of a [finitely generated](./Linear%20Combinations.md#Span) [vector space](./Vector%20Spaces.md) $(V, F, +,\cdot)$.
>
>In each [set](../../Set%20Theory/Sets.md) $\{\mathbf{u}_1,\cdots,\mathbf{u}_m\}\subset V$ of $m$ [linearly independent](./Linear%20Combinations.md#Linear%20Independence) [vectors](./Vector%20Spaces.md) there are $n-m$ [vectors](./Vector%20Spaces.md) in $B$ (without loss of generality $\mathbf{v}_{m+1}, \cdots, \mathbf{v}_n$) such that
>
>$$
>\{\mathbf{u}_1,\cdots,\mathbf{u}_m,\mathbf{v}_{m+1},\cdots,\mathbf{v}_n\}
>$$
>
>is also a [basis](#Bases) of $(V,F,+,\cdot)$.
>
>>[!TIP]
>>
>>This means that for every [set](../../Set%20Theory/Sets.md) $\{\mathbf{u}_1,\cdots,\mathbf{u}_m\}\subset V$ of $m$ [linearly independent](./Linear%20Combinations.md#Linear%20Independence) [vectors](../../../index.md#Vector%20Spaces), we can find $m$ [vectors](../../../index.md#Vector%20Spaces) in $B$ which we can replace with $\mathbf{u}_1,\cdots,\mathbf{u}_m$ and still obtain a [basis](#Bases) of $(V,K,+,\cdot)$.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Ordered Bases

>[!DEFINITION] Definition: Ordered Basis
>
>Let $(V,F,+,\cdot)$ be an [finite-dimensional](#Dimension) [vector space](./Vector%20Spaces.md) with $\dim(V) = n$;
>
>An **ordered basis** of $(V,F,+,\cdot)$ is an $n$-[tuple](../../Set%20Theory/Tuples.md) $(\mathbf{b}_1, \cdots, \mathbf{b}_n)$ such that $\{\mathbf{b}_1, \cdots, \mathbf{b}_n\}$ is a [basis](#Bases) of $(V,F,+,\cdot)$.
>

>[!DEFINITION] Definition: Coordinate Vector
>
>Let $B = (\mathbf{b}_1, \cdots, \mathbf{b}_n)$ be an [ordered basis](#Ordered%20Bases) of an $n$-[dimensional](#Dimension) [vector space](./Vector%20Spaces.md) $(V,F,+,\cdot)$.
>
>If $\mathbf{v} \in V$ has the [basis representation](#Bases) $\mathbf{v} = v_1\mathbf{b}_1 + \cdots + v_n \mathbf{b}_n$, then the **coordinate vector of** $\mathbf{v}$ **with respect to the basis** $B$ is the [column vector](../Matrices/Row%20and%20Column%20Vectors.md)
>
>$$
>[\mathbf{v}]_{B} \overset{\text{def}}{=} \begin{bmatrix} v_1 \\ \vdots \\ v_n \end{bmatrix} \in F^{n}.
>$$
>
>>[!DEFINITION] Definition: Coordinate System
>>
>>The [isomorphism](../../Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md) $\phi: F^n \to V$ which to each $n$-[tuple](../../Set%20Theory/Tuples.md) $(\lambda_1, \dotsc, \lambda_n) \in F^n$ assigns the [vector](./Vector%20Spaces.md) $\sum_{k = 1}^{n} \lambda_k \mathbf{b}_k$ is known as the **coordinate system with respect to** $B$.
>>
>