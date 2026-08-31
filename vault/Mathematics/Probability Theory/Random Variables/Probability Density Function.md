---
tags:
    - probability-theory
    - mathematics
---

# Probability Density Function

>[!DEFINITION] Definition: Probability Density Function
>
>Let $(\Omega, \mathcal{F}, \Pr)$ be a [probability space](../Probability%20Space.md) and let $X: \Omega \to \mathbb{R}$ be a [random variable](./Real%20Random%20Variable.md).
>
>A **probability density function** of $X$ is any [extended real-valued function](../../Analysis/Real%20Analysis/Extended%20Real-Valued%20Function.md) $f: \mathbb{R} \to [0,\infty]$ which is [measurable](../../Measure%20Theory/Measurable%20Functions.md) w.r.t. the [Borel σ-algebras](../../Measure%20Theory/Borel%20σ-Algebra.md) of the [real number line](../../Analysis/Real%20Analysis/Real%20Number%20Line.md) and $[0,\infty]$ such that for each [Borel set](../../Measure%20Theory/Borel%20σ-Algebra.md) $S \subseteq \mathbb{R}$, the [probability](../Probability%20Space.md) that $X$ is in $S$ is the [Lebesgue integral](../../Analysis/Real%20Analysis/Lebesgue%20Integral.md) of $f$ on $S$ w.r.t. the [Lebesgue measure](../../Measure%20Theory/Lebesgue%20Measure.md) on the [real number line](../../Analysis/Real%20Analysis/Real%20Number%20Line.md):
>
>$$\Pr(X \in S) = \int_S f \,\mathrm{d}\lambda$$
>