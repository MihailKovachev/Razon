---
tags:
  - real-analysis
  - analysis
  - mathematics
---

# Antidifferentiability (Real Functions)

>[!DEFINITION] Definition: Antiderivative
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $S \subseteq \mathcal{D}_f$.
>
>An **antiderivative** of $f$ on $S$ is any [real function](./Real%20Functions.md) $F: \mathcal{D}_F \subseteq \mathbb{R} \to \mathbb{R}$ which is [differentiable](./Differentiability%20(Real%20Functions).md) on $S$ with
>
>$$F'(x) = f(x)$$
>
>for all $x \in S$.
>
>>[!DEFINITION] Definition: Antidifferentiability
>>
>>We say that $f$ is **antidifferentiable** on $S$ if it has an [antiderivative](./Antidifferentiability%20(Real%20Functions).md) on $S$.
>>
>
>>[!EXAMPLE]-
>>
>>Consider the [function](./Real%20Functions.md) $f: \mathbb{R} \to \mathbb{R}$ defined as
>>
>>$$f(x) \overset{\text{def}}{=} 3x$$
>>
>>for all $x \in \mathbb{R}$.
>>
>>The [functions](./Real%20Functions.md) $F_1, F_2, F_3: \mathbb{R} \to \mathbb{R}$ defined as
>>
>>$$\begin{aligned}F_1(x) & \overset{\text{def}}{=} \frac{3}{2}x^2 \\ F_2(x) & \overset{\text{def}}{=} \frac{3}{2}x^2 + 7 \\ F_1(x) & \overset{\text{def}}{=} \frac{3}{2}x^2 - \pi \end{aligned}$$
>>
>>for all $x \in \mathbb{R}$ are [antiderivatives](./Antidifferentiability%20(Real%20Functions).md) of $f$ on $\mathbb{R}$.
>>
>

>[!THEOREM] Theorem: Derivative of Antiderivative Difference
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $S \subseteq \mathcal{D}$.
>
>If $H: \mathcal{D}_H \subseteq \mathbb{R} \to \mathbb{R}$ and $G: \mathcal{D}_G \subseteq \mathbb{R} \to \mathbb{R}$ are [antiderivatives](./Antidifferentiability%20(Real%20Functions).md) of $f$ on $S$, then the [derivative](./Differentiability%20(Real%20Functions).md) of their difference $H-G: \mathcal{D}_H \cap \mathcal{D}_G \to \mathbb{R}$ is zero for all $x \in S$:
>
>$$(H - G)'(x) = 0 \qquad \forall x \in S$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antiderivatives on Intervals
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md), let $I \subseteq \mathcal{D}$ be an [interval](../../../Set%20Theory/Orderings/Interval.md).
>
>If $H: \mathcal{D}_H \subseteq \mathbb{R} \to \mathbb{R}$ and $G: \mathcal{D}_G \subseteq \mathbb{R} \to \mathbb{R}$ are [antiderivatives](./Antidifferentiability%20(Real%20Functions).md) of $f$ on $I$, then there exists some $C \in \mathbb{R}$ such that
>
>$$H(x) = G(x) + C$$
>
>for all $x \in I$.
>
>>[!NOTATION]
>>
>>This fact allows us to introduce simplified notation for the [indefinite integral](./Antidifferentiability%20(Real%20Functions).md). Instead of writing
>>
>>$$\int f(x) \,\mathrm{d}x = \{F\mid F \text{ is an antiderivative of } f \text{ on } I\},$$
>>
>>we write
>>
>>$$\int f(x) \,\mathrm{d}x = F(x) + C,$$
>>
>>where $F$ is any particular [antiderivative](./Antidifferentiability%20(Real%20Functions).md).
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Linearity of Antidifferentiation
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](./Real%20Functions.md)
>
>If $f$ and $g$ are [antidifferentiable](./Antidifferentiability%20(Real%20Functions).md) on $S \subseteq \mathcal{D}_f \cap \mathcal{D}_g$, then so is $\alpha f + \beta g$ for all $\alpha, \beta \in \mathbb{R}$ with
>
>$$\int \alpha f(x) + \beta g(x) \,\mathrm{d}x = \alpha \int f(x) \,\mathrm{d}x +  \beta \int g(x) \,\mathrm{d}x.$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Integration by Parts
>
>Let $u: \mathcal{D}_u \subseteq \mathbb{R} \to \mathbb{R}$ and $v: \mathcal{D}_v \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](./Real%20Functions.md) and let $S \subseteq \mathcal{D}_u \cap \mathcal{D}_v$. 
>
>If $u$ and $v$ are [continuously differentiable](./Differentiability%20(Real%20Functions).md) on $S$, then the [antiderivatives](./Antidifferentiability%20(Real%20Functions).md) of $uv'$ are related to the [antiderivatives](./Antidifferentiability%20(Real%20Functions).md) of $u'v$ as follows:
>
>$$\int u(x) v'(x) \mathop{\mathrm{d}x} = u(x)v(x) - \int u'(x)v(x) \mathop{\mathrm{d}x}$$
>
>>[!PROOF]-
>>
>>We begin using the [product rule](./Differentiability%20(Real%20Functions).md) for [differentiation](./Differentiability%20(Real%20Functions).md):
>>
>>$$(u(x)v(x))' = u'(x)v(x) + u(x)v'(x)$$
>>
>>Now, the [antiderivatives](./Antidifferentiability%20(Real%20Functions).md) of the left-hand side must be equal to [antiderivatives](./Antidifferentiability%20(Real%20Functions).md) of the right-hand side, i.e.
>>
>>$$\int (u(x)v(x))' \mathop{\mathrm{d}x} = \int u'(x)v(x) + u(x)v'(x) \mathop{\mathrm{d}x}$$
>>
>> The [antiderivatives](./Antidifferentiability%20(Real%20Functions).md) of $(u(x)v(x))'$ are by definition $u(x)v(x) + C$. Therefore, we have
>>
>>$$(u(x)v(x)) + C = \int u'(x)v(x) + u(x)v'(x) \mathop{\mathrm{d}x}.$$
>>
>>Next, we apply [linearity of antidifferentiation](./Antidifferentiability%20(Real%20Functions).md) to the right-hand side.
>>
>>$$(u(x)v(x)) + C = \int u'(x)v(x) \mathop{\mathrm{d}x} + \int u(x)v'(x) \mathop{\mathrm{d}x}.$$
>>
>>Finally, we just rearrange the terms:
>>
>>$$\int u(x)v'(x) \mathop{\mathrm{d}x} = (u(x)v(x)) - \int u'(x)v(x) \mathop{\mathrm{d}x} + C$$
>>
>
>>[!EXAMPLE]- Example: $\int x \mathrm{e}^x \,\mathrm{d}x$
>>
>>We want to find the [antiderivatives](./Antidifferentiability%20(Real%20Functions).md) of $f(x) = x \mathrm{e}^x$. We have
>>
>>$$f(x) = u(x) v'(x)$$
>>
>>with $u(x) = x$, $u'(x) = 1$, $v'(x) = \mathrm{e}^x$ and $v(x) = \mathrm{e}^x$. Since both $u$ and $v$ are [continuously differentiable](./Differentiability%20(Real%20Functions).md) on $\mathbb{R}$, we have:
>>
>>$$\begin{aligned}\int x \mathrm{e}^x \,\mathrm{d}x  & = u(x)v(x) - \int u'(x) v(x) \,\mathrm{d}x \\ & = x \mathrm{e}^x - \int \mathrm{e}^x \,\mathrm{d}x \\ & = x \mathrm{e}^x - \mathrm{e}^x + C \\ & = \mathrm{e}^x (x - 1) + C \end{aligned}$$
>>
>
>>[!EXAMPLE]- Example: $\int \mathrm{e}^x \sin x \,\mathrm{d}x$
>>
>>We want to find the [antiderivatives](./Antidifferentiability%20(Real%20Functions).md) of $f(x) = \mathrm{e}^x \sin x$. We have
>>
>>$$f(x) = u(x) v'(x)$$
>>
>>with $u(x) = \sin x$, $u'(x) = \cos x$, $v'(x) = \mathrm{e}^x$ and $v(x) = \mathrm{e}^x$. Since both $u$ and $v$ are [continuously differentiable](./Differentiability%20(Real%20Functions).md) on $\mathbb{R}$, we have:
>>
>>$$\begin{aligned}\int \mathrm{e}^{x}\sin x\,\mathrm{d}x & = u(x)v(x) - \int u'(x) v(x)\,\mathrm{d}x \\ & = \mathrm{e}^x \sin x - \int \mathrm{e}^x \cos x \, \mathrm{d}x \end{aligned}$$
>>
>>We can use the same procedure for $\mathrm{e}^x \cos x$, since
>>
>>$$\mathrm{e}^x \cos x = u(x)v'(x)$$
>>
>>with $u(x) = \cos x$, $u'(x) = -\sin x$, $v'(x) = \mathrm{e}^x$ and $v(x) = \mathrm{e}^x$.
>>
>>Since both $u$ and $v$ are [continuously differentiable](./Differentiability%20(Real%20Functions).md) on $\mathbb{R}$, we have:
>>
>>$$\begin{aligned}\int \mathrm{e}^x \cos x \,\mathrm{d}x & = u(x)v(x) - \int u'(x)v(x) \,\mathrm{d}x \\ & = \mathrm{e}^x \cos x - \int \mathrm{e}^x (-\sin x) \,\mathrm{d}x \\ & = \mathrm{e}^x \cos x + \int \mathrm{e}^x \sin x \,\mathrm{d}x \end{aligned}$$
>>
>>We substitute this result into the previous expression:
>>
>>$$\begin{aligned}\int \mathrm{e}^{x}\sin x\,\mathrm{d}x & = \mathrm{e}^x \sin x - \int \mathrm{e}^x \cos x \, \mathrm{d}x \\ & = \mathrm{e}^x \sin x - \left(\mathrm{e}^x \cos x + \int \mathrm{e}^x \sin x \,\mathrm{d}x\right) \\ & =  \mathrm{e}^x \sin x - \mathrm{e}^x \cos x - \int \mathrm{e}^x \sin x \,\mathrm{d}x \end{aligned}$$
>>
>>At first, it might seem that we have achieved nothing because we still have $\int \mathrm{e}^x \sin x \,\mathrm{d}x$. However, on the left side we have it with a plus and on the right side we have it with a minus. Thus, we can move the one on the right to the left and solve for it:
>>
>>$$2\int \mathrm{e}^x \sin x \,\mathrm{d}x = \mathrm{e}^x \sin x - \mathrm{e}^x \cos x$$
>>
>>$$\int \mathrm{e}^x \sin x \,\mathrm{d}x = \frac{1}{2} \mathrm{e}^x (\sin x - \cos x) + C$$
>>
>
>>[!EXAMPLE]- Example: $\int \ln x \,\mathrm{d}x$
>>
>>We want to find the [antiderivatives](./Antidifferentiability%20(Real%20Functions).md) of the [real natural logarithm](./Real%20Logarithms.md#The%20Real%20Natural%20Logarithm).
>>
>>We have
>>
>>$$
>>\ln x = u(x) v'(x)
>>$$
>>
>>with $u(x) = \ln x$, $u'(x) = \frac{1}{x}$, $v'(x) = 1$ and $v(x) = x$ for all $x \in (0, \infty)$. Since $u$ and $v$ are [continuously differentiable](./Differentiability%20(Real%20Functions).md) on $(0,\infty)$, we have the following:
>>
>>$$
>>\begin{aligned}\int \ln x \,\mathrm{d}x & = u(x) v(x) - \int u'(x) v(x) \,\mathrm{d}x \\ & = x \ln x - \int \frac{1}{x}x\,\mathrm{d}x \\ & = x \ln x - x + C\end{aligned}
>>$$
>>
>

>[!THEOREM] Theorem: Integration by Substitution
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](./Real%20Functions.md).
>
>If $g$ is [differentiable](./Differentiability%20(Real%20Functions).md) on $S \subseteq \mathcal{D}_g$ and $F$ is an [antiderivative](./Antidifferentiability%20(Real%20Functions).md) of $f$ on $g(S)$, then the [composition](../../Functions/Functions.md) $F \circ g$ is an [antiderivative](./Antidifferentiability%20(Real%20Functions).md) of $(f\circ g) g'$ on $S$.
>
>>[!EXAMPLE]- Example: $\int x \mathrm{e}^{x^2} \,\mathrm{d}x$
>>
>>We want to determine the [antiderivatives](./Antidifferentiability%20(Real%20Functions).md) of $x \mathrm{e}^{x^2}$:
>>
>>$$\int x \mathrm{e}^{x^2} \,\mathrm{d}x$$
>>
>>We notice that
>>
>>$$x\mathrm{e}^{x^2} = \frac{1}{2}f(g(x))g'(x)$$
>>
>>with $g(x) = x^2$, $g'(x) = 2x$ and $f(x) = \mathrm{e}^x$. One [antiderivative](./Antidifferentiability%20(Real%20Functions).md) $F(x)$ of $f(x)$ is $\mathrm{e}^x$. We can verify that $f$ and $g$ satisfy the requirements of the theorem and so $(F \circ g)(x) = \mathrm{e}^{x^2}$ is an [antiderivative](./Antidifferentiability%20(Real%20Functions).md) of $2x \mathrm{e}^{x^2}$. Therefore, $\frac{1}{2}\mathrm{e}^{x^2}$ is an [antiderivative](./Antidifferentiability%20(Real%20Functions).md) of $x \mathrm{e}^{x^2}$.
>>
>>Using the integral notation, this would be written in the following way with $u = g(x) = x^2$:
>>
>>$$\begin{aligned}\int x \mathrm{e}^{x^2} \,\mathrm{d}x & = \int \frac{1}{2}f(g(x))g'(x)\,\mathrm{d}x \\ & = \frac{1}{2} \int f(g(x))g'(x) \,\mathrm{d}x \\ & = \frac{1}{2}\int f(u)\,\mathrm{d}u \\ & = \frac{1}{2}\mathrm{e}^u + C \\ & = \frac{1}{2}\mathrm{e}^{g(x)} + C \\ & = \frac{1}{2}\mathrm{e}^{x^2} + C\end{aligned}$$
>>
>
>>[!ALGORITHM] Algorithm: Integration by Substitution
>>
>>[Integration by substitution](./Antidifferentiability%20(Real%20Functions).md) can often be used to find the [antiderivatives](./Antidifferentiability%20(Real%20Functions).md) of some [real function](./Real%20Functions.md) $h$, when we have an analytic expression for $h$:
>>
>>$$\int h(x) \,\mathrm{d}x$$
>>
>>The goal is to find $f$ and $g$ such that $h(x) = f(g(x))g'(x)$. 
>>
>>1. Pick some part $u$ of the expression for $h$ such that $h$ can be expressed only in terms of $u$ without $x$.
>>
>>    - Here, $u$ plays the role of our guess for $g$.
>>    - The expression for $h$ in terms of $u$ is our guess for $f$. 
>>
>>2. Compute the [derivative](./Differentiability%20(Real%20Functions).md) of $u$ with respect to $x$ to obtain some expression for $g'$:
>>
>>$$\frac{\mathrm{d}u}{\mathrm{d}x} = \text{expression}$$
>>
>>    - If the resulting expression can be written only in terms of $u$ without $x$, then proceed. If not, go back to step 1.
>>
>>3. Write $\mathrm{d}x$ as the quotient of $\mathrm{d}u$ and this expression:
>>
>>$$\mathrm{d}x = \frac{\mathrm{d}u}{\text{expression}}$$
>>
>>4. Verify that $f$, $g$ and $g'$ satisfy the requirements of the theorem.
>>
>>5. Substitute $\frac{\mathrm{d}u}{\text{expression}}$ and $f(u)$ back into the original [integral](./Antidifferentiability%20(Real%20Functions).md):
>>
>>$$\int h(x) \,\mathrm{d}x = \int f(u) \frac{\mathrm{d}u}{\text{expression}}$$
>>
>>    - Since $f$ and $\text{expression}$ contain only $u$'s and no $x$'s, compute the [integral](./Antidifferentiability%20(Real%20Functions).md) as you would normally.
>>
>>6. Substitute the expression (in terms of $x$) for $u$ back into the result from step 5.
>>
>>>[!EXAMPLE]- Example: $\int \frac{1}{\mathrm{e}^x + 1}\,\mathrm{d}x$
>>>
>>>We want to determine the [antiderivatives](./Antidifferentiability%20(Real%20Functions).md) of $\frac{1}{\mathrm{e}^x + 1}$:
>>>
>>>$$\int \frac{1}{\mathrm{e}^x + 1} \, \mathrm{d}x$$
>>>
>>>Let's try to substitute $\mathrm{e}^x = u$. We have
>>>
>>>$$\frac{\mathrm{d}u}{\mathrm{d}x} = \mathrm{e}^x = u \implies \mathrm{d}x = \frac{\mathrm{d}u}{u}$$
>>>
>>>Therefore:
>>>
>>>$$\begin{aligned}\int \frac{1}{\mathrm{e}^x + 1} \, \mathrm{d}x & = \int \frac{1}{u + 1}\frac{1}{u}\,\mathrm{d}u \\ & = \int \frac{1}{u} - \frac{1}{u + 1}\,\mathrm{d}u \\ & = \ln |u| - \ln |u + 1| + C \\ & = \ln \left\vert\frac{u}{u+1}\right\vert + C \\ & = \ln \frac{\mathrm{e}^x}{\mathrm{e}^x + 1} + C\end{aligned}$$
>>>
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antidifferentiation of Logarithmic Derivatives
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $S \subseteq \mathcal{D}$.
>
>If $f$ is [differentiable](./Differentiability%20(Real%20Functions).md) on an [interval](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) $I \subseteq \mathcal{D}$ and $f(x) \ne 0$ for all $x \in I$, then the [antiderivatives](./Antidifferentiability%20(Real%20Functions).md) of the [quotient](./Real%20Functions.md) $f'/f$ are given by the [composition](../../Functions/Functions.md) of the [real natural logarithm](./Real%20Logarithms.md#The%20Real%20Natural%20Logarithm) and $|f|$:
>
>$$
>\int \frac{f'(x)}{f(x)} \mathop{\mathrm{d}x} = \ln |f(x)| + C
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antiderivatives of Polynomial Functions
>
>$$
>\int x^\alpha \mathop{\mathrm{d}x} = \frac{1}{\alpha + 1} x^{\alpha + 1} + C \qquad \forall \alpha \ne -1 \in \mathbb{R}
>$$
>
>$$
>\int (ax + b)^\gamma \mathop{\mathrm{d}x} = \frac{(ax+b)^{\gamma+1}}{a(\gamma +1)} + C
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antiderivatives of Rational Functions
>
>$$
>\int \frac{c}{ax+b} \mathop{\mathrm{d}x} = \frac{c}{a} \ln |ax+b| + C
>$$
>
>For all $n \in \mathbb{N}$ and $a \in \mathbb{R}$:
>
>$$
>\int \frac{\mathop{\mathrm{d}x}}{(x-a)^n} = \begin{cases}\displaystyle \ln |x-a| + C, \text{ if } n = 1 \\\displaystyle -\frac{1}{(n-1)(x-a)^{n-1}} + C, \text{ if } n\ge 2 \end{cases}
>$$
>
>For all $a,b \in \mathbb{R}$ and all polynomials $x^2 + px + q$ with $p^2 -4q \lt 0$:
>
>$$
>\int\frac{\mathop{\mathrm{d}x}}{x^2+px+q} = \frac{2}{\sqrt{4q-p^2}}\arctan \frac{2x+p}{\sqrt{4q-p^2}} + C
>$$
> 
>$$
>\int\frac{ax+b}{x^2+px+q}\mathop{\mathrm{d}x} = \frac{a}{2}\ln (x^2+px+q)- \left(b-\frac{ap}{2}\right)\int\frac{\mathop{\mathrm{d}x}}{x^2+px+q}
>$$
>
>For all $n\ge 2 \in \mathbb{N}$ and all polynomials $x^2+px+q$ with $p^2-4q\lt 0$:
>
>$$
>\int\frac{\mathop{\mathrm{d}x}}{(x^2+px+q)^n} = \frac{2x+p}{(n-1)(4q-p^2)(x^2+px+q)^{n-1}}+\frac{2(2n-3)}{(n-1)(4q-p^2)}\int\frac{\mathop{\mathrm{d}x}}{(x^2+px+q)^{n-1}}
>$$
> 
>$$
>\int\frac{ax+b}{(x^2+px+q)^n}\mathop{\mathrm{d}x} = -\frac{a}{2(n-1)(x^2+px+q)^{n-1}}+\left(b-\frac{ap}{2}\right)\int\frac{\mathop{\mathrm{d}x}}{(x^2+px+q)^{n-1}}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Higher Order Antidifferentiability

> [!DEFINITION] Definition: Higher Order Antiderivatives (Real Functions)
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md), let $S \subseteq \mathcal{D}_f$, and let $n \in \mathbb{N}_{\ge 0}$.
>
>For $n = 0$: We say that $f$ is **0-times antidifferentiable on** $S$. The **zeroth-order antiderivative function** of $f$ on $S$ is the restriction $f|_S$.
>
>For $n \ge 1$: An **$n$-th order antiderivative** of $f$ on $S$ is any [real function](./Real%20Functions.md) $F: \mathcal{D}_F \subseteq \mathbb{R} \to \mathbb{R}$ which is [$n$-times differentiable](./Differentiability%20(Real%20Functions).md#Higher%20Order%20Differentiability) on $S$ with
> 
>$$F^{(n)}(x) = f(x)$$
> 
>for all $x \in S$.
>
>>[!DEFINITION] Definition: Higher Order Antidifferentiability
>>
>>We say that $f$ is **$n$-times antidifferentiable on** $S$ if it has an [$n$-th order antiderivative](#Higher%20Order%20Antidifferentiability) on $S$.
>>
>

>[!THEOREM] Theorem: Cauchy's Repeated Integration
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md), let $[a,b] \subseteq \mathcal{D}$ and let $n \in \mathbb{N}_{\ge 1}$.
>
>If $f$ is [continuous](./Continuity%20(Real%20Functions).md) on $[a,b]$, then the [function](./Real%20Functions.md) $F: [a,b] \to \mathbb{R}$ defined as
>
>$$F(x) \overset{\text{def}}{=} \frac{1}{(n-1)!}\int_a^x f(\xi) (x - \xi)^{n-1} \,\mathrm{d}\xi$$
>
>is an [$n$-th order antiderivative](#Higher%20Order%20Antidifferentiability) of $f$ on $S$.
>
>>[!PROOF]-
>>
>>TODO
>>
>