---
title: Definite Integrals
tags:
  - integration
  - real-functions
  - real-analysis
  - analysis
  - mathematics
---

# Riemann-Sums

>[!DEFINITION] Definition: Riemann Sum
>
>Let $f: D \to \mathbb{R}$ be a [real function](../../Real%20Functions.md) on a [closed interval](../../../../../Set%20Theory/Ordering/Intervals.md) $D = [a;b] \subset \mathbb{R}$ and let $x_0 \lt x_1 \lt \cdots \lt x_n \in D$.
>
>A **Riemann sum** of $f$ over $D$ is any sum of the form
>
>$$
>\sum_{i = 1}^n f(x_i^\ast) \Delta x_i,
>$$
>
>where $\Delta x_i = (x_i - x_{i-1})$ and $x_i^\ast \in [x_{i-1};x_i]$.
>
>>[!NOTE] Note: Choice of $x_i^\ast$
>>
>>Different choices for $x_i^\ast$ yield different Riemann sums.
>
>>[!DEFINITION]- Definition: Left Riemann Sum
>>
>>A **left Riemann sum** has $x_i^\ast = x_{i-1}$ for all $i$.
>>
>
>>[!DEFINITION]- Definition: Right Riemann Sum
>>
>>A **right Riemann sum** has $x_i^\ast = x_{i}$ for all $i$.
>>
>
>>[!DEFINITION]- Definition: Left Riemann Sum
>>
>>A **middle Riemann sum** has $\displaystyle x_i^\ast = \frac{x_{i-1} + x_i}{2}$ for all $i$.
>>
>

# Definite Integrals

>[!DEFINITION] Definition: Riemann-Integrability
>
>A [real function](../../Real%20Functions.md) $f: [a;b] \to \mathbb{R}$ is **Riemann-integrable** iff all of its [Riemann sums](./index.md) have the same [limit](../../Limits/index.md) as $\Delta x_i$ approaches $0$.
>
>$$
>\lim_{\Delta x_i\to 0}\sum_{i=1}^n f(x_i^\ast)\Delta x_i = S \in \mathbb{R}
>$$
>
>>[!DEFINITION] Definition: Definite Integral
>>
>>If the aforementioned [limit](../../Limits/index.md) exists, then we call it the **definite integral** of $f$ over $[a;b]$.
>>
>>>[!NOTATION]-
>>>
>>>The most common notation for the definite integral is
>>>
>>>$$
>>>\int_a^b f(x) \mathop{\mathrm{d}x}
>>>$$
>>>
>>>The upside of this notation is that it clearly shows where the integrand, i.e. the thing being integrated, begins and where it ends. This is not very useful when we are referring to $f$ by its name, but it helps to remove ambiguity when we substitute $f$ with an expression such as $\displaystyle \int_a^b x^3 + \ln x \mathop{\mathrm{d}x}$.
>>>
>>>Its main downside is that it forces us to assign a symbol to the function's argument which is redundant and can even be confusing in some contexts where we refer to $f$ by its name. In particular, it is irrelevant whether we write $\displaystyle \int_a^b f(x) \mathop{\mathrm{d}x}$ or $\displaystyle \int_a^b f(y) \mathop{\mathrm{d}y}$ or $\displaystyle \int_a^b f(\omega) \mathop{\mathrm{d}\omega}$, hence we can shorten the notation to just
>>>
>>>$$
>>>\qquad \int_a^b f
>>>$$
>>>
>>>The main downside of this notation is that it implies that the order of $a$ and $b$ matters, which is not the case - what matters is the actual [set](../../../../../Set%20Theory/Sets.md) which $[a;b]$ represents. To emphasise this, we can use the following notations:
>>>
>>>$$
>>>\int_{[a;b]} f \qquad \int_D f
>>>$$
>>>
>>>In the latter case, we can also add $\mathrm{d}D$ to clarify where the integrand begins and ends, such as
>>>
>>>$$
>>>\int_D f \mathop{\mathrm{d}D}
>>>$$
>>>
>>>All of these notations are useful in specific contexts and less so in others.
>>>
>>
>>>[!NOTATION]- Notation: Definite Integrals with Special Bounds
>>>
>>>A common convention is to define the notations
>>>
>>>$$
>>>\int_b^a f = -\int_a^b f
>>>$$
>>>
>>>and
>>>
>>>$$
>>>\int_c^c f = 0
>>>$$
>>>
>>>for each $c \in [a;b]$. This is merely notation which makes the formulation of many theorems easier and more natural.
>>>
>>
>

## Properties

>[!THEOREM] Theorem: Linearity of the Definite Integral
>
>The [definite integral](./index.md) is linear - if $f,g: [a;b] \to \mathbb{R}$ are [Riemann-integrable](./index.md), then for all $\alpha,\beta \in \mathbb{R}$
>
>$$
>\int_a^b \alpha \, f(x) + \beta\, g(x) \mathop{\mathrm{d}x} = \alpha \int_a^b f(x) \mathop{\mathrm{d}x} + \beta \int_a^b g(x) \mathop{\mathrm{d}x}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Interval Separation
>
>If $f: [a;b] \to \mathbb{R}$ is [Riemann-integrable](./index.md), then for each $c \in [a;b]$ its [definite integral](./index.md) can be broken down as the sum of the [definite integrals](./index.md) of its [restrictions](../../../../Functions/Restriction.md) on $[a;c]$ and $[c;b]$.
>
>$$
>\int_a^b f = \int_a^c f + \int_c^b f
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Integration by Parts
>
>Let $f,g: D \to \mathbb{R}$ be [real functions](../../Real%20Functions.md) on a [closed interval](../../../../../Set%20Theory/Ordering/Intervals.md) $D = [a;b] \subset \mathbb{R}$.
>
>
>If $f$ and $g$ are [continuously differentiable](../../Differentiation/Derivatives.md), then the [definite integral](./index.md) obeys
>
>$$
>\int_a^b f(x) g'(x) \mathop{\mathrm{d}x} = f(b)g(b) - f(a)g(a) - \int_a^b f'(x)g(x) \mathop{\mathrm{d}x}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Substitution
>
>Let $g: [a;b] \to \mathbb{R}$ and $f: [c;d] \to \mathbb{R}$ be [real functions](../../Real%20Functions.md) such that the [image](../../../../Functions/index.md) of $g$ is a [subset](../../../../../Set%20Theory/Sets.md) of $[c;d]$, i.e. $g([a;b]) \subseteq [c;d]$.
>
>If $f$ is [continuous](../../Continuity.md) and $g$ is [continuously differentiable](../../Differentiation/Derivatives.md), then the following [definite Integral](./index.md) can be solved via substitution.
>
>$$
>\int_a^b f(g(x))g'(x) \mathop{\mathrm{d}x} = \int_{g(a)}^{g(b)} f(u) \mathop{\mathrm{d}u}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Mean Value Theorem for Definite Integrals
>
>Let $f,g: D \to \mathbb{R}$ be [real functions](../../Real%20Functions.md) on a [closed interval](../../../../../Set%20Theory/Ordering/Intervals.md) $D = [a;b] \subset \mathbb{R}$.
>
>If $f$ and $g$ are [continuous](../../Continuity.md) and $g(x) \gt 0$ for all $x\in D$, then there exists some $\xi \in (a;b)$ such that
>
>$$
>\int_a^b f(x)g(x) \mathop{\mathrm{d}x} = f(\xi)\int_a^b g(x) \mathop{\mathrm{d}x}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!TIP]- Tip: $g(x) = 1$
>>
>>In the case of $g(x) = 1$ for all $x$, the mean value theorem simplifies to
>>
>>$$
>>\int_a^b f(x) \mathop{\mathrm{d}x} = f(\xi)(b - a)
>>$$
>>

>[!THEOREM] Theorem: Integrability of the Absolute Value
>
>If $f$ is [Riemann-integrable](./index.md) on a closed interval $[a;b]$, then so is its absolute value $|f|$ with the following inequality:
>
>$$\left|\int_a^b f(x) \mathop{\mathrm{d}x} \right| \le \int_a^b |f(x)| \mathop{\mathrm{d}x}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>