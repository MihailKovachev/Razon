---
title: Closure
tags:
  - topology
  - mathematics
---

# Closure

>[!THEOREM] Theorem: Closure
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces.md) let $A$ be a [subset](../../Set%20Theory/Sets.md) of $X$.
>
>The [union](../../Set%20Theory/Set%20Operations.md) of the [interior](../Interior,%20Boundary%20and%20Exterior.md) $\operatorname{int} A$ of $A$ with the [boundary](../Interior,%20Boundary%20and%20Exterior.md) $\partial A$ of $A$ is [closed](../Topological%20Spaces.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Closure
>>
>>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces.md) and let $A$ be a [subset](../../Set%20Theory/Sets.md) of $X$.
>>
>>The **closure** of $A$ is the [union](../../Set%20Theory/Set%20Operations.md) of its [interior](../Interior,%20Boundary%20and%20Exterior.md) and its [boundary](../Interior,%20Boundary%20and%20Exterior.md).
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
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces.md).
>
>Every [subset](../../Set%20Theory/Sets.md) $S$ is a [subset](../../Set%20Theory/Sets.md) of its own [closure](Closure.md).
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
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces.md) and let $S$ be a [subset](../../Set%20Theory/Sets.md) of $X$.
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
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces.md) and let $A$ and $B$ be two arbitrary [subsets](../../Set%20Theory/Sets.md) of $X$.
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
>Let $(X, \tau_X)$ be a [topological space](../Topological%20Spaces.md).
>
>The [closure](Closure.md) of the [empty set](../../Set%20Theory/Sets.md) is itself.
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