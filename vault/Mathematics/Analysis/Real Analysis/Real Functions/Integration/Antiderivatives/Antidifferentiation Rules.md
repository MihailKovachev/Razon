---
title: Antidifferentiation Rules
tags:
  - antiderivatives
  - real-functions
  - real-analysis
  - analysis
  - mathematics
---

>[!THEOREM]
>
>If $f$ and $g$ are [continuous](../../Continuity.md) on a closed interval $[a;b]$, then for all $\alpha, \beta \in \mathbb{R}$
>
>$$\int \alpha \, f(x) + \beta \, g(x) \mathop{\mathrm{d}x} = \alpha \int f(x) \mathop{\mathrm{d}x} + \beta \int g(x) \mathop{\mathrm{d}x}$$
>
>>[!PROOF]-
>>
>>Let $F(x)$ be an [antiderivative](Antiderivatives.md) $f(x)$ and $G(x)$ be an [antiderivative](Antiderivatives.md) of $g(x)$.
>> 
>>Let's examine the [derivative](../../Differentiation/index.md) of the right-hand side.
>> 
>>$$
>>\frac{\mathrm{d}}{\mathrm{d}x}\left(\lambda \int f(x) \mathop{\mathrm{d}x} + \mu \int g(x) \mathop{\mathrm{d}x}\right)
>>$$
>> 
>>Since [differentiation](../../../Real%20Functions/Differentiation/Differentiation%20Rules.md) is linear, we have
>> 
>>$$
>>\begin{align*}\frac{\mathrm{d}}{\mathrm{d}x}\left(\lambda \int f(x) \mathop{\mathrm{d}x} + \mu \int g(x) \mathop{\mathrm{d}x}\right) &= \lambda\frac{\mathrm{d}}{\mathrm{d}x}\int f(x) \mathop{\mathrm{d}x} + \mu \frac{\mathrm{d}}{\mathrm{d}x}\int g(x) \mathop{\mathrm{d}x} \\ &= \lambda\frac{\mathrm{d}}{\mathrm{d}x} F(x) + \mu\frac{\mathrm{d}}{\mathrm{d}x}G(x) \\ &= \lambda f(x) + \mu g(x)\end{align*}
>>$$
>> 
>>This means that $\lambda F(x) + \mu G(x)$ is an [antiderivative](Antiderivatives.md) of $\lambda \, f(x) + \mu \, g(x)$. All other [antiderivatives](Antiderivatives.md) of $\lambda \, f(x) + \mu \, g(x)$ can be expressed as $\lambda F(x) + \mu G(x) + C$ for some $C\in \mathbb{R}$.
>>
>

>[!THEOREM] Theorem: Integration by Parts
>
>If $u$ and $v$ are [continuously differentiable](../../Differentiation/index.md), then
>
>$$\int u(x) v'(x) \mathop{\mathrm{d}x} = u(x)v(x) + \int u'(x)v(x) \mathop{\mathrm{d}x}$$
>
>>[!PROOF]-
>>
>>TODO

>[!THEOREM] Theorem: Integration by Substitution
>
>$$
>\int f(\underset{u}{\underbrace{g(x)}})\underset{\mathop{\mathrm{d}u}}{\underbrace{g'(x) \mathop{\mathrm{d}x}}} = \int f(u) \mathop{\mathrm{d}u}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]
>
>$$
>\int \frac{f'(x)}{f(x)} \mathop{\mathrm{d}x} = \ln (f(x)) + C, \qquad f(x) \gt  0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>