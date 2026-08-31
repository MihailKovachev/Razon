---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Extrema (Real Scalar Fields)

## Local Extrema

>[!DEFINITION] Definition: Local Minimum
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md).
>
>We say that $\boldsymbol{p} \in \mathcal{D}$ is a **place of a local minimum** of $f$ if there exists some [open](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) [neighborhood](../../../Topology/Topological%20Spaces/Topological%20Space.md#Neighborhoods) $\mathcal{N}$ of $\boldsymbol{p}$ such that
>
>$$f(\boldsymbol{p}) \le f(\boldsymbol{x})$$
>
>for all $\boldsymbol{x} \in \mathcal{N} \cap \mathcal{D}$.
>
>We call $f(\boldsymbol{p})$ the corresponding **local minimum**.
>
>If the inequality is strict, we say **(place of) strict local minimum**.
>

>[!DEFINITION] Definition: Local Maximum
> 
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md).
> 
>We say that $\boldsymbol{p} \in \mathcal{D}$ is a **place of a local maximum** of $f$ if there exists some [open](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) [neighborhood](../../../Topology/Topological%20Spaces/Topological%20Space.md#Neighborhoods) $\mathcal{N}$ of $\boldsymbol{p}$ such that
>
>$$f(\boldsymbol{p}) \ge f(\boldsymbol{x})$$
>
>for all $\boldsymbol{x} \in \mathcal{N} \cap \mathcal{D}$.
>
>We call $f(\boldsymbol{p})$ the corresponding **local maximum**.
>
>If the inequality is strict, we say **(place of) strict local maximum**.
>

>[!DEFINITION] Definition: Local Extremum
>
>A **local extremum** is a [local minimum](#Local%20Extrema) or a [local maximum](#Local%20Extrema).
>

>[!THEOREM] Theorem: First-Order Necessary Optimality Condition
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md), let $\boldsymbol{p}$ be an [interior point](../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}$ and let $\boldsymbol{r} \in \mathbb{R}^n$.
>
>If $f$ is [directionally differentiable](./Differentiation/Directional%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$ along $\boldsymbol{r}$ and has a [local extremum](#Local%20Extrema) at $\boldsymbol{p}$, then this [directional derivative](./Differentiation/Directional%20Differentiability%20(Real%20Scalar%20Fields).md) is zero:
>
>$$\partial_{\boldsymbol{r}}f(\boldsymbol{p}) = 0$$
>
>>[!EXAMPLE]- Example: $f(x,y) = x^2 + 3y^4$
>>
>>Consider the [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^2 \to \mathbb{R}$ defined as follows:
>>
>>$$f(x,y) = x^2 + 3y^4$$
>>
>>It is [partially differentiable](./Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^2$:
>>
>>$$\partial_x f(x, y) = 2x \qquad \partial_y f(x, y) = 12y^3$$
>>
>>The only possible place for a [local extremum](#Local%20Extrema) is thus $(0, 0)$ because it is the only place where both $\partial_x f(x, y)$ and $\partial_y f(x, y)$ are zero. Indeed, we see that it is a place of a [local minimum](#Local%20Extrema), since $f(x, y) \ge 0 = f(0, 0)$ for all $(x, y) \in \mathbb{R}^2$.
>>
>
>>[!PROOF]-
>>
>>Since $\boldsymbol{p}$ is an [interior point](../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}$, there exists some $\varepsilon \gt 0$ such that $\boldsymbol{p} + t \boldsymbol{r} \in \mathcal{D}$ for all $t \in (-\varepsilon, \varepsilon)$. Let $g : (-\varepsilon, \varepsilon) \to \mathbb{R}$ be a [real function](../Real%20Functions/Real%20Functions.md) defined as follows:
>>
>>$$g(t) = f(\boldsymbol{p} + t \boldsymbol{r})$$
>>
>>Since $f$ has a [local extremum](#Local%20Extrema) at $\boldsymbol{p}$, we know that $g$ must have a [local extremum](../Real%20Functions/Extrema%20of%20Real%20Functions.md) at $t = 0$. Furthermore, since $f$ is [directionally differentiable](./Differentiation/Directional%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$ along $\boldsymbol{r}$ we know the following [limit](../Real%20Functions/Limits%20(Real%20Functions.md) exists:
>>
>>$$\partial_{\boldsymbol{r}}f(\boldsymbol{p}) = \lim_{t \to 0}\frac{f(\boldsymbol{p} + t\boldsymbol{r}) - f(\boldsymbol{p})}{t} = \lim_{t \to 0}\frac{g(t) - f(\boldsymbol{p})}{t} = \lim_{t \to 0} \frac{g(0 + t) - g(0)}{t}$$
>>
>>This is just the [derivative](../Real%20Functions/Differentiability%20(Real%20Functions).md) $g'(0)$. Since $g$ has a [local extremum](../Real%20Functions/Extrema%20of%20Real%20Functions.md) at $t = 0$, we know that $g'(0)$ must be zero. Therefore, $\partial_{\boldsymbol{r}}f(\boldsymbol{p})$ is also zero.
>>
>

>[!THEOREM] Theorem: Second-Order Necessary Optimality Condition
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\boldsymbol{p}$ be an [interior point](../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}$ such that $f$ is twice [totally differentiable](./Differentiation/Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$.
>
>If $f$ has a [local minimum](#Local%20Extrema) at $\boldsymbol{p}$, then its [Hessian matrix](./Differentiation/Hessian%20Matrix.md) $H_f(\boldsymbol{p})$ is [positive semidefinite](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md).
>
>If $f$ has a [local maximum](#Local%20Extrema) at $\boldsymbol{p}$, then its [Hessian matrix](./Differentiation/Hessian%20Matrix.md) $H_f(\boldsymbol{p})$ is [negative semidefinite](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md).
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>
>>- (I) If $f$ is twice [totally differentiable](./Differentiation/Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$ and has a [local minimum](#Local%20Extrema) there, then its [Hessian matrix](./Differentiation/Hessian%20Matrix.md) $H_f(\boldsymbol{p})$ is [positive semidefinite](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md).
>>- (II) If $f$ is twice [totally differentiable](./Differentiation/Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$ and has a [local maximum](#Local%20Extrema) there, then its [Hessian matrix](./Differentiation/Hessian%20Matrix.md) $H_f(\boldsymbol{p})$ is [negative semidefinite](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md).
>>
>>Let $\boldsymbol{r} \in \mathbb{R}^n$. Since $\boldsymbol{p}$ is an [interior point](../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}$, there exists some $\varepsilon \gt 0$ such that $\boldsymbol{p} + t \boldsymbol{r} \in \mathcal{D}$ for all $t \in (-\varepsilon, \varepsilon)$. Let $g : (-\varepsilon, \varepsilon) \to \mathbb{R}$ be a [real function](../Real%20Functions/Real%20Functions.md) defined as follows:
>>
>>$$g(t) = f(\boldsymbol{p} + t \boldsymbol{r})$$
>>
>> Since $f$ is twice [totally differentiable](./Differentiation/Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$ and the [curve](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\gamma(t) = \boldsymbol{p} + t \boldsymbol{r}$ is infinitely [differentiable](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md), we know that $g$ is [differentiable](../Real%20Functions/Differentiability%20(Real%20Functions).md) around $t = 0$. The [chain rule](../Real%20Vector%20Functions/Differentiation/Partial%20Differentiability%20(Real%20Vector%20Functions).md) gives us the following:
>>
>>$$\begin{aligned}g'(t) & = \partial_1 (f \circ \gamma)(t) \\ & = \sum_{j = 1}^n \partial_j f(\gamma(t)) \partial_1 \gamma_j(t) \\ & = \sum_{j = 1}^n \partial_j f(\gamma(t)) \gamma_j'(t) \\ & = \nabla f(\gamma(t)) \cdot \gamma' (t) \\ & = \nabla f(\boldsymbol{p} + t \boldsymbol{r}) \cdot \boldsymbol{r}\end{aligned}$$
>>
>>Since $f$ is twice [totally differentiable](./Differentiation/Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$, we know that $g'$ is [differentiable](../Real%20Functions/Differentiability%20(Real%20Functions).md) at $t = 0$:
>>
>>$$\begin{aligned}g''(t)\vert_{t = 0} & = \left.(\nabla f(\boldsymbol{p} + t \boldsymbol{r}) \cdot \boldsymbol{r})'\right\vert_{t = 0} \\ & = \left.\left(\sum_{j = 1}^n \partial_j f(\boldsymbol{p} + t \boldsymbol{r}) r_j\right)'\right\vert_{t = 0} \\ & = \left.\sum_{j = 1}^n \left( \frac{d}{dt} \partial_j f(\boldsymbol{p} + t \boldsymbol{r}) \right) r_j\right\vert_{t = 0}\end{aligned}$$
>>
>>The [chain rule](../Real%20Vector%20Functions/Differentiation/Partial%20Differentiability%20(Real%20Vector%20Functions).md) gives us the following:
>>
>>$$\begin{aligned} g''(t)\vert_{t = 0} & = \left.\sum_{j = 1}^n \left( \frac{d}{dt} \partial_j f(\boldsymbol{p} + t \boldsymbol{r}) \right) r_j\right\vert_{t = 0} \\ & = \left.\sum_{j = 1}^n \sum_{i = 1}^n \partial_i \partial_j f(\boldsymbol{p} + t \boldsymbol{r}) r_i r_j\right\vert_{t = 0} \\ & = \left.\boldsymbol{r}^T H_f(\boldsymbol{p} + t \boldsymbol{r}) \boldsymbol{r}\right \vert_{t = 0} \\ & = \boldsymbol{r}^T H_f(\boldsymbol{p}) \boldsymbol{r}\end{aligned}$$
>>
>>**Proof of (I):**
>>
>>Since $f$ has a [local minimum](#Local%20Extrema) at $\boldsymbol{p}$, we know that $g$ must have a [local minimum](../Real%20Functions/Extrema%20of%20Real%20Functions.md#Local%20Extrema) at $t = 0$. Therefore, $g''(0) \ge 0$ and so
>>
>>$$g''(0) = \boldsymbol{r}^T H_f(\boldsymbol{p}) \boldsymbol{r} \ge 0.$$
>>
>>Since $\boldsymbol{r} \in \mathbb{R}^n$ was chosen arbitrarily, the [Hessian matrix](./Differentiation/Hessian%20Matrix.md) $H_f(\boldsymbol{p})$ is [positive semidefinite](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md).
>>
>>**Proof of (II):**
>>
>>Since $f$ has a [local maximum](#Local%20Extrema) at $\boldsymbol{p}$, we know that $g$ must have a [local maximum](../Real%20Functions/Extrema%20of%20Real%20Functions.md#Local%20Extrema) at $t = 0$. Therefore, $g''(0) \le 0$ and so
>>
>>$$g''(0) = \boldsymbol{r}^T H_f(\boldsymbol{p}) \boldsymbol{r} \le 0.$$
>>
>>Since $\boldsymbol{r} \in \mathbb{R}^n$ was chosen arbitrarily, the [Hessian matrix](./Differentiation/Hessian%20Matrix.md) $H_f(\boldsymbol{p})$ is [negative semidefinite](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md).
>>
>

>[!THEOREM] Theorem: Second-Order Sufficient Optimality Condition
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\boldsymbol{p}$ be an [interior point](../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}$ such that $f$ is twice [totally differentiable](./Differentiation/Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$.
>
>If the [gradient](./Differentiation/Gradient%20(Real%20Scalar%20Fields).md) $\nabla f(\boldsymbol{p})$ is zero and:
>
>- the [Hessian matrix](./Differentiation/Hessian%20Matrix.md) $H_f(\boldsymbol{p})$ is [positive definite](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md), then $f$ has a [strict local minimum](#Local%20Extrema) at $\boldsymbol{p}$.
>
>- the [Hessian matrix](./Differentiation/Hessian%20Matrix.md) $H_f(\boldsymbol{p})$ is [positive semi-definite](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md) with at least one zero and one non-zero [eigenvalue](../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md), then $f$ has either a [local minimum](#Local%20Extrema) or [saddle point](TODO) at $\boldsymbol{p}$.
>
>- the [Hessian matrix](./Differentiation/Hessian%20Matrix.md) $H_f(\boldsymbol{p})$ is [negative definite](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md), then $f$ has a [strict local maximum](#Local%20Extrema) at $\boldsymbol{p}$.
>
>- the [Hessian matrix](./Differentiation/Hessian%20Matrix.md) $H_f(\boldsymbol{p})$ is [negative semi-definite](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md) with at least one zero and one non-zero [eigenvalue](../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md), then $f$ has either a [local maximum](#Local%20Extrema) or [saddle point](TODO) at $\boldsymbol{p}$.
>
>- the [Hessian matrix](./Differentiation/Hessian%20Matrix.md) $H_f(\boldsymbol{p})$ is [indefinite](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md), then $f$ has a [saddle point](TODO) at $\boldsymbol{p}$.
>
>>[!EXAMPLE]- Example: $f(x, y) = x^2 + 3y^2$
>>
>>Let $f: \mathbb{R}^2 \to \mathbb{R}$ be the [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) defined as follows:
>>
>>$$f(x, y) = x^2 + 3y^2$$
>>
>>It is twice [totally differentiable](../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) on $\mathbb{R}^2$ with the following [gradient](./Differentiation/Gradient%20(Real%20Scalar%20Fields).md) and [Hessian matrix](./Differentiation/Hessian%20Matrix.md):
>>
>>$$\nabla f(x, y) = \begin{bmatrix} 2x \\ 6y\end{bmatrix} \qquad H_f (x, y) = \begin{bmatrix} 2 & 0 \\ 0 & 6\end{bmatrix}$$
>>
>>The [gradient](./Differentiation/Gradient%20(Real%20Scalar%20Fields).md) is zero if and only if $x = y = 0$. We have 
>>
>>$$H_f (0, 0) = \begin{bmatrix} 2 & 0 \\ 0 & 6\end{bmatrix}$$
>>
>>with the [eigenvalues](../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) $2$ and $6$. Therefore, $H_f (0, 0)$ is [positive definite](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md) and so $f$ has a [local minimum](#Local%20Extrema) at $(0,0)$.
>>
>
>>[!EXAMPLE]- Example: $f(x, y) = (x-1)^2 - y^4 -4y$
>>
>>Let $f: \mathbb{R}^2 \to \mathbb{R}$ be the [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) defined as follows:
>>
>>$$f(x, y) = (x-1)^2 - y^4 -4y$$
>>
>>It is twice [totally differentiable](../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) on $\mathbb{R}^2$ with the following [gradient](./Differentiation/Gradient%20(Real%20Scalar%20Fields).md) and [Hessian matrix](./Differentiation/Hessian%20Matrix.md):
>>
>>$$\nabla f(x, y) = \begin{bmatrix} 2x - 2 \\ -4y^3 - 4\end{bmatrix} \qquad H_f (x, y) = \begin{bmatrix} 2 & 0 \\ 0 & -12y^2\end{bmatrix}$$
>>
>>The [gradient](./Differentiation/Gradient%20(Real%20Scalar%20Fields).md) is zero if and only if $x = 1$ and $y = -1$. We have 
>>
>>$$H_f (1, -1) = \begin{bmatrix} 2 & 0 \\ 0 & -12\end{bmatrix}$$
>>
>>with the [eigenvalues](../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) $2$ and $-12$. Therefore, $H_f (1, -1)$ is [indefinite](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md) and so $f$ has a [saddle point](TODO) at $(1,-1)$.
>>
>
>>[!EXAMPLE]- Example: $f(x, y) = x^2 + y^4$
>>
>>Let $f: \mathbb{R}^2 \to \mathbb{R}$ be the [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) defined as follows:
>>
>>$$f(x, y) = x^2 + y^4$$
>>
>>It is twice [totally differentiable](../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) on $\mathbb{R}^2$ with the following [gradient](./Differentiation/Gradient%20(Real%20Scalar%20Fields).md) and [Hessian matrix](./Differentiation/Hessian%20Matrix.md):
>>
>>$$\nabla f(x, y) = \begin{bmatrix} 2x \\ 4y^3\end{bmatrix} \qquad H_f (x, y) = \begin{bmatrix} 2 & 0 \\ 0 & 12y^2\end{bmatrix}$$
>>
>>The [gradient](./Differentiation/Gradient%20(Real%20Scalar%20Fields).md) is zero if and only if $x = y = 0$. We have 
>>
>>$$H_f (0, 0) = \begin{bmatrix} 2 & 0 \\ 0 & 0\end{bmatrix}$$
>>
>>with the [eigenvalues](../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) $2$ and $0$. Therefore, $H_f (0, 0)$ is [positive semi-definite](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md) and so $f$ has either a [local minimum](#Local%20Extrema) or a [saddle point](TODO) at $(0,0)$. Since $x^2 \ge 0$ and $y^4 \ge 0$ for all real $x$ and $y$, $f(x,y) \ge f(0,0) = 0$, so $f$ has a [local minimum](#Local%20Extrema) at $(0,0)$, but not a [strict local minimum](#Local%20Extrema).
>>
>
>>[!EXAMPLE]- Example: $f(x, y) = x^2$
>>
>>Let $f: \mathbb{R}^2 \to \mathbb{R}$ be the [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) defined as follows:
>>
>>$$f(x, y) = x^2$$
>>
>>It is twice [totally differentiable](../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) on $\mathbb{R}^2$ with the following [gradient](./Differentiation/Gradient%20(Real%20Scalar%20Fields).md) and [Hessian matrix](./Differentiation/Hessian%20Matrix.md):
>>
>>$$\nabla f(x, y) = \begin{bmatrix} 2x \\ 0\end{bmatrix} \qquad H_f (x, y) = \begin{bmatrix} 2 & 0 \\ 0 & 0\end{bmatrix}$$
>>
>>The [gradient](./Differentiation/Gradient%20(Real%20Scalar%20Fields).md) is zero if and only if $x = 0$. We have 
>>
>>$$H_f (0, y) = \begin{bmatrix} 2 & 0 \\ 0 & 0\end{bmatrix}$$
>>
>>with the [eigenvalues](../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) $2$ and $0$. Therefore, $H_f (0, y)$ is [positive semi-definite](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md) and so $f$ has either a [local minimum](#Local%20Extrema) or a [saddle point](TODO) at $(0,y)$. Since $x^2 \ge 0$ for all real $x$ and $y$, $f(x,y) \ge f(0,y) = 0$, so $f$ has a [local minimum](#Local%20Extrema) at $(0,y)$, but not a [strict local minimum](#Local%20Extrema).
>>
>
>>[!EXAMPLE]- Example: $f(x, y) = x^2 + y^3$
>>
>>Let $f: \mathbb{R}^2 \to \mathbb{R}$ be the [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) defined as follows:
>>
>>$$f(x, y) = x^2 + y^3$$
>>
>>It is twice [totally differentiable](../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) on $\mathbb{R}^2$ with the following [gradient](./Differentiation/Gradient%20(Real%20Scalar%20Fields).md) and [Hessian matrix](./Differentiation/Hessian%20Matrix.md):
>>
>>$$\nabla f(x, y) = \begin{bmatrix} 2x \\ 3y^2\end{bmatrix} \qquad H_f (x, y) = \begin{bmatrix} 2 & 0 \\ 0 & 6y\end{bmatrix}$$
>>
>>The [gradient](./Differentiation/Gradient%20(Real%20Scalar%20Fields).md) is zero if and only if $x = y = 0$. We have 
>>
>>$$H_f (0, 0) = \begin{bmatrix} 2 & 0 \\ 0 & 0\end{bmatrix}$$
>>
>>with the [eigenvalues](../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) $2$ and $0$. Therefore, $H_f (0, 0)$ is [positive semi-definite](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md) and so $f$ has either a [local minimum](#Local%20Extrema) or a [saddle point](TODO) at $(0,0)$. For $x=0$, we have $f(0,y) = y^3$. For all $\delta \gt 0$, we have $f(0, y) \lt 0$ if $y \in (-\delta, 0)$ and $f(0, y) \gt 0$ if $y \in (0, +\delta)$. Therefore, $f$ cannot have a [local minimum](#Local%20Extrema) at $(0,0)$ and so it must have a [saddle point](TODO) there.
>>
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>
>>- (I) If the [Hessian matrix](./Differentiation/Hessian%20Matrix.md) $H_f(\boldsymbol{p})$ is [positive definite](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md), then $f$ has a [strict local minimum](#Local%20Extrema) at $\boldsymbol{p}$.
>>- (II) If the [Hessian matrix](./Differentiation/Hessian%20Matrix.md) $H_f(\boldsymbol{p})$ is [negative definite](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md), then $f$ has a [strict local maximum](#Local%20Extrema) at $\boldsymbol{p}$.
>>
>>Since $f$ is twice [totally differentiable](./Differentiation/Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$ it has a second-order [Taylor expansion](./Taylor%20Expansion%20(Real%20Scalar%20Fields).md) around $\boldsymbol{p}$
>>
>>$$f(\boldsymbol{x}) = f(\boldsymbol{p}) + \nabla f(\boldsymbol{p})^{\mathsf{T}}(\boldsymbol{x}-\boldsymbol{p}) + \frac{1}{2} (\boldsymbol{x}-\boldsymbol{p})^{\mathsf{T}} \boldsymbol{H}_f(\boldsymbol{p})(\boldsymbol{x}-\boldsymbol{p}) + R_3 (\boldsymbol{p}; \boldsymbol{x} - \boldsymbol{p})$$
>>
>>with
>>
>>$$R_3 (\boldsymbol{p}; \boldsymbol{x} - \boldsymbol{p}) = o(||\boldsymbol{x} - \boldsymbol{p}||^2) \qquad \text{for} \qquad \boldsymbol{x} \to \boldsymbol{p}.$$
>>
>>Since $\nabla f(\boldsymbol{p}) = \boldsymbol{0}$, we have:
>>
>>$$f(\boldsymbol{x}) = f(\boldsymbol{p}) + \frac{1}{2} (\boldsymbol{x}-\boldsymbol{p})^{\mathsf{T}} \boldsymbol{H}_f(\boldsymbol{p})(\boldsymbol{x}-\boldsymbol{p}) + R_3 (\boldsymbol{p}; \boldsymbol{x} - \boldsymbol{p})$$
>>
>>$$f(\boldsymbol{x}) - f(\boldsymbol{p}) = \frac{1}{2} (\boldsymbol{x}-\boldsymbol{p})^{\mathsf{T}} \boldsymbol{H}_f(\boldsymbol{p})(\boldsymbol{x}-\boldsymbol{p}) + R_3 (\boldsymbol{p}; \boldsymbol{x} - \boldsymbol{p})$$
>>
>>Since $H_f({\boldsymbol{p}})$ is a [real symmetric matrix](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md), we know that
>>
>>$$\lambda_1 ||\boldsymbol{x} - \boldsymbol{p}||^2 \le (\boldsymbol{x}-\boldsymbol{p})^{\mathsf{T}} \boldsymbol{H}_f(\boldsymbol{p})(\boldsymbol{x}-\boldsymbol{p}) \le \lambda_n ||\boldsymbol{x} - \boldsymbol{p}||^2,$$
>>
>>where $\lambda_n \ge \cdots \ge \lambda_1$ are the [eigenvalues](../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) of $H_f(\boldsymbol{p})$.
>>
>>**Proof of (I):**
>>
>>Since $H_f(\boldsymbol{p})$ is [positive definite](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md), we get
>>
>>$$0 \lt \lambda_1 ||\boldsymbol{x} - \boldsymbol{p}||^2 \le (\boldsymbol{x}-\boldsymbol{p})^{\mathsf{T}} \boldsymbol{H}_f(\boldsymbol{p})(\boldsymbol{x}-\boldsymbol{p}) \le \lambda_n ||\boldsymbol{x} - \boldsymbol{p}||^2$$
>>
>>and so 
>>
>>$$\frac{1}{2} (\boldsymbol{x}-\boldsymbol{p})^{\mathsf{T}} \boldsymbol{H}_f(\boldsymbol{p})(\boldsymbol{x}-\boldsymbol{p}) \ge \frac{1}{2}\lambda_1 ||\boldsymbol{x} - \boldsymbol{p}||^2 \gt 0.$$
>>
>>Since $R_3 (\boldsymbol{p}; \boldsymbol{x} - \boldsymbol{p})$ is [little o](../Asymptotic%20Analysis/Bachmann-Landau%20Notation.md) of $||\boldsymbol{x} - \boldsymbol{p}||^2$ for $\boldsymbol{x} \to \boldsymbol{p}$, we know that for $\varepsilon = \frac{1}{4}\lambda_1$, there exists some [deleted neighborhood](../Euclidean%20Space/Euclidean%20Space.md) $\mathcal{N}(\boldsymbol{p})$ such that
>>
>>$$|R_3 (\boldsymbol{p}; \boldsymbol{x} - \boldsymbol{p})| \le \frac{1}{4}\lambda_1||\boldsymbol{x} - \boldsymbol{p}||^2$$
>>
>>for all $\boldsymbol{x} \in \mathcal{N}(\boldsymbol{p}) \cap \mathcal{D}$. More specifically, we know that
>>
>>$$R_3 (\boldsymbol{p}; \boldsymbol{x} - \boldsymbol{p}) \ge -\frac{1}{4}\lambda_1||\boldsymbol{x} - \boldsymbol{p}||^2$$
>>
>>for all $\boldsymbol{x} \in \mathcal{N}(\boldsymbol{p}) \cap \mathcal{D}$. Therefore,
>>
>>$$\begin{aligned} f(\boldsymbol{x}) - f(\boldsymbol{p}) & = \frac{1}{2} (\boldsymbol{x}-\boldsymbol{p})^{\mathsf{T}} \boldsymbol{H}_f(\boldsymbol{p})(\boldsymbol{x}-\boldsymbol{p}) + R_3 (\boldsymbol{p}; \boldsymbol{x} - \boldsymbol{p}) \\ & \ge \frac{1}{2}\lambda_1 ||\boldsymbol{x} - \boldsymbol{p}||^2 -\frac{1}{4}\lambda_1||\boldsymbol{x} - \boldsymbol{p}||^2 = \frac{1}{4}\lambda_1||\boldsymbol{x} - \boldsymbol{p}||^2 \gt 0\end{aligned}$$
>>
>>for all $\boldsymbol{x} \in \mathcal{N}(\boldsymbol{p}) \cap \mathcal{D}$. In others words, we know that
>>
>>$$f(\boldsymbol{p}) \lt f(\boldsymbol{x})$$
>>
>>for all $\boldsymbol{x} \in \mathcal{N}(\boldsymbol{p}) \cap \mathcal{D}$ and so $f$ has a [strict local minimum](./Extrema%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$.
>>
>>**Proof of (II):**
>>
>>Since $H_f(\boldsymbol{p})$ is [negative definite](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md), we get
>>
>>$$\lambda_1 ||\boldsymbol{x} - \boldsymbol{p}||^2 \le (\boldsymbol{x}-\boldsymbol{p})^{\mathsf{T}} \boldsymbol{H}_f(\boldsymbol{p})(\boldsymbol{x}-\boldsymbol{p}) \le \lambda_n ||\boldsymbol{x} - \boldsymbol{p}||^2 \lt 0$$
>>
>>and so 
>>
>>$$\frac{1}{2} (\boldsymbol{x}-\boldsymbol{p})^{\mathsf{T}} \boldsymbol{H}_f(\boldsymbol{p})(\boldsymbol{x}-\boldsymbol{p}) \le \frac{1}{2}\lambda_n ||\boldsymbol{x} - \boldsymbol{p}||^2 \lt 0.$$
>>
>>Since $R_3 (\boldsymbol{p}; \boldsymbol{x} - \boldsymbol{p})$ is [little o](../Asymptotic%20Analysis/Bachmann-Landau%20Notation.md) of $||\boldsymbol{x} - \boldsymbol{p}||^2$ for $\boldsymbol{x} \to \boldsymbol{p}$, we know that for $\varepsilon = -\frac{1}{4}\lambda_n$, there exists some [deleted neighborhood](../Euclidean%20Space/Euclidean%20Space.md) $\mathcal{N}(\boldsymbol{p})$ such that
>>
>>$$|R_3 (\boldsymbol{p}; \boldsymbol{x} - \boldsymbol{p})| \le -\frac{1}{4}\lambda_n||\boldsymbol{x} - \boldsymbol{p}||^2$$
>>
>>for all $\boldsymbol{x} \in \mathcal{N}(\boldsymbol{p}) \cap \mathcal{D}$. More specifically, we know that
>>
>>$$R_3 (\boldsymbol{p}; \boldsymbol{x} - \boldsymbol{p}) \le -\frac{1}{4}\lambda_n||\boldsymbol{x} - \boldsymbol{p}||^2$$
>>
>>for all $\boldsymbol{x} \in \mathcal{N}(\boldsymbol{p}) \cap \mathcal{D}$. Therefore,
>>
>>$$\begin{aligned} f(\boldsymbol{x}) - f(\boldsymbol{p}) & = \frac{1}{2} (\boldsymbol{x}-\boldsymbol{p})^{\mathsf{T}} \boldsymbol{H}_f(\boldsymbol{p})(\boldsymbol{x}-\boldsymbol{p}) + R_3 (\boldsymbol{p}; \boldsymbol{x} - \boldsymbol{p}) \\ & \le \frac{1}{2}\lambda_n ||\boldsymbol{x} - \boldsymbol{p}||^2 - \frac{1}{4}\lambda_n||\boldsymbol{x} - \boldsymbol{p}||^2 = \frac{1}{4}\lambda_n||\boldsymbol{x} - \boldsymbol{p}||^2 \lt 0\end{aligned}$$
>>
>>for all $\boldsymbol{x} \in \mathcal{N}(\boldsymbol{p}) \cap \mathcal{D}$. In others words, we know that
>>
>>$$f(\boldsymbol{p}) \gt f(\boldsymbol{x})$$
>>
>>for all $\boldsymbol{x} \in \mathcal{N}(\boldsymbol{p}) \cap \mathcal{D}$ and so $f$ has a [strict local maximum](./Extrema%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$.
>>
>

