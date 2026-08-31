---
tags:
  - topology
  - mathematics
---

# Hausdorff Spaces

>[!DEFINITION] Definition: Hausdorff Space
>
>A **Hausdorff space** is a [topological space](./Topological%20Spaces/Topological%20Space.md) $X$ is a **Hausdorff space** or $T_2$ **space** if each two distinct points $p_1,p_2 \in X$ have [disjoint](../Set%20Theory/Sets.md) [neighborhoods](./Topological%20Spaces/Topological%20Space.md#Neighborhoods).
>
>$$\forall p_1, p_2 \in X: \exists N(p_1), N(p_2) : N(p_1) \cap N(p_2) = \varnothing$$
>
>>[!NOTE]
>>
>>[Hausdorff spaces](#Hausdorff%20Spaces) are also known as $T_2$ spaces.
>>
>

>[!THEOREM] Theorem: Finite Subsets of Hausdorff Spaces are Closed
>
>Every [finite](../Set%20Theory/Cardinality.md) [subset](../Set%20Theory/Sets.md#Subsets) of a [Hausdorff space](./Hausdorff%20Space.md) is [closed](./Topological%20Spaces/Topological%20Space.md#Closed%20Sets).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Open Subspaces of Hausdorff Spaces
>
>Every [topological subspace](./Topological%20Subspaces.md) from an [open subset](./Topological%20Spaces/Topological%20Space.md#Open%20Sets) of a [Hausdorff space](./Hausdorff%20Space.md) is itself a [Hausdorff space](./Hausdorff%20Space.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Limit Uniqueness in Hausdorff Spaces
>
>Let $(X, \tau)$ be a [topological space](./Topological%20Spaces/Topological%20Space.md) and let $(x_n)_{n \in I}$ be a [sequence](../Analysis/Functional%20Analysis/Sequences/Sequences.md) of points in $X$.
>
>If $(X, \tau)$ is [Hausdorff](./Hausdorff%20Space.md) and $(x_n)_{n \in I}$ is [convergent](../Analysis/Functional%20Analysis/Sequences/Convergence%20(Sequences.md), then it has only one [limit](../Analysis/Functional%20Analysis/Sequences/Convergence%20(Sequences.md):
>
>$$
>\lim_{n \to \infty} x_n = L \qquad \text{ and } \qquad \lim_{n \to \infty} x_n = L' \implies L = L'
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Infinite Neighborhoods of Accumulation Points
>
>Let $S$ be a [subset](../Set%20Theory/Sets.md#Subsets) of a [Hausdorff space](./Hausdorff%20Space.md) $X$.
>
>If $p \in X$ is a [limit point](./Interior,%20Boundary,%20Exterior.md) of $S$, then every [neighborhood](./Topological%20Spaces/Topological%20Space.md#Neighborhoods) of $p$ contains [infinitely](../Set%20Theory/Cardinality.md) many points of $S$.
>
>>[!PROOF]-
>>
>>TODO
>>
>