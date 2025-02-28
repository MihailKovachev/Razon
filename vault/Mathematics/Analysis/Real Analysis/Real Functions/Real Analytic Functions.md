---
title: Real Analytic Functions
tags:
  - analytic-functions
  - real-functions
  - real-analysis
  - analysis
  - mathematics
---

>[!DEFINITION] Definition: Real Analytic Function
>
>A **real analytic function** is a [real function](Real%20Functions.md) $f: D \to \mathbb{R}$ on an [open interval](../../../../../Set%20Theory/Ordering/Intervals.md) $D \subseteq \mathbb{R}$ for which there exists a [real power series](../Real%20Power%20Series/index.md) $\displaystyle \sum_{n=0}^\infty c_n (x-a)^n$ [](../Real%20Power%20Series/Convergence.md#^intervalofconvergence) on $D$ with
>
>$$
>f(x) = \displaystyle \sum_{n=0}^\infty c_n (x-a)^n \qquad \forall x \in D
>$$
>

# Properties

>[!THEOREM] Theorem: Differentiation of Real Analytic Functions
>
>Every [real analytic function](Real%20Analytic%20Functions.md) $f(x) = \displaystyle \sum_{n=0}^\infty c_n (x-a)^n$ is [differentiable](Differentiation/Derivatives.md) on $D$ and its derivative $f'(x)$ is also a real analytic function given by
>
>$$
>f'(x) = \sum_{n=1}^\infty n c_n (x-a)^{n-1}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antiderivatives of Real Analytic Functions
>
>The [antiderivatives](Integration/Antiderivatives.md) of any [real analytic function](Real%20Analytic%20Functions.md) $f(x) = \displaystyle \sum_{n = 0}^\infty c_n (x-a)^n$ are also real analytic functions and $f$'s [indefinite integral](Integration/Antiderivatives.md) is given by
>
>$$
>\int f(x) \mathop{\mathrm{d}x} = C + \sum_{n = 0}^\infty c_n \frac{(x - a)^{n+1}}{n+1}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>