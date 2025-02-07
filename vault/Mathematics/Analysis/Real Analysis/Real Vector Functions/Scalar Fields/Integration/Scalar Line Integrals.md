---
title: Line Integrals of Scalar Fields
---

>[!DEFINITION] Definition: Line Integral of a Scalar Field
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) and let $\gamma: [a;b] \to \mathbb{R}^n$ be a [differentiable](../../../Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) [parametric curve](../../../Real%20Vector%20Functions/Parametric%20Curves/Parametric%20Curve.md) whose [image](../../../../Functions/index.md) $\gamma([a;b])$ is a [subset](../../../../../Set%20Theory/Subset.md) of $\mathcal{D}$.
>
>The **line integral** of $f$ along $\gamma$ is the [integral](../../../Real%20Functions/Integration/Definite%20Integrals/Definite%20Integral.md)
>
>$$
>\int_a^b f(\gamma(t))\, ||\dot{\gamma}(t)|| \mathop{\mathrm{d}t}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>\int_{\gamma} f \qquad \int_{\gamma} f \mathop{\mathrm{d}s}
>>$$
>>
>>If $\gamma$ is [closed](../../../Real%20Vector%20Functions/Parametric%20Curves/Closed%20Parametric%20Curve.md), we write
>>
>>$$
>>\oint_{\gamma} f \qquad \oint_{\gamma} f \mathop{\mathrm{d}s}
>>$$
>>
>
>>[!NOTE]- Note: Line Integral and Piecewise Countinuous Differentiability
>>
>>If $\gamma$ is [piecewise continuously differentiable](../../../Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) then line integrals over are just the sum of the line integrals over its parts.
>>
>

>[!THEOREM] Theorem: Line Integrals over Reparameterisations
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) and let $\gamma: [a;b] \to \mathbb{R}^n$ and $\varphi: [c;d] \to \mathbb{R}^n$ be [piecewise continuously differentiable](../../../Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) [parametric curves](../../../Real%20Vector%20Functions/Parametric%20Curves/Parametric%20Curve.md) whose [images](../../../../Functions/index.md) are [subsets](../../../../../Set%20Theory/Subset.md) of $\mathcal{D}$.
>
>If $\gamma$ and $\varphi$ are [equivalent](../../../Real%20Vector%20Functions/Parametric%20Curves/Equivalence%20of%20Parametric%20Curves.md), then the [line integrals](Scalar%20Line%20Integrals.md) of $f$ along $\gamma$ and $\varphi$ are equal.
>
>$$
>\int_{\gamma} f = \int_{\varphi} f
>$$
>
>>[!PROOF]-
>>
>>We will just show this for the case when $\gamma$ and $\varphi$ are *not* piecewise, since the proof is easily generalisable - if $\gamma$ and $\varphi$ *are* piecewise, then one can just apply the following proof to each of their partitions and obtain the same end result after summing the results from each partition.
>>
>>Since $\gamma$ and $\varphi$ parameterise the same curve $\mathcal{C}$, we can [reparameterise](../../../../../Geometry/Euclidean%20Geometry/Curves/Curve.md) one in the other. More specifically, there exists a [bijection](../../../../Functions/Types%20of%20Functions/Bijection.md), [continuously differentiable function](../../../Real%20Functions/Differentiation/Differentiability%20of%20Real%20Functions.md) $u: [a;b] \to [c;d]$ such that
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
>>If $\gamma$ and $\varphi$ have the [](../../../../../Geometry/Euclidean%20Geometry/Curves/Curve.md#^orientation), then $u(a) = c$ and $u(b) = d$. Since $a \lt b, c \lt d$ and $u$ is bijective, $u$ must be [strictly increasing](../../../Real%20Functions/Monotony/Monotony%20of%20Real%20Functions.md), i.e. $|u'(t)| = u'(t)$. We thus have
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
>>We are done with the case where $\gamma$ and $\varphi$ have the same orientation. Now, if $\gamma$ and $\varphi$ have [](../../../../../Geometry/Euclidean%20Geometry/Curves/Curve.md#^orientation), then $u(a) = d$ and $u(b) = c$. Since $a \lt b, c \lt d$ and $u$ is bijective, $u$ must be [strictly decreasing](../../../Real%20Functions/Monotony/Monotony%20of%20Real%20Functions.md), i.e. $|u'(t)| = -u'(t)$. We thus have
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


>[!THEOREM] Theorem: Linearity of the Scalar Line Integral
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

>[!THEOREM] Mean value theorem for Scalar Line Integrals
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) and let $\gamma: [a;b] \to \mathbb{R}^n$ be a [continuously differentiable](../../../Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) [parametric curve](../../../Real%20Vector%20Functions/Parametric%20Curves/Parametric%20Curve.md) whose [image](../../../../Functions/index.md) $\gamma([a;b])$ is a [subset](../../../../../Set%20Theory/Subset.md) of $\mathcal{D}$.
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