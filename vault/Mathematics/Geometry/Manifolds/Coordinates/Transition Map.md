>[!DEFINITION] Definition: Transition Map
>
>Let $(U_\alpha, \phi_\beta)$ and $(U_\alpha, \phi_\beta)$ be two [charts](Coordinates/Chart.md) for an $n$-[dimensional](Dimension%20of%20a%20Manifold.md) [manifold](Manifold.md) such that the [intersection](../../../Set%20Theory/Operations%20with%20Sets/Intersection.md) $U_\alpha \cap U_\beta$ is [nonempty](../../../Set%20Theory/The%20Empty%20Set.md).
>
>The **transition map** from $(U_\alpha, \phi_\beta)$ to $(U_\alpha, \phi_\beta)$ is the [homeomorphism](../../../Topology/Continuity/Homeomorphisms/Homeomorphism.md) $\tau_{a\to b}: \phi_\alpha(U_\alpha \cap U_\beta) \to \phi_\beta(U_\alpha \cap U_\beta)$ which maps the [image](../../../Analysis/Functions/Image%20of%20a%20Function.md) of $U_\alpha \cap U_\beta$ under $\phi_\alpha$ to its [image](../../../Analysis/Functions/Image%20of%20a%20Function.md) under $\phi_\beta$ by [composing](../../../Analysis/Functions/Composition.md) $\phi_\beta$ and the [inverse](../../../Analysis/Functions/Types%20of%20Functions/Inverse%20Function.md) of $\phi_\alpha$:
>
>$$
>\tau_{\alpha\to\beta} \overset{\text{def}}{=} \phi_\beta \circ \phi_\alpha^{-1}
>$$
>