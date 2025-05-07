---
title: The Real Sine Function
tags:
  - real-analysis
  - analysis
  - mathematics
---

# The Real Sine Function

>[!THEOREM] Theorem: Convergence of the Sine Power Series
>
>The [real power series](../../Real%20Power%20Series/index.md) $\displaystyle \sum_{n=0}^\infty (-1)^n\frac{x^{2n+1}}{(2n+1)!}$ is [convergent](../../Real%20Power%20Series/Convergence.md) for all $x \in \mathbb{R}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Real Sine Function
>>
>>The **real sine function** is the [real analytic function](../Real%20Analytic%20Functions.md) $\sin: \mathbb{R} \to \mathbb{R}$ defined by the [real power series](../../Real%20Power%20Series/index.md) $\displaystyle \sum_{n=0}^\infty (-1)^n\frac{x^{2n+1}}{(2n+1)!}$.
>>
>>$$
>>\sin(x) = x - \frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\cdots
>>$$
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>\sin x \qquad \sin (x)
>>>$$
>>>
>>
>

## Properties

>[!THEOREM]- Theorem: Parity of the Real Sine Function
>
>The [real sine function](Real%20Sine%20Function.md) is [](../Parity.md#^odd-function):
>
>$$
>\sin(-x) = - \sin(x)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Image of the Real Sine Function
>
>The [image](../../../Functions/Functions.md) of the [real sine function](Real%20Sine%20Function.md) is $[-1;1]$.
>
>$$
>\sin(\mathbb{R}) = [-1;1]
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Periodicity of the Real Sine Function
>
>The [real sine function](Real%20Sine%20Function.md) has a [period](../Periodicity.md) of $2\pi$. More generally,
>
>$$
>\sin (x + 2k\pi) = \sin(x) \qquad \forall k\in\mathbb{Z}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Antiperiodicity of the Real Sine Function
>
>The [real sine function](Real%20Sine%20Function.md) has an [antiperiod](../Periodicity.md) of $\pi$. More generally,
>
>$$
>\sin (x + (2k+1) \pi) = -\sin(x) \qquad k \in \mathbb{Z}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity of the Real Sine Function
>
>The [real sine function](Real%20Sine%20Function.md) is [continuous](../Continuity.md) on $\mathbb{R}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Derivative of the Real Sine Function
>
>The [derivative](../Differentiability.md) of the [real sine function](Real%20Sine%20Function.md) is the [real cosine function](Real%20Cosine%20Function.md).
>
>$$
>(\sin x)' = \cos x
>$$
>
>>[!PROOF]-
>>
>>$$
>>\begin{align*}(\sin x)'  &= \lim_{\Delta x\to 0} \frac{\sin (x + \Delta x) - \sin x}{\Delta x} = \lim_{\Delta x\to 0} \frac{2\sin\frac{\Delta x}{2}\cos\frac{2x + \Delta x}{2}}{\Delta x} \\ &= \lim_{\Delta x \to 0}\frac{\sin\frac{\Delta x}{2}}{\frac{\Delta x}{2}}\lim_{\Delta x \to 0} \cos\left(x + \frac{\Delta x}{2}\right) = 1 \cdot \cos x = \cos x\end{align*}
>>$$
>>
>