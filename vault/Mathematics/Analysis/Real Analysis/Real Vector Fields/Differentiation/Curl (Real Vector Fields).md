---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Curl (Real Vector Fields)

>[!DEFINITION]
>
>TODO
>
>>[!NOTATION]
>>
>>$$\operatorname{curl} f(\boldsymbol{p}) \qquad \operatorname{rot} f(\boldsymbol{p}) \qquad \nabla \times f(\boldsymbol{p})$$
>>
>

>[!THEOREM] Theorem: Curl in Cartesian Coordinates
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [real vector field](../Real%20Vector%20Fields.md).
>
>If $f$ is [totally differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p} \in \operatorname{int} \mathcal{D}$, then its [curl](./Curl%20(Real%20Vector%20Fields).md) is given the [partial derivatives](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) of its [component functions](../../Real%20Vector%20Functions/Real%20Vector%20Functions.md) $f_1,f_2, f_3$ as follows:
>
>$$\operatorname{curl} f(\boldsymbol{p}) = \begin{bmatrix} \partial_2 f_3(\boldsymbol{p}) - \partial_3 f_2(\boldsymbol{p}) \\ \partial_3 f_1(\boldsymbol{p}) - \partial_1 f_3(\boldsymbol{p}) \\ \partial_1 f_2(\boldsymbol{p}) - \partial_2 f_1(\boldsymbol{p})\end{bmatrix}$$
>
>>[!EXAMPLE]- Example: $F(x,y,z) = \begin{bmatrix}xy & y^2 & xz\end{bmatrix}$
>>
>>Consider the [real vector field](../Real%20Vector%20Fields.md) $F: \mathbb{R}^3 \to \mathbb{R}^3$ defined as follows:
>>
>>$$F(x,y,z) = \begin{bmatrix}xy \\ y^2 \\ xz\end{bmatrix}$$
>>
>>It is [totally differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) on $\mathbb{R}^3$ and its [curl](./Curl%20(Real%20Vector%20Fields).md) is given by the [partial derivatives](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) of its [component functions](../../Real%20Vector%20Functions/Real%20Vector%20Functions.md) as follows:
>>
>>
>>$$\begin{aligned}\operatorname{curl} F(x,y,z) & = \begin{bmatrix}\partial_y (xz) - \partial_z(y^2) \\ \partial_z (xy) - \partial_x (xz) \\ \partial_x (y^2) - \partial_y (xy)\end{bmatrix} \\ & = \begin{bmatrix} 0 - 0 \\ 0 - z \\ 0 - x\end{bmatrix} \\ & = \begin{bmatrix}0 \\ -z \\ -x\end{bmatrix}\end{aligned}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Curl in Cylindrical Coordinates
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [real vector field](../Real%20Vector%20Fields.md) and let $\mathcal{T}: (0, +\infty) \times (0, 2\uppi) \times \mathbb{R} \to \mathbb{R}^3$ be the [coordinate transformation](../../Euclidean%20Space/Coordinate%20Transformations.md) from [cylindrical coordinates](../../Euclidean%20Space/Cylindrical%20Coordinates.md):
>
>$$\mathcal{T}(\rho, \varphi, z) = \begin{bmatrix}\rho \cos \varphi \\ \rho \sin \varphi \\ z\end{bmatrix}$$
>
>Let $\tilde{f}$ be the [cylindrical coordinate representation](../Cylindrical%20Coordinate%20Representations%20(Real%20Vector%20Fields).md) of $f$:
>
>$$\tilde{f}(\rho, \varphi, z) = \begin{bmatrix}\cos \varphi & \sin \varphi & 0 \\ - \sin \varphi & \cos \varphi & 0 \\ 0 & 0 & 1 \end{bmatrix} (f \circ \mathcal{T})(\rho, \varphi, z)$$
>
>If $f$ is [totally differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\mathcal{T}(\rho, \varphi, z)$, then the [coordinate vector](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) of its [curl](./Curl%20(Real%20Vector%20Fields).md) at $\mathcal{T}(\rho, \varphi, z)$  in the [local coordinate basis](../../Euclidean%20Space/Local%20Coordinate%20Bases.md) of [cylindrical coordinate](../../Euclidean%20Space/Cylindrical%20Coordinates.md) is expressed using [partial derivatives](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) and $\tilde{f}$'s [component functions](../../Real%20Vector-Valued%20Functions.md) $\tilde{f}_1, \tilde{f}_2, \tilde{f}_3$ as follows:
>
>$$[(\operatorname{curl} f)(\mathcal{T}(\rho, \varphi, z))]_{(\boldsymbol{\hat{\rho}}, \boldsymbol{\hat{\varphi}}, \boldsymbol{\hat{z}})} = \begin{bmatrix} \frac{1}{\rho} \partial_\varphi \tilde{f}_3 (\rho, \varphi, z) - \partial_z \tilde{f}_2 (\rho, \varphi, z) \\ \partial_z \tilde{f}_1 (\rho, \varphi, z) - \partial_\rho \tilde{f}_3 (\rho, \varphi, z) \\ \frac{1}{\rho} \partial_\rho (\rho \tilde{f}_2) (\rho, \varphi, z) - \frac{1}{\rho} \partial_\varphi \tilde{f}_1 (\rho, \varphi, z) \end{bmatrix}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Curl in Spherical Coordinates
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [real vector field](../Real%20Vector%20Fields.md) and let $\mathcal{T}: (0, +\infty) \times (0, \uppi) \times (0, 2\uppi) \to \mathbb{R}^3$ be the [coordinate transformation](../../Euclidean%20Space/Coordinate%20Transformations.md) from [spherical coordinates](../../Euclidean%20Space/Spherical%20Coordinates.md):
>
>$$\mathcal{T}(r, \theta, \varphi) = \begin{bmatrix} r \sin \theta \cos \varphi \\ r \sin \theta \sin \varphi \\ r \cos \theta \end{bmatrix}$$
>
>Let $\tilde{f}$ be the [spherical coordinate representation](../Spherical%20Coordinate%20Representations%20(Real%20Vector%20Fields).md) of $f$:
>
>$$\tilde{f}(r, \theta, \varphi) = \begin{bmatrix} \sin \theta \cos \varphi & \sin \theta \sin \varphi & \cos \theta \\ \cos \theta \cos \varphi & \cos \theta \sin \varphi & - \sin \theta \\ - \sin \varphi & \cos \varphi & 0 \end{bmatrix} (f \circ \mathcal{T})(r, \theta, \varphi)$$
>
>If $f$ is [totally differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\mathcal{T}(r, \theta, \varphi)$, then the [coordinate vector](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) of its [curl](./Curl%20(Real%20Vector%20Fields).md) at $\mathcal{T}(r, \theta, \varphi)$ in the [local coordinate basis](../../Euclidean%20Space/Local%20Coordinate%20Bases.md) of [spherical coordinates](../../Euclidean%20Space/Spherical%20Coordinates.md) is expressed using [partial derivatives](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) and $\tilde{f}$'s [component functions](../../Real%20Vector-Valued%20Functions.md) $\tilde{f}_1, \tilde{f}_2, \tilde{f}_3$ as follows:
>
>$$[(\operatorname{curl} f)(\mathcal{T}(r, \theta, \varphi))]_{(\boldsymbol{\hat{r}}, \boldsymbol{\hat{\theta}}, \boldsymbol{\hat{\varphi}})} = \begin{bmatrix} \frac{1}{r \sin \theta} \partial_\theta (\sin \theta \tilde{f}_3) (r, \theta, \varphi) - \frac{1}{r \sin \theta} \partial_\varphi \tilde{f}_2 (r, \theta, \varphi) \\ \frac{1}{r \sin \theta} \partial_\varphi \tilde{f}_1 (r, \theta, \varphi) - \frac{1}{r} \partial_r (r \tilde{f}_3) (r, \theta, \varphi) \\ \frac{1}{r} \partial_r (r \tilde{f}_2) (r, \theta, \varphi) - \frac{1}{r} \partial_\theta \tilde{f}_1 (r, \theta, \varphi) \end{bmatrix}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Divergence of Curl
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [real vector field](../Real%20Vector%20Fields.md).
>
>If $f$ is twice [totally differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{x} \in \operatorname{int} \mathcal{D}$, then the [divergence](./Divergence%20(Real%20Vector%20Fields).md) of its [curl](./Curl%20(Real%20Vector%20Fields).md) there is zero:
>
>$$\operatorname{div} \operatorname{curl} f(\boldsymbol{x}) = 0$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Stoke's Theorem
>
>Let $\phi: \mathcal{D}_{\phi} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ be a [parametric surface](../../Real%20Parametric%20Surfaces/Real%20Parametric%20Surfaces.md) which is [regular](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) except possibly on a [null set](../../../../Measure%20Theory/Null%20Sets.md) of the [Lebesgue measure](../../../../Measure%20Theory/Lebesgue%20Measure.md) such that the [boundary](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\phi(\mathcal{D}_{\phi})$ can be [parameterized](TODO) by a [positively-oriented](TODO) $\partial \phi$
>
>$$\iint_{\phi} \operatorname{curl} f \cdot \mathrm{d}\boldsymbol{\phi} = \int_{\partial \phi} f \cdot \mathrm{d}\boldsymbol{\partial \phi}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Cross Product with Curl
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [real vector field](../Real%20Vector%20Fields.md) and let $\boldsymbol{v} \in \mathbb{R}^3$.
>
>If $f$ is [totally differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{x} \in \operatorname{int} \mathcal{D}$, then the [cross product](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Cross%20Product.md) of its [curl](./Curl%20(Real%20Vector%20Fields).md) and $\boldsymbol{v}$ can be calculated using $f$'s [Jacobian matrix](../../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md) and its [transpose](../../../../Algebra/Matrices/Matrix%20Transposition.md) as follows:
>
>$$\operatorname{curl} f(\boldsymbol{x}) \times \boldsymbol{v} = (\boldsymbol{J}_f(\boldsymbol{x}) - \boldsymbol{J}_f(\boldsymbol{x})^{\mathsf{T}}) \boldsymbol{v}$$
>
>>[!PROOF]-
>>
>>$$f(\boldsymbol{x}) = \begin{bmatrix}f_1(\boldsymbol{x}) \\ f_2 (\boldsymbol{x}) \\ f_3 (\boldsymbol{x})\end{bmatrix} \qquad \boldsymbol{v} = \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix}$$
>>
>>$$\begin{aligned} \operatorname{curl} f(\boldsymbol{x}) \times \boldsymbol{v} & = \begin{bmatrix} \partial_2 f_3(\boldsymbol{x}) - \partial_3 f_2(\boldsymbol{x}) \\ \partial_3 f_1(\boldsymbol{x}) - \partial_1 f_3(\boldsymbol{x}) \\ \partial_1 f_2(\boldsymbol{x}) - \partial_2 f_1(\boldsymbol{x})\end{bmatrix} \times \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix} \\ & = \begin{bmatrix} (\partial_3 f_1(\boldsymbol{x}) - \partial_1 f_3(\boldsymbol{x}))v_3 - (\partial_1 f_2(\boldsymbol{x}) - \partial_2 f_1(\boldsymbol{x}))v_2 \\ (\partial_1 f_2(\boldsymbol{x}) - \partial_2 f_1(\boldsymbol{x}))v_1 - (\partial_2 f_3(\boldsymbol{x}) - \partial_3 f_2(\boldsymbol{x}))v_3 \\ (\partial_2 f_3(\boldsymbol{x}) - \partial_3 f_2(\boldsymbol{x}))v_2 - (\partial_3 f_1(\boldsymbol{x}) - \partial_1 f_3(\boldsymbol{x}))v_1 \end{bmatrix}  \\ & = \begin{bmatrix} (\partial_2 f_1(\boldsymbol{x}) - \partial_1 f_2(\boldsymbol{x})) v_2 + (\partial_3 f_1(\boldsymbol{x}) - \partial_1 f_3(\boldsymbol{x})) v_3 \\ (\partial_1 f_2(\boldsymbol{x}) - \partial_2 f_1(\boldsymbol{x})) v_1 + (\partial_3 f_2(\boldsymbol{x}) - \partial_2 f_3(\boldsymbol{x})) v_3 \\ (\partial_1 f_3(\boldsymbol{x}) - \partial_3 f_1(\boldsymbol{x})) v_1 + (\partial_2 f_3(\boldsymbol{x}) - \partial_3 f_2(\boldsymbol{x})) v_2 \end{bmatrix}\end{aligned}$$
>>
>>$$\begin{aligned} (\boldsymbol{J}_f(\boldsymbol{x}) - \boldsymbol{J}_f(\boldsymbol{x})^{\mathsf{T}}) \boldsymbol{v} & = \left( \begin{bmatrix} \partial_1 f_1(\boldsymbol{x}) & \partial_2 f_1(\boldsymbol{x}) & \partial_3 f_1(\boldsymbol{x}) \\ \partial_1 f_2(\boldsymbol{x}) & \partial_2 f_2(\boldsymbol{x}) & \partial_3 f_2(\boldsymbol{x}) \\ \partial_1 f_3(\boldsymbol{x}) & \partial_2 f_3(\boldsymbol{x}) & \partial_3 f_3(\boldsymbol{x}) \end{bmatrix} - \begin{bmatrix} \partial_1 f_1(\boldsymbol{x}) & \partial_1 f_2(\boldsymbol{x}) & \partial_1 f_3(\boldsymbol{x}) \\ \partial_2 f_1(\boldsymbol{x}) & \partial_2 f_2(\boldsymbol{x}) & \partial_2 f_3(\boldsymbol{x}) \\ \partial_3 f_1(\boldsymbol{x}) & \partial_3 f_2(\boldsymbol{x}) & \partial_3 f_3(\boldsymbol{x}) \end{bmatrix} \right) \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix} \\ & = \begin{bmatrix} 0 & \partial_2 f_1(\boldsymbol{x}) - \partial_1 f_2(\boldsymbol{x}) & \partial_3 f_1(\boldsymbol{x}) - \partial_1 f_3(\boldsymbol{x}) \\ \partial_1 f_2(\boldsymbol{x}) - \partial_2 f_1(\boldsymbol{x}) & 0 & \partial_3 f_2(\boldsymbol{x}) - \partial_2 f_3(\boldsymbol{x}) \\ \partial_1 f_3(\boldsymbol{x}) - \partial_3 f_1(\boldsymbol{x}) & \partial_2 f_3(\boldsymbol{x}) - \partial_3 f_2(\boldsymbol{x}) & 0 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix} \\ & = \begin{bmatrix} (\partial_2 f_1(\boldsymbol{x}) - \partial_1 f_2(\boldsymbol{x})) v_2 + (\partial_3 f_1(\boldsymbol{x}) - \partial_1 f_3(\boldsymbol{x})) v_3 \\ (\partial_1 f_2(\boldsymbol{x}) - \partial_2 f_1(\boldsymbol{x})) v_1 + (\partial_3 f_2(\boldsymbol{x}) - \partial_2 f_3(\boldsymbol{x})) v_3 \\ (\partial_1 f_3(\boldsymbol{x}) - \partial_3 f_1(\boldsymbol{x})) v_1 + (\partial_2 f_3(\boldsymbol{x}) - \partial_3 f_2(\boldsymbol{x})) v_2 \end{bmatrix}\end{aligned}$$
>>
>>
>