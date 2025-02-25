---
title: Connectedness
tags:
  - connectedness
  - topology
  - mathematics
---

# Connectedness

>[!DEFINITION] Definition: Connectedness of a Topological Space
>
>A [topological space](../Topological%20Spaces/index.md) is **connected** iff it cannot be represented as the [union](../../Set%20Theory/Set%20Operations.md) of two [disjoint](../../Set%20Theory/Disjoint%20Sets.md), [nonempty](../../Set%20Theory/The%20Empty%20Set.md) [open sets](../Topological%20Spaces/Open%20Sets.md).
>

>[!DEFINITION] Definition: Connectedness of a Subset
>
>Let $(X, \tau_X)$ be a [topological space](../Topological%20Spaces/index.md).
>
>A [subset](../../Set%20Theory/Sets.md) $S \subseteq X$ is **connected** iff it is [connected](./index.md) as a [subspace](../Topological%20Subspaces.md).
>

>[!DEFINITION] Definition: Disconnectedness
>
>A [topological space](../Topological%20Spaces/index.md) is **disconnected** iff it is not [connected](./index.md).
>

## Connectedness Criteria

>[!THEOREM]-
>
>A [topological space](../Topological%20Spaces/index.md) $(X, \tau)$ is [connected](./index.md) if and only if its only [clopen subsets](../Topological%20Spaces/Clopen%20Sets.md) are $\varnothing$ and $X$.
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (I) If $(X, \tau)$ is [connected](./index.md), then its only [clopen subsets](../Topological%20Spaces/Clopen%20Sets.md) are $\varnothing$ and $X$.
>>- (II) If the only [clopen subsets](../Topological%20Spaces/Clopen%20Sets.md) of $(X, \tau)$ are $\varnothing$ and $X$, then $(X, \tau)$ is [connected](./index.md).
>>
>>**Proof of (I):**
>>
>>We prove this by contradiction.
>>
>>Suppose that $(X, \tau)$ is [connected](./index.md) and let $U \subset X$ be [clopen](../Topological%20Spaces/Clopen%20Sets.md). If $U$ is [nonempty](../../Set%20Theory/The%20Empty%20Set.md), then so is $X \setminus U$. Since $U$ is [clopen](../Topological%20Spaces/Clopen%20Sets.md), so is its [complement](../../Set%20Theory/Complement.md) $X \setminus U$.  More importantly, this implies that both $U$ and $X \setminus U$ are [open](../Topological%20Spaces/Open%20Sets.md). However, since $X = U \cup X\setminus U$, this means that $X$ can be represented as the [union](../../Set%20Theory/Set%20Operations.md) of two [disjoint](../../Set%20Theory/Disjoint%20Sets.md), [nonempty](../../Set%20Theory/The%20Empty%20Set.md) [open sets](../Topological%20Spaces/Open%20Sets.md) and is thus not [disconnected](./index.md), which is a contradiction.
>>
>>**Proof of (II):**
>>
>>We prove this by contradiction.
>>
>>Suppose that the only [clopen subsets](../Topological%20Spaces/Clopen%20Sets.md) of $(X, \tau)$ are $\varnothing$ and $X$. Assume that $(X, \tau)$ is [disconnected](./index.md), i.e. there exists two [disjoint](../../Set%20Theory/Disjoint%20Sets.md), [nonempty](../../Set%20Theory/The%20Empty%20Set.md) [open sets](../Topological%20Spaces/Open%20Sets.md) $U$ and $V$ such that $X = U \cup V$.
>>
>>
>

>[!THEOREM]
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces/index.md) and let $S$ be a [subset](../../Set%20Theory/Sets.md) of $X$.
>
>If $S$ can be expressed as the [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of a [collection](../../Set%20Theory/Collections/index.md) $\mathcal{C}$ of [](index.md#^connected-subset) [subsets](../../Set%20Theory/Sets.md) whose [intersection](../../Set%20Theory/Collections/Operations%20with%20Collections.md) is [nonempty](../../Set%20Theory/The%20Empty%20Set.md),  then $S$ is also [](index.md#^connected-subset).
>
>>[!PROOF]-
>>
>>TODO
>>
>