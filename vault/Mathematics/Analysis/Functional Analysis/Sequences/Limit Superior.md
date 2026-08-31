---
tags:
    - analysis
    - mathematics
---

# Limit Superior

>[!DEFINITION] Definition: Limit Superior
>
>Let $(X, \le)$ be a [partially ordered set](../../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md) and let $(x_n)_{n \in \mathcal{I}}$ be a [sequence](./Sequences.md) of points in $X$.
>
>The **limit superior** of $(x_n)_{n \in \mathcal{I}}$ is the [infimum](../../../Set%20Theory/Orderings/Infimum.md) of the [supremums](../../../Set%20Theory/Orderings/Supremum.md) of all [tail sequences](./Tail%20Sequences.md) of $(x_n)_{n \in \mathcal{I}}$ (if all those exist):
>
>$$\inf_{n \in \mathcal{I}} \sup \{ x_k \mid k \geq n \}$$
>
>>[!NOTATION]
>>
>>If this value exists, we denote it in the following way:
>>
>>$$\limsup x_n$$
>>
>>If $(x_n)_{n \in \mathcal{I}}$ is [infinite](./Sequences.md), we often write the following:
>>
>>$$\limsup_{n \to \infty} x_n$$
>>
