---
tags:
    - electrical-engineering
---

# Sinusoidal Signals

>[!DEFINITION] Definition: Sinusoidal Signal
>
>A **sinusoidal signal** is a [real function](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) $x: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ which can be expressed as
>
>$$x(t) = X_{\text{max}} \cos(\omega t + \phi)$$
>
>for some $X_$
>

## Phasors

>[!DEFINITION] Definition: Phasors
>
>The **phasor** of a [sinusoidal signal](./Sinusoidal%20Signals.md)
>
>$$x(t) = X_{\text{m}}\cos(\omega t + \phi)$$
>
>is the [complex number](../../Mathematics/Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md) given by the multiplication of the [amplitude](./Sinusoidal%20Signals.md) $X_{\text{m}}$ with the [complex exponential](../../Mathematics/Analysis/Complex%20Analysis/Complex%20Functions/Complex%20Exponential%20Function.md) $\mathrm{e}^{\mathrm{j}\phi}$:
>
>$$X \overset{\text{def}}{=} X_m \mathrm{e}^{\mathrm{j}\phi}$$
>

>[!THEOREM] Theorem: Signal from Phasor
>
>A [sinusoidal signal](./Sinusoidal%20Signals.md)
>
>$$x(t) = X_{\text{m}}\cos(\omega t + \phi)$$
>
>is equal to the [real part](../../Mathematics/Analysis/Complex%20Analysis/Complex%20Functions/Complex%20Functions.md) of the multiplication of its [phasor](#Phasors) $X$ by $\mathrm{e}^{\mathrm{j}\omega t}$:
>
>$$x(t) = \operatorname{Re} (X \mathrm{e}^{\mathrm{j} \omega t})$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Signal Equality $\iff$ Phasor Equality
>
>Two [sinusoidal signals](./Sinusoidal%20Signals.md) are identical if and only if their [phasors](#Phasors) are the same.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Linearity of the Phasor Transform
>
>If a [sinusoidal signal](./Sinusoidal%20Signals.md) $x(t)$ can be expressed as a [linear combination](../../Mathematics/Algebra/Vector%20Spaces/Linear%20Combinations.md) 
>
>$$x(t) = \sum_{k=1}^n \lambda_k x_k(t)$$
>
>of [sinusoidal signals](./Sinusoidal%20Signals.md) $x_1(t), \dotsc, x_n(t)$ with the same [frequency](./Sinusoidal%20Signals.md), then its [phasor](#Phasors) can be expressed as a [linear combination](../../Mathematics/Algebra/Vector%20Spaces/Linear%20Combinations.md) of their [phasors](#Phasors) $X_1, \dotsc, X_n$ with the same coefficients:
>
>$$X = \sum_{k=1}^n \lambda_k X_k$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Differentiation and Phasors
>
>If a [sinusoidal signal](./Sinusoidal%20Signals.md)
>
>$$x(t) = X_{\text{m}} \cos(\omega t + \phi)$$
>
>has the [phasor](#Phasors) $X$, then its [derivative](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Differentiability%20(Real%20Functions).md) has the following [phasor](#Phasors):
>
>$$\mathrm{j}\omega X$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antidifferentiation and Phasors
>
>If a [sinusoidal signal](./Sinusoidal%20Signals.md)
>
>$$x(t) = X_{\text{m}} \cos(\omega t + \phi)$$
>
>has the [phasor](#Phasors) $X$, then its [antiderivative](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Antidifferentiability%20(Real%20Functions).md) has the following [phasor](#Phasors):
>
>$$\frac{1}{\mathrm{j}\omega} X$$
>
>>[!PROOF]-
>>
>>TODO
>>
>