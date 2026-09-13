---
tags:
    - analysis
    - topology
    - mathematics
---

# Differentiable Structures

>[!DEFINITION] Definition: Smooth Compatibility
>
>Let $M$ be an [$n$-manifold](../../Topology/Manifolds/Manifold.md) or an [$n$-manifold with boundary](../../Topology/Manifolds/Manifold%20with%20Boundary.md) and let $(\mathcal{D}_{\varphi}, \varphi)$ and $(\mathcal{D}_{\psi}, \psi)$ be [charts](../../Topology/Manifolds/Charts.md) on $M$.
>
>We say that $(\mathcal{D}_{\varphi}, \varphi)$ and $(\mathcal{D}_{\psi}, \psi)$ are **differentially compatible of order $k$** if the [transition map](../../Topology/Manifolds/Transition%20Maps.md) $\psi \circ \varphi^{-1}$ is a [diffeomorphism](../Real%20Analysis/Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) or $\mathcal{D}_{\varphi} \cap \mathcal{D}_{\psi} = \varnothing$.
>

>[!DEFINITION] Definition: Smooth Atlas
>
>An [atlas](../../Topology/Manifolds/Manifold.md#Charts) for a [manifold](../../Topology/Manifolds/Manifold.md) is **smooth** if all of its [charts](../../Topology/Manifolds/Manifold.md#Charts) are pairwise [smoothly compatible](./Differentiable%20Structures.md).
>
>>[!DEFINITION] Definition: Maximal Smooth Atlas
>>
>>A [smooth atlas](./Differentiable%20Structures.md) $\mathcal{A}$ is **maximal** if there is no  [chart](../../Topology/Manifolds/Manifold.md#Charts) $(U, \varphi)$ which is pairwise [smoothly compatible](./Differentiable%20Structures.md) with the [charts](../../Topology/Manifolds/Manifold.md#Charts) in $\mathcal{A}$ such that $\mathcal{A} \cup \{(U, \varphi)\}$ is still a [smooth atlas](./Differentiable%20Structures.md).
>>
>

>[!DEFINITION] Definition: Differentiable Manifold
>
>A **differentiable manifold** or **smooth manifold** $(M, \mathcal{A})$ is a [manifold](../../Topology/Manifolds/Manifold.md) $M$ equipped with a [maximal smooth atlas](./Differentiable%20Structures.md) $\mathcal{A}$ on it.
>
>We call $\mathcal{A}$ the **differentiable structure** or **smooth structure** of $(M, \mathcal{A})$.
>
