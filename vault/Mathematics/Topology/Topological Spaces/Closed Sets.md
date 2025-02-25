---
title: Closed Sets
tags:
  - topology
  - mathematics
---

# Closed Sets

>[!DEFINITION] Definition: Closed Set
>
>Let $(S, \tau)$ be a [topological space](./index.md).
>
>A [subset](../../Set%20Theory/Sets.md) $U$ of $S$ is **closed** if its [complement](../../Set%20Theory/Complement.md) $S \setminus U$ is an [open set](Open%20Sets.md).
>
>>[!THEOREM]
>>
>>Let $(S, \tau)$ be a [topological space](./index.md).
>>
>>A [subset](../../Set%20Theory/Sets.md) $C \subseteq S$ is [closed](Closed%20Sets.md) if and only if for each $x$ in its [complement](../../Set%20Theory/Complement.md) $S \setminus C$ there exists a [neighbourhood](Neighborhoods.md) $N$ of $x$ such that $N \subseteq S \setminus C$.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

## Closedness Criteria

>[!THEOREM]+
>
>Let $(X, \tau)$ be a [topological space](./index.md).
>
>A [subset](../../Set%20Theory/Sets.md) $S \subseteq X$ is [closed](Closed%20Sets.md) if and only if it is equal to its own [closure](../Interior,%20Boundary,%20Exterior/Closure.md).
>
>>[!PROOF]-
>>
>>We have to prove two things:
>>- (I) If $S$ is [closed](Closed%20Sets.md), then $S = \overline{S}$.
>>- (II) If $S = \overline{S}$, then $S$ is [closed](Closed%20Sets.md).
>>
>>**Proof of (I):**
>>
>>TODO
>>
>>**Proof of (II):**
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Limit Points of Closed Subsets
>
>Let $(X, \tau)$ be a [topological space](./index.md).
>
>A [subset](../../Set%20Theory/Sets.md) $S \subseteq X$ is [closed](Closed%20Sets.md) if and only if it contains all of its [limit points](../Interior,%20Boundary,%20Exterior/Accumulation%20Point.md).
>
>>[!PROOF]-
>>
>>We need to prove two things separately:
>>- (I) If $S$ is [closed](Closed%20Sets.md), then every [limit point](../Interior,%20Boundary,%20Exterior/Accumulation%20Point.md) of $S$ lies in $S$.
>>- (II) If $S$ contains all of its [limit points](../Interior,%20Boundary,%20Exterior/Accumulation%20Point.md), then it is [closed](Closed%20Sets.md).
>>
>>**Proof of (I):**
>>
>>We prove this by contradiction. Suppose that $S$ is [closed](Closed%20Sets.md) and there exists a [limit point](../Interior,%20Boundary,%20Exterior/Accumulation%20Point.md) $p$ of $S$ which lies outside of $S$, i.e. $p \in X \setminus S$. We know that $X \setminus S$ is [open](Open%20Sets.md) because it is the [complement](../../Set%20Theory/Complement.md) of a [closed set](Closed%20Sets.md). However, since $p$ is a [limit point](../Interior,%20Boundary,%20Exterior/Accumulation%20Point.md) of $S$, every [open set](Open%20Sets.md) which contains $p$ must also contain an element of $S$. This implies that $X \setminus S$ contains an element of $S$ which is a contradiction.
>>
>>**Proof of (II):**
>>
>>Suppose that $S$ contains all of its [limit points](../Interior,%20Boundary,%20Exterior/Accumulation%20Point.md). This means that there are no points $p \in X\setminus S$ such that every [open set](Open%20Sets.md) $U$ which contains $p$ also contains another element of $S$. Alternatively, this means that each $p \in X \setminus S$ is contained in some [open set](Open%20Sets.md) $U_p$ such that $U_p \cap S = \varnothing$, i.e. $U_p \subseteq X \setminus S$. Therefore, the [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) $\bigcup_{p \in X \setminus S} U_p$ is a [subset](../../Set%20Theory/Sets.md) of $X \setminus S$ and, since it contains every $p \in X \setminus S$, it means that $\bigcup_{p \in X \setminus S} U_p = X \setminus$. Since $X \setminus S$ is a [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of [open sets](Open%20Sets.md), it is itself [open](Open%20Sets.md) and so $S$ is [closed](Closed%20Sets.md).
>>
>

## Properties

>[!THEOREM] Theorem: Intersection of Closed Sets
>
>Let $(S, \tau)$ be a [topological space](./index.md).
>
>The [intersection](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of any [collection](../../Set%20Theory/Collections/index.md) of [closed subsets](Closed%20Subset.md.md) is also closed.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Union of Closed Sets
>
>Let $(S, \tau)$ be a [topological space](./index.md).
>
>The [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of any finite [collection](../../Set%20Theory/Collections/index.md) of [closed subsets](Closed%20Subset.md.md) is also closed.
>
>>[!PROOF]-
>>
>>Let $S_1,\cdots,S_n$ be closed sets. We need to show that $\bigcup \{S_1,\cdots, S_n\} = S_1 \cup \cdots \cup S_n$ is closed. According to the definition of a closed set, this means we must show that $S \setminus (S_1 \cup \cdots \cup S_n)$ is [open](Open%20Sets.md).
>>
>>By the [distributive law](../../Set%20Theory/Set%20Operations.md)
>>
>>$$
>>S \setminus (S_1 \cup \cdots \cup S_n) = (S\setminus S_1) \cap \cdots \cap (S \setminus S_n)
>>$$
>>
>>The sets $S_1,\cdots,S_n$ are closed and by definition their [complements](../../Set%20Theory/Complement.md) $S\setminus S_1,\cdots, S \setminus S_n$ are open. The right-hand side is thus an intersection of open sets and is, therefore, open itself. This means that the complement $S \setminus S_1 \cup \cdots \cup S_n$ is open and so $S_1 \cup \cdots \cup S_n$ is closed.
>>
>