---
title: 
tags:
  - topology
  - mathematics
---

# Exterior

>[!DEFINITION] Definition: Exterior of a Set
>
>Let $(X, \tau_X)$ be a [topological space](../Topological%20Spaces/index.md) and let $S$ be a [subset](../../../Set%20Theory/index.md) of $X$.
>
>The **exterior** of $S$ is the [complement](../../../Set%20Theory/Complement.md) of its [closure](Closure.md) in $X$.
>
>$$
>X \setminus \overline{S}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>\operatorname{ext} S \qquad \operatorname{Ext} S
>>$$
>>
>
>^exterior
>

>[!DEFINITION] Definition: Exterior Point
>
>Let $(X, \tau_X)$ be a [topological space](../Topological%20Spaces/index.md) and let $S$ be a [subset](../../../Set%20Theory/index.md) of $X$.
>
>A point $p \in X$ is an **exterior point** of $S$ iff it belongs to the [exterior](Exterior.md) of $S$.
>

## Properties


>[!THEOREM] Theorem: Exterior is Closed
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces/index.md).
>
>The [](Exterior.md#^exterior) $\operatorname{Ext} S$ of each [subset](../../../Set%20Theory/index.md) $S \subseteq X$ is [closed](../Topological%20Spaces/Closed%20Sets.md).
>
>>[!PROOF]-
>>
>>The [exterior](Exterior.md) of $S$ is the [complement](../../../Set%20Theory/Complement.md) of its [closure](Closure.md) and since the [closure](Closure.md) is a [closed set](../Topological%20Spaces/Closed%20Sets.md), the [exterior](Exterior.md) is [open](../Topological%20Spaces/Open%20Sets.md).
>>
>