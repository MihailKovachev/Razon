---
tags:
    - topology
    - mathematics
---

# Closure (Topology)

>[!DEFINITION] Definition: Adherent Point
>
>Let $X$ be a [topological space](./Topological%20Space.md) and let $S$ be a [subset](../../Set%20Theory/Subsets.md) of $X$.
>
>We say that $p \in X$ is an **adherent point** / **closure point** of $S$ if every [neighborhood](./Neighborhoods.md) of $p$ [intersects](../../Set%20Theory/Intersections.md) $S$.
>
>$$\forall N(p): N(p) \cap S \ne \varnothing$$
>
>>[!DEFINITION] Definition: Closure
>>
>>The **(topological) closure** of $S$ is the [set](../../Set%20Theory/Sets.md) of all its [adherent points](./Closure%20(Topology).md).
>>
>>>[!NOTATION]
>>>
>>>$$\overline{S}$$
>>>
>>
>

>[!THEOREM] Theorem: Closure via Interior and Boundary
>
>Let $X$ be a [topological space](./Topological%20Space.md) and let $S$ be a [subset](../../Set%20Theory/Subsets.md) of $X$.
>
>The [closure](./Closure%20(Topology).md) of $S$ is the [union](../../Set%20Theory/Unions.md) of $S$'s [iinterior](./Interior%20(Topology).md) and [boundary](./Boundary%20(Topology).md):
>
>$$\overline{S} = \operatorname{int} S \cup \partial S$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Closure is Closed
>
>The [closure](./Closure%20(Topology).md) of a [subset](../../Set%20Theory/Subsets.md) $S \subseteq X$ of a [topological space](./Topological%20Space.md) $X$ is always [closed](./Closed%20Sets.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Closure is a Superset
>
>Every [subset](../../Set%20Theory/Subsets.md) $S \subseteq X$ of a [topological space](./Topological%20Space.md) $X$ is [contained](../../Set%20Theory/Subsets.md) in its own [closure](./Closure%20(Topology).md):
>
>$$S \subseteq \overline{S}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Idempotence of Closure
>
>The [closure](./Closure%20(Topology).md) of the [closure](./Closure%20(Topology).md) a [subset](../../Set%20Theory/Subsets.md) $S \subseteq X$ of a [topological space](./Topological%20Space.md) $X$ is always still the [closure](./Closure%20(Topology).md) of $S$:
>
>$$\overline{\overline{S}} = \overline{S}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Closure of Union
>
>The [closure](./Closure%20(Topology).md) of the [union](../../Set%20Theory/Unions.md) a [finite](../../Set%20Theory/Cardinality.md) [collection](../../Set%20Theory/Collections.md) of [subsets](../../Set%20Theory/Subsets.md) of a [topological space](./Topological%20Space.md) $X$ is the [union](../../Set%20Theory/Unions.md) of the [closures](./Closure%20(Topology).md) of its elements:
>
>$$\overline{S_1\cup \cdots \cup S_n} = \overline{S_1} \cup \cdots \cup \overline{S_n}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>