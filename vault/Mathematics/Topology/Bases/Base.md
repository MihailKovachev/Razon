---
tags:
    - topology
    - mathematics
---

# Base

>[!DEFINITION] Definition: Base 
>
>Let $X$ be a [topological space](../Topological%20Spaces/Topological%20Space.md).
>
>A **base** of $X$ is a [collection](../../Set%20Theory/Collections.md) $\mathcal{B}$ of [open sets](../Topological%20Spaces/Open%20Sets.md) such that every [open set](../Topological%20Spaces/Open%20Sets.md) can be represented as the [union](../../Set%20Theory/Collections.md) of a [subcollection](../../Set%20Theory/Collections.md) of $\mathcal{B}$.
>
>>[!WARNING]
>>
>>This representation is not necessarily unique.
>>
>

>[!DEFINITION] Definition: Subbase
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces/Topological%20Space.md).
>
>A **subbase** for $(X, \tau)$ is a [non-empty](../../Set%20Theory/Sets.md) [collection](../../Set%20Theory/Collections.md) $\mathcal{S}$ of [subsets](../../Set%20Theory/Sets.md) of $X$ such that the [collection](../../Set%20Theory/Collections.md) of all [intersections](../../Set%20Theory/Collections.md) of finite [subcollections](../../Set%20Theory/Collections.md) of $\mathcal{S}$ is a [base](./Base.md) for $(X, \tau)$.
>


 
>[!THEOREM] Theorem: Base Criterion
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces/Topological%20Space.md).
>
>A [collection](../../Set%20Theory/Collections.md) $\mathcal{B}$ of [open sets](../Topological%20Spaces/Topological%20Space.md#Open%20Sets) is a [base](./Base.md) for $(X, \tau)$ if and only if for each [open set](../Topological%20Spaces/Topological%20Space.md#Open%20Sets) $U$ and each $u \in U$, there exists some $B \in \mathcal{B}$ such that $B \subseteq U$ and $u \in B$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Open Sets from Base
>
>Let $X$ be a [topological space](../Topological%20Spaces/Topological%20Space.md) and let $\mathcal{B}$ be a [base](./Base.md) of $X$.
>
>A [subset](../../Set%20Theory/Subsets.md) $U \subseteq X$ is [open](../Topological%20Spaces/Open%20Sets.md) if and only if, for each $u \in U$, there exists some $B \in \mathcal{B}$ with $B \subseteq U$ and $u \in B$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Existence of a Topology with a Base
>
>Let $X$ be a [non-empty set](../../Set%20Theory/Sets.md) and let $\mathcal{B}$ be a [collection](../../Set%20Theory/Collections.md) of [subset](../../Set%20Theory/Sets.md) of $X$.
>
>There exists a [topology](../Topological%20Spaces/Topological%20Space.md) $\tau_\mathcal{B}$ on $X$ such that $\mathcal{B}$ is a [base](./Base.md) for the [topological space](../Topological%20Spaces/Topological%20Space.md) $(X, \tau_\mathcal{B})$ if and only if $X$ is the [union](../../Set%20Theory/Collections.md) of $\mathcal{B}$ and for each $B_1, B_2 \in \mathcal{B}$, the [intersection](../../Set%20Theory/Sets.md) $B_1 \cap B_2$ is a [union](../../Set%20Theory/Collections.md) of a [subollection](../../Set%20Theory/Collections.md) of $\mathcal{B}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Countability



>[!DEFINITION] Definition: Second-Countability Axiom
>
>A [topological space](../Topological%20Spaces/Topological%20Space.md) is **second-countable** iff it has a [countable](../../Set%20Theory/Cardinality.md) [base](./Base.md).
>

>[!THEOREM] Theorem: Second-Countability $\implies$ First-Countability
>
>If a [topological space](../Topological%20Spaces/Topological%20Space.md) is [second-countable](#Countability), then it is also [first-countable](#Countability)
>
>>[!PROOF]-
>>
>>TODO
>>
>