---
tags:
    - algebra
    - real-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Initial Value Problems

## Univariate Initial Value Problems

Many [functions](../../Real%20Functions/Real%20Functions.md) can be solutions to a given [ODE](./Initial%20Value%20Problems.md) on the same [subset](../../../../Set%20Theory/Subsets.md) $S$. However, we are usually interested in [functions](../../Real%20Functions/Real%20Functions.md) which satisfy additional properties because [ODEs](./Initial%20Value%20Problems.md) are ubiquitous in physics models.

>[!DEFINITION] Definition: Initial Value Problem
>
>An **initial value problem (IVP)** consists of an $n$-th order [ODE](./Real%20Ordinary%20Differential%20Equations.md)
>
>$$F\left(x, y, y', y'', \dotsc, y^{(n)}\right) = 0,
>$$
>
>together with a [tuple](../../../../Set%20Theory/Tuples.md) $(x_0, y_0, y_1, \dotsc, y_{n-1})$ of [numbers](../../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) known as **initial conditions**.
>
>>[!DEFINITION] Definition: Solution of an IVP
>>
>>We say that a [function](../../Real%20Functions/Real%20Functions.md) $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ is a **solution** of the [IVP](./Initial%20Value%20Problems.md) on a [subset](../../../../Set%20Theory/Subsets.md) $S \subseteq \mathcal{D}_f$ if $f$ is a [solution](./Initial%20Value%20Problems.md) to the [ODE](./Real%20Ordinary%20Differential%20Equations.md) on $S$ with $x_0 \in S$ and $f^{(k)}(x_0) = y_k$ for all $k \in \{0, 1, \dotsc, n-1\}$.
>>
>
>>[!EXAMPLE]- Example: $y'(x) - x^2 = 0$ with $y(0) = 1$
>>
>>Consider the following [initial value problem](./Initial%20Value%20Problems.md):
>>
>>$$y'(x) - x^2 = 0 \qquad y(0) = 1$$
>>
>>We want to find all [real functions](../../Real%20Functions/Real%20Functions.md) $y$ which are [solutions](./Initial%20Value%20Problems.md) to the [ODE](./Real%20Ordinary%20Differential%20Equations.md) $y'(x) - x^2 = 0$ on $[0,1]$ and which also satisfy the [initial condition](./Initial%20Value%20Problems.md) $y(0) = 1$.
>>
>>By rearranging the [ODE](./Real%20Ordinary%20Differential%20Equations.md), we get
>>
>>$$y'(x) = x^2$$
>>
>>and we see that its [solutions](./Initial%20Value%20Problems.md) are the [antiderivatives](../../Real%20Functions/Antidifferentiability%20(Real%20Functions).md) of $x^2$. Therefore, each [solution](./Initial%20Value%20Problems.md) $y$ has the form
>>
>>$$y(x) = \frac{1}{3}x^3 + C$$
>>
>>for some $C \in \mathbb{R}$. Now, we need to determine specific [solutions](./Initial%20Value%20Problems.md) which also satisfy the [initial condition](./Initial%20Value%20Problems.md):
>>
>>$$y(0) = 1$$
>>
>>$$\left.\left(\frac{1}{3}x^3 + C\right)\right\vert_{x = 0} = 1$$
>>
>>$$C = 1$$
>>
>>We can indeed verify that $y(x) = \frac{1}{3}x^3 + 1$ satisfies both the [ODE](./Real%20Ordinary%20Differential%20Equations.md) and the [initial condition](./Initial%20Value%20Problems.md) on $[0,1]$ and is thus a [solution](./Initial%20Value%20Problems.md) to the [IVP](./Initial%20Value%20Problems.md). However, whether it is the *only* [solution](./Initial%20Value%20Problems.md), is not immediately obvious.
>>
>
>>[!EXAMPLE]- Example: $y'(x) = a y(x)$ with $y(0) = y_0$
>>
>>Consider the [initial value problem](./Initial%20Value%20Problems.md)
>>
>>$$y'(x) = a y(x) \qquad y(0) = y_0$$
>>
>>The [solutions](./Initial%20Value%20Problems.md) of the [ODE](./Real%20Ordinary%20Differential%20Equations.md) on $\mathbb{R}$ have an [exponential](../../Real%20Functions/Real%20Exponentiation.md) form
>>
>>$$y(x) = c \mathrm{e}^{ax}$$
>>
>>for some $c \in \mathbb{R}$. By using the [initial condition](./Initial%20Value%20Problems.md), we get a unique [solution](./Initial%20Value%20Problems.md) to the [initial value problem](./Initial%20Value%20Problems.md):
>>
>>$$y(0) = y_0$$
>>
>>$$c \mathrm{e}^{a\cdot 0} = y_0$$
>>
>>$$c = y_0$$
>>
>>$$y(x) = y_0 \mathrm{e}^{ax}$$
>>
>
>>[!EXAMPLE]- Example: $y'(t) = y^2(t)$ with $y(0) = 1$
>>
>>Consider the following [initial value problem](./Initial%20Value%20Problems.md):
>>
>>$$y'(t) = y^2(t) \qquad y(0) = 1$$
>>
>>On the [interval](../../Euclidean%20Space/Euclidean%20Space.md) $[0,1)$ it has only the following [solution](./Initial%20Value%20Problems.md):
>>
>>$$y(t) = \frac{1}{1-t}$$
>>
>
>>[!EXAMPLE]- Example: $y''(t) + \omega^2 y(t) = 0$ with $y(0) = y_0$ and $y'(0) = y_1$
>>
>>Consider the [initial value problem](./Initial%20Value%20Problems.md)
>>
>>$$y''(t) + \omega^2 y(t) = 0 \qquad y(0) = y_0 \qquad y'(0) = y_1$$
>>
>>for some $\omega, y_0, y_1 \in \mathbb{R}_{\gt 0}$. The [solutions](./Real%20Ordinary%20Differential%20Equations.md) to the [ODE](./Real%20Ordinary%20Differential%20Equations.md) on $\mathbb{R}$ have the form
>>
>>$$y(t) = A \cos (\omega t) + B \sin (\omega t)$$
>>
>>for some $A, B \in \mathbb{R}$. By using the [initial conditions](./Initial%20Value%20Problems.md), we can find the [solutions](./Initial%20Value%20Problems.md) of the [IVP](./Initial%20Value%20Problems.md):
>>
>>$$y(0) = A \cos (\omega \cdot 0) + B \sin (\omega \cdot 0) = A$$
>>
>>We thus get $y_0 = y(0) = A$ and so $A = y_0$. For $y'$, we have:
>>
>>$$y'(t) = -A \omega \sin (\omega t) + B \omega \cos (\omega t)$$
>>
>>Using the second [initial condition](./Initial%20Value%20Problems.md), we get:
>>
>>$$y'(0) =  -A \omega \sin (\omega \cdot 0) + B \omega \cos (\omega \cdot 0) = B \omega$$
>>
>>Therefore, $y_1 = y'(0) = B \omega$ and so $B = \frac{y_1}{\omega}$.
>>
>>The [solution](./Initial%20Value%20Problems.md) of the [IVP](./Initial%20Value%20Problems.md) on $\mathbb{R}$ is thus the following:
>>
>>$$y(t) = y_0 \cos (\omega t) + \frac{y_1}{\omega} \sin (\omega t)$$
>>
>>Showing that this is the *only* [solution](./Initial%20Value%20Problems.md) on $\mathbb{R}$ is not trivial.
>>
>

>[!THEOREM] Peano's Theorem: Existence of Local Solutions to Explicit IVPs
>
>Consider the following $n$-th [order initial value problem](./Initial%20Value%20Problems.md):
>
>$$y^{(n)} = f(t, y, y', \dotsc, y^{(n-1)}) \qquad \begin{aligned}y(t_0) & = y_0 \\ y'(t_0) & = y_1 \\ & \vdots \\ y^{(n-1)}(t_0) & = y_{n-1} \end{aligned}$$
>
>If $f$ is [continuous](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Continuity%20(Real%20Scalar%20Fields).md) on
>
>$$S = [t_0, t_0 + \alpha] \times [y_0 - \beta, y_0 + \beta] \times [y_1 - \beta, y_1 + \beta] \times \dotsb \times [y_{n-1} - \beta, y_{n-1} + \beta],$$
>
>for some $\alpha, \beta \gt 0$, then there exists a [solution](./Initial%20Value%20Problems.md) of the [IVP](./Initial%20Value%20Problems.md) on $[t_0, t_0 + \delta]$ for some $\delta \in \left(0, \min \left\{\alpha, \frac{\beta}{M}\right\}\right]$, where
>
>$$M = \max_{(t, p_0, p_1, \dotsc, p_{n-1}) \in S} \max (|p_1|, |p_2|, \dotsc, |p_{n-1}|, |f(t, p_0, \dotsc, p_{n-1})|).$$
>
>>[!EXAMPLE]- Example: $y'(t) = \sqrt{|y(t)|}$ with $y(0) = 0$
>>
>>Consider the following [initial value problem](./Initial%20Value%20Problems.md):
>>
>>$$y'(t) = \sqrt{|y(t)|} \qquad y(0) = 0$$
>>
>>It has an [explicit](./Initial%20Value%20Problems.md) [first-order ODE](./Initial%20Value%20Problems.md) $y' = f(t, y)$, where $f(t, y) = \sqrt{|y|}$, and an [initial condition](./Initial%20Value%20Problems.md) with $t_0 = 0$ and $y_0 = 0$.
>>
>>For all $\alpha, \beta \gt 0$, we see that $f$ is [continuous](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Continuity%20(Real%20Scalar%20Fields).md) on
>>
>>$$S = [t_0, t_0 + \alpha] \times \left\{p_0 \in \mathbb{R} : |p_0 - y_0| \le \beta \right\} = [0, \alpha] \times [-\beta, \beta]$$
>>
>>and so there exists a [solution](./Initial%20Value%20Problems.md) of the [IVP](./Initial%20Value%20Problems.md) on $[t_0, t_0 + \delta] = [0, \delta]$ for some $\delta \in \left(0, \min \left\{\alpha, \frac{\beta}{M}\right\}\right]$. Specifically,
>>
>>$$M = \max_{(t, p_0) \in S} |f(t, p_0)| = \sqrt{\beta}$$
>>
>>and we get:
>>
>>$$\delta \in \left(0, \min \left\{\alpha, \frac{\beta}{\sqrt{\beta}}\right\}\right] = \left(0, \min \left\{\alpha, \sqrt{\beta}\right\}\right]$$
>>
>>Since $\alpha$ and $\beta$ can be chosen to be arbitrary large, we have shown the existence of [solutions](./Initial%20Value%20Problems.md) for each $\delta \gt 0$. Specifically, we proved that there is a [solution](./Initial%20Value%20Problems.md) of the [IVP](./Initial%20Value%20Problems.md) on $[0, \delta]$ for each $\delta \gt 0$. 
>>
>>However, the existence of a *unique* [solution](./Initial%20Value%20Problems.md) is not guaranteed. For example, both $y(t) = 0$ and $y(t) = \frac{1}{4}t^2$ are [solutions](./Initial%20Value%20Problems.md) on each $[0, \delta]$ for each $\delta \gt 0$. 
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] The Theorem of Picard-Lindelöf: Existence and Uniqueness of Local Solutions to Explicit IVPs
>
>Consider the following $n$-th [order initial value problem](./Initial%20Value%20Problems.md):
>
>$$y^{(n)} = f(t, y, y', \dotsc, y^{(n-1)}) \qquad \begin{aligned}y(t_0) & = y_0 \\ y'(t_0) & = y_1 \\ & \vdots \\ y^{(n-1)}(t_0) & = y_{n-1} \end{aligned}$$
>
>If $f$ is [continuous](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Continuity%20(Real%20Scalar%20Fields).md) on and satisfies a [local Lipschitz condition](./Lipschitz%20Conditions.md) on
>
>$$S = [t_0, t_0 + \alpha] \times [y_0 - \beta, y_0 + \beta] \times [y_1 - \beta, y_1 + \beta] \times \dotsb \times [y_{n-1} - \beta, y_{n-1} + \beta],$$
>
>for some $\alpha, \beta \gt 0$, then there exists a unique [solution](./Initial%20Value%20Problems.md) of the [IVP](./Initial%20Value%20Problems.md) on $[t_0, t_0 + \delta]$ for some $\delta \in \left(0, \min \left\{\alpha, \frac{\beta}{M}\right\}\right]$, where
>
>$$M = \max_{(t, p_0, p_1, \dotsc, p_{n-1}) \in S} \max (|p_1|, |p_2|, \dotsc, |p_{n-1}|, |f(t, p_0, \dotsc, p_{n-1})|).$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Existence and Uniqueness of Solutions to Explicit IVPs
>
>Consider the following $n$-th [order initial value problem](./Initial%20Value%20Problems.md)
>
>$$y^{(n)} = f(t, y, y', \dotsc, y^{(n-1)}) \qquad \begin{aligned}y(t_0) & = y_0 \\ y'(t_0) & = y_1 \\ & \vdots \\ y^{(n-1)}(t_0) & = y_{n-1} \end{aligned}$$
>
>and let $T \gt t_0$.
>
>If $f$ is [continuous](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Continuity%20(Real%20Scalar%20Fields).md) on and satisfies a [global Lipschitz condition](./Lipschitz%20Conditions.md) on
>
>$$S = [t_0, T] \times \mathbb{R}^n,$$
>
>then there exists a unique [solution](./Initial%20Value%20Problems.md) of the [IVP](./Initial%20Value%20Problems.md) on $[t_0, T]$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

