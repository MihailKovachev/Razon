---
tags:
  - real-analysis
  - analysis
  - mathematics
---

# Real Tangent Function

>[!DEFINITION] Definition: Real Tangent Function
>
>The **real tangent function** is defined as the [ratio](../../Real-Valued%20Functions.md) of the [real sine function](#Real%20Sine%20Function) to the [real cosine function](#Real%20Cosine%20Function).
>
>$$\tan(x) \overset{\text{def}}{=} \frac{\sin(x)}{\cos(x)}$$
>
>>[!NOTE]
>>
>>The [domain](../../../Functions/Functions.md) of the [real tangent function](#Real%20Tangent%20Function) is $\{x \in \mathbb{R}\mid x\ne \frac{\pi}{2}+k\pi, k \in \mathbb{Z}\}$ because $\cos (\frac{\pi}{2}+k\pi) = 0$ for all $k \in \mathbb{Z}$.
>>
>
>>[!NOTATION]
>>
>>$$\tan (x) \qquad \mathop{\operatorname{tg}}(x)$$
>>
>

>[!THEOREM] Theorem: Image of the Real Tangent Function
>
>The [image](../../../Functions/Functions.md) of the [real tangent function](#Real%20Tangent%20Function) is $(-\infty;+\infty)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Periodicity of the Real Tangent Function
>
>The [real tangent function](#Real%20Tangent%20Function) has a [period](../Periodicity.md) of $\pi$. More generally,
>
>$$\tan(x + k\pi) = \tan (x) \qquad \forall k \in \mathbb{Z}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity of the Real Tangent Function
>
>The [real tangent function](#Real%20Tangent%20Function) is [continuous](../Continuity%20(Real%20Functions).md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Derivative of the Real Tangent Function
>
>The [real tangent function](#Real%20Tangent%20Function) is [differentiable](../Differentiability%20(Real%20Functions).md) and its [derivative](../Differentiability%20(Real%20Functions).md) is the recirpocal of the square of the [real cosine function](#Real%20Cosine%20Function):
>
>$$(\tan x)' = \frac{1}{\cos^2 x} = 1 + \tan^2 x$$
>
>>[!PROOF]-
>>
>>$$(\tan x)' = \left(\frac{\sin x}{\cos x}\right)' = \frac{(\sin x)'\cos x - (\cos x)'\sin x}{\cos^2 x} = \frac{\cos^2 x + \sin^2 x}{\cos^2 x} = \frac{1}{\cos^2 x}$$
>>
>