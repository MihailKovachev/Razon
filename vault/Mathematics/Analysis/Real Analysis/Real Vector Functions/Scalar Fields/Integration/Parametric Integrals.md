


>[!DEFINITION] Definition: Parametric Integrals
>
>Let $f: D \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) on a [rectangle](TODO) $D = [a;b] \times [c;d]$.
>
>>[!DEFINITION] Definition: Parametric Integral (Type I)
>>
>>Given two [real functions](../../../Real%20Functions/Real%20Functions.md) $l,u: [a;b] \to [c;d]$, we define a **parametric integral** $\mathcal{X}: [a;b] \to \mathbb{R}$ as
>>
>>$$
>>\mathcal{X}(x) \overset{\text{def}}{=} \int_{l(x)}^{u(x)} f(x, y) \mathop{\mathrm{d}y}
>>$$
>>
>>>[!NOTE] Note
>>>
>>>For any particular value $x^\ast$ of $x$, the functions $l$ and $u$ result in concrete real numbers $l(x^\ast)$ and $u(x^\ast)$ and the expression $f(x^\ast, y)$ is a concrete [real function](../../../Real%20Functions/Real%20Functions.md) of $y$.
>>>
>>
>>>[!EXAMPLE]-
>>>
>>>For $x = 3$, we get
>>>
>>>$$
>>>\mathcal{X}(3) = \int_{l(3)}^{u(3)} f(3,y) \mathop{\mathrm{d}y},
>>>$$
>>>
>>>which is just a regular [definite integral](../../../Real%20Functions/Integration/Definite%20Integrals/index.md).
>>>
>>
>
>>[!DEFINITION] Definition: Parametric Integral (Type II)
>>
>>Given two [real functions](../../../Real%20Functions/Real%20Functions.md) $l,u: [c;d] \to [a;b]$, we define a **parametric integral** $\mathcal{Y}: [c;d] \to \mathbb{R}$ as
>>
>>$$
>>\mathcal{Y}(y) \overset{\text{def}}{=} \int_{l(y)}^{u(y)} f(x, y) \mathop{\mathrm{d}x}
>>$$
>>
>>>[!NOTE] Note
>>>
>>>For any particular value $y^\ast$ of $y$, the functions $l$ and $u$ result in concrete real numbers $l(y^\ast)$ and $u(y^\ast)$ and the expression $f(x, y^\ast)$ is a concrete [real function](../../../Real%20Functions/Real%20Functions.md) of $x$.
>>>
>>
>>>[!EXAMPLE]-
>>>
>>>For $y = 3$, we get
>>>
>>>$$\mathcal{Y}(3) = \int_{l(3)}^{u(3)} f(x,3) \mathop{\mathrm{d}x},$$
>>>
>>>which is just a regular [definite integral](../../../Real%20Functions/Integration/Definite%20Integrals/index.md).
>>>
>>
>

>[!THEOREM] Theorem: Continuity of Parametric Integrals
>
>Let $f: R \subset \mathbb{R}^2 \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) on some [rectangle](TODO) $R = [a;b] \times [c;d]$.
>
>If $f$ is [continuous](../Continuity%20of%20Real%20Scalar%20Fields.md) on $R$, then:
>- the [parametric integral](Parametric%20Integrals.md) $\int_c^d f(x,y)\mathop{\mathrm{d}y}$ is [continuous](../../../Real%20Functions/Continuity.md) on $[a;b]$.
>- the [parametric integral](Parametric%20Integrals.md) $\int_a^b f(x,y)\mathop{\mathrm{d}x}$ is [continuous](../../../Real%20Functions/Continuity.md) on $[c;d]$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Leibniz Integral Rule
>
>Let $f: R \subset \mathbb{R}^2 \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) on some [rectangle](TODO) $R = [a;b] \times [c;d]$.
>
>If $f$ is [continuously partially differentiable](../Differentiation/Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md) and $l,u$ are [continuously differentiable](../../../Real%20Functions/Differentiation/Derivatives.md), then the [derivatives](../../../Real%20Functions/Differentiation/Derivatives.md) of $f$'s [parametric integrals](Parametric%20Integrals.md) are given by
>
>$$
>\frac{\mathrm{d}}{\mathrm{d}x} \int_{l(x)}^{u(x)} f(x,y) \mathop{\mathrm{d}y} = \int_{l(x)}^{u(x)} \frac{\partial}{\partial x}f(x,y)\mathop{\mathrm{d}y} \,+\, f(x,u(x))\frac{\mathrm{d}}{\mathrm{d}x}u(x) - f(x, l(x))\frac{\mathrm{d}}{\mathrm{d}x}l(x)
>$$
>
>
>$$
>\frac{\mathrm{d}}{\mathrm{d}y} \int_{l(y)}^{u(y)} f(x,y) \mathop{\mathrm{d}x} = \int_{l(y)}^{u(y)} \frac{\partial}{\partial y}f(x,y)\mathop{\mathrm{d}x} \,+\, f(u(y), y)\frac{\mathrm{d}}{\mathrm{d}y}u(y) - f(l(y), y)\frac{\mathrm{d}}{\mathrm{d}x}l(y)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>