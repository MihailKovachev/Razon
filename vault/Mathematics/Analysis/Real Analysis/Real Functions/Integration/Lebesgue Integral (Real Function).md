---
tags:
    - real-analysis
    - analysis
    - mathematics
---

# Lebesgue Integral (Real Functions)

>[!DEFINITION] Definition: Lebesgue Integral
>
>Let $(\mathbb{R}, \Sigma, \mu)$ be the [measure space](../../../../Measure%20Theory/Measure%20Spaces.md) formed using the [Lebesgue measure](../../Lebesgue%20Integral.md) on $\mathbb{R}$.
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [measurable](../../../../Measure%20Theory/Measurable%20Functions.md) [real function](../Real%20Functions.md) on a [Lebesgue-measurable](../../Lebesgue%20Integral.md) [subset](../../../../Set%20Theory/Sets.md#Subset) $\mathcal{D}$ and let $S \subseteq \mathbb{R}$ also be [Lebesgue-measurable](../../Lebesgue%20Integral.md).
>
>The **Lebesgue integral** of $f$ over $S$ is the [Lebesgue integral](../../Lebesgue%20Integral.md) of $f$ over $S$ with respect to the [Lebesgue measure](../../Lebesgue%20Integral.md) $\mu$:
>
>$$
>\int_S f \mathop{\mathrm{d}\mu}
>$$
>
>>[!DEFINITION] Definition: Lebesgue-Integrability
>>
>>We say that $f$ is **Lebesgue-integrable** on $S$ if its [Lebesgue integral](#Lebesgue%20Integrals) is finite.
>>
>

>[!THEOREM] Theorem: Riemann-Integrability $\implies$ Lebesgue-Integrability
>
>Let $f: I \subset \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Functions.md) on a [closed interval](../../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) $I = [a,b]$.
>
>If $f$ is [Riemann-integrable](#Riemann%20Integrals) on $I$, then $f$ is also [Lebesgue-integrable](#Riemann%20Integrals) on $I$ with
>
>$$
>\int_a^b f(x) \mathop{\mathrm{d}x} = \int_I f \mathop{\mathrm{d}\mu}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Equality of Lebesgue Integrals
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [measurable](../../../../Measure%20Theory/Measurable%20Functions.md) [real functions](../Real%20Functions.md) on [Lebesgue-measurable](../../Lebesgue%20Integral.md) [subsets](../../../../Set%20Theory/Sets.md#Subset) $\mathcal{D}_f$ and $\mathcal{D}_g$ and let $S \subseteq \mathbb{R}$ also be [Lebesgue-measurable](../../Lebesgue%20Integral.md).
>
>If $f$ and $g$ are non-negative on $S$ and the [set](../../../../Set%20Theory/Sets.md) $\{x \in S \mid f(x) \ne g(x)\}$ is a [subset](../../../../Set%20Theory/Sets.md) of a [null set](../../../../Measure%20Theory/Measure%20Spaces.md), then the [Lebesgue integrals](#Lebesgue%20Integrals) of $f$ and $g$ over $S$ are equal.
>
>$$
>\int_S f \mathop{\mathrm{d}\mu} = \int_S g \mathop{\mathrm{d}\mu}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Linearity of Lebesgue Integrals
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [measurable](../../../../Measure%20Theory/Measurable%20Functions.md) [real functions](../Real%20Functions.md) on [Lebesgue-measurable](../../Lebesgue%20Integral.md) [subsets](../../../../Set%20Theory/Sets.md#Subset) $\mathcal{D}_f$ and $\mathcal{D}_g$ and let $S \subseteq \mathbb{R}$ also be [Lebesgue-measurable](../../Lebesgue%20Integral.md).
>
>If $f$ and $g$ are [Lebesgue-integrable](./Riemann%20Integrals%20(Real%20Functions).md) on $S$, then so is the [function](../Real%20Functions.md) $\alpha f + \beta g$ for all $\alpha, \beta \in \mathbb{R}$. Furthermore,
>
>$$
>\int_S \alpha f + \beta g \mathop{\mathrm{d}\mu} = \alpha \int_S f \mathop{\mathrm{d}\mu} + \beta \int_S g \mathop{\mathrm{d}\mu}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>