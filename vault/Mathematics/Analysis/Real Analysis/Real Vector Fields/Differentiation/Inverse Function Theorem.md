---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Inverse Function Theorem

>[!THEOREM] Theorem: Inverse Function Theorem
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}^n$ be a [real vector field](../Real%20Vector%20Fields.md) on an  and let $\boldsymbol{p} \in U$.
>
>If $f$ is [continuously partially differentiable](../../Real%20Vector%20Functions/Differentiation/Partial%20Differentiability%20(Real%20Vector%20Functions).md) on an [open set](../../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) $U \subseteq \mathcal{D}$ and its [Jacobian matrix](../../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md) at $\boldsymbol{p} \in U$ is [invertible](../../../../Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md), then there exists an [open neighborhood](../../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) $V \subseteq U$ of $\boldsymbol{p}$ and an [open neighborhood](../../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) $W \subseteq \mathbb{R}^n$ of $f(\boldsymbol{p})$ such that $f$ is [bijective](../../../Functions/Injections,%20Surjections%20and%20Bijections.md) between $V$ and $W$. Furthermore, its [inverse](../../../Functions/Injections,%20Surjections%20and%20Bijections.md) $f^{-1}$ on $W$ is [continuously partially differentiable](../../Real%20Vector%20Functions/Differentiation/Partial%20Differentiability%20(Real%20Vector%20Functions).md) on $W$ and its [Jacobian matrix](../../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md) is the [inverse](../../../../Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md) of $f$'s [Jacobian matrix](../../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md):
>
>$$J_{f^{-1}} (\boldsymbol{y}) = J_{f} (f^{-1}(\boldsymbol{y}))^{-1} \qquad \forall \boldsymbol{y} \in W$$
>
>>[!EXAMPLE]- Example:
>>
>>Consider the [coordinate transformation](../../Euclidean%20Space/Coordinate%20Transformations.md) $\mathcal{T}: [0, +\infty) \times [0, 2\uppi) \to \mathbb{R}^2$ from [polar coordinates](../../Euclidean%20Space/Polar%20Coordinates.md):
>>
>>$$\mathcal{T}(\rho, \varphi) = \begin{bmatrix}\rho \cos \varphi \\ \rho \sin \varphi\end{bmatrix}$$
>>
>>It is [continuously partially differentiable](../../Real%20Vector%20Functions/Differentiation/Partial%20Differentiability%20(Real%20Vector%20Functions).md) on $(0, +\infty) \times (0, 2\uppi)$ with the following [Jacobian matrix](../../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md):
>>
>>$$J_{\mathcal{T}}(\rho, \varphi) = \begin{bmatrix}\cos \varphi & - \rho \sin \varphi \\ \sin \varphi & \rho \cos \varphi\end{bmatrix}$$
>>
>>The [determinant](../../../../Algebra/Matrices/Square%20Matrices/Determinants.md) is
>>
>>$$\det J_{\mathcal{T}}(\rho, \varphi) = \rho \cos^2 \varphi + \rho \sin^2 \varphi = \rho$$
>>
>>which is non-zero, since $\rho \ne 0$. Therefore, for each $(\rho, \varphi) \in (0, +\infty) \times (0, 2\uppi)$, there exist an [open neighborhood](../../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) $V \subseteq (0, +\infty) \times (0, 2\uppi)$ of $(\rho, \varphi)$ and an [open neighborhood](../../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) $W \subseteq \mathbb{R}^2$ such that $\mathcal{T}$ is [bijective](../../../Functions/Injections,%20Surjections%20and%20Bijections.md) between $V$ and $W$. Furthermore, we have:
>>
>>$$J_{\mathcal{T}^{-1}}(\mathcal{T}(\rho, \varphi)) = J_{\mathcal{T}} (\rho, \varphi)^{-1} = \begin{bmatrix} \cos \varphi & \sin \varphi \\ -\frac{\sin \varphi}{\rho} & \frac{\cos \varphi}{\rho} \end{bmatrix}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>