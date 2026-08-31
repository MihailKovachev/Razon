---
tags:
  - real-analysis
  - vector-analysis
  - analysis
  - mathematics
---

# Conservative Vector Fields

>[!DEFINITION] Definition: Conservative Vector Field
>
>Let $U \subseteq \mathbb{R}^n$ be [open](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets).
>
>A [real vector field](./Real%20Vector%20Fields.md) $f: U \to \mathbb{R}^n$ is **conservative** if there exists a [totally differentiable](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Total%20Differentiability%20(Real%20Scalar%20Fields).md) [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $F: U \to \mathbb{R}$ whose [gradient](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Gradient%20(Real%20Scalar%20Fields).md) is $f$:
>
>$$f(\boldsymbol{x}) = \nabla F(\boldsymbol{x}) \qquad \boldsymbol{x} \in U$$
>
>We also say that $f$ is a **gradient field** or a **potential field**.
>

>[!DEFINITION] Definition: Potential Function
>
>Let $U \subseteq \mathbb{R}^n$ be [open](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) and let $f: U \to \mathbb{R}^n$ be a [conservative](./Conservative%20Vector%20Fields.md) [real vector field](./Real%20Vector%20Fields.md).
>
>A **potential function** of $f$ is any [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $F: U \to \mathbb{R}$ whose negative [gradient](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Gradient%20(Real%20Scalar%20Fields).md) is $f$:
>
>$$f(\boldsymbol{x}) = \nabla F(\boldsymbol{x}) \qquad \boldsymbol{x} \in U$$
>
>>[!NOTE]
>>
>>In pure mathematical contexts, [potential functions](./Conservative%20Vector%20Fields.md) are almost universally defined in the above way. However, in physics and applied mathematics, a minus sign is commonly used: $-\nabla F$.
>>
>

>[!ALGORITHM] Algorithm: Finding Potential Function
>
>Let $U \subseteq \mathbb{R}^n$ be [open](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) and let $f: U \to \mathbb{R}^n$ be a [conservative](./Conservative%20Vector%20Fields.md) [real vector field](./Real%20Vector%20Fields.md) with [component functions](../Real%20Vector%20Functions/Real%20Vector%20Functions.md) $f_1, \dotsc, f_n$. We want to find a [potential function](./Conservative%20Vector%20Fields.md) $F: U \to \mathbb{R}$:
>
>$$f(\boldsymbol{x}) = \nabla F(\boldsymbol{x}) \qquad \boldsymbol{x} \in U$$
>
>1. Set $\partial_1 F = f_1$ and [antidifferentiate](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Partial%20Antidifferentiability%20(Real%20Scalar%20Fields).md) w.r.t. the first variable:
>
>    $$F(x_1, \dotsc, x_n) = \int f_1 (x_1, \dotsc, x_n) \,\mathrm{d}x_1 + C_1(x_2, \dotsc, x_n)$$
>
>2. For $i \in \{2, \dotsc, n\}$:
>
>    - [Differentiate](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) the expression for $F$ obtained from the previous step w.r.t. $x_i$ and set it equal to $f_i$. 
>    - Solve for $\partial_i C_{i-1}$ and [antidifferentiate](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Partial%20Antidifferentiability%20(Real%20Scalar%20Fields).md) w.r.t. $x_i$ to find 
>    
>    $$C_{i-1}(x_i, \dotsc, x_n) = \int \partial_i C_{i-1}(x_i, \dotsc, x_n) \,\mathrm{d}x_i + C_i(x_{i+1}, \dotsc, x_n)$$
>
>>[!EXAMPLE]-
>>
>>Consider the [real vector field](./Real%20Vector%20Fields.md) $f: \mathbb{R}^3 \to \mathbb{R}^3$ defined as follows:
>>
>>$$f(x, y, z) = \begin{bmatrix}\mathrm{e}^x y + 1 \\ \mathrm{e}^x + z \\ y\end{bmatrix}$$
>>
>>It is [conservative](./Conservative%20Vector%20Fields.md) because its [curl](./Differentiation/Curl%20(Real%20Vector%20Fields).md) is zero and $U$ is [simply connected](TODO):
>>
>>$$\operatorname{curl} f(x, y, z) = \begin{bmatrix} \partial_y f_3(x,y,z) - \partial_z f_2(x,y,z) \\ \partial_z f_1(x,y,z) - \partial_x f_3(x,y,z) \\ \partial_x f_2(x,y,z) - \partial_y f_1(x,y,z)\end{bmatrix} = \begin{bmatrix} 1 - 1 \\ 0 - 0 \\ \mathrm{e}^x - \mathrm{e}^x\end{bmatrix} = \boldsymbol{0}$$
>>
>>We set $\partial_1 F = f_1$ and [antidifferentiate](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Partial%20Antidifferentiability%20(Real%20Scalar%20Fields).md) w.r.t. $x$:
>>
>>$$\begin{aligned}F(x, y, z) & = \int f_1(x, y, z) \, \mathrm{d}x \\ & = \int \mathrm{e}^x y + 1 \, \mathrm{d}x \\ & = \mathrm{e}^x y + x + C_1(y, z)\end{aligned}$$
>>
>>We set $\partial_2 F = f_2$:
>>
>>$$\partial_{y} F(x,y,z) = \partial_y (\mathrm{e}^x y + x + C_1(y, z)) = \mathrm{e}^x + \partial_y C_1(y, z) = \mathrm{e}^x + z$$
>>
>>From this, we get
>>
>>$$\partial_y C_1(y,z) = z$$
>>
>>and by [antidifferentiating](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Partial%20Antidifferentiability%20(Real%20Scalar%20Fields).md) w.r.t. $y$, we get:
>>
>>$$C_1(y,z) = yz + C_2(z)$$
>>
>>Therefore:
>>
>>$$F(x,y,z) = \mathrm{e}^x y + x + yz + C_2(z)$$
>>
>>We set $\partial_3 F = f_3$:
>>
>>$$\partial_{z} F(x,y,z) = \partial_z (\mathrm{e}^x y + x + yz + C_2(z)) = y + \partial_z C_2(z) = y$$
>>
>>From this, we get
>>
>>$$\partial_z C_2(z) = 0$$
>>
>>and by [antidifferentiating](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Partial%20Antidifferentiability%20(Real%20Scalar%20Fields).md) w.r.t. $z$, we get:
>>
>>$$C_2(z) = C_3 \in \mathbb{R}$$
>>
>>Therefore:
>>
>>$$F(x,y,z) = \mathrm{e}^x y + x + yz + C_3, \qquad C_3 \in \mathbb{R}$$
>>
>
>>[!WARNING]
>>
>>We must ensure that $f$ is [conservative](./Conservative%20Vector%20Fields.md) before starting the algorithm. Otherwise, the outcome can be unpredictable: we might reach a contradiction and no longer be able to proceed or we might get a result but it won't be a [potential function](./Conservative%20Vector%20Fields.md).
>>
>

>[!THEOREM] The Gradient Theorem (Fundamental Theorem of Calculus for Line Integrals I)
>
>Let $U \subseteq \mathbb{R}^n$ be [open](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets), let $f: U \to \mathbb{R}^n$ be a [real vector field](./Real%20Vector%20Fields.md) and let $\gamma: [a,b] \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [continuous](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Continuity%20(Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable).md) [parametric curve](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) with $\gamma([a,b]) \subseteq U$ which is [differentiable](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) on $(a,b)$.
>
>If $f$ is [conservative](./Conservative%20Vector%20Fields.md) and its [line integral](./Integration/Line%20Integrals%20(Real%20Vector%20Fields).md) over $\gamma$ exists, then this [integral](./Integration/Line%20Integrals%20(Real%20Vector%20Fields).md) is given by
>
>$$\int_{\gamma} f \cdot \mathrm{d}\boldsymbol{r} = F(\gamma(b)) - F(\gamma(a)),$$
>
>where $F$ is any [potential function](./Conservative%20Vector%20Fields.md) of $f$ (meaning $\nabla F = f$).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Fundamental Theorem of Calculus for Line Integrals II
>
>Let $U \subseteq \mathbb{R}^n$ be [open](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) and [path-connected](TODO), let $f: U \to \mathbb{R}^n$ be a [real vector field](./Real%20Vector%20Fields.md) and let $\boldsymbol{p} \in U$.
>
>If $f$ is [continuous](../Real%20Vector%20Functions/Continuity%20(Real%20Vector%20Functions).md) and [conservative](./Conservative%20Vector%20Fields.md), then the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $F: U \to \mathbb{R}$ defined by the [line integral](./Integration/Line%20Integrals%20(Real%20Vector%20Fields).md)
>
>$$F(\boldsymbol{x}) = \int_{\gamma_{\boldsymbol{x}}} f \cdot \mathrm{d}\boldsymbol{r},$$
>
>where $\gamma_{\boldsymbol{x}}: [a,b] \to U$ is any [piecewise continuously differentiable](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) [parametric curve](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) with $\gamma_{\boldsymbol{x}}(a) = \boldsymbol{p}$ and $\gamma_{\boldsymbol{x}}(b) = \boldsymbol{x}$, is a [potential function](./Conservative%20Vector%20Fields.md) of $f$ (meaning $\nabla F = f$).
>
>>[!EXAMPLE]-
>>
>>Let $U = \mathbb{R}^2$ and consider the [real vector field](./Real%20Vector%20Fields.md) $f: U \to \mathbb{R}^2$ defined as follows:
>>
>>$$f(x, y) = \begin{bmatrix}y + 1 \\ x + 4y\end{bmatrix}$$
>>
>>We see that $f$ is [continuously differentiable](../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) on $U$ with the following [Jacobian matrix](../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md):
>>
>>$$J_f(x,y) = \begin{bmatrix}0 & 1 \\ 1 & 4\end{bmatrix}$$
>>
>>Since $U$ is [simply connected](TODO) and since $J_f(x,y)$ is [symmetric](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md), we know that $f$ is [conservative](./Conservative%20Vector%20Fields.md).
>>
>>Let $\boldsymbol{p} = \begin{bmatrix} 0 & 0 \end{bmatrix}^{\mathsf{T}}$. Define the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $F: U \to \mathbb{R}$ via the [line integral](./Integration/Line%20Integrals%20(Real%20Vector%20Fields).md)
>>
>>$$F(x,y) = \int_{\gamma_{(x,y)}} f \cdot \mathrm{d}\boldsymbol{r},$$
>>
>>where $\gamma_{(x,y)}: [0,1] \to \mathbb{R}^2$ is the [parametric curve](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) defined as follows:
>>
>>$$\gamma_{(x,y)}(t) = \begin{bmatrix}t x \\ t y\end{bmatrix}$$
>>
>>We see that $\gamma_{(x,y)}(0) = \begin{bmatrix} 0 & 0\end{bmatrix}^{\mathsf{T}} = \boldsymbol{p}$ and $\gamma_{(x,y)}(1) = \begin{bmatrix}x & y\end{bmatrix}^{\mathsf{T}}$. Since $\gamma$ is also [continuously differentiable](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md), we know that $F(x,y)$ is a [potential function](./Conservative%20Vector%20Fields.md) of $f$. We can also find it explicitly:
>>
>>$$\begin{aligned}F(x,y) & = \int_{\gamma_{(x,y)}} f \cdot \mathrm{d}\boldsymbol{r} \\ & = \int_0^1 f(\gamma_{(x,y)}(t)) \cdot \gamma_{(x,y)}'(t) \,\mathrm{d}t \\ & = \int_0^1 \begin{bmatrix}ty + 1 \\ tx + 4ty\end{bmatrix} \cdot \begin{bmatrix}x \\ y\end{bmatrix} \,\mathrm{d}t \\ & = \int_0^1 (ty + 1)x + (tx + 4ty)y \,\mathrm{d}t \\ & = \int_0^1 tyx + x + txy + 4ty^2 \,\mathrm{d}t \\ & = \int_0^1 t(2yx + 4y^2) + x \,\mathrm{d}t \\ & = \left.\left( \frac{t^2}{2}(2xy + 4y^2) + tx \right)\right\vert_0^1 \\ & = \frac{1}{2}(2xy + 4y^2) + x \\ & = xy + 2y^2 + x\end{aligned}$$
>>
>>To verify, let's find the [gradient](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Gradient%20(Real%20Scalar%20Fields).md) of $F$:
>>
>>$$\nabla F(x,y) = \begin{bmatrix}y + 1 \\ x + 4y\end{bmatrix} = f(x,y)$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Path Independence of Line Integrals of Conservative Vector Fields
>
>Let $U \subseteq \mathbb{R}^n$ be [open](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) and [path-connected](TODO).
>
>A [continuous](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Continuity%20(Real%20Scalar%20Fields).md) [real vector field](./Real%20Vector%20Fields.md) $f: U \subseteq \mathbb{R}^n \to \mathbb{R}^n$ is [conservative](./Conservative%20Vector%20Fields.md) if and only if the [line integrals](./Integration/Line%20Integrals%20(Real%20Vector%20Fields).md) of $f$ over all [piecewise continuously differentiable](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) [parametric curves](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\gamma: [a,b] \subset \mathbb{R} \to U$ and $\varphi: [c,d] \subset \mathbb{R} \to U$ with $\gamma(a) = \varphi(c)$ and $\gamma(b) = \varphi(d)$ are equal:
>
>$$\int_{\gamma} f \cdot \mathrm{d}\boldsymbol{r} = \int_{\varphi} f \cdot \mathrm{d}\boldsymbol{r}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Line Integrals of Conservative Vector Fields over Closed Curves
>
>Let $U \subseteq \mathbb{R}^n$ be [open](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) and [path-connected](TODO).
>
>A [continuous](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Continuity%20(Real%20Scalar%20Fields).md) [real vector field](./Real%20Vector%20Fields.md) $f: U \subseteq \mathbb{R}^n \to \mathbb{R}^n$ is [conservative](./Conservative%20Vector%20Fields.md) if and only if the [line integrals](./Integration/Line%20Integrals%20(Real%20Vector%20Fields).md) of $f$ over all [piecewise continuously differentiable](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) [closed](TODO) [parametric curves](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\gamma: [a,b] \subset \mathbb{R} \to U$ are zero:
>
>$$\oint_{\gamma} f \cdot \mathrm{d}\boldsymbol{r} = 0$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Gradient Field via Jacobian Matrix
>
>Let $U \subseteq \mathbb{R}^n$ be [open](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) and [simply connected](TODO).
>
>A [continuously differentiable](../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) [real vector field](./Real%20Vector%20Fields.md) $f: U \to \mathbb{R}^n$ is [conservative](./Conservative%20Vector%20Fields.md) if and only if its [Jacobian matrix](../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md) is [symmetric](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md) everywhere:
>
>$$J_f(\boldsymbol{x}) = J_f(\boldsymbol{x})^{\mathsf{T}} \qquad \forall \boldsymbol{x} \in U$$
>
>>[!EXAMPLE]-
>>
>>Let $U = \mathbb{R}^2 \setminus \{\boldsymbol{0}\}$ and consider the [real vector field](./Real%20Vector%20Fields.md) $f: U \to \mathbb{R}^2$ defined as follows:
>>
>>$$f(x, y) = \frac{1}{x^2 + y^2}\begin{bmatrix} -y \\ x \end{bmatrix}$$
>>
>>It is [totally differentiable](../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) on $U$ with the following [Jacobian matrix](../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md):
>>
>>$$J_f(x, y) = \frac{1}{(x^2 + y^2)^2}\begin{bmatrix}2xy & y^2 - x^2 \\ y^2 - x^2 & -2xy\end{bmatrix}$$
>>
>>It is obvious that $J_f(x,y)$ is [symmetric](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md) for all $(x,y) \in U$. However, $f$ is *not* [conservative](./Conservative%20Vector%20Fields.md).
>>
>>Consider the [closed](TODO) [parametric curve](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\gamma: [0, 2\uppi] \to \mathbb{R}^2$ defined as follows:
>>
>>$$\gamma(t) = \begin{bmatrix} \cos t \\ \sin t \end{bmatrix}$$
>>
>>The [line integral](./Integration/Line%20Integrals%20(Real%20Vector%20Fields).md) of $f$ over $\gamma$ is the following:
>>
>>$$\begin{aligned}\oint_{\gamma} f \cdot \mathrm{d}\boldsymbol{r} & = \int_{0}^{2\uppi} f(\gamma(t)) \cdot \gamma'(t) \,\mathrm{d}t \\ & = \int_{0}^{2\uppi} \begin{bmatrix} -\sin t \\ \cos t \end{bmatrix} \cdot \begin{bmatrix} -\sin t \\ \cos t \end{bmatrix} \,\mathrm{d}t \\ & = \int_{0}^{2\uppi} (\sin^2 t + \cos^2 t) \,\mathrm{d}t \\ & = \int_{0}^{2\uppi} 1 \,\mathrm{d}t \\ & = 2\uppi\end{aligned}$$
>>
>>Since this [line integral](./Integration/Line%20Integrals%20(Real%20Vector%20Fields).md) is not zero, $f$ cannot be [conservative](./Conservative%20Vector%20Fields.md). 
>>
>>The reason that the [Jacobian matrix](../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md) misled us is that $U$ is not [simply connected](TODO) and so the theorem cannot be applied.
>>
>
>>[!EXAMPLE]-
>>
>>Let $U = \mathbb{R}^2 \setminus \{\boldsymbol{0}\}$ and consider the [real vector field](./Real%20Vector%20Fields.md) $f: U \to \mathbb{R}^2$ defined as follows:
>>
>>$$f(x, y) = \frac{1}{x^2 + y^2}\begin{bmatrix} -y \\ x \end{bmatrix}$$
>>
>>It is [totally differentiable](../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) on $U$ with the following [Jacobian matrix](../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md):
>>
>>$$J_f(x, y) = \frac{1}{(x^2 + y^2)^2}\begin{bmatrix}2xy & y^2 - x^2 \\ y^2 - x^2 & -2xy\end{bmatrix}$$
>>
>>It is obvious that $J_f(x,y)$ is [symmetric](../../../Algebra/Matrices/Real%20Matrices/Real%20Symmetric%20Matrices.md) for all $(x,y) \in U$.
>>
>>Consider the [closed](TODO) [parametric curve](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\gamma: [0, 2\uppi] \to \mathbb{R}^2$ defined as follows:
>>
>>$$\gamma(t) = \begin{bmatrix} 3 + \cos t \\ 4 + \sin t \end{bmatrix}$$
>>
>>While $U$ itself is *not* [simply connected](TODO), $\gamma([0, 2\uppi])$ is [contained](../../../Set%20Theory/Subsets.md) in the [simply connected](TODO) [open ball](../Euclidean%20Space/Euclidean%20Space.md) $B_2(\begin{bmatrix}3, 4\end{bmatrix}^{\mathsf{T}})$. Therefore, the [restriction](../../Functions/Functions.md) of $f$ on $B_2(\begin{bmatrix}3, 4\end{bmatrix}^{\mathsf{T}})$ *is* [conservative](./Conservative%20Vector%20Fields.md) and we have the [line integral](./Integration/Line%20Integrals%20(Real%20Vector%20Fields).md) of $f$ over $\gamma$ must be zero.
>>
>>$$\oint_{\gamma} f \cdot \mathrm{d}\boldsymbol{r} = 0$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Gradient Field via Curl
>
>Let $U \subseteq \mathbb{R}^3$ be [open](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) and [simply connected](TODO).
>
>A [continuously differentiable](../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) [real vector field](./Real%20Vector%20Fields.md) $f: U \to \mathbb{R}^3$ is [conservative](./Conservative%20Vector%20Fields.md) if and only if its [curl](./Differentiation/Curl%20(Real%20Vector%20Fields).md) is zero everywhere:
>
>$$\operatorname{curl} f(\boldsymbol{x}) = \boldsymbol{0} \qquad \forall \boldsymbol{x} \in U$$
>
>>[!PROOF]-
>>
>>TODO
>>
>