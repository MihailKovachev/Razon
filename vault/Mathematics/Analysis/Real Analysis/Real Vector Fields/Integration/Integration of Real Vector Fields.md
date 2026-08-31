---
title: Integration of Real Vector Fields
tags:
  - real-analysis
  - vector-analysis
  - mathematical-analysis
  - mathematics
---

# Line Integrals

>[!THEOREM] Theorem: Vector Line Integrals and Equivalence
>
>Let $\mathbf{F}: \mathcal{D}_{\mathbf{F}} \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [real vector field](../Real%20Vector%20Fields.md) and let $\gamma: \mathcal{D}_{\gamma} \subset \mathbb{R} \to \mathbb{R}^n$ and $\varphi: \mathcal{D}_{\varphi} \subset \mathbb{R} \to \mathbb{R}^n$ be [vector-valued](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md).
>
>If $\gamma$ and $\varphi$ are [continuously differentiable](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) and are [equivalent](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md#Equivalence) up to a [continuously differentiable](../../Real%20Functions/Differentiability%20(Real%20Functions).md) [reparametrization](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md#Equivalence), then the [line integrals](#Vector%20Line%20Integrals) of $\mathbf{F}$ along $\gamma$ and $\varphi$
>
>-  are equal whenever $\gamma$ and $\varphi$ have the [same orientation](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md#Orientation)
>
>$$
>\int_{\gamma} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{s}} = \int_{\varphi} \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{s}}
>$$
>
>- are opposite whenever $\gamma$ and $\varphi$ have [opposite orientations](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md#Orientation)
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

>[!THEOREM] Green's Theorem
>
>Let $\gamma: [a; b] \subseteq \mathbb{R} \to \mathbb{R}^2$ be [simple closed parametric curve](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) which is [positively oriented](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) and [piecewise continuously differentiable](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) on $(a;b)$, let $R \subseteq \mathbb{R}^2$ be the region bounded by $\gamma$ and let $\boldsymbol{v}: \mathcal{D}_{\boldsymbol{v}} \subset \mathbb{R}^2 \to \mathbb{R}^2$ be a [real vector field](../Real%20Vector%20Fields.md) with [component functions](../../Real%20Vector%20Functions/Real%20Vector%20Functions.md) $v_1, v_2$.
>
>If $\boldsymbol{v}$ is [continuously differentiable](./Differentiation%20of%20Real%20Vector%20Fields.md) on $R$, then the [line integral](./Integration%20of%20Real%20Vector%20Fields.md) of $\boldsymbol{v}$ over $\gamma$ is given by the following [double integral](../../Real%20Scalar%20Fields/Integration/Integration%20of%20Real%20Scalar%20Fields.md):
>
>$$
>\int_{\gamma} \boldsymbol{v} \cdot \mathop{\mathrm{d}v} = \iint_R \frac{\partial v_2}{\partial x} - \frac{\partial v_1}{\partial y} \mathop{\mathrm{d}R}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Surface Integrals

>[!DEFINITION] Definition: Vector Surface Integral
>
>Let $\mathbf{F}: \mathcal{D}_{\mathbf{F}} \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [real vector field](../Real%20Vector%20Fields.md) and let $S: \mathcal{D}_S \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ be a [differentiable](../../Real%20Parametric%20Surfaces/Differentiation/Differentiation%20of%20Parametric%20Surfaces.md) [parametric surface](../../Real%20Parametric%20Surfaces/Real%20Parametric%20Surfaces.md) such that $S(\mathcal{D}_S) \subseteq \mathcal{D}_{\mathbf{F}}$.
>
>The **(vector) surface integral** of $\mathbf{F}$ over $S$ is the [double integral](../../Real%20Scalar%20Fields/Integration/Integration%20of%20Real%20Scalar%20Fields.md) of the [dot product](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md#Dot%20Product) $\mathbf{F} \circ S$ with the [surface normal](../../Real%20Parametric%20Surfaces/Differentiation/Differentiation%20of%20Parametric%20Surfaces.md#Normal%20Spaces) of $S$:
>
>$$
>\iint_{\mathcal{D}_S} (\mathbf{F}\circ S) \cdot \mathbf{N} \mathop{\mathrm{d}\mathcal{D}_S}
>$$
>
>>[!NOTATION]
>>
>>$$
>>\iint_S \mathbf{F} \cdot \mathrm{d}\mathbf{S}
>>$$
>>
>>If $S(\mathcal{D}_S)$ is a [closed surface](../../Real%20Parametric%20Surfaces/Real%20Parametric%20Surfaces.md), then a circle can be put through the two integral signs.
>>
>

>[!THEOREM] Theorem: Vector Surface Integral to Scalar Surface Integral
>
>Let $\mathbf{F}: \mathcal{D}_{\mathbf{F}} \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [real vector field](../Real%20Vector%20Fields.md) and let $S: \mathcal{D}_S \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ be a [differentiable](../../Real%20Parametric%20Surfaces/Differentiation/Differentiation%20of%20Parametric%20Surfaces.md) [parametric surface](../../Real%20Parametric%20Surfaces/Real%20Parametric%20Surfaces.md) such that $S(\mathcal{D}_S) \subseteq \mathcal{D}_{\mathbf{F}}$.
>
>The [surface integral](./Integration%20of%20Real%20Vector%20Fields.md) of $\mathbf{F}$ over $S$ is equal to the [surface integral](../../Real%20Scalar%20Fields/Integration/Integration%20of%20Real%20Scalar%20Fields.md#Surface%20Integrals) of the [dot product](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md#Dot%20Product) between $\mathbf{F}$ and the [unit surface normal](../../Real%20Parametric%20Surfaces/Differentiation/Differentiation%20of%20Parametric%20Surfaces.md) of $S$.
>
>$$
>\iint_S \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{S}} = \iint_S \mathbf{F} \cdot \mathbf{n} \mathop{\mathrm{d}S}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Vector Surface Integrals and Equivalence
>
>Let $\mathbf{F}: \mathcal{D}_{\mathbf{F}} \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [real vector field](../Real%20Vector%20Fields.md) and let $\phi: \mathcal{D}_{\phi} \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ and $\psi: \mathcal{D}_{\psi} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ be [parametric surfaces](../../Real%20Parametric%20Surfaces/Real%20Parametric%20Surfaces.md).
>
>If $\phi$ and $\psi$ are [continuously differentiable](../../Real%20Parametric%20Surfaces/Differentiation/Differentiation%20of%20Parametric%20Surfaces.md) and are [equivalent](../../Real%20Parametric%20Surfaces/Real%20Parametric%20Surfaces.md#Equivalence) up to a [continuously differentiable](./Differentiation%20of%20Real%20Vector%20Fields.md) [reparametrization](../../Real%20Parametric%20Surfaces/Real%20Parametric%20Surfaces.md#Equivalence), then the [surface integrals](./Integration%20of%20Real%20Vector%20Fields.md) of $\mathbf{F}$ over $\phi$ and $\psi$ are:
>
>- equal when $\phi$ and $\psi$ have the [same orientation](../../Real%20Parametric%20Surfaces/Differentiation/Differentiation%20of%20Parametric%20Surfaces.md)
>
>$$
>\iint_{\phi} \mathbf{F} \cdot \mathop{\mathrm{d}\phi} = \iint_{\psi} \mathbf{F} \cdot \mathop{\mathrm{d}\psi}
>$$
>
>- opposite when $\phi$ and $\psi$ have [opposite orientations](../../Real%20Parametric%20Surfaces/Differentiation/Differentiation%20of%20Parametric%20Surfaces.md)
>
>$$
>\iint_{\phi} \mathbf{F} \cdot \mathop{\mathrm{d}\phi} = -\iint_{\psi} \mathbf{F} \cdot \mathop{\mathrm{d}\psi}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] The Divergence Theorem (Gauss's Theorem, Ostrogradsky's Theorem)
>
>Let $V$ be a [compact](../../../../Topology/Compactness.md) [subset](../../../../Set%20Theory/Sets.md#Subsets) of the [Euclidean space](../../Euclidean%20Space/Euclidean%20Space.md) $\mathbb{R}^n$, let $s: \mathcal{D}_s \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ be a [parametric surface](../../Real%20Parametric%20Surfaces/Real%20Parametric%20Surfaces.md) whose [image](../../../Functions/Functions.md) is the [boundary](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of $V$ and let $\mathbf{F}: \mathcal{D}_{\mathbf{F}} \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [real vector field](../Real%20Vector%20Fields.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>