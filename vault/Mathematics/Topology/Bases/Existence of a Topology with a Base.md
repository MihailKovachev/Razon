---
title: Existence of a Topology with a Base
tags:
  - topology
  - mathematics
---

>[!THEOREM] Theorem: Existence of a Topology with a Base
>
>Let $X$ be a [non-empty](../../Set%20Theory/The%20Empty%20Set.md) [set](../../Set%20Theory/Sets.md) and let $\mathcal{B}$ be a [collection](../../Set%20Theory/Collections/index.md) of [subsets](../../Set%20Theory/Sets.md) of $X$.
>
>There exists a [topology](../Topological%20Spaces/index.md) $\tau_\mathcal{B}$ on $X$ such that $\mathcal{B}$ is a [base](./index.md) for the [topological space](../Topological%20Spaces/index.md) $(X, \tau_\mathcal{B})$ if and only if
>- $X$ is the [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of $\mathcal{B}$, i.e. $X = \bigcup \mathcal{B}$, and
>- for each $B_1, B_2 \in \mathcal{B}$, the [intersection](../../Set%20Theory/Set%20Operations.md) $B_1 \cap B_2$ is a union of a subset of $\mathcal{B}$.
>
>>[!PROOF]-
>>
>>We need to prove the following things separately:
>>- If there exists a [topology](../Topological%20Spaces/index.md) $\tau_\mathcal{B}$ on $X$ such that $\mathcal{B}$ is a [base](./index.md) for the [topological space](../Topological%20Spaces/index.md) $(X, \tau_\mathcal{B})$, then $X = \bigcup \mathcal{B}$ and for each $B_1, B_2 \in \mathcal{B}$, the [intersection](../../Set%20Theory/Set%20Operations.md) $B_1 \cap B_2$ is a [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of a subset of $\mathcal{B}$.
>>- If $\mathcal{B}$ is such that $X = \bigcup \mathcal{B}$ and for each $B_1, B_2 \in \mathcal{B}$, the [intersection](../../Set%20Theory/Set%20Operations.md) $B_1 \cap B_2$ is a union of a [subset](../../Set%20Theory/Sets.md) of $\mathcal{B}$, then there exists a [topology](../Topological%20Spaces/index.md) $\tau_\mathcal{B}$ on $X$ such that $\mathcal{B}$ is a [base](./index.md) for the [topological space](../Topological%20Spaces/index.md) $(X, \tau_\mathcal{B})$.
>>
>>**Part 1**: 
>>
>>Suppose that there exists a [topology](../Topological%20Spaces/index.md) $\tau_\mathcal{B}$ on $X$ such that $\mathcal{B}$ is a [base](./index.md) for the [topological space](../Topological%20Spaces/index.md) $(X, \tau_\mathcal{B})$.
>>
>>By the definition of a [topology](../Topological%20Spaces/index.md), we have that $X$ is an [open set](../Topological%20Spaces/Open%20Sets.md). Since $\mathcal{B}$ is a [base](./index.md) for $\tau_\mathcal{B}$, the [set](../../Set%20Theory/Sets.md) $X$ can be expressed as a [union](../../Set%20Theory/Set%20Operations.md) of a [subset](../../Set%20Theory/Sets.md) of $\mathcal{B}$. In particular, since $\mathcal{B}$ is comprised only of [subsets](../../Set%20Theory/Sets.md) of $X$, then $X = \bigcup \mathcal{B}$. Similarly, since $\mathcal{B}$ contains only [open sets](../Topological%20Spaces/Open%20Sets.md) by definition, the [intersection](../../Set%20Theory/Set%20Operations.md) $B_1 \cap B_2$ is in $\tau_\mathcal{B}$, which completes the proof, since every [open set](../Topological%20Spaces/Open%20Sets.md) can be expressed as a [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of elements of $\mathcal{B}$ by definition.
>>
>>**Part 2:** 
>>
>>Suppose $\mathcal{B}$ is such that $X = \bigcup \mathcal{B}$ and for each $B_1, B_2 \in \mathcal{B}$, the [intersection](../../Set%20Theory/Set%20Operations.md) $B_1 \cap B_2$ is a union of a [subset](../../Set%20Theory/Sets.md) of $\mathcal{B}$. Define $\tau_\mathcal{B}$ as the [collection](../../Set%20Theory/Collections/index.md) of all [subsets](../../Set%20Theory/Sets.md) of $X$ which are [unions](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of [subsets](../../Set%20Theory/Sets.md) of $\mathcal{B}$. 
>>
>>We need to show that $\tau_\mathcal{B}$ is a [topology](../Topological%20Spaces/index.md) on $X$. To do this we need to show the following three things:
>>- $X \in \tau_\mathcal{B}$ and $\varnothing \in \tau_\mathcal{B}$;
>>- $\tau_\mathcal{B}$ is closed under arbitrary [unions](../../Set%20Theory/Collections/Operations%20with%20Collections.md);
>>- The [intersection](../../Set%20Theory/Set%20Operations.md) $U_1 \cap U_2$ of each $U_1, U_2 \in \tau_\mathcal{B}$ is in $\tau_\mathcal{B}$.
>>
>>The assumption that $X = \bigcup\mathcal{B}$ entails that $X \in \tau_\mathcal{B}$. The [empty set](../../Set%20Theory/The%20Empty%20Set.md) is a [subset](../../Set%20Theory/Sets.md) of $\mathcal{B}$ and since $\varnothing = \bigcup \varnothing$, we have that $\varnothing \in \tau_\mathcal{B}$.
>>
>>Consider now an arbitrary [subset](../../Set%20Theory/Sets.md) $T$ of $\tau_\mathcal{B}$. Since each $U \in T$ is a [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of a [subset](../../Set%20Theory/Sets.md) of $\mathcal{B}$, then $\bigcup T$ is also a [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of a [subset](../../Set%20Theory/Sets.md) $\mathcal{B}$, meaning that $\bigcup T \in \tau_\mathcal{B}$.
>>
>>Finally, we consider two [sets](../../Set%20Theory/Sets.md) $U_1, U_2 \in \tau_\mathcal{B}$. By definition of $\tau_\mathcal{B}$, there exists some [subset](../../Set%20Theory/Sets.md) $\{B_i\}_{i \in I} \subseteq \mathcal{B}$ such that $U_1 = \bigcup_{i \in I} B_i$. Similarly, $U_2 = \bigcup_{j \in J} B_j$. We thus have
>>
>>$$U_1 \cap U_2 = \left(\bigcup_{i \in I} B_i\right) \cap \left(\bigcup_{j \in J} B_j\right) = \bigcup_{i \in i, j \in J} (B_i \cap B_j)$$
>>
>>By assumption, for all $i \in I$ and $j \in J$, the [intersection](../../Set%20Theory/Set%20Operations.md) $(B_i \cap B_j)$ is a [union](../../Set%20Theory/Set%20Operations.md) of a [subset](../../Set%20Theory/Sets.md) of $\mathcal{B}$. Therefore, the [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) $\bigcup_{i \in i, j \in J} (B_i \cap B_j)$ is also a [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of a [subset](../../Set%20Theory/Sets.md) of $\mathcal{B}$ and is thus in $\tau_\mathcal{B}$, Q.E.D.
>>
>