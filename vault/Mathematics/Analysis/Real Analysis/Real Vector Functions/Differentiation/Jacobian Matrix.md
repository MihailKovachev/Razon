---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Jacobian Matrix

>[!DEFINITION] Definition: Jacobian Matrix
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](../Real%20Vector%20Functions.md).
>
>If $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p} \in \mathcal{D}$, then its **Jacobian matrix** at $\boldsymbol{p}$ is the [matrix representation](../../../Functional%20Analysis/Linearity/Linearity%20(Functions).md) of its [total derivative](./Total%20Differentiability%20(Real%20Vector%20Functions).md) there with respect to the [standard bases](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) of $\mathbb{R}^m$ and $\mathbb{R}^n$.
>
>>[!NOTATION]
>>
>>$$Df(\boldsymbol{p}) \qquad J_f(\boldsymbol{p}) \qquad \boldsymbol{J}_f(\boldsymbol{p})$$
>>
>

>[!DEFINITION] Definition: Regularity
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](../Real%20Vector%20Functions.md) and let $\boldsymbol{p}$ be an [interior point](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\boldsymbol{p}$.
>
>We say that $f$ is **regular** if it is [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p}$ and its [Jacobian matrix](./Jacobian%20Matrix.md) there is [invertible](../../../../Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md).
>

>[!THEOREM] Theorem: Jacobian via Partial Derivatives
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](../Real%20Vector%20Functions.md).
>
>If $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p} \in \mathcal{D}$, then its [Jacobian matrix](./Jacobian%20Matrix.md) $J_f(\boldsymbol{p})$ is given by the [partial derivatives](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) of $f$'s [component functions](../Real%20Vector%20Functions.md) $f_1, \dotsc, f_n$ as follows:
>
>$$J_f(\boldsymbol{p}) = \begin{bmatrix}\partial_1 f_1(\boldsymbol{p}) & \cdots & \partial_m f_1(\boldsymbol{p}) \\ \vdots & \ddots & \vdots \\ \partial_1 f_n(\boldsymbol{p}) & \cdots & \partial_m f_n(\boldsymbol{p})\end{bmatrix}$$
>
>>[!EXAMPLE]-
>>
>>Consider the [real vector function](../Real%20Vector%20Functions.md) $f: \mathbb{R}^2 \to \mathbb{R}^3$ defined as follows:
>>
>>$$f\left(x, y\right) = \begin{bmatrix} x^2 y \\ \sin y \\ x^2 + y^2\end{bmatrix}$$
>>
>>It is [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) on $\mathbb{R}^2$ with the following [Jacobian matrix](./Jacobian%20Matrix.md):
>>
>>$$J_f\left(x, y\right) = \begin{bmatrix}2xy & x^2 \\ 0 & \cos y \\ 2x & 2y\end{bmatrix}$$
>>
>
>>[!EXAMPLE]- Example: $f(\boldsymbol{x}) = \boldsymbol{A} \boldsymbol{x}$
>>
>>Consider the [real vector function](../Real%20Vector%20Functions.md) $f: \mathbb{R}^m \to \mathbb{R}^n$ defined as
>>
>>$$f(\boldsymbol{x}) = \boldsymbol{A}\boldsymbol{x}$$
>>
>>for some fixed [real matrix](../../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) $\boldsymbol{A} \in \mathbb{R}^{n\times m}$. It is [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) on $\mathbb{R}^m$ with the following [Jacobian matrix](./Jacobian%20Matrix.md):
>>
>>$$J_f(\boldsymbol{x}) = \boldsymbol{A}$$
>>
>
>>[!EXAMPLE]-
>>
>>Let $f: \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) which is twice [totally differentiable](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Total%20Differentiability%20(Real%20Scalar%20Fields).md).
>>
>>The [Jacobian matrix](./Jacobian%20Matrix.md) of $f$'s [gradient](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Gradient%20(Real%20Scalar%20Fields).md) is $f$'s [Hessian matrix](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Hessian%20Matrix.md):
>>
>>$$J_{\nabla f}(\boldsymbol{x}) = H_f (\boldsymbol{x})$$
>>
>
>>[!EXAMPLE]- Example: Polar Coordinate Transformation
>>
>>Consider the [coordinate transformation](../../Euclidean%20Space/Coordinate%20Transformations.md) $f: [0,+\infty)\times [0, 2\uppi) \to \mathbb{R}^2$ from [polar coordinates](../../Euclidean%20Space/Polar%20Coordinates.md):
>>
>>$$f\left(\rho, \varphi\right) = \begin{bmatrix} \rho \cos \varphi \\ \rho \sin \varphi \end{bmatrix}$$
>>
>>It is [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) on $(0, +\infty) \times (0, 2 \uppi)$ with the following [Jacobian matrix](./Jacobian%20Matrix.md):
>>
>>$$J_f\left(\rho, \varphi\right) = \begin{bmatrix}\cos \varphi & - \rho \sin \varphi \\ \sin \varphi & \rho \cos \varphi\end{bmatrix}$$
>>
>
>>[!EXAMPLE]- Example: Cylindrical Coordinate Transformation
>>
>>Consider the [coordinate transformation](../../Euclidean%20Space/Coordinate%20Transformations.md) $f: [0,+\infty)\times [0, 2\uppi) \times \mathbb{R} \to \mathbb{R}^3$ of [cylindrical coordinates](../../Euclidean%20Space/Cylindrical%20Coordinates.md):
>>
>>$$f\left(\rho, \varphi, z \right) = \begin{bmatrix} \rho \cos \varphi \\ \rho \sin \varphi \\ z\end{bmatrix}$$
>>
>>It is [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) on $(0, +\infty) \times (0, 2 \uppi) \times \mathbb{R}$ with the following [Jacobian matrix](./Jacobian%20Matrix.md):
>>
>>$$J_f\left(\rho, \varphi, z\right) = \begin{bmatrix}\cos \varphi & - \rho \sin \varphi & 0 \\ \sin \varphi & \rho \cos \varphi & 0 \\ 0 & 0 & 1\end{bmatrix}$$
>>
>
>>[!EXAMPLE]- Example: Spherical Coordinate Transformation
>>
>>Consider the [coordinate transformation](../../Euclidean%20Space/Coordinate%20Transformations.md) $f: [0,+\infty)\times [0, \uppi] \times [0, 2\uppi) \to \mathbb{R}^3$ of [spherical coordinates](../../Euclidean%20Space/Spherical%20Coordinates.md):
>>
>>$$f\left(r, \theta, \varphi\right) = \begin{bmatrix} r \sin \theta \cos \varphi \\ r \sin \theta \sin \varphi \\ r \cos \theta\end{bmatrix}$$
>>
>>It is [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) on $(0,+\infty)\times (0, \uppi) \times (0, 2\uppi)$ with the following [Jacobian matrix](./Jacobian%20Matrix.md):
>>
>>$$J_f\left(r, \theta, \varphi\right) = \begin{bmatrix}\sin \theta \cos \varphi & r \cos \theta \cos \varphi & -r \sin \theta \sin \varphi \\ \sin \theta \sin \varphi & r \cos \theta \sin \varphi & r \sin \theta \cos \varphi \\ \cos \theta & - r \sin \theta & 0\end{bmatrix}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Jacobian via Gradients
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](../Real%20Vector%20Functions.md).
>
>If $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p} \in \mathcal{D}$, then the rows of its [Jacobian matrix](./Jacobian%20Matrix.md) $J_f(\boldsymbol{p})$ are the [gradients](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Gradient%20(Real%20Scalar%20Fields).md) of $f$'s [component functions](../Real%20Vector%20Functions.md) $f_1, \dotsc, f_n$:
>
>$$J_f(\boldsymbol{p}) = \begin{bmatrix} - & (\nabla f_1 (\boldsymbol{p}))^\mathsf{T} & - \\ - & \vdots & - \\ - & (\nabla f_n(\boldsymbol{p}))^\mathsf{T} & - \end{bmatrix}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Jacobian of Linear Combination
>
>Let $f:\mathcal{D}_f \subseteq \mathbb{R}^m \to \mathbb{R}^n$ and $g: \mathcal{D}_g \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be [real vector functions](../Real%20Vector%20Functions.md).
>
>If $f$ and $g$ are [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p} \in \mathcal{D}_f \cap \mathcal{D}_g$, then the [Jacobian matrix](./Jacobian%20Matrix.md) of $\lambda f + \mu g$ is given by the [Jacobian matrices](./Jacobian%20Matrix.md) of $f$ and $g$ as
>
>$$J_{\lambda f + \mu g}(\boldsymbol{p}) = \lambda J_{f}(\boldsymbol{p}) + \mu J_g (\boldsymbol{p})$$
>
>for all $\lambda, \mu \in \mathbb{R}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Chain Rule for Jacobian Matrices
>
>Let $g: \mathcal{D}_g \subseteq \mathbb{R}^m \to \mathbb{R}^n$ and $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}^p$ be [real vector functions](../Real%20Vector%20Functions.md).
>
>If $g$ is [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p} \in \mathcal{D}_g$ and $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at $g(\boldsymbol{p}) \in \mathcal{D}_f$, then the [Jacobian matrix](./Jacobian%20Matrix.md) of the [composition](../../../Functions/Functions.md) $f \circ g$ is given by the [matrix product](../../../../Algebra/Matrices/Matrix%20Product.md) of the [Jacobian matrices](./Jacobian%20Matrix.md) of $f$ and $g$ as follows:
>
>$$J_{f \circ g}(\boldsymbol{p}) = J_{f}(g(\boldsymbol{p}))J_g(\boldsymbol{p})$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Product Rule for Jacobian Matrices
>
>Let $f: \mathcal{D}_{f} \subseteq \mathbb{R}^m \to \mathbb{R}$ be a [real scalar field](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $g: \mathcal{D}_{g} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](../Real%20Vector%20Functions.md).
>
>If $f$ and $g$ are [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{x} \in \operatorname{int} (\mathcal{D}_f \cap \mathcal{D}_g)$, then so is $fg$ and with the following [Jacobian matrix](./Jacobian%20Matrix.md):
>
>$$J_{fg}(\boldsymbol{x}) = g(\boldsymbol{x})J_f(\boldsymbol{x}) + f(\boldsymbol{x})J_g (\boldsymbol{x})$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Dot Product Rule for Jacobian Matrices
>
>Let $f: \mathcal{D}_{f} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ and $g: \mathcal{D}_{g} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector functions](../Real%20Vector%20Functions.md).
>
>If $f$ and $g$ are [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{x} \in \operatorname{int} (\mathcal{D}_f \cap \mathcal{D}_g)$, then so is their [dot product](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Dot%20Product.md) $f^{\mathsf{T}}g$ with the following [Jacobian matrix](./Jacobian%20Matrix.md):
>
>$$J_{f^{\mathsf{T}}g}(\boldsymbol{x}) = g(\boldsymbol{x})^{\mathsf{T}}J_f(\boldsymbol{x}) + f(\boldsymbol{x})^{\mathsf{T}}J_g(\boldsymbol{x})$$
>
>>[!PROOF]-
>>
>>Let $f_1, \dotsc, f_n$ and $g_1, \dotsc, g_n$ be the [component functions](../../Real%20Vector-Valued%20Functions.md) of $f$ and $g$, respectively.
>>
>>Let $h: \mathcal{D}_f \cap \mathcal{D}_g \subseteq \mathbb{R}^m \to \mathbb{R}$ be the [dot product](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Dot%20Product.md) $f^{\mathsf{T}}g$:
>>
>>$$h(\boldsymbol{x}) \overset{\text{def}}{=} f^{\mathsf{T}}(\boldsymbol{x}) g(\boldsymbol{x}) = \sum_{i = 1}^n f_i(\boldsymbol{x})g_i(\boldsymbol{x})$$
>>
>>Since $f$ and $g$ are [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{x}$, their [component functions](../../Real%20Vector-Valued%20Functions.md) must be [partially differentiable](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) there. Therefore, so is $h$:
>>
>>$$\begin{aligned}\partial_j h(\boldsymbol{x}) & = \sum_{i = 1}^n \left(\partial_j f_i (\boldsymbol{x})g_i (\boldsymbol{x}) + \partial_j g_i (\boldsymbol{x}) f(\boldsymbol{x})\right) \\ & = \sum_{i = 1}^n \partial_j f_i (\boldsymbol{x})g_i (\boldsymbol{x}) + \sum_{i = 1}^n \partial_j g_i (\boldsymbol{x}) f(\boldsymbol{x})\end{aligned}$$
>>
>>Let $J_h(\boldsymbol{x}) \in \mathbb{R}^{1 \times m}$ be defined using $\partial_j h(\boldsymbol{x})$ as follows:
>>
>>$$\begin{aligned} J_h(\boldsymbol{x}) & \overset{\text{def}}{=} \begin{bmatrix} \partial_1 h(\boldsymbol{x}) & \cdots & \partial_m h(\boldsymbol{x}) \end{bmatrix} \\ & = \begin{bmatrix} \sum_{i = 1}^n (\partial_1 f_i (\boldsymbol{x})g_i (\boldsymbol{x}) + \partial_1 g_i (\boldsymbol{x}) f(\boldsymbol{x})) & \cdots & \sum_{i = 1}^n (\partial_m f_i (\boldsymbol{x})g_i (\boldsymbol{x}) + \partial_m g_i (\boldsymbol{x}) f(\boldsymbol{x})) \end{bmatrix} \end{aligned}$$
>>
>>TODO
>>
>

>[!THEOREM] Mean Value Inequality
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](../Real%20Vector%20Functions.md) and let $\boldsymbol{a}, \boldsymbol{b} \in \mathcal{D}$ such that $L = \{\boldsymbol{a} + t(\boldsymbol{b} - \boldsymbol{a}) \mid t \in [0,1]\} \subseteq \mathcal{D}$.
>
>If $f$ is [continuous](../Continuity%20(Real%20Vector%20Functions).md) on $L$ and [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) on $\operatorname{int} L$, then 
>
>$$||f(\boldsymbol{b}) - f(\boldsymbol{a})|| \le \sup_{\boldsymbol{p} \in \operatorname{int} L} \{||J_f(\boldsymbol{p})||\} \, ||\boldsymbol{b} - \boldsymbol{a}||,$$
>
>where the [matrix norm](../../../../Algebra/Matrices/Matrix%20Norms.md) can be induced by any [vector norms](../../../../Algebra/Vector%20Spaces/Norms.md) on $\mathbb{R}^m$ and $\mathbb{R}^n$.
>
>>[!PROOF]-
>>
>>TODO
>>
>