---
title: Multiplexers
tags:
    - digital-circuits
    - electrical-engineering
---

# Multiplexers

Given some signals, we often want to select a particular one of them based on some condition. Electronic components which realize this are known as **multiplexers**.

>[!DEFINITION] Definition: Multiplexer
>
>An $n:1$ **multiplexer** (**MUX**) is an electronic component which can select one input bit from $n$ input bits and forward it to its output bit based on some condition.
>
>>[!TIP] Tip: Bus Multiplexers
>>
>>There are also $m$-bit $n:1$ [multiplexers](./Multiplexers.md) which take $n$ input [buses](TODO) with a width of $m$ and select one of them to be forwarded to the output [bus](TODO), also of width $m$.
>>
>

An $n:1$ [multiplexer](./Multiplexers.md) has one output, $n$ inputs and at least $\lceil \log_2 n \rceil$ additional inputs, known as **selector pins** or **selector lines**. The combination of the signals on the selector pins is used to uniquely determine which of the $n$ inputs to forward as the output of the [multiplexer](./Multiplexers.md). It is crucial that the number of selector pins is at least $\lceil \log_2 n \rceil$ because, otherwise, the total number of combinations would be less than $n$ and it will be impossible to uniquely assign a combination to each input.

>[!NOTATION]
>
>The following symbol is used for 1-bit [multiplexers](./Multiplexers.md):
>
>![Multiplexer Symbol](./res/Multiplexers/Multiplexer%20Symbol.svg)
>

## Implementation

[Multiplexers](./Multiplexers.md) are typically implemented in one of the following ways:
- By using [AND gates](./Logic%20Gates/Logic%20Gates.md), [NOT gates](./Logic%20Gates/Logic%20Gates.md) and [OR gates](./Logic%20Gates/Logic%20Gates.md).
- By recursively using simpler [multiplexers](./Multiplexers.md).
 
>[!ALGORITHM] Algorithm: Multiplexers from Logic Gates
>
>We want to construct a $p:1$ [multiplexer](./Multiplexers.md), i.e. a [multiplexer](./Multiplexers.md) with $p$ inputs $i_0, \dotsc, i_{p-1}$ and $q = \lceil \log_2 p \rceil$ selector lines $s_0, \dotsc, s_{q-1}$, using $\mathop{\operatorname{AND}}$, $\mathop{\operatorname{NOT}}$ and $\mathop{\operatorname{OR}}$ [gates](./Logic%20Gates/Logic%20Gates.md).
>
>1. Construct the [minterms](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md) $m_0, \dotsc, m_{p - 1}$ as [conjunctions](../../Mathematics/Algebra/Boolean%20Algebra/Conjunction.md) of the selector line [literals](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md).
>2. For each $i_k$, where $k \in \{0, \dotsc, p-1\}$, construct the [conjunction](../../Mathematics/Algebra/Boolean%20Algebra/Conjunction.md) $P_k = i_k \land m_k$ of $i_k$ and $m_k$.
>3. The output of the [multiplexer](./Multiplexers.md) is the [disjunction](../../Mathematics/Algebra/Boolean%20Algebra/Disjunction.md) of $P_0, \dotsc, P_{p - 1}$, i.e. realize this [disjunctive normal form](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Expressions.md) via [logic gates](./Logic%20Gates/Logic%20Gates.md):
>
>$$
>P_0 \lor \cdots \lor P_{p-1}
>$$
>
>>[!EXAMPLE]- Example: $2:1$ Multiplexer
>>
>>We have two inputs $i_0$ and $i_1$ and one selector line $s_0$.
>>
>>We choose the bit string $({}_0 s_0^{\ast}) = (0)$ for $i_0$ and we choose the bit string $({}_1 s_0^{\ast}) = (1)$ for $i_1$. Now we construct the [minterms](../../Mathematics/Algebra/Boolean%20Algebra/Conjunction.md) $S_0$ and $S_1$:
>>
>>$$
>>\begin{aligned}
>>S_0 &= \neg s_0 \land i_0 \text{ because } {}_0 s_0^{\ast} = 0 \\
>>S_1 &= s_0 \land i_1 \text{ because } {}_1 s_1^{\ast} = 1
>>\end{aligned}
>>$$
>>
>>The [operator](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Functions.md) which expresses the behavior of the multiplexer is then the following:
>>
>>$$
>>(\neg s_0 \land i_0) \lor (s_0 \land i_1)
>>$$
>>
>>This formula is realized in the following way via [logic gates](./Logic%20Gates/Logic%20Gates.md):
>>
>>![2 to 1 Multiplexer](./res/Multiplexers/2%20to%201%20Multiplexer.svg)
>>
>>If $s_0 = 0$, we get $i_0$ and if $s_0 = 1$, we get $i_1$.
>>
>
>>[!EXAMPLE]- Example: $4:1$ Multiplexer
>>
>>We have four inputs $i_0$, $i_1$, $i_2$ and $i_3$ and two selector lines $s_0$ and $s_1$. We arbitrarily assign the following bit strings to $i_0$, $i_1$, $i_2$ and $i_3$:
>>
>>|$s_{0}^{\ast}$|$s_{1}^{\ast}$|Input|
>>|:--:|:--:|:--:|
>>|$0$|$0$|$i_0$|
>>|$0$|$1$|$i_1$|
>>|$1$|$0$|$i_2$|
>>|$1$|$1$|$i_3$|
>>
>>
>>We therefore have the strings:
>>- $({}_{0} s_{0}^{\ast}, {}_{0} s_{1}^{\ast}) = 00$;
>>- $({}_{1} s_{0}^{\ast}, {}_{1} s_{1}^{\ast}) = 01$;
>>- $({}_{2} s_{0}^{\ast}, {}_{2} s_{1}^{\ast}) = 10$;
>>- $({}_{3} s_{0}^{\ast}, {}_{3} s_{1}^{\ast}) = 11$
>>
>>From each row, we construct the following [minterms](../../Mathematics/Algebra/Boolean%20Algebra/Conjunction.md), respectively:
>>- $S_0 = \mathop{\operatorname{AND}}(\neg s_0, \neg s_1, i_0)$;
>>- $S_1 = \mathop{\operatorname{AND}}(\neg s_0, s_1, i_1)$;
>>- $S_2 = \mathop{\operatorname{AND}}(s_0, \neg s_1, i_2)$;
>>- $S_0 = \mathop{\operatorname{AND}}(s_0, s_1, i_3)$.
>> 
>>We form the [disjunction](../../Mathematics/Algebra/Boolean%20Algebra/Disjunction.md) of these [minterms](../../Mathematics/Algebra/Boolean%20Algebra/Conjunction.md) to obtain a formula for the [operator](../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Functions.md) which expresses the multiplexers behavior:
>>
>>$$
>>\begin{aligned}
>>S_0 \lor S_1 \lor S_2 \lor S_3 = \mathop{\operatorname{AND}}(\neg s_0, \neg s_1, i_0) \lor \mathop{\operatorname{AND}}(\neg s_0, s_1, i_1) \lor \mathop{\operatorname{AND}}(s_0, \neg s_1, i_2) \lor \mathop{\operatorname{AND}}(s_0, s_1, i_3)
>>\end{aligned}
>>$$
>>
>>This formula is realized in the following way via [logic gates](./Logic%20Gates/Logic%20Gates.md):
>>
>>![4 to 1 Multiplexer](./res/Multiplexers/4%20to%201%20Multiplexer.svg)
>>
>

>[!ALGORITHM] Algorithm: MUX Tree
>
>TODO recursive algorithm via Boolean expression and factoring out control bits.
>
>We want to construct a $p:1$ [multiplexer](./Multiplexers.md), i.e. a [multiplexer](./Multiplexers.md) with $p$ inputs $i_0, \dotsc, i_{p-1}$ and $q = \lceil \log_2 p \rceil$ selector lines $s_0, \dotsc, s_{q-1}$, using smaller $2:1$ [multiplexers](./Multiplexers.md).
>
>We construct a tree with $q$ levels:
>
>1. For the $k$-th layer, where $k \in 0, \dotsc, q-1$:
>    - The input signals are the outputs of layer $k-1$.
>    - Group the input signals into pairs.
>    - Pass the signals of each pair into the inputs of a $2:1$ [multiplexer](./Multiplexers.md).
>    - Connect the selector line of each [multiplexer](./Multiplexers.md) to $s_k$.
>    - The outputs of these [multiplexers](./Multiplexers.md) become the inputs for layer $k+1$.
>
>2. The inputs of layer $0$ are $i_0, \dotsc, i_{p-1}$.
>3. The output of layer $q - 1$ is the output of the entire $p:1$ [multiplexer](./Multiplexers.md).
>
>>[!EXAMPLE]- Example: $4:1$ MUX via $2:1$ MUX
>>
>>![MUX Tree Example](./res/Multiplexers/MUX%20Tree%20Example.svg)
>>
>

>[!ALGORITHM] Algorithm: Bus Multiplexers
>
>We want to construct an $m$-bit $n:1$ [multiplexer](./Multiplexers.md) which takes $n$ input [buses](TODO) with a width of $m$ and selects one of them to be forwarded to the output [bus](TODO), also of width $m$. 
>
>Let $N = \lceil \log_2 n \rceil$ be the number of selector lines and label the selector lines as $s_0, \dotsc, s_{N-1}$. We label the input [buses](TODO) $I_0, \dotsc, I_{n-1}$ and the bits of the bus $I_k$ we denote as $I_k[0], \dotsc, I_{k}[m-1]$. The bits of the output bus we denote as $O[0], \dotsc, O[m-1]$.
>
>1. Take $m$ identical $n:1$ [multiplexers](./Multiplexers.md) and connect their selector lines to the selector lines $s_0, \dotsc, s_{N-1}$.
>2. For each [multiplexer](./Multiplexers.md) $\mathrm{MUX}_i$ and each input bus $I_j$, connect $I_j[i]$ to the $j$-th input $\mathrm{MUX}_i[j]$ of $\mathrm{MUX}_i$.
>3. The value of each output bit $O[i]$ is the output of the $i$-th [multiplexer](./Multiplexers.md) $\mathrm{MUX}_i$.
>
>$$
>\mathrm{MUX}_i \to O[i]
>$$
>
>>[!EXAMPLE]- Example: $4$-bit $2:1$ Multiplexer
>>
>>We have only one selector bit $s[0]$.
>>
>>We have input buses $I_0$ and $I_1$:
>>- The bits of $I_0$ are $I_0[0]$, $I_0[1]$, $I_0[2]$ and $I_0[3]$.
>>- The bits of $I_1$ are $I_1[0]$, $I_1[1]$, $I_1[2]$ and $I_1[3]$.
>>
>>We need four $2:1$ [multiplexers](./Multiplexers.md) $\mathrm{MUX}_0$, $\mathrm{MUX}_1$, $\mathrm{MUX}_2$ and $\mathrm{MUX}_3$. We connect them according to step 2.
>>
>>The connections on $\mathrm{MUX}_0$ are:
>>- $I_0[0] \to \mathrm{MUX}_0[0]$.
>>- $I_1[0] \to \mathrm{MUX}_0[1]$.
>>
>>The connections on $\mathrm{MUX}_1$ are:
>>- $I_0[1] \to \mathrm{MUX}_1[0]$.
>>- $I_1[1] \to \mathrm{MUX}_1[1]$.
>>
>>The connections on $\mathrm{MUX}_2$ are:
>>- $I_0[2] \to \mathrm{MUX}_2[0]$.
>>- $I_1[2] \to \mathrm{MUX}_2[1]$.
>>
>>The connections on $\mathrm{MUX}_2$ are:
>>- $I_0[3] \to \mathrm{MUX}_3[0]$.
>>- $I_1[3] \to \mathrm{MUX}_3[1]$.
>>  
>>Finally, we connect the outputs:
>>- $\mathrm{MUX}_0 \to O[0]$
>>- $\mathrm{MUX}_1 \to O[1]$
>>- $\mathrm{MUX}_2 \to O[2]$
>>- $\mathrm{MUX}_3 \to O[3]$
>>
>>The diagram for this is the following:
>>
>>![Four-Bit 2 to 1 Multiplexer](./res/Multiplexers/Four-Bit%202%20to%201%20Multiplexer.svg)
>>
>