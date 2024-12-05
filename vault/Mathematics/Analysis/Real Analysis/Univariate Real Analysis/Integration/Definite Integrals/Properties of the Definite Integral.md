>[!THEOREM] Theorem: Linearity of the Definite Integral
>
>The [definite integral](Definite%20Integral.md) is linear - if $f,g: [a;b] \to \mathbb{R}$ are [Riemann-integrable](Riemann-Integrability.md), then for all $\alpha,\beta \in \mathbb{R}$
>
>$$
>\int_a^b \alpha \, f(x) + \beta\, g(x) \mathop{\mathrm{d}x} = \alpha \int_a^b f(x) \mathop{\mathrm{d}x} + \beta \int_a^b g(x) \mathop{\mathrm{d}x}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Interval Separation
>
>If $f: [a;b] \to \mathbb{R}$ is [Riemann-integrable](Riemann-Integrability.md), then for each $c \in [a;b]$ its [definite integral](Definite%20Integral.md) can be broken down as the sum of the [definite integrals](Definite%20Integral.md) of its [restrictions](../../../../Functions/Restriction.md) on $[a;c]$ and $[c;b]$.
>
>$$
>\int_a^b f = \int_a^c f + \int_c^b f
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Integration by Parts
>
>Let $f,g: D \to \mathbb{R}$ be [real functions](../../Real%20Functions/Real%20Function.md) on a [closed interval](../../../../../Set%20Theory/Ordering/Intervals.md) $D = [a;b] \subset \mathbb{R}$.
>
>
>If $f$ and $g$ are [continuously differentiable](../../Differentiation/Differentiability%20of%20Real%20Functions.md), then the [definite integral](Definite%20Integral.md) obeys
>
>$$
>\int_a^b f(x) g'(x) \mathop{\mathrm{d}x} = f(b)g(b) - f(a)g(a) - \int_a^b f'(x)g(x) \mathop{\mathrm{d}x}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Substitution
>
>Let $g: [a;b] \to \mathbb{R}$ and $f: [c;d] \to \mathbb{R}$ be [real functions](../../Real%20Functions/Real%20Function.md) such that the [image](../../../../Functions/Image%20of%20a%20Function.md) of $g$ is a [subset](../../../../../Set%20Theory/Subset.md) of $[c;d]$, i.e. $g([a;b]) \subseteq [c;d]$.
>
>If $f$ is [continuous](../../Real%20Functions/Continuity/Continuity%20of%20Real%20Functions.md) and $g$ is [continuously differentiable](../../Differentiation/Differentiability%20of%20Real%20Functions.md), then the following [definite Integral](Definite%20Integral.md) can be solved via substitution.
>
>$$
>\int_a^b f(g(x))g'(x) \mathop{\mathrm{d}x} = \int_{g(a)}^{g(b)} f(u) \mathop{\mathrm{d}u}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>