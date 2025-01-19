>[!DEFINITION] Definition: Combination
>
>Let $S$ be a finite set.
>
>A **combination** of class $k$ is a [subset](../Set%20Theory/Subset.md) of $S$ with $k$ elements.
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
>>\{A, B, C\} \qquad \{A, B, D\} \{A, C, D\}
>>$$
>>
>

>[!THEOREM] Theorem: Total Number of Combinations
>
>The total number of [combinations](Combination.md) of $n$ elements of class $k$ can be calculated the number of [permutations](Permutation.md) of $n$, $k$ and $n - k$ elements as follows:
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