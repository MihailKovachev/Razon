---
title: Homeomorphisms
tags:
  - homeomorphisms
  - continuity
  - topology
  - mathematics
---

# Homeomorphisms

>[!DEFINITION] Definition: Homeomorphism
>
>Let $(X, \tau_X)$ and $(Y,\tau_Y)$ be [topological spaces](../../Topological%20Spaces/index.md).
>
>A **homeomorphism** between $X$ and $Y$ is a [continuous](../index.md#^continuity) [bijection](../../../Analysis/Functions/Types%20of%20Functions/Bijection.md) $f: X \to Y$ with a continuous [inverse](../../../Analysis/Functions/Types%20of%20Functions/Injection.md) $f^{-1}: Y \to X$.

## Criteria for Homeomorphisms

>[!THEOREM]- Theorem: Equivalent Definition
>
>A [bijection](../../../Analysis/Functions/Types%20of%20Functions/Bijection.md) $f: X \to Y$ between two [topological spaces](../../Topological%20Spaces/index.md) $(X, \tau_X)$ and $(Y, \tau_Y)$ is a [homeomorphism](Homeomorphism.md) if and only if the [image](../../../Analysis/Functions/index.md) of each [open subset](../../Topological%20Spaces/Open%20Sets.md) of $(X, \tau_X)$ is [open](../../Topological%20Spaces/Open%20Sets.md) in $(Y, \tau_Y)$ and the [inverse image](../../../Analysis/Functions/index.md) of each [open subset](../../Topological%20Spaces/Open%20Sets.md) in $(Y, \tau_Y)$ is [open](../../Topological%20Spaces/Open%20Sets.md) in $(X, \tau_X)$.
>
>>[!PROOF]-
>>
>>We have to prove two things:
>>- (I) If $f: X \to Y$ is a [homeomorphism](Homeomorphism.md), then the [image](../../../Analysis/Functions/index.md) $f(U)$ of each [open subset](../../Topological%20Spaces/Open%20Sets.md) $U$ of $(X, \tau_X)$ is [open](../../Topological%20Spaces/Open%20Sets.md) in $(Y, \tau_Y)$.
>>- (II) If $f: X \to Y$ is a [bijection](../../../Analysis/Functions/Types%20of%20Functions/Bijection.md) and the [image](../../../Analysis/Functions/index.md) $f(U)$ of each [open subset](../../Topological%20Spaces/Open%20Sets.md) $U$ of $(X, \tau_X)$ is [open](../../Topological%20Spaces/Open%20Sets.md) in $(Y, \tau_Y)$, then $f$ is a [homeomorphism](Homeomorphism.md).
>>
>>**Proof of (I):**
>>
>>**Proof of (II):**
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Homeomorphism via Open Maps
>
>A [bijection](../../../Analysis/Functions/Types%20of%20Functions/Bijection.md) $f: X \to Y$ between two [topological spaces](../../Topological%20Spaces/index.md) $(X, \tau_X)$ and $(Y, \tau_Y)$ is a [homeomorphism](Homeomorphism.md) if and only if it is an [open map](../../Maps/Open%20Map.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Homeomorphism via Closed Maps
>
>A [bijection](../../../Analysis/Functions/Types%20of%20Functions/Bijection.md) $f: X \to Y$ between two [topological spaces](../../Topological%20Spaces/index.md) $(X, \tau_X)$ and $(Y, \tau_Y)$ is a [homeomorphism](Homeomorphism.md) if and only if it is a [closed map](../../Maps/Closed%20Map.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Properties

>[!THEOREM]- Theorem: Composition of Homeomorphisms
>
>Let $(X, \tau_X)$, $(Y, \tau_Y)$ and $(Z, \tau_Z)$ be [topological spaces](../../Topological%20Spaces/index.md).
>
>If $f: X \to Y$ and $g: Y \to Z$ are [homeomorphisms](./index.md), then their [composition](../../../Analysis/Functions/Composition.md) $g \circ f: X \to Z$ is also a [homeomorphism](./index.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Homeomorphism $\implies$ Local Homeomorphism
>
>Every [homeomorphism](./index.md) is also a [local homeomorphism](Local%20Homeomorphisms.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>