---
tags:
    - real-analysis
    - vector-analysis
    - analysis
    - mathematics
---

# Hessian Matrix

>[!DEFINITION] Definition: Hessian Matrix
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md), let $\boldsymbol{p} \in \operatorname{int} \mathcal{D}$ be an [interior point](../../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $\mathcal{D}$ and suppose that $f$ is [twice partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$.
>
>The **Hessian matrix** of $f$ at $\boldsymbol{p}$ is $n\times n$-[real matrix](../../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) whose components are $f$'s [second-order partial derivatives](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$:
>
>$$\begin{bmatrix}\partial_1 \partial_1 f(\boldsymbol{p}) & \cdots & \partial_1\partial_n f(\boldsymbol{p}) \\ \vdots & \ddots & \vdots \\ \partial_n \partial_1 f(\boldsymbol{p}) & \cdots & \partial_n\partial_n f(\boldsymbol{p})\end{bmatrix}$$
>
>>[!TIP] Tip: Hessian Matrix and Gradients
>>
>>The columns of the [Hessian matrix](./Hessian%20Matrix.md) are just the [gradients](./Gradient%20(Real%20Scalar%20Fields).md) of $f$'s [partial derivatives](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md):
>>
>>$$H_f(\boldsymbol{p}) = \begin{bmatrix}\vert & \vert & \vert \\ \nabla(\partial_1 f)(\boldsymbol{p}) & \cdots & \nabla(\partial_n f)(\boldsymbol{p}) \\ \vert & \vert & \vert \end{bmatrix}$$
>>
>
>>[!NOTATION]
>>
>>$$H_f(\boldsymbol{p})$$
>>
>
>>[!EXAMPLE]- Example: $f(x, y) = x^2 y^3 + x$
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^2 \to \mathbb{R}$ defined as follows:
>>
>>$$f\left(x, y\right) = x^2 y^3 + x$$
>>
>>It is [twice partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^2$:
>>
>>$$\partial_x f (x, y) = 2x y^3 + 1 \qquad \partial_x \partial_x f(x,y) = 2y^3 \qquad \partial_{y} \partial_x f(x,y) = 6x y^2$$
>>
>>$$\partial_y f (x, y) = 3 x^2 y^2 \qquad \partial_x \partial_y f(x,y) = 6x y^2 \qquad \partial_y \partial_y f(x,y) = 6 x^2 y$$
>>
>>Its [Hessian matrix](./Hessian%20Matrix.md) is thus the following for all $\begin{bmatrix}x & y\end{bmatrix}^{\mathsf{T}} \in \mathbb{R}^2$:
>>
>>$$H_f(x,y) = \begin{bmatrix} \partial_x \partial_x f(x,y) & \partial_x \partial_y f(x,y) \\ \partial_y \partial_x f(x,y) & \partial_y \partial_y f(x,y)  \end{bmatrix} = \begin{bmatrix} 2y^3 & 6x y^2 \\ 6x y^2 & 6 x^2 y\end{bmatrix}$$
>>
>
>>[!EXAMPLE]- Example: $f(\boldsymbol{x}) = \boldsymbol{a}^{\mathsf{T}}\boldsymbol{x}$
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^n \to \mathbb{R}$ defined as
>>
>>$$f(\boldsymbol{x}) = \boldsymbol{a}^{\mathsf{T}}\boldsymbol{x}$$
>>
>>for some fixed [real vector](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $\boldsymbol{a} = \begin{bmatrix} a^1 & \cdots & a^n \end{bmatrix}^{\mathsf{T}}\in \mathbb{R}^n$.
>>
>>Its [Hessian matrix](./Hessian%20Matrix.md) is zero everywhere:
>>
>>$$H_f(\boldsymbol{p}) = \boldsymbol{0}$$
>>
>
>>[!EXAMPLE]- Example: $f(\boldsymbol{x}) = \boldsymbol{x}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{x}$
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^n \to \mathbb{R}$ defined as
>>
>>$$f(\boldsymbol{x}) = \boldsymbol{x}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{x}$$
>>
>>for some [real matrix](../../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) $\boldsymbol{A} \in \mathbb{R}^{n \times n}$.
>>
>>Its [Hessian matrix](./Hessian%20Matrix.md) is the following:
>>
>>$$H_f(\boldsymbol{p}) = \boldsymbol{A} + \boldsymbol{A}^{\mathsf{T}}$$
>>
>
>>[!EXAMPLE]- Example: $f(\boldsymbol{x}) = ||\boldsymbol{x}||$
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^n \to \mathbb{R}$ defined as follows:
>>
>>$$f(\boldsymbol{x}) = ||\boldsymbol{x}||$$
>>
>>It is [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^n \setminus \{\boldsymbol{0}\}$ with the following [partial derivatives](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md):
>>
>>$$\partial_{i}f(\boldsymbol{x}) = \frac{x_i}{||\boldsymbol{x}||}$$
>>
>>We thus have:
>>
>>$$\partial_{i}\partial_{i}f(\boldsymbol{x}) = \frac{||\boldsymbol{x}|| - x_i \frac{x_i}{||\boldsymbol{x}||}}{||\boldsymbol{x}||^2} = \frac{1}{||\boldsymbol{x}||} - \frac{x_i^2}{||\boldsymbol{x}||^3}$$
>>
>>$$\partial_{i}\partial_{j} f(\boldsymbol{x}) = -\frac{x_i x_j}{||\boldsymbol{x}||^3} \qquad i \ne j$$
>>
>>For its [Hessian matrix](./Hessian%20Matrix.md), we have:
>>
>>$$H_f(\boldsymbol{x}) = \frac{1}{||\boldsymbol{x}||}I_n - \frac{1}{||\boldsymbol{x}||^3}\boldsymbol{x}\boldsymbol{x}^{\mathsf{T}}$$
>>
>

>[!THEOREM] Theorem: Symmetry of the Hessian Matrix
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\boldsymbol{p} \in \operatorname{int} \mathcal{D}$ be an [interior point](../../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $\mathcal{D}$.
>
>If $f$ is [twice totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$, then its [Hessian matrix](./Hessian%20Matrix.md) there is [symmetric](../../../../Algebra/Matrices/Square%20Matrices/Symmetric%20Matrices.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>
