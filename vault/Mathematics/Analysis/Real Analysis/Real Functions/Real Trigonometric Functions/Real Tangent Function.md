---
title: Real Tangent Function
tags:
  - real-analysis
  - analysis
  - mathematics
---

# The Real Tangent Function

>[!DEFINITION] Definition: Real Tangent Function
>
>The **real tangent function** is defined as the ratio of the [real sine function](Real%20Sine%20Function.md) to the [real cosine function](Real%20Cosine%20Function.md).
>
>$$
>\tan(x) \overset{\text{def}}{=} \frac{\sin(x)}{\cos(x)}
>$$
>
>>[!NOTE]
>>
>>The [domain](../../../Functions/Functions.md) of the [real tangent function](Real%20Tangent%20Function.md) is $\{x \in \mathbb{R}\mid x\ne \frac{\pi}{2}+k\pi, k \in \mathbb{Z}\}$ because $\cos (\frac{\pi}{2}+k\pi) = 0$ for all $k \in \mathbb{Z}$.
>>
>
>>[!NOTATION]
>>
>>$$\tan (x) \qquad \mathop{\operatorname{tg}}(x)$$
>>
>

## Properties

>[!THEOREM]- Theorem: Image of the Real Tangent Function
>
>The [image](../../../Functions/Functions.md) of the [real tangent function](Real%20Tangent%20Function.md) is $(-\infty;+\infty)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Periodicity of the Real Tangent Function
>
>The [real tangent function](Real%20Tangent%20Function.md) has a [period](../Periodicity.md) of $\pi$. More generally,
>
>$$
>\tan(x + k\pi) = \tan (x) \qquad \forall k \in \mathbb{Z}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Continuity of the Real Tangent Function
>
>The [real tangent function](Real%20Tangent%20Function.md) is [continuous](../Continuity.md) (everywhere it is defined).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Derivative of the Real Tangent Function
>
>The [real tangent function](Real%20Tangent%20Function.md) is [differentiable](../Differentiability.md) (everywhere it is defined) and its [derivative](../Differentiability.md) is the recirpocal of the square of the [real cosine function](Real%20Cosine%20Function.md):
>
>$$
>(\tan x)' = \frac{1}{\cos^2 x} = 1 + \tan^2 x
>$$
>
>>[!PROOF]-
>>
>>$$
>>(\tan x)' = \left(\frac{\sin x}{\cos x}\right)' = \frac{(\sin x)'\cos x - (\cos x)'\sin x}{\cos^2 x} = \frac{\cos^2 x + \sin^2 x}{\cos^2 x} = \frac{1}{\cos^2 x}
>>$$
>>
>