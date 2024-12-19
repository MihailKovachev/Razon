>[!THEOREM] The Fundamental Theorem of Real Analysis (Part I)
>
>Let $f: D \to \mathbb{R}$ be a [real function](../Real%20Functions/Real%20Function.md) on a [closed interval](../../../../Set%20Theory/Ordering/Intervals.md) $D = [a;b]$.
>
>If $f$ is [Riemann-integrable](Definite%20Integrals/Riemann-Integrability.md), then $F: D \to \mathbb{R}$ defined by the [definite integral](Definite%20Integrals/Definite%20Integral.md)
>
>$$
>F(x) \overset{\text{def}}{=} \int_a^x f
>$$
>
>is [continuous](../Real%20Functions/Continuity/Continuity%20of%20Real%20Functions.md). Furthermore, if $f$ is [continuous](../Real%20Functions/Continuity/Continuity%20of%20Real%20Functions.md) at some $c \in D$, then $F$ is an [antiderivative](Indefinite%20Integrals/Antiderivative.md) of $f$ at $c$, i.e. $F'(c) = f(c)$.
>
>>[!PROOF]-
>>
>>According to the definition of the [derivative](../Real%20Functions/Derivative%20of%20Odd%20and%20Even%20Functions.md) we need to prove
>>
>>$$
>>\lim_{\Delta x\to 0}\frac{F(x+\Delta x) - F(x)}{\Delta x} = f(x)
>>$$
>>
>> 
>>For all $c, x_0,\Delta x \in [a;b]$, where $x_0+\Delta x \in [a;b]$, it holds that
>>
>>$$
>>\begin{align*}F(x_0+\Delta x) - F(x_0) &= \int_c^{x_0+\Delta x} f(t)\mathop{\mathrm{d}t} - \int_c^{x_0} f(t)\mathop{\mathrm{d}t} \\ &= \int_c^{x_0+\Delta x} f(t)\mathop{\mathrm{d}t} + \int_{x_0}^c f(t)\mathop{\mathrm{d}t} \\ &= \int_{x_0}^c f(t)\mathop{\mathrm{d}t} + \int_c^{x_0+\Delta x} f(t)\mathop{\mathrm{d}t} \\ &= \int_{x_0}^{x_0+\Delta x}f(t) \mathop{\mathrm{d}t}\end{align*}
>>$$
>> 
>>The [mean value theorem for definite integrals](Definite%20Integrals/Mean%20Value%20Theorem%20for%20Definite%20Integrals.md) says that there is at least one $\xi \in[x_0;x_0+\Delta x]$ such that
>>
>>$$
>>\int_{x_0}^{x_0+\Delta x}f(t) \mathop{\mathrm{d}t} = f(\xi)(x_0 + \Delta x - x_0) = f(\xi)\cdot\Delta x
>>$$
>>
>>$$
>>\frac{F(x_0+\Delta x) - F(x_0)}{\Delta x} = f(\xi)
>>$$
>>
>>We now take the [limit](../Real%20Functions/Limits%20of%20Functions/Limit%20of%20a%20Real%20Function.md) as $\Delta x \to 0$.
>>
>>$$
>>\lim_{\Delta x \to 0}\frac{F(x_0+\Delta x) - F(x_0)}{\Delta x} = \lim_{\Delta x \to 0}f(\xi)
>>$$
>>
>>The left-hand side is just the [derivative](../Differentiation/Differentiability%20of%20Real%20Functions.md) of $F$ at $x_0$. Since $\xi$ is between $x_0$ and $x_0 + \Delta x$, it must approach $x_0$ for $\Delta x \to 0$. This means that
>>
>>$$
>>\lim_{\Delta x\to 0}f(\xi) = f(x_0)
>>$$
>>
>>and so we have
>>
>>$$
>>\lim_{\Delta x \to 0}\frac{F(x_0+\Delta x) - F(x_0)}{\Delta x} = f(x_0)
>>$$
>>
>>We have thus proven
>>
>>$$
>>F'(x_0) = f(x_0)
>>$$
>>
>

>[!THEOREM] The Fundamental Theorem of Real Analysis (Part II)
>
>If $f: [a;b] \to \mathbb{R}$ , then any [antiderivative](Indefinite%20Integrals/Antiderivative.md) $F:[a;b] \to \mathbb{R}$ of $f$ can be used to calculate its [definite integral](Definite%20Integrals/Definite%20Integral.md) as follows:
>
>$$
>\int_a^b f(x) \mathop{\mathrm{d}x} = F(b) - F(a)
>$$
>
>>[!NOTATION]-
>>
>>The expression $F(b) - F(a)$ is usually shortened to just $F(x)\big|_a^b$.
>
>>[!PROOF]-
>>
>>TODO
>>
>