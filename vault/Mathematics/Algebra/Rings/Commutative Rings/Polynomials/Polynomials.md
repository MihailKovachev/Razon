---
title: Polynomials
tags:
  - polynomials
  - ring-theory
  - abstract-algebra
  - algebra
  - mathematics
---

# Polynomials

>[!DEFINITION] Definition: Polynomial
>
>A **polynomial** over a [commutative ring](../index.md) $R$ in the [variables](TODO) $x_1, \cdots, x_n$ is an [expression](../../../../Formal%20Logic/Formal%20Languages.md) which can be written as a finite sum of [monomials](Monomials.md) in $x_1, \cdots, x_n$.
>
>>[!NOTATION]-
>>
>>We usually use capital Latin letters such as $P$ and $Q$ to denote polynomials. If we want to be explicit about the variables, we write $P(x_1, \cdots, x_n)$.
>>
>
>>[!DEFINITION] Definition: Leading Coefficient
>>
>>The **leading coefficient** of a [polynomial](Polynomials.md) is the [coefficient](Monomials.md) of its highest-[degree](Monomials.md) [monomial](Monomials.md).
>>
>

## Degree

>[!DEFINITION] Definition: Degree of a Polynomial
>
>The **degree** of a [nonzero](Zero%20Polynomial.md) [polynomial](Polynomials.md) $P$ is the highest [degree](Monomials.md) amongst its [monomials](Monomials.md).
>
>>[!NOTATION]
>>
>>$$
>>\deg(P)
>>$$
>>
>
>>[!EXAMPLE]-
>>
>>$$
>>\deg(3x^3 y + 4z^5 x^3 y^2) = 5
>>$$
>>
>

## Evaluation

>[!DEFINITION] Definition: Evaluation of a Polynomial
>
>Let $P(x_1, \cdots, x_n)$ be a [polynomial](Polynomials.md) over a [commutative ring](../index.md) $R$.
>
>The **value** or **evaluation** of $P$ at an $n$-[Tuples](../../../../Set%20Theory/Tuples.md) $(r_1, \cdots, r_n)$, where $r_1, \cdots, r_n \in R$, is obtained by replacing $x_i$ with $r_i$ and carrying out all ring operations.
>
>>[!NOTATION]
>>
>>$$
>>P(r_1, \cdots, r_n)
>>$$
>>
>

### Roots

>[!DEFINITION] Definition: Root of a Polynomial
>
>The **roots** of a [polynomial](Polynomials.md) $P$ are the [solutions](../../../Equations/Polynomial%20Equations/index.md) to the [polynomial equation](../../../Equations/Polynomial%20Equations/index.md) $P = 0$.
>

## Equality

>[!DEFINITION]
>
>Two [polynomials](Polynomials.md) are **equal** if they are built from the [same](Monomials.md) [monomials](Monomials.md).
>
>>[!NOTE]
>>
>>The order of the monomials is irrelevant.
>
>>[!EXAMPLE]-
>>
>>$$
>>4x^2 y z^4 - 3x^3 y + 7z^2 = 7z^2 + 4x^2 y z^4 - 3x^3 y
>>$$
>>
>

# Operations

>[!DEFINITION] Definition: Polynomial Addition
>
>TODO
>

>[!DEFINITION] Definition: Polynomial Multiplication
>
>TODO
>

