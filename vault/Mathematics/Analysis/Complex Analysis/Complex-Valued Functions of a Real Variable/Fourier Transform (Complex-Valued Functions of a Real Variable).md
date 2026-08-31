---
tags:
    - complex-analysis
    - real-analysis
    - analysis
    - mathematics
---

# Fourier Transform (Complex-Valued Functions of a Real Variable)

>[!DEFINITION] Definition: Fourier Transform (Complex-Valued Functions of a Real Variable)
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{C}$ be a [complex-valued function of a real variable](./Complex-Valued%20Function%20of%20a%20Real%20Variable.md) and let $\mathcal{D}_F \subseteq \mathbb{R}$ be the [set](../../../Set%20Theory/Sets.md) of all $\xi \in \mathbb{R}$ for which the following [integral](./Definite%20Integrals%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable).md) of the product between $f$ and the [complex exponential function](../Complex%20Functions/Complex%20Exponential%20Function.md) exists:
>
>$$\int_{\mathcal{D}_f} f(t) \exp(-2\uppi \xi t\mathrm{i})\,\mathrm{d}t$$
>
>The **Fourier transform** of $f$ is the [complex-valued function of a real variable](./Complex-Valued%20Function%20of%20a%20Real%20Variable.md) $F: \mathcal{D}_F \subseteq \mathbb{C} \to \mathbb{C}$ defined as follows:
>
>$$\mathcal{F}\{f\}(\xi) \overset{\text{def}}{=} \int_{\mathcal{D}_f} f(t) \exp(-2\uppi \xi t\mathrm{i})\,\mathrm{d}t$$
>
>>[!NOTATION]
>>
>>The [Fourier transform](./Fourier%20Transform%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable).md) of $f$ is typically denoted in one of the following ways:
>>
>>$$\hat{f} \qquad \mathcal{F}\{f\} \qquad \mathcal{F}[f]$$
>>
>