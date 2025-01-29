---
title: Ordinary Differential Equations (ODEs)
---

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
>>A [real function](../../../../Analysis/Real%20Analysis/Univariate%20Real%20Analysis/Real%20Functions/Real%20Function.md) $\phi: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ is a **solution** to the ODE on the [subset](../../../../Set%20Theory/Subset.md) $S \subseteq \mathcal{D}$ iff the [restriction](../../../../Analysis/Functions/Restriction.md) $\phi\big|_S$ is $n$-times [differentiable](../../../../Analysis/Real%20Analysis/Univariate%20Real%20Analysis/Differentiation/Differentiability%20of%20Real%20Functions.md) and
>>
>>$$
>>F\left(x, \phi(x), \phi'(x), \phi''(x), \dotsc, \phi^{(n)}(x)\right) = 0 \qquad \forall x \in S
>>$$
>>
>