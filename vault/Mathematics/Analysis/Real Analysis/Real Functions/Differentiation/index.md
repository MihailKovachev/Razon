---
title: Differentiability of Real Functions
tags:
  - differentiability
  - real-functions
  - real-analysis
  - analysis
  - mathematics
---

# The Derivative

>[!DEFINITION] Definition: Derivative of a Real Function
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../index.md).
>
>The **derivative of** $f$ **in** $x_0 \in D$ is the [limit](../Limits/index.md)
>
>$$
>\lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}
>$$
>
>More generally, the derivative of $f$ is the [function](../index.md) which maps every $x \in D$ to $f'(x)$.
>
>>[!NOTATION]-
>>
>>$$
>>f'(x_0) \qquad \frac{\mathrm{d}f}{\mathrm{d}x} (x_0) \qquad \frac{\mathrm{d}}{\mathrm{d}x}f(x_0)
>>$$
>
>>[!DEFINITION] Definition: Higher-Order Derivatives
>>
>>The $k$**-th order derivative** of $f$ is the derivative of the $(k-1)$-th order derivative of $f$:
>> - The $0$**-th order derivative of** $f$ is just $f$ itself;
>> - The **first order derivative of** $f$ is just the aforementioned derivative $f'$;
>> - The **second order derivative of** $f$ is the derivative of $f'$, etc.
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>f' \qquad f'' \qquad f''' \qquad f^{\mathrm{IV}} \qquad f^{\mathrm{V}} \qquad \cdots \qquad f^{(n)}
>>>$$
>>>
>>>$$
>>>\frac{\mathrm{d}f}{\mathrm{d}x} \qquad \frac{\mathrm{d}^2 f}{\mathrm{d}x^2} \qquad \frac{\mathrm{d}^3 f}{\mathrm{d}x^3} \qquad \frac{\mathrm{d}^4 f}{\mathrm{d}x^4} \qquad  \frac{\mathrm{d}^5 f}{\mathrm{d}x^5} \qquad \cdots \qquad \frac{\mathrm{d}^n f}{\mathrm{d}x^n}
>>>$$
>>>
>>
>

>[!DEFINITION] Definition: Differentiability
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../index.md).
>
>We say that $f$ is **differentiable at** some $x \in D$ if the first-order derivative of $f$ in $x$ exists.
>
>We say that $f$ is $k$**-times (continuously) differentiable on** $D$ if its $k$-th derivative exists (and is [continuous](../Continuity.md)).

# Properties

>[!THEOREM] Theorem: Differentiability $\implies$ Continuity
>
>If $f: D \subseteq \mathbb{R} \in \mathbb{R}$ is [differentiable](./index.md) at $x_0 \in D$, then $f$ is also [continuous](../Continuity.md) at $x_0$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Mean Value Theorem for Derivatives
>
>If $f: D \to \mathbb{R}$ is [continuous](../Continuity.md) on the [closed interval](../../../../Set%20Theory/Ordering/Intervals.md) $D = [a;b] \subset \mathbb{R}$ and [differentiable](./index.md) on the [open interval](../../../../Set%20Theory/Ordering/Intervals.md) $(a;b)$, then there exists at least one $x_0 \in (a;b)$ such that
>
>$$
>f'(x_0) = \frac{f(b) - f(a)}{b - a}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!INTUITION]- Intuition: Geometric Meaning
>>
>>The theorem says that there is at least one point $(x_0; f(x_0))$ on the graph of $f$, where the tangent line to $f$ is parallel to the secant line through the points $(a; f(a))$ and $(b; f(b))$.
>>
>>TODO
>>


>[!THEOREM] Theorem: Darboux's Theorem
>
>Let $f: D \to \mathbb{R}$ be a [differentiable](./index.md) [real function](../index.md) on a [closed interval](../../../../Set%20Theory/Ordering/Intervals.md) $D = [a;b] \subset \mathbb{R}$.
>
>For each $\lambda \in \mathbb{R}$ such that $f'(a) \lt \lambda \lt f'(b)$ or $f'(a) \gt \lambda \gt f'(b)$, there exists some $c \in [a;b]$ such that
>
>$$
>f'(c) = \lambda
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>