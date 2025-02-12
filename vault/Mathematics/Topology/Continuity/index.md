---
title: Continuity
tags:
  - continuity
  - topology
  - mathematics
---

# Continuity

>[!DEFINITION] Definition: Continuity at a Point
>
>Let $(X,\tau_X)$ and $(Y,\tau_Y)$ be [topological spaces](../Topological%20Spaces/index.md).
>
>A [function](../../Analysis/Functions/index.md) $f: X \to Y$ is **continuous at** $x \in X$ iff for each [neighbourhood](../Topological%20Spaces/Neighborhoods.md) $V$ of $f(x)$ there exists a neighbourhood $U$ of $x$ such that $f(U) \subset V$.
>

>[!DEFINITION] Definition: Continuity
>
>Let $(X,\tau_X)$ and $(Y,\tau_Y)$ be [topological spaces](../Topological%20Spaces/index.md).
>
>A [function](../../Analysis/Functions/index.md) $f: X \to Y$ is **continuous on** $X$ or simply **continuous** iff it is [continuous](../../Analysis/Real%20Analysis/Real%20Functions/Continuity.md) at each $x \in X$.

## Continuity Criteria

>[!THEOREM]- Theorem: Continuity via Openness
>
>Let $(X,\tau_X)$ and $(Y,\tau_Y)$ be [topological spaces](../Topological%20Spaces/index.md).
>
>A [function](../../Analysis/Functions/index.md) $f: X \to Y$ is [continuous](./index.md) if and only if the [inverse image](../../Analysis/Functions/index.md) of each [open subset](../Topological%20Spaces/Open%20Sets.md) of $Y$ is an open subset of $X$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Continuity via Closedness
>
>Let $(X,\tau_X)$ and $(Y,\tau_Y)$ be [topological spaces](../Topological%20Spaces/index.md).
>
>A [function](../../Analysis/Functions/index.md) $f: X \to Y$ is [continuous](./index.md) if and only if the [inverse image](../../Analysis/Functions/index.md) of each [closed subset](../Topological%20Spaces/Closed%20Sets.md) of $Y$ is a [closed subset](../Topological%20Spaces/Closed%20Sets.md) of $X$.
>
>>[!PROOF]-
>>
>>TODO
>>
>>

>[!THEOREM]- Theorem: Local Criterion
>
>Let $(X,\tau_X)$ and $(Y,\tau_Y)$ be [topological spaces](../Topological%20Spaces/index.md).
>
>A [function](../../Analysis/Functions/index.md) $f: X \to Y$ is [continuous](./index.md) if and only if each point $x \in X$ has a [neighbourhood](../Topological%20Spaces/Neighborhoods.md) $N$ such that the [restriction](../../Analysis/Functions/Restriction.md) $f\big|_N$ is [continuous](./index.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Properties

>[!THEOREM]- Extreme Value Theorem
>
>Let $(X, \tau_X)$ and $(Y,\tau_Y)$ be [topological spaces](../Topological%20Spaces/index.md).
>
>If $(X,\tau_X)$ is [compact](../Compactness/index.md), then its [image](../../Analysis/Functions/index.md) $f(X)$ under every [continuous function](./index.md) $f: X \to Y$ is also [compact](../Compactness/index.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Continuity of Composition
>
>Let $(X, \tau_X)$, $(Y, \tau_Y)$ and $(Z, \tau_Z)$ be [topological spaces](../Topological%20Spaces/index.md).
>
>If $f: X \to Y$ and $g: Y \to Z$ are [continuous](./index.md), then so is their [composition](../../Analysis/Functions/Composition.md) $g \circ f: X \to Z$.
>
>>[!PROOF]-
>>
>>We need to prove only that if $U$ is [open](../Topological%20Spaces/Open%20Sets.md) in $(Z, \tau_Z)$, then its [inverse image](../../Analysis/Functions/index.md)  $(g\circ f)^{-1}(U)$ is [open](../Topological%20Spaces/Open%20Sets.md) in $(X, \tau_X)$.
>>
>>
>>
>>Let $U$ be [open](../Topological%20Spaces/Open%20Sets.md) in $(Z, \tau_Z)$. We know that $(g\circ f)^{-1}(U) = f^{-1}(g^{-1}(U))$. Since $g$ is [](index.md#^continuity) and $U$ is [open](../Topological%20Spaces/Open%20Sets.md) in $(Z, \tau_Z)$, the aforementioned theorem tells us that $g^{-1}(U)$ is [open](../Topological%20Spaces/Open%20Sets.md) in $(Y, \tau_Y)$. Analogously, since $f$ is [](index.md#^continuity) and $g^{-1}(U)$ is [open](../Topological%20Spaces/Open%20Sets.md) in $(Y, \tau_Y)$, the theorem tells us that $f^{-1}(g^{-1}(U))$ is [](index.md#^continuity) in $(X,\tau_X)$.
>>
>

>[!THEOREM]- Theorem: Continuity of Restrictions
>
>Let $(X, \tau_X)$ and $(Y, \tau_Y)$ be [topological spaces](../Topological%20Spaces/index.md).
>
>If $f: X \to Y$ is [continuous](./index.md) and $S$ is an [open subset](../Topological%20Spaces/Open%20Sets.md) of $X$, then the [restriction](../../Analysis/Functions/Restriction.md) $f\big|_S$ is also [continuous](./index.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Intermediate Value Theorem
>
>Let $(X, \tau_X)$ and $(Y, \tau_Y)$ be [topological spaces](../Topological%20Spaces/index.md).
>
>If $(X, \tau_X)$ is [connected](../Connectedness/index.md), then so its [image](../../Analysis/Functions/index.md) $f(X)$ under any [continuous function](../Continuity/index.md) $f: X \to Y$.
>
>>[!PROOF]-
>>
>>TODO
>>
>