---
title: The Complex Exponential Function
tags:
    - exponentials
    - complex-functions
    - complex-analysis
    - analysis
    - mathematics
---

# The Complex Exponential

>[!THEOREM] Theorem: Complex Exponential
>
>The [complex power series](../Complex%20Power%20Series/Complex%20Power%20Series.md)
>
>$$
>\sum_{n = 0}^{\infty} \frac{z^n}{n!} = 1 + \frac{z^1}{1!} +  \frac{z^2}{2!} + \frac{z^3}{3!} + \frac{z^4}{4!} + \cdots
>$$
>
>[converges absolutely](../Complex%20Power%20Series/Convergence.md) for all $z \in \mathbb{C}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Complex Exponential
>>
>>The [complex function](Complex%20Functions.md) $\exp: \mathbb{C} \to \mathbb{C}$ defined as
>>
>>$$
>>\exp (z) = \sum_{n = 0}^{\infty} \frac{z^n}{n!}
>>$$
>>
>>is known as the **complex exponential function**.
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\exp z \qquad \exp(z) \qquad \mathrm{e}^z
>>>$$
>>>
>>
>>>[!NOTE]
>>>
>>>The [restriction](../../Functions/Restriction.md) of the [complex exponential function](The%20Complex%20Exponential%20Function.md) to $\mathbb{R}$ is the [real exponential function](../../Real%20Analysis/Real%20Functions/The%20Real%20Exponential%20Function.md).
>>>
>>
>

## Properties

>[!THEOREM] Theorem: Periodicity of the Complex Exponential
>
>The [complex exponential function](The%20Complex%20Exponential%20Function.md) is [periodic](Periodicity.md) with period $2\pi \mathrm{i}$:
>
>$$
>\exp(z + 2k\pi \mathrm{i}) = \exp (z) \qquad \forall z \in \mathbb{C}, \forall k \in \mathbb{Z}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Euler's Formula
>
>For every $\varphi \in \mathbb{R}$, the real part of the [complex exponential](The%20Complex%20Exponential%20Function.md) $\mathrm{e}^{\mathrm{i}\varphi}$ is the [real cosine](../../Real%20Analysis/Real%20Functions/Real%20Trigonometric%20Functions/Real%20Cosine%20Function/Real%20Cosine%20Function.md) of $\varphi$ and the imaginary part is the [real sine](../../Real%20Analysis/Real%20Functions/Real%20Trigonometric%20Functions/Real%20Cosine%20Function/Real%20Cosine%20Function.md) of $\varphi$:
>
>$$
>\mathrm{e}^{\mathrm{i}\varphi} = \cos \varphi + \mathrm{i} \sin \varphi
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Exponent Arithmetic
>
>The [complex exponential](The%20Complex%20Exponential%20Function.md) of a sum is equal to the product of the complex exponentials of its terms:
>
>$$
>\mathrm{e}^{z + w} = \mathrm{e}^z \cdot \mathrm{e}^w \qquad \forall z,w \in \mathbb{C}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Modulus of the Complex Exponential
>
>For all $z \in \mathbb{C}$, the [modulus](../../../Algebra/Fields/The%20Complex%20Numbers/index.md) of the [complex exponential](The%20Complex%20Exponential%20Function.md) of $z$ is the [real exponential](../../Real%20Analysis/Real%20Functions/The%20Real%20Exponential%20Function.md) of its real part:
>
>$$
>|\mathrm{e}^z| = \mathrm{e}^{\operatorname{Re}(z)}
>$$
>
>>[!PROOF]-
>>
>>Let $x = \operatorname{Re}(z)$ and $y = \operatorname{Im}(z)$.
>>
>>$$
>>\begin{align*}
>>
>>|\mathrm{e}^z| = \left| \mathrm{e}^{x + \mathrm{i} y} \right| &= \left| \mathrm{e}^{x} \cdot \mathrm{e}^{\mathrm{i} y} \right| \\ &= \left| \mathrm{e}^{x} \cdot \cos y + \mathrm{i} \sin y \right| \\ &= \left| \mathrm{e}^{x} \sqrt{\cos^2 y + \sin^2 y} \right| \\ &= \left|\mathrm{e}^{x} \cdot \sqrt{1}\right| \\ &= \left|\mathrm{e}^{\operatorname{Re}(z)}\right| = \mathrm{e}^{\operatorname{Re}(z)}
>>
>>\end{align*}
>>$$
>>
>