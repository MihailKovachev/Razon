# Spherical Coordinates

Each vector (point) $P$ in the 3-dimensional [Euclidean space](../Euclidean%20Space.md) $\mathbb{R}^3$ can be uniquely identified using its magnitude $r$ (distance from the origin), the angle $\theta$ it makes with the $z$-axis and the angle $\phi$ its projection in the $xy$ plane makes with the $x$-axis.

![](res/Spherical%20Coordinates.drawio.svg)

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
>The number $\phi$ is known as the **azimuth** or **azimuthal angle**.
>

## Conventions

The radial distance can be denoted either by $r$ or $\rho$. Some people also switch $\theta$ and $\phi$ around, using the former for the azimuthal angle and the latter for the polar angle. 

>[!NOTE]- Note: Elevation
>
>Instead of inclination, some people prefer to use **elevation**. This is the angle between the point and the $xy$-plane and is equal to $\frac{\pi}{2}$ minus the inclination.
>

### Value Ranges

If the range of values for the angles is not restricted, then every point has infinitely many different spherical coordinates because adding or substracting an integer multiple of $2\pi$ to an angle does not change the point it correaponds to. However, using the formalism of [coordinate systems](../../../Manifolds/Coordinates/Coordinate%20System.md) requires that coordinates are always unique. To guarantee this, the set of possible values for the angles needs to be restricted.

Most commonly, the following conventions are used:

|Coordinate|Range|
|:--:|:--:|
|$r$|$[0; \infty)$|
|$\theta$|$[0; \pi]$|
|$\phi$|$[0; 2\pi)$|

>[!THEOREM] Theorem: Spherical Coordinate System
>
>The [function](../../../../Analysis/Real%20Analysis/Multivariate%20Real%20Analysis/Vector%20Fields/Real%20Vector%20Field.md) $s: \mathbb{R}^3 \to \mathbb{R}^3$ defined for each $\mathbf{p} = \begin{bmatrix}x & y & z\end{bmatrix}^\mathsf{T} \in \mathbb{R}^n$ as 
>
>$$
>s(\mathbf{p}) \overset{\text{def}}{=} (r, \theta, \phi) 
>$$
>
>where
>
>$$
>\begin{align*}
>
>r &= \sqrt{x^2 + y^2 + z^2} \in [0; \infty) \\
>
>\theta &= \arccos \frac{z}{\sqrt{x^2 + y^2 + z^2}} \in [0; \pi] \\
>
>\phi &= \operatorname{sgn}(y) \arccos \frac{x}{\sqrt{x^2 + y^2}} \in [0; 2\pi)
>
>\end{align*}
>$$
>
>is a [global coordinate system](../../../Manifolds/Coordinates/Global%20Coordinate%20System.md) for $\mathbb{R}^3$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
