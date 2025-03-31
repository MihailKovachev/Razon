---
title: Univariate Polynomials
tags:
  - univariate-polynomials
  - polynomials
  - ring-theory
  - abstract-algebra
  - algebra
  - mathematics
---

# Univariate Polynomials

>[!DEFINITION] Definition: Univariate Polynomial
>
>A **univariate polynomial** is a [polynomial](../Polynomials.md) in a single variable.
>
>>[!NOTE]
>>
>>A univariate polynomial has the form
>>
>>$$
>>a_n x^n + \cdots a_{n-1}x^{n-1} + \cdots + a_1 x + a_0
>>$$
>>
>

# Properties

>[!THEOREM] Theorem: Ring of Univariate Polynomials
>
>Let $R$ be a [commutative ring](../../index.md).
>
>The [set](../../../../../Set%20Theory/Sets.md) of all [univariate polynomials](./index.md) over $R$ form a commutative ring together with [polynomial addition](../Polynomials.md) and [polynomial multiplication](../Polynomials.md).
>
>>[!NOTATION]
>>
>>This ring is often denoted as $R[x]$ or $R[X]$.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Equality

>[!THEOREM] Theorem: Equality of Univariate Polynomials
>
>Let $A(x)$ and $B(x)$ be two [nonzero](../Zero%20Polynomial.md) [polynomials](./index.md) over an [integral domain](../../Integral%20Domains/Integral%20Domain.md) with [degrees](../Polynomials.md) $\deg(A)$ and $\deg(B)$.
>
>If $A(x)$ and $B(x)$ have the same [value](../Polynomials.md) for $\max\{\deg(A), \deg(B)\}+1$ different values for $x$, then $A$ and $B$ are [equal](../Polynomials.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Roots

>[!THEOREM] Theorem: Roots of Univariate Polynomials
>
>Let $A(x)$ be a [univariate polynomial](./index.md) over a [commutative ring](../../index.md) $R$.
>
>An element $p \in R$ is a [root](../Polynomials.md) of $A$ if and only if $A$ is [divisible](Polynomial%20Division.md) by $x - p$.
>
>>[!PROOF]-
>>
>>**In the forward direction:** Suppose that $p$ is a root of $A$, i.e. $A(p) = 0$. The [polynomial remainder theorem](Polynomial%20Division.md) then tells us that the remainder of the division of $A$ by $x-p$ is zero, i.e. $A$ is divisible by $x - p$.
>>
>>**In the backward direction:** Suppose that $A$ is divisible by $x-p$. This means that $A(x) = (x-p)Q(x)$ for some polynomial $Q$. Plugging in $p$ gives us $A(p) = (p - p)Q(p) = 0\cdot Q(p) = 0$ and so $p$ is a root of $A$.
>>
>

>[!THEOREM] Theorem: Number of Roots of Univariate Polynomials
>
>If $P(x)$ is a [polynomial](./index.md) $P(x)$ over an [integral domain](../../Integral%20Domains/Integral%20Domain.md), then the maximum number of distinct [roots](../Polynomials.md) which $P$ can have is equal its [degree](../Polynomials.md) $\deg(P)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>