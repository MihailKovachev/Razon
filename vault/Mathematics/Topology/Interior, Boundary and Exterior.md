---
title: Boundary
tags:
  - topology
  - mathematics
---

Every [subset](../Set%20Theory/Subsets.md) of $S$ of a [topological space](Topological%20Spaces.md) $(X, \tau)$ divides it into three different regions such that $X$ is always equal to the [union](../Set%20Theory/Collections/Operations%20with%20Collections.md) of those regions.

# Interior

>[!DEFINITION] Definition: Interior of a Set
>
>Let $(X, \tau)$ be a [topological space](Topological%20Spaces.md) and let $S$ be a [subset](../../Set%20Theory/Subsets.md) of $X$.
>
>A point $p \in X$ is an **interior point** of $S$ if and only if it has a [neighbourhood](Topological%20Spaces.md#Neighborhoods) $N(p)$ contained in $S$. The **interior** of $S$ is the [set](../Set%20Theory/Sets.md) of all of its [interior points](Interior,%20Boundary%20and%20Exterior.md).
>
>$$
>\{p \in X \mid \exists N(p) : N(p) \subseteq S \}
>$$
>
>>[!NOTATION]
>>
>>$$
>>\mathring S \qquad S^\circ \qquad \operatorname{int} S \qquad \operatorname{int}_X S
>>$$
>>
>

## Characterizations

>[!THEOREM]- Theorem: Interior via Open Sets
>
>Let $(X, \tau)$ be a [topological space](Topological%20Spaces.md).
>
>The [interior](Interior,%20Boundary%20and%20Exterior.md#Interior) of a [subset](../Set%20Theory/Subsets.md) $S \subseteq X$ is the [union](../../../Set%20Theory/Collections/Operations%20with%20Collections.md) of all [open sets](Topological%20Spaces.md#Open%20Sets) contained in $S$.
>
>$$
>\operatorname{int} S = \bigcup\{I \subseteq S \mid I \in \tau \}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Properties

>[!THEOREM]- Theorem: Interior is a Subset
>
>Let $(X, \tau)$ be a [topological space](Topological%20Spaces.md).
>
>The [interior](Interior,%20Boundary%20and%20Exterior.md#Interior) $\operatorname{Int} S$ of each [subset](../../Set%20Theory/Subsets.md) $S \subseteq X$ is a [subset](../../Set%20Theory/Subsets.md) of $S$.
>
>$$
>\operatorname{Int} S \subseteq S
>$$
>
>>[!PROOF]-
>>
>>Suppose that $\operatorname{int} S$ is not a [subset](../../Set%20Theory/Subsets.md) of $S$. Then there must exist some $s \in \operatorname{int} S$ such that $s \notin S$. Since $s \in \operatorname{int} S$, there must exist some [open set](Topological%20Spaces.md#Open%20Sets) $O$ such that $s \in O$ and $O \subseteq S$. However, $s \notin S$ implies that $O$ is not a [subset](../../Set%20Theory/Subsets.md) of $S$, which is a contradiction.
>>
>

# Boundary

>[!DEFINITION] Definition: Boundary
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces.md) and let $S$ be a [subset](../../Set%20Theory/Sets.md) of $X$.
>
>The **boundary** of $S$ is the [set](../../Set%20Theory/Sets.md) of all points $x \in X$ such that every [neighbourhood](../Topological%20Spaces.md) of $x$ contains at least one point of $S$ and at least one point of its [complement](../../Set%20Theory/Complement.md) $X \setminus S$.
>
>>[!NOTATION]-
>>
>>$$
>>\partial S \qquad \partial_X S \qquad \operatorname{Bd}_X S
>>$$
>>
>

>[!DEFINITION] Definition: Boundary Point
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces.md) and let $S$ be a [subset](../../Set%20Theory/Sets.md) of $X$.
>
>A point $p \in X$ is a **boundary point** of $S$ iff it belongs to the [boundary](Boundary.md) of $S$.
>
>$$
>p \in \partial S
>$$
>

# Exterior

>[!DEFINITION] Definition: Exterior of a Set
>
>Let $(X, \tau_X)$ be a [topological space](../Topological%20Spaces.md) and let $S$ be a [subset](../../Set%20Theory/Sets.md) of $X$.
>
>The **exterior** of $S$ is the [complement](../../../Set%20Theory/Complement.md) of its [closure](Closure.md) in $X$.
>
>$$
>X \setminus \overline{S}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>\operatorname{ext} S \qquad \operatorname{Ext} S
>>$$
>>
>
>^exterior
>

>[!DEFINITION] Definition: Exterior Point
>
>Let $(X, \tau_X)$ be a [topological space](../Topological%20Spaces.md) and let $S$ be a [subset](../../Set%20Theory/Sets.md) of $X$.
>
>A point $p \in X$ is an **exterior point** of $S$ iff it belongs to the [exterior](Exterior.md) of $S$.
>

## Properties


>[!THEOREM] Theorem: Exterior is Closed
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces.md).
>
>The [](Exterior.md#^exterior) $\operatorname{Ext} S$ of each [subset](../../Set%20Theory/Sets.md) $S \subseteq X$ is [closed](../Topological%20Spaces.md).
>
>>[!PROOF]-
>>
>>The [exterior](Exterior.md) of $S$ is the [complement](../../../Set%20Theory/Complement.md) of its [closure](Closure.md) and since the [closure](Closure.md) is a [closed set](../Topological%20Spaces.md), the [exterior](Exterior.md) is [open](../Topological%20Spaces.md).
>>
>