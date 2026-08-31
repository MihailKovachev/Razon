---
tags:
    - complex-analysis
    - analysis
    - mathematics
---

# Continuity (Complex Functions)

>[!DEFINITION] Definition: Continuity of Complex Functions
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](./Complex%20Functions.md).
>
>A [complex function](./Complex%20Functions.md) $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ is [continuous](../../Continuity/Continuity.md) at $c \in \mathcal{D}$ if and only if its [limit](./Limits%20(Complex%20Functions.md) for $z \to c$ is equal to its value there.
>
>$$
>\lim_{z \to c} f(z) = f(c)
>$$
>
>We say that $f$ is **continuous on** $S\subseteq \mathcal{D}$ if it is [continuous](./Continuity%20(Complex%20Functions).md) at each $z \in S$. Moreover, if $S = \mathcal{D}$, we just say that $f$ is **continuous**.
>

>[!THEOREM] Theorem: Continuity of the Real and Imaginary Parts
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](./Complex%20Functions.md).
>
>If $f$ is [continuous](./Continuity%20(Complex%20Functions).md) at $c \in \mathbb{C}$, then its [real part](../Complex-Valued%20Functions.md) $\operatorname{Re} f$ and [real part](../Complex-Valued%20Functions.md) $\operatorname{Re} f$ part $\operatorname{Im} f$ are also [continuous](./Continuity%20(Complex%20Functions).md) at $c$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity of Sum, Product and Division
>
>Let $f$ and $g$ be [complex function](./Complex%20Functions.md).
>
>If $f$ and $g$ are [continuous](./Continuity%20(Complex%20Functions).md) at $c \in \mathbb{C}$, then so are
>- $\lambda f + \mu g$ for all $\lambda, \mu \in \mathbb{C}$;
>- $fg$;
>- $f/g$, provided that $g(c) \ne 0$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity of Composition
>
>Let $f$ and $g$ be [complex function](./Complex%20Functions.md).
>
>If $g$ is [continuous](./Continuity%20(Complex%20Functions).md) at $c \in \mathbb{C}$ and $f$ is [continuous](./Continuity%20(Complex%20Functions).md) at $g(c)$, then their [composition](../../Functions/Functions.md) $f\circ g$ is also [continuous](./Continuity%20(Complex%20Functions).md) at $c$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Bibliography

1. N. H. Asmar, L. Grafakos, "Analytic Functions," in *Complex Analysis with Applications*, Columbia, MO, USA: Springer, 2018