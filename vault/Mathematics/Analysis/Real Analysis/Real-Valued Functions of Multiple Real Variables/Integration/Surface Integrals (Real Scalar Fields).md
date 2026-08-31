---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Surface Integrals (Real Scalar Fields)

TODO: Make more rigorous

>[!DEFINITION] Definition: Surface Integral
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^3 \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\phi: \mathcal{D}_{\phi} \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ be a [real parametric surface](../../Real%20Parametric%20Surfaces/Real%20Parametric%20Surfaces.md) which is [totally differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md), except possibly on a [null set](../../../../Measure%20Theory/Null%20Sets.md) of the [Lebesgue measure](../../../../Measure%20Theory/Lebesgue%20Measure.md)..
>
>The **surface integral** of $f$ over $\phi$ is the [integral](./Multidimensional%20Integrals%20(Real%20Scalar%20Fields).md) of the product between $f \circ \phi$ and [magnitude](../../Euclidean%20Space/Euclidean%20Space.md) of the [normal vector](../../Real%20Parametric%20Surfaces/Differentiation/Normal%20Vectors%20(Real%20Parametric%20Surfaces).md) of $\phi$ over $\mathcal{D}_{\phi}$ (if it exists):
>
>$$\iint_{\mathcal{D}_{\phi}} f(\phi(u,v)) ||\partial_u \phi(u,v) \times \partial_v \phi(u,v)||\,\mathrm{d}\mathcal{D}_{\phi}$$
>
>>[!NOTATION]
>>
>>The [surface integral](./Surface%20Integrals%20(Real%20Scalar%20Fields).md) of $f$ over $\phi$ is typically denoted as follows:
>>
>>$$\iint_{\phi} f \, \mathrm{d}\phi$$
>>
>>We also denote $\mathrm{d}\phi$ in various other ways such as $\mathrm{d}A$, $\mathrm{d}S$, etc.
>>
>
>>[!EXAMPLE]-
>>
>>Let $f: \mathbb{R}^3 \to \mathbb{R}$ be the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) defined as follows:
>>
>>$$f(x,y,z) = z^2$$
>>
>>We want to find the [surface integral](./Surface%20Integrals%20(Real%20Scalar%20Fields).md)
>>
>>$$\iint_{\phi} f \,\mathrm{d}\phi$$
>>
>>of $f$ over the [lateral surface](TODO) of a [cylinder](TODO) with radius $R$ and height $h$ which is [parameterized](TODO) by the following [parametric surface](../../Real%20Parametric%20Surfaces/Real%20Parametric%20Surfaces.md):
>>
>>$$\phi: [0, 2\uppi] \times [0, h] \to \mathbb{R}^3 \qquad \phi(u,v) = \begin{bmatrix}R \cos u \\ R \sin u \\ v\end{bmatrix}$$
>>
>>For the [partial derivatives](../../Real%20Vector%20Functions/Differentiation/Partial%20Differentiability%20(Real%20Vector%20Functions).md) of $\phi$, we have:
>>
>>$$\partial_u \phi(u,v) = \begin{bmatrix} - R \sin u \\ R \cos u \\ 0\end{bmatrix} \qquad \partial_v \phi(u,v) = \begin{bmatrix} 0 \\ 0 \\ 1\end{bmatrix}$$
>>
>>The [normal vector](../../Real%20Parametric%20Surfaces/Differentiation/Normal%20Vectors%20(Real%20Parametric%20Surfaces).md) of $\phi$ is thus given by
>>
>>$$\partial_u \phi(u,v) \times \partial_v \phi(u,v) = \begin{bmatrix} - R \sin u \\ R \cos u \\ 0\end{bmatrix} \times \begin{bmatrix} 0 \\ 0 \\ 1\end{bmatrix} = \begin{bmatrix}R \cos u \\ R \sin u \\ 0\end{bmatrix}$$
>>
>>and its [magnitude](../../Euclidean%20Space/Euclidean%20Space.md) is the following:
>>
>>$$||\partial_u \phi(u,v) \times \partial_v \phi(u,v)|| = R$$
>>
>>For the [surface integral](./Surface%20Integrals%20(Real%20Scalar%20Fields).md), we have:
>>
>>$$\begin{aligned}\iint_{\phi} f \,\mathrm{d}\phi & = \iint_{\mathcal{D}_{\phi}} f(\phi(u,v)) ||\partial_u \phi(u,v) \times \partial_v \phi(u,v)||\,\mathrm{d}\mathcal{D}_{\phi} \\ & = \iint_{[0, 2\uppi] \times [0, h]} R^2 \cos^2 (u) R \, \mathrm{d}\mathcal{D}\end{aligned}$$
>>
>>Since $R^2 \cos^2 (u) R$ is [continuous](../Continuity%20(Real%20Scalar%20Fields).md), we can evaluate it via an [iterated integral](./Parametric%20Integrals.md):
>>
>>$$\begin{aligned} \iint_{[0, 2\uppi] \times [0, h]} R^2 \cos^2 (u) R \, \mathrm{d}\mathcal{D} & = \int_0^h \left(\int_0^{2\uppi} R^2 \cos^2 (u) R \,\mathrm{d}u \right) \, \mathrm{d}v \\ & = R^3 \int_0^h \left(\int_0^{2\uppi} \cos^2 u \,\mathrm{d}u \right) \, \mathrm{d}v \\ & = R^3 \int_0^h \left(\int_0^{2\uppi} \frac{1 + \cos(2u)}{2} \,\mathrm{d}u \right) \, \mathrm{d}v \\ & = R^3 \int_0^h \left.\left( \frac{u}{2} + \frac{\sin(2u)}{4} \right)\right\vert_0^{2\uppi} \, \mathrm{d}v \\ & = R^3 \int_0^h \left( \left( \frac{2\uppi}{2} + 0 \right) - (0 + 0) \right) \, \mathrm{d}v \\ & = R^3 \int_0^h \uppi \, \mathrm{d}v \\ & = \uppi R^3 v \vert_0^h \\ & = \uppi R^3 h \end{aligned}$$
>>
>
