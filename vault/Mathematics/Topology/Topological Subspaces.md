---
tags:
    - topology
    - mathematics
---

# Topological Subspaces

>[!THEOREM] Theorem: Topological Subspace
>
>Let $(X, \tau_X)$ be a [topological space](./Topological%20Spaces/Topological%20Space.md).
>
>For every [non-empty](../Set%20Theory/Sets.md) [subset](../Set%20Theory/Sets.md) $S$ of $X$, the [collection](../Set%20Theory/Collections.md)
>
>$$
>\tau_S \overset{\text{def}}{=} \{O \cap S \mid O \in \tau_X\}
>$$
>
>is a [topology](./Topological%20Spaces/Topological%20Space.md) on $S$.
>
>>[!PROOF]-
>>
>>We need to prove three things:
>>- (I) $S \in \tau_S$ and $\varnothing \in \tau_S$.
>>- (II) $\tau_S$ is closed under arbitrary unions.
>>- (III) $\tau_S$ is closed under finite intersections.
>>
>>**Proof of (I):**
>>
>>This follows from the fact that $\varnothing = S \cap \varnothing$ and $S = S \cap X$.
>>
>>**Proof of (II):**
>>
>>Let $\mathcal{U}$ be an arbitrary [subset](../Set%20Theory/Sets.md) of $\tau_S$. By definition, for each $U \in \mathcal{U}$ there exists some $O_U \in \tau_X$ such that $U = O_U \cap S$.  Then
>>
>>$$
>>\bigcup \mathcal{U} = \bigcup_{U \in \mathcal{U}} (O_U \cap S) = \left(\bigcup_{U \in \mathcal{U}} O_U\right) \cap S
>>$$
>>
>>Since $\bigcup_{U \in \mathcal{U}} O_U$ is a [union](../Set%20Theory/Collections.md) of [open sets](./Topological%20Spaces/Topological%20Space.md), it is itself [open](./Topological%20Spaces/Topological%20Space.md), i.e. $\bigcup_{U \in \mathcal{U}} O_U \in \tau_X$. Therefore $\left(\bigcup_{U \in \mathcal{U}} O_U\right) \cap S$ is in $\tau_S$.
>>
>>**Proof of (III):**
>>
>>Consider the [intersection](../Set%20Theory/Collections.md) $U_1 \cap \cdots \cap U_n$ where $U_1,\cdots, U_n \in \tau_S$. By definition, for each $U_k$ there exists some $O_k \in \tau_X$ such that $U_k = O_k \cap S$. This means that
>>
>>$$
>>U_1 \cap \cdots \cap U_n = (O_1 \cap S) \cap \cdots \cap (O_n \cap S) = (O_1 \cap \cdots \cap O_n) \cap S
>>$$
>>
>>Since $(O_1 \cap \cdots \cap O_n)$ is an [intersection](../Set%20Theory/Collections.md) of finitely many [open sets](./Topological%20Spaces/Topological%20Space.md), it is itself [open](./Topological%20Spaces/Topological%20Space.md). Therefore, $U_1 \cap \cdots \cap U_n \in \tau_S$.
>>
>
>>[!DEFINITION] Definition: Topological Subspace
>>
>>The [topological space](./Topological%20Spaces/Topological%20Space.md) $(S, \tau_S)$ is known as a **subspace** of $(X,\tau_X)$.
>>
>

>[!THEOREM] Theorem: Ambient Openness $\implies$ Subspace Openness
>
>Let $X$ be a [topological space](./Topological%20Spaces/Topological%20Space.md) and let $S$ be a [subspace](./Topological%20Subspaces.md) of $X$.
>
>If a [subset](../Set%20Theory/Subsets.md) $T \subseteq S$ is [open](./Topological%20Spaces/Open%20Sets.md) in $X$, then it is also [open](./Topological%20Spaces/Open%20Sets.md) in $S$.
>
>>[!EXAMPLE]- Example: Converse is False
>>
>>TODO
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Ambient Closedness $\implies$ Subspace Closedness
>
>Let $X$ be a [topological space](./Topological%20Spaces/Topological%20Space.md) and let $S$ be a [subspace](./Topological%20Subspaces.md) of $X$.
>
>If a [subset](../Set%20Theory/Subsets.md) $T \subseteq S$ is [closed](./Topological%20Spaces/Closed%20Sets.md) in $X$, then it is also [closed](./Topological%20Spaces/Closed%20Sets.md) in $S$.
>
>>[!EXAMPLE]- Example: Converse is False
>>
>>TODO
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Properties

>[!THEOREM] Theorem: Openness in Topological Subspaces
>
>Let $(S, \tau_S)$ be a [subspace](./Topological%20Subspaces.md) of a [topological space](./Topological%20Spaces/Topological%20Space.md) $(X, \tau_X)$ and let $U$ be a [subset](../Set%20Theory/Sets.md) of $S$.
>
>If $U$ is [open](./Topological%20Spaces/Topological%20Space.md) in $(S, \tau_S)$ and $S$ is [open](./Topological%20Spaces/Topological%20Space.md) $(X, \tau_X)$, then $U$ is also [open](./Topological%20Spaces/Topological%20Space.md) in $(X, \tau_X)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Closedness in Topological Subspaces (I)
>
>Let $(S, \tau_S)$ be a [subspace](./Topological%20Subspaces.md) of a [topological space](./Topological%20Spaces/Topological%20Space.md) $(X, \tau_X)$.
>
>A [set](../Set%20Theory/Sets.md) $A$ is [closed](./Topological%20Spaces/Topological%20Space.md) in $(S, \tau_S)$ if and only if it is the [intersection](../Set%20Theory/Sets.md) of a [closed set](./Topological%20Spaces/Topological%20Space.md) of $(X, \tau_X)$ with $S$.
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (I) If $A$ is a [closed set](./Topological%20Spaces/Topological%20Space.md) of $(S, \tau_S)$, then there exists a [closed set](./Topological%20Spaces/Topological%20Space.md) $C$ of $(X, \tau_X)$ such that $A = C \cap S$.
>>- (II) If there exists a [closed set](./Topological%20Spaces/Topological%20Space.md) $C$ of $(X, \tau_X)$ such that $A = C \cap S$, then $A$ is [closed](./Topological%20Spaces/Topological%20Space.md) in $(S, \tau_S)$.
>>
>>**Proof of (I):**
>>
>>Suppose that $A$ is [closed](./Topological%20Spaces/Topological%20Space.md) in $(S, \tau_S)$. Then its [Sets](../Set%20Theory/Sets.md) $S \setminus A$ is [open](./Topological%20Spaces/Topological%20Space.md) in $(S, \tau_S)$ and, by definition, there exists an [open set](./Topological%20Spaces/Topological%20Space.md) $O_A$ of $(X, \tau_X)$ such that $S \setminus A = O_A \cap S$. Furthermore, $X \setminus O_A$ is [closed](./Topological%20Spaces/Topological%20Space.md) in $(X, \tau_X)$, since $O_A$ is [open](./Topological%20Spaces/Topological%20Space.md) in $(X, \tau_X)$.
>>
>>**Proof of (II):**
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Closedness in Topological Subspaces (II)
>
>Let $(S, \tau_S)$ be a [subspace](./Topological%20Subspaces.md) of a [topological space](./Topological%20Spaces/Topological%20Space.md) $(X, \tau_X)$ and let $C$ be a [subset](../Set%20Theory/Sets.md) of $S$.
>
>If $C$ is [closed](./Topological%20Spaces/Topological%20Space.md) in $(S, \tau_S)$ and $S$ is [closed](./Topological%20Spaces/Topological%20Space.md) $(X, \tau_X)$, then $C$ is also [closed](./Topological%20Spaces/Topological%20Space.md) in $(X, \tau_X)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Base for Topological Subspaces
>
>Let $(S, \tau_S)$ be a [subspace](./Topological%20Subspaces.md) of a [topological space](./Topological%20Spaces/Topological%20Space.md) $(X, \tau_X)$.
>
>If $\mathcal{B}$ is a [base](../../index.md) for $(X, \tau_X)$, then the [collection](../Set%20Theory/Collections.md)
>
>$$
>\mathcal{B}_S \overset{\text{def}}{=} \{ B \cap S \mid B \in \mathcal{B}\}
>$$
>
>is a [base](../../index.md) for $(S, \tau_S)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

### Compactness of Subspaces

>[!THEOREM] Theorem: Compactness of Subspaces
>
>A [subspace](./Topological%20Subspaces.md) $(S, \tau_S)$ of a [topological space](./Topological%20Spaces/Topological%20Space.md) $(X, \tau_X)$ is [compact](../../index.md) if and only if every [cover](../../index.md#covers) of $S$ by [open subsets](./Topological%20Spaces/Topological%20Space.md) in $(X, \tau_X)$ contains a finite [subcollection](../Set%20Theory/Collections.md) which is also a [cover](../../index.md#covers) of $(S, \tau_S)$.
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (I) If $(S, \tau_S)$ is [compact](../../index.md), then every [cover](../../index.md) of $S$ by [open subsets](./Topological%20Spaces/Topological%20Space.md) in $(X, \tau_X)$ contains a finite [subcollection](../Set%20Theory/Collections.md) which is also a [cover](../../index.md) of $(S, \tau_S)$.
>>- (II) If every [cover](../../index.md) of $S$ by [open subsets](./Topological%20Spaces/Topological%20Space.md) in $(X, \tau_X)$ contains a finite [subcollection](../Set%20Theory/Collections.md) which is also a [cover](../../index.md#covers) of $(S, \tau_S)$, then $(S, \tau_S)$ is [compact](../../index.md).
>>
>>**Proof of (I):**
>>
>>Suppose that $(S, \tau_S)$ is [compact](../../index.md) and let $\mathcal{C}$ be a [cover](../../index.md#covers) of $S$ consisting of [open subset](./Topological%20Spaces/Topological%20Space.md) of $(X, \tau_X)$.
>>
>

>[!THEOREM] Theorem
>
>Let $(S, \tau_S)$ be a [subspace](./Topological%20Subspaces.md) of a [topological space](./Topological%20Spaces/Topological%20Space.md) $(X, \tau_X)$.
>
>If $(X, \tau_X)$ is [compact](../../index.md) and $S$ is [closed](./Topological%20Spaces/Topological%20Space.md) in $(X, \tau_X)$, then $(S, \tau_S)$ is also [compact](../../index.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>