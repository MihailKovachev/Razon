---
tags:
  - real-analysis
  - analysis
  - mathematics
---

# Real Sine Function

>[!THEOREM] Theorem: Convergence of the Sine Power Series
>
>The [real power series](../../Real%20Power%20Series.md) $\displaystyle \sum_{n=0}^\infty (-1)^n\frac{x^{2n+1}}{(2n+1)!}$ is [convergent](../../Real%20Power%20Series.md#Convergence) for all $x \in \mathbb{R}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Real Sine Function
>>
>>The **real sine function** is the [real analytic function](../Real%20Analytic%20Functions.md) $\sin: \mathbb{R} \to \mathbb{R}$ defined by the [real power series](../../Real%20Power%20Series.md) $\displaystyle \sum_{n=0}^\infty (-1)^n\frac{x^{2n+1}}{(2n+1)!}$.
>>
>>$$\sin(x) = x - \frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\cdots$$
>>
>>>[!NOTATION]
>>>
>>>$$\sin x \qquad \sin (x)$$
>>>
>>
>

>[!THEOREM] Theorem: Parity of the Real Sine Function
>
>The [real sine function](#The%20Real%20Sine%20Function) is [odd](../Parity.md):
>
>$$\sin(-x) = - \sin(x)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Image of the Real Sine Function
>
>The [image](../../../Functions/Functions.md) of the [real sine function](#The%20Real%20Sine%20Function) is $[-1;1]$.
>
>$$\sin(\mathbb{R}) = [-1;1]$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Periodicity of the Real Sine Function
>
>The [real sine function](#The%20Real%20Sine%20Function) has a [period](../Periodicity.md) of $2\pi$. More generally,
>
>$$\sin (x + 2k\pi) = \sin(x) \qquad \forall k\in\mathbb{Z}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antiperiodicity of the Real Sine Function
>
>The [real sine function](#The%20Real%20Sine%20Function) has an [antiperiod](../Periodicity.md) of $\pi$. More generally,
>
>$$\sin (x + (2k+1) \pi) = -\sin(x) \qquad k \in \mathbb{Z}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity of the Real Sine Function
>
>The [real sine function](#The%20Real%20Sine%20Function) is [continuous](../Continuity%20(Real%20Functions).md) on $\mathbb{R}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Derivative of the Real Sine Function
>
>The [derivative](../Differentiability%20(Real%20Functions).md) of the [real sine function](#The%20Real%20Sine%20Function) is the [real cosine function](#The%20Real%20Cosine%20Function).
>
>$$(\sin x)' = \cos x$$
>
>>[!PROOF]-
>>
>>$$\begin{aligned}(\sin x)'  &= \lim_{\Delta x\to 0} \frac{\sin (x + \Delta x) - \sin x}{\Delta x} = \lim_{\Delta x\to 0} \frac{2\sin\frac{\Delta x}{2}\cos\frac{2x + \Delta x}{2}}{\Delta x} \\ &= \lim_{\Delta x \to 0}\frac{\sin\frac{\Delta x}{2}}{\frac{\Delta x}{2}}\lim_{\Delta x \to 0} \cos\left(x + \frac{\Delta x}{2}\right) = 1 \cdot \cos x = \cos x\end{aligned}$$
>>
>

>[!THEOREM] Theorem: Sine in Bachmann-Landau Notation
>
>The [real sine function](#The%20Real%20Sine%20Function) $\sin x$ can be expressed in [Bachmann-Landau notation](../../Asymptotic%20Analysis/Bachmann-Landau%20Notation.md) for $x \to 0$ as follows:
>
>$$\sin x = \sum_{k=0}^m (-1)^k \frac{x^{2k+1}}{(2k+1)!} + O(x^{2m+3}) \qquad \text{for} \qquad x \to 0$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Limits of Sine Variations
>
>Following are the [limits](../Limits%20(Real%20Functions.md) of some variations of [real sine function](#The%20Real%20Sine%20Function):
>
>$$\lim_{x \to 0} \frac{\sin (\alpha x)}{x} = \alpha \qquad \forall \alpha \in \mathbb{R}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>