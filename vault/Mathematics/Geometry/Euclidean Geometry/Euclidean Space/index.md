---
title: Euclidean Space
tags:
    - euclidean-geometry
    - geometry
    - topology
    - mathematics
---

# Euclidean Space

>[!DEFINITION] Definition: Euclidean Topology
>
>The **Euclidean topology** on the [real vector space](../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Structure%20of%20the%20Real%20Vector%20Space.md) $\mathbb{R}^n$ is the [metric topology](../../../Topology/Metric%20Spaces/index.md) induced on it by the [Euclidean metric](../../../Algebra/Linear%20Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Euclidean%20Metric.md).
>

>[!DEFINITION] Definition: Euclidean Space
>
>The [vector space](../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Structure%20of%20the%20Real%20Vector%20Space.md) $\mathbb{R}^n$ equipped with its [Euclidean topology](./index.md) is known as the $n$-dimensional **Euclidean space**.
>
>>[!NOTE]
>>
>>When it is clear from context what $n$ is, or when $n$ is irrelevant, we usually drop "$n$-dimensional" and "geometric" and talk simply about "space".
>>
>

>[!THEOREM] Theorem: Euclidean Space is a Smooth Manifold
>
>The [atlas](../../Manifolds/Coordinates/Atlases.md) whose only [chart](../../Manifolds/Coordinates/index.md) is $(\mathbb{R}^n, \operatorname{id})$, where $\operatorname{id}$ is the [identity function](../../../Analysis/Functions/Identity%20Function.md) on the [Euclidean space](./index.md) $\mathbb{R}^n$, is a [smooth structure](../../../Analysis/Analysis%20on%20Manifolds/Smooth%20Manifolds.md) on $\mathbb{R}^n$ and naturally makes it a [smooth manifold](../../../Analysis/Analysis%20on%20Manifolds/Smooth%20Manifolds.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Open Sets

>[!INTUITION] Intuition: Open Balls in Euclidean Space
>
>Let $p \in \mathbb{R}^n$ be an element of the [Euclidean space](./index.md) $\mathbb{R}^n$.
>
>An [open ball](../../../Topology/Metric%20Spaces/index.md) $B_r(p)$ of radius $r$ around $p$ contains all $x \in \mathbb{R}^n$ whose distance from $p$ is less than$r$. It is essentially an $n$-dimensional sphere which is centred at $p$ and has radius $r$.
>

>[!TIP] Tip: Open Sets in Euclidean Space
>
>The [open subsets](../../../Topology/Topological%20Spaces/Open%20Sets.md) of the [Euclidean space](./index.md) $\mathbb{R}^n$ are precisely the following:
>- All [open balls](./index.md);
>- All [unions](../../../Set%20Theory/Collections/Operations%20with%20Collections.md) of arbitrary [collections](../../../Set%20Theory/Collections/index.md) of [open balls](./index.md);
>- All [intersections](../../../Set%20Theory/Collections/Operations%20with%20Collections.md) of finite [collections](../../../Set%20Theory/Collections/index.md) of [open balls](./index.md).
>

# Connectedness

>[!THEOREM] Theorem: Connectedness of Euclidean Space
>
>The [Euclidean space](./index.md) $\mathbb{R}^n$ is [connected](../../../Topology/Connectedness/index.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Connectedness on the Real Line
>
>All [intervals](../../../Set%20Theory/Ordering/Intervals.md) and [rays](../../../Set%20Theory/Ordering/Rays.md) in the [Euclidean space](./index.md) $\mathbb{R}$ of the real line are [connected](../../../Topology/Connectedness/index.md#^connected-subset).
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Compactness

>[!THEOREM] Heine-Borel Theorem: Compactness in Euclidean Space
>
>A [subspace](../../../Topology/Topological%20Subspaces.md) of the [Euclidean space](./index.md) $\mathbb{R}^n$ is [compact](../../../Topology/Compactness/index.md) if and only if it is [closed](../../../Topology/Topological%20Spaces/Closed%20Sets.md) and [bounded](../../../Topology/Metric%20Spaces/Boundedness%20in%20Metric%20Spaces.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]
>
>Every [closed interval](../../../Set%20Theory/Ordering/Intervals.md) of the [Euclidean space](./index.md) $\mathbb{R}$ is [compact](../../../Topology/Compactness/index.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>