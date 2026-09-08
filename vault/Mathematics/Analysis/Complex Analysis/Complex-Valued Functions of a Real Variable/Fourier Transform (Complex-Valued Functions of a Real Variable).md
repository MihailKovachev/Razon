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
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{C}$ be a [complex-valued function of a real variable](./Complex-Valued%20Function%20of%20a%20Real%20Variable.md).
>
>The **Fourier transform** of $f$ is the [complex-valued function of a real variable](./Complex-Valued%20Function%20of%20a%20Real%20Variable.md) $F: \mathcal{D}_F \subseteq \mathbb{R} \to \mathbb{C}$ defined as
>
>$$F(\xi) \overset{\text{def}}{=} \int_{\mathcal{D}_f} f(t) \mathrm{e}^{-2\uppi \mathrm{i} \xi t}\,\mathrm{d}t$$
>
>for all $\xi \in \mathbb{R}$ for which the above [Lebesgue integral](./Lebesgue%20Integrals%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable).md) exists.
>
>>[!NOTATION]
>>
>>The [Fourier transform](./Fourier%20Transform%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable).md) of $f$ is typically denoted in one of the following ways:
>>
>>$$\hat{f} \qquad \mathcal{F}\{f\} \qquad \mathcal{F}[f]$$
>>
>

>[!THEOREM] Theorem: Linearity of the Fourier Transform
>
>Let $f,g: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{C}$ be [complex-valued functions of a real variable](./Complex-Valued%20Function%20of%20a%20Real%20Variable.md) and let $\mathcal{F}\{f\}: \mathcal{D}_{\hat{f}} \subseteq \mathbb{R} \to \mathbb{C}$ and $\mathcal{F}\{g\}: \mathcal{D}_{\hat{g}} \subseteq \mathbb{R} \to \mathbb{C}$ be their [Fourier transforms](./Fourier%20Transform%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable).md).
>
>For each $\xi \in \mathcal{D}_{\hat{f}} \cap \mathcal{D}_{\hat{g}}$ and all $\alpha, \beta \in \mathbb{C}$, we have:
>
>$$\mathcal{F}\{\alpha f + \beta g\}(\xi) = \alpha \mathcal{F}\{f\}(\xi) + \beta \mathcal{F}\{g\}(\xi)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>