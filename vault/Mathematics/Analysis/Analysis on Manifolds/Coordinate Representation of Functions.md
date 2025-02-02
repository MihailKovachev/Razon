>[!DEFINITION] Definition: Coordinate Representation of a Function
>
>Let $f: M \to \mathbb{R}^n$ be a [real vector-valued function](Real%20Vector-Valued%20Function.md) on a $k$-[manifold](../../Geometry/Manifolds/Manifolds.md) $M$ and let $(U, \phi)$ be a [chart](../../Geometry/Manifolds/Coordinates/Chart.md) for $M$.
>
>The **coordinate representation** of $f$ on $(U, \phi)$ is the [real vector function](../Real%20Analysis/Real%20Vector%20Functions/Real%20Vector%20Function.md) ${}_{(U, \phi)}f: \phi(U) \subseteq \mathbb{R}^k \to \mathbb{R}^n$ obtained by the [compositions](../Real%20Analysis/Real%20Vector%20Functions/Real%20Vector%20Function.md) of $f$ and the [inverse](../Functions/Types%20of%20Functions/Inverse%20Function.md) of $\phi$.
>
>$$
>{}_{(U, \phi)}f \overset{\text{def}}{=} f \circ \phi^{-1}
>$$
>
>>[!INTUITION]+
>>
>>Although all points on a chart can be uniquely represented by their coordinates, the $f$ does not act on coordinates - it acts on points. Hence, we need a way to convert coordinates to the points they represent before $f$ can be used. This is precisely what $\phi^{-1}$ does. If we are given coordinates $(p^1, \dotsc, p^k)$, we can pass them to $\phi^{-1}$ to obtain the point $p \in U$ which they represent. After having converted the coordinates $(p^1, \dotsc, p^k)$ to the point $p$, we can invoke $f$, i.e. we can obtain the value $f(p)$.
>>
>>The coordinate representation ${}_{(U, \phi)}f$ does all of this in one single step. It takes coordinates $(p^1, \dotsc, p^k)$, converts them to the point $p$ which they represent and then returns the value of $f$ at $p$. 
>>
>