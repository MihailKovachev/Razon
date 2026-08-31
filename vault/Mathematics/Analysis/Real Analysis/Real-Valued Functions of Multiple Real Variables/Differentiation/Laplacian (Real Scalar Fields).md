---
tags:
    - real-analysis
    - vector-analysis
    - analysis
    - mathematics
---

# Laplacian (Real Scalar Fields)

>[!DEFINITION] Definition: Laplacian (Real Scalar Fields)
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md), let $\boldsymbol{p} \in \operatorname{int} \mathcal{D}$ be an [interior point](../../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $\mathcal{D}_f$, suppose that $f$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$ and suppose that each [partial derivative](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) $\partial_k f$ is itself [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$ with respect to the $k$-th variable.
>
>The **Laplacian** of $f$ at $\boldsymbol{p}$ is defined as follows:
>
>$$\sum_{k = 1}^n \partial_k \partial_k f(\boldsymbol{p})$$
>
>>[!NOTATION]
>>
>>$$\nabla^2 f (\boldsymbol{p}) \qquad \Delta f(\boldsymbol{p})$$
>>
>
>>[!EXAMPLE]- Example: $f(x,y) = \sin(\uppi x)\sin (\uppi y)$
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^2 \to \mathbb{R}$ defined as follows:
>>
>>$$f(x, y) \overset{\text{def}}{=} \sin(\uppi x)\sin (\uppi y)$$
>>
>>We see that $f$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^2$:
>>
>>$$\partial_x f(x,y) = \uppi \cos (\uppi x) \sin(\uppi y) \qquad \partial_y f(x,y) = \uppi \sin (\uppi x) \cos (\uppi y)$$
>>
>>Similarly, we see that $\partial_x f$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^2$ with respect to $x$:
>>
>>$$\partial_x \partial_x f(x,y) = - \uppi^2 \sin(\uppi x)\sin (\uppi y)$$
>>
>>By the same token, $\partial_y f$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^2$ with respect to $y$:
>>
>>$$\partial_y \partial_y f(x,y) = - \uppi^2 \sin(\uppi x)\sin (\uppi y)$$
>>
>>Therefore, the [Laplacian](./Laplacian%20(Real%20Scalar%20Fields).md) of $f$ exists at each $\begin{bmatrix}x & y\end{bmatrix}^{\mathsf{T}} \in \mathbb{R}^2$:
>>
>>$$\begin{aligned}\nabla^2 f (x,y) & = \partial_x \partial_x f(x,y) + \partial_y \partial_y f(x,y) \\ & = - \uppi^2 \sin(\uppi x)\sin (\uppi y) - \uppi^2 \sin(\uppi x)\sin (\uppi y) \\ & = -2 \uppi^2 \sin(\uppi x)\sin (\uppi y)\end{aligned}$$
>>
>

>[!THEOREM] Theorem: Laplacian = Divergence of Gradient
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md), let $\boldsymbol{p} \in \operatorname{int} \mathcal{D}$ be an [interior point](../../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $f$.
>
>If TODO, then the [Laplacian](./Laplacian%20(Real%20Scalar%20Fields).md) of $f$ at $\boldsymbol{p}$ is the [divergence](../../Real%20Vector%20Fields/Differentiation/Divergence%20(Real%20Vector%20Fields).md) of $f$'s [gradient](./Gradient%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$:
>
>$$\nabla^2 f (\boldsymbol{p}) = \operatorname{div} \operatorname{grad} f(\boldsymbol{p})$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Laplacian from Polar Coordinate Representation
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^2 \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\mathcal{T}: (0, +\infty) \times (0, 2\uppi) \to \mathbb{R}^2$ be the [coordinate transformation](../../Euclidean%20Space/Coordinate%20Transformations.md) from [polar coordinates](../../Euclidean%20Space/Polar%20Coordinates.md):
>
>$$\mathcal{T}(\rho, \varphi) = \begin{bmatrix} \rho \cos \varphi \\ \rho \sin \varphi\end{bmatrix}$$
>
>Let $\tilde{f} = f \circ \mathcal{T}$ be the [polar coordinate representation](../Polar%20Coordinate%20Representations%20(Real%20Scalar%20Fields).md) of $f$.
>
>If $f$ is [twice totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\mathcal{T}(\rho, \varphi)$, then its [Laplacian](./Laplacian%20(Real%20Scalar%20Fields).md) at $\mathcal{T}(\rho, \varphi)$ is expressed using [partial derivatives](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) of $\tilde{f}$ as follows:
>
>$$(\nabla^2 f) (\mathcal{T}(\rho, \varphi)) = (\partial_{\rho} (\partial_{\rho} \tilde{f}))(\rho, \varphi) + \frac{1}{\rho} \partial_{\rho} \tilde{f}(\rho, \varphi) + \frac{1}{\rho^2} (\partial_{\varphi} (\partial_{\varphi} \tilde{f}))(\rho, \varphi)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Green's First Identity
>
>$$\iiint_{\mathcal{D}} (\nabla^2 f) g \, \mathrm{d}\mathcal{D} = -\iiint_{\mathcal{D}} \nabla f \cdot \nabla g \, \mathrm{d}\mathcal{D} + \iint_{\partial \mathcal{D}} g \nabla f \cdot \mathbf{n} \, \mathrm{d}S$$
>
>>[!PROOF]-
>>
>>TODO
>>
>