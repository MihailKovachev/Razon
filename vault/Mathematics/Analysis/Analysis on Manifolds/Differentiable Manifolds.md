---
title: Differentiable Manifolds
tags:
    - mathematical-analysis
    - topology
    - mathematics
---

# Differentiable Manifolds

>[!DEFINITION] Definition: Smooth Compatibility
>
>Let $(\mathcal{D}_{\varphi}, \varphi)$ and $(\mathcal{D}_{\psi}, \psi)$ be [charts](../../Topology/Manifolds/Manifold.md#Charts) on a [manifold](../../Topology/Manifolds/Manifold.md).
>
>We say that $(\mathcal{D}_{\varphi}, \varphi)$ and $(\mathcal{D}_{\psi}, \psi)$ are **smoothly compatible** if the [transition map](../../Topology/Manifolds/Manifold.md#Charts) $\psi \circ \varphi^{-1}$ is a [diffeomorphism](../Real%20Analysis/Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) or $\mathcal{D}_{\varphi} \cap \mathcal{D}_{\psi} = \varnothing$.
>

>[!DEFINITION] Definition: Smooth Atlas
>
>An [atlas](../../Topology/Manifolds/Manifold.md#Charts) for a [manifold](../../Topology/Manifolds/Manifold.md) is **smooth** if all of its [charts](../../Topology/Manifolds/Manifold.md#Charts) are pairwise [smoothly compatible](./Differentiable%20Manifolds.md).
>
>>[!DEFINITION] Definition: Maximal Smooth Atlas
>>
>>A [smooth atlas](./Differentiable%20Manifolds.md) $\mathcal{A}$ is **maximal** if there is no  [chart](../../Topology/Manifolds/Manifold.md#Charts) $(U, \varphi)$ which is pairwise [smoothly compatible](./Differentiable%20Manifolds.md) with the [charts](../../Topology/Manifolds/Manifold.md#Charts) in $\mathcal{A}$ such that $\mathcal{A} \cup \{(U, \varphi)\}$ is still a [smooth atlas](./Differentiable%20Manifolds.md).
>>
>

>[!DEFINITION] Definition: Differentiable Manifold
>
>A **differentiable manifold** or **smooth manifold** $(M, \mathcal{A})$ is a [manifold](../../Topology/Manifolds/Manifold.md) $M$ equipped with a [maximal smooth atlas](./Differentiable%20Manifolds.md) $\mathcal{A}$ on it.
>
>We call $\mathcal{A}$ the **differentiable structure** or **smooth structure** of $(M, \mathcal{A})$.
>
