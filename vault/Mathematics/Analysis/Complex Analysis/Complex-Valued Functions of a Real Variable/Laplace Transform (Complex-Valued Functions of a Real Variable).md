---
tags:
    - complex-analysis
    - real-analysis
    - analysis
    - mathematics
---

# Laplace Transform (Complex-Valued Functions of a Real Variable)

>[!DEFINITION] Definition: Laplace Transform (Complex-Valued Functions of a Real Variable)
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{C}$ be a [complex-valued function of a real variable](./Complex-Valued%20Function%20of%20a%20Real%20Variable.md).
>
>The **Laplace transform** of $f$ is the [complex function](../Complex%20Functions/Complex%20Functions.md) $F: \mathcal{D}_F \subseteq \mathbb{C} \to \mathbb{C}$ defined as
>
>$$F(s) \overset{\text{def}}{=} \int_{\mathcal{D}_f} f(t) \mathrm{e}^{-st}\,\mathrm{d}t$$
>
>for all $s \in \mathbb{C}$ for which the above [Lebesgue integral](./Lebesgue%20Integrals%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable).md) exists.
>
>>[!NOTATION]
>>
>>The [Laplace transform](./Laplace%20Transform%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable).md) of $f$ is typically denoted in one of the following ways:
>>
>>$$F \qquad \mathcal{L}\{f\} \qquad \mathcal{L}[f]$$
>>
>>The argument is often denoted by $s$ or $\sigma + \mathrm{i}\omega$.
>>
>

>[!THEOREM] Theorem: Linearity of Laplace Transforms
>
>Let $f,g: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{C}$ be [complex-valued functions of a real variable](./Complex-Valued%20Function%20of%20a%20Real%20Variable.md) and let $\mathcal{L}\{f\}: \mathcal{D}_F \subseteq \mathbb{C} \to \mathbb{C}$ and $\mathcal{L}\{g\}: \mathcal{D}_G \subseteq \mathbb{C} \to \mathbb{C}$ be their [Laplace transforms](./Laplace%20Transform%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable).md).
>
>For each $s \in \mathcal{D}_F \cap \mathcal{D}_G$ and all $\alpha, \beta \in \mathbb{C}$, we have:
>
>$$\mathcal{L}\{\alpha f + \beta g\}(s) = \alpha \mathcal{L}\{f\}(s) + \beta \mathcal{L}\{g\}(s)$$
>
>>[!PROOF]-
>>
>>$$\begin{aligned}\mathcal{L}\{\alpha f + \beta g\}(s) & = \int_{\mathcal{D}} (\alpha f(t) + \beta g(t)) \mathrm{e}^{-st}\,\mathrm{d}t \\ & = \int_{\mathcal{D}} \alpha f(t) \mathrm{e}^{-st}\,\mathrm{d}t + \int_{\mathcal{D}} \beta g(t) \mathrm{e}^{-st}\,\mathrm{d}t \\ & = \alpha \int_{\mathcal{D}} f(t) \mathrm{e}^{-st}\,\mathrm{d}t + \beta \int_{\mathcal{D}} g(t) \mathrm{e}^{-st}\,\mathrm{d}t \\ & = \alpha \mathcal{L}\{\}\cap\end{aligned}$$
>>
>