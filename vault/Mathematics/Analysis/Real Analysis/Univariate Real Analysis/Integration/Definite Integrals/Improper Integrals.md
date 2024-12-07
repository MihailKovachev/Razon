>[!NOTATION] Notation: Improper Integrals
>
>An **improper integral** is a [definite integral](Definite%20Integral.md) for a [real function](../../Real-Valued%20Function.md) $f: D \subseteq \mathbb{R} \to \mathbb{R}$ on an open or a semi-open interval $D$:
>- If $D = [a;b)$ where $a, b \in \mathbb{R}$, the improper integral is defined through the [left-sided limit](../../Real%20Functions/Limits%20of%20Functions/One-Sided%20Limits.md)
>
>$$\int_a^b f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \lim_{\beta \to b^-} \int_a^\beta f(x) \mathop{\mathrm{d}x}$$
>
>- If $D = (a;b]$ where $a, b \in \mathbb{R}$, the improper integral is defined through the [right-sided limit](../../Real%20Functions/Limits%20of%20Functions/One-Sided%20Limits.md)
>
>$$\int_a^b f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \lim_{\alpha \to a^+} \int_\alpha^b f(x) \mathop{\mathrm{d}x}$$
>
>- If $D = [a;\infty)$ where $a \in \mathbb{R}$, the improper integral is defined through the [limit](../../Real%20Functions/Limits%20of%20Functions/Limits%20of%20a%20Function.md)
>
>$$\int_a^\infty f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \lim_{\beta \to \infty} \int_a^\beta f(x) \mathop{\mathrm{d}x}$$
>
>- If $D = (-\infty;b]$ where $b \in \mathbb{R}$, the improper integral is defined through the [limit](../../Real%20Functions/Limits%20of%20Functions/Limits%20of%20a%20Function.md)
>
>$$\int_{-\infty}^b f(x) \mathop{\mathrm{d}x} \overset{\text{def}}{=} \lim_{\alpha \to -\infty} \int_\alpha^b f(x) \mathop{\mathrm{d}x}$$
>
>- If $D = (-\infty;\infty)$, then for any choice of $c \in \mathbb{R}$ the improper integral is defined as
>
>$$\int_{-\infty}^\infty f(x)\mathop{\mathrm{d}x} \overset{\text{def}}{=} \int_{-\infty}^c f(x)\mathop{\mathrm{d}x} +\int_c^\infty f(x)\mathop{\mathrm{d}x}$$
>
>If the respective limit exists, then the improper integral is said to **converge** or simply **exist**. Otherwise, it **diverges** or does **not exist**.