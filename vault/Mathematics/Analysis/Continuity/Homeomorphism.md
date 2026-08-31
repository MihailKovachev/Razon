---
tags:
    - analysis
    - topology
    - mathematics
---

# Homeomorphism

>[!DEFINITION] Definition: Homeomorphism
>
>Let $X$ and $Y$ be [topological spaces](../../Topology/Topological%20Spaces/Topological%20Space.md).
>
>A **homeomorphism** between $X$ and $Y$ is a [continuous](./Continuity.md) [bijection](../Functions/Bijections.md) $f: X \to Y$ whose [inverse](../Functions/Injections,%20Surjections%20and%20Bijections.md#Injections) $f^{-1}: Y \to X$ is also [continuous](./Continuity.md).
>

>[!THEOREM] Theorem: Composition of Homeomorphisms
>
>Let $(X, \tau_X)$, $(Y, \tau_Y)$ and $(Z, \tau_Z)$ be [topological spaces](../../Topology/Topological%20Spaces/Topological%20Space.md).
>
>If $f: X \to Y$ and $g: Y \to Z$ are [homeomorphisms](./Homeomorphism.md), then their [composition](../Functions/Functions.md) $g \circ f: X \to Z$ is also a [homeomorphism](./Homeomorphism.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Interior $\to$ Interior
>
>Let $X$ and $Y$ be [topological spaces](../../Topology/Topological%20Spaces/Topological%20Space.md), let $f: X \to Y$ be a [homeomorphism](./Homeomorphism.md) between them and let $S$ be a [subset](../../Set%20Theory/Subsets.md) of $X$.
>
>If $p \in S$ is an [interior point](../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $S$, then $f(p)$ is an [interior point](../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $f(S)$:
>
>$$p \in \operatorname{int} S \implies f(p) \in \operatorname{int} f(S)$$
>
>$$f(\operatorname{int} S) = \operatorname{int} f(S)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Boundary $\to$ Boundary
>
>Let $X$ and $Y$ be [topological spaces](../../Topology/Topological%20Spaces/Topological%20Space.md), let $f: X \to Y$ be a [homeomorphism](./Homeomorphism.md) between them and let $S$ be a [subset](../../Set%20Theory/Subsets.md) of $X$.
>
>If $p \in X$ is a [boundary point](../../Topology/Topological%20Spaces/Boundary%20(Topology).md) of $S$, then $f(p)$ is a [boundary point](../../Topology/Topological%20Spaces/Boundary%20(Topology).md) of $f(S)$:
>
>$$p \in \partial S \implies f(p) \in \partial f(S)$$
>
>$$f(\partial S) = \partial f(S)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>