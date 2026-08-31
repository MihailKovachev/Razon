---
tags:
    - topology
    - mathematics
---

# Interior (Topology)

>[!DEFINITION] Definition: Interior Point
>
>Let $S \subseteq X$ be a [subset](../../Set%20Theory/Subsets.md) of a [topological space](./Topological%20Space.md) $X$.
>
>We say that $p \in X$ is an **interior point** of $S$ if it has a [neighborhood](./Neighborhoods.md) [contained](../../Set%20Theory/Subsets.md) in $S$:
>
>$$\exists N(p): N(p) \subseteq S$$
>
>>[!DEFINITION] Definition Topological Interior
>>
>>The **(topological) interior** of $S$ is the [set](../../Set%20Theory/Sets.md) of all its [interior points](./Interior%20(Topology).md).
>>
>>>[!NOTATION]
>>>
>>>$$\operatorname{int} S \qquad \operatorname{int}_X S \qquad \mathring{S}$$
>>>
>>
>

>[!THEOREM] Theorem: Interior via Open Sets
>
>Let $S \subseteq X$ be a [subset](../../Set%20Theory/Subsets.md) of a [topological space](./Topological%20Space.md) $X$.
>
>The [interior](./Interior%20(Topology).md) of $S$ is the [union](../../Set%20Theory/Unions.md) of all [open sets](./Open%20Sets.md) [contained](../../Set%20Theory/Subsets.md) in $S$:
>
>$$\operatorname{int} S = \bigcup \{U \subseteq X \mid U \text{ is open and } U \subseteq S\}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Interior is a Subset
>
>Let $S \subseteq X$ be a [subset](../../Set%20Theory/Subsets.md) of a [topological space](./Topological%20Space.md) $X$.
>
>The [interior](./Interior%20(Topology).md) of $S$ is a [subset](../../Set%20Theory/Subsets.md) of $S$:
>
>$$\operatorname{int} S \subseteq S$$
>
>>[!PROOF]-
>>
>>TODO
>>
>