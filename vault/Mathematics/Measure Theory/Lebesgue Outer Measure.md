---
tags:
    - measure-theory
    - mathematics
---

# Lebesgue Outer Measure

>[!DEFINITION] Definition: Lebesgue Outer Measure
>
>Let $n \in \mathbb{N}$ and let $\mathcal{P}(\mathbb{R}^n)$ be the [power set](../Set%20Theory/Power%20Set.md) of the [Euclidean space](../Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md) $\mathbb{R}^n$. For each [open cuboid](../Set%20Theory/Orderings/Cuboids.md) $C = (a_1, b_1)\times \cdots \times (a_n, b_n) \subseteq \mathbb{R}^n$, let $\operatorname{vol}(C)$ denote the **volume** of $C$:
>
>$$\operatorname{vol}(C) \overset{\text{def}}{=} \prod_{k = 1}^n (b_k - a_k)$$
>
>The **Lebesgue outer measure** is the [function](../Analysis/Functions/Functions.md) $\lambda^{\ast}: \mathcal{P}(\mathbb{R}^n) \to [0,\infty]$ from $\mathcal{P}(\mathbb{R}^n)$ to the [subspace](../Topology/Topological%20Subspaces.md) of the [non-negative extended real number line](../Analysis/Real%20Analysis/Extended%20Real%20Number%20Line.md) defined for each $S \subseteq \mathbb{R}^n$ as the [infimum](../Set%20Theory/Orderings/Infimum.md) of all [sums](TODO) of [volumes](./Lebesgue%20Outer%20Measure.md) of [sequences](../Analysis/Functional%20Analysis/Sequences/Sequences.md) of [open cuboids](../Set%20Theory/Orderings/Cuboids.md) which [cover](../Set%20Theory/Covers.md) $S$:
>
>$$\lambda^{\ast}(S) \overset{\text{def}}{=} \inf \left\{ \sum_{k \in \mathcal{I}} \operatorname{vol}(C_k) : (C_k)_{k \in \mathcal{I}} \text{ is a sequence of open cuboids with } S \subseteq \bigcup_{k \in \mathcal{I}} C_k\right\}$$
>

>[!THEOREM] Theorem: Lebesgue Outer Measure
>
>The [Lebesgue outer measure](./Lebesgue%20Outer%20Measure.md) $\lambda^{\ast}: \mathcal{P}(\mathbb{R}^n) \to [0,\infty]$ is an [outer measure](./Outer%20Measures.md) on the [Euclidean space](../Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md) $\mathbb{R}^n$.
>
>>[!PROOF]-
>>
>>TODO
>>
>