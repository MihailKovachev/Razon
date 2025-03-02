---
title: Line Integrals of Scalar Fields
---

# Scalar Line Integrals over Parametric Curves

>[!DEFINITION] Definition: Line Integral of a Scalar Field
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) and let $\gamma: [a;b] \to \mathbb{R}^n$ be a [parametric curve](../../../Real%20Vector%20Functions/Parametric%20Curves/Parametric%20Curve.md) which is [continuously differentiable](../../../Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) on $(a;b)$ and whose [image](../../../../Functions/Functions.md) $\gamma([a;b])$ is a [subset](../../../../../Set%20Theory/Sets.md) of $\mathcal{D}$.
>
>The **line integral** of $f$ along $\gamma$ is the [integral](../../../Real%20Functions/Integration/Definite%20Integrals.md)
>
>$$
>\int_a^b f(\gamma(t))\, ||\dot{\gamma}(t)|| \mathop{\mathrm{d}t}
>$$
>
>>[!NOTATION]
>>
>>$$
>>\int_{\gamma} f \qquad \int_{\gamma} f \mathop{\mathrm{d}s}
>>$$
>>
>>If the [image](../../../../Functions/Functions.md) of $\gamma$ is a [closed curve](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md), we write
>>
>>$$
>>\oint_{\gamma} f \qquad \oint_{\gamma} f \mathop{\mathrm{d}s}
>>$$
>>
>

## Properties

>[!THEOREM]- Theorem: Linearity of the Scalar Line Integral
>
>The [scalar line integral](Scalar%20Line%20Integrals.md) is [linear](../../../../../Algebra/Linear%20Algebra/Linear%20Transformations/Linear%20Transformation.md):
>
>$$
>\int_{\gamma} (\lambda\, f +\mu \, g)\mathop{\mathrm{d}s} = \lambda\int_{\gamma} f\mathop{\mathrm{d}s} + \mu \int_{\gamma} g\mathop{\mathrm{d}s}
>$$
>
>>[!PROOF]-
>>
>>$$
>>\begin{align*}\int_\gamma (\lambda\, f +\mu \, g)\mathop{\mathrm{d}s} &=\int_a^b [\lambda\, f(\gamma(t)) +\mu \, g(\gamma(t))]\,||\dot{\gamma}(t)||\mathop{\mathrm{d}t} \\ &=\int_a^b \lambda\, f(\gamma(t))\,||\dot{\gamma}(t)|| +\mu \, g(\gamma(t))\,||\dot{\gamma}(t)||\mathop{\mathrm{d}t} \\ &= \lambda \int_a^b f(\gamma(t)) \, ||\dot{\gamma}(t)|| \mathop{\mathrm{d}t} + \mu \int_a^b g(\gamma(t))\,||\dot{\gamma}(t)||\mathop{\mathrm{d}t} \\ &= \lambda\int_\gamma f\mathop{\mathrm{d}s} + \mu \int_\gamma g\mathop{\mathrm{d}s} \end{align*}
>>$$
>>
>

>[!THEOREM]- Mean value theorem for Scalar Line Integrals
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) and let $\gamma: [a;b] \to \mathbb{R}^n$ be a [continuously differentiable](../../../Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) [parametric curve](../../../Real%20Vector%20Functions/Parametric%20Curves/Parametric%20Curve.md) whose [image](../../../../Functions/Functions.md) $\gamma([a;b])$ is a [subset](../../../../../Set%20Theory/Sets.md) of $\mathcal{D}$.
>
>If $f$ is [continuous](../Continuity%20of%20Real%20Scalar%20Fields.md), then there exists some $\mathbf{p} \in \gamma([a;b])$ such that the [line integral](Scalar%20Line%20Integrals.md) of $f$ along $\gamma$ is
>
>$$
>\int_{\gamma} f = f(\mathbf{p})\cdot L,
>$$
>
>where $L$ is the [length](../../../Real%20Vector%20Functions/Parametric%20Curves/Length.md) of $\gamma$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Scalar Line Integrals over Geometric Curves

The following theorem makes it possible to provide an unambiguous definition of the line integral of a scalar field over a [curve](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md) in $\mathbb{R}^n$.

>[!THEOREM] Theorem: Line Integrals over Equivalent Parametrizations
>
>Let $\mathcal{C}$ be a [simple curve](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Simple%20Curves) in $\mathbb{R}^n$, let $\gamma: [a;b] \to \mathbb{R}^n$ and $\varphi: [c;d] \to \mathbb{R}^n$ be [parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizations) of $\mathcal{C}$ and let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md).
>
>If $\gamma$ and $\varphi$ are [continuously differentiable](../../Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) on $(a;b)$ and $(c;d)$, respectively, and are [equivalent](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Equivalence%20of%20Parametrizations) up to a [continuously differentiable](../../../Real%20Functions/Differentiation/Derivatives.md) [reparametrization](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md), then the [line integrals](Scalar%20Line%20Integrals.md) of $f$ along $\gamma$ and $\varphi$ are equal.
>
>$$
>\int_{\gamma} f = \int_{\varphi} f
>$$
>
>>[!PROOF]-
>>
>>We will just show this for the case when $\gamma$ and $\varphi$ are *not* piecewise, since the proof is easily generalizable - if $\gamma$ and $\varphi$ *are* piecewise, then one can just apply the following proof to each of their partitions and obtain the same end result after summing the results from each partition.
>>
>>Since $\gamma$ and $\varphi$ parameterise the same curve $\mathcal{C}$, we can [reparameterise](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md) one in the other. More specifically, there exists a [bijection](../../../../Functions/Types%20of%20Functions/Bijection.md), [continuously differentiable function](../../../Real%20Functions/Differentiation/Derivatives.md) $u: [a;b] \to [c;d]$ such that
>>
>>$$
>>\varphi(u(t)) = \gamma (t)
>>$$
>>
>>The [](../../../Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiation%20Rules%20for%20Curve%20Parameterisations.md#^chainrule) then gives us
>>
>>$$
>>\int_a^b f(\gamma(t))\, ||\dot\gamma (t)||\mathop{\mathrm{d}t} = \int_a^b f(\varphi(u(t)))\, ||\dot\varphi (u(t)) u'(t)|| \mathop{\mathrm{d}t} =  \int_a^b f(\varphi(u(t)))\, ||\dot\varphi (u(t))|| \, |u'(t)|\mathop{\mathrm{d}t}
>>$$
>>
>>If $\gamma$ and $\varphi$ have the [](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#^orientation), then $u(a) = c$ and $u(b) = d$. Since $a \lt b, c \lt d$ and $u$ is bijective, $u$ must be [strictly increasing](../../../Real%20Functions/Monotony.md), i.e. $|u'(t)| = u'(t)$. We thus have
>>
>>$$
>>\int_a^b f(\varphi(u(t)))\, ||\dot\varphi (u(t))|| \, |u'(t)|\mathop{\mathrm{d}t} = \int_a^b f(\varphi(u(t))) \, ||\dot\varphi (u(t))|| \, u'(t)\mathop{\mathrm{d}t}
>>$$
>>
>>By applying the [substitution](../../../Real%20Functions/Differentiation/Differentiation%20Rules.md) $\mathrm{d}u = u' \mathop{\mathrm{d}t}$, we obtain 
>>
>>$$
>>\int_a^b f(\varphi(u(t)))\, ||\dot\varphi (u(t))|| \, u'(t)\mathop{\mathrm{d}t} = \int_c^d f(\varphi(u))\, ||\dot \varphi(u)|| \mathop{\mathrm{d}u}
>>$$
>>
>>$$
>>\int_a^b f(\gamma(t))\, ||\dot\gamma (t)||\mathop{\mathrm{d}t} = \int_c^d f(\varphi(u))\, ||\dot \varphi(u)|| \mathop{\mathrm{d}u}
>>$$
>>
>>We are done with the case where $\gamma$ and $\varphi$ have the same orientation. Now, if $\gamma$ and $\varphi$ have [](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#^orientation), then $u(a) = d$ and $u(b) = c$. Since $a \lt b, c \lt d$ and $u$ is bijective, $u$ must be [strictly decreasing](../../../Real%20Functions/Monotony.md), i.e. $|u'(t)| = -u'(t)$. We thus have
>>
>>$$
>>\int_a^b f(\varphi(u(t)))\, ||\dot\varphi (u(t))|| \, |u'(t)|\mathop{\mathrm{d}t} = - \int_a^b f(\varphi(u(t)))\, ||\dot\varphi (u(t))|| \, u'(t)\mathop{\mathrm{d}t}
>>$$
>>
>>By applying the substitution $\mathrm{d}u = u' \mathop{\mathrm{d}t}$, we obtain 
>>
>>$$
>>-\int_a^b f(\varphi(u(t)))\, ||\dot\varphi (u(t))|| \, u'(t)\mathop{\mathrm{d}t} = - \int_d^c f(\varphi(u))\, ||\dot \varphi(u)|| \mathop{\mathrm{d}u} = \int_c^d f(\varphi(u))\, ||\dot \varphi(u)|| \mathop{\mathrm{d}u}
>>$$
>>
>>$$
>>\int_a^b f(\gamma(t))\, ||\dot\gamma (t)||\mathop{\mathrm{d}t} = - \int_d^c f(\varphi(u))\, ||\dot \varphi(u)|| \mathop{\mathrm{d}u} = \int_c^d f(\varphi(u))\, ||\dot \varphi(u)|| \mathop{\mathrm{d}u}
>>$$
>>
>>And so the proof is complete.
>>
>

The aforementioned theorem guarantees that [line integrals](Scalar%20Line%20Integrals.md) of a [real scalar field](../Real%20Scalar%20Field.md) over [continuously differentiable](../../Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md), [equivalent](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Equivalence%20of%20Parametrizations) [parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizatoins) of the same [simple curve](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Simple%20Curves) $\mathcal{C}$ are equal. However, while some [parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizatoins) may be [equivalent](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Equivalence%20of%20Parametrizations) amongst each other and some other [parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizatoins) may also be [equivalent](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Equivalence%20of%20Parametrizations) amongst each other, this does not ensure that the two groups of [parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizatoins) are *all* [equivalent](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Equivalence%20of%20Parametrizations). But then how do we know which group to choose? Well, a very natural choice is based on the [equivalence of regular injective parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Equivalence%20of%20Parametrizations). Since these [parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizatoins) are [injective](../../../../Functions/Types%20of%20Functions/Injection.md), [scalar line integrals](Scalar%20Line%20Integrals.md) over them depend only on the intrinsic [length](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Length) of $\mathcal{C}$ and not on the way these [parametrizations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizatoins) trace out $\mathcal{C}$.

>[!DEFINITION] Definition: Scalar Line Integrals over Curves
>
>The **line integral** of a [real scalar field](../Real%20Scalar%20Field.md) $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ over a [simple curve](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Curves) $\mathcal{C} \subseteq \mathcal{D}$ is defined as the [line integral](Scalar%20Line%20Integrals.md) of $f$ over any [injective](../../../../Functions/Types%20of%20Functions/Injection.md) [parametrization](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Parametrizations) $\gamma: [a;b] \subset \mathbb{R} \to \mathbb{R}^n$ of $\mathcal{C}$ which is [continuously differentiable](../../Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) on $(a;b)$ with a non-vanishing [derivative](../../Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md):
>
>$$
>\int_{\gamma} f
>$$
>
>>[!NOTATION]
>>
>>$$
>>\int_{\mathcal{C}} f \qquad \int_{\mathcal{C}} f \mathop{\mathrm{d}s}
>>$$
>
>>[!NOTE] Note: Generalization to Non-Simple Curves
>>
>>If $\mathcal{C}$ is not [simple](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Simple%20Curves) but can be represented as the [union](../../../../../Set%20Theory/Collections/Operations%20with%20Collections.md) $\mathcal{C} = \mathcal{C}_1 \cup \mathcal{C}_2 \cup \cdots \cup \mathcal{C}_{p-1} \cup \mathcal{C}_p$ of finitely many [simple curves](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Simple%20Curves) $\mathcal{C}_1, \dotsc, \mathcal{C}_p$ such that $\mathcal{C}_{k}$ and $\mathcal{C}_{k+1}$ share exactly one point and this point is an [endpoint](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Curves%20with%20Endpoints) for both $\mathcal{C}_{k}$ and $\mathcal{C}_{k+1}$, then we define the line integral of $\mathcal{f}$ over $\mathcal{C}$ as the sum of the [line integrals](Scalar%20Line%20Integrals.md#Scalar%20Line%20Integrals%20over%20Curves) of $f$ over $\mathcal{C}_1, \dotsc, \mathcal{C}_p$:
>>
>>$$
>>\int_{\mathcal{C}} f = \sum_{i = 1}^p \int_{\mathcal{C}_i} f
>>$$
>>
>>>[!NOTATION] Notation: Line Integrals over Closed Curves
>>>
>>>If $\mathcal{C}$ is [closed](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md#Closed%20Curves), we denote the line integral of $f$ over $\mathcal{C}$ as one of the following:
>>>
>>>$$
>>>\oint_{\mathcal{C}} f \qquad \oint_{\mathcal{C}} f \mathop{\mathrm{d}s}
>>>$$
>>>
>>
>