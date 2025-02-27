---
title: Combinations
tags:
    - combinatorics
    - mathematics
---

# Combinations without Repetitions

>[!DEFINITION] Definition: Combination
>
>Let $S$ be a finite set.
>
>A **combination** of class $k$ is a [subset](../Set%20Theory/Sets.md) of $S$ with $k$ elements.
>
>>[!NOTE]
>>
>>If $S$ has $n$ elements, we also say a "combination of $n$ elements of class $k$".
>>
>
>>[!INTUITION]-
>>
>>A combination of class $k$ is just a way to pick $k$ elements of $S$, irrespective of any order. You can imagine $S$ as a big box full of marbles, each marble with a unique colour. You grab a small bucket and dunk it inside the box. It fills up with $k$ marbles and you pull it out. Inside the bucket is now a combination of class $k$. If you now put a lid on the bucket and shake it so that the marbles stay inside but shift their places around, you would still be considered to have the same combination.
>>
>
>>[!EXAMPLE]-
>>
>>Suppose $S = \{A, B, C, D\}$.
>>
>>The following are combinations of class $2$:
>>
>>$$
>>\{A, B\} \qquad \{B, C\} \qquad \{A, C\} \qquad \{B, D\} \qquad \{A, D\}
>>$$
>>
>>The following are combinations of class $3$:
>>
>>$$
>>\{A, B, C\} \qquad \{A, B, D\} \qquad \{A, C, D\}
>>$$
>>
>

>[!THEOREM] Theorem: Total Number of Combinations
>
>The total number of [combinations](Combinations.md) of $n$ elements of class $k$ can be calculated the number of [permutations](Permutations.md) of $n$, $k$ and $n - k$ elements as follows:
>
>$$
>\frac{P_n}{P_k \times P_{n-k}} = \frac{n!}{k! (n-k)!}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>C_n^k \qquad C_k^n \qquad \binom{n}{k} 
>>$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Combinations with Repetition

>[!DEFINITION] Definition: Combination with Repetition
>
>Let $S = \{s_1, \dotsc, s_n\}$ be a [set](../Set%20Theory/Sets.md).
>
>A **combination with repetition** of $S$ of class $k$ is a [multiset](../Set%20Theory/Multisets.md) with cardinality $k$ whose elements are elements of $S$.
>
>>[!EXAMPLE]-
>>
>>Let $S = \{1, 2, 3\}$.
>>
>>Some combinations with repetition of class $2$ are
>>
>>$$
>>\{1, 3\} \qquad \{2, 2\}
>>$$
>>
>>Some combinations with repetition of class $3$ are
>>
>>$$
>>\{1, 2, 3\} \qquad \{1, 2, 2\} \qquad \{3, 3, 2\} \qquad \{1, 1, 1\}
>>$$
>>
>>Some combinations with repetition of class $4$ are
>>
>>$$
>>\{3, 3, 3, 1\} \qquad \{2, 1, 1, 3\} \qquad \{2, 2, 2, 2\} \qquad \{1, 1, 2, 3\}
>>$$
>>
>

>[!THEOREM] Theorem: Total Number of Combinations with Repetition
>
>If $S$ is a [set](../Set%20Theory/Sets.md) with $n$ elements, then the total number of [combinations with repetition](Combinations.md#Combinations%20with%20Repetition) of class $k$, denoted by $\tilde{C}_n^k$ is the total number of [combinations without elements](Combinations.md#Combinations%20without%20Repetition) of $(n+k-1)$ elements of class $k$.
>
>$$
>\tilde{C}_n^k = C_{n+k-1}^k
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>