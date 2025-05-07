---
title: The Real Cosine Function
tags:
  - real-analysis
  - analysis
  - mathematics
---

# The Real Cosine Function

>[!THEOREM] Theorem: Convergence of the Cosine Power Series
>
>The [real power series](../../Real%20Power%20Series/index.md) $\displaystyle \sum_{n=0}^\infty (-1)^n \frac{x^{2n}}{(2n)!}$ is [convergent](../../Real%20Power%20Series/Convergence.md) for all $x \in \mathbb{R}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Real Cosine Function
>>
>>The **real cosine function** is the [real analytic function](../Real%20Analytic%20Functions.md) $\cos: \mathbb{R} \to \mathbb{R}$ defined by the [real power series](../../Real%20Power%20Series/index.md) $\displaystyle \sum_{n=0}^\infty (-1)^n \frac{x^{2n}}{(2n)!}$.
>>
>>$$
>>\cos(x) = 1 - \frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}+\cdots
>>$$
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>\cos x \qquad \cos (x)
>>>$$
>>>
>>
>

## Properties

>[!THEOREM]- Theorem: Parity of the Real Cosine Function
>
>The [real cosine function](Real%20Cosine%20Function.md) is [](../Parity.md#^even-function):
>
>$$
>\cos(-x) = \cos(x)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Image of the Real Cosine Function
>
>The [image](../../../Functions/Functions.md) of the [real cosine function](Real%20Cosine%20Function.md) is $[-1;1]$.
>
>$$
>\cos(\mathbb{R}) = [-1;1]
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Periodicity of the Real Cosine Function
>
>The [real cosine function](Real%20Cosine%20Function.md) has a [period](../Periodicity.md) of $2\pi$. More generally,
>
>$$
>\cos (x + 2k\pi) = \cos(x) \qquad \forall k\in\mathbb{Z}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>


>[!THEOREM]- Theorem: Antiperiodicity of the Real Cosine Function
>
>The [real cosine function](Real%20Cosine%20Function.md) has an [antiperiod](../Periodicity.md) of $\pi$. More generally,
>
>$$
>\cos (x + (2k+1) \pi) = -\cos(x) \qquad k \in \mathbb{Z}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>


>[!THEOREM]- Theorem: Continuity of the Real Cosine Function
>
>The [real cosine function](Real%20Cosine%20Function.md) is [continuous](../Continuity.md) on $\mathbb{R}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Derivative of the Real Cosine Function
>
>The [real cosine function](Real%20Cosine%20Function.md) is [differentiable](../Differentiability.md) everywhere and its [derivative](../Differentiability.md) is the negative [real sine function](Real%20Sine%20Function.md).
>
>$$
>(\cos x)' = -\sin x
>$$
>
>>[!PROOF]-
>>
>>$$
>>(\cos x)' = \sin\left(\frac{\pi}{2} - x\right)' = \left(\frac{\pi}{2} - x\right)'\cos\left(\frac{\pi}{2} - x\right) = -\cos\left(\frac{\pi}{2} - x\right) = -\sin x
>>$$
>>
>