---
title: Real Trigonometric Functions
tags:
  - real-analysis
  - mathematical-analysis
  - mathematics
---

# Real Trigonometric Functions

## The Real Sine Function

## The Real Cosine Function



## The Real Cotangent Function

>[!DEFINITION] Definition: Real Cotangent Function
>
>The **real cotangent function** is defined as the [ratio](../../Real-Valued%20Functions.md) of the [real cosine function](#The%20Real%20Cosine%20Function) to the [real sine function](#The%20Real%20Sine%20Function).
>
>$$\cot(x) \overset{\text{def}}{=} \frac{\cos(x)}{\sin(x)}$$
>
>>[!NOTE]
>>
>>The [domain](../../../Functions/Functions.md) of the [real cotangent function](#The%20Real%20Cotangent%20Function) is $\{x \in \mathbb{R}\mid x\ne k\pi, k \in \mathbb{Z}\}$ because $\sin (k\pi) = 0$ for all $k \in \mathbb{Z}$.
>>
>
>>[!NOTATION]-
>>
>>$$\cot (x) \qquad \mathop{\operatorname{ctg}}(x) \qquad \mathop{\operatorname{cotg}}(x)$$
>>
>

>[!THEOREM] Theorem: Image of the Real Cotangent Function
>
>The [image](../../../Functions/Functions.md) of the [real cotangent function](#The%20Real%20Cotangent%20Function) is $(-\infty; +\infty)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Periodicity of the Real Cotangent Function
>
>The [real cotangent function](#The%20Real%20Cotangent%20Function) has a [period](../Periodicity.md) of $\pi$. More generally,
>
>$$\cot(x + k\pi) = \cot (x) \qquad \forall k \in \mathbb{Z}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity of the Real Cotangent Function
>
>The [real cotangent function](#The%20Real%20Cotangent%20Function) is [continuous](../Continuity%20(Real%20Functions).md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Derivative of the Real Cotangent Function
>
>The [real cotangent function](#The%20Real%20Cotangent%20Function) is [differentiable](../Differentiability%20(Real%20Functions).md) and its [derivative](../Differentiability%20(Real%20Functions).md) is the negative reciprocal of the square of the [real sine function](#The%20Real%20Sine%20Function):
>
>$$(\cot x)' = - \frac{1}{\sin^2 x} = -1 - \cot^2 x$$
>
>>[!PROOF]-
>>
>>$$(\cot x)' = \left(\frac{\cos x}{\sin x}\right)^\prime = \frac{(\cos x)^\prime \sin x - (\sin x)^\prime \cos x}{\sin^2 x} = \frac{-\sin^2 x -\cos^2 x}{\sin^2 x} = \frac{-(\sin^2 x + \cos^2 x)}{\sin^2 x} = \frac{-1}{\sin^2 x}$$
>>
>

>[!THEOREM] Theorem: Antiderivatives of $\cot$
>
>The [antidirivatives](../Antidifferentiability%20(Real%20Functions).md) of the [real cotangent](./Real%20Trigonometric%20Functions.md) are given by
>
>$$\int \cot x \mathop{\mathrm{d}x} = \ln |\sin x| + C$$
>
>>[!PROOF]-
>>
>>TODO
>>
>