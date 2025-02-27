---
title: Coordinate Systems
tags:
  - coordinate-systems
  - manifolds
  - geometry
  - topology
---

# Coordinate Systems on Manifolds

>[!DEFINITION] Definition: Coordinate System
>
>Let $U$ be an [open subset](../../../Topology/Topological%20Spaces/Open%20Sets.md) of an $n$-[manifold](../Manifolds.md) $M$.
>
>A **coordinate system** or **coordinate map** on $U$ is a [homeomorphism](../../../Topology/Continuity/Homeomorphisms/index.md) $\phi: U \to \mathbb{R}^n$ from the [subspace](../../../Topology/Topological%20Subspaces.md) $U$ to an [open subset](../../../Topology/Topological%20Spaces/Open%20Sets.md) of the [Euclidean space](../../../Analysis/Real%20Analysis/The%20Topology%20of%20Euclidean%20Space.md) $\mathbb{R}^n$.
>
>>[!DEFINITION] Definition: Coordinates on a Subset
>>
>>The [component functions](../../../Analysis/Real%20Analysis/Real%20Vector-Valued%20Function.md) $\phi^1, \dotsc, \phi^n: U \to \mathbb{R}$ of $\phi$ are known as **local coordinates** or simply **coordinates** on $U$.
>>
>>>[!NOTATION]-
>>>
>>>The component functions of a coordinate system $\phi$ are usually denoted using superscripts instead of subscripts, i.e. $\phi^1, \dotsc, \phi^n$ instead of $\phi_1, \dotsc, \phi_n$.
>>>
>>
>
>>[!DEFINITION] Definition: Coordinates of a Point
>>
>>Given a point $p \in U$, we call $\phi^k(p)$ the $k$-th **coordinate** of $p$.
>>
>>>[!NOTATION]-
>>>
>>>The coordinates of a point $p$ are usually written together as an $n$-[tuple](../../../Set%20Theory/Tuples.md):
>>>
>>>$$
>>>(\phi^1(p), \dotsc, \phi^n(p))
>>>$$
>>>
>>>Oftentimes, we denote the coordinates of $p$ using superscripts in order to make it clear that they are coordinates of some point:
>>>
>>>$$
>>>(p^1, \dotsc, p^n),
>>>$$
>>>
>>>where $p^k = \phi_k(p)$.
>>>
>>
>
>>[!INTUITION]-
>>
>>In its essence, a coordinate system is just a way to identify each point of $U$ with a point (vector) of $\mathbb{R}^n$. More importantly, it is a way to *uniquely* do so, since $\phi$ is a homeomorphism and therefore bijective. No two points of $U$ can correspond to the same vector of $\mathbb{R}^n$ and no two vectors in $\mathbb{R}^n$ can correspond to the same point in $U$. This means that each point $u \in U$ can be uniquely assigned coordinates
>>
>>$$
>>u^1 = \phi_1(u), \dotsc, u^n = \phi_n(u)
>>$$
>>
>>Another useful property of coordinate systems is the fact that they are continuous (since they are homeomorphism by definition). Intuitively, this means that if two points $p$ and $q$ of $U$ are "close", then the [Euclidean distance](../../../Algebra/Linear%20Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Euclidean%20Distance.md) between the vectors they correspond to will be small.
>>
>


>[!DEFINITION] Definition: Origin of a Coordinate System
>
>We say that a point $p \in U$ is the **origin** of $\phi$ or that $\phi$ is **centered** at $p$ iff $\varphi(p) = \vec{0}$.
>

>[!DEFINITION] Definition: Global Coordinate System
>
>A [coordinate system](index.md) on an $n$-[manifold](../Manifolds.md) $M$ is **global** iff its [domain](../../../Analysis/Functions/Functions.md) is the entirety of $M$.
>
>>[!INTUITION]-
>>
>>A global coordinate system extends to the entire manifold - each point $p \in M$ can be uniquely assigned $n$ coordinates.
>>
>
>>[!WARNING]
>>
>>Most manifolds do *not* admit global coordinate systems because this would require that they are [homeomorphic](../../../Topology/Continuity/Homeomorphisms/Homeomorphic%20Spaces.md) to $\mathbb{R}^n$.
>>
>

## Charts on Manifolds

>[!DEFINITION] Definition: Chart
>
>Let $M$ be an $n$-[manifold](../Manifolds.md).
>
>A **chart** $(U, \phi)$ for $M$ is an [open subset](../../../Topology/Topological%20Spaces/Open%20Sets.md) $U \subseteq M$ equipped with a [coordinate system](index.md) $\phi: U \to \mathbb{R}^n$ on it.
>
>>[!DEFINITION] Definition: Coordinate Domain
>>
>>We call $U$ the **coordinate domain** of $(U, \phi)$.
>>
>

>[!DEFINITION] Definition: Chart Compatibility
>
>Let $(U_{\alpha}, \phi_{\alpha})$ and $(U_{\beta}, \phi_{\beta})$ be two [charts](index.md) on an $n$-[manifold](../Manifolds.md) $M$.
>
>We say that $(U_{\alpha}, \phi_{\alpha})$ and $(U_{\beta}, \phi_{\beta})$ are $C^k$-**compatible** (where $k \in \mathbb{N}_0\cup \{\infty\}$) iff the [transition maps](Transition%20Maps.md) between them are $k$-times [continuously partially differentiable](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Differentiation/Partial%20Derivatives%20of%20Real%20Vector%20Functions.md) or $U_{\alpha} \cap U_{\beta} = \varnothing$. 
>

