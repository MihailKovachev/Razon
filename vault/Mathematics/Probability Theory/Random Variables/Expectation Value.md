---
tags:
    - probability-theory
    - mathematics
---

# Expectation Value

>[!DEFINITION] Definition: Expectation Value
>
>Let $(\Omega, \mathcal{F}, \Pr)$ be a [probability space](../Probability%20Space.md) and let $X: \Omega \to \mathbb{R}$ be a [real random variable](./Real%20Random%20Variable.md).
>
>The **expectation value** of $X$ is its [Lebesgue integral](../../Analysis/Real%20Analysis/Lebesgue%20Integral.md) with respect to $\Pr$ (provided that $X$ is [Lebesgue-integrable](../../Analysis/Real%20Analysis/Lebesgue%20Integral.md)):
>
>$$\int_{\Omega} X \, \mathrm{d} \mathrm{Pr}$$
>
>>[!NOTATION]
>>
>>$$\begin{array} EX & \mathbb{E}[X] & \langle X \rangle & \overline{X} & \end{array}$$
>>
>
>>[!WARNING] Warning:
>>
>>If $X$ is not [Lebesgue-integrable](../../Analysis/Real%20Analysis/Lebesgue%20Integral.md), then $\int_{\Omega} X \, \mathrm{d} \mathrm{Pr}$ and thus $\mathbb{E}[X]$ might not exist.
>>
>