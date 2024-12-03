>[!THEOREM]
>
>Let $(X, \tau)$ be a [topological space](Topological%20Space.md).
>
>A [subset](../../Set%20Theory/Subset.md) $U \subseteq X$ is [open](Open%20Subset.md) if and only if each $x \in U$ has a [neighbourhood](Neighbourhoods.md) $N(x)$ such that $N(x) \subseteq U$.
>
>>[!PROOF]-
>>
>>If $U$ is [open](Open%20Subset.md), then $U$ is, by definition, a [neighbourhood](Neighbourhoods.md) of every $x \in U$.
>>
>>If there exists a [neighbourhood](Neighbourhoods.md) $N(x)$ of each $x$ such that $N(x) \subseteq U$, then inside each neighbourhood $N(x)$ there exists, by definition, an open set $O(x) \subseteq N(x)$ which contains $x$. Since $N(x) \subseteq U$, we have $O(x) \subseteq N(x) \subseteq U$. This means that we can construct $U$ as the [union](../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) of these open sets $O(x)$.
>>
>>$$
>>U = \bigcup_{x \in U} O(x)
>>$$
>>
>>Since this is a union of open sets, i.e. it is a union of a subset of the [topology](Topology.md) $\tau$, we have that $U \in \tau$. 
>>
>

>[!THEOREM] Theorem
>
>Let $(X, \tau)$ be a [topological space](Topological%20Space.md).
>
>A [subset](../../Set%20Theory/Subset.md) $U \subseteq X$ is [open](Open%20Subset.md) if and only if for each $x \in U$ there exists an open set $V$ such that $V \subseteq U$ and $x \in V$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem
>
>Let $(X, \tau)$ be a [topological space](Topological%20Space.md).
>
>A [subset](../../Set%20Theory/Subset.md) $S \subseteq X$ is [open](Open%20Subset.md) if and only if it is equal to its own [interior](../Interior,%20Exterior,%20Boundary/Interior/Interior.md).
>
>$$
>S = \operatorname{int} S
>$$
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (I) If $S$ is [open](Open%20Subset.md), then $S = \operatorname{int} S$.
>>- (II) If $S = \operatorname{int} S$, then $S$ is [open](Open%20Subset.md).
>>
>>**Proof of (I):**
>>
>>Suppose $S$ is [open](Open%20Subset.md). Recall the definition of the [interior](../Interior,%20Exterior,%20Boundary/Interior/Interior.md) $\operatorname{int} S$:
>>
>>$$
>>\operatorname{int} S \overset{\text{def}}{=} \bigcup \{O \subseteq S \mid O \text{ is open}\}
>>$$
>>
>>Since $S\subseteq S$ and $S$ is [open](Open%20Subset.md), we know that $S \in \{O \subseteq S \mid O \text{ is open}\}$ and thus $S \subseteq \operatorname{int} S$. However, the [interior](../Interior,%20Exterior,%20Boundary/Interior/Interior.md) is a [subset](../../Set%20Theory/Subset.md) of $S$. Since $S \subseteq \operatorname{int} S$ and $\operatorname{int} S \subseteq S$, we know deduce that $S = \operatorname{int} S$.
>>
>>**Proof of (II):**
>>
>>Suppose that $S = \operatorname{int} S$. Since the [interior](../Interior,%20Exterior,%20Boundary/Interior/Interior.md) $\operatorname{int} S$ is a [union](../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) of [open sets](Open%20Subset.md), it is itself [open](Open%20Subset.md). Therefore, $S$ is [open](Open%20Subset.md).
>>
>