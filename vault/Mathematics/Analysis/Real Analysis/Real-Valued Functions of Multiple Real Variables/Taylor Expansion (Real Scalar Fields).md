---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Taylor Expansion (Real Scalar Fields)

>[!DEFINITION] Definition: Taylor Polynomial
>
>TODO
>

>[!THEOREM] Theorem: Taylor Polynomial via Partial Derivatives
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md).
>
>If $f$ is $m$-times [totally differentiable](./Differentiation/Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p} \in \operatorname{int} \mathcal{D}$, then its [Taylor polynomial](./Taylor%20Expansion%20(Real%20Scalar%20Fields).md) there is given by $f$'s [partial derivatives](./Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) as follows:
>
>$$T(\boldsymbol{p}; \boldsymbol{x}) = f(\boldsymbol{p}) + \sum_{k = 1}^m \frac{1}{k!}\left(\sum_{i_1 = 1}^n\cdots \sum_{i_k = 1}^n \partial_{i_1}\cdots \partial_{i_k}f(\boldsymbol{p}) \prod_{j = 1}^k (x_{i_j} - p_{i_j})\right)$$
>
>>[!TIP]
>>
>>This formula can be rewritten using $f$'s [gradient](./Differentiation/Gradient%20(Real%20Scalar%20Fields).md) and [Hessian matrix](./Differentiation/Hessian%20Matrix.md) as follows:
>>
>>$$T(\boldsymbol{p}; \boldsymbol{x}) = f(\boldsymbol{p}) + \nabla f(\boldsymbol{p})^{\mathsf{T}}(\boldsymbol{x}-\boldsymbol{p}) + \frac{1}{2} (\boldsymbol{x}-\boldsymbol{p})^{\mathsf{T}} \boldsymbol{H}_f(\boldsymbol{p})(\boldsymbol{x}-\boldsymbol{p}) + \sum_{k = 3}^m \frac{1}{k!}\left(\sum_{i_1 = 1}^n\cdots \sum_{i_k = 1}^n \partial_{i_1}\cdots \partial_{i_k}f(\boldsymbol{p}) \prod_{j = 1}^k (x_{i_j} - p_{i_j})\right)$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Lagrange Form of the Remainder
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\boldsymbol{p},\boldsymbol{x} \in \mathcal{D}$.
>
>If $f$ is $(m+1)$-times [totally differentiable](./Differentiation/Total%20Differentiability%20(Real%20Scalar%20Fields).md) on an [open set](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) which [contains](../../../Set%20Theory/Subsets.md) $L = \{\boldsymbol{p} + t(\boldsymbol{x} -\boldsymbol{p}): t \in [0,1]\}$, then there exists some $\boldsymbol{\xi} \in \operatorname{int} L$ such that the [remainder](./Taylor%20Expansion%20(Real%20Scalar%20Fields).md) $R_{m+1}(\boldsymbol{p}; \boldsymbol{x})$ of $f$'s $m$-th [Taylor polynomial](./Taylor%20Expansion%20(Real%20Scalar%20Fields).md) $T_m(\boldsymbol{p};\boldsymbol{x})$ is given by $f$'s [partial derivatives](./Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) as follows:
>
>$$R_{m+1}(\boldsymbol{p}; \boldsymbol{x}) = \frac{1}{(m+1)!} \left(\sum_{i_1 = 1}^n\cdots \sum_{i_{m+1} = 1}^n \partial_{i_1}\cdots \partial_{i_{m+1}}f(\boldsymbol{\xi}) \prod_{j = 1}^{m+1} (x_{i_j} - p_{i_j})\right),$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Integral Form of the Remainder
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\boldsymbol{p}, \boldsymbol{x} \in \mathcal{D}$.
>
>If $f$ is $(m+1)$-times [continuously partially differentiable](./Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on an [open set](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) which [contains](../../../Set%20Theory/Subsets.md) $L = \{\boldsymbol{p} + t(\boldsymbol{x} -\boldsymbol{p}): t \in [0,1]\}$, then the [remainder](./Taylor%20Expansion%20(Real%20Scalar%20Fields).md) $R_{m+1}(\boldsymbol{p}; \boldsymbol{x})$ of $f$'s $m$-th [Taylor polynomial](./Taylor%20Expansion%20(Real%20Scalar%20Fields).md) $T_m(\boldsymbol{p};\boldsymbol{x})$ is given by the following [integral](../Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md):
>
>$$R_{m+1}(\boldsymbol{p}; \boldsymbol{x}) = \frac{1}{m!}\int_0^1 (1-t)^m \left(\sum_{i_1 = 1}^n\cdots \sum_{i_{m+1} = 1}^n \partial_{x^{i_1}}\cdots \partial_{x^{i_{m+1}}}f(\boldsymbol{p} + t(\boldsymbol{x} - \boldsymbol{p})) \prod_{j = 1}^{m+1} (x^{i_j} - p^{i_j})\right)\,\mathrm{d}t$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Remainder and Bachmann-Landau Notation
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\boldsymbol{p} \in \mathcal{D}$.
>
>If $f$ is $m$-times [totally differentiable](./Differentiation/Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$, then the [remainder](./Taylor%20Expansion%20(Real%20Scalar%20Fields).md) $R_{m+1}(\boldsymbol{p}; \boldsymbol{x}) = f(\boldsymbol{x}) - T_m(\boldsymbol{p};\boldsymbol{x})$ of $f$'s $m$-th [Taylor polynomial](./Taylor%20Expansion%20(Real%20Scalar%20Fields).md) $T_m(\boldsymbol{p};\boldsymbol{x})$ is [little o](../Asymptotic%20Analysis/Bachmann-Landau%20Notation.md#Little%20o%20Notation) of $||\boldsymbol{x} - \boldsymbol{p}||^m$ for $\boldsymbol{x} \to \boldsymbol{p}$:
>
>$$R_{m+1}(\boldsymbol{p}; \boldsymbol{x}) = o(||\boldsymbol{x} - \boldsymbol{p}||^m) \qquad \text{for} \qquad \boldsymbol{x} \to \boldsymbol{p}$$
>
>If $f$ is $(m+1)$-times [continuously partially differentiable](./Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on an [open](../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) [neighborhood](../../../Topology/Topological%20Spaces/Topological%20Space.md#Neighborhoods) of $\boldsymbol{p}$, then the [remainder](./Taylor%20Expansion%20(Real%20Scalar%20Fields).md) $R_{m+1}(\boldsymbol{p}; \boldsymbol{x}) = f(\boldsymbol{x}) - T_m(\boldsymbol{p};\boldsymbol{x})$ of $f$'s $m$-th [Taylor polynomial](./Taylor%20Expansion%20(Real%20Scalar%20Fields).md) $T_m(\boldsymbol{p};\boldsymbol{x})$ is [Big O](../Asymptotic%20Analysis/Bachmann-Landau%20Notation.md#Big%20O%20Notation) of $||\boldsymbol{x} - \boldsymbol{p}||^{m+1}$ for $\boldsymbol{x} \to \boldsymbol{p}$:
>
>$$R_{m+1}(\boldsymbol{p}; \boldsymbol{x}) = O(||\boldsymbol{x} - \boldsymbol{p}||^{m+1}) \qquad \text{for} \qquad \boldsymbol{x} \to \boldsymbol{p}$$
>
>>[!EXAMPLE]- Example: $f(x, y) = x^3 \mathrm{e}^{y}$
>>
>>Consider the [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^2 \to \mathbb{R}$ defined as follows:
>>
>>$$f\left(x, y\right) = x^3 \mathrm{e}^{y}$$
>>
>>For its [partial derivatives](./Differentiation/Partial%20Differentiability%20(Real%20Scalar%20Fields).md), we have:
>>
>>$$\partial_{x}f(x, y) = 3x^2 \mathrm{e}^{y} \qquad \partial_{y}f(x, y) = x^3 \mathrm{e}^{y}$$
>>
>>$$\partial_{x}\partial_{x}f(x, y) = 6x \mathrm{e}^{y} \qquad \partial_{x}\partial_{y}f(x, y) = 3x^2 \mathrm{e}^{y} = \partial_{y}\partial_{x}f(x, y) \qquad \partial_{y}\partial_{y}f(x, y) = x^3 \mathrm{e}^{y}$$
>>
>>Therefore:
>>
>>$$f\left(\begin{bmatrix}1 \\ 0\end{bmatrix}\right) = 1 \qquad \nabla f\left(\begin{bmatrix}1 \\ 0\end{bmatrix}\right) = \begin{bmatrix}3 \\ 1\end{bmatrix} \qquad H_f\left(\begin{bmatrix}1 \\ 0\end{bmatrix}\right) = \begin{bmatrix}6 & 3 \\ 3 & 1\end{bmatrix}$$
>>
>>We thus have:
>>
>>$$\begin{aligned}f\left(x, y\right) & = T_2\left(\begin{bmatrix}1 \\ 0\end{bmatrix}; \begin{bmatrix}x \\ y\end{bmatrix}\right) + R_3\left(\begin{bmatrix}1 \\ 0\end{bmatrix}; \begin{bmatrix}x \\ y\end{bmatrix}\right) \\ & = f\left(\begin{bmatrix}1 \\ 0\end{bmatrix}\right) + \nabla f\left(\begin{bmatrix}1 \\ 0\end{bmatrix}\right)^{\mathsf{T}}\left(\begin{bmatrix}x \\ y\end{bmatrix}-\begin{bmatrix}1 \\ 0\end{bmatrix}\right) + \frac{1}{2}\left(\begin{bmatrix}x \\ y\end{bmatrix}-\begin{bmatrix}1 \\ 0\end{bmatrix}\right)^{\mathsf{T}} H_f\left(\begin{bmatrix}1 \\ 0\end{bmatrix}\right) \left(\begin{bmatrix}x \\ y\end{bmatrix}-\begin{bmatrix}1 \\ 0\end{bmatrix}\right) + R_3\left(\begin{bmatrix}1 \\ 0\end{bmatrix}; \begin{bmatrix}x \\ y\end{bmatrix}\right) \\ & = f\left(\begin{bmatrix}1 \\ 0\end{bmatrix}\right) + \begin{bmatrix}3 & 1\end{bmatrix}\left(\begin{bmatrix}x \\ y\end{bmatrix}-\begin{bmatrix}1 \\ 0\end{bmatrix}\right) + \frac{1}{2}\left(\begin{bmatrix}x \\ y\end{bmatrix}-\begin{bmatrix}1 \\ 0\end{bmatrix}\right)^{\mathsf{T}}\begin{bmatrix}6 & 3 \\ 3 & 1\end{bmatrix}\left(\begin{bmatrix}x \\ y\end{bmatrix}-\begin{bmatrix}1 \\ 0\end{bmatrix}\right) + O\left(\left\vert\left\vert \begin{bmatrix}x \\ y\end{bmatrix} - \begin{bmatrix}1 \\ 0\end{bmatrix}\right\vert\right\vert^3\right) \qquad \text{for} \qquad \begin{bmatrix}x \\ y\end{bmatrix} \to \begin{bmatrix}1 \\ 0\end{bmatrix} \\ & = f\left(\begin{bmatrix} 1 \\ 0 \end{bmatrix}\right) + 3(x - 1) + y + 3(x - 1)^2 + 3(x - 1)y + \frac{1}{2}y^2 + O\left(\left((x-1)^2 + y^2\right)^{3/2}\right)\end{aligned}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>