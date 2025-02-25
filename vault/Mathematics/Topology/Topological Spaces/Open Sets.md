---
title: Open Sets
tags:
  - topology
  - mathematics
---

# Open Sets

>[!DEFINITION] Definition: Open Subset
>
>Let $(X, \tau)$ be a [topological space](./index.md).
>
>A [subset](../../Set%20Theory/Sets.md) of $X$ is **open** iff it is an element of $\tau$.
>

## Openness Criteria

>[!THEOREM]
>
>Let $(X, \tau)$ be a [topological space](./index.md).
>
>A [subset](../../Set%20Theory/Sets.md) $U \subseteq X$ is [open](Open%20Sets.md) if and only if each $x \in U$ has a [neighbourhood](Neighborhoods.md) $N(x)$ such that $N(x) \subseteq U$.
>
>>[!PROOF]-
>>
>>If $U$ is [open](Open%20Sets.md), then $U$ is, by definition, a [neighbourhood](Neighborhoods.md) of every $x \in U$.
>>
>>If there exists a [neighbourhood](Neighborhoods.md) $N(x)$ of each $x$ such that $N(x) \subseteq U$, then inside each neighbourhood $N(x)$ there exists, by definition, an open set $O(x) \subseteq N(x)$ which contains $x$. Since $N(x) \subseteq U$, we have $O(x) \subseteq N(x) \subseteq U$. This means that we can construct $U$ as the [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of these open sets $O(x)$.
>>
>>$$
>>U = \bigcup_{x \in U} O(x)
>>$$
>>
>>Since this is a union of open sets, i.e. it is a union of a subset of the [topology](./index.md) $\tau$, we have that $U \in \tau$. 
>>
>

>[!THEOREM] Theorem
>
>Let $(X, \tau)$ be a [topological space](./index.md).
>
>A [subset](../../Set%20Theory/Sets.md) $U \subseteq X$ is [open](Open%20Sets.md) if and only if for each $x \in U$ there exists an open set $V$ such that $V \subseteq U$ and $x \in V$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem
>
>Let $(X, \tau)$ be a [topological space](./index.md).
>
>A [subset](../../Set%20Theory/Sets.md) $S \subseteq X$ is [open](Open%20Sets.md) if and only if it is equal to its own [interior](../Interior,%20Boundary,%20Exterior/Interior.md).
>
>$$
>S = \operatorname{int} S
>$$
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (I) If $S$ is [open](Open%20Sets.md), then $S = \operatorname{int} S$.
>>- (II) If $S = \operatorname{int} S$, then $S$ is [open](Open%20Sets.md).
>>
>>**Proof of (I):**
>>
>>Suppose $S$ is [open](Open%20Sets.md). Recall the definition of the [interior](../Interior,%20Boundary,%20Exterior/Interior.md) $\operatorname{int} S$:
>>
>>$$
>>\operatorname{int} S \overset{\text{def}}{=} \bigcup \{O \subseteq S \mid O \text{ is open}\}
>>$$
>>
>>Since $S\subseteq S$ and $S$ is [open](Open%20Sets.md), we know that $S \in \{O \subseteq S \mid O \text{ is open}\}$ and thus $S \subseteq \operatorname{int} S$. However, the [interior](../Interior,%20Boundary,%20Exterior/Interior.md) is a [subset](../../Set%20Theory/Sets.md) of $S$. Since $S \subseteq \operatorname{int} S$ and $\operatorname{int} S \subseteq S$, we know deduce that $S = \operatorname{int} S$.
>>
>>**Proof of (II):**
>>
>>Suppose that $S = \operatorname{int} S$. Since the [interior](../Interior,%20Boundary,%20Exterior/Interior.md) $\operatorname{int} S$ is a [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of [open sets](Open%20Sets.md), it is itself [open](Open%20Sets.md). Therefore, $S$ is [open](Open%20Sets.md).
>>
>

## Properties

>[!THEOREM] Theorem: Union of Open Sets
>
>Let $(S, \tau)$ be a [topological space](./index.md).
>
>The [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of any [collection](../../Set%20Theory/Collections/index.md) of [open subsets](Open%20Sets.md) is also open.
>
>>[!PROOF]-
>>
>>This follows directly from the definition of a [topology](./index.md).
>>
>

>[!THEOREM] Theorem: Intersection of Open Sets
>
>Let $(S, \tau)$ be a [topological space](./index.md).
>
>The [intersection](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of any finite [collection](../../Set%20Theory/Collections/index.md) of [open sets](Open%20Sets.md) is also open.
>
>>[!PROOF]-
>>
>>We consider $n \ge 2$ arbitrary [open subsets](Open%20Sets.md) $U_1,\cdots, U_n$.
>>
>>For $n = 2$, the definition of the [topology](./index.md) $\tau$ tells us that $U_1 \cap U_2 \in \tau$.
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