---
tags:
    - real-analysis
    - analysis
    - mathematics
---

# Polar Coordinates

>[!THEOREM] Theorem: Polar Coordinate Transformation
>
>A [polar coordinates](./Polar%20Coordinates.md)
>
>>[!PROOF]-
>>
>>TODO
>>
>

**Polar coordinates** are a way to identify [vectors](../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) in the [Euclidean space](./Euclidean%20Space.md) $\mathbb{R}^2$ based on their magnitude and the angle they make with the $x$-axis:

![Polar Coordinates](./res/Polar%20Coordinates.svg)

Convention $\varphi \in [0, 2\pi)$:

$$\rho(\boldsymbol{p}) = \sqrt{p_1^2 + p_2^2}$$

$$\varphi(\boldsymbol{p}) = \begin{cases}\arccos \left(\frac{p_1}{||\boldsymbol{p}||}\right) & \text{if} & p_2 \ge 0 \\ 2\uppi - \left(\arccos \frac{p_1}{||\boldsymbol{p}||}\right) & \text{if} & p_2 \lt 0\end{cases}$$

$$\boldsymbol{p} = \begin{bmatrix} \rho \cos \varphi \\ \rho \sin \varphi \end{bmatrix}$$

>[!THEOREM] Theorem: Local Coordinate Basis of Polar Coordinates
>
>Let $\tau: (0, +\infty) \times (0, 2\uppi) \to \mathbb{R}^2$ be the [transition map](../../../Geometry/Manifolds/Coordinate%20Systems/Transition%20Maps.md) from [polar coordinates](./Polar%20Coordinates.md) to [Cartesian coordinates](./Cartesian%20Coordinate%20System.md).
>
>Its [normalized local coordinate basis](./Local%20Coordinate%20Bases.md) at $(\rho, \varphi)$ is the following:
>
>$$\boldsymbol{\hat{\rho}} = \begin{bmatrix}\cos \varphi \\ \sin \varphi\end{bmatrix} \qquad \boldsymbol{\hat{\varphi}} = \begin{bmatrix}-\sin \varphi \\ \cos \varphi\end{bmatrix}$$
>
>>[!PROOF]-
>>
>>We have the following by definition:
>>
>>$$\tau\left(\begin{bmatrix}\rho \\ \varphi \end{bmatrix}\right) = \begin{bmatrix} \rho \cos \varphi \\ \rho \sin \varphi \end{bmatrix}$$
>>
>>We see that $\tau$ is [totally differentiable](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Total%20Differentiability%20(Real%20Scalar%20Fields).md) on $(0, +\infty) \times (0, 2\uppi)$ with the following [Jacobian matrix](../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md):
>>
>>$$J_{\tau}\left(\begin{bmatrix}\rho \\ \varphi \end{bmatrix}\right) = \begin{bmatrix}\cos \varphi & -\rho \sin \varphi \\ \sin \varphi & \rho \cos \varphi\end{bmatrix}$$
>>
>>For the [determinant](../../../Algebra/Matrices/Square%20Matrices/Determinants.md), we have:
>>
>>$$\det J_{\tau}\left(\begin{bmatrix}\rho \\ \varphi \end{bmatrix}\right) = \rho \cos^2 \varphi + \rho \sin^2 \varphi = \rho$$
>>
>>Since $\rho \ne 0$, we know that the columns of $J_{\tau}$ form a [local coordinate basis](./Local%20Coordinate%20Bases.md):
>>
>>$$\boldsymbol{\rho} = \begin{bmatrix}\cos \varphi \\ \sin \varphi\end{bmatrix} \qquad \boldsymbol{\varphi} = \begin{bmatrix}-\rho \sin \varphi \\ \rho \cos \varphi\end{bmatrix} $$
>>
>>We just need to normalize them:
>>
>>$$\boldsymbol{\hat{\rho}} = \begin{bmatrix}\cos \varphi \\ \sin \varphi\end{bmatrix} \qquad \boldsymbol{\hat{\varphi}} = \begin{bmatrix}-\sin \varphi \\ \cos \varphi\end{bmatrix}$$
>>
>

## Conventions

Technically, each point has infinitely many polar coordinates, since adding or substracting a multiple of $2\pi$ to an angle has no effect. However, in order to have a [coordinate system](../../../../index.md), coordinates must be unique which means that the range of values for $\varphi$ needs to be restricted. The most common conventions for the possible values of $\varphi$ are $[0;2\pi)$ and $(-\pi; \pi]$.
