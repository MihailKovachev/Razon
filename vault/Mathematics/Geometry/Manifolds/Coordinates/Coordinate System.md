>[!DEFINITION] Definition: Coordinate System
>
>Let $U$ be an [open subset](../../../Topology/Topological%20Spaces/Open%20Subset.md) of an $n$-[dimensional](Dimension%20of%20a%20Manifold.md) [manifold](Manifold.md) $M$.
>
>A **coordinate system** or **coordinate map** on $U$ is a [homeomorphism](../../../Topology/Continuity/Homeomorphisms/Homeomorphism.md) $\phi: U \to \mathbb{R}^n$ from the [subspace](../../../Topology/Subspaces/Topological%20Subspace.md) $U$ to an [open subset](../../../Topology/Topological%20Spaces/Open%20Subset.md) of the [Euclidean space](../../Euclidean%20Geometry/Euclidean%20Space/Euclidean%20Space.md) $\mathbb{R}^n$.
>
>>[!DEFINITION] Definition: Coordinates on a Subset
>>
>>The [component functions](../../../Analysis/Real%20Analysis/Multivariate%20Real%20Analysis/Real%20Vector-Valued%20Function.md) $\phi_1, \dotsc, \phi_n: U \to \mathbb{R}$ of $\phi$ are known as **local coordinates** or simply **coordinates** on $U$.
>>
>
>>[!DEFINITION] Definition: Coordinates of a Point
>>
>>Given a point $p \in U$, we call $\phi_k(p)$ the $k$-th **coordinate** of $p$.
>>
>>>[!NOTATION]-
>>>
>>>The coordinates of a point $p$ are usually written together as an $n$-[tuple](../../../Set%20Theory/Tuple.md):
>>>
>>>$$
>>>(\phi_1(p), \dotsc, \phi_n(p))
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
>>In fact, we usually ignore that $f(u)$ is a vector and we simply treat it as an $n$-tuple because what really matters for coordinates are the components of $f(u)$, i.e. $u^1, \cdots, u^n$, and not the other properties which vectors can possess.
>>
>>Another useful property of coordinate systems is the fact that they are continuous (since they are homeomorphism by definition). Intuitively, this means that if two points $p$ and $q$ of $U$ are "close", then their coordinates will be close real numbers.
>>
>


>[!DEFINITION] Definition: Origin of a Coordinate System
>
>We say that a point $p \in U$ is the **origin** of $\phi$ or that $\phi$ is **centered** at $p$ iff $\varphi(p) = \vec{0}$.
>
