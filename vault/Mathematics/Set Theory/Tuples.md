---
title: Tuples
tags:
  - set-theory
  - mathematics
---

# Tuples

>[!DEFINITION] Definition: Tuple
>
>The $0$**-tuple** is the [empty set](./Sets.md) $\varnothing$:
>
>$$() \overset{\text{def}}{=} \varnothing$$
>
>A $1$**-tuple** $(x)$ is just $x$ itself:
>
>$$(x) \overset{\text{def}}{=} x$$
>
>An $n$**-tuple** is defined recursively via [sets](./Sets.md) in the following way:
>
>$$(x_1,\dotsc,x_n) \overset{\text{def}}{=} \begin{cases}\{\{x_1\},\{x_1,x_2\}\} & \text{if } n = 2 \\ \\ ((x_1, \dotsc, x_{n-1}), x_n) & \text{if } n \gt 2\end{cases}$$
>

>[!DEFINITION] Definition: Ordered Pair
>
>The **ordered pair** $(a;b)$ of two objects $a$ and $b$ is the [collection](./Collections.md)
>
>$$
>(a;b) \overset{\text{def}}{=} \{\{a\},\{a,b\}\}
>$$
>

>[!THEOREM] Theorem: Equality of Ordered Pairs
>
>Two [ordered pairs](Ordered%20Pairs.md) $(a;b)$ and $(c;d)$ are [equal](./Sets.md#Sets) if and only if $a = b$ and $c = d$.
>
>$$
>(a;b) = (c;d) \iff (a = b \land c=d)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!NOTE]
>>
>>This property of ordered pairs means that, in general, $(a;b) \ne (b;a)$, hence the name "ordered".
>>
>

## Tuples

>[!DEFINITION] Definition: $n$-Tuple
>
>An $n$-**tuple** $(a_1,\cdots,a_n)$ is a [collection](./Collections.md) of $n$ [ordered pairs](#Ordered%20Pairs) $\{(1,a_1), \cdots, (n,a_n)\}$.
>

>[!THEOREM] Theorem: Equality of $n$-Tuples
>
>Two $n$-[tuples](./Tuples.md) $(a_1,\cdots,a_n)$ and $(b_1,\cdots,b_n)$ are [equal](./Sets.md#Sets) if and only if $a_1 = b_1, \cdots, a_n = b_n$:
>
>$$
>(a_1,\cdots,a_n) = (b_1,\cdots,b_n) \iff a_1 = b_1, \cdots, a_n = b_n
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
