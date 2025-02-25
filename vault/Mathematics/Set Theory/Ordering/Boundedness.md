---
title: Bounds
tags:
  - boundedness
  - orderings
  - set-theory
  - mathematics
---

# Lower Bounds

>[!DEFINITION] Definition: Lower Bound
>
>Let $T$ be a [subset](../Sets.md) of a [partially ordered](Partial%20Order.md) [set](../Sets.md) $S$.
>
>An element $l \in S$ is called a **lower bound** of $T$ iff
>
>$$
>l \le t \qquad \forall t\in T
>$$
>

## Infimum

>[!DEFINITION] Definition: Infimum
>
>Let $L$ be the [set](../Sets.md) of all [lower bounds](./index.md) of $T$.
>
>The **infimum** $\inf (T)$ of $T$ is its smallest [lower bound](./index.md).
>
>$$
>\inf (T) \le l \qquad \forall l \in L
>$$
>
>>[!THEOREM] Theorem: Uniqueness of the Infimum
>>
>>The [infimum](Boundedness.md#infimum) of $T$ is unique.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

# Upper Bounds

>[!DEFINITION] Definition: Upper Bound
>
>Let $T$ be a [subset](../Sets.md) of a [partially ordered](Partial%20Order.md) [set](../Sets.md) $S$.
>
>An element $u \in S$ is called an **upper bound** of $T$ iff
>
>$$
>t \le u \qquad \forall t \in T
>$$
>

## Supremum

>[!DEFINITION] Definition: Supremum
>
>Let $U$ be the [set](../Sets.md) of all [upper bounds](./index.md) of $T$.
>
>The **supremum** $\sup (T)$ of $T$ is its largest [upper bound](./index.md).
>
>$$
>u \le \sup (T) \qquad \forall u \in U
>$$
>
>>[!THEOREM] Theorem: Uniqueness of the Supremum
>>
>>The [supremum](Boundedness.md#supremum) of $T$ is unique.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

# Boundedness

>[!DEFINITION] Definition: Bounded Sets
>
>A [partially ordered](Partial%20Order.md) [set](../Sets.md) is:
>- **bounded above** if it has an [upper bound](./index.md#upper%20bounds);
>- **bounded below** if it has a [lower bound](./index.md#lower%20bounds);
>- **bounded** if it has both an [upper bound](./index.md#upper%20bounds) and a [lower bound](./index.md#lower%20bounds).
>