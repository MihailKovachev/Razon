---
tags:
    - complex-analysis
    - analysis
    - mathematics
---

# Differentiability (Complex Functions)

>[!DEFINITION] Definition: Differentiability (Complex Functions)
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](./Complex%20Functions.md) and let $p \in \mathcal{D}$ be an [accumulation point](../../../Topology/Accumulation%20Points.md) of $\mathcal{D}$.
>
>We say that $f$ is **differentiable** at $p$ if the [limit](./Limits%20(Complex%20Functions).md)
>
>$$\lim_{z \to p} \frac{f(z) - f(p)}{z - p}$$
>
>exists and is finite, then we say that $f$ is **differentiable** at $p$. In this case, the value of this [limit](./Limits%20(Complex%20Functions).md) is known as $f$'s **derivative** at $p$.
>
>For $S \subseteq \mathcal{D}$, we say that $f$ is **differentiable on** $S$ if it is [differentiable](#Differentiability%20(Complex%20Functions)) at each $x \in S$.
>
>>[!NOTATION]
>>
>>$$f'(p) \qquad \frac{\mathrm{d}f}{\mathrm{d}z}(p)$$
>>
>

## Higher Order Differentiability

>[!DEFINITION] Definition: Higher Order Differentiability (Complex Functions)
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](./Complex%20Functions.md) and let $n \in \mathbb{N}_{\ge 0}$.
>
>For $n = 0$: We say that $f$ is **0-times differentiable at** each $p \in \mathcal{D}$ and **0-times differentiable on** each $S \subseteq \mathcal{D}$. The **zeroth-order derivative function** of $f$ is $f$.
>
>For $n \ge 1$:
>
>We say that $f$ is **$n$-times differentiable at** $p \in \mathcal{D}$ if $p$ is an [accumulation point](../../../Topology/Accumulation%20Points.md) of the [domain](../../Functions/Functions.md) $\mathcal{D}^{(n-1)}$ of $f$'s $(n-1)$-th [derivative function](#Higher%20Order%20Differentiability) $f^{(n-1)}: \mathcal{D}^{(n-1)} \to \mathbb{R}$ and $f^{(n-1)}$ is [differentiable](./Differentiability%20(Complex%20Functions).md) at $p$. In this case, the [derivative](./Differentiability%20(Complex%20Functions).md) of $f^{(n-1)}$ at $p$ is known as $f$'s **$n$-th order derivative at** $p$. For $S \subseteq \mathcal{D}$, we say that $f$ is **$n$-times differentiable on** $S$ if $f$ is [$n$-times differentiable](#Higher%20Order%20Differentiability) at each $x \in S$.
>
>The **$n$-th order derivative function** of $f$ is the [complex function](./Complex%20Functions.md) $f^{(n)}: \mathcal{D}^{(n)} \to \mathbb{R}$ whose [domain](../../Functions/Functions.md) $\mathcal{D}^{(n)}$ is the [set](../../../Set%20Theory/Sets.md) of all $x \in \mathcal{D}$ at which $f$ is [$n$-times differentiable](#Higher%20Order%20Differentiability) and which maps each $x \in \mathcal{D}^{(n)}$ to $f$'s [$n$-th order derivative](#Higher%20Order%20Differentiability) at $x$.
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
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ and let $n \in \mathbb{N}_{\ge 0}$.
>
>We say that $f$ is **continuously $n$-times differentiable at** $p \in \mathcal{D}$ if $f$ is [$n$-times differentiable](#Higher%20Order%20Differentiability) at $p$ and its [$n$-th order derivative function](#Higher%20Order%20Differentiability) is [continuous](./Continuity%20(Complex%20Functions).md) at $p$.
>
>We say that $f$ is **continuously $n$-times differentiable on** $S \subseteq \mathcal{D}$ if $f$ is [$n$-times differentiable](#Higher%20Order%20Differentiability) on $S$ and its [$n$-th order derivative function](#Higher%20Order%20Differentiability) is [continuous](./Continuity%20(Complex%20Functions).md) on $S$.
>
>>[!NOTATION]
>>
>>When $f$ is [$n$-times continuously differentiable](#Higher%20Order%20Differentiability) on $S$, we say that "$f$ is $C^n$ on $S$" or we write $f \in C^n(S)$.
>>
>

>[!THEOREM] Theorem: Differentiability $\implies$ Infinite Differentiability
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](./Complex%20Functions.md) and let $U \subseteq \mathcal{D}$ be [open](../../../Topology/Topological%20Spaces/Open%20Sets.md) in the [complex plane](../Complex%20Plane.md).
>
>If $f$ is [differentiable](./Differentiability%20(Complex%20Functions).md) on $U$, then $f$ is [infinitely differentiable](./Differentiability%20(Complex%20Functions).md) on $U$.
>
>>[!PROOF]-
>>
>>TODO
>>
>