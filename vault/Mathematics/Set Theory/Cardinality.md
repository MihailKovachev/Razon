---
title: Cardinality
tags:
  - set-theory
  - mathematics
---

# Cardinality

Comparing the sizes of [sets](./Sets.md) is easy when they are finite but gets tricky when dealing with [sets](./Sets.md) with infinitely many elements because, as it turns out, some infinite [sets](./Sets.md) are actually "bigger" than others.

>[!DEFINITION] Definition: Cardinality
>
>The **cardinality** of a [set](./Sets.md) $S$ is the mathematical notion of the number of elements in $S$.
>
>>[!NOTE]
>>
>>There is no precise definition of "cardinality". Rather, the word is always used in certain mathematical expressions with a fixed meaning and does not really have any other meaning on its own.
>>
>

>[!DEFINITION] Definition: Size Comparisons of Sets
>
>Let $A$ and $B$ be two [sets](./Sets.md).
>
>We say that:
>- the [cardinality](./Cardinality.md) of $A$ is **equal** to the [cardinality](./Cardinality.md) of $B$ if there is a [bijection](../Analysis/Functions/Injections,%20Surjections%20and%20Bijections.md#Bijections) between $A$ and $B$. We notate this fact as $|A| = |B|$
>
>>[!NOTATION]
>>
>>$$
>>|A| = |B|
>>$$
>> 
> 
>- the [cardinality](./Cardinality.md) of $A$ is **less than or equal** to the [cardinality](./Cardinality.md) of $B$ if there is an [injection](../Analysis/Functions/Injections,%20Surjections%20and%20Bijections.md#Injections) from $A$ to $B$;
>
>>[!NOTATION]
>>
>>$$
>>|A| \le |B|
>>$$
>> 
>
>- the [cardinality](./Cardinality.md) of $A$ is **less than** the [cardinality](./Cardinality.md) of $B$ if there is an [injection](../Analysis/Functions/Injections,%20Surjections%20and%20Bijections.md#Injections) from $A$ to $B$ but there is no [bijection](../Analysis/Functions/Injections,%20Surjections%20and%20Bijections.md#Bijections) between them.
>
>>[!NOTATION]
>>
>>$$
>>|A| \lt |B|
>>$$
>>
>

>[!DEFINITION] Definition: Finite Set
>
>A [set](./Sets.md) $S$ is **finite** if there exists some integer $n \in \mathbb{N}_0$ such that $S$ has the same [cardinality](./Cardinality.md) as the [set](./Sets.md) $\{1,2,\dotsc,n\}$.
>
>>[!NOTATION]
>>
>>$$
>>|S| = n
>>$$
>>
>

>[!THEOREM] Theorem: Cardinality of Finite Sets
>
>If $A$ and $B$ are [finite](./Cardinality.md) [sets](./Sets.md), then the [cardinalities](./Cardinality.md) of their [union](./Sets.md#Operations), [difference](./Sets.md#Operations) and [Cartesian product](./Sets.md#Operations) are:
>
>$$
>\begin{aligned}
>&|A \cup B| = |A| + |B| - |A \cap B| \\
>&|A \setminus B| = |A| - |A \cap B| \\
>&|A \times B| = |A| \times |B| \\
>\end{aligned}
>$$
>
>Moreover, the [cardinality](./Cardinality.md) of the [intersection](./Sets.md#Operations) $A \cap B$ is zero if and only if $A$ and $B$ are [disjoint](./Sets.md#Operations):
>
>$$
>|A \cap B| = 0 \iff A \cap B = \varnothing
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Infinite Sets

>[!DEFINITION] Definition: Infinite Set
>
>A [set](./Sets.md) is **infinite** if it is not [finite](./Cardinality.md).
>

>[!DEFINITION] Definition: Countably Infinite Set
>
>A [set](./Sets.md) $S$ is **countably infinite** if it has the same [cardinality](./Cardinality.md) as the [set](./Sets.md) of [natural numbers](TODO) $\mathbb{N}$.
>
>>[!NOTATION]
>>
>>$$
>>|S| = \aleph_0
>>$$
>>
>>The symbol $\aleph_0$ is read as "aleph null".
>>
>

>[!DEFINITION] Definition: Uncountable Set
>
>A [set](./Sets.md) $S$ is **uncountable** if it is [infinite](#Infinite%20Sets) but not [countable](#Infinite%20Sets).
>