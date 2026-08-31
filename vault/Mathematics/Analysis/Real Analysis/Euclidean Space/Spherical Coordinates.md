---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - geometry
    - mathematics
---

# Spherical Coordinates

Each vector (point) $P$ in the 3-dimensional [Euclidean space](./Euclidean%20Space.md) $\mathbb{R}^3$ can be uniquely identified using its magnitude $r$ (distance from the origin), the angle $\theta$ it makes with the $z$-axis and the angle $\varphi$ its projection in the $xy$ plane makes with the $x$-axis.

![](../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Coordinate%20Systems/res/Spherical%20Coordinates.drawio.svg)

>[!DEFINITION] Definition: Radial Distance (Radius)
>
>The number $r$ is known as **radial distance** or **radius**.
>

>[!DEFINITION] Definition: Inclination (Polar Angle)
>
>The number $\theta$ is known as the **inclination** or **polar angle**.
>

>[!DEFINITION] Definition: Azimuth (Azimuthal Angle)
>
>The number $\varphi$ is known as the **azimuth** or **azimuthal angle**.
>

>[!THEOREM] Theorem: Local Coordinate Basis of Spherical Coordinates
>
>Let $\tau: (0, +\infty) \times (0, \uppi) \times (0, 2\uppi) \to \mathbb{R}^3$ be the [transition map](../../../Geometry/Manifolds/Coordinate%20Systems/Transition%20Maps.md) from [spherical coordinates](./Spherical%20Coordinates.md) to [Cartesian coordinates](./Cartesian%20Coordinate%20System.md).
>
>Its [normalized local coordinate basis](./Local%20Coordinate%20Bases.md) at $(r, \theta, \varphi)$ is the following:
>
>$$\boldsymbol{\hat{r}} = \begin{bmatrix}\sin \theta \cos \varphi \\ \sin \theta \sin \varphi \\ \cos \theta\end{bmatrix} \qquad \boldsymbol{\hat{\theta}} = \begin{bmatrix}\cos \theta \cos \varphi \\ \cos \theta \sin \varphi \\ -\sin \theta\end{bmatrix} \qquad \boldsymbol{\hat{\varphi}} = \begin{bmatrix}-\sin \varphi \\ \cos \varphi \\ 0\end{bmatrix}$$
>
>>[!PROOF]-
>>
>>We have the following by definition:
>>
>>$$\tau\left(\begin{bmatrix}r \\ \theta \\ \varphi \end{bmatrix}\right) = \begin{bmatrix} r \sin \theta \cos \varphi \\ r \sin \theta \sin \varphi \\ r \cos \theta \end{bmatrix}$$
>>
>>We see that $\tau$ is [totally differentiable](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Total%20Differentiability%20(Real%20Scalar%20Fields).md) on $(0, +\infty) \times (0, \uppi) \times (0, 2\uppi)$ with the following [Jacobian matrix](../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md):
>>
>>$$J_{\tau}\left(\begin{bmatrix}r \\ \theta \\ \varphi \end{bmatrix}\right) = \begin{bmatrix}\sin \theta \cos \varphi & r \cos \theta \cos \varphi & -r \sin \theta \sin \varphi \\ \sin \theta \sin \varphi & r \cos \theta \sin \varphi & r \sin \theta \cos \varphi \\ \cos \theta & -r \sin \theta & 0\end{bmatrix}$$
>>
>>For the [determinant](../../../Algebra/Matrices/Square%20Matrices/Determinants.md), we have:
>>
>>$$\det J_{\tau}\left(\begin{bmatrix}r \\ \theta \\ \varphi \end{bmatrix}\right) = r^2 \sin \theta \cos^2 \theta + r^2 \sin^3 \theta = r^2 \sin \theta$$
>>
>>Since $r^2 \sin \theta \ne 0$, we know that the columns of $J_{\tau}$ form a [local coordinate basis](./Local%20Coordinate%20Bases.md):
>>
>>$$\boldsymbol{r} = \begin{bmatrix}\sin \theta \cos \varphi \\ \sin \theta \sin \varphi \\ \cos \theta\end{bmatrix} \qquad \boldsymbol{\theta} = \begin{bmatrix}r \cos \theta \cos \varphi \\ r \cos \theta \sin \varphi \\ -r \sin \theta\end{bmatrix} \qquad \boldsymbol{\varphi} = \begin{bmatrix}-r \sin \theta \sin \varphi \\ r \sin \theta \cos \varphi \\ 0\end{bmatrix}$$
>>
>>We just need to normalize them:
>>
>>$$\boldsymbol{\hat{r}} = \begin{bmatrix}\sin \theta \cos \varphi \\ \sin \theta \sin \varphi \\ \cos \theta\end{bmatrix} \qquad \boldsymbol{\hat{\theta}} = \begin{bmatrix}\cos \theta \cos \varphi \\ \cos \theta \sin \varphi \\ -\sin \theta\end{bmatrix} \qquad \boldsymbol{\hat{\varphi}} = \begin{bmatrix}-\sin \varphi \\ \cos \varphi \\ 0\end{bmatrix}$$
>>
>


## Conventions

The radial distance can be denoted either by $r$ or $\rho$. Some people also switch $\theta$ and $\varphi$ around, using the former for the azimuthal angle and the latter for the polar angle. 

>[!NOTE]- Note: Elevation
>
>Instead of inclination, some people prefer to use **elevation**. This is the angle between the point and the $xy$-plane and is equal to $\frac{\pi}{2}$ minus the inclination.
>

If the range of values for the angles is not restricted, then every point has infinitely many different spherical coordinates because adding or subtracting an integer multiple of $2\pi$ to an angle does not change the point it corresponds to. However, in order to have a [coordinate system](../../../../index.md), coordinates must be unique. To guarantee this, the set of possible values for the angles needs to be restricted. Two of the most common conventions are $\theta \in [0;\pi]$, $\varphi \in [0; 2\pi)$ and $\theta \in [0;\pi]$, $\varphi \in (-\pi; \pi]$.