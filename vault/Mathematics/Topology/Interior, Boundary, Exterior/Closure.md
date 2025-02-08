---
title: Closure
tags:
  - topology
  - mathematics
---

# Closure

>[!THEOREM] Theorem: Closure
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces/index.md) let $A$ be a [subset](../../Set%20Theory/index.md) of $X$.
>
>The [union](../../Set%20Theory/Set%20Operations.md) of the [interior](Interior.md) $\operatorname{int} A$ of $A$ with the [boundary](Boundary.md) $\partial A$ of $A$ is [closed](../Topological%20Spaces/Closed%20Sets.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Closure
>>
>>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces/index.md) and let $A$ be a [subset](../../Set%20Theory/index.md) of $X$.
>>
>>The **closure** of $A$ is the [union](../../Set%20Theory/Set%20Operations.md) of its [interior](Interior.md) and its [boundary](Boundary.md).
>>
>>$$
>>\operatorname{int} A \cup \partial A
>>$$
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>\overline{A}
>>>$$
>>>
>>
>

## Properties

>[!THEOREM]+ Theorem: Closure is a Superset
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces/index.md).
>
>Every [subset](../../Set%20Theory/index.md) $S$ is a [subset](../../Set%20Theory/index.md) of its own [closure](Closure.md).
>
>$$
>S \subseteq \overline{S}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>^closure-is-a-superset
>

>[!THEOREM]+ Theorem: Closure of a Closure
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces/index.md) and let $S$ be a [subset](../../Set%20Theory/index.md) of $X$.
>
>The [closure](Closure.md) of the [closure](Closure.md) of $S$ is still the [closure](Closure.md) of $S$.
>
>$$
>\overline{\overline{S}} = \overline{S}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]+ Theorem: Closure of a Union
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces/index.md) and let $A$ and $B$ be two arbitrary [subsets](../../Set%20Theory/index.md) of $X$.
>
>The [closure](Closure.md) of the [union](../../Set%20Theory/Set%20Operations.md) of $A$ and $B$ is the [union](../../Set%20Theory/Set%20Operations.md) of the [closures](Closure.md) of $A$ and $B$.
>
>$$
>\overline{A \cup B} = \overline{A} \cup \overline{B}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Closure of the Empty Set
>
>Let $(X, \tau_X)$ be a [topological space](../Topological%20Spaces/index.md).
>
>The [closure](Closure.md) of the [empty set](../../Set%20Theory/The%20Empty%20Set.md) is itself.
>
>$$
>\overline{\varnothing} = \varnothing
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>^closure-of-the-empty-set
>