>[!THEOREM] Theorem: Topological Subspace
>
>Let $(X, \tau_X)$ be a [topological space](../Topological%20Spaces/Topological%20Space.md).
>
>For every [non-empty](../../Set%20Theory/The%20Empty%20Set.md) [subset](../../Set%20Theory/Subset.md) $S$ of $X$, the [collection](../../Set%20Theory/Collections/Collection.md)
>
>$$
>\tau_S \overset{\text{def}}{=} \{O \cap S \mid O \in \tau_X\}
>$$
>
>is a [topology](../Topological%20Spaces/Topology.md) on $S$.
>
>>[!PROOF]-
>>
>>We need to prove three things:
>>- (I) $S \in \tau_S$ and $\varnothing \in \tau_S$.
>>- (II) $\tau_S$ is closed under arbitrary unions.
>>- (III) $\tau_S$ is closed under finite intersections.
>>
>>**Proof of (I):**
>>
>>This follows from the fact that $\varnothing = S \cap \varnothing$ and $S = S \cap X$.
>>
>>**Proof of (II):**
>>
>>Let $\mathcal{U}$ be an arbitrary [subset](../../Set%20Theory/Subset.md) of $\tau_S$. By definition, for each $U \in \mathcal{U}$ there exists some $O_U \in \tau_X$ such that $U = O_U \cap S$.  Then
>>
>>$$
>>\bigcup \mathcal{U} = \bigcup_{U \in \mathcal{U}} (O_U \cap S) = \left(\bigcup_{U \in \mathcal{U}} O_U\right) \cap S
>>$$
>>
>>Since $\bigcup_{U \in \mathcal{U}} O_U$ is a [union](../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) of [open sets](../Topological%20Spaces/Open%20Subset.md), it is itself [open](../Topological%20Spaces/Open%20Subset.md), i.e. $\bigcup_{U \in \mathcal{U}} O_U \in \tau_X$. Therefore $\left(\bigcup_{U \in \mathcal{U}} O_U\right) \cap S$ is in $\tau_S$.
>>
>>**Proof of (III):**
>>
>>Consider the [intersection](../../Set%20Theory/Collections/Intersection%20of%20a%20Collection.md) $U_1 \cap \cdots \cap U_n$ where $U_1,\cdots, U_n \in \tau_S$. By definition, for each $U_k$ there exists some $O_k \in \tau_X$ such that $U_k = O_k \cap S$. This means that
>>
>>$$
>>U_1 \cap \cdots \cap U_n = (O_1 \cap S) \cap \cdots \cap (O_n \cap S) = (O_1 \cap \cdots \cap O_n) \cap S
>>$$
>>
>>Since $(O_1 \cap \cdots \cap O_n)$ is an [intersection](../../Set%20Theory/Collections/Intersection%20of%20a%20Collection.md) of finitely many [open sets](../Topological%20Spaces/Open%20Subset.md), it is itself [open](../Topological%20Spaces/Open%20Subset.md). Therefore, $U_1 \cap \cdots \cap U_n \in \tau_S$.
>>
>
>>[!DEFINITION] Definition: Topological Subspace
>>
>>The [topological space](../Topological%20Spaces/Topological%20Space.md) $(S, \tau_S)$ is known as a **subspace** of $(X,\tau_X)$.
>>
>