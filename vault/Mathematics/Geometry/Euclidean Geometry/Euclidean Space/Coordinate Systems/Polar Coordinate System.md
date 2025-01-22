# Polar Coordinate System

Polar coordinates uniquely identify each point in the [Euclidean space](../Euclidean%20Space.md) $\mathbb{R}^2$ by its distance $r$ from the origin and the angle $\theta$ it makes with the $x$-axis.

![](res/Polar%20Coordinates.drawio.svg)

## Conventions

Technically, each point has infinitely many polar coordinates, since adding or substracting a multiple of $2\pi$ to an angle has no effect. However, it is often required that polar coordinates are unique for each point which means that the range of values for $\theta$ needs to be restricted. The most common conventions for the possible values of $\theta$ are $[0;2\pi)$ and $(-\pi; \pi]$.

>[!THEOREM] Theorem: Polar Coordinate System
>
>The [function](../../../../Analysis/Real%20Analysis/Multivariate%20Real%20Analysis/Vector%20Fields/Real%20Vector%20Field.md) $s: \mathbb{R}^2 \to \mathbb{R}^2$ defined for each $\mathbf{p} = \begin{bmatrix} x & y\end{bmatrix}^\mathsf{T} \in \mathbb{R}^2$ as
>
>$$
>s(\mathbf{p}) \overset{\text{def}}{=} (r, \theta)
>$$
>
>where $r \ge 0$, $\theta \in (-\pi; \pi]$ and
>
>$$
>\begin{align*}
>r &= \sqrt{x^2 + y^2} \\
>
>\theta &=
>
>\begin{cases}
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
>\end{cases}
>
>\end{align*}
>$$
>
>is a [global coordinate system](../../../Manifolds/Coordinates/Global%20Coordinate%20System.md) for the [Euclidean space](../Euclidean%20Space.md) $\mathbb{R}^2$.
>
>>[!PROOF]-
>>
>>TODO
>>
>