---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Directional Differentiability (Real Vector Functions)

>[!DEFINITION] Definition: Directional Differentiability (Real Vector Functions)
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](../Real%20Vector%20Functions.md), $\boldsymbol{\hat{r}} \in \mathbb{R}^n$ be a [unit](../../../../Algebra/Vector%20Spaces/Norms.md) [vector](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) and let $\boldsymbol{p} \in \mathcal{D}$.  
>
>We say that $f$ is **(directionally) differentiable at** $\boldsymbol{p}$ **along** $\boldsymbol{\hat{r}}$ if the following [limit](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Limits%20of%20Parametric%20Curves.md) exists:
>
>$$\lim_{h\to 0}\frac{f(\boldsymbol{p} + h \cdot \boldsymbol{\hat{r}} ) - f(\boldsymbol{p})}{h}$$
>
>>[!DEFINITION] Definition: Directional Derivative
>>
>>In this case, this [limit](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Limits%20of%20Parametric%20Curves.md) is known as $f$'s **directional derivative at** $\boldsymbol{p}$ **along** $\boldsymbol{\hat{r}}$.
>>
>>>[!NOTATION]
>>>
>>>$$\frac{\partial f}{\partial \boldsymbol{\hat{r}}}(\boldsymbol{p}) \qquad \partial_{\boldsymbol{\hat{r}}}f(\boldsymbol{p}) \qquad f_{\boldsymbol{\hat{r}}}(\boldsymbol{p}) \qquad D_{\boldsymbol{\hat{r}}} f(\boldsymbol{p})$$
>>>
>>
>