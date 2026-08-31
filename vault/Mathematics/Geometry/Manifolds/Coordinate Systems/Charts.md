---
tags:
  - manifolds
  - geometry
  - topology
---

# Charts

>[!DEFINITION] Definition: Coordinate System
>
>Let $U$ be an [open set](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) of an $n$-[manifold](../../../Topology/Manifolds/Manifold.md).
>
>A **coordinate system** on $U$ is a [homeomorphism](../../../Analysis/Continuity/Homeomorphism.md) $\phi: U \to \mathbb{R}^n$ between the [subspace](../../../Topology/Topological%20Subspaces.md) $U$ and the [Euclidean space](../../../Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md) $\mathbb{R}^n$.
>
>>[!DEFINITION] Definition: Local Coordinates
>>
>>The [component functions](TODO) of $\phi$ are known as **(local) coordinates on** $U$. When evaluated at some $p \in U$, we call them **(local) coordinates of** $p$.
>>
>>>[!NOTATION]
>>>
>>>[Local coordinates](./Charts.md) of $\phi$ are usually denoted via superscripts:
>>>
>>>$$\phi^1 \qquad \cdots \qquad \phi^n$$
>>>
>>>$$p^k = \phi^k(p)$$
>>>
>>
>

>[!DEFINITION] Definition: Chart
>
>A **chart** $(U, \phi)$ on an $n$-[manifold](../../../Topology/Manifolds/Manifold.md) $M$ is an [open subset](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) $U \subseteq M$ equipped with a [coordinate system](./Charts.md) $\phi: U \to \mathbb{R}^n$.
>
>>[!NOTATION]
>>
>>We also write $(U, \phi^1, \dotsc, \phi^n)$ instead of $(U,\phi)$.
>>
>

>[!DEFINITION] Definition: Coordinate Curve
>
>Let $(U, \phi^1, \dotsc, \phi^n)$ be a [chart](./Charts.md) on an $n$-[manifold](../../../Topology/Manifolds/Manifold.md) and let $p \in U$.
>
>The **coordinate curve** of $\phi^k$ ($k \in \{1, \dotsc, n\}$) is the following [subset](../../../Set%20Theory/Subsets.md):
>
>$$\{c \in U \mid \phi^j(c) = \phi^j (p) \text{ for all } j \ne k\}$$
>