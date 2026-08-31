---
title: Interior, Boundary, Exterior
tags:
  - topology
  - mathematics
---

# Interior, Boundary and Exterior

Every [subset](../Set%20Theory/Sets.md) $S$ of a [topological space](./Topological%20Spaces/Topological%20Space.md) $(X, \tau)$ divides $X$ into three [pairwise disjoint](../Set%20Theory/Intersections.md) [subsets](../Set%20Theory/Subsets.md) whose [union](../Set%20Theory/Unions.md) is $X$.

>[!DEFINITION] Definition: Interior Point
>
>Let $(X, \tau)$ be a [topological space](./Topological%20Spaces/Topological%20Space.md) $(X, \tau)$ and let $S$ be a [subset](../Set%20Theory/Subsets.md) of $X$.
>
>We say that $p \in X$ is an **interior point** of $S$ if it has a [neighborhood](./Topological%20Spaces/Topological%20Space.md#Neighborhoods) [contained](../Set%20Theory/Subsets.md) in $S$.
>
>>[!DEFINITION] Definition: Topological Interior
>>
>>The **(topological) interior** of $S$ is the [set](../Set%20Theory/Sets.md) of all its [interior points](./Interior,%20Boundary,%20Exterior.md):
>>
>>$$\{p \in X \mid \exists N(p) : N(p) \subseteq S \}$$
>>
>>>[!NOTATION]
>>>
>>>$$\mathring S \qquad S^\circ \qquad \operatorname{int} S \qquad \operatorname{int}_X S$$
>>>
>>
>

>[!DEFINITION] Definition: Boundary Point
>
>Let $(X, \tau)$ be a [topological space](./Topological%20Spaces/Topological%20Space.md) $(X, \tau)$ and let $S$ be a [subset](../Set%20Theory/Subsets.md) of $X$.
>
>We say that $p \in X$ is a **boundary point** of $S$ if every [neighborhood](./Topological%20Spaces/Topological%20Space.md#Neighborhoods) of $p$ [intersects](../Set%20Theory/Intersections.md) both $S$ and and its [complement](../Set%20Theory/Set%20Difference.md) $X \setminus S$.
>
>>[!DEFINITION] Definition: Topological Boundary
>>
>>The **(topological) boundary** of $S$ is the [set](../Set%20Theory/Sets.md) of all its [boundary points](./Interior,%20Boundary,%20Exterior.md).
>>
>>>[!NOTATION]
>>>
>>>$$\partial S \qquad \partial_X S \qquad \operatorname{Bd}_X S$$
>>>
>>
>

>[!DEFINITION] Definition: Exterior Point
>
>Let $(X, \tau)$ be a [topological space](./Topological%20Spaces/Topological%20Space.md) $(X, \tau)$ and let $S$ be a [subset](../Set%20Theory/Subsets.md) of $X$.
>
>We say that $p \in X$ is an **exterior point** of $S$ if it has a [neighborhood](./Topological%20Spaces/Topological%20Space.md) which contains no points of $S$.
>
>>[!DEFINITION] Definition: Topological Exterior
>>
>>The **(topological) exterior** of $S$ is the [set](../Set%20Theory/Sets.md) of all its [exterior points](./Interior,%20Boundary,%20Exterior.md):
>>
>>$$\{p \in X \mid \exists N(p) : N(p) \cap S = \varnothing \}$$
>>
>>>[!NOTATION]
>>>
>>>$$\operatorname{ext} S \qquad \operatorname{Ext} S$$
>>>
>>
>

![](./res/Interior,%20Boundary,%20Exterior.svg)

>[!THEOREM] Theorem: Union of Interior, Boundary and Exterior
>
>Let $(X, \tau)$ be a [topological space](./Topological%20Spaces/Topological%20Space.md).
>
>If $S$ is any [subset](../Set%20Theory/Subsets.md) of $X$, then $X$ is the [union](../Set%20Theory/Collections.md) of $S$'s [interior, boundary and exterior](./Interior,%20Boundary,%20Exterior.md):
>
>$$X = \mathop{\operatorname{int}} S \cup \partial S \cup \mathop{\operatorname{ext}} S$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Interior via Open Sets
>
>Let $(X, \tau)$ be a [topological space](./Topological%20Spaces/Topological%20Space.md) and let $S$ be a [subset](../Set%20Theory/Subsets.md) of $X$.
>
>The [interior](./Interior,%20Boundary,%20Exterior.md) of $S$ is the [union](../Set%20Theory/Collections.md) of all [open sets](./Topological%20Spaces/Topological%20Space.md#Open%20Sets) [contained](../Set%20Theory/Subsets.md) in $S$.
>
>$$\operatorname{int} S = \bigcup\{U \in \tau \mid U \subseteq S \}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Interior is a Subset
>
>Let $(X, \tau)$ be a [topological space](./Topological%20Spaces/Topological%20Space.md) and let $S$ be a [subset](../Set%20Theory/Subsets.md) of $X$.
>
>The [interior](./Interior,%20Boundary,%20Exterior.md) of $S$ is a [subset](../Set%20Theory/Subsets.md) of $S$:
>
>$$\operatorname{int} S \subseteq S$$
>
>>[!PROOF]-
>>
>>Suppose that $\operatorname{int} S$ is not a [subset](../Set%20Theory/Sets.md) of $S$. Then there must exist some $s \in \operatorname{int} S$ such that $s \notin S$. Since $s \in \operatorname{int} S$, there must exist some [open set](./Topological%20Spaces/Topological%20Space.md#Open%20Sets) $O$ such that $s \in O$ and $O \subseteq S$. However, $s \notin S$ implies that $O$ is not a [subset](../Set%20Theory/Sets.md) of $S$, which is a contradiction.
>>
>

>[!THEOREM] Theorem: Openness $\iff$ Interior
>
>Let $(X, \tau)$ be a [topological space](./Topological%20Spaces/Topological%20Space.md).
>
>A [subset](../Set%20Theory/Subsets.md) $S \subseteq X$ is [open](./Topological%20Spaces/Topological%20Space.md#Open%20Sets) if and only if it is equal to its own [interior](./Interior,%20Boundary,%20Exterior.md).
>
>$$S = \operatorname{int} S$$
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>
>>- (I) If $S$ is [open](./Topological%20Spaces/Topological%20Space.md#Open%20Sets), then $S = \operatorname{int} S$.
>>- (II) If $S = \operatorname{int} S$, then $S$ is [open](./Topological%20Spaces/Topological%20Space.md#Open%20Sets).
>>
>>**Proof of (I):**
>>
>>Suppose $S$ is [open](./Topological%20Spaces/Topological%20Space.md#Open%20Sets). Recall the definition of the [interior](./Interior,%20Boundary,%20Exterior.md) $\operatorname{int} S$:
>>
>>$$\operatorname{int} S \overset{\text{def}}{=} \bigcup \{O \subseteq S \mid O \text{ is open}\}$$
>>
>>Since $S\subseteq S$ and $S$ is [open](./Topological%20Spaces/Topological%20Space.md#Open%20Sets), we know that $S \in \{O \subseteq S \mid O \text{ is open}\}$ and thus $S \subseteq \operatorname{int} S$. However, the [interior](./Interior,%20Boundary,%20Exterior.md) is a [subset](../Set%20Theory/Sets.md) of $S$. Since $S \subseteq \operatorname{int} S$ and $\operatorname{int} S \subseteq S$, we know deduce that $S = \operatorname{int} S$.
>>
>>**Proof of (II):**
>>
>>Suppose that $S = \operatorname{int} S$. Since the [interior](./Interior,%20Boundary,%20Exterior.md) $\operatorname{int} S$ is a [union](../Set%20Theory/Collections.md) of [open sets](./Topological%20Spaces/Topological%20Space.md#Open%20Sets), it is itself [open](./Topological%20Spaces/Topological%20Space.md#Open%20Sets). Therefore, $S$ is [open](./Topological%20Spaces/Topological%20Space.md#Open%20Sets).
>>
>

>[!THEOREM] Theorem: Exterior via Open Sets
>
>Let $(X, \tau)$ be a [topological space](./Topological%20Spaces/Topological%20Space.md) and let $S$ be a [subset](../Set%20Theory/Subsets.md) of $X$.
>
>The [exterior](./Interior,%20Boundary,%20Exterior.md) of $S$ is the [union](../Set%20Theory/Unions.md) of all [open sets](./Topological%20Spaces/Topological%20Space.md#Open%20Sets) which are [disjoint](../Set%20Theory/Intersections.md) from $S$:
>
>$$\operatorname{ext} S = \bigcup\{U \in \tau \mid U \cap S = \varnothing\}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>