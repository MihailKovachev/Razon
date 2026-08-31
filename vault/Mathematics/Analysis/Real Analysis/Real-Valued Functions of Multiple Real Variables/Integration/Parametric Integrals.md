---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Parametric Integrals

>[!DEFINITION] Definition: Parametric Integral
>
>A **parametric integral** is a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $\mathcal{I}: \mathcal{D}_{\mathcal{I}} \subseteq \mathbb{R}^{n-1} \to \mathbb{R}$, defined via a [Riemann integral](../../Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md)
>
>$$\mathcal{I}(x_1, \dotsc, x_{k-1}, x_{k+1}, \dotsc, x_n) \overset{\text{def}}{=} \int_{l(x_1, \dotsc, x_{k-1}, x_{k+1}, \dotsc, x_n)}^{u(x_1, \dotsc, x_{k-1}, x_{k+1}, \dotsc, x_n)} f(x_1, \dotsc, x_n) \, \mathrm{d}x_k,$$
>
>where $f: \mathcal{D}_f \to \mathbb{R}$ and $l, u: \mathcal{D}_{\mathcal{I}} \to \mathbb{R}$ are [real scalar fields](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) such that the [real function](../../Real%20Functions/Real%20Functions.md) $x_k \to f(x_1, \dotsc, x_k, \dotsc, x_n)$ is [Riemann integrable](../../Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md) on the [closed interval](../../Euclidean%20Space/Euclidean%20Space.md) between $l(x_1, \dotsc, x_{k-1}, x_{k+1}, \dotsc, x_n)$ and $u(x_1, \dotsc, x_{k-1}, x_{k+1}, \dotsc, x_n)$ for all $\begin{bmatrix}x_1, \dotsc, x_{k-1}, x_{k+1}, \dotsc, x_n \end{bmatrix}^{\mathsf{T}} \in \mathcal{D}_{\mathcal{I}}$.
>

>[!THEOREM] Theorem: Continuity of Parametric Integrals
>
>Let $\mathcal{I}: \mathcal{D}_{\mathcal{I}} \subseteq \mathbb{R}^{n-1} \to \mathbb{R}$ be a [parametric integral](./Parametric%20Integrals.md) defined as
>
>$$\mathcal{I}(x_1, \dotsc, x_{k-1}, x_{k+1}, \dotsc, x_n) = \int_{l(x_1, \dotsc, x_{k-1}, x_{k+1}, \dotsc, x_n)}^{u(x_1, \dotsc, x_{k-1}, x_{k+1}, \dotsc, x_n)} f(x_1, \dotsc, x_n) \, \mathrm{d}x_k$$
>
>for some [real scalar fields](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ and $l, u: \mathcal{D}_{\mathcal{I}} \to \mathbb{R}$.
>
>If $f$, $l$ and $u$ are [continuous](../Continuity%20(Real%20Scalar%20Fields).md), then so is $\mathcal{I}$.
>
>>[!EXAMPLE]- Example: $F(x) = \int_0^{\uppi} x \sin y \, \mathrm{d}y$
>>
>>Consider the [parametric integral](./Parametric%20Integrals.md) $F: \mathbb{R} \to \mathbb{R}$ defined as follows:
>>
>>$$F(x) = \int_0^{\uppi} x \sin y \, \mathrm{d}y$$
>>
>>In this case, $l$ and $u$ are the following [real functions](../../Real%20Functions/Real%20Functions.md) $l, u: \mathbb{R} \to \mathbb{R}$:
>>
>>$$l(x) = 0 \qquad u(x) = \uppi$$
>>
>>For $f$, we have the following [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^2 \to \mathbb{R}$:
>>
>>$$f(x, y) = x \sin y$$
>>
>>We see that $l$ and $u$ are [continuous](../../Real%20Functions/Continuity%20(Real%20Functions).md) on $\mathbb{R}$ and that $f$ is [continuous](../Continuity%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^2$. Therefore, $F$ is [continuous](../../Real%20Functions/Continuity%20(Real%20Functions).md) on $\mathbb{R}$.
>>
>
>>[!EXAMPLE]- 
>>
>>Consider the [parametric integral](./Parametric%20Integrals.md) $F: \mathbb{R} \to \mathbb{R}$ defined as
>>
>>$$F(x) = \int_0^{1} f(x,y) \mathrm{d}y,$$
>>
>>where $f$ is the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: [0,1] \times [0,1] \to \mathbb{R}$ defined as follows:
>>
>>$$f(x,y) = \begin{cases} \frac{y}{x^2} & \text{if} & 0 \le y \lt x \\ \frac{2x - y}{x^2} & \text{if} & x \le y \lt 2x \\ 0 & \text{if} & 2x \le y \end{cases}$$
>>
>>In this case, $l$ and $u$ are the following [real functions](../../Real%20Functions/Real%20Functions.md) $l, u: \mathbb{R} \to \mathbb{R}$:
>>
>>$$l(x) = 0 \qquad u(x) = 1$$
>>
>>Both $l$ and $u$ are [continuous](../../Real%20Functions/Continuity%20(Real%20Functions).md) on $\mathbb{R}$. However, $f$ is *not* [continuous](../Continuity%20(Real%20Scalar%20Fields).md) at $\boldsymbol{0}$. Therefore, we cannot use the theorem.
>>
>>Indeed, it turns out that $F(x)$ is *not* [continuous](../../Real%20Functions/Continuity%20(Real%20Functions).md) at $x = 0$:
>>
>>$$F(0) = \int_0^{1} f(0,y) \mathrm{d}y = \int_0^{1} 0 \mathrm{d}y = 0$$
>>
>>However,
>>
>>$$\begin{aligned}\lim_{x \to 0} F(x) & = \lim_{x \to 0} \int_0^{1} f(x,y) \mathrm{d}y \\ & = \lim_{x \to 0} \left( \int_0^{x} \frac{y}{x^2} \mathrm{d}y + \int_{x}^{2x} \frac{2x - y}{x^2} \mathrm{d}y + \int_{2x}^{1} 0 \mathrm{d}y \right) \\ & = \lim_{x \to 0} \left( \frac{1}{x^2} \left[ \frac{y^2}{2} \right]_0^x + \frac{1}{x^2} \left[ 2xy - \frac{y^2}{2} \right]_x^{2x} \right) \\ & = \lim_{x \to 0} \left( \frac{1}{x^2} \left( \frac{x^2}{2} \right) + \frac{1}{x^2} \left( \left(4x^2 - 2x^2\right) - \left(2x^2 - \frac{x^2}{2}\right) \right) \right) \\ & = \lim_{x \to 0} \left( \frac{1}{2} + \frac{1}{x^2} \left( 2x^2 - \frac{3x^2}{2} \right) \right) \\ & = \lim_{x \to 0} \left( \frac{1}{2} + \frac{1}{2} \right) \\ & = 1 \ne 0 \end{aligned}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Leibniz Integral Rule (Differentiation under the Integral Sign)
>
>Let $\mathcal{I}: \mathcal{D}_{\mathcal{I}} \subseteq \mathbb{R}^{n-1} \to \mathbb{R}$ be a [parametric integral](./Parametric%20Integrals.md) defined as
>
>$$\mathcal{I}(x_1, \dotsc, x_{k-1}, x_{k+1}, \dotsc, x_n) = \int_{l(x_1, \dotsc, x_{k-1}, x_{k+1}, \dotsc, x_n)}^{u(x_1, \dotsc, x_{k-1}, x_{k+1}, \dotsc, x_n)} f(x_1, \dotsc, x_n) \, \mathrm{d}x_k$$
>
>for some [real scalar fields](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ and $l, u: \mathcal{D}_{\mathcal{I}} \to \mathbb{R}$.
>
>If $f$, $l$ and $u$ are [continuously partially differentiable](../Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) with respect to $x_j$ ($j \ne k$) variable, then so is $\mathcal{I}$ and its [partial derivative](../Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) is the following:
>
>$$\partial_{x_j} \mathcal{I} = \int_{l(x_1, \dotsc, x_{k-1}, x_{k+1}, \dotsc, x_n)}^{u(x_1, \dotsc, x_{k-1}, x_{k+1}, \dotsc, x_n)} \partial_{ x_j} f(x_1, \dotsc, x_n) \, \mathrm{d}x_k + f\big|_{x_k=u} \partial_{x_j} u - f\big|_{x_k=l} \partial_{x_j} l$$
>
>>[!EXAMPLE]- Example: $F(x) = \int_{x^2}^{3-x} \sin(xy) \,\mathrm{d}y$
>>
>>Consider the [parametric integral](./Parametric%20Integrals.md) $F: \mathbb{R} \to \mathbb{R}$ defined as follows:
>>
>>$$F(x) = \int_{x^2}^{3-x} \sin(xy) \,\mathrm{d}y$$
>>
>>In this case, $l$ and $u$ are the following [real functions](../../Real%20Functions/Real%20Functions.md) $l, u: \mathbb{R} \to \mathbb{R}$:
>>
>>$$l(x) = x^2 \qquad u(x) = 3-x$$
>>
>>For $f$, we have the following [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^2 \to \mathbb{R}$:
>>
>>$$f(x, y) = \sin (xy)$$
>>
>>We see that $l$ and $u$ are [continuously differentiable](../../Real%20Functions/Differentiability%20(Real%20Functions).md) on $\mathbb{R}$ and that $f$ is [continuously partially differentiable](../Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^2$ w.r.t. $x$. Therefore, $F$ is [continuously differentiable](../../Real%20Functions/Differentiability%20(Real%20Functions).md) on $\mathbb{R}$ with the following [derivative](../../Real%20Functions/Differentiability%20(Real%20Functions).md):
>>
>>$$\begin{aligned} F'(x) & = \int_{x^2}^{3-x} \partial_x f(x,y) \,\mathrm{d}y + f(x,u(x)) u'(x) - f(x, l(x)) l'(x) \\ & = \int_{x^2}^{3-x} y \cos(xy) \,\mathrm{d}y + \sin(x(3-x)) \cdot (3-x)' - \sin(x(x^2)) \cdot (x^2)' \\ & = \int_{x^2}^{3-x} y \cos(xy) \,\mathrm{d}y + \sin(3x - x^2) \cdot (-1) - \sin(x^3) \cdot (2x) \\ & = \int_{x^2}^{3-x} y \cos(xy) \,\mathrm{d}y - \sin(3x - x^2) - 2x \sin(x^3) \end{aligned}$$
>>
>>For $x \ne 0$, we get:
>>
>>$$\begin{aligned} F'(x) & = \int_{x^2}^{3-x} y \cos(xy) \,\mathrm{d}y - \sin(3x - x^2) - 2x \sin(x^3) \\ & = \left.\left( \frac{y}{x} \sin(xy) + \frac{1}{x^2} \cos(xy) \right)\right\vert_{y=x^2}^{y=3-x} - \sin(3x - x^2) - 2x \sin(x^3) \\ & = \left( \frac{3-x}{x} \sin(3x-x^2) + \frac{1}{x^2} \cos(3x-x^2) \right) - \left( x \sin(x^3) + \frac{1}{x^2} \cos(x^3) \right) - \sin(3x - x^2) - 2x \sin(x^3) \\ & = \left( \frac{3-x}{x} - 1 \right) \sin(3x - x^2) + \frac{1}{x^2} \cos(3x - x^2) - (x + 2x) \sin(x^3) - \frac{1}{x^2} \cos(x^3) \\ & = \frac{3-2x}{x} \sin(3x - x^2) + \frac{1}{x^2} \cos(3x - x^2) - 3x \sin(x^3) - \frac{1}{x^2} \cos(x^3) \end{aligned}$$
>>
>>For $x = 0$, we get:
>>
>>$$\begin{aligned} F'(0) & = \int_{0}^{3} y \cos(0) \,\mathrm{d}y - \sin(0) - 0 \\ & = \int_{0}^{3} y \,\mathrm{d}y \\ & = \left. \frac{1}{2}y^2 \right\vert_{0}^{3} = \frac{9}{2}\end{aligned}$$
>>
>>We can also verify that $F'$ is [continuous](../../Real%20Functions/Continuity%20(Real%20Functions).md):
>>
>>$$\begin{aligned} \lim_{x \to 0} F'(x) & = \lim_{x \to 0} \left( \frac{3-2x}{x} \sin(3x - x^2) + \frac{\cos(3x - x^2) - \cos(x^3)}{x^2} - 3x \sin(x^3) \right) \\ & = \lim_{x \to 0} \left( (3-2x)(3-x) \frac{\sin(3x - x^2)}{3x - x^2} \right) + \lim_{x \to 0} \left( \frac{\cos(3x - x^2) - \cos(x^3)}{x^2} \right) - 0 \\ & = 9 \cdot 1 + \lim_{x \to 0} \frac{-(3-2x)\sin(3x - x^2) + 3x^2\sin(x^3)}{2x} \quad \text{(using L'Hôpital's rule)} \\ & = 9 + \lim_{x \to 0} \left( -\frac{(3-2x)(3-x)}{2} \frac{\sin(3x - x^2)}{3x - x^2} + \frac{3}{2} x \sin(x^3) \right) \\ & = 9 - \frac{9}{2} \cdot 1 + 0 \\ & = \frac{9}{2} \end{aligned}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Fubini's Theorem
>
>Let $f: [a_1, b_1] \times \cdots \times [a_n, b_n] \subset \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md).
>
>If $f$ is [continuous](../Continuity%20(Real%20Scalar%20Fields).md), then [iterated integrals](TODO) of $f$ are invariant for all [permutations](../../../../Combinatorics/Permutations.md) $\sigma: \{1, \dotsc, n\} \to \{1, \dotsc, n\}$:
>
>$$\int_{a_1}^{b_1} \cdots \int_{a_n}^{b_n} f(x_1, \dotsc, x_n) \,\mathrm{d}x_n \cdots \mathrm{d}x_1 = \int_{a_{\sigma(1)}}^{b_{\sigma(1)}} \cdots \int_{a_{\sigma(n)}}^{b_{\sigma(n)}} f(x_1, \dotsc, x_n) \,\mathrm{d}x_{\sigma(n)} \cdots \mathrm{d}x_{\sigma(1)}$$
>
>>[!EXAMPLE]- Example: $f(x, y) = 2x\mathrm{e}^y$
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: [0,1] \times [0,1]$ defined as follows:
>>
>>$$f(x, y) = 2x\mathrm{e}^y$$
>>
>>We have:
>>
>>$$\begin{aligned}\int_0^1 \int_0^1 2x\mathrm{e}^y \,\mathrm{d}y \,\mathrm{d}x & = \int_0^1 \left(\left. 2x \mathrm{e}^y\right\vert_{y=0}^{y=1}\right) \,\mathrm{d}x \\ & = \int_0^1 (2x \mathrm{e}^1 - 2x \mathrm{e}^0) \, \mathrm{d}x \\ & = \int_0^1 2x(\mathrm{e} - 1) \, \mathrm{d}x \\ & = (\mathrm{e} - 1) \int_0^1 2x \,\mathrm{d}x \\ & = \left.(e-1)x^2 \right\vert_{0}^1 \\ & = \mathrm{e} - 1\end{aligned}$$
>>
>>Also:
>>
>>$$\begin{aligned}\int_0^1 \int_0^1 2x\mathrm{e}^y \,\mathrm{d}x \,\mathrm{d}y & = \int_0^1 \left(\left. x^2 \mathrm{e}^y\right\vert_{x=0}^{x=1}\right) \,\mathrm{d}y \\ & = \int_0^1 (\mathrm{e}^y - 0) \, \mathrm{d}y \\ & = \int_0^1 \mathrm{e}^y \, \mathrm{d}y \\ & = \left. \mathrm{e}^y \right\vert_{0}^1 \\ & = \mathrm{e} - 1\end{aligned}$$
>>
>>Therefore,
>>
>>$$\int_0^1 \int_0^1 2x\mathrm{e}^y \,\mathrm{d}y \,\mathrm{d}x = \int_0^1 \int_0^1 2x\mathrm{e}^y \,\mathrm{d}x \,\mathrm{d}y,$$
>>
>>which is what we expect because $f$ is [continuous](../Continuity%20(Real%20Scalar%20Fields).md).
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>