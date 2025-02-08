>[!DEFINITION] Definition: Linear Independence
>
>Let $\mathbf{v}_1, \cdots, \mathbf{v}_n$ be [vectors](Vector.md) in some [vector space](Vector%20Space.md) $(V,F,+,\cdot$).
>
>We say that $\mathbf{v}_1, \cdots, \mathbf{v}_n$ are **linearly independent** iff
>
>$$
>c_1\mathbf{v}_1 + \cdots + c_n\mathbf{v}_n = \mathbf{0} \implies c_1 = \cdots = c_n = 0
>$$
>
>>[!DEFINITION] Definition: Maximality
>>
>>A [set](../../../Set%20Theory/index.md) of [linearly independent](Linear%20Independence.md) [vectors](Vector.md) $S = \{ \mathbf{v}_1, \mathbf{v}_2, \cdots \}$ is **maximal** if there is no $\mathbf{v} \in V \setminus S$ such that $S \cup \{ \mathbf{v} \}$ are still [linearly independent](Linear%20Independence.md). 
>>
>

>[!THEOREM] Theorem: Size Limit for Linearly Independent Sets
>
>The number of elements in any [set](../../../Set%20Theory/index.md) $I$ of [linearly independent](Linear%20Independence.md) [vectors](Vector.md) from a [finitely generated](Vector%20Spaces/Spanning%20Set%20(Generator).md) [vector space](Vector%20Space.md) $(V,F,+,\cdot)$ is always less than or equal to the [dimension](Bases/Dimension.md) of $V$.
>
>$$
>|I| \le \dim(V)
>$$
>
>>[!PROOF]-
>>
>>Let $B = \{\mathbf{b}_1, \cdots, \mathbf{b}_n,\}$ be a [basis](Bases/Basis.md) of $V$ and let $I = \{\mathbf{v}_1, \cdots, \mathbf{v}_m\}$ be a [set](../../../Set%20Theory/index.md) of [linearly independent](Linear%20Independence.md) [vectors](Vector%20Space.md).
>>
>>According to the [Steinitz exchange lemma](Bases/Steinitz%20Exchange%20Lemma.md) there are $n-m$ [vectors](Vector%20Space.md) in $B$ which form a basis with the vectors from $I$. This means that $n-m$ cannot be negative and thus the proof is complete.
>>
>