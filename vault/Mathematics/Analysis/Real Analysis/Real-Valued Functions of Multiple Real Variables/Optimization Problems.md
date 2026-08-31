---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Optimization Problems

We are often interested in finding [extrema](./Extrema%20(Real%20Scalar%20Fields).md) of a [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) under specific conditions.

Imagine we are tasked with the construction of a box with a lid which should be able to fit exactly $1$ cubic meter of stuff. We want to minimize the cost and thus the amount of material used for the box. In other words, we want to find the dimensions of the box which require the least material. Suppose the amount of material is given by

$$f(x, y, z) = \underset{\text{front and back}}{2xy} + \underset{\text{sides}}{2yz} + \underset{\text{bottom and lid}}{2xz}.$$

We see that $f$ has no [extrema](./Extrema%20(Real%20Scalar%20Fields).md) on its own. However, we also have another condition: the box should have a volume of $1$ cubic meter. This gives us a constraint for the dimensions $x, y, z$:

$$xyz = 1$$

We are now looking for the dimensions $x, y, z$ with $xyz = 1$ for which $f(x, y, z)$ is minimal. Mathematically, we are no longer searching for the [extrema](./Extrema%20(Real%20Scalar%20Fields).md) of $f$ but rather of $f$'s [restriction](../../Functions/Functions.md) on $\Omega = \{(x, y, z) \in \mathbb{R}_{\gt 0}^3 \mid xyz = 1\}$. It turns out that $f\vert_{\Omega}$ *does* have [extrema](./Extrema%20(Real%20Scalar%20Fields).md).

>[!DEFINITION] Definition: Optimization Problem
>
>An **optimization problem** $(f, \Omega_{\text{ad}})$ consists of an **objective function** which is a [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ and a [set](../../../Set%20Theory/Sets.md) $\Omega_{\text{ad}} \subseteq \mathcal{D}$ of **admissible values**.
>
>>[!DEFINITION] Definition: Equality Constraint
>>
>>An **equality constraint** is a [real vector function](../Real%20Vector%20Functions/Real%20Vector%20Functions.md) $g: \mathcal{D}_g \subseteq \mathbb{R}^n \to \mathbb{R}^m$ such that $g(\boldsymbol{p}) = 0$ for all $\boldsymbol{p} \in \Omega_{\text{ad}}$.
>>
>>>[!EXAMPLE]- Example: $f(x, y) = x^2 + y^2$ with $-x^2 + y = -3$
>>>
>>>Consider the [optimization problem](./Optimization%20Problems.md) $(f, \Omega_{\text{ad}})$ consisting of the [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^2 \to \mathbb{R}$ defined as
>>>
>>>$$f(x, y) = x^2 + y^2$$
>>>
>>>and the following [admissible values](./Optimization%20Problems.md):
>>>
>>>$$\Omega_{\text{ad}} = \{ (x, y) \in \mathbb{R}^2 \mid -x^2 + y = -3\}$$
>>>
>>>The [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $g: \mathbb{R}^2 \to \mathbb{R}$ defined as
>>>
>>>$$g(x, y) = -x^2 + y + 3$$
>>>
>>>is an [equality constraint](./Optimization%20Problems.md).
>>>
>>>In fact, we could have written $\Omega_{\text{ad}}$ as follows:
>>>
>>>$$\Omega_{\text{ad}} = \{ (x, y) \in \mathbb{R}^2 \mid g(x, y) = 0 \}$$
>>>
>>
>
>>[!DEFINITION] Definition: Local Solution
>>
>>We say that $\boldsymbol{p} \in \Omega_{\text{ad}}$ is a **local solution** of $(f, \Omega_{\text{ad}})$ if the [restriction](../../Functions/Functions.md) $f\vert_{\Omega_{\text{ad}}}$ has a [local extremum](./Extrema%20(Real%20Scalar%20Fields).md#Local%20Extrema) at $\boldsymbol{p}$.
>>
>
>>[!DEFINITION] Definition: Global Solution
>>
>>We say that $\boldsymbol{p} \in \Omega_{\text{ad}}$ is a **global solution** of $(f, \Omega_{\text{ad}})$ if the [restriction](../../Functions/Functions.md) $f\vert_{\Omega_{\text{ad}}}$ has a [global extremum](./Extrema%20(Real%20Scalar%20Fields).md#Local%20Extrema) at $\boldsymbol{p}$.
>>
>

In the vast majority of cases, we are interested in only one type of [local extrema](./Extrema%20(Real%20Scalar%20Fields).md#Local%20Extrema): either [local minima](./Extrema%20(Real%20Scalar%20Fields).md#Local%20Extrema) or [local maxima](./Extrema%20(Real%20Scalar%20Fields).md#Local%20Extrema).

>[!EXAMPLE]- Example: $f(x, y) = x^2 + y^2$ with $-x^2 + y + 3 = 0$
>
>Consider the [optimization problem](./Optimization%20Problems.md) $(f, \Omega_{\text{ad}})$ consisting of the [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^2 \to \mathbb{R}$ defined as
>
>$$f(x, y) = x^2 + y^2$$
>
>and the following [admissible values](./Optimization%20Problems.md):
>
>$$\Omega_{\text{ad}} = \{ (x, y) \in \mathbb{R}^2 \mid -x^2 + y + 3 = 0\}$$
>
>We have $(x, y) \in \Omega_{\text{ad}}$ if and only if $y = x^2 - 3$. Therefore:
>
>$$f|_{\Omega_{\text{ad}}}(x, y) = x^2 + (x^2 - 3)^2$$
>
>Let $\tilde{f}: \mathbb{R} \to \mathbb{R}$ be the [real function](../Real%20Functions/Real%20Functions.md) defined as follows:
>
>$$\tilde{f}(x) = x^2 + (x^2 - 3)^2$$
>
>We see that $f|_{\Omega_{\text{ad}}}$ has a [local extremum](./Extrema%20(Real%20Scalar%20Fields).md#Local%20Extrema) at $(x, y)$ if and only if $\tilde{f}$ has a [local extremum](../Real%20Functions/Extrema%20of%20Real%20Functions.md) at $x$. The [derivative](../Real%20Functions/Differentiability%20(Real%20Functions).md) of $\tilde{f}$ is the following:
>
>$$\tilde{f}'(x) = 4x^3 - 10x$$
>
>This is $0$ at the following points:
>
>$$x_1 = -\frac{\sqrt{10}}{2} \qquad x_2 = 0 \qquad x_3 = \frac{\sqrt{10}}{2}$$
>
>The second [derivative](../Real%20Functions/Differentiability%20(Real%20Functions).md) of $\tilde{f}$ is the following:
>
>$$\tilde{f}''(x) = 12x^2 - 10$$
>
>We have:
>
>$$\tilde{f}''(x_1) = 20 \gt 0 \qquad \tilde{f}''(x_2) = -10 \lt 0 \qquad \tilde{f}''(x_3) = 20 \gt 0$$
>
>Therefore, $\tilde{f}$ has [local minima](../Real%20Functions/Extrema%20of%20Real%20Functions.md#Local%20Extrema) at $x_1$ and $x_3$ and a [local maximum](../Real%20Functions/Extrema%20of%20Real%20Functions.md#Local%20Extrema) at $x_2$. This implies that $f|_{\Omega_{\text{ad}}}(x, y)$ has [local minima](./Extrema%20(Real%20Scalar%20Fields).md#Local%20Extrema) at $\left(-\frac{\sqrt{10}}{2}, -\frac{1}{2}\right)$ and $\left(\frac{\sqrt{10}}{2}, -\frac{1}{2}\right)$ and a [local maximum](./Extrema%20(Real%20Scalar%20Fields).md#Local%20Extrema) at $(0, -3)$.
>
>If we are interested at the [local minima](./Extrema%20(Real%20Scalar%20Fields).md#Local%20Extrema), then we would say that $\left(-\frac{\sqrt{10}}{2}, -\frac{1}{2}\right)$ and $\left(\frac{\sqrt{10}}{2}, -\frac{1}{2}\right)$ are the solutions and if we are interested at the [local maxima](./Extrema%20(Real%20Scalar%20Fields).md#Local%20Extrema), then the solution would be $(0, -3)$.
>

## Lagrange Multipliers

The **method of Lagrange multipliers** allows us to find possible [local solutions](./Optimization%20Problems.md) to an [optimization problem](./Optimization%20Problems.md) specified by an [equality constraint](./Optimization%20Problems.md).

>[!DEFINITION] Definition: Lagrangian Function
>
>Let $(f, \Omega_{\text{ad}})$ be an [optimization problem](./Optimization%20Problems.md), where $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ is a [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and $\Omega_{\text{ad}}$ can be specified via an [equality constraint](./Optimization%20Problems.md) $g: \mathcal{D}_g \subseteq \mathbb{R}^n \to \mathbb{R}^m$ with $m \lt n$:
>
>$$\Omega_{\text{ad}} = \{ \boldsymbol{x} \in \mathcal{D}_f \cap \mathcal{D}_g \mid g(\boldsymbol{x}) = \boldsymbol{0} \}$$
>
>The **Lagrangian function** is the [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $\mathcal{L}: (\mathcal{D}_f \cap \mathcal{D}_g) \times \mathbb{R}^m \to \mathbb{R}$ defined as
>
>$$\mathcal{L}(\boldsymbol{x}, \boldsymbol{\lambda}) = f(\boldsymbol{x}) + \boldsymbol{\lambda}^{\mathsf{T}} g(\boldsymbol{x})$$
>
>for all $\boldsymbol{x} \in \mathcal{D}_f \cap \mathcal{D}_g$ and all $\boldsymbol{\lambda} \in \mathbb{R}^m$.
>
>>[!NOTATION]
>>
>>If we denote $\boldsymbol{\lambda} = \begin{bmatrix}\lambda_1 & \cdots & \lambda_m\end{bmatrix}^{\mathsf{T}}$, we also write $\mathcal{L}(\boldsymbol{x}, \lambda_1, \dotsc, \lambda_m)$.
>>
>

>[!THEOREM] Theorem: First-Order Necessary Optimality Condition for Optimization Problems
>
>Let $(f, \Omega_{\text{ad}})$ be an [optimization problem](./Optimization%20Problems.md), where $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ is a [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and $\Omega_{\text{ad}}$ can be specified via an [equality constraint](./Optimization%20Problems.md) $g: \mathcal{D}_g \subseteq \mathbb{R}^n \to \mathbb{R}^m$ with $m \lt n$:
>
>$$\Omega_{\text{ad}} = \{ \boldsymbol{x} \in \mathcal{D}_f \cap \mathcal{D}_g \mid g(\boldsymbol{x}) = \boldsymbol{0} \}$$
>
>If $f\vert_{\Omega_{\text{ad}}}$ has a [local extremum](./Extrema%20(Real%20Scalar%20Fields).md#Local%20Extrema) at $\boldsymbol{p} \in \Omega_{\text{ad}}$ and $f$ and the [component functions](../Real%20Vector%20Functions/Real%20Vector%20Functions.md) $g_1, \dotsc, g_m$ are [continuously partially differentiable](./Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on an [open](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) [neighborhood](../../../Topology/Topological%20Spaces/Topological%20Space.md#Neighborhoods) of $\boldsymbol{p}$ such that the [gradients](./Differentiation/Gradient%20(Real%20Scalar%20Fields).md) $\nabla g_1 (\boldsymbol{p}), \dotsc, \nabla g_m (\boldsymbol{p})$ are [linearly independent](../../../Algebra/Vector%20Spaces/Linear%20Combinations.md#Linear%20Independence), then there exist $\tilde{\lambda}_1, \dotsc, \tilde{\lambda}_m \in \mathbb{R}$ such that
>
>$$\nabla f(\boldsymbol{p}) + \tilde{\lambda}_1 \nabla g_1 (\boldsymbol{p}) + \cdots + \tilde{\lambda}_m \nabla g_m (\boldsymbol{p}) = \boldsymbol{0}.$$
>
>Alternatively, using the [Lagrangian function](./Optimization%20Problems.md): If $f\vert_{\Omega_{\text{ad}}}$ has a [local extremum](./Extrema%20(Real%20Scalar%20Fields).md#Local%20Extrema) at $\boldsymbol{p} \in \Omega_{\text{ad}}$ and $f$ and $g$ are [continuously partially differentiable](./Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on an [open](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) [neighborhood](../../../Topology/Topological%20Spaces/Topological%20Space.md#Neighborhoods) of $\boldsymbol{p}$ such that the [Jacobian matrix](../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md) $J_g(\boldsymbol{p})$ has [rank](../../../Algebra/Matrices/Matrix%20Rank.md) $m$, then there exists some $\boldsymbol{\tilde{\lambda}} = \begin{bmatrix} \tilde{\lambda}_1, \dotsc, \tilde{\lambda}_m \end{bmatrix}^{\mathsf{T}} \in \mathbb{R}^m$ such that the [gradient](./Differentiation/Gradient%20(Real%20Scalar%20Fields).md) of the [Lagrangian function](#Lagrangian%20Multipliers) is zero at $(\boldsymbol{p}, \boldsymbol{\tilde{\lambda}})$:
>
>$$\nabla \mathcal{L} (\boldsymbol{p}, \boldsymbol{\tilde{\lambda}}) = \boldsymbol{0}$$
>
>>[!DEFINITION] Definition: Lagrange Multipliers
>>
>>We call $\tilde{\lambda}_1, \dotsc, \tilde{\lambda}_m$ **Lagrange multipliers**.
>>
>>>[!NOTATION]
>>>
>>>An alternative convention is sometimes used, where the [Lagrange multipliers](#Lagrange%20Multipliers) are defined as $-\tilde{\lambda}_1, \dotsc, -\tilde{\lambda}_m$.
>>>
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

This theorem gives us a way to find [solution](./Optimization%20Problems.md) candidates for [optimization problems](./Optimization%20Problems.md) by solving the system

$$\begin{cases} \nabla f(\boldsymbol{x}) + \lambda_1 \nabla g_1 (\boldsymbol{x}) + \cdots + \lambda_m \nabla g_m (\boldsymbol{x}) = \boldsymbol{0} \\ g_1(\boldsymbol{x}) =  0 \\ \vdots  \\  g_m(\boldsymbol{x}) = 0\end{cases}$$

for $\boldsymbol{x}$ and $\lambda_1, \dotsc, \lambda_m$.

>[!NOTATION]
>
>We can also write this system using the [Lagrangian function](#Lagrange%20Multipliers). The condition $\nabla \mathcal{L}(\boldsymbol{p})$
>
>$$\nabla \mathcal{L} (\boldsymbol{p}, \boldsymbol{\tilde{\lambda}}) = \boldsymbol{0}$$
>
>is equivalent to the following:
>
>$$\begin{cases} \partial_{x_1} \mathcal{L}(\boldsymbol{p}, \boldsymbol{\tilde{\lambda}}) & = & 0 \\ & \vdots & \\ \partial_{x_n} \mathcal{L}(\boldsymbol{p}, \boldsymbol{\tilde{\lambda}}) & = & 0 \\ \partial_{\lambda_1} \mathcal{L}(\boldsymbol{p}, \boldsymbol{\tilde{\lambda}}) & = & 0 \\ & \vdots & \\ \partial_{\lambda_m} \mathcal{L}(\boldsymbol{p}, \boldsymbol{\tilde{\lambda}}) & = & 0\end{cases}$$
>
>Therefore, the [solutions](./Optimization%20Problems.md) to the system
>
>$$\begin{cases} \partial_{x_1} \mathcal{L}(\boldsymbol{x}, \boldsymbol{\lambda}) & = & 0 \\ & \vdots & \\ \partial_{x_n} \mathcal{L}(\boldsymbol{x}, \boldsymbol{\lambda}) & = & 0 \\ \partial_{\lambda_1} \mathcal{L}(\boldsymbol{x}, \boldsymbol{\lambda}) & = & 0 \\ & \vdots & \\ \partial_{\lambda_m} \mathcal{L}(\boldsymbol{x}, \boldsymbol{\lambda}) & = & 0\end{cases}$$
>
>are candidates for [solutions](./Optimization%20Problems.md) of the [optimization problem](./Optimization%20Problems.md). Since $\mathcal{L}(\boldsymbol{x}, \boldsymbol{\lambda}) = f(\boldsymbol{x}) + \boldsymbol{\lambda}^{\mathsf{T}} g(\boldsymbol{x})$ can be expressed as
>
>$$\mathcal{L}(\boldsymbol{x}, \boldsymbol{\lambda}) = f(\boldsymbol{x}) + \lambda_1 g_1(\boldsymbol{x}) + \cdots + \lambda_m g_m(\boldsymbol{x}),$$
>
>the first $n$ equations are equivalent to the following:
>
>$$\begin{cases}\lambda_1 \nabla g_1(\boldsymbol{x}) = 0 \\  \vdots \\ \lambda_m \nabla g_m(\boldsymbol{x})  =  0\end{cases}$$
>
>This is often written as
>
>$$\nabla_{\boldsymbol{x}} \mathcal{L}(\boldsymbol{x}, \boldsymbol{\lambda}) = \boldsymbol{0}$$
>
>and we get:
>
>$$\begin{cases} \nabla_{\boldsymbol{x}} \mathcal{L}(\boldsymbol{x}, \boldsymbol{\lambda}) & = & \boldsymbol{0} \\ \partial_{\lambda_1} \mathcal{L}(\boldsymbol{x}, \boldsymbol{\lambda}) & = & 0 \\ & \vdots & \\ \partial_{\lambda_m} \mathcal{L}(\boldsymbol{x}, \boldsymbol{\lambda}) & = & 0\end{cases}$$
>

>[!EXAMPLE]- Example: $f(x, y) = x^3 y^3$ under $g(x, y) = x^2 + 2y^2 - 1 = 0$
>
>Consider the [optimization problem](./Optimization%20Problems.md) $(f, \Omega_{\text{ad}})$ consisting of the [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^2 \to \mathbb{R}$ defined as
>
>$$f(x, y) = x^3 y^3$$
>
>and the [admissible values](./Optimization%20Problems.md) due to the the [equality constraint](./Optimization%20Problems.md) $g: \mathbb{R}^2 \to \mathbb{R}$:
>
>$$g(x, y) = x^2 + 2y^2 - 1$$
>
>$$\Omega_{\text{ad}} = \{ (x, y) \in \mathbb{R}^2 \mid x^2 + 2y^2 - 1 = 0\}$$
>
>Both $f$ and $g$ are [continuously partially differentiable](./Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^2$. For the [Jacobian matrix](../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md) $J_g(x, y)$, we have:
>
>$$J_g(x, y) = \begin{bmatrix}2x & 4y\end{bmatrix}$$
>
>Its [rank](../../../Algebra/Matrices/Matrix%20Rank.md) is $0 \lt 1$ if and only if $(x,y) = (0,0)$. However, $(0,0) \notin \Omega_{\text{ad}}$, since $g(0,0) = 0^2 + 2\cdot 0^2 - 1 = -1 \ne 0$. Therefore, the [Jacobian matrix](../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md) has full [rank](../../../Algebra/Matrices/Matrix%20Rank.md) for all $(x, y) \in \Omega_{\text{ad}}$. We can thus use the theorem to find [solution](./Optimization%20Problems.md) candidates.
>
>We have [Lagrangian function](#Lagrange%20Multipliers)
>
>$$\mathcal{L}(x, y, \lambda) = f(x, y) + \lambda g(x,y) = x^3y^3 + \lambda (x^2 + 2y^2 -1)$$
>
>with the following [gradient](./Differentiation/Gradient%20(Real%20Scalar%20Fields).md):
>
>$$\nabla \mathcal{L}(x, y, \lambda) = \begin{bmatrix}3x^2y^3 + 2\lambda x \\ 3x^3y^2 + 4\lambda y \\ x^2 + 2y^2 - 1\end{bmatrix}$$
>
>Therefore, we want to solve the following system:
>
>$$\begin{cases}3x^2y^3 + 2\lambda x = 0 \\ 3x^3y^2 + 4\lambda y = 0 \\ x^2 + 2y^2 - 1 = 0\end{cases}$$
>
>We multiply the first equation by $x$, the second by $y$ and examine the difference:
>
>$$2 \lambda (x^2 - 2y^2) = 0$$
>
>We thus have $\lambda = 0$ or $x = -\sqrt{2}y$ or $x = +\sqrt{2}y$.
>
>If $\lambda = 0$, we get $3x^2y^3 = 0$ and so $x$ or $y$ must also be zero. For $x = 0$, we get the following solutions by plugging $x$ into the third equation:
>
>$$(\lambda_1, x_1, y_1) = \left(0, 0, -\frac{1}{\sqrt{2}}\right) \qquad (\lambda_2, x_2, y_2) = \left(0, 0, +\frac{1}{\sqrt{2}}\right)$$
>
>For $y = 0$, we get the following solutions by plugging $x$ into the third equation:
>
>$$(\lambda_3, x_3, y_3) = \left(0, -1, 0\right) \qquad (\lambda_4, x_4, y_4) = \left(0, 1, 0\right)$$
>
>If $\lambda \ne 0$, and $x = -\sqrt{2}y$, plugging this into the third equation gives $(-\sqrt{2}y)^2 + 2y^2 - 1 = 0 \implies 4y^2 = 1 \implies y = \pm\frac{1}{2}$.
>
>For $y = \frac{1}{2}$, we get $x = -\frac{\sqrt{2}}{2}$. We can find $\lambda$ by substituting into the first equation ($2\lambda x = -3x^2y^3 \implies \lambda = -\frac{3}{2}xy^3$):
>
>$$\lambda = -\frac{3}{2}\left(-\frac{\sqrt{2}}{2}\right)\left(\frac{1}{2}\right)^3 = \frac{3\sqrt{2}}{32}$$
>
>For $y = -\frac{1}{2}$, we get $x = \frac{\sqrt{2}}{2}$. Finding $\lambda$:
>
>$$\lambda = -\frac{3}{2}\left(\frac{\sqrt{2}}{2}\right)\left(-\frac{1}{2}\right)^3 = \frac{3\sqrt{2}}{32}$$
>
>This yields the following solutions:
>
>$$(\lambda_5, x_5, y_5) = \left(\frac{3\sqrt{2}}{32}, -\frac{\sqrt{2}}{2}, \frac{1}{2}\right) \qquad (\lambda_6, x_6, y_6) = \left(\frac{3\sqrt{2}}{32}, \frac{\sqrt{2}}{2}, -\frac{1}{2}\right)$$
>
>If $\lambda \ne 0$, and $x = +\sqrt{2}y$, plugging this into the third equation similarly gives $4y^2 = 1 \implies y = \pm\frac{1}{2}$.
>
>For $y = \frac{1}{2}$, we get $x = \frac{\sqrt{2}}{2}$. Finding $\lambda$:
>
>$$\lambda = -\frac{3}{2}\left(\frac{\sqrt{2}}{2}\right)\left(\frac{1}{2}\right)^3 = -\frac{3\sqrt{2}}{32}$$
>
>For $y = -\frac{1}{2}$, we get $x = -\frac{\sqrt{2}}{2}$. Finding $\lambda$:
>
>$$\lambda = -\frac{3}{2}\left(-\frac{\sqrt{2}}{2}\right)\left(-\frac{1}{2}\right)^3 = -\frac{3\sqrt{2}}{32}$$
>
>This yields the following solutions:
>
>$$(\lambda_7, x_7, y_7) = \left(-\frac{3\sqrt{2}}{32}, \frac{\sqrt{2}}{2}, \frac{1}{2}\right) \qquad (\lambda_8, x_8, y_8) = \left(-\frac{3\sqrt{2}}{32}, -\frac{\sqrt{2}}{2}, -\frac{1}{2}\right)$$
>
>Our candidates are thus the following:
>
>$$\begin{aligned}(x_1, y_1) &= \left(0, -\frac{1}{\sqrt{2}}\right) & (x_2, y_2) & = \left(0, \frac{1}{\sqrt{2}}\right) \\(x_3, y_3) & = \left(-1, 0\right) & (x_4, y_4) &= \left(1, 0\right) \\ (x_5, y_5) & = \left(-\frac{\sqrt{2}}{2}, \frac{1}{2}\right) & (x_6, y_6) &= \left(\frac{\sqrt{2}}{2}, -\frac{1}{2}\right) \\ (x_7, y_7) &= \left(\frac{\sqrt{2}}{2}, \frac{1}{2}\right) & (x_8, y_8) &= \left(-\frac{\sqrt{2}}{2}, -\frac{1}{2}\right)\end{aligned}$$
>
>However, these are not guaranteed to be [solutions](./Optimization%20Problems.md) to the [optimization problem](./Optimization%20Problems.md) without further investigation.
>

>[!EXAMPLE]- Example: $f(x, y, z) = x^2$ under $g_1(x, y, z) = x^2 + y^2 + z^2 - 1 = 0$ and $g_2 (x, y, z) = x - z = 0$
>
>Consider the [optimization problem](./Optimization%20Problems.md) $(f, \Omega_{\text{ad}})$ consisting of the [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^3 \to \mathbb{R}$ defined as
>
>$$f(x, y, z) = x^2$$
>
>and the [admissible values](./Optimization%20Problems.md) due to the the [equality constraints](./Optimization%20Problems.md) $g_1: \mathbb{R}^3 \to \mathbb{R}$ and $g_2: \mathbb{R}^3 \to \mathbb{R}$:
>
>$$g_1(x, y, z) = x^2 + y^2 + z^2 - 1 \qquad g_2(x, y, z) = x - z$$
>
>$$\Omega_{\text{ad}} = \{ (x, y, z) \in \mathbb{R}^3 \mid g_1(x, y, z) = g_2(x, y, z) = 0\}$$
>
>Both $f$, $g_1$, and $g_2$ are [continuously partially differentiable](./Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^3$. For the [Jacobian matrix](../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md) $J_g(x, y, z)$ where $g = (g_1, g_2)$, we have:
>
>$$J_g(x, y, z) = \begin{bmatrix}2x & 2y & 2z \\ 1 & 0 & -1\end{bmatrix}$$
>
>The rank of $J_g(x, y, z)$ is strictly less than 2 if and only if its rows are linearly dependent, which occurs when $y = 0$ and $x = -z$. We must check if any such points exist in $\Omega_{\text{ad}}$. If $x = -z$, the second constraint $g_2(x, y, z) = x - z = 0$ forces $x = 0$ and $z = 0$. Plugging $(0, 0, 0)$ into the first constraint yields $g_1(0,0,0) = -1 \ne 0$. Therefore, no point where the rank drops exists in $\Omega_{\text{ad}}$, meaning the Jacobian matrix has full rank for all $(x, y, z) \in \Omega_{\text{ad}}$. We can thus use the theorem to find solution candidates.
>
>We have [Lagrangian function](#Lagrange%20Multipliers)
>
>$$\mathcal{L}(x, y, z, \lambda_1, \lambda_2) = f(x, y, z) + \lambda_1 g_1(x,y,z) + \lambda_2 g_2(x,y,z) = x^2 + \lambda_1 (x^2 + y^2 + z^2 -1) + \lambda_2 (x - z)$$
>
>with the following [gradient](./Differentiation/Gradient%20(Real%20Scalar%20Fields).md):
>
>$$\nabla \mathcal{L}(x, y, z, \lambda_1, \lambda_2) = \begin{bmatrix}2x + 2\lambda_1 x + \lambda_2 \\ 2\lambda_1 y \\ 2\lambda_1 z - \lambda_2 \\ x^2 + y^2 + z^2 - 1 \\ x - z\end{bmatrix}$$
>
>Therefore, we want to solve the following system:
>
>$$\begin{cases}2x + 2\lambda_1 x + \lambda_2 = 0 \\ 2\lambda_1 y = 0 \\ 2\lambda_1 z - \lambda_2 = 0 \\ x^2 + y^2 + z^2 - 1 = 0 \\ x - z = 0\end{cases}$$
>
>From the second equation, we have $\lambda_1 = 0$ or $y = 0$.
>
>If $\lambda_1 = 0$, we get $-\lambda_2 = 0 \implies \lambda_2 = 0$ from the third equation. Substituting these into the first equation yields $2x = 0 \implies x = 0$. From the fifth equation, we get $x - z = 0 \implies z = 0$. For $x = 0$ and $z = 0$, we get the following solutions by plugging into the fourth equation ($0^2 + y^2 + 0^2 - 1 = 0 \implies y = \pm 1$):
>
>$$(\lambda_{1,1}, \lambda_{2,1}, x_1, y_1, z_1) = \left(0, 0, 0, -1, 0\right) \qquad (\lambda_{1,2}, \lambda_{2,2}, x_2, y_2, z_2) = \left(0, 0, 0, 1, 0\right)$$
>
>If $y = 0$, we get $x - z = 0 \implies z = x$ from the fifth equation. Plugging $y=0$ and $z=x$ into the fourth equation gives $x^2 + 0^2 + x^2 - 1 = 0 \implies 2x^2 = 1 \implies x = \pm\frac{1}{\sqrt{2}}$. Since $z = x$, this means $z = \pm\frac{1}{\sqrt{2}}$ as well.
>
>Adding the first and third equations gives $2x + 2\lambda_1(x+z) = 0$. Substituting $z=x$ yields $2x + 4\lambda_1 x = 0 \implies 2x(1 + 2\lambda_1) = 0$. Since $x \ne 0$, we have $1 + 2\lambda_1 = 0 \implies \lambda_1 = -\frac{1}{2}$.
>
>For $x = \frac{1}{\sqrt{2}}$ and $z = \frac{1}{\sqrt{2}}$, we find $\lambda_2$ by substituting into the third equation ($\lambda_2 = 2\lambda_1 z$):
>
>$$\lambda_2 = 2\left(-\frac{1}{2}\right)\left(\frac{1}{\sqrt{2}}\right) = -\frac{1}{\sqrt{2}}$$
>
>For $x = -\frac{1}{\sqrt{2}}$ and $z = -\frac{1}{\sqrt{2}}$, finding $\lambda_2$:
>
>$$\lambda_2 = 2\left(-\frac{1}{2}\right)\left(-\frac{1}{\sqrt{2}}\right) = \frac{1}{\sqrt{2}}$$
>
>This yields the following solutions:
>
>$$(\lambda_{1,3}, \lambda_{2,3}, x_3, y_3, z_3) = \left(-\frac{1}{2}, -\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0, \frac{1}{\sqrt{2}}\right) \qquad (\lambda_{1,4}, \lambda_{2,4}, x_4, y_4, z_4) = \left(-\frac{1}{2}, \frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}, 0, -\frac{1}{\sqrt{2}}\right)$$
>
>Our candidates are thus the following:
>
>$$\begin{aligned}(x_1, y_1, z_1) &= \left(0, -1, 0\right) & (x_2, y_2, z_2) & = \left(0, 1, 0\right) \\(x_3, y_3, z_3) & = \left(\frac{1}{\sqrt{2}}, 0, \frac{1}{\sqrt{2}}\right) & (x_4, y_4, z_4) &= \left(-\frac{1}{\sqrt{2}}, 0, -\frac{1}{\sqrt{2}}\right)\end{aligned}$$
>
>However, these are not guaranteed to be [solutions](./Optimization%20Problems.md) to the [optimization problem](./Optimization%20Problems.md) without further investigation.
>
