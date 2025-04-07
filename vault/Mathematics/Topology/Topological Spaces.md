---
title: Topological Spaces
tags:
  - topology
  - mathematics
---

# Topologies and Topological Spaces

>[!DEFINITION] Definition: Topology
>
>A **topology** on a [non-empty](../../Set%20Theory/Sets.md) [set](../../Set%20Theory/Sets.md) $X$ is a [collection](../../Set%20Theory/Collections/Collections.md) $\tau$ of [subsets](../../Set%20Theory/Sets.md) of $X$ which has the following properties:
>
>- The [empty set](../../Set%20Theory/Sets.md) $\varnothing$ and $X$ are in $\tau$.
>- The [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of any subset of $\tau$ is in $\tau$.
>- The [intersection](../../Set%20Theory/Set%20Operations.md) of any two elements of $\tau$ is in $\tau$.
>
>>[!INTUITION]-
>>
>>A topology $\tau$ on a [set](../../Set%20Theory/Sets.md) $X$ can be interpreted as a definition of "closeness" between elements of $X$ without using any notion of distance. Moreover, a topology provides a way for us to define what is "inside" a set, what is "outside" a set and what separates the inside of a set from its outside.
>> 
>
>>[!EXAMPLE]-
>>
>>Consider the sets $X = \{1,2,3,4,5,6\}$ and $\tau = \{\varnothing, X, \{1\}, \{3,4\}, \{1,3,4\}, \{2,3,4,5,6\}\}$. The set $\tau$ is a topology on $X$, since it satisfies the requirements in the definition.
>>
>

>[!DEFINITION] Definition: Topological Space
>
>A **topological space** $(S,\tau)$ is a [non-empty](../../Set%20Theory/Sets.md) [set](../../Set%20Theory/Sets.md) $S$ equipped with a [topology](Topological%20Spaces.md) $\tau$ on it.
>
>>[!NOTE] Note: Points
>>
>>It is common to refer to the elements $s \in S$ of a topological space as **points**.
>>
>


# Open Sets

>[!DEFINITION] Definition: Open Subset
>
>Let $(X, \tau)$ be a [topological space](Topological%20Spaces.md).
>
>A [subset](../../Set%20Theory/Sets.md) of $X$ is **open** iff it is an element of $\tau$.
>

## Openness Criteria

>[!THEOREM]-
>
>Let $(X, \tau)$ be a [topological space](Topological%20Spaces.md).
>
>A [subset](../../Set%20Theory/Sets.md) $U \subseteq X$ is [open](Open%20Sets.md) if and only if each $x \in U$ has [neighbourhood](Topological%20Spaces.md)d) $N(x)$ such that $N(x) \subseteq U$.
>
>>[!PROOF]-
>>
>>If $U$ is [open](Open%20Sets.md), then $U$ is, by definition, [neighbourhood](Topological%20Spaces.md)d) of every $x \in U$.
>>
>>If there exists [neighbourhood](Topological%20Spaces.md)d) $N(x)$ of each $x$ such that $N(x) \subseteq U$, then inside each neighbourhood $N(x)$ there exists, by definition, an open set $O(x) \subseteq N(x)$ which contains $x$. Since $N(x) \subseteq U$, we have $O(x) \subseteq N(x) \subseteq U$. This means that we can construct $U$ as the [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of these open sets $O(x)$.
>>
>>$$
>>U = \bigcup_{x \in U} O(x)
>>$$
>>
>>Since this is a union of open sets, i.e. it is a union of a subset of the [topology](Topological%20Spaces.md) $\tau$, we have that $U \in \tau$. 
>>
>

>[!THEOREM]- Theorem
>
>Let $(X, \tau)$ be a [topological space](Topological%20Spaces.md).
>
>A [subset](../../Set%20Theory/Sets.md) $U \subseteq X$ is [open](Open%20Sets.md) if and only if for each $x \in U$ there exists an open set $V$ such that $V \subseteq U$ and $x \in V$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem
>
>Let $(X, \tau)$ be a [topological space](Topological%20Spaces.md).
>
>A [subset](../../Set%20Theory/Sets.md) $S \subseteq X$ is [open](Open%20Sets.md) if and only if it is equal to its own [interior](Interior,%20Boundary%20and%20Exterior.md).
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
>>Suppose $S$ is [open](Open%20Sets.md). Recall the definition of the [interior](Interior,%20Boundary%20and%20Exterior.md) $\operatorname{int} S$:
>>
>>$$
>>\operatorname{int} S \overset{\text{def}}{=} \bigcup \{O \subseteq S \mid O \text{ is open}\}
>>$$
>>
>>Since $S\subseteq S$ and $S$ is [open](Open%20Sets.md), we know that $S \in \{O \subseteq S \mid O \text{ is open}\}$ and thus $S \subseteq \operatorname{int} S$. However, the [interior](Interior,%20Boundary%20and%20Exterior.md) is a [subset](../../Set%20Theory/Sets.md) of $S$. Since $S \subseteq \operatorname{int} S$ and $\operatorname{int} S \subseteq S$, we know deduce that $S = \operatorname{int} S$.
>>
>>**Proof of (II):**
>>
>>Suppose that $S = \operatorname{int} S$. Since the [interior](Interior,%20Boundary%20and%20Exterior.md) $\operatorname{int} S$ is a [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of [open sets](Open%20Sets.md), it is itself [open](Open%20Sets.md). Therefore, $S$ is [open](Open%20Sets.md).
>>
>

## Properties of Open Sets

>[!THEOREM]- Theorem: Union of Open Sets
>
>Let $(S, \tau)$ be a [topological space](Topological%20Spaces.md).
>
>The [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of any [collection](../../Set%20Theory/Collections/Collections.md) of [open subsets](Open%20Sets.md) is also open.
>
>>[!PROOF]-
>>
>>This follows directly from the definition of a [topology](Topological%20Spaces.md).
>>
>

>[!THEOREM]- Theorem: Intersection of Open Sets
>
>Let $(S, \tau)$ be a [topological space](Topological%20Spaces.md).
>
>The [intersection](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of any finite [collection](../../Set%20Theory/Collections/Collections.md) of [open sets](Open%20Sets.md) is also open.
>
>>[!PROOF]-
>>
>>We consider $n \ge 2$ arbitrary [open subsets](Open%20Sets.md) $U_1,\cdots, U_n$.
>>
>>For $n = 2$, the definition of the [topology](Topological%20Spaces.md) $\tau$ tells us that $U_1 \cap U_2 \in \tau$.
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

# Closed Sets

>[!DEFINITION] Definition: Closed Set
>
>Let $(S, \tau)$ be a [topological space](Topological%20Spaces.md).
>
>A [subset](../../Set%20Theory/Sets.md) $U$ of $S$ is **closed** if its [complement](../../Set%20Theory/Complement.md) $S \setminus U$ is an [open set](Topological%20Spaces.md).
>
>>[!THEOREM]
>>
>>Let $(S, \tau)$ be a [topological space](Topological%20Spaces.md).
>>
>>A [subset](../../Set%20Theory/Sets.md) $C \subseteq S$ is [closed](Closed%20Sets.md) if and only if for each $x$ in its [complement](../../Set%20Theory/Complement.md) $S \setminus C$ there exists [neighbourhood](Topological%20Spaces.md)d) $N$ of $x$ such that $N \subseteq S \setminus C$.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

## Closedness Criteria

>[!THEOREM]-
>
>Let $(X, \tau)$ be a [topological space](Topological%20Spaces.md).
>
>A [subset](../../Set%20Theory/Subsets.md) $S \subseteq X$ is [closed](Topological%20Spaces.md) if and only if it is equal to its own [closure](Interior,%20Boundary,%20Exterior/Closure.md).
>
>>[!PROOF]-
>>
>>We have to prove two things:
>>- (I) If $S$ is [closed](Closed%20Sets.md), then $S = \overline{S}$.
>>- (II) If $S = \overline{S}$, then $S$ is [closed](Topological%20Spaces.md).
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

>[!THEOREM]- Theorem: Limit Points of Closed Subsets
>
>Let $(X, \tau)$ be a [topological space](Topological%20Spaces.md).
>
>A [subset](../../Set%20Theory/Subsets.md) $S \subseteq X$ is [closed](Closed%20Sets.md) if and only if it contains all of its [limit points](Interior,%20Boundary,%20Exterior/Accumulation%20Point.md).
>
>>[!PROOF]-
>>
>>We need to prove two things separately:
>>- (I) If $S$ is [closed](Closed%20Sets.md), then every [limit point](Interior,%20Boundary,%20Exterior/Accumulation%20Point.md) of $S$ lies in $S$.
>>- (II) If $S$ contains all of its [limit points](Interior,%20Boundary,%20Exterior/Accumulation%20Point.md), then it is [closed](Closed%20Sets.md).
>>
>>**Proof of (I):**
>>
>>We prove this by contradiction. Suppose that $S$ is [closed](Closed%20Sets.md) and there exists a [limit point](Interior,%20Boundary,%20Exterior/Accumulation%20Point.md) $p$ of $S$ which lies outside of $S$, i.e. $p \in X \setminus S$. We know that $X \setminus S$ is [open](Topological%20Spaces.md) because it is the [complement](../../Set%20Theory/Complement.md) of a [closed set](Closed%20Sets.md). However, since $p$ is a [limit point](Interior,%20Boundary,%20Exterior/Accumulation%20Point.md) of $S$, every [open set](Topological%20Spaces.md) which contains $p$ must also contain an element of $S$. This implies that $X \setminus S$ contains an element of $S$ which is a contradiction.
>>
>>**Proof of (II):**
>>
>>Suppose that $S$ contains all of its [limit points](Interior,%20Boundary,%20Exterior/Accumulation%20Point.md). This means that there are no points $p \in X\setminus S$ such that every [open set](Topological%20Spaces.md) $U$ which contains $p$ also contains another element of $S$. Alternatively, this means that each $p \in X \setminus S$ is contained in some [open set](Topological%20Spaces.md) $U_p$ such that $U_p \cap S = \varnothing$, i.e. $U_p \subseteq X \setminus S$. Therefore, the [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) $\bigcup_{p \in X \setminus S} U_p$ is a [subset](../../Set%20Theory/Sets.md) of $X \setminus S$ and, since it contains every $p \in X \setminus S$, it means that $\bigcup_{p \in X \setminus S} U_p = X \setminus$. Since $X \setminus S$ is a [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of [open sets](Topological%20Spaces.md), it is itself [open](Topological%20Spaces.md) and so $S$ is [closed](Closed%20Sets.md).
>>
>

## Properties

>[!THEOREM] Theorem: Intersection of Closed Sets
>
>Let $(S, \tau)$ be a [topological space](Topological%20Spaces.md).
>
>The [intersection](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of any [collection](../../Set%20Theory/Collections/Collections.md) of [closed subsets](Topological%20Spaces.md) is also closed.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Union of Closed Sets
>
>Let $(S, \tau)$ be a [topological space](Topological%20Spaces.md).
>
>The [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of any finite [collection](../../Set%20Theory/Collections/Collections.md) of [closed subsets](Topological%20Spaces.md) is also closed.
>
>>[!PROOF]-
>>
>>Let $S_1,\cdots,S_n$ be closed sets. We need to show that $\bigcup \{S_1,\cdots, S_n\} = S_1 \cup \cdots \cup S_n$ is closed. According to the definition of a closed set, this means we must show that $S \setminus (S_1 \cup \cdots \cup S_n)$ is [open](Topological%20Spaces.md).
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

# Clopen Sets

It is important to note that "openness" and "closedness" are neither mutually exclusive nor complete - [subsets](../../Set%20Theory/Subsets.md) in a [topological spaces](Topological%20Spaces.md) can be both [open](Topological%20Spaces.md#Open%20Sets.md) and [closed](Topological%20Spaces.md#Closed%20Sets.md) or they can also be neither.

>[!DEFINITION] Definition: Clopen Set
>
>Let $(X, \tau)$ be a [topological space](Topological%20Spaces.md).
>
>A [subset](../../Set%20Theory/Sets.md) of $X$ is a **clopen** iff it is both [open](Topological%20Spaces.md) and [closed](Topological%20Spaces.md).
>

# Neighborhoods

>[!DEFINITION] Definition: Neighborhood of a Point
>
>Let $(X,\tau)$ be a [topological space](Topological%20Spaces.md) and let $x \in X$.
>
>A [subset](../../Set%20Theory/Sets.md) $N \subseteq X$ is a **neighbourhood** of $x$ iff there exists an [open set](Topological%20Spaces.md) $U$ such that $U \subseteq N$ and $x \in U$.
>
>>[!NOTATION]-
>>
>>$$
>>N(x) \qquad N_x
>>$$
>>
>
>^neighbourhood-of-a-point
>

>[!DEFINITION] Definition: Neighbourhood of a Set
>
>Let $(X,\tau)$ be a [topological space](Topological%20Spaces.md) and let $S$ be a [subset](../../Set%20Theory/Sets.md) of $X$.
>
>A [subset](../../Set%20Theory/Sets.md) $N \subseteq X$ is a **neighbourhood** of $S$ iff there exists an [open set](Topological%20Spaces.md) $U$ such that
>
>$$
>S \subseteq U \subseteq N
>$$
>
>>[!NOTATION]-
>>
>>$$
>>N_S \qquad N(S)
>>$$
>>
>