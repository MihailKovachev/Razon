---
tags:
    - complex-analysis
    - analysis
    - mathematics
---

# Contour Integrals (Complex Functions)

>[!DEFINITION] Definition: Contour Integral
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](./Complex%20Functions.md) and let $\gamma: [a,b] \subset \mathbb{R} \to \mathbb{C}$ be a [complex-valued function of a real variable](../Complex-Valued%20Functions%20of%20a%20Real%20Variable/Complex-Valued%20Function%20of%20a%20Real%20Variable.md) which is [piecewise differentiable](../Complex-Valued%20Functions%20of%20a%20Real%20Variable/Differentiability%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable).md) with $\gamma([a,b]) \subseteq \mathcal{D}_f$.
>
>If the [integral](../Complex-Valued%20Functions%20of%20a%20Real%20Variable/Riemann%20Integrals%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable).md)
>
>$$\int_a^b f(\gamma(t)) \gamma'(t) \,\mathrm{d}t$$
>
>exists, then it is known as $f$'s **contour integral over** $\gamma$.
>
>>[!NOTATION]
>>
>>We denote the [contour integral](./Contour%20Integrals%20(Complex%20Functions).md) of $f$ over $\gamma$ as follows:
>>
>>$$\int_{\gamma} f(z) \,\mathrm{d}z$$
>>
>>If $\gamma(a) = \gamma(b)$, then we write:
>>
>>$$\oint_{\gamma} f(z) \,\mathrm{d}z$$
>>
>
