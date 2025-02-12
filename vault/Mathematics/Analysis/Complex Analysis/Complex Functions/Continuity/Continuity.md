---
title: Continuity of Complex Functions
tags:
    - continuity
    - complex-functions
    - complex-analysis
    - analysis
    - mathematics
---

# Continuity

>[!DEFINITION] Definition: Continuity of Complex Functions
>
>A [complex function](../index.md) $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ is **continuous at** $c \in \mathcal{D}$ iff its [limit](../Limits/Limits.md) for $z \to c$ is equal to its value there.
>
>$$
>\lim_{z \to c} f(z) = f(c)
>$$
>

## Discontinuities

>[!DEFINITION] Definition: Point of Discontinuity
>
>If a [complex function](../index.md) $f$ is *not* [continuous](Continuity.md) at $c \in \mathbb{C}$, then we call $c$ a **point of discontinuity**.
>

>[!DEFINITION] Definition: Removable Discontinuity
>
>Let $f$ be a [complex function](../index.md)
>
>A [point of discontinuity](Continuity.md#Discontinuities) $c \in \mathbb{C}$ is a **removable discontinuity** if the [limit](../Limits/Limits.md) $\lim_{z \to c} f(z)$ exists, but $f$ is not defined at $c$.
>

# Properties

>[!THEOREM]- Theorem: Continuity of the Real and Imaginary Parts
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](../index.md). 
>
>If $f$ is [continuous](Continuity.md) at $z_0 \in \mathbb{C}$, then its [real](../../Complex-Valued%20Functions.md) $\operatorname{Re} f$ and [imaginary](../../Complex-Valued%20Functions.md) part $\operatorname{Im} f$ are also [continuous](Continuity.md) there.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Continuity of Sum, Product and Division
>
>Let $f$ and $g$ be [complex functions](../index.md).
>
>If $f$ and $g$ are [continuous](Continuity.md) at $c \in \mathbb{C}$, then so are
>- $\lambda f + \mu g$ for all $\lambda, \mu \in \mathbb{C}$;
>- $fg$;
>- $f/g$, provided that $g(c) \ne 0$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM]- Theorem: Continuity of Composition
>
>Let $f$ and $g$ be [complex functions](../index.md).
>
>If $g$ is [continuous](Continuity.md) at $c \in \mathbb{C}$ and $f$ is [continuous](Continuity.md) at $g(c)$, then their [composition](../../../Functions/Composition.md) $f\circ g$ is also [continuous](Continuity.md) at $c$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Bibliography

1. N. H. Asmar, L. Grafakos, "Analytic Functions," in *Complex Analysis with Applications*, Columbia, MO, USA: Springer, 2018