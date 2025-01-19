>[!DEFINITION] Definition: Variation of a Finite Set
>
>Let $S$ be a finite [set](../Set%20Theory/Set.md).
>
>A **variation** of class $k$ is a [permutation](Permutation.md) of a [subset](../Set%20Theory/Subset.md) of $S$ with $k$ elements.
>
>>[!NOTE] Note: Terminology
>>
>>If $S$ has $n$ elements, we also say a "variation of $n$ elements of class $k$".
>>
>>Variations of class $k$ are unfortunately also called permutations of class $k$.
>>
>
>>[!INTUITION]-
>>
>>A variation of class $k$ is a way to arrange exactly $k$ of the elements of $S$. You can also think of it as a way to choose $k$ elements of $S$ in a specific order. If you pick the same $k$ elements but in a different order, you will have different variations.
>>
>>Since a set does not contain duplicate elements, repetitions are not allowed - you cannot choose the same element from $S$ multiple times in the same variation.
>>
>
>>[!EXAMPLE]-
>>
>>Suppose $S = \{A, B, C, D, E\}$.
>>
>>The following are different variations of class 3:
>>
>>$$
>>(A, D, E) \qquad (E, D, A) \qquad (C, A, E) \qquad (D, B, C) \qquad (B, D, A)
>>$$
>>
>>The following are different variations of class 4:
>>
>>$$
>>(A, D, C, B) \qquad (C, B, A, D) \qquad (E, D, A, B)
>>$$
>>
>>The following are *not* variations:
>>
>>$$
>>(A, A, C, B) \qquad (A, B, C, D, E, C) 
>>$$
>>
>

>[!THEOREM] Theorem: Number of Variations
>
>The total number of [variations](Variation.md) of $n$ elements of class $k$ is 
>
>$$
>n \times (n - 1) \times (n - 2) \times \cdots \times (n - (k - 1))
>$$
>
>It is also given by the ratio of the total number of [permutations](Permutation.md) of $n$ elements to the total number of [permutations](Permutation.md) of $n-k$ elements.
>
>$$
>\frac{P_n}{P_{n - k}} = \frac{n!}{(n - k)!}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>V_n^k \qquad V_k^n \qquad P_n^k \qquad P_k^n
>>$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>