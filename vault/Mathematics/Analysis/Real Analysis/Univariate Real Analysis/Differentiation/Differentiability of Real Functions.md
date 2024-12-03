>[!DEFINITION] Definition: Derivative of a Real Function
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Functions/Real%20Function.md).
>
>The **derivative of** $f$ **in** $x_0 \in D$ is the [limit](../Real%20Functions/Limits%20of%20Functions/Real%20Limits%20of%20a%20Function.md)
>
>$$
>\lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}
>$$
>
>More generally, the derivative of $f$ is the [function](../Real%20Functions/Real%20Function.md) which maps every $x \in D$ to $f'(x)$.
>
>>[!NOTATION]-
>>
>>$$
>>f'(x_0) \qquad \frac{\mathrm{d}f}{\mathrm{d}x} (x_0) \qquad \frac{\mathrm{d}}{\mathrm{d}x}f(x_0)
>>$$
>
>>[!DEFINITION] Definition: Higher-Order Derivatives
>>
>>The $k$**-th order derivative** of $f$ is the derivative of the $(k-1)$-th order derivative of $f$:
>> - The $0$**-th order derivative of** $f$ is just $f$ itself;
>> - The **first order derivative of** $f$ is just the aforementioned derivative $f'$;
>> - The **second order derivative of** $f$ is the derivative of $f'$, etc.
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>f' \qquad f'' \qquad f''' \qquad f^{\mathrm{IV}} \qquad f^{\mathrm{V}} \qquad \cdots \qquad f^{(n)}
>>>$$
>>>
>>>$$
>>>\frac{\mathrm{d}f}{\mathrm{d}x} \qquad \frac{\mathrm{d}^2 f}{\mathrm{d}x^2} \qquad \frac{\mathrm{d}^3 f}{\mathrm{d}x^3} \qquad \frac{\mathrm{d}^4 f}{\mathrm{d}x^4} \qquad  \frac{\mathrm{d}^5 f}{\mathrm{d}x^5} \qquad \cdots \qquad \frac{\mathrm{d}^n f}{\mathrm{d}x^n}
>>>$$
>>>
>>
>

>[!DEFINITION] Definition: Differentiability
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Functions/Real%20Function.md).
>
>We say that $f$ is **differentiable at** some $x \in D$ if the first-order derivative of $f$ in $x$ exists.
>
>We say that $f$ is $k$**-times (continuously) differentiable on** $D$ if its $k$-th derivative exists (and is [continuous](../Real%20Functions/Continuity/Continuity.md)).

