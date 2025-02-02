>[!DEFINITION] Definition: Definite Integral
>
>Let $f: D \to \mathbb{R}$ be a [Riemann-integrable](Riemann-Integrability.md) [real function](../../../Real%20Functions/Real%20Function.md) on a [closed interval](../../../../../Set%20Theory/Ordering/Intervals.md) $D = [a;b] \subset \mathbb{R}$.
>
>The **definite integral** of $f$ is the [limit](../../../Real%20Functions/Limits%20of%20Functions/Limit%20of%20a%20Real%20Function.md) of its [Riemann sums](Riemann%20Sum.md).
>
>$$
>\lim_{\Delta x_i\to 0}\sum_{i=1}^n f(x_i^\ast)\Delta x_i
>$$
>
>>[!NOTATION]-
>>
>>The most common notation for the definite integral is
>>
>>$$
>>\int_a^b f(x) \mathop{\mathrm{d}x}
>>$$
>>
>>The upside of this notation is that it clearly shows where the integrand, i.e. the thing being integrated, begins and where it ends. This is not very useful when we are referring to $f$ by its name, but it helps to remove ambiguity when we substitute $f$ with an expression such as $\displaystyle \int_a^b x^3 + \ln x \mathop{\mathrm{d}x}$.
>>
>>Its main downside is that it forces us to assign a symbol to the function's argument which is redundant and can even be confusing in some contexts where we refer to $f$ by its name. In particular, it is irrelevant whether we write $\displaystyle \int_a^b f(x) \mathop{\mathrm{d}x}$ or $\displaystyle \int_a^b f(y) \mathop{\mathrm{d}y}$ or $\displaystyle \int_a^b f(\omega) \mathop{\mathrm{d}\omega}$, hence we can shorten the notation to just
>>
>>$$
>>\qquad \int_a^b f
>>$$
>>
>>The main downside of this notation is that it implies that the order of $a$ and $b$ matters, which is not the case - what matters is the actual [set](../../../../../Set%20Theory/Set.md) which $[a;b]$ represents. To emphasise this, we can use the following notations:
>>
>>$$
>>\int_{[a;b]} f \qquad \int_D f
>>$$
>>
>>In the latter case, we can also add $\mathrm{d}D$ to clarify where the integrand begins and ends, such as
>>
>>$$
>>\int_D f \mathop{\mathrm{d}D}
>>$$
>>
>>All of these notations are useful in specific contexts and less so in others.
>>
>
>>[!NOTATION]- Notation: Definite Integrals with Special Bounds
>>
>>A common convention is to define the notations
>>
>>$$
>>\int_b^a f = -\int_a^b f
>>$$
>>
>>and
>>
>>$$
>>\int_c^c f = 0
>>$$
>>
>>for each $c \in [a;b]$. This is merely notation which makes the formulation of many theorems easier and more natural.
>>
>
>>[!INTUITION]- Intuition: Geometric Meaning of the Definite Integral
>>
>>The definite integral of $f$ gives us the *signed* are between the $x$-axis and the graph of $f$ from $a$ to $b$ - areas above the $x$-axis are positive and areas below it are negative.
>>
>>![Definite Integral](Resources/Definite%20Integral.png)
>