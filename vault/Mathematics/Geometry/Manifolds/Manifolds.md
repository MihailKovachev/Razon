---
title: Manifolds
tags:
    - manifolds
    - geometry
    - topology
---

# Manifolds

>[!DEFINITION] Definition: Manifold
>
>A **manifold** is a [second-countable](../../Topology/Bases/Second-Countability%20Axiom.md) [Hausdorff space](../../Topology/Hausdorff%20Spaces.md) which is [locally homeomorphic](../../Topology/Continuity/Homeomorphisms/Locally%20Homeomorphic%20Spaces.md) to a [Euclidean space](../../Analysis/Real%20Analysis/The%20Topology%20of%20Euclidean%20Space.md).
>

>[!THEOREM] Theorem: Invariance of Manifold Dimension
>
>A [nonempty](../../Set%20Theory/Sets.md) [topological space](../../Topology/Topological%20Spaces.md) cannot be [locally homeomorphic](../../Topology/Continuity/Homeomorphisms/Locally%20Homeomorphic%20Spaces.md) to more than one [Euclidean space](../../Analysis/Real%20Analysis/The%20Topology%20of%20Euclidean%20Space.md) - if it is [locally homeomorphic](../../Topology/Continuity/Homeomorphisms/Locally%20Homeomorphic%20Spaces.md) to $\mathbb{R}^n$ and to $\mathbb{R}^m$, then $n = m$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Dimension of a Manifold
>>
>>The **dimension** of a [manifold](Manifolds.md) is the [dimension](../../Algebra/Linear%20Algebra/Vector%20Spaces/Bases/Dimension.md) of the [Euclidean space](../../Analysis/Real%20Analysis/The%20Topology%20of%20Euclidean%20Space.md) which it is [locally homeomorphic](../../Topology/Continuity/Homeomorphisms/Locally%20Homeomorphic%20Spaces.md) to.
>>
>>>[!NOTATION]-
>>>
>>> The dimension of a manifold is such a fundamental property that we often denote it as a superscript on the manifold's name. If the manifold is $M$ and its dimension is $n$, we write $M^n$ and call $M$ an $n$-manifold or an $n$-dimensional manifold.
>>>
>>
>

## Manifolds with Boundary

>[!DEFINITION] Definition: Manifold with Boundary
>
>An $n$-dimensional **manifold with boundary** is a [second countable](../../Topology/Bases/Second-Countability%20Axiom.md) [Hausdorff space](../../Topology/Hausdorff%20Spaces.md) $M$ in which each point has a [neighbourhood](../../Topology/Topological%20Spaces.md) which is [homeomorphic](../../Topology/Continuity/Homeomorphisms/Homeomorphic%20Spaces.md) to the [Euclidean space](../../Analysis/Real%20Analysis/The%20Topology%20of%20Euclidean%20Space.md) $\mathbb{R}^n$ or to the [closed upper half-space](../Euclidean%20Geometry/Euclidean%20Space/Half-Spaces.md) $\mathbb{H}^n$.
>
>>[!DEFINITION] Definition: Manifold Interior
>>
>>A point $p \in M$ is an **interior point** of $M$ iff $p$ has a [neighbourhood](../../Topology/Topological%20Spaces.md) which is [homeomorphic](../../Topology/Continuity/Homeomorphisms/Homeomorphic%20Spaces.md) to the [Euclidean space](../../Analysis/Real%20Analysis/The%20Topology%20of%20Euclidean%20Space.md) $\mathbb{R}^n$.
>>
>>The **interior** of $M$ is the [set](../../Set%20Theory/Sets.md) of all its interior points.
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\operatorname{Int} M
>>>$$
>>>
>>
>
>>[!DEFINITION] Definition: Boundary
>>
>>The **boundary** of $M$ is the [complement](../../Set%20Theory/Complement.md) of $M$'s interior in $M$.
>>
>>$$
>>M \setminus \operatorname{Int} M
>>$$
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\partial M
>>>$$
>>>
>>
>>>[!WARNING]
>>>
>>>Despite the name and terminology used, the interior and boundary of a manifold with boundary $M$ are not necessarily the same as its [interior](../../Topology/Interior,%20Boundary%20and%20Exterior.md) and [boundary](../../Topology/Interior,%20Boundary%20and%20Exterior.md) when $M$ is considered a [subset](../../Set%20Theory/Sets.md) of some other [topological space](../../Topology/Topological%20Spaces.md).
>>>
>>
>
