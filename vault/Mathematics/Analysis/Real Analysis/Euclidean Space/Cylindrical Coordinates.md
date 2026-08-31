---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - geometry
    - mathematics
---

# Cylindrical Coordinates

Cylindrical coordinates are a natural extension of the [Polar Coordinates](./Polar%20Coordinates.md) to three dimensions. They identify each point in the [Euclidean space](./Euclidean%20Space.md) $\mathbb{R}^3$ by its distance from the $z$-axis, the angle $\phi$ its projection in the $xy$-plane makes with the $x$-axis and its $z$ component.

![](../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Coordinate%20Systems/res/Cylindrical%20Coordinates.drawio.svg)

>[!DEFINITION] Definition: Radial Distance
>
>The number $\rho$ is known as the **radial distance**.
>
>>[!WARNING]
>>
>>This is not the same as the radial distance used in [spherical coordinates](./Spherical%20Coordinates.md).
>>
>

>[!DEFINITION] Definition: Azimuthal Angle (Azimuth)
>
>The number $\phi$ is known as the **azimuthal angle** or **azimuth**.
>

>[!DEFINITION] Definition: Axial Coordinate (Height)
>
>The number $z$ is known as the **axial coordinate** or **height**. 
>
>>[!NOTE]
>>
>>Despite the word "height", the axial coordinate's algebraic sign is crucial.
>>
>

>[!THEOREM] Theorem: Local Coordinate Basis of Cylindrical Coordinates
>
>Let $\tau: (0, +\infty) \times (0, 2\uppi) \times \mathbb{R} \to \mathbb{R}^3$ be the [transition map](../../../Geometry/Manifolds/Coordinate%20Systems/Transition%20Maps.md) from [cylindrical coordinates](./Cylindrical%20Coordinates.md) to [Cartesian coordinates](./Cartesian%20Coordinate%20System.md).
>
>Its [normalized local coordinate basis](./Local%20Coordinate%20Bases.md) at $(\rho, \varphi, z)$ is the following:
>
>$$\boldsymbol{\hat{\rho}} = \begin{bmatrix}\cos \varphi \\ \sin \varphi \\ 0\end{bmatrix} \qquad \boldsymbol{\hat{\varphi}} = \begin{bmatrix}-\sin \varphi \\ \cos \varphi \\ 0\end{bmatrix} \qquad \boldsymbol{\hat{z}} = \begin{bmatrix}0 \\ 0 \\ 1\end{bmatrix}$$
>
>>[!PROOF]-
>>
>>We have the following by definition:
>>
>>$$\tau\left(\begin{bmatrix}\rho \\ \varphi \\ z \end{bmatrix}\right) = \begin{bmatrix} \rho \cos \varphi \\ \rho \sin \varphi \\ z \end{bmatrix}$$
>>
>>We see that $\tau$ is [totally differentiable](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Total%20Differentiability%20(Real%20Scalar%20Fields).md) on $(0, +\infty) \times (0, 2\uppi) \times \mathbb{R}$ with the following [Jacobian matrix](../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md):
>>
>>$$J_{\tau}\left(\begin{bmatrix}\rho \\ \varphi \\ z \end{bmatrix}\right) = \begin{bmatrix}\cos \varphi & -\rho \sin \varphi & 0 \\ \sin \varphi & \rho \cos \varphi & 0 \\ 0 & 0 & 1\end{bmatrix}$$
>>
>>For the [determinant](../../../Algebra/Matrices/Square%20Matrices/Determinants.md), we have:
>>
>>$$\det J_{\tau}\left(\begin{bmatrix}\rho \\ \varphi \\ z \end{bmatrix}\right) = 1 \cdot (\rho \cos^2 \varphi + \rho \sin^2 \varphi) = \rho$$
>>
>>Since $\rho \ne 0$, we know that the columns of $J_{\tau}$ form a [local coordinate basis](./Local%20Coordinate%20Bases.md):
>>
>>$$\boldsymbol{\rho} = \begin{bmatrix}\cos \varphi \\ \sin \varphi \\ 0\end{bmatrix} \qquad \boldsymbol{\varphi} = \begin{bmatrix}-\rho \sin \varphi \\ \rho \cos \varphi \\ 0\end{bmatrix} \qquad \boldsymbol{z} = \begin{bmatrix}0 \\ 0 \\ 1\end{bmatrix}$$
>>
>>We just need to normalize them:
>>
>>$$\boldsymbol{\hat{\rho}} = \begin{bmatrix}\cos \varphi \\ \sin \varphi \\ 0\end{bmatrix} \qquad \boldsymbol{\hat{\varphi}} = \begin{bmatrix}-\sin \varphi \\ \cos \varphi \\ 0\end{bmatrix} \qquad \boldsymbol{\hat{z}} = \begin{bmatrix}0 \\ 0 \\ 1\end{bmatrix}$$
>>
>


## Conventions

Some people prefer to use $\theta$ or $\varphi$ for the azimuth.

Additionally, a single point has infinitely many possible values for its azimuth, since adding or subtracting a multiple of $2\pi$ to an angle has no effect. However, in order to have a [coordinate system](../../../../index.md), coordinates must be unique. This means that the possible values for $\phi$ must be restricted. Common conventions for the range of $\phi$ are $[0; 2\pi)$ and $(-\pi, \pi]$.