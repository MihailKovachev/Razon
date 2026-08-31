---
tags:
    - probability-theory
    - mathematics
---

# Real Random Variable

>[!DEFINITION] Definition: Real Random Variable
>
>Let $(\Omega, \mathcal{F}, \Pr)$ be a [probability space](../Probability%20Space.md).
>
>A **real random variable** is a [real-valued function](../../Analysis/Real%20Analysis/Real-Valued%20Functions.md) $X: \Omega \to \mathbb{R}$ which is [measurable](../../Measure%20Theory/Measurable%20Functions.md) with respect to $\mathcal{F}$ and the [Borel σ-algebra](../../Measure%20Theory/Borel%20σ-Algebra.md) of the [real number line](../../Analysis/Real%20Analysis/Real%20Number%20Line.md).
>

>[!THEOREM] Theorem: Linear Combination of Random Variables is Random Variable
>
>Let $(\Omega, \mathcal{F}, \Pr)$ be a [probability space](../Probability%20Space.md).
>
>If $X: \Omega \to \mathbb{R}$ and $Y: \Omega \to \mathbb{R}$ are [real random variables](./Real%20Random%20Variable.md), then so is $\alpha X+\beta  Y: \Omega \to \mathbb{R}$ for all $\alpha, \beta \in \mathbb{R}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Product of Random Variables is Random Variable
>
>Let $(\Omega, \mathcal{F}, \Pr)$ be a [probability space](../Probability%20Space.md).
>
>If $X: \Omega \to \mathbb{R}$ and $Y: \Omega \to \mathbb{R}$ are [real random variables](./Real%20Random%20Variable.md), then so is $X\cdot Y: \Omega \to \mathbb{R}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Measurable Scalar Fields of Random Variables are Random Variables
>
>Let $(\Omega, \mathcal{F}, \Pr)$ be a [probability space](../Probability%20Space.md), let $X_1, \dotsc, X_n:\Omega \to \mathbb{R}$ be [real random variables](./Real%20Random%20Variable.md), let $X: \Omega \to \mathbb{R}^n$ be the [real random vector](./Real%20Random%20Vector.md) $X = \begin{bmatrix}X_1 & \cdots & X_n\end{bmatrix}^{\mathsf{T}}$ and let $f: \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../../Analysis/Real%20Analysis/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md).
>
>If $f$ is [measurable](../../Measure%20Theory/Measurable%20Functions.md) with respect to the [Borel σ-algebras](../../Measure%20Theory/Borel%20σ-Algebra.md) on the [Euclidean spaces](../../Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md) $\mathbb{R}^n$ and $\mathbb{R}$, then the [composition](../../Analysis/Functions/Composition%20(Functions).md) $f \circ X: \Omega \to \mathbb{R}$ is a [random variable](./Real%20Random%20Variable.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>