---
tags:
    - measure-theory
    - mathematics
---

# Pushforward

>[!DEFINITION] Definition: Pushforward
>
>Let $(X, \Sigma_X)$ and $(Y, \Sigma_Y)$ be [measurable spaces](./Measurable%20Space.md), let $f: X \to Y$ be a [measurable](./Measurable%20Functions.md) [function](../Analysis/Functions/Functions.md) and let $\mu: \Sigma_X \to [0,\infty]$ be a [measure](./Measures.md) on $(X, \Sigma_X)$.
>
>The **pushforward** of $\mu$ by $f$ is the [function](TODO) $g: \Sigma_Y \to [0, \infty]$ defined for each $S \in \Sigma_Y$ as the [measure](./Measures.md) of $S$'s [preimage](TODO) under $f$:
>
>$$g(S) \overset{\text{def}}{=} \mu (f^{-1}(S))$$
>
>>[!NOTATION]
>>
>>We denote $g$ in one of the following ways:
>>
>>$$f_{\ast}(\mu) \qquad \mu \circ f^{-1} \qquad f_{\sharp} \mu \qquad f_{\#}\mu \qquad f\# \mu$$
>>
>