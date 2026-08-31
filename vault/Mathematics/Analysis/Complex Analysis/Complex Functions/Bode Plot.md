---
tags:
    - complex-analysis
    - analysis
    - mathematics
---

# Bode Plot

A **Bode plot** is a way of visualizing [complex-valued functions](../Complex-Valued%20Functions.md) $H: (0, +\infty) \to \mathbb{R}$ defined on the positive [real numbers](../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md). [Bode plots](./Bode%20Plot.md) are used ubiquitously in engineering to illustrate how [linear time-invariant systems](TODO) react to [sinusoidal inputs](TODO) withs varying frequencies.

## Bode Magnitude Plot

>[!DEFINITION] Definition: Gain
>
>Let $H: (0, +\infty) \to \mathbb{R}$ be a [complex-valued function](../Complex-Valued%20Functions.md) and let $\omega \in (0, +\infty)$.
>
>The **gain** at $\omega$ is defined as $20$ times the base-10 [logarithm](../../Real%20Analysis/Real%20Functions/Real%20Logarithms.md) of the [absolute value](../../../Algebra/Fields/The%20Complex%20Numbers/Absolute%20Value%20(Complex%20Numbers).md) of $H(\omega)$:
>
>$$20 \log_{10} |H(\omega)|$$
>
>>[!NOTATION]
>>
>>There isn't any standard notation for this, but we can denote it as $\text{Gain}(\omega)$ or $\text{Gain}_H(\omega)$.
>>
>

The **Bode magnitude plot** of $H$ is a [logarithmic plot](TODO) of the [gain](#Bode%20Magnitude%20Plot) on a vertical [linear axis](TODO) against $\omega$ on a horizontal [logarithmic axis](TODO):

![Bode Magnitude Plot](./res/Bode%20Magnitude%20Plot.svg)

## Bode Phase Plot

>[!DEFINITION] Definition: Phase Shift
>
>Let $H: (0, +\infty) \to \mathbb{R}$ be a [complex-valued function](../Complex-Valued%20Functions.md) and let $\omega \in (0, +\infty)$.
>
>The **phase shift** at $\omega$ is the [principal argument](../../../Algebra/Fields/The%20Complex%20Numbers/Principal%20Argument%20(Complex%20Numbers).md) of $H(\omega)$:
>
>$$\operatorname{Arg} H(\omega)$$
>
>>[!NOTATION]
>>
>>There isn't any standard notation for this, but we can denote it as $\text{Phase}(\omega)$ or $\text{Phase}_H(\omega)$.
>>
>

The **Bode phase plot** of $H$ is a [logarithmic plot](TODO) of the [phase shift](#Bode%20Phase%20Plot) on a vertical [linear axis](TODO) against $\omega$ on a horizontal [logarithmic axis](TODO):

![Bode Phase Plot](./res/Bode%20Phase%20Plot.svg)