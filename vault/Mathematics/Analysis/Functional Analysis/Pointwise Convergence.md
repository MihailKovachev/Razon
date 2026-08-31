---
tags:
    - functional-analysis
    - analysis
    - mathematics
---

# Pointwise Convergence

>[!DEFINITION] Definition: Pointwise Convergence
>
>Let $X$ be a [set](../../Set%20Theory/Sets.md), let $Y$ be a [topological space](../../Topology/Topological%20Spaces/Topological%20Space.md) and let $(f_n)_{n \in \mathcal{I}}$ be a [sequence](./Sequences/Sequences.md) of [functions](../Functions/Functions.md) from $X$ to $Y$.
>
>A **pointwise limit** of $(f_n)_{n \in \mathcal{I}}$ is any [function](../Functions/Functions.md) $f: X \to Y$ such that  $f(x)$ is a [limit](./Sequences/Limits%20(Sequences).md) of the [sequence](./Sequences/Sequences.md) $(f_n(x))_{n \in \mathcal{I}}$ for each $x \in X$:
>
>$$\forall x \in X: (f_n(x))_{n \in \mathcal{I}} \to f(x)$$
>
>If $f$ is a [pointwise limit](./Pointwise%20Convergence.md) of $(f_n)_{n \in \mathcal{I}}$, then we say that $(f_n)_{n \in \mathcal{I}}$ **converges pointwise** to $f$.
>
>>[!NOTATION]
>>
>>If $f$ is a [pointwise limit](./Pointwise%20Convergence.md) of $(f_n)_{n \in \mathcal{I}}$, then we write
>>
>>$$(f_n)_{n \in \mathcal{I}} \to f \text{ pointwise}.$$
>>
>>If $f$ is the only [pointwise limit](./Pointwise%20Convergence.md) of $(f_n)_{n \in \mathcal{I}}$, then we can also write:
>>
>>$$\lim f_n = f \text{ pointwise}$$
>>
>>If $f$ is the only [pointwise limit](./Pointwise%20Convergence.md) of $(f_n)_{n \in \mathcal{I}}$ and $(f_n)_{n \in \mathcal{I}}$ is [infinite](./Sequences/Sequences.md), then we can also write:
>>
>>$$\lim_{n \to \infty} f_n = f \text{ pointwise}$$
>>
>