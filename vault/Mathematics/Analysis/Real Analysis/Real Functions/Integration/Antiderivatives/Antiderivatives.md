---
title: Antiderivatives of Real Functions
tags:
  - antiderivatives
  - real-functions
  - real-analysis
  - analysis
  - mathematics
---

# Antiderivatives

>[!DEFINITION] Definition: Antiderivative
>
>An **antiderivative** of the [real function](../../Real%20Functions.md) $f: D \subseteq \mathbb{R} \to \mathbb{R}$ is any [differentiable](../../Differentiation/Derivatives.md) [function](../../Real%20Functions.md) $F: D \subseteq \mathbb{R} \to \mathbb{R}$ whose [derivative](../../Differentiation/Derivatives.md) is $f$.
>
>$$
>F'(x) = f(x)
>$$
>
>>[!THEOREM] Theorem: Family of Antiderivatives
>>
>>Let $F$ be an [antiderivative](Antiderivatives.md) of $f$.
>>
>>Any other [differentiable](../../Differentiation/Derivatives.md) [function](../../Real%20Functions.md) $\mathcal{F}: D \subseteq \mathbb{R} \to \mathbb{R}$ is also an [antiderivative](Antiderivatives.md) of $f$ if and only if there is some constant $C \in \mathbb{R}$ such that
>>
>>$$\mathcal{F}(x) = F(x) + C \qquad \forall x \in D$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

## Indefinite Integrals

>[!DEFINITION] Definition: Indefinite Integral
>
>The **indefinite integral** of a [real function](../../Real%20Functions.md) $f$ is the [set](../../../../../Set%20Theory/Sets.md) of all [antiderivatives](Antiderivatives.md) of $f$.
>
>$$
>\int f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \{F \mid F' = f\}
>$$
>
>>[!NOTATION]-
>>
>>The notation $\int f(x) \mathop{\mathrm{d}x}$ is often used to denote a particular [antiderivative](Antiderivatives.md) of $f$ or simply the process of [integration](Integration.md), as well.
>>
>>Since [antiderivatives](Antiderivatives.md) are unique up to a constant, if we know a particular [antiderivative](Antiderivatives.md) $F$ of $f$, we write 
>>
>>$$
>>\int f(x) \mathop{\mathrm{d}x} = F(x) + C
>>$$
>>
>>for the indefinite integral.
>>
>
