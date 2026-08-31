---
tags:
    - analysis
    - mathematics
---

# Limit Inferior

>[!DEFINITION] Definition: Limit Inferior
>
>Let $(X, \le)$ be a [partially ordered set](../../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md) and let $(x_n)_{n \in \mathcal{I}}$ be a [sequence](./Sequences.md) of points in $X$.
>
>The **limit inferior** of $(x_n)_{n \in \mathcal{I}}$ is the [supremum](../../../Set%20Theory/Orderings/Supremum.md) of the [infimums](../../../Set%20Theory/Orderings/Infimum.md) of all [tail sequences](./Tail%20Sequences.md) of $(x_n)_{n \in \mathcal{I}}$ (if all those exist):
>
>$$\sup_{n \in \mathcal{I}} \inf \{ x_k \mid k \geq n \}$$
>
>>[!NOTATION]
>>
>>If this value exists, we denote it in the following way:
>>
>>$$\liminf x_n$$
>>
>>If $(x_n)_{n \in \mathcal{I}}$ is [infinite](./Sequences.md), we often write the following:
>>
>>$$\liminf_{n \to \infty} x_n$$
>>
>