---
tags:
    - algebra
    - real-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# First-Order Linear Ordinary Differential Equations

A [first-order](./Initial%20Value%20Problems.md) [linear ODE](./Linear%20Ordinary%20Differential%20Equations.md) can be expressed as

$$Q(x)y' + P(x)y = G(x)$$

for some [functions](../../Real%20Functions/Real%20Functions.md) $P$, $Q$ and $G$. We often need transform this into a more standard form by dividing by $Q(x)$ and imposing the condition that $Q(x) \ne 0$:

$$y' + p(x) = g(x),$$

where $p = P / Q$ and $g = G / Q$.

>[!THEOREM] Theorem: Variation of Parameters
>
>Consider a [first-order](./Real%20Ordinary%20Differential%20Equations.md) [linear ODE](./Linear%20Ordinary%20Differential%20Equations.md) which can be expressed as follows:
>
>$$y' + p(x)y = q(x)$$
>
>A [real function](../../Real%20Functions/Real%20Functions.md) $\phi$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md) on some [subset](../../../../Set%20Theory/Subsets.md) $S \subseteq \mathbb{R}$ if and only if it can be expressed as 
>
>$$\phi(x) = c(x) \mathrm{e}^{-P(x)},$$
>
>where $P(x)$ is any [antiderivative](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) of $p(x)$ on $S$ and $c(x)$ is an [antiderivative](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) of $q(x)\mathrm{e}^{P(x)}$ on $S$.
>
>>[!EXAMPLE]- Example: $y'(t) + \frac{y(t)}{t} = \cos t$
>>
>>Consider the following [first-order linear ODE](./Linear%20Ordinary%20Differential%20Equations.md):
>>
>>$$y'(t) + \frac{y(t)}{t} = \cos t$$
>>
>>It has the following form:
>>
>>$$y' + p(t)y(t) = q(t) \qquad p(t) = \frac{1}{t} \qquad q(t) = \cos t$$
>>
>>The [antiderivatives](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) of $p$ for $t \in (0, \infty)$ are the following:
>>
>>$$P(t) = \int p(t) \, \mathrm{d}t = \int \frac{1}{t} \, \mathrm{d}t = \ln t + C_1, \qquad C_1 \in \mathbb{R}$$
>>
>>For $c(t)$, we get:
>>
>>$$c(t) = \int q(t)\mathrm{e}^{P(t)} \, \mathrm{d}t = \int t \mathrm{e}^{C_1} \cos t \,\mathrm{d}t = \mathrm{e}^{C_1}(t \sin t + \cos t + C_2), C_2 \in \mathbb{R}$$
>>
>>Therefore:
>>
>>$$y(t) = c(t)\mathrm{e}^{-P(t)} = \mathrm{e}^{C_1}(t \sin t + \cos t + C_2) \mathrm{e}^{-\ln t -C_1} = \frac{t \sin t + \cos t + C_2}{t}, C_2 \in \mathbb{R}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!ALGORITHM] Algorithm: Solving First-Order Linear ODEs
>
>We are given the following [first-order linear ODE](./Linear%20Ordinary%20Differential%20Equations.md):
>
>$$
>y' + p(x)y = g(x)
>$$
>
>To solve this, we use the **method of integrating factors**. The goal is to find some [function](../../Real%20Functions/Real%20Functions.md) $\mu(x)$ such that we can use the [product rule](../../Real%20Functions/Differentiability%20(Real%20Functions).md) to express the left-hand side as the [derivative](../../Real%20Functions/Differentiability%20(Real%20Functions).md) of $(\mu(x)y)$. We can then use [antidifferentiation](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) to find the solutions.
>
>1. Multiply both sides by a yet unknown [function](../../Real%20Functions/Real%20Functions.md) $\mu(x)$:
>
>$$
>\mu(x)y' + \mu(x)p(x)y = \mu(x)g(x)
>$$
>
>2. In order for $\mu(x)y' + \mu(x)p(x)y$ to be the [derivative](../../Real%20Functions/Differentiability%20(Real%20Functions).md) of $(\mu(x)y)$, we need $\mu(x)p(x)$  to be equal to $\mu'(x)$ because the [product rule](../../Real%20Functions/Differentiability%20(Real%20Functions).md) gives us $(\mu(x)y)' = \mu(x)y' + \mu'(x)y$:
>
>$$
>\mu(x)y' + \mu(x)p(x)y = (\mu(x)y)' \iff \mu'(x) = \mu(x)p(x)
>$$
>
>3. Divide both sides of $\mu'(x) = \mu(x)p(x)$ by $\mu(x)$, imposing the condition $\mu(x) \ne 0$:
>
>$$
>\frac{1}{\mu(x)}\mu'(x) = p(x)
>$$
>
>4. By also imposing the condition that $\mu(x) \gt 0$ and then [antidifferentiating](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) both sides, we can transform this further:
>
>$$
>\ln (\mu(x)) = \int p(x) \mathop{\mathrm{d}x} + C
>$$
>
>5. We take the [real exponential function](../../Real%20Functions/Real%20Exponentiation.md) of both sides:
>
>$$
>\mu(x) = \mathrm{e}^{\int p(x) \mathop{\mathrm{d}x} + C}
>$$
>
>For each choice of $C \in \mathbb{R}$, the expression $\int p(x) \mathop{\mathrm{d}x} + C$ is some [antiderivative](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) $P(x)$ of $p(x)$. Thus, if we can find an [antiderivative](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) $P(x)$ of $p(x)$, then we can find a $\mu(x) = \mathrm{e}^{P(x)}$ which satisfies the condition $(\mu(x)y)' = \mu(x)y' + \mu'(x)y$. We can easily verify this as well by applying the [chain rule](../../Real%20Functions/Differentiability%20(Real%20Functions).md) and the rules for the [derivative](../../Real%20Functions/Differentiability%20(Real%20Functions).md) of the [real exponential function](../../Real%20Functions/Real%20Exponentiation.md):
>
>$$
>(\mu(x)y)' = (\mathrm{e}^{P(x)}y)' = \mathrm{e}^{P(x)}y' + (\mathrm{e}^{P(x)})'y = \mathrm{e}^{P(x)}P'(x)y = \mathrm{e}^{P(x)}y' + \mathrm{e}^{P(x)}p(x)y = \mu(x)y' + \mu'(x)y
>$$
>
>Moreover, since the [real exponential function](../../Real%20Functions/Real%20Exponentiation.md) is always positive, we have a $\mu(x)$ which satisfies the previously imposed condition that $\mu(x) \gt 0$.
>
>6. We have shown how to find an appropriate $\mu(x)$, so we can proceed with the original equation:
>
>$$
>(\mu(x)y)' = \mu(x)g(x)
>$$
>
>7. We [antidifferentiate](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) both sides:
>
>$$
>\mu(x)y = \int \mu(x)g(x) \mathop{\mathrm{d}x} + C
>$$
>
>8. To obtain the solutions, we divide both sides by $\mu(x)$:
>
>$$
>y = \frac{1}{\mu(x)} \left(\int \mu(x)g(x) \mathop{\mathrm{d}x} + C\right)
>$$
>
>For each choice of $C \in \mathbb{R}$, the expression $\int \mu(x)g(x) \mathop{\mathrm{d}x} + C$ is just some [antiderivative](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) $\mathcal{F}$ of $\mu(x)g(x)$. Therefore, the solutions of the original equation on some [open subset](../../Euclidean%20Space/Euclidean%20Space.md) $U \subseteq \mathbb{R}$ are the [functions](../../../Functions/Functions.md) $y: U \to \mathbb{R}$ which for all $x \in U$ can be expressed for as
>
>$$
>y(x) = \frac{1}{\mu(x)} \mathcal{F}(x) = \frac{1}{\mathrm{e}^{P(x)}} \mathcal{F}(x) = \mathrm{e}^{-P(x)}\mathcal{F}(x),
>$$
>
>where $P(x)$ is any [antiderivative](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) of $p(x)$ and $\mathcal{F}(x)$ is any [antiderivative](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) of $\mu(x)g(x) = \mathrm{e}^{P(x)}g(x)$.
>
>>[!SUMMARY] Summary
>>
>>Given some [open subset](../../Euclidean%20Space/Euclidean%20Space.md) $U \subseteq \mathbb{R}$, the solutions of the ODE on $U$ are the [functions](../../../Functions/Functions.md) $y: U \to \mathbb{R}$ which on $U$ can be expressed as
>>
>>$$
>>y(x) = \mathrm{e}^{-P(x)}\mathcal{F}(x)
>>$$
>>
>>for some [antiderivative](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) $P$ of $p$ and some [antiderivative](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) $\mathcal{F}$ of $\mathrm{e}^{P(x)}g(x)$.
>>
>
>>[!EXAMPLE]- Example: $y' - 2y = 4 - x$
>>
>>Here we have $p(x) = -2$ and $g(x) = 4 - x$. We want to rewrite this as
>>
>>$$
>>(\mu(x)y)' = \mu(x)(4 - x)
>>$$
>>
>>The [antiderivatives](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) of $p$ are given by 
>>
>>$$
>>\int p(x) \mathop{\mathrm{d}x} = \int -2 \mathop{\mathrm{d}x} = -2x + C
>>$$
>>
>>We choose $C = 0$ to make everything simple and so
>>
>>$$
>>\mu(x) = \mathrm{e}^{-2x}
>>$$
>>
>>The equation thus becomes
>>
>>$$
>>(\mathrm{e}^{-2x} y)' = \mathrm{e}^{-2x}(4-x)
>>$$
>>
>>We [antidifferentiate](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) both sides:
>>
>>$$
>>\mathrm{e}^{-2x} y = \int \mathrm{e}^{-2x}(4-x) \mathop{\mathrm{d}x}
>>$$
>>
>>Use [integration by parts](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) on the right-hand side:
>>
>>$$
>>\begin{aligned}
>>\int \mathrm{e}^{-2x}(4-x) \mathop{\mathrm{d}x} &= (4-x)\left(-\frac{1}{2}\mathrm{e}^{2x}\right) - \int \frac{1}{2}\mathrm{e}^{-2x} \mathop{\mathrm{d}x} \\
>>&= -\frac{1}{2}(4-x)\left(\mathrm{e}^{-2x}\right) - \frac{1}{2} \mathrm{e}^{-2x} \mathop{\mathrm{d}x} \\
>>&= -\frac{1}{2}(4-x)\left(\mathrm{e}^{-2x}\right) - \frac{1}{2}\left(-\frac{1}{2}\mathrm{e}^{-2x} + C\right) \\
>>&= -\frac{1}{2}(4-x)\left(\mathrm{e}^{-2x}\right) + \frac{1}{4}\mathrm{e}^{-2x} + C \\
>>&= -2\mathrm{e}^{-2x} + \frac{1}{2}x\mathrm{e}^{-2x} + \frac{1}{4}\mathrm{e}^{-2x} + C \\
>>&= \left(-2 + \frac{1}{4}\right)\mathrm{e}^{-2x} + \frac{1}{2}x\mathrm{e}^{-2x} + C \\
>>&= \left(-\frac{8}{4} + \frac{1}{4}\right)\mathrm{e}^{-2x} + \frac{1}{2}x\mathrm{e}^{-2x} + C \\
>>&= -\frac{7}{4}\mathrm{e}^{-2x} + \frac{1}{2}x\mathrm{e}^{-2x} + C \\
>>&= \mathrm{e}^{-2x} \left(\frac{1}{2}x - \frac{7}{4}\right) + C 
>>\end{aligned}
>>$$
>>
>>Therefore, we have
>>
>>$$
>>\mathrm{e}^{-2x} y = \mathrm{e}^{-2x} \left(\frac{1}{2}x - \frac{7}{4}\right) + C
>>$$
>>
>>and so the solutions are
>>
>>$$
>>y(x) = C\mathrm{e}^{2x} + \frac{1}{2}x - \frac{7}{4}
>>$$
>>
>>
>
>>[!EXAMPLE]- Example: $xy' + 2y = 4x^2$
>>
>>TODO
>>
>

## Constant Coefficients

A [first-order linear ordinary differential equation](./First-Order%20Linear%20Ordinary%20Differential%20Equations.md) with constant coefficients can always be written in the form

$$\dot{x} = \alpha x + f(t)$$

with some [real number](../../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) $\alpha \in \mathbb{R}$ and some [real function](../../Real%20Functions/Real%20Functions.md) $f: \mathbb{R} \to \mathbb{R}$. In this case, $x$ is often called the **state** and $f$ the **input**.

### General Solution

>[!THEOREM] Theorem: General Solution of First-Order Linear ODEs with Constant Coefficients
>
>Let $\alpha \in \mathbb{R}$ be a [real number](../../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md), let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../../Real%20Functions/Real%20Functions.md) and let $\mathcal{I} \subseteq \mathcal{D}_f$ be an [interval](../../../../Set%20Theory/Orderings/Interval.md).
>
>If $f$ is [antidifferentiable](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) on $\mathcal{I}$, then the [first-order linear ordinary differential equation](./First-Order%20Linear%20Ordinary%20Differential%20Equations.md)
>
>$$\dot{x} = \alpha x + f(t)$$
>
>has infinitely many [solutions](./Real%20Ordinary%20Differential%20Equations.md) $x: \mathcal{I} \to \mathbb{R}$ on $\mathcal{I}$.
>
>If $\int \mathrm{e}^{-\alpha t} f(t) \,\mathrm{d}t$ is an [antiderivative](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) of $\mathrm{e}^{-\alpha t} f(t)$, then for each [solution](./Real%20Ordinary%20Differential%20Equations.md) $x(t)$, there exists some [real number](../../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) $C \in \mathbb{R}$ such that $x$ can be expressed as follows:
>
>$$x(t) = C \mathrm{e}^{\alpha t} + \mathrm{e}^{\alpha t}\int \mathrm{e}^{-\alpha t} f(t) \,\mathrm{d}t$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

### Constant Input

>[!THEOREM] Theorem: Constant Input Solution of First-Order Linear ODEs with Constant Coefficients
>
>Let $\alpha, \beta \in \mathbb{R}$ be [real numbers](../../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) and let $\mathcal{I} \subseteq \mathbb{R}$ be an [interval](../../../../Set%20Theory/Orderings/Interval.md).
>
>The [first-order linear ordinary differential equation](./First-Order%20Linear%20Ordinary%20Differential%20Equations.md)
>
>$$\dot{x} = \alpha x + \beta$$
>
>has infinitely many [solutions](./Real%20Ordinary%20Differential%20Equations.md) $x: \mathcal{I} \to \mathbb{R}$ on $\mathcal{I}$.
>
>If $\alpha = 0$, then for each [solution](./Real%20Ordinary%20Differential%20Equations.md) $x(t)$, there exists some [real number](../../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) $C \in \mathbb{R}$ such that $x$ can be expressed as follows:
>
>$$x(t) = \beta t + C$$
>
>If $\alpha \ne 0$, then for each [solution](./Real%20Ordinary%20Differential%20Equations.md) $x(t)$, there exists some [real number](../../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) $C \in \mathbb{R}$ such that $x$ can be expressed as follows:
>
>$$x(t) = C \mathrm{e}^{\alpha t} - \frac{\beta}{\alpha}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
