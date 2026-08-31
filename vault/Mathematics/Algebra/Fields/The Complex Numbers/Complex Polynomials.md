---
title: Complex Polynomials
tags:
    - algebra
    - mathematics
---

# Complex Polynomials

>[!DEFINITION] Definition: Complex Polynomial
>
>A **complex polynomial** is a [polynomial](../../Rings/Commutative%20Rings/Polynomials/Polynomials.md) over the [complex numbers](The%20Complex%20Numbers/Complex%20Numbers.md).
>

# Polynomial Division

>[!THEOREM] Theorem: Polynomial Division
>
>Let $A(z)$ and $B(z)$ be two [complex polynomials](Complex%20Polynomials.md) such that $\deg A \ge \deg B$.
>
>If $B(z)$ is non-zero, then there exist unique polynomials $Q(z)$ and $R(z)$ such that
>
>$$
>A(z) = Q(z)B(z) + R(z),
>$$
>
>where 
>- $\deg(Q) = \deg(A) - \deg(B)$
>- $\deg(R) \lt \deg(B)$ or $R(z)$ is zero.
>
>We call $A$ the **dividend**, $B$ the **divisor**, $Q$ the **quotient** and $R$ the **remainder**.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Divisibility
>>
>>If $R(z) = 0$, then we say that $A$ is **divisible** by $B$.
>>
>

>[!THEOREM] The Fundamental Theorem of Algebra
>
>Every non-constant [complex polynomial](Complex%20Polynomials.md) $A(z) = \sum_{k = 0}^n a_k z^k$ can be factorized into a product of [complex polynomials](Complex%20Polynomials.md) with $\deg = 1$. More specifically,
>
>$$
>A(z) = a_n (z - z_1)^{m_1} \cdots (z - z_l)^{m_l},
>$$
>
>where $z_i$ are the distinct [roots](../../Equations/Polynomial%20Equations/Complex%20Polynomial%20Equations.md) of $A(z) = 0$ and $m_i$ are their respective [multiplicities](../../Equations/Polynomial%20Equations/Complex%20Polynomial%20Equations.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>