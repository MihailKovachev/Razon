---
title: Permutations
tags:
    - combinatorics
    - mathematics
---

# Permutations without Repetition

>[!DEFINITION] Definition: Permutation
>
>Let $S$ be a finite [set](../Set%20Theory/Sets.md) with $n$ elements.
>
>A **permutation (without repetition)** of $S$ is an $n$-[tuple](../Set%20Theory/Tuples.md) which contains every element of $S$ exactly once.
>
>>[!INTUITION]-
>>
>>A permutation of $S$ is just a way to arrange all elements of $S$.
>>
>
>>[!EXAMPLE]-
>>
>>Suppose $S = \{A, B, C, D\}$. The following are permutations of $S$:
>>
>>$$
>>(A, B, C, D) \qquad (D, A, C, B) \qquad (B, D, A, C) \qquad (C, B, D, A)
>>$$
>>
>>The following are *not* permutations of $S$: 
>>
>>$$
>>(A, B, D) \qquad (B, C) \qquad (A, B, B, D, C)
>>$$
>>
>

>[!THEOREM] Theorem: Number of Permutations
>
>Let $S$ be a finite [set](../Set%20Theory/Sets.md) with $n$ elements.
>
>The total number of possible permutations of $S$ is
>
>$$
>\prod_{k = 1}^n k = 1 \times 2 \times \cdots \times (n-1) \times n = n!
>$$
>
>>[!NOTATION]-
>>
>>$$
>>P_n
>>$$
>>
>
>>[!PROOF]-
>>
>>We go through the process of constructing a permutation.
>>
>>For the first element of the permutation, we can choose any one of the $n$ elements inside $S$. For the second element of the permutation, we can choose only between the remaining $n - 1$ elements of $S$, since we already chose one element as our first. In general, for the $k$-th element of the permutation, we can choose between $n - (k - 1)$ elements, since at the $k$-th step, we have already filled $k-1$ places of the permutation with elements from $S$. Multiplying these possibilities together, we get the stated result.
>>
>

# Permutations with Repetition

>[!DEFINITION] Definition: Permutation with Repetition
>
>Let $S = \{s_1, \dotsc, s_k\}$ be a [set](../Set%20Theory/Sets.md).
>
>A **permutation with repetition** of class $n$ is a $n$-[tuple](../Set%20Theory/Tuples.md) of elements from $S$ such that the element $s_i$ appears in the $n$-tuple exactly $n_i$ times.
>

>[!THEOREM] Theorem: Total Number of Permutations with Repetition
>
>If $S \{s_1, \dotsc, s_k\}$ is a [set](../Set%20Theory/Sets.md) with $n$ elements, then the total number of [permutations with repetition](Permutations.md#Permutations%20with%20Repetition) of class $k$ such that $s_i$ appears $n_i$ times, denoted by $\tilde{P}(n_1, \dotsc, n_k$ is given by
>
>$$
>\tilde{P}(n_1, \dotsc, n_k) = \frac{n!}{n_1! \cdots n_k!}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>