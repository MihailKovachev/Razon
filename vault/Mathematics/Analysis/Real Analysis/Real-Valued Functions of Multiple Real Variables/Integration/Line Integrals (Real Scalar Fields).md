---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Line Integrals (Real Scalar Fields)

>[!DEFINITION] Definition: Line Integral of a Real Scalar Field
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\gamma: I \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [real parametric curve](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) which is [differentiable](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) on the [interior](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of the [interval](../../Euclidean%20Space/Euclidean%20Space.md) $I$ with $\gamma(I) \subseteq \mathcal{D}_f$.
>
>The **line integral** of $f$ **along** $\gamma$ is the [(potentially improper) Riemann integral](../../Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md)
>
>$$\int_I f(\gamma(t)) ||\gamma'(t)||\, \mathrm{d}t,$$
>
>provided that it exists.
>
>>[!NOTATION]
>>
>>We denote the [line integral](./Line%20Integrals%20(Real%20Scalar%20Fields).md) of $f$ along $\gamma$ as follows:
>>
>>$$\int_{\gamma} f \,\mathrm{d}s$$
>>
>>If $\gamma$ is [closed](TODO), we write:
>>
>>$$\oint_{\gamma} f \,\mathrm{d}s$$
>>
>
>>[!EXAMPLE]-
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^2 \to \mathbb{R}$ defined as
>>
>>$$f(x, y) = x$$
>>
>>and the [parametric curve](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\gamma: [0,1] \to \mathbb{R}^2$ defined as follows:
>>
>>$$\gamma(t) = \begin{bmatrix}t \\ t^2\end{bmatrix}$$
>>
>>It is [continuous](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Continuity%20(Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable).md) on $[0,1]$ and [continuously differentiable](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) on $(0,1)$:
>>
>>$$\gamma'(t) = \begin{bmatrix} 1 \\ 2t\end{bmatrix}$$
>>
>>Since $f$ is also [continuous](../Continuity%20(Real%20Scalar%20Fields).md), we know that $f(\gamma(t))||\gamma'(t)||$ is [continuous](../../Real%20Functions/Continuity%20(Real%20Functions).md) and thus [Riemann-integrable](../../Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md). Therefore, we have
>>
>>$$\begin{aligned}\int_{\gamma} f \,\mathrm{d}s & = \int_0^1 f(\gamma(t))||\gamma'(t)|| \,\mathrm{d}t \\ & = \int_0^1 t\sqrt{1+4t^2}\,\mathrm{d}t \\ & = \left.\frac{1}{12}(1+4t^2)^{\frac{3}{2}}\right\vert_0^1 \\ & = \frac{1}{12}(5^{\frac{3}{2}} - 1)\end{aligned}$$
>>
>>for the [line integral](./Line%20Integrals%20(Real%20Scalar%20Fields).md) of $f$ along $\gamma$.
>>
>

>[!THEOREM] Theorem: Linearity of Line Integrals
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R}^n \to \mathbb{R}$ be [real scalar fields](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\gamma: I \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [real parametric curve](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) which is [differentiable](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) on the [interior](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of the [interval](../../Euclidean%20Space/Euclidean%20Space.md) $I$ with $\gamma(I) \subseteq \mathcal{D}_f \cap \mathcal{D}_g$.
>
>If the [line integrals](./Line%20Integrals%20(Real%20Scalar%20Fields).md) of $f$ and $g$ along $\gamma$ exist, then so does the [line Integral](./Line%20Integrals%20(Real%20Scalar%20Fields).md) of $\alpha f + \beta g$ for all $\alpha, \beta \in \mathbb{R}$:
>
>$$\int_{\gamma} \alpha f + \beta g\,\mathrm{d}s = \alpha \int_{\gamma} f \, \mathrm{d}s + \beta \int_{\gamma} g \, \mathrm{d}s$$
>
>>[!PROOF]-
>>
>>$$\begin{aligned}\int_{\gamma} \alpha f + \beta g\,\mathrm{d}s & = \int_I((\alpha f + \beta g) \circ \gamma)(t) ||\gamma'(t)||\,\mathrm{d}t \\ & = \int_I(\alpha f (\gamma(t)) + \beta g(\gamma(t)))||\gamma'(t)||\,\mathrm{d}t \\ & = \int_I\alpha f (\gamma(t))||\gamma'(t)|| \,\mathrm{d}t + \int_I\beta g(\gamma(t))||\gamma'(t)|| \,\mathrm{d}t \end{aligned}$$
>>
>>Since the [line integrals](./Line%20Integrals%20(Real%20Scalar%20Fields).md) of $f$ and $g$ along $\gamma$ exist, we know that
>>
>>$$\int_If (\gamma(t))||\gamma'(t)|| \,\mathrm{d}t= \int_{\gamma} f \,\mathrm{d}s$$
>>
>>and
>>
>>$$\int_Ig (\gamma(t))||\gamma'(t)|| \,\mathrm{d}t = \int_{\gamma} g \,\mathrm{d}s$$
>>
>>exist. Therefore:
>>
>>$$\begin{aligned}\int_{\gamma} \alpha f + \beta g\,\mathrm{d}s & = \alpha \int_If (\gamma(t))||\gamma'(t)|| \,\mathrm{d}t + \beta \int_Ig (\gamma(t))||\gamma'(t)|| \,\mathrm{d}t \\ & = \alpha \int_{\gamma} f \, \mathrm{d}s + \beta \int_{\gamma} g \, \mathrm{d}s\end{aligned}$$
>>
>

>[!THEOREM] Theorem: Line Integrals under Reparametrization
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\gamma: I_{\gamma} \subseteq \mathbb{R} \to \mathbb{R}^n$ and $\varphi: I_{\varphi} \subseteq \mathbb{R} \to \mathbb{R}^n$ be [real parametric curve](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) which are [continuously differentiable](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) on the [interior](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of the [intervals](../../Euclidean%20Space/Euclidean%20Space.md) $I_{\gamma}$ and $I_{\varphi}$, respectively, with $\gamma(I_{\gamma}) = \varphi(I_{\varphi}) \subseteq \mathcal{D}_f$.
>
>If the [line integrals](./Line%20Integrals%20(Real%20Scalar%20Fields).md) of $f$ along $\gamma$ and $\varphi$ exist and $\gamma$ and $\varphi$ are [equivalent](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md#Equivalence) up to a [continuously differentiable](../../Real%20Functions/Differentiability%20(Real%20Functions).md) [reparametrization](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md#Equivalence), then those [line integrals](./Line%20Integrals%20(Real%20Scalar%20Fields).md) are equal:
>
>$$\int_{\gamma} f \,\mathrm{d}s = \int_{\varphi} f \,\mathrm{d}s$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Mean Value Theorem for Scalar Line Integrals
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\gamma: [a,b] \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [real parametric curve](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) with $\gamma([a,b]) \subseteq \mathcal{D}_f$.
>
>If $f$ is [continuous](../Continuity%20(Real%20Scalar%20Fields).md) on $\gamma([a,b])$ and $\gamma$ is [continuous](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Continuity%20(Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable).md) on $[a,b]$ and [continuously differentiable](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) on $(a,b)$, then there exists some $t \in [a,b]$ such that the [line integral](./Line%20Integrals%20(Real%20Scalar%20Fields).md) of $f$ along $\gamma$ is equal to $f(\gamma(t))\cdot L$, where $L$ is the [arclength](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Arclength.md) traced by $\gamma$:
>
>$$\int_{\gamma} f \, \mathrm{d}s = f(\gamma(t))\cdot L$$
>
>>[!PROOF]-
>>
>>TODO
>>
>