---
tags:
    - complex-analysis
    - real-analysis
    - analysis
    - mathematics
---

# Differentiability (Complex-Valued Functions of a Real Variable)

>[!DEFINITION] Definition: Differentiability (Complex-Valued Functions of a Real Variable)
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{C}$ be a [complex-valued function of a real variable](./Complex-Valued%20Function%20of%20a%20Real%20Variable.md) and let $p \in \mathbb{D}$ be an [accumulation point](../../../Topology/Accumulation%20Points.md) of $\mathcal{D}$.
>
>We say that $f$ is **differentiable** at $p$ if the [limit](./Limits%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable).md)
>
>$$\lim_{x \to p} \frac{f(x) - f(p)}{x - p}$$
>
>exists and is finite. In this case, the value of this [limit](./Limits%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable).md) is known as $f$'s **derivative** at $p$.
>
>For $S \subseteq \mathcal{D}$, we say that $f$ is **differentiable on** $S$ if it is [differentiable](#Differentiability%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable)) at each $x \in S$.
>
>>[!NOTATION]
>>
>>We denote $f$'s [derivative](#Differentiability%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable)) at $p$ as $f'(p)$. If a specific label such as $x$, $t$, etc. is used for $f$'s input, then we also denote it in one of the following ways:
>>
>>$$\left.\frac{\mathrm{d}f}{\mathrm{d}x}\right\vert_{x=p} \qquad \left.\frac{\mathrm{d}f}{\mathrm{d}t}\right\vert_{t=p} \qquad \frac{\mathrm{d}f}{\mathrm{d}x}(p)$$
>>
>

## Higher Order Differentiability

>[!DEFINITION] Definition: Higher Order Differentiability (Complex-Valued Functions of a Real Variable)
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{C}$ be a [complex-valued function of a real variable](./Complex-Valued%20Function%20of%20a%20Real%20Variable.md) and let $n \in \mathbb{N}_{\ge 0}$.
>
>For $n = 0$: We say that $f$ is **0-times differentiable at** each $p \in \mathcal{D}$ and **0-times differentiable on** each $S \subseteq \mathcal{D}$. The **zeroth-order derivative function** of $f$ is $f$.
>
>For $n \ge 1$:
>
>We say that $f$ is **$n$-times differentiable at** $p \in \mathcal{D}$ if $p$ is an [accumulation point](../../../Topology/Accumulation%20Points.md) of the [domain](../../Functions/Functions.md) $\mathcal{D}^{(n-1)}$ of $f$'s $(n-1)$-th [derivative function](#Higher%20Order%20Differentiability) $f^{(n-1)}: \mathcal{D}^{(n-1)} \to \mathbb{C}$ and $f^{(n-1)}$ is [differentiable](#Differentiability%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable)) at $p$. In this case, the [derivative](#Differentiability%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable)) of $f^{(n-1)}$ at $p$ is known as $f$'s **$n$-th order derivative at** $p$. For $S \subseteq \mathcal{D}$, we say that $f$ is **$n$-times differentiable on** $S$ if $f$ is [$n$-times differentiable](#Higher%20Order%20Differentiability) at each $x \in S$.
>
>The **$n$-th order derivative function** of $f$ is the [complex-valued function of a real variable](./Complex-Valued%20Function%20of%20a%20Real%20Variable.md) $f^{(n)}: \mathcal{D}^{(n)} \to \mathbb{C}$ whose [domain](../../Functions/Functions.md) $\mathcal{D}^{(n)}$ is the [set](../../../Set%20Theory/Sets.md) of all $x \in \mathcal{D}$ at which $f$ is [$n$-times differentiable](#Higher%20Order%20Differentiability) and which maps each $x \in \mathcal{D}^{(n)}$ to $f$'s [$n$-th order derivative](#Higher%20Order%20Differentiability) at $x$.
>
>>[!NOTATION]
>>
>>The [derivative functions](#Higher%20Order%20Differentiability) are denoted as follows:
>>
>>$$f' \qquad f'' \qquad f''' \qquad f^{\text{IV}} \qquad f^{\text{V}} \qquad \cdots \qquad f^{(n)}$$
>>
>>$$\frac{\mathrm{d}f}{\mathrm{d}x} \qquad \frac{\mathrm{d}^2 f}{\mathrm{d}x^2} \qquad \frac{\mathrm{d}^3 f}{\mathrm{d}x^3} \qquad \frac{\mathrm{d}^4 f}{\mathrm{d}x^4} \qquad  \frac{\mathrm{d}^5 f}{\mathrm{d}x^5} \qquad \cdots \qquad \frac{\mathrm{d}^n f}{\mathrm{d}x^n}$$
>>
>
>>[!DEFINITION] Definition: Infinite Differentiability
>>
>>We say that $f$ is **infinitely differentiable at** $p \in \mathcal{D}$ if $f$ is [$n$-times differentiable](#Higher%20Order%20Differentiability) at $p$ for all $n \in \mathbb{N}_{\ge 0}$.
>>
>>>[!NOTATION]
>>>
>>>When $f$ is [infinitely differentiable](#Higher%20Order%20Differentiability) on $S$, we say that "$f$ is $C^{\infty}$ on $S$" or we write $f \in C^{\infty}(S)$.
>>>
>>>
>>
>

>[!DEFINITION] Definition: Continuous Higher Order Differentiability
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{C}$ be a [complex-valued function of a real variable](./Complex-Valued%20Function%20of%20a%20Real%20Variable.md) and let $n \in \mathbb{N}_{\ge 0}$.
>
>We say that $f$ is **continuously $n$-times differentiable at** $p \in \mathcal{D}$ if $f$ is [$n$-times differentiable](#Higher%20Order%20Differentiability) at $p$ and its [$n$-th order derivative function](#Higher%20Order%20Differentiability) is [continuous](./Continuity%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable).md) at $p$.
>
>We say that $f$ is **continuously $n$-times differentiable on** $S \subseteq \mathcal{D}$ if $f$ is [$n$-times differentiable](#Higher%20Order%20Differentiability) on $S$ and its [$n$-th order derivative function](#Higher%20Order%20Differentiability) is [continuous](./Continuity%20(Complex-Valued%20Functions%20of%20a%20Real%20Variable).md) on $S$.
>
>>[!NOTATION]
>>
>>When $f$ is [$n$-times continuously differentiable](#Higher%20Order%20Differentiability) on $S$, we say that "$f$ is $C^n$ on $S$" or we write $f \in C^n(S)$.
>>
>

## Piecewise Differentiability

>[!DEFINITION] Definition: Piecewise (Continuous) Differentiability (Complex-Valued Functions of a Real Variable)
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{C}$ be a [complex-valued function of a real variable](./Complex-Valued%20Function%20of%20a%20Real%20Variable.md) and let $n \in \mathbb{N}_{\ge 0}$.
>
>We say that $f$ is **$n$-times piecewise (continuously) differentiable on** a [closed interval](../../../Set%20Theory/Orderings/Interval.md) $[a,b] \subseteq \mathcal{D}$ if there exist $t_0, t_1, \dotsc, t_k \in [a,b]$ with $a = t_0 \lt t_1 \lt \cdots \lt t_k = b$ and such that $f$ is [$n$-times (continuously) differentiable](#Higher%20Order%20Differentiability) on $[t_{i-1}, t_i]$ for each $i \in \{1, \dotsc, k\}$.
>