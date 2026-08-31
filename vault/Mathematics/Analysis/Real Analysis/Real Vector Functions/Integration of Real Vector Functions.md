---
title: Integration of Real Vector Functions
tags:
    - real-analysis
    - vector-analysis
    - mathematical-analysis
    - mathematics
---

# Integrals

>[!DEFINITION] Definition: Integral of a Real Vector Function
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](./Real%20Vector%20Functions.md) with component functions $f_1,\dotsc,f_n$ and let $S \subseteq \mathbb{R}^m$.
>
>We say that $f$ is **integrable** on $S$ if $f_1,\dotsc,f_n$ are [integrable](../Real%20Scalar%20Fields/Integration/Integration%20of%20Real%20Scalar%20Fields.md#Definite%20Integrals) on $S$. In this case, we define the **integral** of $f$ over $S$ as the [real vector](../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md)
>
>$$
>\int_S f(\mathbf{x}) \mathop{\mathrm{d}^m\mathbf{x}} \overset{\text{def}}{=} \begin{bmatrix}\int_S f_1(\mathbf{x}) \mathop{\mathrm{d}^m\mathbf{x}} \\ \vdots \\ \int_S f_n(\mathbf{x}) \mathop{\mathrm{d}^m\mathbf{x}} \\ \end{bmatrix}
>$$
>