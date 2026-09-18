---
tags:
    - complex-analysis
    - real-analysis
    - analysis
    - mathematics
---

# Directional Differentiability (Complex-Valued Functions of Multiple Real Variables)

>[!DEFINITION] Definition: Directional Differentiability (Complex-Valued Functions of Multiple Real Variables)
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{C}$ be a [complex-valued function of multiple real variables](./Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables.md), let $\boldsymbol{d} \in \mathbb{R}^n$ and let $\boldsymbol{p} \in \mathcal{D}$ be such that $0$ is an [accumulation point](../../../Topology/Accumulation%20Points.md) of $\{h \in \mathbb{R}\mid \boldsymbol{p}+h\boldsymbol{d} \in \mathcal{D}\}$.
>
>We say that $f$ is **directionally differentiable at $\boldsymbol{p}$ along $\boldsymbol{d}$** if the [limit](./Limits%20(Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables).md)
>
>$$\lim_{t\to 0}\frac{f(\boldsymbol{p} + t \cdot \boldsymbol{d} ) - f(\boldsymbol{p})}{t}$$
>
>exists. In this case, its value is known as $f$'s **directional derivative at $\boldsymbol{p}$ along $\boldsymbol{d}$**.
>
>>[!NOTATION]
>>
>>$$\frac{\partial f}{\partial \boldsymbol{d}}(\boldsymbol{p}) \qquad \partial_{\boldsymbol{d}}f(\boldsymbol{p}) \qquad f_{\boldsymbol{d}}(\boldsymbol{p}) \qquad D_{\boldsymbol{d}} f(\boldsymbol{p})$$
>>
>