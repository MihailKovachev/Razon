>[!DEFINITION] Definition: Riemann Sum
>Let $f: D \to \mathbb{R}$ be a [real function](../../../Real%20Functions/Real%20Function.md) on a [closed interval](../../../../../Set%20Theory/Ordering/Intervals.md) $D = [a;b] \subset \mathbb{R}$ and let $x_0 \lt x_1 \lt \cdots \lt x_n \in D$.
>
>A **Riemann sum** of $f$ over $D$ is any sum of the form
>
>$$\sum_{i = 1}^n f(x_i^\ast) \Delta x_i,$$
>
>where $\Delta x_i = (x_i - x_{i-1})$ and $x_i^\ast \in [x_{i-1};x_i]$.
>
>>[!NOTE] Note: Choice of $x_i^\ast$
>>
>>Different choices for $x_i^\ast$ yield different Riemann sums.
>
>>[!DEFINITION]- Definition: Left Riemann Sum
>>A **left Riemann sum** has $x_i^\ast = x_{i-1}$ for all $i$.
>>
>
>>[!DEFINITION]- Definition: Right Riemann Sum
>>A **right Riemann sum** has $x_i^\ast = x_{i}$ for all $i$.
>>
>
>>[!DEFINITION]- Definition: Left Riemann Sum
>>A **middle Riemann sum** has $\displaystyle x_i^\ast = \frac{x_{i-1} + x_i}{2}$ for all $i$.