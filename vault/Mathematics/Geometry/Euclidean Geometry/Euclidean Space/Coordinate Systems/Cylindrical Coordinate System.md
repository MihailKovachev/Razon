# Cylindrical Coordinate System

Cylindrical coordinates are a natural extension of the [polar coordinate system](Polar%20Coordinate%20System.md) to three dimensions. They identify each point in the [Euclidean space](../Euclidean%20Space.md) $\mathbb{R}^3$ by its distance from the $z$-axis, the angle $\phi$ its projection in the $xy$-plane makes with the $x$-axis and its $z$ component.

![](res/Cylindrical%20Coordinates.drawio.svg)

>[!DEFINITION] Definition: Radial Distance
>
>The number $\rho$ is known as the **radial distance**.
>
>>[!WARNING]
>>
>>This is not the same as the radial distance used in [spherical coordinates](Spherical%20Coordinate%20System.md).
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

## Conventions

Some people prefer to use $\theta$ or $\varphi$ for the azimuth.

Additionally, a single point has infinitely many possible values for its azimuth, since adding or subtracting a multiple of $2\pi$ to an angle has no effect. To use the formalism of coordinate systems and insure uniqueness of the azimuthal angle for each point, however, one needs to restricts the possible values for it. Common conventions are for the range of $\phi$ are $[0; 2\pi)$ and $(-\pi, \pi]$.

>[!THEOREM] Theorem: Cylindrical Coordinate System
>
>The [function](../../../../Analysis/Real%20Analysis/Multivariate%20Real%20Analysis/Vector%20Fields/Real%20Vector%20Field.md) $s: \mathbb{R}^3 \to \mathbb{R}^3$ defined for each $\mathbf{p} = \begin{bmatrix}x & y & z\end{bmatrix}^\mathsf{T} \in \mathbb{R}^n$ as 
>
>$$
>s(\mathbf{p}) \overset{\text{def}}{=} (\rho, \phi, z) 
>$$
>
>where
>
>$$
>\begin{align*}
>\rho &= \sqrt{x^2 + y^2} \\
>
>\phi &= \begin{cases}
>
>\arctan \left( \frac{y}{x} \right) \qquad \qquad \text{if } x \gt 0 \\
>
>\arctan \left( \frac{y}{x} \right) + \pi \qquad \text{ if } x \lt 0, y \ge 0 \\
>
>\arctan \left( \frac{y}{x} \right) - \pi \qquad \text{ if } x \lt 0, y \lt 0 \\
>
>\frac{\pi}{2} \qquad \qquad \qquad \qquad \text{if } x = 0, y \gt 0 \\
>
>-\frac{\pi}{2} \qquad \qquad \qquad \, \, \, \, \, \, \text{ if } x = 0, y \lt 0 \\
>
>0 \qquad \qquad \qquad \qquad \, \text{ if } x = y = 0 
>
>\end{cases} \in (-\pi; \pi] \\
>
>z &= z
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