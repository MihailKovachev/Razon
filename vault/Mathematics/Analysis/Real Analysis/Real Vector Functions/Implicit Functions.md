---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Implicit Functions

>[!THEOREM] The Implicit Function Theorem
>
>Let $F: U \subseteq \mathbb{R}^m \times \mathbb{R}^n \to \mathbb{R}^n$ be a [real vector function](./Real%20Vector%20Functions.md) which is $k$-times [continuously partially differentiable](./Differentiation/Partial%20Differentiability%20(Real%20Vector%20Functions).md) ($k \ge 1$) on an [open set](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) $U$.
>
>If there exists some $\boldsymbol{p} \in U$ such that 
>
>$$F(\boldsymbol{p}) = F(p_1, \dotsc, p_{m+n}) = \boldsymbol{0}$$
>
>and the [Jacobian matrix](./Differentiation/Jacobian%20Matrix.md) $J_F(\boldsymbol{p})$ has $n$ columns $\boldsymbol{j}_{i_1}(\boldsymbol{p}), \dotsc, \boldsymbol{j}_{i_n}(\boldsymbol{p})$ (where $i_1, \dotsc, i_n$ are the corresponding indices) which are [linearly independent](../../../Algebra/Vector%20Spaces/Linear%20Combinations.md), then there exist an [open](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) [neighborhood](../../../Topology/Topological%20Spaces/Topological%20Space.md#Neighborhoods) $V \subseteq \mathbb{R}^m$ of $(p_{i_1'}, \dotsc, p_{i_m'})$ (where $i_1', \dotsc, i_m'$ are the indices of the remaining $m$ columns $\boldsymbol{j}_{i_1'}(\boldsymbol{p}), \dotsc, \boldsymbol{j}_{i_m'}(\boldsymbol{p})$), an [open](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) [neighborhood](../../../Topology/Topological%20Spaces/Topological%20Space.md#Neighborhoods) $W \subseteq \mathbb{R}^n$ of $(p_{i_1}, \dotsc, p_{i_n})$ and a unique [real vector function](./Real%20Vector%20Functions.md) $f: V \to W$ such that for all $\boldsymbol{z} \in U$ with $(z_{i_1'}, \dotsc, z_{i_m'}) \in V$ and $(z_{i_1}, \dotsc, z_{i_n}) \in W$ we have $F(\boldsymbol{z}) = \boldsymbol{0}$ if and only if $f(z_{i_1'}, \dotsc, z_{i_m'}) = (z_{i_1}, \dotsc, z_{i_n})$.
>
>In this case, $f$ is $k$-times [continuously partially differentiable](./Differentiation/Partial%20Differentiability%20(Real%20Vector%20Functions).md) on $V$ and its [Jacobian matrix](./Differentiation/Jacobian%20Matrix.md) is given as follows:
>
>$$J_f(z_{i_1'}, \dotsc, z_{i_m'}) = -\begin{bmatrix}\vert & \vert & \vert \\ \boldsymbol{j}_{i_1}(\boldsymbol{z}) & \cdots & \boldsymbol{j}_{i_n}(\boldsymbol{z}) \\ \vert & \vert & \vert\end{bmatrix}^{-1} \begin{bmatrix}\vert & \vert & \vert \\ \boldsymbol{j}_{i_1'}(\boldsymbol{z}) & \cdots & \boldsymbol{j}_{i_m'}(\boldsymbol{z}) \\ \vert & \vert & \vert\end{bmatrix}$$
>
>>[!EXAMPLE]- Example: $F(x,y) = 2x + 3y +3$
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $F: \mathbb{R}^2 \to \mathbb{R}$ defined as follows:
>>
>>$$F(x,y) = 2x + 3y +3$$
>>
>>It is infinitely [continuously partially differentiable](./Differentiation/Partial%20Differentiability%20(Real%20Vector%20Functions).md) on $\mathbb{R}^2$ with the following [Jacobian matrix](./Differentiation/Jacobian%20Matrix.md):
>>
>>$$J_F(x, y) = \begin{bmatrix}2 & 3\end{bmatrix}$$
>>
>>For $\boldsymbol{p} = (0, -1)$, we have:
>>
>>$$F(\boldsymbol{p}) = F(0, -1) = 0 \qquad J_F(\boldsymbol{p}) = \begin{bmatrix}2 & 3\end{bmatrix}$$
>>
>>>[!EXAMPLE] Example: Solving in Terms of $x$
>>>
>>>The "column" $\boldsymbol{j}_2$ of $J_F(\boldsymbol{p})$ is just $3 \ne 0$ and so the "[matrix](../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md)"
>>>
>>>$$\begin{bmatrix} \vert \\ \boldsymbol{j}_2(\boldsymbol{p}) \\ \vert \end{bmatrix} = \begin{bmatrix} 3 \end{bmatrix}$$
>>>
>>>is "[invertible](../../../Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md)".
>>>
>>>We thus know that there is an [open interval](../Euclidean%20Space/Euclidean%20Space.md) $V$ around $0$, an [open interval](../Euclidean%20Space/Euclidean%20Space.md) $W$ around $-1$ and a unique [real function](../Real%20Functions/Real%20Functions.md) $f: V \to W$ such that for all $\boldsymbol{z} = (x, y) \in V \times W$ we have $F(x, y) = 0$ if and only if $y = f(x)$.
>>>
>>>Furthermore, $f$ is infinitely [continuously differentiable](../Real%20Functions/Differentiability%20(Real%20Functions).md) on $V$ with the following [derivative](../Real%20Functions/Differentiability%20(Real%20Functions).md):
>>>
>>>$$\begin{aligned}f'(x) & = -\begin{bmatrix}\vert \\ \boldsymbol{j}_2(x,y) \\ \vert \end{bmatrix}^{-1} \begin{bmatrix}\vert \\ \boldsymbol{j}_1(x,y) \\ \vert \end{bmatrix} \\ & = -\begin{bmatrix}3\end{bmatrix}^{-1} \begin{bmatrix}2\end{bmatrix} \\ & = -\begin{bmatrix}\frac{1}{3}\end{bmatrix} \begin{bmatrix}2\end{bmatrix} \\ & = -\frac{2}{3}\end{aligned}$$
>>>
>>>We can also verify this explicitly, since $F(x, y) = 0$ if and only if $y = -\frac{2}{3}x - 1$. If we define $f: \mathbb{R} \to \mathbb{R}$ as $f(x) = -\frac{2}{3}x - 1$, we have actually found a concrete example. Specifically, $V = \mathbb{R} = W$ and we easily see that $F(x, y) = 0$ if and only if $y = f(x)$. Moreover, we have $f'(x) = -\frac{2}{3}$.
>>>
>>
>>>[!EXAMPLE] Example: Solving in Terms of $y$
>>>
>>>The "column" $\boldsymbol{j}_1$ of $J_F(\boldsymbol{p})$ is just $2 \ne 0$ and so the "[matrix](../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md)"
>>>
>>$$\begin{bmatrix} \vert \\ \boldsymbol{j}_1(\boldsymbol{p}) \\ \vert \end{bmatrix} = \begin{bmatrix} 2 \end{bmatrix}$$
>>>
>>>is "[invertible](../../../Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md)".
>>>
>>>We thus know that there is an [open interval](../Euclidean%20Space/Euclidean%20Space.md) $V$ around $-1$, an [open interval](../Euclidean%20Space/Euclidean%20Space.md) $W$ around $0$ and a unique [real function](../Real%20Functions/Real%20Functions.md) $f: V \to W$ such that for all $(y, x) \in V \times W$ we have $F(x,y) = 0$ if and only if $x = f(y)$.
>>>
>>>Furthermore, $f$ is infinitely [continuously differentiable](../Real%20Functions/Differentiability%20(Real%20Functions).md) on $V$ with the following [derivative](../Real%20Functions/Differentiability%20(Real%20Functions).md):
>>>
>>>$$\begin{aligned}f'(y) & = -\begin{bmatrix}\vert \\ \boldsymbol{j}_1(x,y) \\ \vert \end{bmatrix}^{-1} \begin{bmatrix}\vert \\ \boldsymbol{j}_2(x,y) \\ \vert \end{bmatrix} \\ & = -\begin{bmatrix}2\end{bmatrix}^{-1} \begin{bmatrix}3\end{bmatrix} \\ & = -\begin{bmatrix} \frac{1}{2} \end{bmatrix} \begin{bmatrix} 3 \end{bmatrix} \\ & = -\frac{3}{2}\end{aligned}$$
>>>
>>>We can also verify this explicitly, since $F(x, y) = 0$ if and only if $x = -\frac{3}{2}y - \frac{3}{2}$. If we define $f: \mathbb{R} \to \mathbb{R}$ as $f(y) = -\frac{3}{2}y - \frac{3}{2}$, we have actually found a concrete example. Specifically, $V = \mathbb{R} = W$ and we easily see that $F(x, y) = 0$ if and only if $x = f(y)$. Moreover, we have $f'(y) = -\frac{3}{2}$.
>>>
>>
>
>>[!EXAMPLE]- Example: $F(x, y) = \mathrm{e}^y + y^3 - x^3 - x^2 -1$
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $F: \mathbb{R}^2 \to \mathbb{R}$ defined as follows:
>>
>>$$F(x, y) = \mathrm{e}^y + y^3 - x^3 - x^2 -1$$
>>
>>It is infinitely [continuously partially differentiable](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^2$ with the following [Jacobian matrix](./Differentiation/Jacobian%20Matrix.md):
>>
>>$$J_F(x, y) = \begin{bmatrix}-3x^2 - 2x & \mathrm{e}^y + 3y^2\end{bmatrix}$$
>>
>>For $\boldsymbol{p} = (0, 0)$, we have:
>>
>>$$F(\boldsymbol{p}) = F(0, 0) = 0 \qquad J_F(\boldsymbol{p}) = \begin{bmatrix}0 & 1\end{bmatrix}$$
>>
>>>[!EXAMPLE] Example: Solving in Terms of $x$
>>>
>>>The "column" $\boldsymbol{j}_2$ of $J_F(\boldsymbol{p})$ is just $1 \ne 0$ and so the "[matrix](../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md)"
>>>
>>>$$\begin{bmatrix} \vert \\ \boldsymbol{j}_2(\boldsymbol{p}) \\ \vert \end{bmatrix} = \begin{bmatrix} 1 \end{bmatrix}$$
>>>
>>>is "[invertible](../../../Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md)".
>>>
>>>We thus know that there is an [open interval](../Euclidean%20Space/Euclidean%20Space.md) $V$ around $0$, an [open interval](../Euclidean%20Space/Euclidean%20Space.md) $W$ around $0$ and a unique [real function](../Real%20Functions/Real%20Functions.md) $f: V \to W$ such that for all $\boldsymbol{z} = (x, y) \in V \times W$ we have $F(x, y) = 0$ if and only if $y = f(x)$.
>>>
>>>Furthermore, $f$ is infinitely [continuously differentiable](../Real%20Functions/Differentiability%20(Real%20Functions).md) on $V$ with the following [derivative](../Real%20Functions/Differentiability%20(Real%20Functions).md):
>>>
>>>$$\begin{aligned}f'(x) & = -\begin{bmatrix}\vert \\ \boldsymbol{j}_2(x,y) \\ \vert \end{bmatrix}^{-1} \begin{bmatrix}\vert \\ \boldsymbol{j}_1(x,y) \\ \vert \end{bmatrix} \\ & = -\begin{bmatrix}\mathrm{e}^{f(x)} + 3 f(x)^2\end{bmatrix}^{-1} \begin{bmatrix}-3x^2 - 2x\end{bmatrix} \\ & = \frac{3x^2 + 2x}{\mathrm{e}^{f(x)} + 3 f(x)^2}\end{aligned}$$
>>> 
>>>We can also simplify this a bit to get rid of $\mathrm{e}^{f(x)}$. Since $F(x, f(x)) = 0$ for all $x \in V$, we have:
>>>
>>>$$F(x, f(x)) = \mathrm{e}^{f(x)}+f(x)^3 - x^3 - x^2 - 1 = 0$$
>>>
>>>From that, we obtain:
>>>
>>>$$\mathrm{e}^{f(x)} = -f(x)^3 + x^3 + x^2 + 1$$
>>>
>>>Plugging this into the expression for $f'(x)$, we get:
>>>
>>>$$f'(x) = \frac{3x^2 + 2x}{-f(x)^3 + 3f(x)^2 + x^3 + x^2 + 1}$$
>>>
>>
>>>[!EXAMPLE] Example: Solving in Terms of $y$
>>>
>>>The "column" $\boldsymbol{j}_1$ of $J_F(\boldsymbol{p})$ is just $0$ and so the "[matrix](../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md)"
>>>
>>>$$\begin{bmatrix} \vert \\ \boldsymbol{j}_1(\boldsymbol{p}) \\ \vert \end{bmatrix} = \begin{bmatrix} 0 \end{bmatrix}$$
>>>
>>>is *not* "[invertible](../../../Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md)". Therefore, the theorem cannot tell us anything.
>>>
>>
>
>>[!EXAMPLE]- Example: $F(x, y) = x^2 + y^2 - 1$
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $F: \mathbb{R}^2 \to \mathbb{R}$ defined as follows:
>>
>>
>>$$F(x, y) = x^2 + y^2 - 1$$
>>
>>It is infinitely [continuously partially differentiable](./Differentiation/Partial%20Differentiability%20(Real%20Vector%20Functions).md) on $\mathbb{R}^2$ with the following [Jacobian matrix](./Differentiation/Jacobian%20Matrix.md):
>>
>>$$J_F(x, y) = \begin{bmatrix}2x & 2y\end{bmatrix}$$
>>
>>>[!EXAMPLE] Example: Solving in Terms of $x$
>>>
>>>For an arbitrary point $\boldsymbol{p} = (x_0, y_0)$ such that $x_0^2 + y_0^2 - 1 = 0$ with $y_0 \ne 0$, we have:
>>>
>>>$$F(\boldsymbol{p}) = F(x_0, y_0) = 0 \qquad J_F(\boldsymbol{p}) = \begin{bmatrix}2x_0 & 2y_0\end{bmatrix}$$
>>>
>>>The "column" $\boldsymbol{j}_2(\boldsymbol{p})$ of $J_F(\boldsymbol{p})$ is just $2y_0 \ne 0$ and so the "[matrix](../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md)"
>>>
>>>$$\begin{bmatrix} \vert \\ \boldsymbol{j}_2(\boldsymbol{p}) \\ \vert \end{bmatrix} = \begin{bmatrix} 2y_0 \end{bmatrix}$$
>>>
>>>is "[invertible](../../../Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md)".
>>>
>>>We thus know that there is an [open interval](../Euclidean%20Space/Euclidean%20Space.md) $V$ around $x_0$, an [open interval](../Euclidean%20Space/Euclidean%20Space.md) $W$ around $y_0$ and a unique [real function](../Real%20Functions/Real%20Functions.md) $f: V \to W$ such that for all $\boldsymbol{z} = (x, y) \in V \times W$ we have $F(x, y) = 0$ if and only if $y = f(x)$.
>>>
>>>Furthermore, $f$ is infinitely [continuously differentiable](../Real%20Functions/Differentiability%20(Real%20Functions).md) on $V$ with the following [derivative](../Real%20Functions/Differentiability%20(Real%20Functions).md):
>>>
>>>$$\begin{aligned}f'(x) & = -\begin{bmatrix}\vert \\ \boldsymbol{j}_2(x,y) \\ \vert \end{bmatrix}^{-1} \begin{bmatrix}\vert \\ \boldsymbol{j}_1(x,y) \\ \vert \end{bmatrix} \\ & = -\begin{bmatrix}2y\end{bmatrix}^{-1} \begin{bmatrix}2x\end{bmatrix} \\ & = -\begin{bmatrix}\frac{1}{2y}\end{bmatrix} \begin{bmatrix}2x\end{bmatrix} \\ & = -\frac{x}{y}\end{aligned}$$
>>>
>>>We can also verify this explicitly. For $y_0 \gt 0$, we have $f(x) = \sqrt{1-x^2}$ and for $y_0 \lt 0$, we have $f(x) = -\sqrt{1 - x^2}$. In both cases, we easily see that $F(x, y) = 0$ if and only if $y = f(x)$. Moreover, we have $f'(x) = -\frac{x}{\pm\sqrt{1-x^2}} = -\frac{x}{f(x)}$, matching our result.
>>>
>>
>>>[!EXAMPLE] Example: Solving in Terms of $y$
>>>
>>>For an arbitrary point $\boldsymbol{p} = (x_0, y_0)$ such that $x_0^2 + y_0^2 - 1 = 0$ with $x_0 \ne 0$, we have:
>>>
>>>$$F(\boldsymbol{p}) = F(x_0, y_0) = 0 \qquad J_F(\boldsymbol{p}) = \begin{bmatrix}2x_0 & 2y_0\end{bmatrix}$$
>>>
>>>
>>>The "column" $\boldsymbol{j}_1(\boldsymbol{p})$ of $J_F(\boldsymbol{p})$ is just $2x_0 \ne 0$ and so the "[matrix](../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md)"
>>>
>>>$$\begin{bmatrix} \vert \\ \boldsymbol{j}_1(\boldsymbol{p}) \\ \vert \end{bmatrix} = \begin{bmatrix} 2x_0 \end{bmatrix}$$
>>>
>>>is "[invertible](../../../Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md)".
>>>
>>>We thus know that there is an [open interval](../Euclidean%20Space/Euclidean%20Space.md) $V$ around $y_0$, an [open interval](../Euclidean%20Space/Euclidean%20Space.md) $W$ around $x_0$ and a unique [real function](../Real%20Functions/Real%20Functions.md) $f: V \to W$ such that for all $(y, x) \in V \times W$ we have $F(x,y) = 0$ if and only if $x = f(y)$.
>>>
>>>Furthermore, $f$ is infinitely [continuously differentiable](../Real%20Functions/Differentiability%20(Real%20Functions).md) on $V$ with the following [derivative](../Real%20Functions/Differentiability%20(Real%20Functions).md):
>>>
>>>$$\begin{aligned}f'(y) & = -\begin{bmatrix}\vert \\ \boldsymbol{j}_1(x,y) \\ \vert \end{bmatrix}^{-1} \begin{bmatrix}\vert \\ \boldsymbol{j}_2(x,y) \\ \vert \end{bmatrix} \\ & = -\begin{bmatrix}2x\end{bmatrix}^{-1} \begin{bmatrix}2y\end{bmatrix} \\ & = -\begin{bmatrix} \frac{1}{2x} \end{bmatrix} \begin{bmatrix} 2y \end{bmatrix} \\ & = -\frac{y}{x}\end{aligned}$$
>>>
>>>We can also verify this explicitly. For $x_0 \gt 0$, we have $f(y) = \sqrt{1-y^2}$ and for $x_0 \lt 0$, we have $f(y) = -\sqrt{1 - y^2}$. In both cases, we easily see that $F(x, y) = 0$ if and only if $x = f(y)$. Moreover, we have $f'(y) = -\frac{y}{\pm\sqrt{1-y^2}} = -\frac{y}{f(y)}$, matching our result.
>>>
>>
>
>>[!EXAMPLE]- Example: $F(x, y, z) = \sin (x + y - z^2) - \frac{1}{\sqrt{2}}$
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $F: \mathbb{R}^3 \to \mathbb{R}$ defined as follows:
>>
>>$$F(x, y, z) = \sin (x + y - z^2) - \frac{1}{\sqrt{2}}$$
>>
>>It is infinitely [continuously partially differentiable](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^3$ with the following [Jacobian matrix](./Differentiation/Jacobian%20Matrix.md):
>>
>>$$J_F(x, y, z) = \begin{bmatrix}\cos(x + y - z^2) & \cos(x + y - z^2) & -2z\cos(x + y - z^2)\end{bmatrix}$$
>>
>>For $\boldsymbol{p} = \left(\frac{\uppi}{4}, 0, 0\right)$, we have:
>>
>>$$F(\boldsymbol{p}) = F\left(\frac{\uppi}{4}, 0, 0\right) = 0 \qquad J_F(\boldsymbol{p}) = \begin{bmatrix}\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0\end{bmatrix}$$
>>
>>>[!EXAMPLE] Example: Solving in Terms of $y$ and $z$
>>>
>>>The "column" $\boldsymbol{j}_1(\boldsymbol{p})$ of $J_F(\boldsymbol{p})$ is just $\frac{1}{\sqrt{2}} \ne 0$ and so the "[matrix](../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md)"
>>>
>>>$$\begin{bmatrix} \vert \\ \boldsymbol{j}_1(\boldsymbol{p}) \\ \vert \end{bmatrix} = \begin{bmatrix} \frac{1}{\sqrt{2}} \end{bmatrix}$$
>>>
>>>is "[invertible](../../../Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md)".
>>>
>>>We thus know that there is an [open set](../Euclidean%20Space/Euclidean%20Space.md) $V$ around $(0, 0)$, an [open interval](../Euclidean%20Space/Euclidean%20Space.md) $W$ around $\frac{\uppi}{4}$ and a unique [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: V \to W$ such that for all $\boldsymbol{z} = (y, z, x) \in V \times W$ we have $F(x, y, z) = 0$ if and only if $x = f(y, z)$.
>>>
>>>Furthermore, $f$ is infinitely [continuously partially differentiable](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on $V$ with the following [Jacobian matrix](./Differentiation/Jacobian%20Matrix.md):
>>>
>>>$$\begin{aligned}J_f(y, z) & = -\begin{bmatrix}\vert \\ \boldsymbol{j}_1(x,y,z) \\ \vert \end{bmatrix}^{-1} \begin{bmatrix}\vert & \vert \\ \boldsymbol{j}_2(x,y,z) & \boldsymbol{j}_3(x,y,z) \\ \vert & \vert \end{bmatrix} \\ & = -\begin{bmatrix}\frac{1}{\sqrt{2}}\end{bmatrix}^{-1} \begin{bmatrix}\frac{1}{\sqrt{2}} & 0\end{bmatrix} \\ & = -\begin{bmatrix}\sqrt{2}\end{bmatrix} \begin{bmatrix}\frac{1}{\sqrt{2}} & 0\end{bmatrix} \\ & = \begin{bmatrix}-1 & 0\end{bmatrix}\end{aligned}$$
>>>
>>>We can also verify this explicitly, since $F(x, y, z) = 0$ locally if and only if $x = -y + z^2 + \frac{\uppi}{4}$. If we define $f: \mathbb{R}^2 \to \mathbb{R}$ as $f(y, z) = -y + z^2 + \frac{\uppi}{4}$, we have actually found a concrete example. Specifically, $V = \mathbb{R}^2$ and $W = \mathbb{R}$, and we easily see that $F(x, y, z) = 0$ if and only if $x = f(y, z)$. Moreover, we have $J_f(y, z) = \begin{bmatrix}-1 & 2z\end{bmatrix}$, which at $(0, 0)$ gives $\begin{bmatrix}-1 & 0\end{bmatrix}$.
>>>
>>
>>>[!EXAMPLE] Example: Solving in Terms of $x$ and $z$
>>>
>>>The "column" $\boldsymbol{j}_2(\boldsymbol{p})$ of $J_F(\boldsymbol{p})$ is just $\frac{1}{\sqrt{2}} \ne 0$ and so the "[matrix](../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md)"
>>>
>>>$$\begin{bmatrix} \vert \\ \boldsymbol{j}_2(\boldsymbol{p}) \\ \vert \end{bmatrix} = \begin{bmatrix} \frac{1}{\sqrt{2}} \end{bmatrix}$$
>>>
>>>is "[invertible](../../../Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md)".
>>>
>>>We thus know that there is an [open set](../Euclidean%20Space/Euclidean%20Space.md) $V$ around $\left(\frac{\uppi}{4}, 0\right)$, an [open interval](../Euclidean%20Space/Euclidean%20Space.md) $W$ around $0$ and a unique [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: V \to W$ such that for all $\boldsymbol{z} = (x, z, y) \in V \times W$ we have $F(x, y, z) = 0$ if and only if $y = f(x, z)$.
>>>
>>>Furthermore, $f$ is infinitely [continuously partially differentiable](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on $V$ with the following [Jacobian matrix](./Differentiation/Jacobian%20Matrix.md):
>>>
>>>$$\begin{aligned}J_f(x, z) & = -\begin{bmatrix}\vert \\ \boldsymbol{j}_2(x,y,z) \\ \vert \end{bmatrix}^{-1} \begin{bmatrix}\vert & \vert \\ \boldsymbol{j}_1(x,y,z) & \boldsymbol{j}_3(x,y,z) \\ \vert & \vert \end{bmatrix} \\ & = -\begin{bmatrix}\frac{1}{\sqrt{2}}\end{bmatrix}^{-1} \begin{bmatrix}\frac{1}{\sqrt{2}} & 0\end{bmatrix} \\ & = -\begin{bmatrix}\sqrt{2}\end{bmatrix} \begin{bmatrix}\frac{1}{\sqrt{2}} & 0\end{bmatrix} \\ & = \begin{bmatrix}-1 & 0\end{bmatrix}\end{aligned}$$
>>>
>>>We can also verify this explicitly, since $F(x, y, z) = 0$ locally if and only if $y = -x + z^2 + \frac{\uppi}{4}$. If we define $f: \mathbb{R}^2 \to \mathbb{R}$ as $f(x, z) = -x + z^2 + \frac{\uppi}{4}$, we have actually found a concrete example. Specifically, $V = \mathbb{R}^2$ and $W = \mathbb{R}$, and we easily see that $F(x, y, z) = 0$ if and only if $y = f(x, z)$. Moreover, we have $J_f(x, z) = \begin{bmatrix}-1 & 2z\end{bmatrix}$, which at $\left(\frac{\uppi}{4}, 0\right)$ gives $\begin{bmatrix}-1 & 0\end{bmatrix}$.
>>>
>>
>>>[!EXAMPLE] Example: Solving in Terms of $x$ and $y$
>>>
>>>The "column" $\boldsymbol{j}_3(\boldsymbol{p})$ of $J_F(\boldsymbol{p})$ is $0$ and so the "[matrix](../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md)"
>>>
>>>$$\begin{bmatrix} \vert \\ \boldsymbol{j}_3(\boldsymbol{p}) \\ \vert \end{bmatrix} = \begin{bmatrix} 0 \end{bmatrix}$$
>>>
>>>is *not* "[invertible](../../../Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md)". Therefore, the theorem cannot tell us anything.
>>>
>>
>
>>[!EXAMPLE]- Example: $F: \mathbb{R}^3 \to \mathbb{R}^2$
>>
>>Consider the [real vector function](./Real%20Vector%20Functions.md) $F: \mathbb{R}^3 \to \mathbb{R}^2$ defined as follows:
>>
>>$$F(x, y, z) = \begin{bmatrix} x^2 + y^2 - z^2 - 8 \\ \sin(\uppi x) + \sin (\uppi y) + \sin (\uppi z)\end{bmatrix}$$
>>
>>It is infinitely [continuously partially differentiable](./Differentiation/Partial%20Differentiability%20(Real%20Vector%20Functions).md) on $\mathbb{R}^3$ with the following [Jacobian matrix](./Differentiation/Jacobian%20Matrix.md):
>>
>>$$J_F(x, y, z) = \begin{bmatrix}2x & 2y & -2z \\ \uppi \cos(\uppi x) & \uppi \cos(\uppi y) & \uppi \cos(\uppi z)\end{bmatrix}$$
>>
>>For $\boldsymbol{p} = (2, 2, 0)$, we have:
>>
>>$$F(\boldsymbol{p}) = F(2, 2, 0) = \boldsymbol{0} \qquad J_F(\boldsymbol{p}) = \begin{bmatrix}4 & 4 & 0 \\ \uppi & \uppi & \uppi \end{bmatrix}$$
>>
>>>[!EXAMPLE] Example: Solving in Terms of $x$
>>>
>>>The [matrix](../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) formed by columns $\boldsymbol{j}_2(\boldsymbol{p})$ and $\boldsymbol{j}_3(\boldsymbol{p})$ of $J_F(\boldsymbol{p})$ is
>>>
>>>$$\begin{bmatrix} \vert & \vert \\ \boldsymbol{j}_2(\boldsymbol{p}) & \boldsymbol{j}_3(\boldsymbol{p}) \\ \vert & \vert \end{bmatrix} = \begin{bmatrix} 4 & 0 \\ \uppi & \uppi \end{bmatrix}$$
>>>
>>>and is [invertible](../../../Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md).
>>>
>>>We thus know that there is an [open interval](../Euclidean%20Space/Euclidean%20Space.md) $V \subseteq \mathbb{R}$ around $x = 2$, an [open](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) [neighborhood](../../../Topology/Topological%20Spaces/Topological%20Space.md#Neighborhoods) $W \subseteq \mathbb{R}^2$ around $(y, z) = (2, 0)$ and a unique [function](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $f: V \to W$ such that for all $(x, y, z) \in V \times W$ we have $F(x, y, z) = \boldsymbol{0}$ if and only if $(y, z) = f(x)$.
>>>
>>>Furthermore, $f$ is infinitely [continuously differentiable](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) on $V$ with the following [derivative](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md):
>>>
>>>$$\begin{aligned}f'(x) &= -\begin{bmatrix} \vert & \vert \\ \boldsymbol{j}_2(x,y,z) & \boldsymbol{j}_3(x,y,z) \\ \vert & \vert \end{bmatrix}^{-1} \begin{bmatrix}\vert \\ \boldsymbol{j}_1(x,y,z) \\ \vert \end{bmatrix} \\ &= -\begin{bmatrix} \partial_2 F_1(x, f_1(x), f_2(x)) & \partial_3 F_1(x, f_1(x), f_2(x)) \\ \partial_2 F_2(x, f_1(x), f_2(x)) & \partial_3 F_2(x, f_1(x), f_2(x)) \end{bmatrix}^{-1} \begin{bmatrix}\partial_1 F_1(x, f_1(x), f_2(x)) \\ \partial_1 F_2 (x, f_1(x), f_2(x)) \end{bmatrix} \\ & = -\begin{bmatrix} 2f_1(x) & -2f_2(x) \\ \uppi \cos (\uppi f_1(x)) & \uppi \cos (\uppi f_2(x)) \end{bmatrix}^{-1} \begin{bmatrix}  2x \\ \uppi \cos(\uppi x) \end{bmatrix} \\ & = -\frac{1}{2 \uppi f_1(x) \cos (\uppi f_2(x)) + 2\uppi f_2(x) \cos (\uppi f_1(x))} \begin{bmatrix}\uppi \cos (\uppi f_2(x)) & 2 f_2(x) \\ -\uppi \cos(\uppi f_1(x)) & 2 f_1(x)\end{bmatrix}\begin{bmatrix}  2x \\ \uppi \cos(\uppi x) \end{bmatrix} \\ & = \frac{1}{f_1(x) \cos(\uppi f_2(x)) + f_2(x) \cos(\uppi f_1(x))} \begin{bmatrix} -x \cos(\uppi f_2(x)) - f_2(x) \cos(\uppi x) \\ x \cos(\uppi f_1(x)) - f_1(x) \cos(\uppi x) \end{bmatrix}\end{aligned}$$
>>>
>>
>>>[!EXAMPLE] Example: Solving in Terms of $y$
>>>
>>>The [matrix](../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) formed by columns $\boldsymbol{j}_1(\boldsymbol{p})$ and $\boldsymbol{j}_3(\boldsymbol{p})$ of $J_F(\boldsymbol{p})$ is
>>>
>>>$$\begin{bmatrix} \vert & \vert \\ \boldsymbol{j}_1(\boldsymbol{p}) & \boldsymbol{j}_3(\boldsymbol{p}) \\ \vert & \vert \end{bmatrix} = \begin{bmatrix} 4 & 0 \\ \uppi & \uppi \end{bmatrix}$$
>>>
>>>which is [invertible](../../../Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md).
>>>
>>>We thus know that there is an [open interval](../Euclidean%20Space/Euclidean%20Space.md) $V \subseteq \mathbb{R}$ around $y = 2$, an [open](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) [neighborhood](../../../Topology/Topological%20Spaces/Topological%20Space.md#Neighborhoods) $W \subseteq \mathbb{R}^2$ around $(x, z) = (2, 0)$ and a unique [function](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $f: V \to W$ such that for all $(y, x, z) \in V \times W$ we have $F(x, y, z) = \boldsymbol{0}$ if and only if $(x, z) = f(y)$.
>>>
>>>Furthermore, $f$ is infinitely [continuously differentiable](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) on $V$ with the following [derivative](../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md):
>>>
>>>$$\begin{aligned}f'(y) &= -\begin{bmatrix} \vert & \vert \\ \boldsymbol{j}_1(x,y,z) & \boldsymbol{j}_3(x,y,z) \\ \vert & \vert \end{bmatrix}^{-1} \begin{bmatrix}\vert \\ \boldsymbol{j}_2(x,y,z) \\ \vert \end{bmatrix} \\ &= -\begin{bmatrix} \partial_1 F_1(f_1(y), y, f_2(y)) & \partial_3 F_1(f_1(y), y, f_2(y)) \\ \partial_1 F_2(f_1(y), y, f_2(y)) & \partial_3 F_2(f_1(y), y, f_2(y)) \end{bmatrix}^{-1} \begin{bmatrix}\partial_2 F_1(f_1(y), y, f_2(y)) \\ \partial_2 F_2 (f_1(y), y, f_2(y)) \end{bmatrix} \\ & = -\begin{bmatrix} 2f_1(y) & -2f_2(y) \\ \uppi \cos (\uppi f_1(y)) & \uppi \cos (\uppi f_2(y)) \end{bmatrix}^{-1} \begin{bmatrix}  2y \\ \uppi \cos(\uppi y) \end{bmatrix} \\ & = \frac{1}{f_1(y) \cos(\uppi f_2(y)) + f_2(y) \cos(\uppi f_1(y))} \begin{bmatrix} -y \cos(\uppi f_2(y)) - f_2(y) \cos(\uppi y) \\ y \cos(\uppi f_1(y)) - f_1(y) \cos(\uppi y) \end{bmatrix}\end{aligned}$$
>>>
>>
>>>[!EXAMPLE] Example: Solving in Terms of $z$
>>>
>>>The [matrix](../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) formed by columns $\boldsymbol{j}_1(\boldsymbol{p})$ and $\boldsymbol{j}_2(\boldsymbol{p})$ of $J_F(\boldsymbol{p})$ is
>>>
>>>$$\begin{bmatrix} \vert & \vert \\ \boldsymbol{j}_1(\boldsymbol{p}) & \boldsymbol{j}_2(\boldsymbol{p}) \\ \vert & \vert \end{bmatrix} = \begin{bmatrix} 4 & 4 \\ \uppi & \uppi \end{bmatrix}$$
>>>
>>>which is *not* [invertible](../../../Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md). Therefore, the theorem cannot tell us anything.
>>>
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>