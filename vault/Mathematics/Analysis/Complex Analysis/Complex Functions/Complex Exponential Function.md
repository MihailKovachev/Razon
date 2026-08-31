---
tags:
    - complex-analysis
    - mathematical-analysis
    - mathematics
---

# The Complex Exponential Function

>[!THEOREM] Theorem: Complex Exponential Function
>
>The [complex power series](../Complex%20Power%20Series.md)
>
>$$
>\sum_{n = 0}^{\infty} \frac{z^n}{n!} = 1 + \frac{z^1}{1!} +  \frac{z^2}{2!} + \frac{z^3}{3!} + \frac{z^4}{4!} + \cdots
>$$
>
>[converges absolutely](../Complex%20Power%20Series.md#Convergence) for all $z \in \mathbb{C}$.
>
>>[!PROOF]-
>>
>>We use the [ratio convergence test](../Complex%20Series.md#Convergence). Let $a_n = \frac{z^n}{n!}$. We have:
>>
>>$$
>>\left\vert\frac{a_{n+1}}{a_n}\right\vert = \frac{|z|^{n+1}}{(n+1)!}\frac{n!}{|z|^n} = \frac{|z|}{n+1}
>>$$
>>
>>Since
>>
>>$$
>>\lim_{n \to \infty} \frac{|z|}{n+1} = 0 \lt 1
>>$$
>>
>>for all $z \in \mathbb{C}$, we know that $\sum_{n = 0}^{\infty} \frac{z^n}{n!}$ is [absolutely convergent](../Complex%20Series.md#Convergence) for all $z \in \mathbb{C}$.
>>
>
>>[!DEFINITION] Definition: Complex Exponential
>>
>>The **complex exponential function** is the [complex function](./Complex%20Functions.md) $\exp: \mathbb{C} \to \mathbb{C}$ defined by the aforementioned [complex power series](../Complex%20Power%20Series.md):
>>
>>$$
>>\exp (z) \overset{\text{def}}{=} \sum_{n = 0}^{\infty} \frac{z^n}{n!}
>>$$
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\exp z \qquad \exp(z) \qquad \mathrm{e}^z
>>>$$
>>>
>>
>

>[!THEOREM] Theorem: Complex Exponential Extends Real Exponential
>
>The [restriction](../../Functions/Functions.md) of the [complex exponential function](./Complex%20Exponential%20Function.md) to the [real numbers](../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) $\mathbb{R}$ is the [real exponential function](../../Real%20Analysis/Real%20Functions/Real%20Exponentiation.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Periodicity of the Complex Exponential
>
>The [complex exponential function](./Complex%20Exponential%20Function.md) is [periodic](../../Real%20Analysis/Real%20Functions/Periodicity.md) with period $2\pi \mathrm{i}$:
>
>$$
>\exp(z + 2k\pi \mathrm{i}) = \exp (z) \qquad \forall z \in \mathbb{C}, \forall k \in \mathbb{Z}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Euler's Formula
>
>For every $\varphi \in \mathbb{R}$, the [real part](../Complex-Valued%20Functions.md) of the [complex exponential function](./Complex%20Exponential%20Function.md) $\mathrm{e}^{\mathrm{i}\varphi}$ is the [real cosine](../../Real%20Analysis/Real%20Functions/Real%20Trigonometric%20Functions/Real%20Trigonometric%20Functions.md#The%20Real%20Cosine%20Function) of $\varphi$ and the [imaginary part](../Complex-Valued%20Functions.md) is the [real sine](../../Real%20Analysis/Real%20Functions/Real%20Trigonometric%20Functions/Real%20Trigonometric%20Functions.md#The%20Real%20Sine%20Function) of $\varphi$:
>
>$$
>\mathrm{e}^{\mathrm{i}\varphi} = \cos \varphi + \mathrm{i} \sin \varphi
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Exponent Arithmetic
>
>The [complex exponential function](./Complex%20Exponential%20Function.md) has the following property for all $z, w \in \mathbb{C}$:
>
>$$
>\mathrm{e}^{z + w} = \mathrm{e}^z \cdot \mathrm{e}^w \qquad \forall z,w \in \mathbb{C}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Modulus of the Complex Exponential
>
>For all $z \in \mathbb{C}$, the [modulus](../../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md) of the [complex exponential function](./Complex%20Exponential%20Function.md) of $z$ is the [real exponential](../../Real%20Analysis/Real%20Functions/Real%20Exponentiation.md) of its [real part](../Complex-Valued%20Functions.md):
>
>$$
>|\mathrm{e}^z| = \mathrm{e}^{\operatorname{Re}(z)}
>$$
>
>>[!PROOF]-
>>
>>Let $x = \operatorname{Re}(z)$ and $y = \operatorname{Im}(z)$.
>>
>>$$
>>\begin{aligned}
>>
>>|\mathrm{e}^z| = \left| \mathrm{e}^{x + \mathrm{i} y} \right| &= \left| \mathrm{e}^{x} \cdot \mathrm{e}^{\mathrm{i} y} \right| \\ &= \left| \mathrm{e}^{x} \cdot \cos y + \mathrm{i} \sin y \right| \\ &= \left| \mathrm{e}^{x} \sqrt{\cos^2 y + \sin^2 y} \right| \\ &= \left|\mathrm{e}^{x} \cdot \sqrt{1}\right| \\ &= \left|\mathrm{e}^{\operatorname{Re}(z)}\right| = \mathrm{e}^{\operatorname{Re}(z)}
>>
>>\end{aligned}
>>$$
>>
>

>[!THEOREM] Theorem: Conjugation of the Complex Exponential
>
>The [conjugate](../../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md#Operations) of the [complex exponential](#The%20Complex%20Exponential%20Function) is the [complex exponential](#The%20Complex%20Exponential%20Funcion) of the [conjugate](../../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md#Operations):
>
>$$
>\overline{\mathrm{e}^z} = \mathrm{e}^{\overline{z}}
>$$
>
>>[!PROOF]-
>>
>>PROOF
>>
>

>[!THEOREM] Theorem: Complex Exponential via Complex Limit
>
>The [complex exponential function](#The%20Complex%20Exponential%20Function) $\mathrm{e}^z$ is equal to the following [limit](../Complex%20Sequences.md#Convergence):
>
>$$
>\mathrm{e}^z = \lim_{n \to \infty}\left(1 + \frac{z}{n}\right)^n
>$$
>
>>[!PROOF]-
>>
>>We need to prove that for each $\varepsilon \gt 0$, there exists some $N \in \mathbb{N}_0$ such that
>>
>>$$
>>\left\vert \left(1 + \frac{z}{n}\right)^n - \sum_{k=0}^{\infty}\frac{z^k}{k!} \right\vert \lt \varepsilon
>>$$
>>
>>for all $n \ge N$.
>>
>>TODO
>>
>