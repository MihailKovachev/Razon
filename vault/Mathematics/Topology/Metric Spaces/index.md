---
title: Metric Spaces
tags:
  - metric-spaces
  - topology
  - mathematics
---

# Metric

>[!DEFINITION] Definition: Metric
>
>Let $M$ be a [set](../../Set%20Theory/Sets.md).
>
>A **metric** on $M$ is a [real-valued function](../../Analysis/Real%20Analysis/Real-Valued%20Function.md) which has the following properties for all $x, y, z \in M$:
>
>- Identity of indiscernibles: $d(x, y) \ge 0$ with $d(x, y) = 0 \iff x = y$
>- Symmetry: $d(x,y) = d(y,x)$
>- Triangle inequality: $d(x,z) \le d(x,y) + d(y,z)$
>
>>[!INTUITION]-
>>
>>A metric on a set can be thought of as a way to define distance between the members of the set.
>> 
>

>[!DEFINITION] Definition: Open Ball
>
>Let $(M, d)$ be a [metric space](./index.md).
>
>The **open ball** of radius $r$ around a given $x \in M$ is the [set](../../Set%20Theory/Sets.md) of all elements in $M$ which are a [distance](./index.md) less than $r$ from $m$.
>
>$$
>\{x \in M \mid d(x, m)  \lt r\}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>B_r(x) \qquad B(x, r)
>>$$
>>
>

# Metric Spaces

>[!DEFINITION] Definition: Metric Space
>
>A **metric space** $(M, d)$ is a [set](../../Set%20Theory/Sets.md) $M$ equipped with a [metric](./index.md) on it.
>

## The Metric Topology

>[!THEOREM] Theorem: The Metric Topology
>
>Let $(M,d)$ be a [metric space](./index.md).
>
>The [collection](../../Set%20Theory/Collections/index.md) of all [open balls](./index.md) in $M$ forms a [base](../Bases/index.md) $(M, \tau_d)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Metric Topology
>>
>>The [topology](../Topological%20Spaces/index.md) $\tau_d$ is known as the **metric topology** induced on $M$ by $d$.
>>
>

>[!TIP] Corollary: Open Sets in the Metric Topology
>
>Let $(S,d)$ be a [metric space](./index.md) and let $\tau$ be the [topology](./index.md) induced on it by $d$.
>
>A [subset](../../Set%20Theory/Sets.md) $U$ of $S$ is [open](../Topological%20Spaces/Open%20Sets.md) if and only if for each $u \in U$ there exists an [open ball](./index.md) $B_\varepsilon (u)$ which is contained entirely in $U$.
>
>>[!PROOF]-
>>
>>This follows directly from [topology generation](../Bases/index.md).
>>
>

## Properties

>[!THEOREM] Theorem: Metric Spaces are Hausdorff Spaces
>
>Every [metric space](./index.md) is a [Hausdorff Spaces](../Hausdorff%20Spaces.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: First-Countability of Metric Spaces
>
>Every [metric space](./index.md) is [first countable](../Bases/First-Countability%20Axiom.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Convergence of Sequences in Metric Spaces
>
>Let $(M, d)$ be a [metric space](./index.md) with its [metric topology](./index.md).
>
>A [sequence](../../Analysis/Functions/Sequences/Sequences.md) $(x_n)_{n\in I}$ [converges](../../Analysis/Functions/Sequences/Convergence%20of%20Sequences.md) to some $l \in M$ if and only if for each [open ball](./index.md) $B_\varepsilon(l)$ around $l$, there exists some $N \in I$ such that $x_n \in B_\varepsilon(l)$ for all $n \ge N$.
>
>>[!PROOF]-
>>
>>TODO
>>
>