---
title: Derivatives of Elementary Functions
tags:
  - differentiability
  - real-functions
  - real-analysis
  - analysis
  - mathematics
---

>[!THEOREM] Theorem: Power Rule
>
>$$
>(x^\alpha)' = \alpha x^{\alpha - 1} \qquad \forall \alpha \in \mathbb{R}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Derivative of Exponential Functions
>
>$$
>(\mathrm{e}^x)' = \mathrm{e}^x
>$$
>
>$$
>(a^x)' = a^x \ln a
>$$
>
>>[!PROOF]-
>>
>>$$
>>\begin{align*}(e^x)' &= \lim_{\Delta x \to 0}\frac{e^{x+\Delta x}-e^x}{\Delta x} = \lim_{\Delta x \to 0}\frac{e^x(e^{\Delta x}-1)}{\Delta x} = e^x\lim_{\Delta x \to 0}\frac{e^{\Delta x}-1}{\Delta x} \\ &= e^x \lim_{\Delta x\to 0}\frac{\displaystyle \lim_{n\to \infty} \left(1+\frac{\Delta x}{n}\right)^n - 1}{\Delta x} = e^x \lim_{\Delta x\to 0} \operatorname*{lim}_{n\rightarrow\infty}\frac{(1+\frac{\Delta x}{n})^{n}-1}{\Delta x} \\ &= e^x \lim_{\Delta x\to 0} \operatorname*{lim}_{n\rightarrow\infty} \frac{\displaystyle 1+n\frac{\Delta x}{n} + \begin{pmatrix}n \\ 2\end{pmatrix}\left(\frac{\Delta x}{n}\right)^{2}+\cdots+\begin{pmatrix}n \\ n-1\end{pmatrix}\left(\frac{\Delta x}{n}\right)^{n-1} + \left(\frac{\Delta x}{n}\right)^n - 1}{\Delta x} \\ &= e^x \lim_{\Delta x\to 0} \operatorname*{lim}_{n\rightarrow\infty} \left(\displaystyle 1 + \begin{pmatrix}n \\ 2\end{pmatrix} \frac{\Delta x}{n^2}+\cdots + \begin{pmatrix} n \\ n-1 \end{pmatrix}\frac{\Delta x^{n-2}}{n^{n-1}} + \frac{\Delta x^{n-1}}{n^n}\right) \\ &= e^x \lim_{n\to \infty}\lim_{\Delta x\to 0} \left(\displaystyle 1 + \underset{\to 0}{\underbrace{\begin{pmatrix}n \\ 2\end{pmatrix} \frac{\Delta x}{n^2}+\cdots + \begin{pmatrix} n \\ n-1 \end{pmatrix}\frac{\Delta x^{n-2}}{n^{n-1}} + \frac{\Delta x^{n-1}}{n^n}}}\right) \\ &= e^x \lim_{n\to\infty} 1 = e^x\end{align*}
>>$$
>>
>>$$
>>\begin{align*}(a^x)' = ((e^{\ln a})^x)' = (e^{x \ln a})' = e^{x\ln a}\ln a = (e^{\ln a})^x \ln a = a^x \ln a\end{align*}
>>$$
>>
>

>[!THEOREM] Theorem: Derivative of Logarithmic Functions
>
>$$
>(\ln x)' = \frac{1}{x}
>$$
>
>$$
>(\log_a x)' = \frac{1}{x \ln a}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>