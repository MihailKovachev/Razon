---
tags:
    - real-analysis
    - analysis
    - mathematics
---

# Differentiability (Real Functions)

>[!DEFINITION] Definition: Differentiability (Real Functions)
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $p \in \mathcal{D}$ be an [accumulation point](../../../Topology/Accumulation%20Points.md) of $\mathcal{D}$.
>
>We say that $f$ is **differentiable** at $p$ if the [limit](./Limits%20(Real%20Functions).md)
>
>$$\lim_{x \to p} \frac{f(x) - f(p)}{x - p}$$
>
>exists and is finite. In this case, the value of this [limit](./Limits%20(Real%20Functions).md) is known as $f$'s **derivative** at $p$.
>
>For $S \subseteq \mathcal{D}$, we say that $f$ is **differentiable on** $S$ if it is [differentiable](#Differentiability%20(Real%20Functions)) at each $x \in S$.
>
>>[!NOTATION]
>>
>>We denote $f$'s [derivative](#Differentiability%20(Real%20Functions)) at $p$ as $f'(p)$. If a specific label such as $x$, $t$, etc. is used for $f$'s input, then we also denote it in one of the following ways:
>>
>>$$\left.\frac{\mathrm{d}f}{\mathrm{d}x}\right\vert_{x=p} \qquad \left.\frac{\mathrm{d}f}{\mathrm{d}t}\right\vert_{t=p} \qquad \frac{\mathrm{d}f}{\mathrm{d}x}(p)$$
>>
>

>[!THEOREM] Theorem: Differentiability at Interior Points
>
>A [real function](./Real%20Functions.md) $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ is [differentiable](./Differentiability%20(Real%20Functions).md) at an [interior point](../../../Topology/Interior,%20Boundary,%20Exterior.md) $p$ of $\mathcal{D}$ if and only if the [limit](./Limits%20(Real%20Functions).md)
>
>$$\lim_{h \to 0} \frac{f(p+h) - f(p)}{h}$$
>
>exists and is finite. In this case, the value of this [limit](./Limits%20(Real%20Functions).md) is $f'(p)$.
>
>>[!EXAMPLE]- Example: $f(x) = ax + b$
>>
>>We want to find the [derivative](./Differentiability%20(Real%20Functions).md) at each $x \in \mathbb{R}$ of the [function](./Real%20Functions.md) $f: \mathbb{R} \to \mathbb{R}$ defined as
>>
>>$$f(x) = ax + b,$$
>>
>>where $a, b \in \mathbb{R}$. Since every $x$ is an [interior point](../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathbb{R}$, we have:
>>
>>$$\begin{aligned}f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h} &= \frac{a(x+h) + b - (ax + b)}{h} \\ &= \lim_{h\to 0}\frac{ax + ah + b - ax - b}{h} \\ &= \lim_{h \to \infty} \frac{ah}{h} = a\end{aligned}$$
>>
>>Therefore:
>>
>>$$f'(x) = a$$
>>
>
>>[!EXAMPLE]- Example: $f(x) = x^2$
>>
>>We want to find the [derivative](./Differentiability%20(Real%20Functions).md) at each $x \in \mathbb{R}$ of the following [function](./Real%20Functions.md) $f: \mathbb{R} \to \mathbb{R}$:
>>
>>$$f(x) = x^2$$
>>
>>Since every $x$ is an [interior point](../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathbb{R}$, we have:
>>
>>$$\begin{aligned}f'(x) = \lim_{h \to 0} \frac{(x + h)^2 - x^2}{h} &= \lim_{h \to 0} \frac{x^2 + 2xh + h^2 -x^2}{h} \\ & = \lim_{h \to 0} \frac{2xh + h^2}{h} \\ &= \lim_{h \to 0} (2x + h) = 2x\end{aligned}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!DEFINITION] Definition: Critical Point
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $p \in \mathcal{D}$.
>
>We say $p$ is a **critical point** of $f$ if $f$ is not [differentiable](./Differentiability%20(Real%20Functions).md) at $x_0$ or its [derivative](./Differentiability%20(Real%20Functions).md) there is zero.
>

>[!THEOREM] Theorem: Differentiability $\implies$ Continuity
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $p \in \mathcal{D}$ be an [accumulation point](../../../Topology/Accumulation%20Points.md) of $\mathcal{D}$.
>
>If $f$ is [differentiable](./Differentiability%20(Real%20Functions).md) at $p$, then $f$ is also [continuous](./Continuity%20(Real%20Functions).md) at $p$.
>
>>[!PROOF]-
>>
>>We need to show that $f(p)$ is equal to the [limit](./Limits%20(Real%20Functions.md) of $f$ at $p$:
>>
>>$$
>>\lim_{x \to p} f(x) = f(p)
>>$$
>>
>>With the substition $h = x - p$, we get the following:
>>
>>$$
>>\lim_{x \to p} f(x) = f(p) \iff \lim_{h \to 0} (f(p + h) - f(p)) = 0
>>$$
>>
>>This means that we need to show that $\lim_{h \to 0} (f(p + h) - f(p)) = 0$. 
>>
>>We have the following:
>>
>>$$
>>\lim_{h \to 0} (f(p + h) - f(p)) = \lim_{h \to 0}\left(h \times \frac{f(p + h) - f(p)}{h}\right) = 0 \cdot f'(p) = 0
>>$$
>>
>

>[!THEOREM] Mean Value Theorem for Derivatives
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
>
>If $f$ is [continuous](./Continuity%20(Real%20Functions).md) on the [closed interval](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) $[a;b]$ and is [differentiable](./Differentiability%20(Real%20Functions).md) on the [open interval](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) $(a;b)$, then there exists as least one $\xi \in (a;b)$ such that
>
>$$
>f'(\xi) = \frac{f(b) - f(a)}{b - a}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Darboux's Theorem
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $[a;b]$ be a [closed interval](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) such that $[a;b] \subseteq \mathcal{D}$.
>
>If $f$ is [differentiable](./Differentiability%20(Real%20Functions).md) on the [open interval](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) $(a;b)$, then for each $\lambda \in \mathbb{R}$ such that $f'(a) \lt \lambda \lt f'(b)$ or $f'(a) \gt \lambda \gt f'(b)$, there exists some $c \in (a;b)$ such that
>
>$$
>f'(c) = \lambda
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Power Rule
>
>For all $r \in \mathbb{R}$, the [exponentiation](./Real%20Exponentiation.md) $x^r$ is [differentiable](./Differentiability%20(Real%20Functions).md) with
>
>$$
>(x^r)' = rx^{r-1}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: $(\sqrt{x})'$
>>
>>We can use this to find the [derivative](./Differentiability%20(Real%20Functions).md) of $\sqrt{x}$:
>>
>>$$
>>(\sqrt{x})' = \left(x^{\frac{1}{2}}\right)' = \frac{1}{2}x^{-\frac{1}{2}} = \frac{1}{2\sqrt{x}}
>>$$
>>
>

>[!THEOREM] Theorem: Linearity of Differentiation
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$  and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be a [real functions](../Real-Valued%20Functions.md).
>
>If $f$ and $g$ are both [differentiable](./Differentiability%20(Real%20Functions).md) on $S \subseteq \mathcal{D}_f \cap \mathcal{D}_g$, then $\alpha f + \beta g$ is also [differentiable](./Differentiability%20(Real%20Functions).md) on $S$ for all $\alpha, \beta \in \mathbb{R}$ with
>
>$$
>(\alpha f + \beta g)' = \alpha f' + \beta g'
>$$
>
>>[!PROOF]-
>>
>>$$
>>\begin{aligned}[\lambda\, f(x) + \mu\, g(x)]' &= \operatorname*{lim}_{h\rightarrow0}\frac{\lambda f(x_{0}+h)+\mu g(x_{0}+h) - \lambda f(x_{0})-\mu g(x_{0})}{h}\\ &= \lim_{h\to 0}\frac{\lambda[f(x_{0}+h)-f(x_{0})] + \mu[g(x_{0}+h)-g(x_{0})]}{h} \\ &= \lim_{h\to 0}\lambda\frac{f(x_0+h)-f(x_0)}{h} + \lim_{h\to 0}\mu\frac{g(x_0+h)-g(x_0)}{h} \\ &= \lambda\lim_{h\to 0}\frac{f(x_0+h)-f(x_0)}{h} + \mu\lim_{h\to 0}\frac{g(x_0+h)-g(x_0)}{h} \\ &= \lambda f'(x_0) + \mu g'(x_0)\end{aligned}
>>$$
>>
>

>[!THEOREM] Theorem: Product Rule
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$  and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be a [real functions](../Real-Valued%20Functions.md#Real%20Functions).
>
>If $f$ and $g$ are both [differentiable](./Differentiability%20(Real%20Functions).md) on $S \subseteq \mathcal{D}_f \cap \mathcal{D}_g$, then their [product](../Real-Valued%20Functions.md#Real%20Functions) $fg$ is also [differentiable](./Differentiability%20(Real%20Functions).md) on $S$ with
>
>$$
>(fg)' = f'g+ fg'
>$$
>
>>[!PROOF]-
>>
>>$$
>>\begin{aligned}
>>(f(x)g(x))' &= \lim_{h\to 0} \frac{f(x + h)g(x+h)-f(x)g(x)}{h} \\ &= \lim_{h \to 0} \frac{f(x+h)g(x+h) - f(x+h)g(x)+f(x+h)g(x)-f(x)g(x)}{h} \\ &= \lim_{h \to 0}\left(f(x+h)\frac{g(x+h)-g(x)}{h} + g(x)\frac{f(x+h)-f(x)}{h}\right) \\ &= \left(\lim_{h \to 0}f(x+h)\right)\left(\lim_{h\to 0} \frac{g(x+h)-g(x)}{h} \right) + \left(\lim_{h \to 0}g(x)\right)\left(\lim_{h\to 0} \frac{f(x+h)-f(x)}{h}\right) \\ &= \left(\lim_{h\to 0} f(x + h)\right) g'(x) + g(x)f'(x)
>>\end{aligned}
>>$$
>>
>>Since $f$ is [differentiable](./Differentiability%20(Real%20Functions).md) at $x$, it must also be [continuous](./Continuity%20(Real%20Functions).md) there, i.e. $\lim_{h \to 0}f(x +h) = f(x)$. Therefore, we have:
>>
>>$$
>>(f(x)g(x))' = f(x)g'(x) + g(x)f'(x)
>>$$
>>
>

>[!THEOREM] Theorem: Quotient Rule
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$  and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be a [real functions](../Real-Valued%20Functions.md#Real%20Functions).
>
>If $f$ and $g$ are both [differentiable](./Differentiability%20(Real%20Functions).md) at $x \in \mathcal{D}_f \cap \mathcal{D}_g$ and $g(x) \ne 0$, then their [quotient](../Real-Valued%20Functions.md#Real%20Functions) $f/g$ is also [differentiable](./Differentiability%20(Real%20Functions).md) at $x$ with
>
>$$
>\left(\frac{f(x)}{g(x)}\right)' = \frac{f'(x)g(x)-f(x)g'(x)}{g(x)^2}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Chain Rule
>
>Let $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ also be a [real function](./Real%20Functions.md) such that the [image](../../Functions/Functions.md) of $g$ is contained in the [domain](../../Functions/Functions.md) of $f$, i.e. $g(\mathcal{D}_g) \subseteq \mathcal{D}_f$.
>
>If $g$ is [differentiable](./Differentiability%20(Real%20Functions).md) at some $x \in \mathcal{D}_g$ and $f$ is [differentiable](./Differentiability%20(Real%20Functions).md) at $g(x)$, then their [composition](../../Functions/Functions.md) $f \circ g: \mathcal{D}_g \to \mathbb{R}$ is also [differentiable](./Differentiability%20(Real%20Functions).md) at $x$ with
>
>$$
>(f\circ g)'(x) = f'(g(x)) g'(x)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: General Power Rule
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$  and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be a [real functions](../Real-Valued%20Functions.md#Real%20Functions).
>
>If $f$ and $g$ are both [differentiable](./Differentiability%20(Real%20Functions).md) at $x \in \mathcal{D}_f \cap \mathcal{D}_g$ and $f(x) \gt 0$, then the [exponentiation](./Real%20Exponentiation.md) $f^g$ is also [differentiable](./Differentiability%20(Real%20Functions).md) at $x$ with
>
>$$
>\left(f(x)^{g(x)}\right)' = f(x)^{g(x)}\left(f'(x)\frac{g(x)}{f(x)} + g'(x)\ln(f(x))\right),
>$$
>
>where $\ln$ is the [real natural logarithm](./Real%20Logarithms.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Derivatives of Inverse Functions
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be an [injective](../../Functions/Injections,%20Surjections%20and%20Bijections.md#Injections) [real function](./Real%20Functions.md) and let $y \in f(\mathcal{D})$.
>
>If $f$ is [differentiable](./Differentiability%20(Real%20Functions).md) at $f^{-1}(y)$ with $f'(f^{-1}(y)) \ne 0$ and its [inverse function](../../Functions/Injections,%20Surjections%20and%20Bijections.md#Injections) $f^{-1}: f(\mathcal{D}) \to \mathcal{D}$ is [continuous](./Continuity%20(Real%20Functions).md) at $y$, then $f^{-1}$ is [differentiable](./Differentiability%20(Real%20Functions).md) at $y$ with
>
>$$
>(f^{-1})'(y) = \frac{1}{f'(f^{-1}(y))}
>$$
>
>>[!PROOF]-
>>
>>Since $y \in f(\mathcal{D})$, we have $y = f(x)$ for some unique $x \in \mathcal{D}$. 
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: $(\arcsin x)'$
>>
>>The [restriction](../../Functions/Functions.md) of the [sine function](./Real%20Trigonometric%20Functions/Real%20Trigonometric%20Functions.md#The%20Real%20Sine%20Function) on $\left[\frac{-\pi}{2}; \frac{\pi}{2}\right]$ is [injective](../../Functions/Injections,%20Surjections%20and%20Bijections.md#Injections) and [differentiable](./Differentiability%20(Real%20Functions).md) with $\sin '(x) \ne 0$. We can therefore use the aforementioned theorem to find the [derivative](./Differentiability%20(Real%20Functions).md) of the [arcsine function](./Real%20Trigonometric%20Functions/Inverse%20Real%20Trigonometric%20Functions.md#The%20Real%20Arcsince%20Function):
>>
>>$$
>>(\arcsin y)' = \frac{1}{\sin'(\arcsin y)} = \frac{1}{\cos (\arcsin y)}
>>$$
>>
>>On $\left[\frac{-\pi}{2}; \frac{\pi}{2}\right]$ we know that $\cos x = \sqrt{1 - \sin x}$ and since $\sin(\arcsin y) = y$, we get:
>>
>>$$
>>(\arcsin y)' = \frac{1}{\sqrt{1-y^2}}
>>$$
>>
>

## Higher Order Differentiability

>[!DEFINITION] Definition: Higher Order Differentiability (Real Functions)
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $n \in \mathbb{N}_{\ge 0}$.
>
>For $n = 0$: We say that $f$ is **0-times differentiable at** each $p \in \mathcal{D}$ and **0-times differentiable on** each $S \subseteq \mathcal{D}$. The **zeroth-order derivative function** of $f$ is $f$.
>
>For $n \ge 1$:
>
>We say that $f$ is **$n$-times differentiable at** $p \in \mathcal{D}$ if $p$ is an [accumulation point](../../../Topology/Accumulation%20Points.md) of the [domain](../../Functions/Functions.md) $\mathcal{D}^{(n-1)}$ of $f$'s $(n-1)$-th [derivative function](#Higher%20Order%20Differentiability) $f^{(n-1)}: \mathcal{D}^{(n-1)} \to \mathbb{R}$ and $f^{(n-1)}$ is [differentiable](./Differentiability%20(Real%20Functions).md) at $p$. In this case, the [derivative](./Differentiability%20(Real%20Functions).md) of $f^{(n-1)}$ at $p$ is known as $f$'s **$n$-th order derivative at** $p$. For $S \subseteq \mathcal{D}$, we say that $f$ is **$n$-times differentiable on** $S$ if $f$ is [$n$-times differentiable](#Higher%20Order%20Differentiability) at each $x \in S$.
>
>The **$n$-th order derivative function** of $f$ is the [real function](./Real%20Functions.md) $f^{(n)}: \mathcal{D}^{(n)} \to \mathbb{R}$ whose [domain](../../Functions/Functions.md) $\mathcal{D}^{(n)}$ is the [set](../../../Set%20Theory/Sets.md) of all $x \in \mathcal{D}$ at which $f$ is [$n$-times differentiable](#Higher%20Order%20Differentiability) and which maps each $x \in \mathcal{D}^{(n)}$ to $f$'s [$n$-th order derivative](#Higher%20Order%20Differentiability) at $x$.
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
>We say that $f$ is **continuously $n$-times differentiable at** $p \in \mathcal{D}$ if $f$ is [$n$-times differentiable](#Higher%20Order%20Differentiability) at $p$ and its [$n$-th order derivative function](#Higher%20Order%20Differentiability) is [continuous](./Continuity%20(Real%20Functions).md) at $p$.
>
>We say that $f$ is **continuously $n$-times differentiable on** $S \subseteq \mathcal{D}$ if $f$ is [$n$-times differentiable](#Higher%20Order%20Differentiability) on $S$ and its [$n$-th order derivative function](#Higher%20Order%20Differentiability) is [continuous](./Continuity%20(Real%20Functions).md) on $S$.
>
>>[!NOTATION]
>>
>>When $f$ is [$n$-times continuously differentiable](#Higher%20Order%20Differentiability) on $S$, we say that "$f$ is $C^n$ on $S$" or we write $f \in C^n(S)$.
>>
>

>[!THEOREM] Theorem: Higher-Order Product Rule
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$  and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be a [real functions](../Real-Valued%20Functions.md#Real%20Functions).
>
>If $f$ and $g$ are both $n$-[times differentiable](./Differentiability%20(Real%20Functions).md) on $S \subseteq \mathcal{D}_f \cap \mathcal{D}_g$, then their [product](../Real-Valued%20Functions.md#Real%20Functions) is also $n$[-times differentiable](./Differentiability%20(Real%20Functions).md) on $S$ with
>
>$$(fg)^{(n)} = \sum_{k = 0}^n \binom{n}{k} f^{(n-k)}g^{(k)}$$
>
>>[!PROOF]-
>>
>>The proof is by [induction](../../../Logic/Mathematical%20Induction.md).
>>
>>**Base case** ($n = 0$):
>>
>>We have $(fg)^{(0)} = fg$ and $\sum_{k = 0}^0 \binom{n}{k} f^{(n-k)}g^{(k)} = f^{(0 - 0)}g^{(0)} = fg$.
>>
>>**Induction hypothesis**: There exists some $n \in \mathbb{N}_0$ such that $(fg)^{(n)} = \sum_{k = 0}^n \binom{n}{k} f^{(n-k)}g^{(k)}$ implies that $(fg)^{(n+1)} = \sum_{k = 0}^{n+1} \binom{n+1}{k} f^{(n-k+1)}g^{(k)}$.
>>
>>**Inductive step:**
>>
>>$$\begin{aligned}(fg)^{(n+1)} = ((fg)^{(n)})' & = \left(\sum_{k = 0}^n \binom{n}{k} f^{(n-k)}g^{(k)}\right)' \\ & = \sum_{k = 0}^n \binom{n}{k}(f^{(n-k)}g^{(k)})' \\ & = \sum_{k = 0}^n \binom{n}{k} (f^{(n-k)})'g^{(k)} + f^{(n-k)}(g^{(k)})'\\ & = \sum_{k = 0}^{n+1} \binom{n+1}{k} f^{(n-k+1)}g^{(k)}\end{aligned}$$
>>
>