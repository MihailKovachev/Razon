---
title: Ordinary Differential Equations (ODEs)
tags:
    - ordinary-differential-equations
    - differential-equations
    - equations
    - algebra
    - mathematics
---

# Ordinary Differential Equations

>[!DEFINITION] Definition: Ordinary Differential Equation
>
>An **ordinary differential equation** of order $n$ is an [equation](../../Equation.md) which can be written as
>
>$$
>F\left(x, y, y', y'', \dotsc, y^{(n)}\right) = 0,
>$$
>
>where $F$ is some expression containing $x, y, y', y'', \dotsc, y^{(n)}$.
>
>>[!DEFINITION] Definition: Solution to an ODE
>>
>>A **solution** to the ODE on the [subset](../../../../Set%20Theory/Sets.md) $\mathcal{D} \subseteq \mathbb{R}$ is an $n$-times [differentiable](../../../../Analysis/Real%20Analysis/Real%20Functions/Differentiability.md) [real function](../../../../Analysis/Real%20Analysis/Functions%20of%20the%20Real%20Numbers.md) $\phi: \mathcal{D} \to \mathbb{R}$ such that
>>
>>$$
>>F\left(x, \phi(x), \phi'(x), \phi''(x), \dotsc, \phi^{(n)}(x)\right) = 0 \qquad \forall x \in \mathcal{D}
>>$$
>>
>

# Ordinary Initial Value Problems

>[!DEFINITION] Definition: Ordinary Initial Value Problem
>
>An **ordinary initial value problem** of order $n$ consists of an $n$-th order [ODE](./index.md)
>
>$$
>F\left(x, y, y', y'', \dotsc, y^{(n)}\right) = 0
>$$
>
>and a system of $n$ 
>