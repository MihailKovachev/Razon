---
tags:
    - topology
    - mathematics
---

# Closed Sets

>[!DEFINITION] Definition: Closed Set
>
>A [subset](../../Set%20Theory/Subsets.md) $S \subseteq X$ of a [topological space](./Topological%20Space.md) $X$ is **closed** if each point in its [complement](../../Set%20Theory/Set%20Difference.md) $X \setminus S$ has at least one [neighborhood](./Neighborhoods.md) which is [disjoint](../../Set%20Theory/Intersections.md) from $S$:
>
>$$\forall p \in X \setminus S: \exists N(p) \text{ with } N(p) \cap S = \varnothing$$
>

>[!THEOREM] Theorem: The Fundamental Properties of Closed Sets
>
>If $X$ is a [topological space](./Topological%20Space.md), then:
>
>    - The [empty set](../../Set%20Theory/Sets.md) $\varnothing$ and $X$ itself are [closed](#Closed%20Sets).
>    - If $\mathcal{S}$ is a [collection](../../Set%20Theory/Collections.md) of [closed sets](#Closed%20Sets), then its [intersection](../../Set%20Theory/Intersections.md) is also [closed](#Closed%20Sets).
>    - If $\mathcal{S}$ is a [finite](../../Set%20Theory/Cardinality.md) [collection](../../Set%20Theory/Collections.md) of [closed sets](#Closed%20Sets), then its [union](../../Set%20Theory/Unions.md) is also [closed](#Closed%20Sets).
>
>>[!PROOF]-
>>
>>We need to prove three things:
>>
>>- (I) The [empty set](../../Set%20Theory/Sets.md) $\varnothing$ and $X$ itself are [closed](#Closed%20Sets).
>>- (II) If $\mathcal{S}$ is a [collection](../../Set%20Theory/Collections.md) of [closed sets](#Closed%20Sets), then its [intersection](../../Set%20Theory/Intersections.md) is also [closed](#Closed%20Sets).
>>- (III) If $\mathcal{S}$ is a [finite](../../Set%20Theory/Cardinality.md) [collection](../../Set%20Theory/Collections.md) of [closed sets](#Closed%20Sets), then its [union](../../Set%20Theory/Unions.md) is also [closed](#Closed%20Sets).
>>
>>**Proof of (I):**
>>
>>**Proof of (II):**
>>
>>**Proof of (III):**
>>
>

>[!THEOREM] Theorem: Closed Sets via Open Sets
>
>Let $X$ be a [topological space](./Topological%20Space.md).
>
>A [subset](../../Set%20Theory/Subsets.md) $S \subseteq X$ is [closed](./Closed%20Sets.md) if and only if its [complement](../../Set%20Theory/Set%20Difference.md) $X \setminus S$ is [open](./Open%20Sets.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Closed Sets via Closure
>
>A [subset](../../Set%20Theory/Subsets.md) of  [topological space](./Topological%20Space.md) is [closed](./Closed%20Sets.md) if and only if it is equal to its own [closure](./Closure%20(Topology).md):
>
>$$S = \overline{S}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>