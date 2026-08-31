---
tags:
    - mathematical-analysis-on-manifolds
    - mathematical-analysis
    - smooth-manifolds
    - mathematics
---

# Coordinate Representations

>[!DEFINITION] Definition: Coordinate Representation
>
>Let $M$ be an $m$-[manifold](../../Topology/Manifolds/Manifold.md), let $N$ be an $n$-[manifold](../../Topology/Manifolds/Manifold.md) and let $f: M \to N$ be a [function](../Functions/Functions.md). Let $(U_M, \phi_M)$ be a [chart](../../Geometry/Manifolds/Coordinate%20Systems/Charts.md) on $M$ and let $(U_N, \phi_N)$ be a [chart](../../Geometry/Manifolds/Coordinate%20Systems/Charts.md) on $N$.
>
>The **coordinate representation** of $f$ w.r.t. $(U_M, \phi_M)$ and $(U_N, \phi_N)$ is the [real vector function](../Real%20Analysis/Real%20Vector%20Functions/Real%20Vector%20Functions.md)
>
>$$\phi_M(U_M \cap f^{-1}(U_N)) \subseteq \mathbb{R}^m \to \phi_N(U_N) \subseteq \mathbb{R}^n$$
>
>defined as the following [composition](../Functions/Functions.md):
>
>$$\phi_N \circ f \circ \phi_M^{-1}$$
>

The [coordinate representation](./Coordinate%20Representations.md) $\phi_N \circ f \circ \phi_M^{-1}$ serves as a wrapper which allows us to express $f$ entirely using [coordinates](../../Geometry/Manifolds/Coordinate%20Systems/Charts.md). It does this by first taking [coordinates](../../Geometry/Manifolds/Coordinate%20Systems/Charts.md) ${}_{\phi_M}{p^1}, \dotsc, {}_{\phi_M}{p^m}$ and mapping them to $p \in M$ via $\phi_M^{-1}$. It then invokes $f$ on $p$ to obtain $f(p) \in N$. Finally, it uses $\phi_N$ to map $f(p)$ to [coordinates](../../Geometry/Manifolds/Coordinate%20Systems/Charts.md) ${}_{\phi_N}f(p)^{1}, \dotsc, {}_{\phi_N} f(p)^n$.