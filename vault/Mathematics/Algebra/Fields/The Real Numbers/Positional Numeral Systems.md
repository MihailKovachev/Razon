---
title: Positional Numeral Systems
tags:
    - algebra
---

# Positional Numeral Systems

>[!DEFINITION] Definition: Positional Numeral System
>
>A **positional numeral system** or **place value system** consists of a [natural number](TODO) $b \gt 1$ and a [set]() of $b-1$ distinct symbols $D = \{d_0, d_1, \dotsc, d_{b-1}\}$.
>
>We call $b$ the **base** or **radix** and we call $d_0, d_1, \dotsc, d_{b-1}$ **digits**.
>

>[!THEOREM] Theorem: Representing Integers
>
>Let $b \gt 1$ be a [natural number](TODO).
>
>For every $N \in \mathbb{N}_0$, there exists a [finite sequence](../../../Analysis/Real%20Analysis/Real%20Sequences.md) of [extended natural numbers] $a_0, a_1, \dotsc, a_n$ such that $0 \le a_k \lt b$ and
>
>$$
>N = \sum_{k=0}^n a_k b^k
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

The above theorem tells us that we can use any [positional numeral system](./Positional%20Numeral%20Systems.md) to represent all non-negative integers by identifying the [digits](TODO) $D = \{d_0, d_1, \dotsc, d_{b-1}\}$ with the first $b$ numbers from $\mathbb{N}_0$. Then, each [finite string](TODO) $a_n a_{n-1} \cdots a_1 a_0$ represents a number $N \in \mathbb{N}_0$.

>[!NOTATION]
>
>When multiple [positional numeral systems](./Positional%20Numeral%20Systems.md) are used, it can be difficult to know in which system a particular number is given, especially when the systems use the same symbols for some digits. This is why we usually write the radix $b$ as a subscript at the end:
>
>$$
>(a_n a_{n-1} \cdots a_1 a_0)_b
>$$
>

>[!EXAMPLE]- Example: Base 2
>
>Consider the [positional numeral system](./Positional%20Numeral%20Systems.md) with radix $b = 2$ and digits $D = \{0, 1\}$.
>
>The string $11011_2$ represents the number
>
>$$
>11011_2 = 1\cdot 2^4 + 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdots 2^0 = 16 + 8 + 0 + 2 + 1 = 27
>$$
>

>[!EXAMPLE]- Example: Base 5
>
>Consider the [positional numeral system](./Positional%20Numeral%20Systems.md) with radix $b = 5$ and digits $D = \{0, 1, 2, 3, 4\}$.
>
>The string $3402_5$ represents the number
>
>$$
>\begin{aligned}
>3402 &= 3 \cdot 5^3 + 4 \cdot 5^2 + 0 \cdot 5^1 + 2 \cdot 5^0 \\ &= 375 + 100 + 0 + 2 = 477
>\end{aligned}
>$$
>

>[!EXAMPLE]- Example: Base 16
>
>Consider the [positional numeral system](./Positional%20Numeral%20Systems.md) with radix $b = 16$ and digits $D = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, \mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}, \mathrm{E}, \mathrm{F}\}$.
>
>The string $\mathrm{2AF70}_{16}$ represents the number
>
>$$
>\begin{aligned}
>\mathrm{2AF70}_{16} &= 2\cdot 16^4 + \mathrm{A} \cdot 16^3 + \mathrm{F} \cdot 16^2 + 7 \cdot 16^1 + 0 \cdots 16^0 \\ &= 2 \cdot 16^4 + 10 \cdot 16^3 + 15 \cdot 16^2 + 7 \cdot 16^1 + 0 \cdot 16^0 \\ &= 131072 + 40960 + 3840 + 112 + 0 \\ &= 175984
>\end{aligned}
>$$
>

>[!THEOREM] Theorem: Representing Real Numbers
>
>Let $b \gt 1$ be a [natural number](TODO).
>
>For every [real number](./The%20Real%20Numbers.md) $r \ge 0$ there exists a [finite sequence](../../../Analysis/Real%20Analysis/Real%20Sequences.md) of [extended natural numbers] $a_0, a_1, \dotsc, a_n$ and an [infinite series](../../../Analysis/Real%20Analysis/Real%20Series.md) of [extended natural numbers](TODO) $(c_k)_{k \in \mathbb{N}}$ such that $0 \le a_k \lt b$ and $0 \le c_k \lt b$ and
>
>$$
>r = \sum_{k=0}^n a_k b^k + \sum_{k=1}^{\infty} c_k b^{-k}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

According to this theorem, we can use  any [positional numeral system](./Positional%20Numeral%20Systems.md)  to represent all real numbers by again identifying the digits $D = \{d_0,\dotsc,d_{n-1}\}$ with the first $b$ numbers from $\mathbb{N}_0$.

>[!NOTATION]
>
>Each each [string](TODO) of the form $a_n a_{n-1} \cdots a_1 a_0.c_1 c_2 \cdots$ represents a [real number](./The%20Real%20Numbers.md) $r \ge 0$:
>
>$$
>r = \sum_{k=0}^n a_k b^k + \sum_{k=1}^{\infty} c_k b^{-k}
>$$
>
>If there is some index $p$ such that $c_k = 0$ for all $k \gt p$, then we can also omit the trailing zeros and just write $a_n a_{n-1} \cdots a_1 a_0.c_1 c_2 \cdots c_p$.
>
>When multiple [positional numeral systems](./Positional%20Numeral%20Systems.md) are used, it can be difficult to know in which system a particular number is given, especially when the systems use the same symbols for some digits. This is why we usually write the radix $b$ as a subscript at the end:
>
>$$
>(a_n a_{n-1} \cdots a_1 a_0 . c_1 c_2 \cdots)_b
>$$
>