---
title: Separable ODEs
tags:
    - algebra
    - mathematical-analysis
    - mathematics
---

# Separable ODEs

>[!DEFINITION] Definition: Separable Ordinary Differential Equation
>
>A first-order [ODE](./Real%20Ordinary%20Differential%20Equations.md) $F(x, y, y')$ with $F: \mathcal{D}_F \subseteq \mathbb{R} \times \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ is **separable** if there exist [real functions](../../Real%20Functions/Real%20Functions.md) $M$ and $N$ such that
>
>$$F(x, y, y') = P(x) + Q(y)y'$$
>
>for all $(x, y, y') \in \mathcal{D}_F$.
>

More specifically, this means that a [real function](../../Real%20Functions/Real%20Functions.md) $\phi$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md) of $F$ on some [subset](../../../../Set%20Theory/Subsets.md) $S \subseteq \mathbb{R}$ if and only if

$$P(x) + Q(\phi(x)) \phi'(x) = 0$$

for all $x \in S$. Many [separable ODEs](./Separable%20ODEs.md) can be solved via direct [antidifferentiation](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md).

>[!THEOREM] Theorem: Solving Separable ODEs via Antidifferentiation
>
>Let $F(x,y,y')$ be a [separable ODE](./Separable%20ODEs.md) expressed as follows:
>
>$$N(y)y' = M(x)$$
>
>A [real function](../../Real%20Functions/Real%20Functions.md) $\phi$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md) of $F$ on some [subset](../../../../Set%20Theory/Subsets.md) $S \subseteq \mathbb{R}$ if and only if $\phi$ is [differentiable](../../Real%20Functions/Differentiability%20(Real%20Functions).md) on $S$ and the [antiderivatives](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) of $M$ and $(N \circ \phi) \cdot \phi'$ exist and are equal on $S$:
>
>$$\int N(\phi(x))\phi'(x) \, \mathrm{d}x = \int M(x) \, \mathrm{d}x$$
>
>>[!IMPORTANT]
>>
>>If we can explicitly find $\int N(\phi(x))\phi'(x) \, \mathrm{d}x$ (e.g. via [substitution](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md)) and $\int M(x) \, \mathrm{d}x$, then we can often find an explicit expression for the [solutions](./Real%20Ordinary%20Differential%20Equations.md) of the [separable ODE](./Separable%20ODEs.md).
>>
>
>>[!EXAMPLE]- Example $y' = yx$
>>
>>Consider the following [ordinary differential equation](./Real%20Ordinary%20Differential%20Equations.md):
>>
>>$$y' = y x$$
>>
>>We immediately see that $y = 0$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md) on $\mathbb{R}$.
>>
>>For $y \ne 0$, we have a [separable ODE](./Separable%20ODEs.md):
>>
>>$$N(y)y' = M(x) \qquad N(y) = \frac{1}{y} \qquad M(x) = x$$
>>
>>The theorem tells us that $y$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md) on $\mathbb{R}$ if and only if
>>
>>$$\int N(y(x))y'(x) \, \mathrm{d}x = \int M(x) \, \mathrm{d}x.$$
>>
>>In other words:
>>
>>$$\int \frac{y'(x)}{y(x)} \, \mathrm{d}x = \int M(x) \, \mathrm{d}x$$
>>
>>$$\ln |y(x)| = \frac{1}{2}x^2 + C$$
>>
>>$$|y(x)| = \mathrm{e}^{\frac{1}{2}x^2 + C}, \qquad C \in \mathbb{R}$$
>>
>>$$|y(x)| = \mathrm{e}^C \mathrm{e}^{\frac{1}{2}x^2}$$
>>
>>$$y(x) = \pm \mathrm{e}^C \mathrm{e}^{\frac{1}{2}x^2}$$
>>
>>Since $\pm \mathrm{e}^C$ can take on any value in $\mathbb{R}_{\ne 0}$ and since $y = 0$ is also a [solution](./Real%20Ordinary%20Differential%20Equations.md), we can express every [solution](./Real%20Ordinary%20Differential%20Equations.md) in the following form:
>>
>>$$y(x) = C \mathrm{e}^{\frac{1}{2}x^2}, \qquad C \in \mathbb{R}$$
>>
>
>>[!EXAMPLE]- Example: $y' = -t \mathrm{e}^{y}$
>>
>>Consider the following [ordinary differential equation](./Real%20Ordinary%20Differential%20Equations.md):
>>
>>$$y' = -t \mathrm{e}^{y}$$
>>
>>It is [separable](./Separable%20ODEs.md):
>>
>>$$N(y)y' = M(t) \qquad N(y) = \mathrm{e}^{-y} \qquad M(t) = -t$$
>>
>>The theorem tells us that $y$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md) on $\mathbb{R}$ if and only if
>>
>>$$\int N(y(t))y'(t) \, \mathrm{d}t = \int M(t) \, \mathrm{d}t.$$
>>
>>In other words:
>>
>>$$\int \mathrm{e}^{-y(t)} y'(t)\, \mathrm{d}t = \int -t \,\mathrm{d}t$$
>>
>>$$-\mathrm{e}^{-y(t)} = - \frac{1}{2}t^2 + C, \qquad C \in \mathbb{R}$$
>>
>>$$y(t) = -\ln \left(\frac{1}{2}t^2 + C\right), \qquad C \in \mathbb{R}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>
