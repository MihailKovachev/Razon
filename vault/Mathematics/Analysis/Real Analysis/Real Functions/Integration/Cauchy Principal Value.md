---
tags:
    - real-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Cauchy Principal Value

>[!DEFINITION] Definition: Cauchy Principal Value
>
>Let $f: \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Functions.md) which is [locally Riemann-integrable](./Riemann%20Integrals%20(Real%20Functions).md) on $\mathbb{R}$.
>
>The **Cauchy principal value** of $f$ is the following [limit](../Limits%20(Real%20Functions.md) of its [Riemann integral](./Riemann%20Integrals%20(Real%20Functions).md) (if it exists):
>
>$$\lim_{M \to \infty} \int_{-M}^{+M} f(x)\,\mathrm{d}x$$
>
>>[!NOTATION]
>>
>>$$\text{CPV} \int_{-\infty}^{+\infty} f(x) \,\mathrm{d}x$$
>>
>
>>[!EXAMPLE]- Example: $\text{CPV} \int_{-\infty}^{+\infty} x \,\mathrm{d}x$
>>
>>We want to determine the following [Cauchy principal value](./Cauchy%20Principal%20Value.md):
>>
>>$$\text{CPV} \int_{-\infty}^{+\infty} x \,\mathrm{d}x$$
>>
>>We have:
>>
>>$$\begin{aligned}\text{CPV} \int_{-\infty}^{+\infty} x \,\mathrm{d}x & = \lim_{M \to \infty} \int_{-M}^M x \,\mathrm{d}x \\ & = \lim_{M \to \infty} \left. \frac{1}{2}x^{2} \right\vert_{-M}^M \\ & = \lim_{M \to \infty} \left(\frac{1}{2}M^2 - \frac{1}{2}(-M)^2  \right) \\ & = \lim_{M \to \infty} 0 = 0\end{aligned}$$
>>
>

>[!THEOREM] Theorem: Improper Integral $\implies$ Cauchy Principal Value
>
>Let $f: \mathbb{R} \to \mathbb{R}$ be a [real function](../Real%20Functions.md).
>
>If $f$ is [improperly Riemann-integrable](./Riemann%20Integrals%20(Real%20Functions).md#Improper%20Riemann%20Integrals) on $(-\infty, +\infty)$, then its [Cauchy principal value](./Cauchy%20Principal%20Value.md) exists and is equal to the [integral](./Riemann%20Integrals%20(Real%20Functions).md#Improper%20Riemann%20Integrals) of $f$:
>
>$$\int_{-\infty}^{+\infty} f(x) \,\mathrm{d}x = \text{CPV} \int_{-\infty}^{+\infty} f(x) \,\mathrm{d}x$$
>
>>[!PROOF]-
>>
>>TODO
>>
>