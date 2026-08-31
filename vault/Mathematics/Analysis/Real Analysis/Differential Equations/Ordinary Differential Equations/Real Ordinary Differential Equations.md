---
tags:
    - algebra
    - real-analysis
    - analysis
    - mathematics
---

# Real Ordinary Differential Equations

>[!DEFINITION] Definition: Real Ordinary Differential Equation
>
>Let $n \in \mathbb{N}_{\ge 1}$.
>
>A **real ordinary differential equation** is a [real scalar field](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) 
>
>$$F: \mathcal{D}_F \subseteq \mathbb{R} \times \mathbb{R} \times \mathbb{R}^n \to \mathbb{R}$$
>
>which is [dependent](TODO) on its last argument.
>
>>[!DEFINITION] Definition: Explicit ODE
>>
>>We say that $F$ is **explicit** if there exists a [function](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) 
>>
>>$$f: \mathcal{D}_f \subseteq \mathbb{R}^{n+1} \to \mathbb{R}$$
>>
>>with 
>>
>>$$F(x, y, y', y'', \dotsc, y^{(n)}) = y^{(n)} - f(x, y, y', \dotsc, y^{(n-1)})$$
>>
>>for all $(x, y, y', y'', \dotsc, y^{(n)}) \in \mathcal{D}_F$.
>>
>
>>[!DEFINITION] Definition: Solution
>>
>>Let $S \subseteq \mathbb{R}$.
>>
>>A **solution** of $F$ on $S$ is any [real function](../../Real%20Functions/Real%20Functions.md) $\phi: \mathcal{D}_{\phi} \to \mathbb{R}$ with $S \subseteq \mathcal{D}_{\phi}$ which is$n$-times [differentiable](../../Real%20Functions/Differentiability%20(Real%20Functions).md) on $S$ with $(x, \phi(x), \phi'(x), \phi''(x), \dotsc, \phi^{(n)}(x)) \in \mathcal{D}_F$ and
>>
>>$$F\left(x, \phi(x), \phi'(x), \phi''(x), \dotsc, \phi^{(n)}(x)\right) = 0$$
>>
>>for all $x \in S$.
>>
>
>>[!DEFINITION] Definition: Weak Solution
>>
>>Let $S \subseteq \mathbb{R}$ be [open](../../../../Topology/Topological%20Spaces/Open%20Sets.md) in the [real number line](../../Real%20Number%20Line.md) $\mathbb{R}$.
>>
>>A **weak solution** of $F$ on $S$ is a [locally integrable](../../Real%20Vector%20Functions/Locally%20Lebesgue-Integrable%20Functions.md) [real function](../../Real%20Functions/Real%20Functions.md) $\phi: \mathcal{D}_{\phi} \subseteq \mathbb{R} \to \mathbb{R}$ with $S \subseteq \mathcal{D}_{\phi}$,
>>
>>Let $I \subseteq \mathbb{R}$ be an interval. Suppose $F$ is sufficiently measurable so that the following composition makes sense.
>>
>>A **weak solution** of $F$ on $I$ is a function
>>
>>$$\phi \in W^{n,1}_{\mathrm{loc}}(I)$$
>>
>>such that, using weak derivatives,
>>
>>$$\left(x, \phi(x), \phi'(x), \dotsc, \phi^{(n)}(x)\right) \in \mathcal{D}_F$$
>>
>>and
>>
>>$$F\left(x, \phi(x), \phi'(x), \dotsc, \phi^{(n)}(x)\right) = 0$$
>>
>>for almost every $x \in I$.
>
>>[!NOTATION]
>>
>>Most commonly, an [ODE](./Real%20Ordinary%20Differential%20Equations.md) is written directly as follows:
>>
>>$$F(x, y, y', y'', \dotsc, y^{(n)}) = 0$$
>>
>
>>[!EXAMPLE]- Example: $y'(x) = a y(x)$
>>
>>Consider the [ordinary differential equation](./Real%20Ordinary%20Differential%20Equations.md)
>>
>>$$y'(x) = a y(x)$$
>>
>>for some $a \in \mathbb{R}$. It is a [first-order ODE](./Real%20Ordinary%20Differential%20Equations.md) with the following canonical form $F: \mathbb{R} \times \mathbb{R} \times \mathbb{R} \to \mathbb{R}$:
>>
>>$$F(x, y, y') = y' - a y$$
>>
>>Its [solutions](./Real%20Ordinary%20Differential%20Equations.md) on $\mathbb{R}$ have an [exponential](../../Real%20Functions/Real%20Exponentiation.md) form
>>
>>$$y(x) = c \mathrm{e}^{ax}$$
>>
>>for some $c \in \mathbb{R}$. We easily see that any $y$ of this form is a [solution](./Real%20Ordinary%20Differential%20Equations.md) on $\mathbb{R}$ by [differentiating](../../Real%20Functions/Differentiability%20(Real%20Functions).md):
>>
>>$$y'(x) =  (c \mathrm{e}^{ax})' = ca \mathrm{e}^{ax} = a (c\mathrm{e}^{ax}) = ay(x)$$
>>
>>To show that all [solutions](./Real%20Ordinary%20Differential%20Equations.md) on $\mathbb{R}$ have such a form, let $v$ be any arbitrary [solution](./Real%20Ordinary%20Differential%20Equations.md) on $\mathbb{R}$ and let $q(x) = v(x) \mathrm{e}^{-ax}$. By [differentiating](../../Real%20Functions/Differentiability%20(Real%20Functions).md) $q$, we get:
>>
>>$$q'(x) = v'(x)\mathrm{e}^{-ax} - av(x)\mathrm{e}^{-ax} = \mathrm{e}^{-ax}(v'(x) - a v(x))$$
>>
>>Since $v$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md), we have $v'(x) = a v(x)$ and so $q'(x) = 0$. This means that $q$ must be constant on $\mathbb{R}$, i.e. $q(x) = c$ for some $c \in \mathbb{R}$. Therefore, $c = v(x)\mathrm{e}^{-ax}$ and so $v(x) = c\mathrm{e}^{ax}$.
>>
>
>>[!EXAMPLE]- Example: $y''(t) + \omega^2 y(t) = 0$
>>
>>Consider the [ordinary differential equation](./Real%20Ordinary%20Differential%20Equations.md)
>>
>>$$y''(t) + \omega^2 y(t) = 0$$
>>
>>for some $\omega \in \mathbb{R}_{\gt 0}$. It is very common in physics. It is a [second-order ODE](./Real%20Ordinary%20Differential%20Equations.md) with the following canonical form:
>>
>>$$F: \mathbb{R} \times \mathbb{R} \times \mathbb{R}^{2} \to \mathbb{R} \qquad F(t, y, y', y'') = y'' + \omega^2 y$$
>>
>>It can be shown that its [solutions](./Real%20Ordinary%20Differential%20Equations.md) on $\mathbb{R}$ have the form
>>
>>$$y(t) = A \cos (\omega t) + B \sin (\omega t)$$
>>
>>for some $A, B \in \mathbb{R}$.
>>
>

>[!THEOREM] Theorem: Reduction of an ODE to a First-Order System
>
>Every [explicit](./Real%20Ordinary%20Differential%20Equations.md) [ODE](./Real%20Ordinary%20Differential%20Equations.md)
>
>$$y^{(n)} = f(t, y, y', \dotsc, y^{(n-1)})$$
>
>of [order](./Real%20Ordinary%20Differential%20Equations.md) $n$ is equivalent to an [explicit](./System%20of%20Real%20Ordinary%20Differential%20Equations.md) [system of ODEs](./System%20of%20Real%20Ordinary%20Differential%20Equations.md)
>
>$$\boldsymbol{u}' = \boldsymbol{f}(t, \boldsymbol{u}) \qquad \boldsymbol{f}(t, \boldsymbol{u}) = \begin{bmatrix} u_2 \\ u_3 \\ \vdots \\ u_n \\ f(t, u_1, u_2, \dotsc, u_n) \end{bmatrix}$$
>
>with $n$ equations of order $1$. Specifically, a [function](../../Real%20Functions/Real%20Functions.md) $\phi: \mathcal{D}_{\phi} \subseteq \mathbb{R} \to \mathbb{R}$ is a [solution](./Real%20Ordinary%20Differential%20Equations.md) to the [ODE](./Real%20Ordinary%20Differential%20Equations.md) if and only if the [function](../../Real%20Vector%20Functions/Real%20Vector%20Functions.md) $\boldsymbol{\phi}: \mathcal{D}_{\phi} \subseteq \mathbb{R} \to \mathbb{R}^n$ defined as
>
>$$\boldsymbol{\phi}(t) = \begin{bmatrix} \phi(t) \\ \phi'(t) \\ \phi''(t) \\ \vdots \\ \phi^{(n-1)}(t) \end{bmatrix}$$
>
>is a [solution](./System%20of%20Real%20Ordinary%20Differential%20Equations.md) to the [system of ODEs](./System%20of%20Real%20Ordinary%20Differential%20Equations.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>