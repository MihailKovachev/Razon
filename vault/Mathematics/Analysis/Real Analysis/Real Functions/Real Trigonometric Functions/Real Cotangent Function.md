---
title: The Real Cotangent Function
tags:
  - real-analysis
  - analysis
  - mathematics
---

# The Real Cotangent Function

>[!DEFINITION] Definition: Real Cotangent Function
>
>The **real cotangent function** is defined as the ratio of the [real cosine function](Real%20Cosine%20Function.md) to the [real sine function](Real%20Sine%20Function.md).
>
>$$
>\cot(x) \overset{\text{def}}{=} \frac{\cos(x)}{\sin(x)}
>$$
>
>>[!NOTE]
>>
>>The [domain](../../../Functions/Functions.md) of the [real cotangent function](Real%20Cotangent%20Function.md) is $\{x \in \mathbb{R}\mid x\ne k\pi, k \in \mathbb{Z}\}$ because $\sin (k\pi) = 0$ for all $k \in \mathbb{Z}$.
>>
>
>>[!NOTATION]-
>>
>>$$
>>\cot (x) \qquad \mathop{\operatorname{ctg}}(x) \qquad \mathop{\operatorname{cotg}}(x)
>>$$
>>
>

## Properties

>[!THEOREM]- Theorem: Image of the Real Cotangent Function
>
>The [image](../../../Functions/Functions.md) of the [real cotangent function](Real%20Cotangent%20Function.md) is $(-\infty; +\infty)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>


>[!THEOREM]- Theorem: Periodicity of the Real Cotangent Function
>
>The [real cotangent function](Real%20Cotangent%20Function.md) has a [period](../Periodicity.md) of $\pi$. More generally,
>
>$$
>\cot(x + k\pi) = \cot (x) \qquad \forall k \in \mathbb{Z}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Continuity of the Real Cotangent Function
>
>The [real cotangent function](Real%20Cotangent%20Function.md) is [continuous](../Continuity.md) (everywhere it is defined).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Derivative of the Real Cotangent Function
>
>The [real cotangent function](Real%20Cotangent%20Function.md) is [differentiable](../Differentiability.md) (everywhere it is defined) and its [derivative](../Differentiability.md) is the negative reciprocal of the square of the [real sine function](Real%20Sine%20Function.md):
>
>$$
>(\cot x)' = - \frac{1}{\sin^2 x} = -1 - \cot^2 x
>$$
>
>>[!PROOF]-
>>
>>$$
>>(\cot x)' = \left(\frac{\cos x}{\sin x}\right)^\prime = \frac{(\cos x)^\prime \sin x - (\sin x)^\prime \cos x}{\sin^2 x} = \frac{-\sin^2 x -\cos^2 x}{\sin^2 x} = \frac{-(\sin^2 x + \cos^2 x)}{\sin^2 x} = \frac{-1}{\sin^2 x}
>>$$
>>
>