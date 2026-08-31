---
tags:
    - topology
    - mathematics
---

# Manifold

>[!DEFINITION] Definition: Manifold
>
>A **manifold** is a [second-countable](../Bases/Second-Countable%20Topological%20Space.md) [Hausdorff space](../Hausdorff%20Space.md) $M$ which is [locally homeomorphic](../../Analysis/Continuity/Locally%20Homeomorphic%20Spaces.md) to some [Euclidean space](../../Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md) $\mathbb{R}^n$.
>
>>[!NOTATION]
>>
>>We often say that $M$ is an $n$-**manifold** and write $M^n$.
>>
>

>[!DEFINITION] Definition: Manifold
>
>An $n$-**(topological) manifold** is a [second-countable](../Bases/Base.md#Countability) [Hausdorff space](../Topological%20Spaces/Topological%20Space.md) which is [locally homeomorphic](../../Analysis/Continuity/Homeomorphism.md) to a [Euclidean space](../../Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md) $\mathbb{R}^n$.
>
>>[!NOTATION]
>>
>>$$
>>M^n
>>$$
>>
>
>
>>[!THEOREM] Theorem: Invariance of Dimension
>>
>>A [non-empty](../../Set%20Theory/Sets.md) [topological space](../Topological%20Spaces/Topological%20Space.md) cannot be both an $n$[-manifold](./Manifold.md) and an $m$[-manifold](./Manifold.md) with $n \ne m$.
>>
>>
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>>>[!DEFINITION] Definition: Dimension
>>>
>>>We say that $n$ is the **dimension** of $M$.
>>>
>>
>

>[!THEOREM] Theorem: Open Subsets of $n$-Manifolds
>
>Every [open](../Topological%20Spaces/Topological%20Space.md#Open%20Sets) [subset](../Topological%20Subspaces.md) of an $n$[-manifold](./Manifold.md) is also an $n$[-manifold](./Manifold.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!DEFINITION] Definition: Topological Manifolds with Boundary
>
>An **(topological) manifold with boundary** is a [second-countable](../Bases/Base.md#Countability) [Hausdorff space](../Topological%20Spaces/Topological%20Space.md) $(M, \tau)$ in which each point has a [neighborhood](../Topological%20Spaces/Topological%20Space.md#Neighborhoods) which is [homeomorphic](../../Analysis/Continuity/Homeomorphism.md) to an [open subset](../../Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md#SOpen%20Subsets) of the [Euclidean space](../../Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md) $\mathbb{R}^n$ or to an [open subset](../../Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md#SOpen%20Subsets) of the [subspace](../Topological%20Spaces/Topological%20Space.md) $\mathbb{R}^n_+$ of $\mathbb{R}^n$ defined by $\left\{\begin{bmatrix} x_1, \dotsc, x_n \end{bmatrix}^{\mathsf{T}} \in \mathbb{R}^n \mid x_n \ge 0\right\}$.
>
>>[!DEFINITION] Definition: Dimension
>>
>>We say that $n$ is the **dimension** of $(M, \tau)$.
>>
>
>>[!DEFINITION] Definition: Interior
>>
>>A point $p \in M$ is an **interior point** of $(M, \tau)$ if it has a a [neighborhood](../Topological%20Spaces/Topological%20Space.md#Neighborhoods) [homeomorphic](../../Analysis/Continuity/Homeomorphism.md) to an [open subset](../../Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md#SOpen%20Subsets) of $\mathbb{R}^n$.
>>
>>The **interior** of $(M, \tau)$ is the [set](../../Set%20Theory/Sets.md) of all its [interior points](./Manifold.md).
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\operatorname{int} M
>>>$$
>>>
>>
>
>>[!DEFINITION] Definition: Boundary
>>
>>A point $p \in M$ is a **boundary point** of $(M, \tau)$ if it has a a [neighborhood](../Topological%20Spaces/Topological%20Space.md#Neighborhoods) [homeomorphic](../../Analysis/Continuity/Homeomorphism.md) to an [open subset](../../Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md#SOpen%20Subsets) of $\mathbb{R}^n_+$.
>>
>>The **boundary** of $(M, \tau)$ is the [set](../../Set%20Theory/Sets.md) of all its [boundary points](./Manifold.md).
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\partial M
>>>$$
>>>
>>
>

>[!THEOREM] Theorem: Interior is a Manifold
>
>The [interior](./Manifold.md) of an $n$-dimensional [manifold with boundary](./Manifold.md) is an an $n$-dimensional [manifold without boundary](./Manifold.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Boundary is a Manifold
>
>The [boundary](./Manifold.md) of an $n$-dimensional [manifold with boundary](./Manifold.md) is an an $(n-1)$-dimensional [manifold without boundary](./Manifold.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Closedness of Boundary
>
>The [boundary](./Manifold.md) of a [manifold with boundary](./Manifold.md) $M$ is [closed](../Topological%20Spaces/Topological%20Space.md#Closed%20Sets) in $M$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Disjointness of Interior and Boundary
>
>The [interior](./Manifold.md) and [boundary](./Manifold.md) of a [manifold with boundary](./Manifold.md) $M$ are [disjoint](../../Set%20Theory/Sets.md#Operations) whose [union](../../Set%20Theory/Sets.md#Operations) is $M$:
>
>$$
>\mathop{\operatorname{int}} M \cap \partial M = \varnothing \qquad \text{ and } \qquad \mathop{\operatorname{int}} M \cup \partial M = M
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Manifold is a Manifold with Boundary
>
>An $n$-dimensional [manifold with boundary](./Manifold.md) $M$ is also an $n$-[manifold without boundary](./Manifold.md) if and only if $\partial M = \varnothing$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
