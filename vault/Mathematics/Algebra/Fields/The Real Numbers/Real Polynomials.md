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

# Polynomial Division

>[!THEOREM] Theorem: Polynomial Division
>
>Let $A(x)$ and $B(x)$ be two [real polynomials](Real%20Polynomials.md) such that the [degree](../../Rings/Commutative%20Rings/Polynomials/Polynomials.md#Degree) of $A$ is greater than or equal to the degree of $B$.
>
>If $B(x)$ is [nonzero](../../Rings/Commutative%20Rings/Polynomials/Polynomials.md#Polynomials), then there exist unique polynomials $Q(x)$ and $R(x)$ such that
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

## Properties

>[!THEOREM]- Polynomial Remainder Theorem (Little Bézout's Theorem)
>
>The [remainder](Real%20Polynomials.md#Polynomial%20Division) $R$ upon the [division](Real%20Polynomials.md#Polynomial%20Division) of a [real polynomial](Real%20Polynomials.md) $A(x)$ with a [real polynomial](Real%20Polynomials.md) $B(x) = x - p$ is the [value](../../Rings/Commutative%20Rings/Polynomials/Polynomials.md#Evaluation) of $A$ at $p$.
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
>>Since the [degree](../Polynomials.md) of $B(x)$ is $1$, the degree of $R$ must either be $1$, i.e. $R$ is a constant and contains no variables or $R$ must be [zero](../Zero%20Polynomial.md). We can therefore denote $R(x)$ as just $R$. For $x = p$ we obtain 
>>
>>$$
>>A(p) = (p-p)Q(p) + R = 0 + R = R
>>$$
>>
>

>[!ALGORITHM]- Algorithm: Horner's Method
>
>**Horner's method** is a way to easily [divide](Real%20Polynomials.md#Polynomial%20Division) a [polynomial](Real%20Polynomials.md) $A(x)$ by a [polynomial](Real%20Polynomials.md) $B(x)$ of [degree](../../Rings/Commutative%20Rings/Polynomials/Polynomials.md#Degree) one.
> 
>1. Write $B(x)$ as $B(x) = x - p$. Since $\deg(B) = 1$, the [remainder](Real%20Polynomials.md#Polynomial%20Division) $R$ is just a [real number](The%20Real%20Numbers.md) because $\deg (R) \lt \deg(B) \implies \deg (R) = 0$. This means that we have
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
>We are given a [real polynomial](Real%20Polynomials.md) $A(x)$ and want to transform it into another [real polynomial](Real%20Polynomials.md) $B(y)$ where $y = x - p$ for some $p \in \mathbb{R}$.
>
>1. [Divide](Real%20Polynomials.md#Polynomial%20Division) $A$ by $(x-p)$.
>
>$$
>A(x) = (x-p) Q_1(x) + R_0
>$$
>
>2. [Divide](Real%20Polynomials.md#Polynomial%20Division) $Q_1$ by $(x-p)$.
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
>>You can use [Horner's method](Real%20Polynomials.md#Polynomial%20Division) to speed up the process.
>>
>
>>[!EXAMPLE]-
>>
>>Let $A(x) = x^4 + 8x^3 + 24x^2 + 50x + 90$ and let $y = x + 2$. We can write $y$ as $y = x - p$, where $p = -2$.
>>
>>Apply [Horner's method](Real%20Polynomials.md#Polynomial%20Division):
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
>>\begin{align*}
>>B(y) &= R_0 + R_1 y + R_2 y^2 + R_3 y^3 + R_4 y^4 \\ 
>>&= 38 + 18y + y^4 \\
>>&= y^4 + 18y + 38 \\
>>&= (x+2)^4 + 18(x + 2) + 38
>>\end{align*}
>>$$
>>
>