---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Real Parametric Surfaces

>[!DEFINITION] Definition: Real Parametric Function
>
>A **real parametric surface** is a [real vector function](../Real%20Vector%20Functions/Real%20Vector%20Functions.md) of the following form:
>
>$$f: \mathcal{D} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$$
>
>>[!EXAMPLE]- Example: Graph of Scalar Field
>>
>>The [graph](TODO) of a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathcal{D} \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ can be [parameterized](TODO) via the [real parametric surface](./Real%20Parametric%20Surfaces.md) $\phi: \mathcal{D}^2 \to \mathbb{R}^3$ defined as follows:
>>
>>$$\phi(u,v) = \begin{bmatrix} u \\ v \\ f(u, v) \end{bmatrix}$$
>>
>
>>[!EXAMPLE]- Example: Surface of a Sphere
>>
>>The [surface](TODO) of a [sphere](TODO) of radius $R$ centered at the origin in $\mathbb{R}^3$ can be [parameterized](TODO) via the [real parametric surface](./Real%20Parametric%20Surfaces.md) $\phi: [0, \uppi] \times [0, 2\uppi] \to \mathbb{R}^3$ defined as follows:
>>
>>$$\phi(u,v) = \begin{bmatrix}R \sin u \cos v \\ R \sin u \sin v \\ R \cos u\end{bmatrix}$$
>>
>
>>[!EXAMPLE]- Example: Lateral Surface of Cylinder
>>
>>The [lateral surface](TODO) of a [cylinder](TODO) of radius $R$ and height $h$ centered placed the origin in $\mathbb{R}^3$ can be [parameterized](TODO) via the [real parametric surface](./Real%20Parametric%20Surfaces.md) $\phi: [0, 2\uppi] \times [0, h] \to \mathbb{R}^3$ defined as follows:
>>
>>$$\phi(u, v) = \begin{bmatrix}R \cos u \\ R \sin u \\ v\end{bmatrix}$$
>>
>

Some people require more stringent conditions in the definition such as [continuity](../Real%20Vector%20Functions/Continuity%20(Real%20Vector%20Functions).md) or [differentiability](../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md).
