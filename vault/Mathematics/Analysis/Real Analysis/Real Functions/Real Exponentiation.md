---
tags:
  - real-mathematical-analysis
  - mathematical-analysis
  - mathematics
---

# Real Exponentiation

## The Real Exponential Function

>[!THEOREM] Theorem: The Real Exponential Function
>
>The [real power series](../Real%20Power%20Series.md) $\displaystyle \sum_{n = 0}^\infty \frac{x^n}{n!}$ [converges](../Real%20Power%20Series.md#Convergence) for all $x \in \mathbb{R}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: The Real Exponential Function
>>
>>The **real exponential function** is the [real analytic function](./Real%20Analytic%20Functions.md) $\exp: \mathbb{R} \to \mathbb{R}$ defined by this [real power series](../Real%20Power%20Series.md).
>>
>>$$
>>\exp(x) \overset{\text{def}}{=} \sum_{n = 0}^\infty \frac{x^n}{n!}
>>$$
>>
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\exp(x) \qquad \mathrm{e}^x
>>>$$
>>>
>>
>

>[!THEOREM] Theorem: Image of the Real Exponential Function
>
>The [image](../../Functions/Functions.md) of the [real exponential function](./Real%20Exponentiation.md) is the [open interval](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) $(0;+\infty)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Monotony of the Real Exponential Function
>
>The [real exponential function](./Real%20Exponentiation.md) is [strictly increasing](./Monotonicity%20of%20Real%20Functions.md).
>
>$$
>\mathrm{e}^x \lt \mathrm{e}^y \iff x \lt y
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Addition Theorem for the Real Exponential Function
>
>The [real exponential function](./Real%20Exponentiation.md) has the following property for all $x,y \in \mathbb{R}$:
>
>$$
>\mathrm{e}^x \mathrm{e}^y = \mathrm{e}^{x + y}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Derivative of the Real Exponential Function
>
>The [real exponential function](./Real%20Exponentiation.md) is [differentiable](./Differentiability%20(Real%20Functions).md) with
>
>$$
>(\mathrm{e}^x)' = \mathrm{e}^x
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antiderivatives of the Real Exponential Function and Variations
>
>The [real exponential function](./Real%20Exponentiation.md) $e^{x}$ is [antidifferentiable](./Antidifferentiability%20(Real%20Functions).md) on $\mathbb{R}$:
>
>$$\int \mathrm{e}^x \,\mathrm{d}x = \mathrm{e}^x + C$$
>
>The [function](./Real%20Functions.md) $\mathrm{e}^{\alpha x}$ is [antidifferentiable](./Antidifferentiability%20(Real%20Functions).md) on $\mathbb{R}$ for all $\alpha \ne 0$:
>
>$$\int \mathrm{e}^{\alpha x} \,\mathrm{d}x = \frac{1}{\alpha} \mathrm{e}^{\alpha x} + C$$
>
>If a [real function](./Real%20Functions.md) $f$ is [differentiable](./Differentiability%20(Real%20Functions).md) on some [open interval](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) $I$, then $f'(x)\mathrm{e}^{f(x)}$ is [antidifferentiable](./Antidifferentiability%20(Real%20Functions).md) on $I$:
>
>$$\int f'(x)\mathrm{e}^{f(x)} \,\mathrm{d}x = \mathrm{e}^{f(x)} + C$$
>
>If a [real function](./Real%20Functions.md) $f$ is [differentiable](./Differentiability%20(Real%20Functions).md) on some [open interval](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) $I$, then $\mathrm{e}^x(f(x) + f'(x))$ is [antidifferentiable](./Antidifferentiability%20(Real%20Functions).md) on $I$:
>
>$$\int \mathrm{e}^x(f(x) + f'(x)) \,\mathrm{d}x = \mathrm{e}^x f(x) + C$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: The Real Exponential through Convergent Sequences
>
>The [real exponential function](./Real%20Exponentiation.md) $e^x$ is equal to the [limit](../Real%20Sequences.md#Convergence) of the following [real sequence](../Real%20Sequences.md):
>
>$$e^x = \lim_{n \to \infty} \left(1 + \frac{x}{n}\right)^n$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Real Exponentiation in Bachmann-Landau
>
>The [real exponential](./Real%20Exponentiation.md) $\mathrm{e}^x$ can be expressed in [Bachmann-Landau notation](../Asymptotic%20Analysis/Bachmann-Landau%20Notation.md) for $x \to 0$ as follows:
>
>$$\mathrm{e}^x = \sum_{k=0}^m \frac{x^k}{k!} + O(x^{m+1}) \qquad \text{for} \qquad x \to 0$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Exponentiation

>[!DEFINITION] Definition: Exponentiation
>
>Let $a$ and $b$ be [real numbers](../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md).
>
>We define the **exponentiation** $a^b$ as
>
>$$a^b \overset{\text{def}}{=}\left\{\begin{array}{l@{\quad}l}1 & \text{if } a \ne 0, b = 0 \\\underset{b\text{ times}}{\underbrace{a \times \cdots \times a}} & \text{if } b \in \mathbb{N} \\\sqrt[n]{a^m} & \text{if } b = \frac{m}{n} \text{ with } m,n \in \mathbb{N}\end{array}\right.$$
>

>[!THEOREM] Theorem: Antidifferentiability of Exponentiation
>
>The [exponential](#Exponentiation) $a^x$ is [antidifferentiable](./Antidifferentiability%20(Real%20Functions).md) on $\mathbb{R}$ for all $a \gt 0$ and for $a \ne 1$ its [antiderivatives](./Antidifferentiability%20(Real%20Functions).md) can be constructed via the [real natural logarithm](./Real%20Logarithms.md#The%20Real%20Natural%20Logarithm):
>
>$$\int a^x \,\mathrm{d}x = \frac{a^x}{\ln a} + C$$
>
>>[!PROOF]-
>>
>>TODO
>>
>