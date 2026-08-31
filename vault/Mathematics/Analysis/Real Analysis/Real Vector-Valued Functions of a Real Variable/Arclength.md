---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Arclength

>[!DEFINITION] Definition: Arclength
>
>Let $\gamma: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [vector-valued function](./Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) and let $I \subseteq \mathcal{D}$ be an [interval](../Euclidean%20Space/Euclidean%20Space.md) with [endpoints](../Euclidean%20Space/Euclidean%20Space.md) $a$ and $b$ ($a \le b$).
>
>The **arclength** traced by $\gamma$ over $I$ is the [integral](../Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md) of the [Euclidean norm](../Euclidean%20Space/Euclidean%20Space.md) of $\gamma$'s [derivative](#Differentiation%20of%20Parametric%20Curves) on $I$ (if it exists):
>
>$$\int_a^b ||\dot{\gamma}(t)|| \,\mathrm{d}t$$
>
>>[!EXAMPLE]- Example: Circumference
>>
>>We can use this to calculate the [circumference](TODO) of a [circle](TODO) in $\mathbb{R}$ which is centered at the origin and has [radius](TODO) $r$. One [parametrization](../../../Geometry/Euclidean%20Geometry/Curves/Parametrization.md) of this [circle](TODO) is the [function](./Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md)
>>
>>$$k: [0; 2\pi] \to \mathbb{R}^2$$
>>
>>defined as
>>
>>$$k(t) = \begin{bmatrix}r \cos (t) \\ r \sin (t)\end{bmatrix}$$
>>
>>for all $t \in [0;2\pi]$. The [circumference](TODO) is given as follows:
>>
>>$$\begin{aligned}\int_0^{2\pi} \vert\vert k'(t) \vert\vert \, \mathrm{d}t & = \int_0^{2\pi} \left\vert\left\vert \begin{bmatrix}-r \sin (t) \\ r \cos (t)\end{bmatrix}\right\vert\right\vert\,\mathrm{d}t \\ & = \int_0^{2\pi}\sqrt{r^2 \sin^2 t + r^2 \cos^2 (t)}\,\mathrm{d}t \\ & = \int_0^{2\pi} r\,\mathrm{d}t = 2\pi r  \end{aligned}$$
>>
>
>>[!EXAMPLE]- Example: Graph Length
>>
>>Let $f: [a,b] \subset \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Functions/Real%20Functions.md).
>>
>>If $f$ is [differentiable](../Real%20Functions/Differentiability%20(Real%20Functions).md) on $[a,b]$, the [function](./Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md)
>>
>>$$k: [a, b] \to \mathbb{R}^2$$
>>
>>defined as
>>
>>$$k(t) = \begin{bmatrix}t \\ f(t)\end{bmatrix}$$
>>
>>is a [parametrization](../../../Geometry/Euclidean%20Geometry/Curves/Parametrization.md) of $f$'s [graph](TODO). Therefore,
>>
>>$$\int_a^b ||k'(t)||\,\mathrm{d}t = \int_a^b \sqrt{1 + f'(t)^2}\,\mathrm{d}t$$
>>
>>is the [length](TODO) of this [graph](TODO).
>>
>

>[!THEOREM] Theorem: Continuously Differentiable Equivalence $\implies$ Equal Arclength
>
>Let $\gamma: [a, b] \subset \mathbb{R}$ and $\varphi: [c, d] \subset \mathbb{R}$ be [parametric curves](./Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md).
>
>If  $\gamma$ and $\phi$ are [continuously differentiable](./Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) and are [equivalent](./Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) up to a [continuously differentiable](../Real%20Functions/Differentiability%20(Real%20Functions).md) [reparametrization](./Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md), then they trace the same [arclength](./Arclength.md):
>
>$$\int_a^b ||\dot{\gamma}(t)||\,\mathrm{d}t = \int_c^d ||\dot{\varphi}(t)|| \,\mathrm{d}t$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Arclength Parametrization

>[!DEFINITION] Definition: Arclength Function
>
>Let $k: [a,b] \subset \mathbb{R} \to \mathbb{R}^n$ be a [regular](./Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) [parametric curve](./Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md).
>
>The **arclength function** of $k$ is the [function](../Real%20Functions/Real%20Functions.md)
>
>$$s: [a, b] \subset \mathbb{R} \to \mathbb{R}$$
>
>defined as the [arclength](./Arclength.md) traced by $k$ from $a$ to $t$:
>
>$$s(t) = \int_a^t ||k'(\tau)||\,\mathrm{d}\tau$$
>

>[!DEFINITION] Definition: Arclength Parametrization
>
>Let $\mathcal{C} \subseteq \mathbb{R}^n$ and let $k: [a,b] \subset \mathbb{R} \to \mathbb{R}^n$ be a [regular](./Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) [vector-valued function](./Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) which is a [parametrization](../../../Geometry/Euclidean%20Geometry/Curves/Parametrization.md) of $\mathcal{C}$.
>
>The **arclength parametrization** of $\mathcal{C}$ is the [parametric curve](./Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\tilde{k}: [0, L(k)] \to \mathbb{R}^n$ defined as
>
>$$\tilde{k}(\tau) = k (s^{-1}(\tau)),$$
>
>where $s$ is the [arclength function](./Arclength.md) of $k$.
>

>[!THEOREM] Theorem: Derivative of Arclength Parametrization
>
>The [derivative](./Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) of an [arclength parametrization](./Arclength.md) is always a [unit vector](TODO) with respect to the [Euclidean norm](../Euclidean%20Space/Euclidean%20Space.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>