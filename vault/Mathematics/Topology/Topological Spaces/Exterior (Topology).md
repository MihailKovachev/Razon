---
tags:
    - topology
    - mathematics
---

# Exterior (Topology)

>[!DEFINITION] Definition: Exterior Point
>
>Let $S \subseteq X$ be a [subset](../../Set%20Theory/Subsets.md) of a [topological space](./Topological%20Space.md) $X$.
>
>We say that $p \in X$ is an **exterior point** of $S$ if it has a [neighborhood](./Neighborhoods.md) which is [disjoint](../../Set%20Theory/Intersections.md) from $S$.
>
>$$\exists N(p): N(p) \cap S = \varnothing$$
>
>>[!DEFINITION] Definition: Topological Exterior
>>
>>The **(topological) exterior** of $S$ is the [set](../../Set%20Theory/Sets.md) of all its [exterior points](./Exterior%20(Topology).md).
>>
>>>[!NOTATION]
>>>
>>>$$\operatorname{ext} S \qquad \operatorname{ext}_X S$$
>>>
>>
>

>[!THEOREM] Theorem: Exterior via Open Sets
>
>Let $S \subseteq X$ be a [subset](../../Set%20Theory/Subsets.md) of a [topological space](./Topological%20Space.md) $X$.
>
>The [exterior](./Exterior%20(Topology).md) of $S$ is the [union](../../Set%20Theory/Unions.md) of all [open sets](./Open%20Sets.md) which are [disjoint](../../Set%20Theory/Intersections.md) from $S$:
>
>$$\operatorname{ext} S = \bigcup \{U \subseteq X \mid U \text{ is open and } U \cap S = \varnothing\}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>