---
title: Definite Integrals of Vector Fields
tags:
    - vector-analysis
    - real-analysis
    - analysis
    - mathematics
---

# Integrals over Curves

>[!DEFINITION] Definition: Integrals over Parametric Curves
>
>Let $\mathbf{F}: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [real vector field](../Real%20Vector%20Field.md) with [component functions](../../Real%20Vector%20Function.md) $f_1, \dotsc, f_n$ and let $\gamma: [a;b] \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [parametric curve](../../Parametric%20Curves/Parametric%20Curve.md) with such that $\gamma([a;b]) \subseteq \mathcal{D}$.
>
>The **integral** of $\mathbf{F}$ over $\gamma$ is defined as the [vector](../../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Vector.md) whose components are the [line integrals](../../Scalar%20Fields/Integration/Scalar%20Line%20Integrals.md) of $f_1, \dotsc, f_n$ over $\gamma$:
>
>$$
>\int_{\gamma} \mathbf{F} \overset{\text{def}}{=} \begin{bmatrix} \int_{\gamma} f_1 \\ \vdots \\ \int_{\gamma} f_n \end{bmatrix}
>$$
>

It is also possible to define an integral of a [real vector field](../Real%20Vector%20Field.md) over a [curve](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md) which depends only on its geometry and on the way it is traversed by a particular [parametrization](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizations) using the following theorem.

>[!THEOREM] Theorem: Integrals over Equivalent Parametrizations
>
>Let $\mathbf{F}: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [real vector field](../Real%20Vector%20Field.md), let $\mathcal{C} \subseteq \mathcal{D}$ be a [curve](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md) in $\mathbb{R}^n$ and let $\gamma: [a;b] \subseteq \mathbb{R} \to \mathbb{R}^n$ and $\varphi: [c;d] \subseteq \mathbb{R} \to \mathbb{R}^n$ be [parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizations) of $\mathcal{C}$.
>
>If $\gamma$ and $\varphi$ are [continuously differentiable](../../Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) on $(a;b)$ and $(c;d)$, respectively, and are [equivalent](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Equivalence%20of%20Parametrizations) up to a [continuously differentiable](../../../Real%20Functions/Differentiation/Derivatives.md) [reparametrization](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md), then the [integrals](Definite%20Integrals.md#Integrals%20over%20Curves) of $\mathbf{F}$ over $\gamma$ and $\varphi$ are equal:
>
>$$
>\int_{\gamma} \mathbf{F} = \int_{\varphi} \mathbf{F}
>$$
>
>>[!PROOF]-
>>
>>This is guaranteed by applying the corresponding theorem for [scalar line integrals](../../Scalar%20Fields/Integration/Scalar%20Line%20Integrals.md#Scalar%20Line%20Integrals%20over%20Geometric%20Curves) for each of the component functions.
>>
>

The aforementioned theorem guarantees that the [integrals](Definite%20Integrals.md#Integrals%20over%20Curves) of a [vector field](../Real%20Vector%20Field.md) $\mathbf{F}$ over [continuously differentiable](../../Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) [parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizations) of the same [curve](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md) $\mathcal{C}$ which are [equivalent](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Equivalence%20of%20Parametrizations) up to a [continuously differentiable](../../../Real%20Functions/Differentiation/Derivatives.md) [reparametrization](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md) are equal. However, while some [parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizations) may be [equivalent](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Equivalence%20of%20Parametrizations) amongst each other and some other [parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizations) may also be [equivalent](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Equivalence%20of%20Parametrizations) amongst each other, this does not ensure that these groups of [parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizations) are *all* [equivalent](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Equivalence%20of%20Parametrizations). If we want to define the notion of an integral over a curve geometrically, we need to determine which equivalence class to consider. A very natural choice is based on the [equivalence of regular injective parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Equivalence%20of%20Parametrizations). According to the above theorem, the [integrals](Definite%20Integrals.md#Integrals%20over%20Curves) of $\mathbf{F}$ over these [parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizatoins) are all equal and, since they are also [injective](../../../../Functions/Types%20of%20Functions/Injection.md), this value depends only on the [length](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Length) of $\mathcal{C}$. 

>[!DEFINITION] Definition: Vector Field Integrals over Curves
>
>The **integral** of a [real vector field](../Real%20Vector%20Field.md) $\mathbf{F}$ over a [curve](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md) $\mathcal{C}$ is defined as the [integral](Definite%20Integrals.md#Integrals%20over%20Curves) of $\mathbf{F}$ over any [continuously differentiable](../../Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) [parametrization](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizations) $\gamma$ of $\mathcal{C}$ with a non-vanishing [derivative](../../Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md)
>
>$$
>\int_{\gamma} \mathbf{F}
>$$
>
>>[!NOTATION]
>>
>>$$
>>\int_{\mathcal{C}} \mathbf{F}
>>$$
>>
>

>[!WARNING] Warning: Integrals over Curves vs Vector Line Integrals
>
>[Integrals over curves](Definite%20Integrals.md#Integrals%20over%20Curves) should not be confused with [vector line integrals](Vector%20Line%20Integrals.md). At the very least, the former yields a vector, while the latter yields a number. So, remember that the distinction between "integral over a curve" and "line integral" is crucial.
>

# Integrals over Surfaces

TODO

# Integrals over Volumes

TODO

# Higher-Dimensional Integrals

TODO

# Bibliography