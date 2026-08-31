---
tags:
    - real-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Real Logarithms

## The Real Natural Logarithm

>[!THEOREM] Theorem: Injectivity of the Real Natural Logarithm
>
>The [real exponential function](./Real%20Exponentiation.md#The%20Real%20Exponential%20Function) is [injective](../../Functions/Injections,%20Surjections%20and%20Bijections.md#Injections) on $(0; \infty)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: The Real Natural Logarithm
>>
>>The **real natural logarithm** is the [inverse](../../Functions/Injections,%20Surjections%20and%20Bijections.md#Injections) of the [real exponential function](./Real%20Exponentiation.md#The%20Real%20Exponential%20Function) on $(0; \infty)$.
>>
>>>[!NOTATION]
>>>
>>>$$\ln(x) \qquad \log_\mathrm{e}(x) \qquad \log(x)$$
>>>
>>
>

>[!THEOREM] Addition and Subtraction Theorem for the Real Natural Logarithm
>
>The [real natural logarithm](#The%20Real%20Natural%20Logarithm) has the following property:
>
>$$\ln (xy) = \ln x + \ln y \qquad \ln \left(\frac{x}{y}\right) = \ln x - \ln y$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity of the Real Natural Logarithm
>
>The [real natural logarithm](#The%20Real%20Natural%20Logarithm) is [continuous](./Continuity%20(Real%20Functions).md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Derivative of the Real Natural Logarithm
>
>The [real natural logarithm](#The%20Real%20Natural%20Logarithm) is [differentiable](./Differentiability%20(Real%20Functions).md) with
>
>$$(\ln x)' = \frac{1}{x}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antiderivatives of the Real Natural Logarithm
>
>The [real natural logarithm](#The%20Real%20Natural%20Logarithm) is [antidifferentiable](./Antidifferentiability%20(Real%20Functions).md) with
>
>$$\int \ln x = x \ln x - x + C.$$
>
>>[!PROOF]-
>>
>>We have
>>
>>$$\ln x = u(x) v'(x)$$
>>
>>with $u(x) = \ln x$, $u'(x) = \frac{1}{x}$, $v'(x) = 1$ and $v(x) = x$ for all $x \in (0, \infty)$. Since $u$ and $v$ are [continuously differentiable](./Differentiability%20(Real%20Functions).md) on $(0,\infty)$, we can use [integration by parts](./Antidifferentiability%20(Real%20Functions).md):
>>
>>$$\begin{aligned}\int \ln x \,\mathrm{d}x & = u(x) v(x) - \int u'(x) v(x) \,\mathrm{d}x \\ & = x \ln x - \int \frac{1}{x}x\,\mathrm{d}x \\ & = x \ln x - x + C\end{aligned}$$
>>
>

>[!THEOREM] Theorem: Real Natural Logarithm Variation in Bachmann-Landau
>
>The [real natural logarithm](#The%20Real%20Natural%20Logarithm) $\ln (x + 1)$ can expressed in [Bachmann-Landau notation](../Asymptotic%20Analysis/Bachmann-Landau%20Notation.md) for $x \to 0$ as follows:
>
>$$\ln (x+1) = \sum_{k=1}^m \frac{(-1)^{k+1}}{k}x^k + O(x^{m+1}) \qquad \text{for} \qquad x \to 0$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Logarithms

>[!DEFINITION] Definition: Real Logarithm
>
>Let $b \in \mathbb{R}_{\gt 0}$ and $b \ne 1$.
>
>The **logarithm with base** $b$ is the [function](./Real%20Functions.md) $\log_b: \mathbb{R}_{\gt 0} \to \mathbb{R}$ defined using the [real natural logarithm](./Real%20Logarithms.md) as 
>
>$$\log_{b}(x) \overset{\text{def}}{=} \frac{\ln(x)}{\ln(b)}$$
>
>for each $x \gt 0$.
>
>>[!NOTATION]
>>
>>We can also write $\log_b x$.
>>
>

>[!THEOREM] Theorem: Logarithm as Solution to Equations
>
>If $b \in \mathbb{R}_{\gt 0}$ and $b \ne 1$ and $y \gt 0$, then the equation
>
>$$b^x = y$$
>
>has the only solution
>
>$$x = \log_b y$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Multiplication $\leftrightarrow$ Addition
>
>[Logarithms](./Real%20Logarithms.md) can be used to turn products into sums and viceversa:
>
>$$\log_{b} (a_1 \times \cdots \times a_n) = \log_{b} (a_1) + \cdots + \log_{b} (a_n)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Division $\leftrightarrow$ Subtraction
>
>[Logarithms](./Real%20Logarithms.md) can be used to turn division into subtraction and vice versa:
>
>$$\log_{b}\left( \frac{a}{c} \right) = \log_{b}(a) - \log_{b}(c)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Exponentiation $\leftrightarrow$ Multiplication
>
>[Logarithms](./Real%20Logarithms.md) can be used to turn multiplication into [exponentiation](./Real%20Exponentiation.md) and vice versa:
>
>$$\log_{b}(a^c) = c\cdot\log_{b}(a)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Base Change
>
>Let $a \gt 0$ and $b_1, b_2 \gt 0$ with $b_1 \ne 1$ and $b_2 \ne 1$.
>
>We can turn the [real logarithm](#Real%20Logarithms) with base $b_1$ to [real logarithms](#Real%20Logarithms) with base $b_2$ as follows:
> 
>$$\log_{b_1} a = \frac{\log_{b_2} a}{\log_{b_2} b_1}$$
>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Differentiability of Logarithms
>
>The [real logarithm](#Logarithms) $\log_b x$ ($b \gt 0$, $b \ne 1$) is [differentiable](./Differentiability%20(Real%20Functions).md) on $(0, +\infty)$ and its [derivative](./Differentiability%20(Real%20Functions).md) can be constructed via the [real natural logarithm](#The%20Real%20Natural%20Logarithm):
>
>$$(\log_b x)' = \frac{1}{x \ln b}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antidifferentiability of Logarithms
>
>The [real logarithm](#Logarithms) $\log_b x$ ($b \gt 0$, $b \ne 1$) is [antidifferentiable](./Antidifferentiability%20(Real%20Functions).md) on $(0, +\infty)$ and its [antiderivatives](./Antidifferentiability%20(Real%20Functions).md) can be constructed via the [real natural logarithm](#The%20Real%20Natural%20Logarithm):
>
>$$\int \log_b x \,\mathrm{d}x = x \log_b x - \frac{x}{\ln b} + C$$
>
>>[!PROOF]-
>>
>>TODO
>>
>