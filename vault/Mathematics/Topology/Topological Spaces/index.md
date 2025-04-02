---
title: Topological Spaces
tags:
  - topology
  - mathematics
---

# Topological Spaces

>[!DEFINITION] Definition: Topology
>
>A **topology** on a [non-empty](../../Set%20Theory/Sets.md) [set](../../Set%20Theory/Sets.md) $X$ is a [collection](../../Set%20Theory/Collections/Collections.md) $\tau$ of [subsets](../../Set%20Theory/Sets.md) of $X$ which has the following properties:
>
>- The [empty set](../../Set%20Theory/Sets.md) $\varnothing$ and $X$ are in $\tau$.
>- The [union](../../Set%20Theory/Collections/Operations%20with%20Collections.md) of any subset of $\tau$ is in $\tau$.
>- The [intersection](../../Set%20Theory/Set%20Operations.md) of any two elements of $\tau$ is in $\tau$.
>
>>[!INTUITION]-
>>
>>A topology $\tau$ on a [set](../../Set%20Theory/Sets.md) $X$ can be interpreted as a definition of "closeness" between elements of $X$ without using any notion of distance. Moreover, a topology provides a way for us to define what is "inside" a set, what is "outside" a set and what separates the inside of a set from its outside.
>> 
>
>>[!EXAMPLE]-
>>
>>Consider the sets $X = \{1,2,3,4,5,6\}$ and $\tau = \{\varnothing, X, \{1\}, \{3,4\}, \{1,3,4\}, \{2,3,4,5,6\}\}$. The set $\tau$ is a topology on $X$, since it satisfies the requirements in the definition.
>>
>

>[!DEFINITION] Definition: Topological Space
>
>A **topological space** $(S,\tau)$ is a [non-empty](../../Set%20Theory/Sets.md) [set](../../Set%20Theory/Sets.md) $S$ equipped with a [topology](./index.md) $\tau$ on it.
>
>>[!NOTE] Note: Points
>>
>>It is common to refer to the elements $s \in S$ of a topological space as **points**.
>>
>

