---
title: Real Polynomials
tags:
  - real-polynomials
  - polynomials
  - real-numbers
  - abstract-algebra
  - algebra
  - mathematics
---

# Real Polynomials

>[!DEFINITION] Definition: Real Polynomial
>
>A **real polynomial** is a [polynomials](../../Rings/Commutative%20Rings/Polynomials/Polynomials.md) over the [real numbers](./The%20Real%20Numbers.md).
>

## Binomial Theorem

>[!THEOREM] The Binomial Theorem
>
>The expansion of the expression
>
>$$
>(x + y)^n,
>$$
>
>where $n \in \mathbb{N}$ is given by the [real polynomials](./Real%20Polynomials.md)
>
>$$
>(x + y)^n = \sum_{k = 0}^n \binom{n}{k}x^{n-k}y^k = \sum_{k = 0}^n \binom{n}{k}x^{k}y^{n-k}
>$$
>
>>[!TIP]
>>
>>The expansion has $n+1$ terms. The $k$-th term ($k \in \{1, \dotsc, n + 1\}$) is given by the [number of combinations](../../../Combinatorics/Combinations.md) $C_n^{k-1} x^{n-(k-1)} y^{k-1}$.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Polynomial Division

>[!THEOREM] Theorem: Polynomial Division
>
>Let $A(x)$ and $B(x)$ be two [real polynomials](./Real%20Polynomials.md) such that the [degree](../../Rings/Commutative%20Rings/Polynomials/Polynomials.md) of $A$ is greater than or equal to the degree of $B$.
>
>If $B(x)$ is nonzero, then there exist unique polynomials $Q(x)$ and $R(x)$ such that
>
>$$
>A(x) = Q(x)B(x) + R(x),
>$$
>
>where 
>- $\deg(Q) = \deg(A) - \deg(B)$
>- $\deg(R) \lt \deg(B)$ or $R(x)$ is the zero polynomial.
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
>>If $R(x) = 0$, then we say that $A$ is **divisible** by $B$.
>>
>

>[!THEOREM] Theorem: Factorization Theorem
>
>Every [real polynomial](./Real%20Polynomials.md) $A(x) = \sum_{k=0}^n a_k x^k$ can be factorized into a product of [real polynomials](./Real%20Polynomials.md) of degree $\le 2$. More specifically,
>
>$$
>A(x) = a_n(x-r_1)^{p_1}\cdots(x-r_l)^{p_l} (x^2 + c_1 x + d_1)^{q_1}\cdots(x^2+c_s x + d_s)^{q_s},
>$$
>
>where:
>- $r_i$ are the distinct [real roots](../../Equations/Polynomial%20Equations/Real%20Polynomial%20Equations.md) of $A(x) = 0$;
>- $p_i$ is the [multiplicity](../../Equations/Polynomial%20Equations/Real%20Polynomial%20Equations.md) of $r_i$;
>- $c_j, d_j \in \mathbb{R}$;
>- $q_j \in \mathbb{N}_0$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Polynomial Remainder Theorem (Little Bézout's Theorem)
>
>The [remainder](#Polynomial%20Division) $R$ upon the [division](#Polynomial%20Division) of a [real polynomial](./Real%20Polynomials.md) $A(x)$ with a [real polynomial](./Real%20Polynomials.md) $B(x) = x - p$ is the [value](../../Polynomials/Univariate%20Polynomials.md#Evaluation) of $A$ at $p$.
>
>$$
>R = A(p)
>$$
>
>>[!PROOF]-
>>
>>The polynomial division theorem tells us that
>>
>>$$
>>A(x) = (x-p)Q(x) + R(x)
>>$$
>>
>>Since the [degree](../../Polynomials/Univariate%20Polynomials.md) of $B(x)$ is $1$, the degree of $R$ must either be $1$, i.e. $R$ is a constant and contains no variables or $R$ must be [zero](../../Polynomials/Zero%20Polynomial.md). We can therefore denote $R(x)$ as just $R$. For $x = p$ we obtain 
>>
>>$$
>>A(p) = (p-p)Q(p) + R = 0 + R = R
>>$$
>>
>

>[!ALGORITHM]- Algorithm: Horner's Method
>
>**Horner's method** is a way to easily [divide](#Polynomial%20Division) a [polynomial](./Real%20Polynomials.md) $A(x)$ by a [polynomial](./Real%20Polynomials.md) $B(x)$ of [degree](../../Polynomials/Univariate%20Polynomials.md#Degree) one.
> 
>1. Write $B(x)$ as $B(x) = x - p$. Since $\deg(B) = 1$, the [remainder](#Polynomial%20Division) $R$ is just a [real number](./The%20Real%20Numbers.md) because $\deg (R) \lt \deg(B) \implies \deg (R) = 0$. This means that we have
>
>$$
>A(x) = (x-p)Q(x) + R
>$$
>
>2. To determine $Q(x)$ and $R$, construct the following table:
> 
>||$a_n$|$a_{n-1}$|$\cdots$|$a_1$|$a_0$|
>|:--:|:--:|:--:|:--:|:--:|:--:|
>|$p$|$q_{n-1} = a_n$|$q_{n-2} = pq_{n-1} + a_{n-1}$|$\cdots$|$q_0 = pq_1 + a_1$|$R = pq_0 + a_0$|
>
>- We calculate the table from left to right.
>- The first coefficient $q_{n-1}$ of $Q(x)$ is equal to the first coefficient of $A(x)$, i.e. $q_{n-1} = a_n$.
> - For all other coefficients of $Q(x)$ we have $q_i = pq_{i+1} + a_{i-1}$.
> - At the end of the calculation, the right-most cell will contain $R$.
>
>>[!EXAMPLE]-
>>
>>Let $A(x) = 2x^5+3x^3-11x^2+6$ and $B(x) = x-3$. Create the table.
>>
>>||$2$|$0$|$3$|$-11$|$0$|$6$|
>>|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
>>|$p = 3$|||||||
>>
>>Perform the algorithm step by step.
>> 
>>||$2$|$0$|$3$|$-11$|$0$|$6$|
>>|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
>>|$p = 3$|2||||||
>> 
>>||$2$|$0$|$3$|$-11$|$0$|$6$|
>>|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
>>|$p = 3$|2|6|||||
>>
>>||$2$|$0$|$3$|$-11$|$0$|$6$|
>>|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
>>
>

>[!ALGORITHM]- Algorithm: Change of Variables
>
>We are given a [real polynomial](./Real%20Polynomials.md) $A(x)$ and want to transform it into another [real polynomial](./Real%20Polynomials.md) $B(y)$ where $y = x - p$ for some $p \in \mathbb{R}$.
>
>1. [Divide](#Polynomial%20Division) $A$ by $(x-p)$.
>
>$$
>A(x) = (x-p) Q_1(x) + R_0
>$$
>
>2. [Divide](#Polynomial%20Division) $Q_1$ by $(x-p)$.
>
>$$
>Q_1(x) = (x-p) Q_2(x) + R_1
>$$
>
>3. Repeat step 2, dividing $Q_i$ by $(x-p)$ in order to obtain $Q_{i + 1}$ and $R_1$ until $Q_{i+1}$ is just a number.
>4. Finally,
>
>$$
>B(y) = R_0 + R_1y + R_2y^2 + R_3y^3 + \cdots
>$$
>
>>[!TIP]
>>
>>You can use [Horner's method](#Polynomial%20Division) to speed up the process.
>>
>
>>[!EXAMPLE]-
>>
>>Let $A(x) = x^4 + 8x^3 + 24x^2 + 50x + 90$ and let $y = x + 2$. We can write $y$ as $y = x - p$, where $p = -2$.
>>
>>Apply [Horner's method](#Polynomial%20Division):
>>
>>||$1$|$8$|$24$|$50$|$90$|
>>|:--:|:--:|:--:|:--:|:--:|:--:|
>>|$-2$|$1$|$6$|$12$|$26$|$38 = R_0$|
>>|$-2$|$1$|$4$|$4$|$18 = R_1$||
>>|$-2$|$1$|$2$|$0 = R_2$|||
>>|$-2$|$1$|$0 = R_3$||||
>>|$-2$|$1 = R_4$|||||
>>
>>We have
>>
>>$$
>>\begin{aligned}
>>B(y) &= R_0 + R_1 y + R_2 y^2 + R_3 y^3 + R_4 y^4 \\ 
>>&= 38 + 18y + y^4 \\
>>&= y^4 + 18y + 38 \\
>>&= (x+2)^4 + 18(x + 2) + 38
>>\end{aligned}
>>$$
>>
>