---
title: Vector Line Integrals
tags:
    - vector-analysis
    - real-analysis
    - analysis
    - mathematics
---

# Vector Line Integrals over Parametric Curves

>[!DEFINITION] Definition: Vector Line Integral
>
>Let $\mathbf{F}: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [real vector field](../Real%20Vector%20Field.md) and let $\gamma: [a;b] \to \mathbb{R}^n$ be a [differentiable](../../../Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) [parametric curve](../../../Real%20Vector%20Functions/Parametric%20Curves/Parametric%20Curve.md) whose [image](../../../../Functions/Functions.md) $\gamma([a;b])$ is a [subset](../../../../../Set%20Theory/Sets.md) of $\mathcal{D}$.
>
>The **(vector) line integral** of $\mathbf{F}$ over $\gamma$ is the [definite integral](../../../Real%20Functions/Integration/Definite%20Integrals.md) 
>
>$$
>\int_a^b \mathbf{F}(\gamma(t)) \cdot \gamma'(t) \mathop{\mathrm{d}t},
>$$
>
>where $\cdot$ denotes the [dot product](../../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Dot%20Product.md).
>
>>[!NOTATION]-
>>
>>$$
>>\int_{\gamma} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{s}} \qquad \int_{\gamma} \mathbf{F}
>>$$
>>
>>If the [image](../../../../Functions/Functions.md) of $\gamma$ is a [closed curve](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Closed%20Curves), then we write
>>
>>$$
>>\oint_{\gamma} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{s}} \qquad \oint_{\gamma} \mathbf{F}
>>$$
>>
>

## Properties

>[!THEOREM]- Theorem: Vector Line Integral to Scalar Line Integral
>
>Let $\mathbf{F}: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [real vector field](../Real%20Vector%20Field.md) and let $\gamma: [a;b] \to \mathbb{R}^n$ be a [differentiable](../../../Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) [parametric curve](../../../Real%20Vector%20Functions/Parametric%20Curves/Parametric%20Curve.md) whose [image](../../../../Functions/Functions.md) $\gamma([a;b])$ is a [subset](../../../../../Set%20Theory/Sets.md) of $\mathcal{D}$.
>
>The [line integral](Vector%20Line%20Integrals.md) of $\mathbf{F}$ over $\gamma$ is equal to the [line ntegral](../../../Real%20Vector%20Functions/Scalar%20Fields/Integration/Scalar%20Line%20Integrals.md) of the [dot product](../../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Dot%20Product.md) of $\mathbf{F}$ with the [unit tangent vector](../../../../../Geometry/Euclidean%20Geometry/Curves/Parametrization.md) of $\gamma$:
>
>$$
>\int_{\gamma} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{s}} = \int_{\gamma} \mathbf{F} \cdot \mathbf{T} \mathop{\mathrm{d}s}
>$$
>
>>[!PROOF]-
>>
>>$$
>>\begin{align*}
>>
>>\int_{\gamma}\mathbf{F}\cdot \mathop{\mathrm{d}\mathbf{s}} & =\int_a^b \mathbf{F}({\gamma}(t)) \cdot{\gamma}^{\prime}(t)dt \\
>>\int_{\gamma}\mathbf{F}\cdot \mathop{\mathrm{d}\mathbf{s}} & =\int_a^b\mathbf{F}({\gamma}(t))\cdot\frac{{\gamma}^{\prime}(t)}{\left\|{\gamma}^{\prime}(t)\right\|}\left\|{\gamma}^{\prime}(t)\right\|dt \\
>>& =\int_a^b\left(\mathbf{F}({\gamma}(t))\cdot\mathbf{T}(t)\right)\left\|{\gamma}^{\prime}(t)\right\| \mathop{\mathrm{d}t} \\
>>& =\int_{\gamma}(\mathbf{F}\cdot\mathbf{T}) \mathop{\mathrm{d}s}
>>
>>\end{align*}
>>$$
>>
>

>[!THEOREM]- Theorem: Linearity of the Vector Line Integral
>
>The [vector line integral](Vector%20Line%20Integrals.md) is [linear](../../../../../Algebra/Linear%20Algebra/Linear%20Transformations/Linear%20Transformation.md):
>
>$$
>\int_{\gamma} (\lambda\, \boldsymbol{v} +\mu \, \boldsymbol{w})\cdot\mathop{\mathrm{d}\boldsymbol{s}} = \lambda\int_{\gamma} \boldsymbol{v}\cdot\mathop{\mathrm{d}\boldsymbol{s}} + \mu \int_{\gamma} \boldsymbol{w}\cdot \mathop{\mathrm{d}\boldsymbol{s}}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Vector Line Integrals over Geometric Curves

>[!THEOREM] Theorem: Line Integrals over Equivalent Parametrizations
>
>Let $\mathcal{C}$ be a [simple curve](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Simple%20Curves) in $\mathbb{R}^n$, let $\gamma: [a;b] \to \mathbb{R}^n$ and $\varphi: [c;d] \to \mathbb{R}^n$ be [parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizations) of $\mathcal{C}$ and let $\mathbf{F}: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [real vector field](../Real%20Vector%20Field.md).
>
>If $\gamma$ and $\varphi$ are [continuously differentiable](../../Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) on $(a;b)$ and $(c;d)$, respectively, and are [equivalent](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Equivalence%20of%20Parametrizations) up to a [continuously differentiable](../../../Real%20Functions/Differentiability.md) [reparametrization](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md), then the [line integrals](Vector%20Line%20Integrals.md) of $\mathbf{F}$ along $\gamma$ and $\varphi$
>
>-  are equal whenever $\gamma$ and $\varphi$ have the [same orientation](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Orientation%20of%20Equivalent%20Parametrizations)
>
>$$
>\int_{\gamma} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{s}} = \int_{\varphi} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{s}}
>$$
>
>- are equal in magnitude but opposite in sign whenever $\gamma$ and $\varphi$ have [opposite orientations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Orientation%20of%20Equivalent%20Parametrizations)
>
>$$
>\int_{\gamma} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{s}} = -\int_{\varphi} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{s}}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

The aforementioned theorem guarantees that the [line integrals](Vector%20Line%20Integrals.md) of a [vector field](../Real%20Vector%20Field.md) $\mathbf{F}$ over [continuously differentiable](../../Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) [parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizations) of the same [curve](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md) $\mathcal{C}$ which are [equivalent](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Equivalence%20of%20Parametrizations) up to a [continuously differentiable](../../../Real%20Functions/Differentiability.md) [reparametrization](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md) are either equal or equal in magnitude but opposite in sign. However, while some [parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizations) may be [equivalent](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Equivalence%20of%20Parametrizations) amongst each other and some other [parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizations) may also be [equivalent](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Equivalence%20of%20Parametrizations) amongst each other, this does not ensure that these groups of [parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizations) are *all* [equivalent](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Equivalence%20of%20Parametrizations). If we want to define the notion of a line integral over a curve geometrically, we need to determine which equivalence class to consider. A very natural choice is based on the [equivalence of regular injective parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Equivalence%20of%20Parametrizations). Since these [parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizatoins) are [injective](../../../../Functions/Injections,%20Surjections%20and%20Bijections.md), the absolute value of the [line integrals](Vector%20Line%20Integrals.md) of $\mathbf{F}$ over them depend only on the [length](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md) of $\mathcal{C}$ and are thus equal. However, each of these [parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizations) still has one of two possible [orientations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Orientation%20of%20Equivalent%20Parametrizations). This leaves us with two options for defining the line integral of $\mathbf{F}$ over $\mathcal{C}$, none of which is objectively better. 

>[!DEFINITION] Definition: Vector Line Integrals over Curves
>
>Let $\mathbf{F}: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [real vector field](../Real%20Vector%20Field.md) and let $\mathcal{C} \subseteq \mathcal{D}$ be a [simple curve](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Simple%20Curves) in $\mathbb{R}^n$.
>
>The **line integral** of $\mathbf{F}$ over $\mathcal{C}$ is defined as a [line integral](Vector%20Line%20Integrals.md) of $\mathbf{F}$ over any [injective](../../../../Functions/Injections,%20Surjections%20and%20Bijections.md) [parametrization](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizations) $\gamma: [a;b] \subset \mathbb{R} \to \mathbb{R}^n$ of $\mathcal{C}$ which is [continuously differentiable](../../Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) on $(a;b)$ with a non-vanishing [derivative](../../Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md):
>
>$$
>\int_{\gamma} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{s}}
>$$
>
>>[!NOTATION]
>>
>>$$
>>\int_{\mathcal{C}} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{s}}
>>$$
>>
>
>>[!WARNING] Warning: Ambiguity of the Line Integral
>>
>>As explained above, the line integral is *not* uniquely defined. There are two possible values for it depending on the [orientation](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Orientation%20of%20Equivalent%20Parametrizations) of $\gamma$ - one positive and one negative. One should always beware which value is relevant to the context.
>>
>