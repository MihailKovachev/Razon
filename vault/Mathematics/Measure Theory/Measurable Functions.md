---
title: Measurable Functions
tags:
    - measure-theory
    - mathematics
---

# Measurable Functions

>[!DEFINITION] Definition: Measurable Functions
>
>Let $(X, \Sigma_X)$ and $(Y, \Sigma_Y)$ be [measurable spaces](./Measurable%20Space.md).
>
>A [function](../Analysis/Functions/Functions.md) $f: \mathcal{D} \subseteq X \to Y$ is **measurable** if the [inverse image](../Analysis/Functions/Functions.md) of each [measurable set](./Measurable%20Space.md) of $(Y, \Sigma_Y)$ is a [measurable set](./Measurable%20Space.md) of $(X, \Sigma_X)$:
>
>$$f^{-1}(S) \in \Sigma_X \qquad \forall S \in \Sigma_Y$$
>

>[!THEOREM] Theorem: Composition of Measurables is Measurable
>
>Let $(X, \Sigma_X)$, $(Y, \Sigma_Y)$ and $(Z, \Sigma_Z)$ be [measurable spaces](./Measurable%20Space.md) and let $g: \mathcal{D}_g \subseteq X \to Y$ and $f: \mathcal{D}_f \subseteq Y \to Z$ be [functions](../Analysis/Functions/Functions.md).
>
>If $g$ is $(\Sigma_X, \Sigma_Y)$[-measurable](./Measurable%20Functions.md) and $f$ is $(\Sigma_Y, \Sigma_Z)$[-measurable](./Measurable%20Functions.md), then the [composition](../Analysis/Functions/Composition%20(Functions).md) $f \circ g: \mathcal{D}_g \to Z$ is $(\Sigma_X, \Sigma_Z)$[-measurable](./Measurable%20Functions.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>