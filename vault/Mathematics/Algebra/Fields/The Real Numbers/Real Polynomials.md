---
title: The Binomial Theorem
tags:
  - real-polynomials
  - polynomials
  - real-numbers
  - abstract-algebra
  - algebra
  - mathematics
---


>[!DEFINITION] Definition: Real Polynomial
>
>A **real polynomial** is a [polynomial](../../Rings/Commutative%20Rings/Polynomials/Polynomials.md) over the [field of the real numbers](The%20Real%20Numbers.md).
>

## Properties

>[!THEOREM]- The Binomial Theorem
>
>The expansion of the expression
>
>$$
>(x + y)^n,
>$$
>
>where $n \in \mathbb{N}$ is given by the [polynomial](Real%20Polynomials.md)
>
>$$
>(x + y)^n = C_n^0 x^n y^0 + C_n^1 x^{n-1}y^1 + C_n^2 x^{n - 2}y^{2} + \cdots + C_n^n x^0 y^n,
>$$
>
>where $C$ is the notation for the [total number of combinations without repetition](../../../Combinatorics/Combinations.md#Combinations%20without%20Repetition).
>
>>[!TIP]
>>
>>The expansion has $n+1$ terms. The $k$-th term ($k \in \{1, \dotsc, n + 1\}$) is $C_n^{k-1} x^{n-(k-1)} y^{k-1}$.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>