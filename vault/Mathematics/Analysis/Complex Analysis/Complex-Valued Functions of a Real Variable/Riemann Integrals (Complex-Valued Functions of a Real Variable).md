---
tags:
    - complex-analysis
    - real-analysis
    - analysis
    - mathematics
---

# Riemann Integrals (Complex-Valued Functions of a Real Variable)

>[!DEFINITION] Definition: Riemann Integrals (Complex-Valued Functions of a Real Variable)
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{C}$ be a [complex-valued function of a real variable](./Complex-Valued%20Function%20of%20a%20Real%20Variable.md) and let $S \subseteq \mathcal{D}$.
>
>We say that $f$ is **Riemann-integrable on** $S$ if its [real part](../Complex-Valued%20Functions.md) $\operatorname{Re} f$ and [imaginary part](../Complex-Valued%20Functions.md) $\operatorname{Im} f$ are both [Riemann-integrable](../../Real%20Analysis/Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md) on $S$. In this case, the **Riemann integral** of $f$ on $S$ is defined as follows:
>
>$$\int_S \operatorname{Re} f(x) \,\mathrm{d}x + \mathrm{i}\int_S \operatorname{Im} f(x) \,\mathrm{d}x$$
>
>>[!NOTATION]
>>
>>$$\int_S f(x) \,\mathrm{d}x$$
>>
>

>[!THEOREM] Theorem: $\operatorname{Re} \int = \int \operatorname{Re}$ and $\operatorname{Im} \int = \int \operatorname{Im}$
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{C}$ be a [complex-valued function of a real variable](./Complex-Valued%20Function%20of%20a%20Real%20Variable.md) and let $S \subseteq \mathcal{D}$.
>
>If $f$ is [Riemann-integrable](./Riemann%20Integrals%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable).md) on $S$, then:
>- the [real part](../../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md) of its [Riemann integral](./Riemann%20Integrals%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable).md) is equal to the [Riemann integral](../../Real%20Analysis/Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md) of its [real part](../Complex-Valued%20Functions.md);
>- the [imaginary part](../../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md) of its [Riemann integral](./Riemann%20Integrals%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable).md) is equal to the [Riemann integral](../../Real%20Analysis/Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md) of its [imaginary part](../Complex-Valued%20Functions.md).
>
>$$\operatorname{Re} \int_S f(x)\,\mathrm{d}x = \int_S \operatorname{Re} f(x) \,\mathrm{d}x$$
>
>$$\operatorname{Im} \int_S f(x)\,\mathrm{d}x = \int_S \operatorname{Im} f(x) \,\mathrm{d}x$$
>
>>[!PROOF]-
>>
>>TODO
>>
>