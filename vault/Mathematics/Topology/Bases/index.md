---
title: Bases for a Topological Space
tags:
  - topology
  - mathematics
---

# Base

>[!DEFINITION] Definitiom: Base for a Topological Space
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces.md).
>
>A **base** for $(X,\tau)$ is a [collection](../../Set%20Theory/Collections/Collections.md) $\mathcal{B}$ of [open subsets](../Topological%20Spaces.md) of $X$ such that every open set can be represented as a [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of a [subset](../../Set%20Theory/Sets.md) of $\mathcal{B}$.
>
>>[!WARNING]
>>
>>This representation is not necessarily unique.
>>

## Base Criteria

>[!THEOREM]- Theorem
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces.md).
>
>A [collection](../../Set%20Theory/Collections/Collections.md) $\mathcal{B}$ of [open sets](../Topological%20Spaces.md) is a [base](./index.md) for $(X, \tau)$ if and only if for each [open set](../Topological%20Spaces.md) $U$ and each $u \in U$, there exists some $B \in \mathcal{B}$ such that $B \subseteq U$ and $u \in B$.
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (I) If $\mathcal{B}$ is a [base](./index.md) for $(X, \tau)$, then for each [open set](../Topological%20Spaces.md) $U$ and each $u \in U$, there exists some $B \in \mathcal{B}$ such that $B \subseteq U$ and $u \in B$.
>>- (II) If for each [open set](../Topological%20Spaces.md) $U$ and each $u \in U$, there exists some $B \in \mathcal{B}$ such that $B \subseteq U$ and $u \in B$, then $\mathcal{B}$ is a  [base](./index.md) for $(X, \tau)$.
>>
>>**Part I:**
>>
>>Suppose $\mathcal{B}$ is a [base](Base%20for%20a%20Topological%20Space.md) for $(X, \tau)$. Let $U$ be [open](../Topological%20Spaces.md) and let $u \in U$. Since $\mathcal{B}$ is a [base](Base%20for%20a%20Topological%20Space.md), $U$ can be represented as a [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of some [subset](../../Set%20Theory/Sets.md) $\mathcal{B}_U \subseteq \mathcal{B}$, i.e. $U = \bigcup \mathcal{B}_U$. This implies that every $B \in \mathcal{B}_U$ is a [subset](../../Set%20Theory/Sets.md) of $U$. Moreover, since $u \in U$, there must exist at least one $B \in \mathcal{B}_U$ which contains $u$.
>>
>>**Part II:**
>>
>>Suppose that for each [open set](../Topological%20Spaces.md) $U \in \tau$ and each $u \in U$, there exists a $B(u) \in \mathcal{B}$ such that $B(u) \subseteq U$ and $u \in B(u)$. Since $B(u) \subseteq U$ for each $u \in U$, it holds that $\bigcup_{u \in U} B(u) \subseteq U$. Since this [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) contains every $u \in U$, it follows that $\bigcup_{u \in U} B(u) = U$. Therefore, $U$ is a [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of a [subset](../../Set%20Theory/Sets.md) of $\mathcal{B}$, Q.E.D.
>>
>

## Topology Generation

>[!THEOREM] Theorem: Topology Generation
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces.md) and let $\mathcal{B}$ be a [base](./index.md) for $(X, \tau)$.
>
>A [subset](../../Set%20Theory/Sets.md) $U \subseteq X$ is [open](../Topological%20Spaces.md) if and only if for each $u \in U$ there exists some $B \in \mathcal{B}$ such that $B \subseteq U$ and $u \in B$.
>
>>[!PROOF]-
>>
>>We need to prove two things separately:
>>- (I) If $U$ is [open](../Topological%20Spaces.md), then for each $u \in U$ there exists some $B_u \in \mathcal{B}$ such that $B_u \subseteq U$ and $u \in B_u$.
>>- (II) If for each $u \in U$ there exists some $B \in \mathcal{B}$ such that $B \subseteq U$ and $u \in B$, then $U$ is [open](../Topological%20Spaces.md).
>>
>>**Proof of (I):**
>>
>>Suppose $U$ is [open](../Topological%20Spaces.md). The fact that for each $u \in U$ there exists some $B_u \in \mathcal{B}$ such that $B_u \subseteq U$ and $u \in B_u$ follows immediately from the [base criterion](./index.md).
>>
>>**Proof of (II):**
>>
>>Suppose that for each $u \in U$ there exists some $B \in \mathcal{B}$ such that $B \subseteq U$ and $u \in B$. Since $u$ is contained in $B_u$ and $B_u \subseteq U$, we know that $U = \bigcup_{u \in U} B_u$, i.e. $U$ is a [union](../../Set%20Theory/Set%20Operations.md) of [open subsets](../Topological%20Spaces.md) and is thus [open](../Topological%20Spaces.md).
>>
>
>>[!INTUITION]
>>
>>This theorems allows us to determine the [topology](../Topological%20Spaces.md) $\tau$ given only a [base](./index.md) for it.
>>
>
>^topology-generation
>
