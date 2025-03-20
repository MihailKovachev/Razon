---
title: Compactness
tags:
  - compactness
  - topology
  - mathematics
---

# Covers

>[!DEFINITION] Definition: Cover
>
>Let $X$ be a [set](../../Set%20Theory/Sets.md).
>
>A [collection](../../Set%20Theory/Collections/Collections.md) $\mathcal{C}$ of [subsets](../../Set%20Theory/Sets.md) of $X$ is a **cover** of $X$ iff $X$ is a [subset](../../Set%20Theory/Sets.md) of the [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of $\mathcal{C}$.
>
>$$
>X \subseteq \bigcup \mathcal{C}
>$$
>

>[!DEFINITION] Definition: Subcover
>
>Let $X$ be a [set](../../Set%20Theory/Sets.md) and let $\mathcal{C}$ be a [cover](./index.md#covers) of $X$.
>
>A **subcover** of $\mathcal{C}$ is [subcollection](../../Set%20Theory/Collections/Collections.md) of $\mathcal{C}$ which is still a [cover](./index.md#covers) of $X$.
>

>[!DEFINITION] Definition: Open Cover
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces/index.md).
>
>A [cover](./index.md#covers) of $X$ is an **open cover** iff all of its elements are [open sets](../Topological%20Spaces/Open%20Sets.md).
>

# Compactness

>[!DEFINITION] Definition: Compactness of a Topological Space
>
>A [topological space](../Topological%20Spaces/index.md) is **compact** iff each of its [open covers](./index.md#covers) has a finite [subcover](./index.md#covers).
>
>>[!NOTE] Note: Compactness of a Subset
>>
>>A [subset](../../Set%20Theory/Sets.md) of a [topological space](../Topological%20Spaces/index.md) is called compact iff it is [compact](/index.md#compactness) as a [subspace](../Topological%20Subspaces.md).
>>
>


