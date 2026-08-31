---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Surface Integrals (Real Vector Fields)

TODO: Make more rigorous

>[!DEFINITION] Definition: Surface Integral (Real Vector Field)
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [real vector field](../Real%20Vector%20Fields.md) and let $\phi: \mathcal{D}_{\phi} \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ be a [real parametric surface](../../Real%20Parametric%20Surfaces/Real%20Parametric%20Surfaces.md) which is [totally differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md), except possibly on a [null set](../../../../Measure%20Theory/Null%20Sets.md) of the [Lebesgue measure](../../../../Measure%20Theory/Lebesgue%20Measure.md).
>
>The **surface integral** of $f$ over $\phi$ is the [integral](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Integration/Lebesgue%20Integrals%20(Real%20Scalar%20Fields).md) of the [dot product](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Dot%20Product.md) between $f \circ \phi$ and the [normal vector](../../Real%20Parametric%20Surfaces/Differentiation/Normal%20Vectors%20(Real%20Parametric%20Surfaces).md) of $\phi$ over $\mathcal{D}_{\phi}$ (if it exists):
>
>$$\iint_{\mathcal{D}_{\phi}} f(\phi(u,v)) \cdot \partial_u \phi(u,v) \times \partial_v \phi(u,v) \,\mathrm{d}\mathcal{D}_{\phi}$$
>
>>[!NOTATION]
>>
>>The [surface integral](./Surface%20Integrals%20(Real%20Vector%20Fields).md) of $f$ over $\phi$ is denoted as follows:
>>
>>$$\iint_{\phi} f \cdot \mathrm{d}\boldsymbol{\phi}$$
>>
>>Sometimes, $\mathrm{d}\boldsymbol{\phi}$ is denoted by $\mathrm{d}\boldsymbol{S}$, $\mathrm{d}\boldsymbol{A}$, etc.
>>
>

>[!THEOREM] Theorem: Vector Surface Integral $=$ Scalar Surface Integral
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [real vector field](../Real%20Vector%20Fields.md) and let $\phi: \mathcal{D}_{\phi} \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ be a [real parametric surface](../../Real%20Parametric%20Surfaces/Real%20Parametric%20Surfaces.md) which is [regular](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md), except possibly on a [null set](../../../../Measure%20Theory/Null%20Sets.md) of the [Lebesgue measure](../../../../Measure%20Theory/Lebesgue%20Measure.md).
>
>If the [surface integral](./Surface%20Integrals%20(Real%20Vector%20Fields).md) of $f$ over $\phi$ and the [surface integral](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Integration/Surface%20Integrals%20(Real%20Scalar%20Fields).md) of the [dot product](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Dot%20Product.md) between $f$ and the [unit normal vector](../../Real%20Parametric%20Surfaces/Differentiation/Normal%20Vectors%20(Real%20Parametric%20Surfaces).md) of $\phi$ exist, then they are equal:
>
>$$\int_{\phi} f \, \cdot \mathrm{d}\boldsymbol{\phi} = \int_{\phi} (f \cdot \mathbf{n}) \, \mathrm{d}\phi$$
>
>>[!PROOF]-
>>
>>TODO
>>
>