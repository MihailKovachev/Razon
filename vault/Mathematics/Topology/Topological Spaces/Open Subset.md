>[!DEFINITION] Definition: Open Subset
>
>Let $(X, \tau)$ be a [topological space](Topological%20Space.md).
>
>A [subset](../../Set%20Theory/Subset.md) of $X$ is **open** iff it is an element of $\tau$.
>

>[!THEOREM] Theorem: Union of Open Sets
>
>Let $(S, \tau)$ be a [topological space](Topological%20Space.md).
>
>The [union](../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) of any [collection](../../Set%20Theory/Collections/Collection.md) of [open subsets](Open%20Subset.md) is also open.
>
>>[!PROOF]-
>>
>>This follows directly from the definition of a [topology](Topology.md).
>>
>

>[!THEOREM] Theorem: Intersection of Open Sets
>
>Let $(S, \tau)$ be a [topological space](Topological%20Space.md).
>
>The [intersection](../../Set%20Theory/Collections/Intersection%20of%20a%20Collection.md) of any finite [collection](../../Set%20Theory/Collections/Collection.md) of [open sets](Open%20Subset.md) is also open.
>
>>[!PROOF]-
>>
>>We consider $n \ge 2$ arbitrary [open subsets](Open%20Subset.md) $U_1,\cdots, U_n$.
>>
>>For $n = 2$, the definition of the [topology](Topology.md) $\tau$ tells us that $U_1 \cap U_2 \in \tau$.
>>
>>Now suppose $U' = U_1 \cap \cdots \cap U_{n-1} \in \tau$. We have
>>
>>$$
>>\begin{align*}U_1 \cap \cdots \cap U_n &= (U_1 \cap \cdots \cap U_{n-1}) \cap U_n \\ U_1 \cap \cdots \cap U_n &= U' \cap U_n\end{align*}
>>$$
>>
>>Since $U_1 \cap \cdots \cap U_n$ is the intersection of two elements of $\tau$, it must itself be an element of $\tau$, Q.E.D.
>>
>
>^intersection-of-open-sets
>