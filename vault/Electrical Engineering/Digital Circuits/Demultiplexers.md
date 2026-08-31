---
title: Demultiplexers
tags:
    - digital-circuits
    - electrical-engineering
---

# Demultiplexers

>[!DEFINITION] Definition: Multiplexer
>
>A $1:n$ **demultiplexer** (**DEMUX**) is an electronic component which has one input and $n$ outputs and can select to which output to forward the input based on some condition.
>

A $1:n$ [demultiplexer](./Demultiplexers.md) has one input, $n$ outputs and $\lceil \log_2 n \rceil$ additional inputs, known as **selector pins** or **selector lines**. The combination of the signals on the selector pins is used to uniquely determine to which of the $n$ outputs to forward the input of the [demultiplexer](./Multiplexers.md). It is crucial that the number of selector pins is at least $\lceil \log_2 n \rceil$ because, otherwise, the total number of combinations would be less than $n$ and it will be impossible to uniquely assign a combination to each output.

>[!NOTATION]
>
>The following symbol is used for [demultiplexers](./Demultiplexers.md):
>
>![Demultiplexer Symbol](./res/Demultiplexer/Demultiplexer%20Symbol.svg)
>

## Implementation

>[!ALGORITHM] Algorithm: Demultiplexer from Logic Gates
>
>We want to construct an $1:p$ [demultiplexer](./Demultiplexers.md), i.e. a [demultiplexer](./Demultiplexers.md) with input $i$, $p$ outputs $o_0, \dotsc, o_{p-1}$ and $q = \lceil \log_2 p \rceil$ selector lines $s_0, \dotsc, s_{q-1}$, using $\mathop{\operatorname{AND}}$, $\mathop{\operatorname{NOT}}$ and $\mathop{\operatorname{OR}}$ [gates](./Logic%20Gates/Logic%20Gates.md).
>
>1. Construct the [minterms](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md) $m_0, \dotsc, m_{p - 1}$ as [conjunctions](../../Mathematics/Algebra/Boolean%20Algebra/Conjunction.md) of the selector line [literals](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md).
>
>2. For each $m_k$, where $k \in \{0, \dotsc, p - 1\}$, construct the [conjunction](../../Mathematics/Algebra/Boolean%20Algebra/Conjunction.md) $P_k = i \land m_k$ of the input $i$ and the [minterm](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md) $m_k$.
>
>3. The $k$-th output $o_k$ is the [conjunction](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md) $P_k$, i.e. realize the following [conjunctions](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md) via [logic gates](./Logic%20Gates/Logic%20Gates.md):
>
>$$
>\begin{aligned}
>o_0 &= i \land m_0 \\
>&\vdots \\
>o_{p - 1} &= i \land m_{p-1}
>\end{aligned}
>$$
>
>>[!EXAMPLE]- Example: $1:2$ Demultiplexer
>>
>>We have two outputs $o_0$ and $o_1$ and one selector line $s_0$.
>>
>>We choose the bit string $({}_0 s_0^{\ast}) = (0)$ for $o_0$ and we choose the bit string $({}_1 s_0^{\ast}) = (1)$ for $o_1$. Now we construct the [minterms](../../Mathematics/Algebra/Boolean%20Algebra/Conjunction.md) $S_0$ and $S_1$:
>>
>>$$
>>\begin{aligned}
>>S_0 &= \neg s_0 \land i \text{ because } {}_0 s_0^{\ast} = 0 \\
>>S_1 &= s_0 \land i \text{ because } {}_1 s_1^{\ast} = 1
>>\end{aligned}
>>$$
>>
>>These formulae are realized in the following way via [logic gates](./Logic%20Gates/Logic%20Gates.md):
>>
>>![1 to 2 Demultiplexer](./res/Demultiplexer/1%20to%202%20Demultiplexer.svg)
>>
>>If $s_0 = 0$, we get $o_0$ and if $s_0 = 1$, we get $o_1$.
>>
>
>>[!EXAMPLE]- Example: $1:4$ Demultiplexer
>>
>>We have four outputs $o_0$, $o_1$, $o_2$ and $o_3$ and two selector lines $s_0$ and $s_1$. We arbitrarily assign the following bit strings to $o_0$, $o_1$, $o_2$ and $o_3$:
>>
>>|$s_{0}^{\ast}$|$s_{1}^{\ast}$|Output|
>>|:--:|:--:|:--:|
>>|$0$|$0$|$o_0$|
>>|$0$|$1$|$o_1$|
>>|$1$|$0$|$o_2$|
>>|$1$|$1$|$o_3$|
>>
>>
>>We therefore have the strings:
>>- $({}_{0} s_{0}^{\ast}, {}_{0} s_{1}^{\ast}) = 00$;
>>- $({}_{1} s_{0}^{\ast}, {}_{1} s_{1}^{\ast}) = 01$;
>>- $({}_{2} s_{0}^{\ast}, {}_{2} s_{1}^{\ast}) = 10$;
>>- $({}_{3} s_{0}^{\ast}, {}_{3} s_{1}^{\ast}) = 11$
>>
>>From each row, we construct the following [minterms](../../Mathematics/Algebra/Boolean%20Algebra/Conjunction.md), respectively:
>>- $S_0 = \mathop{\operatorname{AND}}(\neg s_0, \neg s_1, o_0)$;
>>- $S_1 = \mathop{\operatorname{AND}}(\neg s_0, s_1, o_1)$;
>>- $S_2 = \mathop{\operatorname{AND}}(s_0, \neg s_1, o_2)$;
>>- $S_0 = \mathop{\operatorname{AND}}(s_0, s_1, o_3)$.
>>
>>This formulae are realized in the following way via [logic gates](./Logic%20Gates/Logic%20Gates.md):
>>
>>![1 to 4 Demultiplexer](./res/Demultiplexer/1%20to%204%20Demultiplexer.svg)
>>
>