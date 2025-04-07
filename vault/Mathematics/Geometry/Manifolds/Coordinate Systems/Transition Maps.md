---
title: Transition Maps
tags:
  - coordinate-systems
  - manifolds
  - geometry
  - topology
---

>[!DEFINITION] Definition: Transition Map
>
>Let $(U_{\alpha}, \phi_{\alpha})$ and $(U_{\beta}, \phi_{\beta})$ be two [charts](index.md) for an $n$-[manifold](../Manifolds.md) such that the [intersection](../../../Set%20Theory/Set%20Operations.md) $U_{\alpha} \cap U_{\beta}$ is [nonempty](../../../Set%20Theory/Sets.md).
>
>The **transition map** from $(U_{\alpha}, \phi_{\alpha})$ to $(U_{\beta}, \phi_{\beta})$ is the [homeomorphism](../../../Topology/Continuity/Homeomorphisms/index.md) $\tau_{a\to b}: \phi_\alpha(U_\alpha \cap U_\beta) \to \phi_\beta(U_\alpha \cap U_\beta)$ which maps the [image](../../../Analysis/Functions/Functions.md) of $U_\alpha \cap U_\beta$ under $\phi_\alpha$ to its [image](../../../Analysis/Functions/Functions.md) under $\phi_\beta$ by [composing](../../../Analysis/Functions/Composition.md) $\phi_\beta$ and the [inverse](../../../Analysis/Functions/Injections,%20Surjections%20and%20Bijections.md) of $\phi_\alpha$:
>
>$$
>\tau_{ \alpha \to \beta} \overset{\text{def}}{=} \phi_\beta \circ \phi_\alpha^{-1}
>$$
>
>>[!INTUITION]-
>>
>>The transition map $\tau_{ \alpha \to \beta }$ is simply a change-of-coordinates operation, which converts coordinates from the coordinate system $\phi_{\alpha}$ to the coordinate system $\phi_{\beta}$. However, since coordinates on a manifold are only locally defined, such a change of coordinates makes sense only for those points which have coordinates in both systems, i.e. those points which belong to $U_{\alpha} \cap U_{\beta}$.
>>
>