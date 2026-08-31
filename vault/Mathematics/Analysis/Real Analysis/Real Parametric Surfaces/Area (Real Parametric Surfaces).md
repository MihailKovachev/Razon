---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Area (Real Parametric Surfaces)

TODO: Make this more rigorous

>[!DEFINITION] Definition: Area
>
>Let $\phi: \mathcal{D} \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ be a [totally differentiable](../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) [real parametric surface](./Real%20Parametric%20Surfaces.md).
>
>The **area** of $\phi$ is the [integral](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Integration/Multidimensional%20Integrals%20(Real%20Scalar%20Fields).md) of the [magnitude](../Euclidean%20Space/Euclidean%20Space.md) of its [normal vector](./Differentiation/Normal%20Vectors%20(Real%20Parametric%20Surfaces).md) (if it exists):
>
>$$\iint_{\mathcal{D}} ||\partial_u \phi(u, v) \times \partial_v \phi(u,v)||\,\mathrm{d}\mathcal{D}$$
>
>>[!NOTATION]
>>
>>$$A(\phi) \qquad S(\phi)$$
>>
>
>>[!EXAMPLE]- Example: Area of Graph
>>
>>Let $f: \mathcal{D} \subseteq \mathbb{R}^2 \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\phi: \mathcal{D} \to \mathbb{R}^3$ be a [parametric surface](./Real%20Parametric%20Surfaces.md) which [parameterizes](TODO) $f$'s [graph](TODO):
>>
>>$$\phi(u,v) = \begin{bmatrix}u \\ v \\ f(u, v)\end{bmatrix}$$
>>
>>If $f$ is [totally differentiable](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Total%20Differentiability%20(Real%20Scalar%20Fields).md), then $\phi$ is also [totally differentiable](../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) and for $\phi$'s [partial derivatives](../Real%20Vector%20Functions/Differentiation/Partial%20Differentiability%20(Real%20Vector%20Functions).md), we have:
>>
>>$$\partial_u \phi(u,v) = \begin{bmatrix} 1 \\ 0 \\ \partial_u f(u,v) \end{bmatrix} \qquad \partial_v \phi(u,v) = \begin{bmatrix} 0 \\ 1 \\ \partial_v f(u,v) \end{bmatrix}$$
>>
>>For $\phi$'s [normal vector](./Differentiation/Normal%20Vectors%20(Real%20Parametric%20Surfaces).md), we have:
>>
>>$$\partial_u \phi(u,v) \times \partial_v \phi(u,v) = \begin{bmatrix} 1 \\ 0 \\ \partial_u f(u,v) \end{bmatrix} \times \begin{bmatrix} 0 \\ 1 \\ \partial_v f(u,v) \end{bmatrix} = \begin{bmatrix} - \partial_u f(u, v) \\ - \partial_v f(u, v) \\ 1 \end{bmatrix}$$
>>
>>$$||\partial_u \phi(u,v) \times \partial_v \phi(u,v)|| = \sqrt{1 + \partial_u f(x,y)^2 + \partial_v f(u,v)^2}$$
>>
>>The [area](./Area%20(Real%20Parametric%20Surfaces).md) of $\phi$ is thus given by the following [integral](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Integration/Riemann%20Integrals%20(Real%20Scalar%20Fields).md) (if it exists):
>>
>>$$\iint_{\mathcal{D}} \sqrt{1 + \partial_u f(x,y)^2 + \partial_v f(u,v)^2} \,\mathrm{d}(u,v)$$
>>
>
>>[!EXAMPLE]- Example: Surface of a Sphere
>>
>>The [surface](TODO) of a [sphere](TODO) of radius $R$ centered at the origin in $\mathbb{R}^3$ can be [parameterized](TODO) via the [real parametric surface](./Real%20Parametric%20Surfaces.md) $\phi: [0, \uppi] \times [0, 2\uppi] \to \mathbb{R}^3$ defined as follows:
>>
>>$$\phi(u,v) = \begin{bmatrix}R \sin u \cos v \\ R \sin u \sin v \\ R \cos u\end{bmatrix}$$
>>
>>We see that $\phi$ is [totally differentiable](../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md). For its [partial derivatives](../Real%20Vector%20Functions/Differentiation/Partial%20Differentiability%20(Real%20Vector%20Functions).md), we have
>>
>>$$\partial_u \phi(u, v) = \begin{bmatrix} R \cos u \cos v \\ R \cos u \sin v \\ -R \sin u \end{bmatrix} \qquad \partial_v \phi(u, v) = \begin{bmatrix} -R \sin u \sin v \\ R \sin u \cos v \\ 0 \end{bmatrix}$$
>>
>>and so its [normal vector](./Differentiation/Normal%20Vectors%20(Real%20Parametric%20Surfaces).md) is the following:
>>
>>$$\begin{aligned}\partial_u \phi(u, v) \times \partial_v \phi(u, v) & = \begin{bmatrix} R \cos u \cos v \\ R \cos u \sin v \\ -R \sin u \end{bmatrix} \times \begin{bmatrix} -R \sin u \sin v \\ R \sin u \cos v \\ 0 \end{bmatrix} \\ & = R^2 \sin u \begin{bmatrix}\sin u \cos v \\ \sin u \sin v \\ \cos u\end{bmatrix}\end{aligned}$$
>>
>>We have:
>>
>>$$||\partial_u \phi(u, v) \times \partial_v \phi(u, v)|| = R^2 \sin u$$
>>
>>The [area](./Area%20(Real%20Parametric%20Surfaces).md) of $\phi$ is thus given by the following [integral](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Integration/Multidimensional%20Integrals%20(Real%20Scalar%20Fields).md):
>>
>>$$F(\phi) = \iint_{\mathcal{D}} ||\partial_u \phi(u, v) \times \partial_v \phi(u, v)|| \,\mathrm{d}\mathcal{D} = \iint_{[0, \uppi] \times [0, 2\uppi]} R^2 \sin u\,\mathrm{d}\mathcal{D}$$
>>
>>Since $R^2 \sin u$ is [continuous](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Continuity%20(Real%20Scalar%20Fields).md), we can compute it via an [iterated integral](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Integration/Parametric%20Integrals.md):
>>
>>$$\begin{aligned}\iint_{[0, \uppi] \times [0, 2\uppi]} R^2 \sin u\,\mathrm{d}\mathcal{D} & = \int_0^{2\uppi} \int_{0}^{\uppi} R^2 \sin u \,\mathrm{d}u \,\mathrm{d}v \\ & = R^2\int_0^{2\uppi} \int_{0}^{\uppi} \sin u \,\mathrm{d}u \,\mathrm{d}v \\ & = R^2 \int_{0}^{2\uppi} \left(\left.-\cos u \right\vert_{0}^{\uppi}\right) \,\mathrm{d}v \\ & = R^2 \int_{0}^{2\uppi} 2 \,\mathrm{d}v \\ & = 4\uppi R^2\end{aligned}$$
>>
>