---
tags:
    - manifolds
    - geometry
    - topology
---

# Transition Maps

>[!DEFINITION] Definition: Transition Map
>
>Let $(U_{\alpha}, \phi_{\alpha})$ and $(U_{\beta}, \phi_{\beta})$ be two [charts](./Charts.md) on an $n$-[manifold](../../../Topology/Manifolds/Manifold.md) such that the [intersection](../../../Set%20Theory/Intersections.md) $U_{\alpha} \cap U_{\beta}$ is [non-empty](../../../Set%20Theory/Sets.md).
>
>The **transition map** from $(U_{\alpha}, \phi_{\alpha})$ to $(U_{\beta}, \phi_{\beta})$ is the [function](../../../Analysis/Real%20Analysis/Real%20Vector%20Fields/Real%20Vector%20Fields.md) $\tau_{\alpha \to \beta}: \phi_{\alpha}(U_{\alpha} \cap U_{\beta}) \to \phi_\beta(U_{\alpha} \cap U_{\beta})$ defined as the following [composition](../../../Analysis/Functions/Functions.md):
>
>$$\tau_{\alpha \to \beta} \overset{\text{def}}{=} \phi_{\beta} \circ \phi_{\alpha}^{-1}$$
>

[Transition maps](./Transition%20Maps.md) are transformations which allow us to change [coordinates](./Charts.md) between two [charts](./Charts.md) whenever they overlap somewhere. The way $\tau_{\alpha \to \beta}$ does this is  by first taking [coordinates](./Charts.md) $({p^1}_{\alpha}, \dotsc, {p^n}_{\alpha})$ w.r.t. $(U_{\alpha}, \phi_{\alpha})$ and mapping them to their corresponding $p \in M$. Then it maps $p$ to its [coordinates](./Charts.md) $({p^1}_{\beta}, \dotsc, {p^n}_{\beta})$ w.r.t. $(U_{\beta}, \phi_{\beta})$.

>[!THEOREM] Theorem: Homeomorphicity of Transition Maps
>
>Let $(U_{\alpha}, \phi_{\alpha})$ and $(U_{\beta}, \phi_{\beta})$ be two [charts](./Charts.md) on an $n$-[manifold](../../../Topology/Manifolds/Manifold.md) such that the [intersection](../../../Set%20Theory/Intersections.md) $U_{\alpha} \cap U_{\beta}$ is [non-empty](../../../Set%20Theory/Sets.md).
>
>The [transition map](./Transition%20Maps.md) $\tau_{\alpha \to \beta}: \phi_{\alpha}(U_{\alpha} \cap U_{\beta}) \to \phi_{\beta}(U_{\alpha} \cap U_{\beta})$ from $(U_{\alpha}, \phi_{\alpha})$ to $(U_{\beta}, \phi_{\beta})$ is a [homeomorphism](../../../Analysis/Continuity/Homeomorphism.md) and its [inverse](../../../Analysis/Functions/Injections,%20Surjections%20and%20Bijections.md) is the [transition map](./Transition%20Maps.md) $\tau_{\beta \to \alpha}: \phi_{\beta}(U_{\alpha} \cap U_{\beta}) \to \phi_{\alpha}(U_{\alpha} \cap U_{\beta})$ from $(U_{\beta}, \phi_{\beta})$ to $(U_{\alpha}, \phi_{\alpha})$.
>
>>[!PROOF]-
>>
>>TODO
>>
>