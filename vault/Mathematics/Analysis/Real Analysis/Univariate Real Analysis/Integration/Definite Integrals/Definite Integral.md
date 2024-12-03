>[!DEFINITION] Definition: Definite Integral
>
>Let $f: D \to \mathbb{R}$ be a [Riemann-integrable](Riemann-integrability.md) [real function](../../Real%20Functions/Real%20Function.md) on a [closed interval](../../../../../Set%20Theory/Ordering/Intervals.md) $D = [a;b] \subset \mathbb{R}$.
>
>The **definite integral** of $f$ is the [limit](../../Real%20Functions/Limits%20of%20Functions/Real%20Limits%20of%20a%20Function.md) of its [Riemann sums](Riemann%20Sum.md).
>
>$$
>\lim_{\Delta x_i\to 0}\sum_{i=1}^n f(x_i^\ast)\Delta x_i
>$$
>
>>[!NOTATION]-
>>
>>$$
>>\int_a^b f(x) \mathop{\mathrm{d}x} \qquad \int_a^b f
>>$$
>>
>
>>[!INTUITION]- Intuition: Geometric Meaning of the Definite Integral
>>
>>The definite integral of $f$ gives us the *signed* are between the $x$-axis and the graph of $f$ from $a$ to $b$ - areas above the $x$-axis are positive and areas below it are negative.
>>
>>![Definite Integral](Resources/Definite%20Integral.png)
>