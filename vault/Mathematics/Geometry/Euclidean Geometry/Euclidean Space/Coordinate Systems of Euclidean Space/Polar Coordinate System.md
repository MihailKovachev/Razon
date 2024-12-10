>[!THEOREM] Theorem: Polar Coordinate System
>
>The [function](../../../../Analysis/Real%20Analysis/Multivariate%20Real%20Analysis/Real%20Vector%20Functions/Real%20Vector%20Function.md) $\phi: \mathbb{R}^2 \to \mathbb{R}^2$ defined as $p \to (r, \theta)$ where
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
>for every [point](../../Points%20and%20Vectors/Points%20vs%20Vectors.md) $p = \begin{bmatrix}x \\ y\end{bmatrix} \in \mathbb{R}^2$ is a [global coordinate system](../../../Manifolds/Coordinates/Global%20Coordinate%20System.md) for the [Euclidean space](../Euclidean%20Space.md) $\mathbb{R}^2$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!INTUITION]-
>>
>>Polar coordinates specify each point in $\mathbb{R}^2$ by its distance $r$ from the origin and the angle $\theta$ it makes with the positive x-axis.
>>
>>![Polar Coordinate System](res/Polar%20Coordinate%20System.jpg)
>>
>
>>[!NOTE]- Note: Polar Coordinates of the Origin
>>
>>The way we have defined the polar coordinate system entails that the polar coordinates of the origin are $r = 0$ and $\theta = 0$. However, the origin is the only point whose distance from the origin is $0$. This means that the value of $\theta$ is irrelevant when $r = 0$. Nevertheless, defining the coordinates of the origin to be $r = 0$, $\theta = 0$ is a useful convention which fits into the topological formalism of coordinates.
>>
>