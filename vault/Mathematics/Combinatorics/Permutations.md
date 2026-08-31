---
title: Permutations
tags:
    - combinatorics
    - mathematics
---

# Permutations without Repetition

>[!DEFINITION] Definition: Permutation
>
>A **permutation** of a [set](../Set%20Theory/Sets.md) $S$ is a [bijection](../Analysis/Functions/Injections,%20Surjections%20and%20Bijections.md) $f: S \to S$ between $S$ and itself.
>
>>[!INTUITION]
>>
>>A [permutation](./Permutations.md) of $S$ is just a way to arrange all its elements.
>>
>
>>[!NOTATION] Notation
>>
>>[Permutations](./Permutations.md) are usually denoted by $\sigma$.
>>
>

## Finite Permutations

When $S$ is [finite](../Set%20Theory/Cardinality.md), a [permutation](./Permutations.md) of $S$ is an $n$-[tuple](../Set%20Theory/Tuples.md) which contains every element of $S$ exactly once.

>[!EXAMPLE]- Example: Permutations of Finite Sets
>
>Suppose $S = \{A, B, C, D\}$. The following are permutations of $S$:
>
>$$
>(A, B, C, D) \qquad (D, A, C, B) \qquad (B, D, A, C) \qquad (C, B, D, A)
>$$
>
>The following are *not* permutations of $S$: 
>
>$$
>(A, B, D) \qquad (B, C) \qquad (A, B, B, D, C)
>$$
>

>[!THEOREM] Theorem: Number of Permutations
>
>If $S$ is a [finite](../Set%20Theory/Cardinality.md) [set](../Set%20Theory/Sets.md), then the total number of [permutations](./Permutations.md) $S$ is the following:
>
>$$
>\prod_{k = 1}^n k = 1 \times 2 \times \cdots \times (n-1) \times n = n!
>$$
>
>>[!NOTATION]
>>
>>$$
>>P_n
>>$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: The Symmetric Group
>
>If $X$ is a [finite](../Set%20Theory/Cardinality.md) [set](../Set%20Theory/Sets.md), then the [set](../Set%20Theory/Sets.md) $\mathcal{S}$ of all [permutations](./Permutations.md) of $X$ forms a [group](../Algebra/Groups/Groups.md) $(\mathcal{S}, \circ)$ under [composition](../Analysis/Functions/Functions.md).
>
>>[!DEFINITION] Definition: The Symmetric Group
>>
>>We call $(\mathcal{S}, \circ)$ the **symmetric group** on $X$.
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\operatorname{Sym}(X) \qquad S_X
>>>$$
>>>
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

### Parity

>[!DEFINITION] Definition: Sign
>
>TODO
>
>>[!DEFINITION] Definition: Parity
>>
>>A [permutation](./Permutations.md) $\sigma$ of a [finite](../Set%20Theory/Cardinality.md) [set](../Set%20Theory/Sets.md) is:
>>- **odd** if its [sign](#Parity) is $-1$: $\operatorname{sgn}(\sigma) = -1$;
>>- **even** if its [sign](#Parity) is $+1$: $\operatorname{sgn}(\sigma) = +1$.
>>
>

>[!THEOREM] Theorem: Sign via Inversions
>
>Let $X$ be a [totally ordered](../Set%20Theory/Orderings/Partially%20Ordered%20Set.md) [finite](../Set%20Theory/Cardinality.md) [set](../Set%20Theory/Sets.md) and let $\sigma$ be a [permutation](./Permutations.md) of $X$.
>
>>[!DEFINITION] Definition: Inversion
>>
>>An **inversion** of $\sigma$ are any $i, j \in X$ such that $i \lt j$ and $\sigma(i) \gt \sigma(j)$.
>>
>
>If $N(\sigma)$ is the total number of [inversions](#Parity) of $\sigma$, then the [sign](#Parity) of $\sigma$ is given by
>
>$$
>\operatorname{sgn}(\sigma) = (-1)^{N(\sigma)}.
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Permutations with Repetition

>[!DEFINITION] Definition: Permutation with Repetition
>
>Let $S$ be a [multiset](../Set%20Theory/Multisets.md) with cardinality $k$.
>
>A **permutation with repetition** of $S$ is a $k$-[tuple](../Set%20Theory/Tuples.md) of elements from $S$ in which each element $s_i$ is present as many times as its multiplicity $k_i$.
>
>>[!EXAMPLE]-
>>
>>Let $S = \{3, 3, 4, 5, 5, 5\}$.
>>
>>Some permutations with repetition of $S$ are
>>
>>$$
>>(4, 3, 5, 5, 3, 5) \qquad (5, 3, 4, 5, 5, 3) \qquad (5, 3, 5, 4, 3, 5). 
>>$$
>>
>

>[!THEOREM] Theorem: Total Number of Permutations with Repetition
>
>If $S = \{s_1, \dotsc, s_n\}$ is a [multiset](../Set%20Theory/Multisets.md) with cardinality $k$, then the total number of [permutations with repetition](#Permutations%20with%20Repetition) $S$ can be calculated via $k$ and the multiplicity $k_i$ of each element as follows:
>
>$$
>\frac{k!}{k_1! \cdots k_n!}
>$$
>
>>[!NOTATION]
>>
>>Since this number depends only on the cardinality $k$ and multiplicities $k_i$ but does not depend on the elements themselves, we call the above number the **total number of permutations with repetition of class** $k$ and denote it by
>>
>>$$
>>\tilde{P}(k_1, \dotsc, k_n) 
>>$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>