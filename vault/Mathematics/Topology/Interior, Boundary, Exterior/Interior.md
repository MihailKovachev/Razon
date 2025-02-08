---
title: Interior
tags:
  - topology
  - mathematics
---

# Interior

>[!DEFINITION] Definition: Interior of a Set
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces/index.md).
>
>The **interior** of a [set](../../../Set%20Theory/index.md) $S \subseteq X$ is the [union](../../../Set%20Theory/Collections/Operations%20with%20Collections.md) of all [open sets](../Topological%20Spaces/Open%20Sets.md) contained in $S$.
>
>$$
>\bigcup\{I \subseteq S \mid I \in \tau \}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>\mathring S \qquad S^\circ \qquad \operatorname{int} S \qquad \operatorname{int}_X S
>>$$
>>
>
>^interior
>

>[!DEFINITION] Definition: Interior Point
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces/index.md) and let $S$ be a [subset](../../../Set%20Theory/index.md) of $X$.
>
>A point $x \in X$ is an **interior point** of $S$ iff $x$ belongs to the [interior](Interior.md) of $S$.
>
>>[!THEOREM] Theorem
>>
>>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces/index.md) and let $S$ be a [subset](../../../Set%20Theory/index.md) of $X$.
>>
>>A point $p \in X$ is an [interior point](Interior.md) of $S$ if and only if it has a [neighbourhood](../Topological%20Spaces/Neighborhoods.md) contained in $S$.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

## Properties

>[!THEOREM] Theorem: Interior is a Subset
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces/index.md).
>
>The [interior](Interior.md) $\operatorname{Int} S$ of each [subset](../../../Set%20Theory/index.md) $S \subseteq X$ is a [subset](../../../Set%20Theory/index.md) of $S$.
>
>$$
>\operatorname{Int} S \subseteq S
>$$
>
>>[!PROOF]-
>>
>>Suppose that $\operatorname{int} S$ is not a [subset](../../../Set%20Theory/index.md) of $S$. Then there must exist some $s \in \operatorname{int} S$ such that $s \notin S$. Since $s \in \operatorname{int} S$, there must exist some [open set](../Topological%20Spaces/Open%20Sets.md) $O$ such that $s \in O$ and $O \subseteq S$. However, $s \notin S$ implies that $O$ is not a [subset](../../../Set%20Theory/index.md) of $S$, which is a contradiction.
>>
>
>^interior-is-a-subset
>