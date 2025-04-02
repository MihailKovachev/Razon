---
title: Real Polynomial Equations
tags:
  - real-polynomial-equations
  - polynomial-equations
  - equations
  - algebra
  - mathematics
---

# Polynomial Equations

>[!DEFINITION] Definition: Real Polynomial Equation
>
>A **real polynomial equation** is a [polynomial equation](index.md) $P = 0$ where $P$ is a [real polynomial](../../Fields/The%20Real%20Numbers/Real%20Polynomials.md).
>

## Properties

>[!THEOREM] Theorem: Real Polynomial Equations with Integer Coefficients
>
>If the coefficients $a_0, \cdots, a_n$ of the [real polynomial equation](Real%20Polynomial%20Equations.md)
>
>$$
>a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0 = 0
>$$
>
>are [integers](TODO) and it has a [rational](TODO) [root](../../Rings/Commutative%20Rings/Polynomials/Polynomials.md) $x^\ast = \frac{p}{q}$ (where $p$ and $q$ are [coprime](TODO)), then $p$ is a [divisor](TODO) of $a_0$ and $q$ is a divisor of $a_n$.
>
>>[!PROOF]-
>>
>>**Proof that** $q$ **is a divisor of** $a_n$**:**
>>
>>If $x^\ast = \frac{p}{q}$ is a root of the polynomial equation, then
>>
>>$$
>>a_n \frac{p^n}{q^n} + a_{n-1} \frac{p^{n-1}}{q^{n-1}} + \cdots + a_1 \frac{p}{q} + a_0 = 0
>>$$
>>
>>Multiply by $q^{n-1}$.
>>
>>$$
>>a_n \frac{p^n}{q} + a_{n-1} p^{n-1} + \cdots + a_1 p q^{n-2} + a_0 q^{n-1} = 0
>>$$
>>
>>$$
>>a_n \frac{p^n}{q} = - a_{n-1} p^{n-1} - \cdots - a_1 p q^{n-2} - a_0 q^{n-1}
>>$$
>>
>>Since $p,q$ and $a_k$ are all integers, the right-hand side must be an integer as well. This means that $a_n \frac{p^n}{q}$ is an integer, but $p^n$ and $q$ have no common divisors, since they are coprime. This means that $q$ must divide $a_n$.
>>
>>**Proof that** $p$ **is a divisor of** $a_0$**:**
>>
>>If $x^\ast = \frac{p}{q}$ is a root of the polynomial equation, then
>>
>>$$
>>a_n \frac{p^n}{q^n} + a_{n-1} \frac{p^{n-1}}{q^{n-1}} + \cdots + a_1 \frac{p}{q} + a_0 = 0
>>$$
>>
>>Multiply by $q^n$.
>>
>>$$
>>a_n p^n + a_{n-1} p^{n-1} q + \cdots + a_1 p q^{n-1} + a_0 q^n = 0
>>$$
>>
>>Divide by $p$.
>>
>>$$
>>a_n p^n + a_{n-1} p^{n-1} q + \cdots + a_1 p q^{n-1} + a_0 q^n = 0
>>$$
>>
>>$$
>>a_n p^{n-1} + a_{n-1} p^{n-2} q + \cdots + a_1 q^{n-1} + a_0 \frac{q^n}{p} = 0
>>$$
>>
>>$$
>>a_0 \frac{q^n}{p} = - a_n p^{n-1} - a_{n-1} p^{n-2} q - \cdots - a_1 q^{n-1}
>>$$
>>
>>Once again, $p,q$ and $a_k$ are all integers and so the right-hand side must be an integer. This means that $a_0 \frac{q^n}{p}$ is an integer. The numbers $q^n$ and $p$ have no common divisors, since $q$ and $p$ are coprime. This means that $p$ must be a divisor of $a_0$.
>>
>

# Reciprocal Polynomial Equations

>[!DEFINITION] Definition: Reciprocal Polynomial Equations
>
>A **reciprocal polynomial equation** is a [polynomial equation](Real%20Polynomial%20Equations.md) which can be written either as
>
>$$
>a_0 x^{2n} + a_1x^{2n - 1} + \cdots + a_{n-1} x^{n+1} + a_n x^n + a_{n-1} p x^{n-1} + \cdots + a_1 p^{n-1}x + a_0 p^n = 0
>$$
>
>or as
>
>$$
>a_0 x^{2n + 1} + a_1 x^{2n} + \cdots + a_n x^{n+1} + a_n p x^n + a_{n-1} p^3 x^{n-1} + \cdots + a_1 p^{2n - 1}x + a_0 p^{2n+1} = 0.
>$$
>

>[!DEFINITION] Definition: Reciprocal Polynomial Equations

## Properties

>[!THEOREM]- Algorithm: Degree Reduction for Reciprocal Polynomial Equations of Even Degree
>
>We are given a [reciprocal polynomial equation](Real%20Polynomial%20Equations.md#Reciprocal%20Polynomial%20Equations)
>
>$$
>a_0 x^{2n} + a_1x^{2n - 1} + \cdots + a_{n-1} x^{n+1} + a_n x^n + a_{n-1} p x^{n-1} + \cdots + a_1 p^{n-1}x + a_0 p^n = 0
>$$
>
>of degree $2n$. 
>
>1. Divide by $x^n$.
>2. Substitute $y = x + \frac{p}{x}$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Roots of Reciprocal Polynomial Equations of Odd Degree
>
>Every [reciprocal polynomial equation](Real%20Polynomial%20Equations.md#Reciprocal%20Polynomial%20Equations)
>
>$$
>a_0 x^{2n + 1} + a_1 x^{2n} + \cdots + a_n x^{n+1} + a_n p x^n + a_{n-1} p^3 x^{n-1} + \cdots + a_1 p^{2n - 1}x + a_0 p^{2n+1} = 0.
>$$
>
>of odd degree $2n+1$ has the root $x = -p$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Reduction of Reciprocal Polynomial Equations of Odd Degree
>
>Every [reciprocal polynomial equation](Real%20Polynomial%20Equations.md#Reciprocal%20Polynomial%20Equations)
>
>$$
>a_0 x^{2n + 1} + a_1 x^{2n} + \cdots + a_n x^{n+1} + a_n p x^n + a_{n-1} p^3 x^{n-1} + \cdots + a_1 p^{2n - 1}x + a_0 p^{2n+1} = 0.
>$$
>
>of odd degree $2n+1$ can be reduced to a [reciprocal polynomial equation](Real%20Polynomial%20Equations.md#Reciprocal%20Polynomial%20Equations) of even degree $2n$ by dividing it by $x+p$.
>
>>[!PROOF]-
>>
>>TODO
>>
>