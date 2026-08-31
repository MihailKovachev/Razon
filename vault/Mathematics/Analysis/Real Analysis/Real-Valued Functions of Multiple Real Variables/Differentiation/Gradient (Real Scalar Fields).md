---
tags:
    - real-analysis
    - vector-analysis
    - analysis
    - mathematics
---

# Gradient (Real Scalar Fields)

>[!DEFINITION] Definition: Gradient
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md), let $\boldsymbol{p} \in \operatorname{int} \mathcal{D}$ be an [interior point](../../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $\mathcal{D}$ and suppose that $f$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$.
>
>The **gradient** of $f$ at $\boldsymbol{p}$ is the [vector](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) whose components are $f$'s [partial derivatives](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$:
>
>$$\begin{bmatrix} \partial_1 f(\boldsymbol{p}) \\ \vdots \\ \partial_n f(\boldsymbol{p}) \end{bmatrix}$$
>
>>[!NOTATION]
>>
>>$$\nabla f(\boldsymbol{p}) \qquad \operatorname{grad} f(\boldsymbol{p})$$
>>
>
>>[!EXAMPLE]- Example: $f(x, y) = x^2 y^3 + x$
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^2 \to \mathbb{R}$ defined as follows:
>>
>>$$f\left(x, y\right) = x^2 y^3 + x$$
>>
>>It is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^2$:
>>
>>$$\frac{\partial f}{\partial x} \left(x, y\right) = 2x y^3 + 1 \qquad \frac{\partial f}{\partial y} \left(x, y\right) = 3 x^2 y^2$$
>>
>>Its [gradient](./Gradient%20(Real%20Scalar%20Fields).md) is thus the following for all $\begin{bmatrix}x & y\end{bmatrix}^{\mathsf{T}} \in \mathbb{R}^2$:
>>
>>$$\nabla f(x,y) = \begin{bmatrix} 2x y^3 + 1 \\ 3 x^2 y^2\end{bmatrix}$$
>>
>
>>[!EXAMPLE]- Example: $f(\boldsymbol{x}) = \boldsymbol{a}^{\mathsf{T}}\boldsymbol{x}$
>>
>>Let $\boldsymbol{a} = \begin{bmatrix} a_1 & \cdots & a_n \end{bmatrix}^{\mathsf{T}}\in \mathbb{R}^n$ be a [real vector](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) and consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^n \to \mathbb{R}$ defined as follows:
>>
>>$$f(\boldsymbol{x}) \overset{\text{def}}{=} \boldsymbol{a}^{\mathsf{T}}\boldsymbol{x} = a_1 x_1 + \cdots + a_n x_n$$
>>
>>We see that $f$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) at every $\boldsymbol{x} \in \mathbb{R}^n$:
>>
>>$$\partial_1 f(\boldsymbol{x}) = a_1 \qquad \cdots \qquad \partial_n f(\boldsymbol{x}) = a_n$$
>>
>>Therefore, $f$'s [gradient](./Gradient%20(Real%20Scalar%20Fields).md) is the following for each $\boldsymbol{x} \in \mathbb{R}^n$:
>>
>>$$\nabla f(\boldsymbol{x}) = \begin{bmatrix}a_1 \\ \vdots \\ a_n\end{bmatrix} = \boldsymbol{a}$$
>>
>
>>[!EXAMPLE]- Example: $f(\boldsymbol{x}) = \boldsymbol{x}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{x}$
>>
>>Let $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ be a [real matrix](../../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md)
>>
>>$$\boldsymbol{A} = \begin{bmatrix}A_{11} & \cdots & A_{1n} \\ \vdots & \ddots & \vdots \\ A_{n1} & \cdots & A_{nn}\end{bmatrix}$$
>>
>>and consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^n \to \mathbb{R}$ defined as follows:
>>
>>$$f(\boldsymbol{x}) \overset{\text{def}}{=} \boldsymbol{x}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{x} = \sum_{i = 1}^n \sum_{j = 1}^n x_i A_{ij} x_j$$
>>
>>We see that $f$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^n$. By applying the [product rule](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md), we get the following for each $k \in \{1, \dotsc, n\}$:
>>
>>$$\begin{aligned}\partial_k f(x_1, \dotsc, x_n) & = \partial_k \left(\sum_{i = 1}^n \sum_{j = 1}^n x_i A_{ij} x_j \right) \\ & = \sum_{i=1}^n \sum_{j = 1}^n \partial_k (x_i A_{ij} x_j) \\ & = \sum_{i=1}^n \sum_{j = 1}^n (\partial_k x_i) A_{ij} x_j + x_i \partial_k (A_{ij} x_j) \\ & = \sum_{i=1}^n \sum_{j = 1}^n (\partial_k x_i) A_{ij} x_j + x_i A_{ij}(\partial_k x_j) \\ & = \sum_{i=1}^n \sum_{j = 1}^n (\partial_k x_i) A_{ij} x_j + \sum_{i=1}^n \sum_{j = 1}^n x_i A_{ij}(\partial_k x_j)\end{aligned}$$
>>
>>We have $\partial_k x_i = 1$ for $i = k$ and $\partial_k x_i = 0$ otherwise. Summing over $i$ leaves only the one term where $i = k$ and so the first sum collapses to the following:
>>
>>$$\sum_{i = 1}^n \sum_{j = 1}^n (\partial_k x_i) A_{ij} x_j = \sum_{j = 1}^n A_{kj} x_j$$
>>
>>By the same token, $\partial_k x_j = 1$ for $j = k$ and $\partial_k x_j = 0$ otherwise. Summing over $j$ leaves only the one term where $j = k$ and so the second sum collapses to the following:
>>
>>$$\sum_{i = 1}^n \sum_{j = 1}^n x_i A_{ij}(\partial_k x_j) = \sum_{i = 1}^n x_i A_{ik}$$
>>
>>Together, we get:
>>
>>$$\partial_k f(x_1, \dotsc, x_n) = \sum_{j = 1}^n A_{kj} x_j + \sum_{i = 1}^n x_i A_{ik}$$
>>
>>Therefore, $f$'s [gradient](./Gradient%20(Real%20Scalar%20Fields).md) is given as follows for each $\boldsymbol{x} \in \mathbb{R}^n$:
>>
>>$$\begin{aligned}\nabla f(x_1, \dotsc, x_n) & = \begin{bmatrix} \sum_{j = 1}^n A_{1j} x_j + \sum_{i = 1}^n x_i A_{i1} \\ \vdots \\ \sum_{j = 1}^n A_{nj} x_j + \sum_{i = 1}^n x_i A_{in}\end{bmatrix} \\ & = \begin{bmatrix} \sum_{j = 1}^n A_{1j} x_j \\ \vdots \\ \sum_{j = 1}^n A_{nj} x_j\end{bmatrix} + \begin{bmatrix}\sum_{i = 1}^n x_i A_{i1} \\ \vdots \\ \sum_{i = 1}^n x_i A_{in} \end{bmatrix} \\ & = \boldsymbol{A}\boldsymbol{x} + \boldsymbol{A}^{\mathsf{T}}\boldsymbol{x} \\ & = (\boldsymbol{A}+\boldsymbol{A}^{\mathsf{T}})\boldsymbol{x} \end{aligned}$$
>>
>

>[!THEOREM] Theorem: Gradient and Jacobian
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md), let $\boldsymbol{p} \in \operatorname{int} \mathcal{D}$ be an [interior point](../../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $\mathcal{D}$ and suppose that $f$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$.
>
>The [gradient](./Gradient%20(Real%20Scalar%20Fields).md) of $f$ at $\boldsymbol{p}$ is the [transpose](../../../../Algebra/Matrices/Matrix%20Transposition.md) of $f$'s [Jacobian matrix](../../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md) at $\boldsymbol{p}$:
>
>$$\nabla f(\boldsymbol{p}) = (J_f(\boldsymbol{p}))^{\mathsf{T}}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Total Differentiability of Real Scalar Fields
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\boldsymbol{p} \in \operatorname{int} \mathcal{D}$ be an [interior point](../../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $\mathcal{D}$.
>
>Then $f$ is [totally differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p}$ if and only if the following [limit](../Limits%20(Real%20Scalar%20Fields).md) involving a [dot product](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Dot%20Product.md) with $f$'s [gradient](./Gradient%20(Real%20Scalar%20Fields).md) is zero:
>
>$$\lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{f(\boldsymbol{x}) - f(\boldsymbol{p}) - \nabla f(\boldsymbol{p}) \cdot (\boldsymbol{x} - \boldsymbol{p})}{||\boldsymbol{x} - \boldsymbol{p}||} = 0,$$
>
>>[!EXAMPLE]- Example: $f(\boldsymbol{x}) = \boldsymbol{a}^{\mathsf{T}}\boldsymbol{x}$
>>
>>Let $\boldsymbol{a} = \begin{bmatrix} a_1 & \cdots & a_n \end{bmatrix}^{\mathsf{T}}\in \mathbb{R}^n$ be a [real vector](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) and consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^n \to \mathbb{R}$ defined as follows:
>>
>>$$f(\boldsymbol{x}) \overset{\text{def}}{=} \boldsymbol{a}^{\mathsf{T}}\boldsymbol{x} = a_1 x_1 + \cdots + a_n x_n$$
>>
>>Its [gradient](./Gradient%20(Real%20Scalar%20Fields).md) is the following for all $\boldsymbol{p} \in \mathbb{R}^n$:
>>
>>$$\nabla f(\boldsymbol{p}) = \boldsymbol{a}$$
>>
>>
>>Now, for each $\boldsymbol{p} \in \mathbb{R}^n$, we have
>>
>>$$\begin{aligned}\lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{f(\boldsymbol{x}) - f(\boldsymbol{p}) - \nabla f(\boldsymbol{x}) \cdot (\boldsymbol{x} - \boldsymbol{p})}{||\boldsymbol{x} - \boldsymbol{p}||} & = \lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{f(\boldsymbol{x}) - f(\boldsymbol{p}) - \boldsymbol{a} \cdot (\boldsymbol{x} - \boldsymbol{p})}{||\boldsymbol{x} - \boldsymbol{p}||} \\ & = \lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{\boldsymbol{a}^{\mathsf{T}}\boldsymbol{x} - \boldsymbol{a}^{\mathsf{T}}\boldsymbol{p} - \boldsymbol{a}^{\mathsf{T}}(\boldsymbol{x} - \boldsymbol{p})}{||\boldsymbol{x} - \boldsymbol{p}||} \\ & = \lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{\boldsymbol{a}^{\mathsf{T}}(\boldsymbol{x} - \boldsymbol{p}) - \boldsymbol{a}^{\mathsf{T}}(\boldsymbol{x} - \boldsymbol{p})}{||\boldsymbol{x} - \boldsymbol{p}||} \\ & = \lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{0}{||\boldsymbol{x} - \boldsymbol{p}||} \\ & = 0\end{aligned}$$
>>
>>Therefore, $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^n$.
>>
>
>>[!EXAMPLE]- Example: $f(\boldsymbol{x}) = \boldsymbol{x}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{x}$
>>
>>Let $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ be a [real matrix](../../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md)
>>
>>$$\boldsymbol{A} = \begin{bmatrix}A_{11} & \cdots & A_{1n} \\ \vdots & \ddots & \vdots \\ A_{n1} & \cdots & A_{nn}\end{bmatrix}$$
>>
>>and consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^n \to \mathbb{R}$ defined as follows:
>>
>>$$f(\boldsymbol{x}) \overset{\text{def}}{=} \boldsymbol{x}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{x} = \sum_{i = 1}^n \sum_{j = 1}^n x_i A_{ij} x_j$$
>>
>>Its [gradient](./Gradient%20(Real%20Scalar%20Fields).md) is the following for all $\boldsymbol{p} \in \mathbb{R}^n$:
>>
>>$$\nabla f(\boldsymbol{p}) = (\boldsymbol{A} + \boldsymbol{A}^{\mathsf{T}})\boldsymbol{p}$$
>>
>>Now, for each $\boldsymbol{p} \in \mathbb{R}^n$, we have:
>>
>>$$\begin{aligned}\lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{f(\boldsymbol{x}) - f(\boldsymbol{p}) - \nabla f(\boldsymbol{p}) \cdot (\boldsymbol{x} - \boldsymbol{p})}{||\boldsymbol{x} - \boldsymbol{p}||} & = \lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{\boldsymbol{x}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{x} - \boldsymbol{p}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{p} - ((\boldsymbol{A} + \boldsymbol{A}^{\mathsf{T}})\boldsymbol{p})^{\mathsf{T}}(\boldsymbol{x} - \boldsymbol{p})}{||\boldsymbol{x} - \boldsymbol{p}||} \\ & = \lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{\boldsymbol{x}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{x} - \boldsymbol{p}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{p} - \boldsymbol{p}^{\mathsf{T}}(\boldsymbol{A}^{\mathsf{T}} + A)(\boldsymbol{x} - \boldsymbol{p})}{||\boldsymbol{x} - \boldsymbol{p}||} \\ & = \lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{\boldsymbol{x}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{x} - \boldsymbol{p}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{p} - \boldsymbol{p}^{\mathsf{T}} (\boldsymbol{A}^{\mathsf{T}}\boldsymbol{x} - \boldsymbol{A}^{\mathsf{T}}\boldsymbol{p} + \boldsymbol{A}\boldsymbol{x} - \boldsymbol{A}\boldsymbol{p})}{||\boldsymbol{x} - \boldsymbol{p}||} \\ & = \lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{\boldsymbol{x}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{x} - \boldsymbol{p}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{p} - \boldsymbol{p}^{\mathsf{T}}\boldsymbol{A}^{\mathsf{T}}\boldsymbol{x} + \boldsymbol{p}^{\mathsf{T}}\boldsymbol{A}^{\mathsf{T}}\boldsymbol{p} - \boldsymbol{p}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{x} + \boldsymbol{p}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{p}}{||\boldsymbol{x} - \boldsymbol{p}||} \\ & = \lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{\boldsymbol{x}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{x} - \boldsymbol{p}^{\mathsf{T}}\boldsymbol{A}^{\mathsf{T}}\boldsymbol{x} + \boldsymbol{p}^{\mathsf{T}}\boldsymbol{A}^{\mathsf{T}}\boldsymbol{p} - \boldsymbol{p}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{x}}{||\boldsymbol{x} - \boldsymbol{p}||} \\ & = \lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{\boldsymbol{x}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{x} - (\boldsymbol{x}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{p})^{\mathsf{T}} + (\boldsymbol{p}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{p})^{\mathsf{T}} - \boldsymbol{p}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{x}}{||\boldsymbol{x} - \boldsymbol{p}||} \\ & = \lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{\boldsymbol{x}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{x} - \boldsymbol{x}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{p} + \boldsymbol{p}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{p} - \boldsymbol{p}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{x}}{||\boldsymbol{x} - \boldsymbol{p}||} \\ & = \lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{\boldsymbol{x}^{\mathsf{T}} \boldsymbol{A} (\boldsymbol{x} - \boldsymbol{p}) - \boldsymbol{p}^{\mathsf{T}}\boldsymbol{A} (\boldsymbol{x} - \boldsymbol{p})}{||\boldsymbol{x} - \boldsymbol{p}||} \\ & = \lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{(\boldsymbol{x}^{\mathsf{T}} - \boldsymbol{p}^{\mathsf{T}}) \boldsymbol{A} (\boldsymbol{x} - \boldsymbol{p})}{||\boldsymbol{x} - \boldsymbol{p}||} \\ & = \lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{(\boldsymbol{x} - \boldsymbol{p})^{\mathsf{T}} \boldsymbol{A} (\boldsymbol{x} - \boldsymbol{p})}{||\boldsymbol{x} - \boldsymbol{p}||}\end{aligned}$$
>>
>>With the substitution $\boldsymbol{h} = \boldsymbol{x} - \boldsymbol{p} = \begin{bmatrix}h_1, \dotsc, h_n \end{bmatrix}^{\mathsf{T}}$ we get:
>>
>>$$\lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{(\boldsymbol{x} - \boldsymbol{p})^{\mathsf{T}} \boldsymbol{A} (\boldsymbol{x} - \boldsymbol{p})}{||\boldsymbol{x} - \boldsymbol{p}||} = \lim_{\boldsymbol{h} \to \boldsymbol{0}} \frac{\boldsymbol{h}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{h}}{||\boldsymbol{h}||}$$
>>
>>The [product](../../../../Algebra/Matrices/Matrix%20Product.md) $\boldsymbol{h}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{h}$ is given by the following:
>>
>>$$\begin{aligned}\boldsymbol{h}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{h} & = \boldsymbol{h}^{\mathsf{T}}(\boldsymbol{A}\boldsymbol{h}) = \begin{bmatrix} h_1 & h_2 & \dots & h_n \end{bmatrix} \begin{bmatrix} \sum_{j=1}^{n} A_{1j} h_j \\ \sum_{j=1}^{n} A_{2j} h_j \\ \vdots \\ \sum_{j=1}^{n} A_{nj} h_j \end{bmatrix} \\ & = \sum_{i=1}^{n} h_i \left( \sum_{j=1}^{n} A_{ij} h_j \right) \\ & = \sum_{i=1}^{n} \sum_{j=1}^{n} A_{ij} h_i h_j\end{aligned}$$
>>
>>We thus have:
>>
>>$$|\boldsymbol{h}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{h}| \leq \sum_{i=1}^{n} \sum_{j=1}^{n} |A_{ij}| |h_i| |h_j|$$
>>
>>From $||\boldsymbol{h}|| = \sqrt{\sum_{k = 1}^n (h_k)^2}$, we know that
>>
>>$$|h_k| \le ||\boldsymbol{h}||$$
>>
>>for all $k \in \{1,\dotsc,n\}$.
>>
>>Therefore,
>>
>>$$|h_i||h_j| \le ||\boldsymbol{h}||^2$$
>>
>>for all $i,j \in \{1,\dotsc,n\}$.
>>
>>From this, we obtain the following:
>>
>>$$|\boldsymbol{h}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{h}| \leq \sum_{i=1}^{n} \sum_{j=1}^{n} |A_{ij}| ||\boldsymbol{h}||^2 = ||\boldsymbol{h}||^2 \sum_{i=1}^{n} \sum_{j=1}^{n} |A_{ij}|$$
>>
>>The sum $\sum_{i=1}^{n} \sum_{j=1}^{n} |A_{ij}|$ is just a constant and so
>>
>>$$|\boldsymbol{h}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{h}| \leq C ||\boldsymbol{h}||^2$$
>>
>>with $C = \sum_{i=1}^{n} \sum_{j=1}^{n} |A_{ij}|$. Divide by $||\boldsymbol{h}||$:
>>
>>$$0 \le \frac{|\boldsymbol{h}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{h}|}{||\boldsymbol{h}||} \leq C ||\boldsymbol{h}||$$
>>
>>We know that the [limit](../Limits%20(Real%20Scalar%20Fields).md) of $C ||\boldsymbol{h}||$ for $\boldsymbol{h} \to \boldsymbol{0}$ is zero. By the [squeeze theorem](../Limits%20(Real%20Scalar%20Fields).md) we get:
>>
>>$$\lim_{\boldsymbol{h} \to \boldsymbol{0}} \frac{|\boldsymbol{h}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{h}|}{||\boldsymbol{h}||} = 0,$$
>>
>>i.e.
>>
>>$$\lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{(\boldsymbol{x} - \boldsymbol{p})^{\mathsf{T}} \boldsymbol{A} (\boldsymbol{x} - \boldsymbol{p})}{||\boldsymbol{x} - \boldsymbol{p}||} = 0.$$
>>
>>Therefore, $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^n$.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Gradient of Linear Combination
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R}^n \to \mathbb{R}$ be [real scalar fields](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\boldsymbol{p} \in \operatorname{int} (\mathcal{D}_f \cap \mathcal{D}_g)$ be an [interior point](../../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $\mathcal{D}_f \cap \mathcal{D}_g$.
>
>If $f$ and $g$ are [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$, then so is $\lambda f + \mu g$ for all $\lambda, \mu \in \mathbb{R}$ and its [gradient](./Gradient%20(Real%20Scalar%20Fields).md) is given by the [gradients](./Gradient%20(Real%20Scalar%20Fields).md) of $f$ and $g$ as follows:
>
>$$\nabla (\lambda f + \mu g)(\boldsymbol{p}) = \lambda \nabla f(\boldsymbol{p}) + \mu \nabla g(\boldsymbol{p})$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Product Rule with Gradients
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R}^n \to \mathbb{R}$ be [real scalar fields](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\boldsymbol{p} \in \operatorname{int} (\mathcal{D}_f \cap \mathcal{D}_g)$ be an [interior point](../../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $\mathcal{D}_f \cap \mathcal{D}_g$.
>
>If $f$ and $g$ are [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$, then so is $fg$ and its [gradient](./Gradient%20(Real%20Scalar%20Fields).md) is given by the [gradients](./Gradient%20(Real%20Scalar%20Fields).md) of $f$ and $g$ as follows:
>
>$$\nabla(fg)(\boldsymbol{p}) = g(\boldsymbol{p}) \nabla f(\boldsymbol{p}) + f(\boldsymbol{p}) \nabla g(\boldsymbol{p})$$
>
>>[!PROOF]-
>>
>>Since $f$ and $g$ are both [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$, we know that their [partial derivatives](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) $\partial_k f(\boldsymbol{p})$ and $\partial_k g(\boldsymbol{p})$ exist for all $k \in \{1, \dotsc, n\}$. We apply the [product rule](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md):
>>
>>$$\partial_k (fg)(\boldsymbol{p}) = (\partial_k f)(\boldsymbol{p})g(\boldsymbol{p}) + f(\boldsymbol{p})(\partial_k g)(\boldsymbol{p}) = g(\boldsymbol{p}) \partial_k f(\boldsymbol{p}) + f(\boldsymbol{p})\partial_k g(\boldsymbol{p})$$
>>
>>Therefore, the [gradient](./Gradient%20(Real%20Scalar%20Fields).md) of $fg$ is the following:
>>
>>$$\nabla (fg)(\boldsymbol{p}) = \begin{bmatrix} g(\boldsymbol{p}) \partial_1 f(\boldsymbol{p}) + f(\boldsymbol{p})\partial_1 g(\boldsymbol{p}) \\ \vdots \\ g(\boldsymbol{p}) \partial_n f(\boldsymbol{p}) + f(\boldsymbol{p})\partial_n g(\boldsymbol{p})\end{bmatrix} = g(\boldsymbol{p}) \nabla f(\boldsymbol{p}) + f(\boldsymbol{p}) \nabla g(\boldsymbol{p})$$
>>
>

>[!THEOREM] Theorem: Quotient Rule with Gradients
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R}^n \to \mathbb{R}$ be [real scalar fields](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\boldsymbol{p} \in \operatorname{int} (\mathcal{D}_f \cap \mathcal{D}_g)$ be an [interior point](../../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $\mathcal{D}_f \cap \mathcal{D}_g$.
>
>If $f$ and $g$ are both [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$ and $g(\boldsymbol{p}) \ne 0$, then $f/g$ is also [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) there and its [gradient](./Gradient%20(Real%20Scalar%20Fields).md) is given by the [gradients](./Gradient%20(Real%20Scalar%20Fields).md) of $f$ and $g$ as follows:
>
>$$\nabla(f/g)(\boldsymbol{p}) = \frac{g(\boldsymbol{p}) \nabla f(\boldsymbol{p}) - f(\boldsymbol{p}) \nabla g(\boldsymbol{p})}{g(\boldsymbol{p})^2}$$
>
>>[!PROOF]-
>>
>>Since $f$ and $g$ are both [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$ and $g(\boldsymbol{p}) \ne 0$, we know that their [partial derivatives](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) $\partial_k f(\boldsymbol{p})$ and $\partial_k g(\boldsymbol{p})$ exist for all $k \in \{1, \dotsc, n\}$. We apply the [quotient rule](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md):
>>
>>$$\partial_k (f/g)(\boldsymbol{p}) = \frac{(\partial_k f)(\boldsymbol{p})g(\boldsymbol{p}) - f(\boldsymbol{p})(\partial_k g)(\boldsymbol{p})}{g(\boldsymbol{p})^2} = \frac{g(\boldsymbol{p}) \partial_k f(\boldsymbol{p}) - f(\boldsymbol{p})\partial_k g(\boldsymbol{p})}{g(\boldsymbol{p})^2}$$
>>
>>Therefore, the [gradient](./Gradient%20(Real%20Scalar%20Fields).md) of $f/g$ is the following:
>>
>>$$\nabla (f/g)(\boldsymbol{p}) = \begin{bmatrix} \frac{g(\boldsymbol{p}) \partial_1 f(\boldsymbol{p}) - f(\boldsymbol{p})\partial_1 g(\boldsymbol{p})}{g(\boldsymbol{p})^2} \\ \vdots \\ \frac{g(\boldsymbol{p}) \partial_n f(\boldsymbol{p}) - f(\boldsymbol{p})\partial_n g(\boldsymbol{p})}{g(\boldsymbol{p})^2}\end{bmatrix} = \frac{g(\boldsymbol{p}) \nabla f(\boldsymbol{p}) - f(\boldsymbol{p}) \nabla g(\boldsymbol{p})}{g(\boldsymbol{p})^2}$$
>>
>

>[!THEOREM] Theorem: Dot Product Rule
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^m \to \mathbb{R}^n$ and $g: \mathcal{D}_g \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be [real vector functions](../../Real%20Vector%20Functions/Real%20Vector%20Functions.md) and let $\boldsymbol{p} \in \operatorname{int} (\mathcal{D}_f \cap \mathcal{D}_g)$ be an [interior point](../../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $\mathcal{D}_f \cap \mathcal{D}_g$.
>
>If $f$ and $g$ are [partially differentiable](../../Real%20Vector%20Functions/Differentiation/Partial%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p}$, then so is their [dot product](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Dot%20Product.md) and its [gradient](./Gradient%20(Real%20Scalar%20Fields).md) is given by the [transpositions](../../../../Algebra/Matrices/Matrix%20Transposition.md) of the [Jacobian matrices](../../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md) of $f$ and $g$ as follows:
>
>$$\nabla (f\cdot g)(\boldsymbol{p}) = J_f(\boldsymbol{p})^{\mathsf{T}}g(\boldsymbol{p}) + J_g(\boldsymbol{p})^{\mathsf{T}}f(\boldsymbol{p})$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Chain Rule with Real Functions
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../../Real%20Functions/Real%20Functions.md), let $g: \mathcal{D}_g \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and with $g(\mathcal{D}_g) \subseteq \mathcal{D}_f$ and let $\boldsymbol{p} \in \operatorname{int} \mathcal{D}_g$ be an [interior point](../../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $\mathcal{D}_g$.
>
>If $g$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$ and $g(\boldsymbol{p})$ is an [interior point](../../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $\mathcal{D}_f$ and $f$ is [differentiable](../../Real%20Functions/Differentiability%20(Real%20Functions).md) at $g(\boldsymbol{p})$, then the [composition](../../../Functions/Functions.md) $f\circ g$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$ with the following [gradient](./Gradient%20(Real%20Scalar%20Fields).md):
>
>$$\nabla (f \circ g)(\boldsymbol{p}) = f'(g(\boldsymbol{p}))\nabla g(\boldsymbol{p})$$
>
>>[!EXAMPLE]-
>>
>>Let $f: \mathbb{R}_{\gt 0} \to \mathbb{R}$ be a [real function](../../Real%20Functions/Real%20Functions.md) which is [differentiable](../../Real%20Functions/Differentiability%20(Real%20Functions).md) on $\mathbb{R}_{\gt 0}$ and consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f(||\boldsymbol{x}||)$.
>>
>>We have:
>>
>>$$f(||\boldsymbol{x}||) = f\left(\sqrt{\sum_{i=1}^n x_i^2}\right)$$
>>
>>The [partial derivatives](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) of $\sqrt{\sum_{i=1}^n x_i^2}$ are defined on $\mathbb{R}^n$:
>>
>>$$\begin{aligned}\partial_k\sqrt{\sum_{i=1}^n x_i^2} = \frac{2 x_k}{2\sqrt{\sum_{i=1}^n x_i^2}} = \frac{x_k}{||\boldsymbol{x}||}\end{aligned}$$
>>
>>The [gradient](./Gradient%20(Real%20Scalar%20Fields).md) of $\sqrt{\sum_{i=1}^n x_i^2}$ at each $\boldsymbol{p} \in \mathbb{R}^n \setminus \{\boldsymbol{0}\}$ is thus the following:
>>
>>$$\nabla \left(\sqrt{\sum_{i=1}^n x_i^2}\right) (\boldsymbol{x}) = \frac{1}{||\boldsymbol{x}||}\boldsymbol{x}$$
>>
>>Since $f$ is [differentiable](../../Real%20Functions/Differentiability%20(Real%20Functions).md) on $\mathbb{R}_{\gt 0}$, the [gradient](./Gradient%20(Real%20Scalar%20Fields).md) of $f(||\boldsymbol{x}||)$ at each $\boldsymbol{x} \in \mathbb{R}^n \setminus \{\boldsymbol{0}\}$ is the following:
>>
>>$$\begin{aligned}\nabla f(||\boldsymbol{x}||) = \frac{f'(||\boldsymbol{x}||)}{||\boldsymbol{x}||} \boldsymbol{x}\end{aligned}$$
>>
>
>>[!EXAMPLE]- Example: $f(\boldsymbol{x}) = \ln (||\boldsymbol{x}||)$
>>
>>From the above example, we know that $f(\boldsymbol{x}) = \ln (||\boldsymbol{x}||)$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^n \setminus \{\boldsymbol{0}\}$  with the following [gradient](./Gradient%20(Real%20Scalar%20Fields).md):
>>
>>$$\nabla \ln (||\boldsymbol{x}||) = \frac{1}{||\boldsymbol{x}||} \frac{1}{||\boldsymbol{x}||} \boldsymbol{x} = \frac{1}{||\boldsymbol{x}||^2}\boldsymbol{x}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Chain Rule with Curves
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md), and let $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [parametric curve](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) with $g(\mathcal{D}_g) \subseteq \mathcal{D}_f$ and let $t \in \operatorname{int} \mathcal{D}_g$ be an [interior point](../../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $\mathcal{D}_g$.
>
>If $g$ is [differentiable](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) at $t$ and $g(t)$ is an [interior point](../../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $\mathcal{D}_f$ and $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $g(t)$, then the [composition](../../../Functions/Functions.md) $f \circ g$ is [differentiable](../../Real%20Functions/Differentiability%20(Real%20Functions).md) at $t$ and its [derivative](../../Real%20Functions/Differentiability%20(Real%20Functions).md) is the [dot product](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Dot%20Product.md) of $f$'s [gradient](./Gradient%20(Real%20Scalar%20Fields).md) and $g$'s [derivative](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md):
>
>$$(f\circ g)'(t) = \nabla f(g(t))\cdot g'(t)$$
>
>>[!EXAMPLE]-
>>
>>Let $g: [0,2\uppi] \to \mathbb{R}^2$ be the [curve](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) defined as follows:
>>
>>$$g(t) \overset{\text{def}}{=} \begin{bmatrix} \cos t \\ \sin t \end{bmatrix}$$
>>
>>Let $f: \mathbb{R}^2 \to \mathbb{R}$ be the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) defined as follows:
>>
>>$$f(x,y) \overset{\text{def}}{=} x^2 + xy + y^2$$
>>
>>We see that $g$ is [differentiable](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) on $[0,2\uppi]$:
>>
>>$$g'(t) = \begin{bmatrix}-\sin t \\ \cos t \end{bmatrix}$$
>>
>>We also see that $f$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^2$ with the following [gradient](./Gradient%20(Real%20Scalar%20Fields).md):
>>
>>$$\nabla f (x,y) = \begin{bmatrix}2x + y \\ x + 2y\end{bmatrix}$$
>>
>>We can also show that $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^2$. Therefore, $f \circ g$ is [differentiable](../../Real%20Functions/Differentiability%20(Real%20Functions).md) on $[0, 2\uppi]$:
>>
>>$$\begin{aligned}(f \circ g)'(t) & = \nabla f(g(t))^{\mathsf{T}}g'(t) \\ & = \begin{bmatrix}2 \cos t + \sin t & \cos t + 2\sin t\end{bmatrix} \begin{bmatrix}-\sin t \\ \cos t \end{bmatrix} \\ & = (2 \cos t + \sin t)(-\sin t) + (\cos t + 2\sin t) \cos t \\ & = \cos^2 t - \sin^2 t \\ & = \cos (2t)\end{aligned}$$
>>
>
>>[!PROOF]-
>>
>>Since $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $g(t) \in \mathcal{D}_f$, we know that $f(g(t) + \boldsymbol{h}) - f(g(t)) - \nabla f(g(t))^{\mathsf{T}} \boldsymbol{h}$ is [little o](../../Asymptotic%20Analysis/Bachmann-Landau%20Notation.md#Little%20o%20Notation) of $||\boldsymbol{h}||$ for $\boldsymbol{h} \to \boldsymbol{0}$:
>>
>>$$f(g(t) + \boldsymbol{h}) - f(g(t)) - \nabla f(g(t))^{\mathsf{T}} \boldsymbol{h} = o(||\boldsymbol{h}||) \qquad \text{for} \qquad \boldsymbol{h} \to \boldsymbol{0}$$
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Chain Rule with Real Vector Functions
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md), and let $g: \mathcal{D}_g \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](../../Real%20Vector%20Functions/Real%20Vector%20Functions.md) with $g(\mathcal{D}_g) \subseteq \mathcal{D}_f$ and let $\boldsymbol{p} \in \operatorname{int} \mathcal{D}_g$ be an [interior point](../../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $\mathcal{D}_g$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Curl of Gradient
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^3 \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md).
>
>If $f$ is twice [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{x} \in \operatorname{int} \mathcal{D}$, then the [curl](../../Real%20Vector%20Fields/Differentiation/Curl%20(Real%20Vector%20Fields).md) of $f$'s [gradient](./Gradient%20(Real%20Scalar%20Fields).md) at $\boldsymbol{x}$ is zero:
>
>$$\operatorname{curl} \operatorname{grad} f(\boldsymbol{x}) = \boldsymbol{0}$$
>
>>[!PROOF]-
>>
>>Let $(\nabla f)_1, (\nabla f)_2, (\nabla f)_3$ be the [component functions](../../Real%20Vector-Valued%20Functions.md) of $f$'s [gradient](./Gradient%20(Real%20Scalar%20Fields).md):
>>
>>$$\nabla f (\boldsymbol{x}) = \begin{bmatrix}(\nabla f)_1 (\boldsymbol{x}) \\ (\nabla f)_2(\boldsymbol{x}) \\ (\nabla f)_3 (\boldsymbol{x})\end{bmatrix} = \begin{bmatrix} \partial_1 f(\boldsymbol{x}) \\ \partial_2 f(\boldsymbol{x}) \\ \partial_3 f(\boldsymbol{x}) \end{bmatrix}$$
>>
>>The [curl](../../Real%20Vector%20Fields/Differentiation/Curl%20(Real%20Vector%20Fields).md) of $\nabla f$ is the following:
>>
>>$$\begin{aligned}\nabla \times \nabla f(\boldsymbol{x}) & = \begin{bmatrix} \partial_2 (\nabla f)_3(\boldsymbol{x}) - \partial_3 (\nabla f)_2(\boldsymbol{x}) \\ \partial_3 (\nabla f)_1(\boldsymbol{x}) - \partial_1 (\nabla f)_3(\boldsymbol{x}) \\ \partial_1 (\nabla f)_2(\boldsymbol{x}) - \partial_2 (\nabla f)_1(\boldsymbol{x}) \end{bmatrix} \\ & = \begin{bmatrix} \partial_2 \partial_3 f(\boldsymbol{x}) - \partial_3 \partial_2 f(\boldsymbol{x}) \\ \partial_3 \partial_1 f(\boldsymbol{x}) - \partial_1 \partial_3 f(\boldsymbol{x}) \\ \partial_1 \partial_2 f(\boldsymbol{x}) - \partial_2 \partial_1 f(\boldsymbol{x}) \end{bmatrix} \\ & = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} \\ & = \boldsymbol{0}\end{aligned}$$
>>
>

>[!THEOREM] Theorem: Mean Value Theorem via Gradient
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\boldsymbol{a}, \boldsymbol{b} \in \mathcal{D}$ such that $L = \{\boldsymbol{a} + t(\boldsymbol{b} - \boldsymbol{a}) \mid t \in [0,1]\} \subseteq \mathcal{D}$.
>
>If $f$ is [continuous](../Continuity%20(Real%20Scalar%20Fields).md) on $L$ and [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) on $\operatorname{int} L$, then there exists some $\boldsymbol{\xi} \in \operatorname{int} L$ such that $f(\boldsymbol{b}) - f(\boldsymbol{a})$ is equal to the [product](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Dot%20Product.md) of $f$'s [gradient](./Gradient%20(Real%20Scalar%20Fields).md) at $\boldsymbol{\xi}$ and $\boldsymbol{b} - \boldsymbol{a}$:
>
>$$f(\boldsymbol{b}) - f(\boldsymbol{a}) = \nabla f(\boldsymbol{\xi}) \cdot (\boldsymbol{b} - \boldsymbol{a})$$
>
>>[!EXAMPLE]- Example: $f(x, y, z) = x^2 - 3y^2 + z$
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathcal{D} \to \mathbb{R}$ defined on $\mathcal{D} = \{\boldsymbol{p} \in \mathbb{R}^3 \mid ||\boldsymbol{p}|| \le 1\}$ as follows:
>>
>>$$f(x, y, z) = x^2 - 3y^2 + z$$
>>
>>For all $\boldsymbol{a}, \boldsymbol{b} \in \mathcal{D}$ and $t \in [0,1]$, we have:
>>
>>$$||\boldsymbol{a} + t(\boldsymbol{b} - \boldsymbol{a})|| = ||(1 - t)\boldsymbol{a} + t \boldsymbol{b}|| \le ||(1 - t)\boldsymbol{a}|| + ||t \boldsymbol{b}|| = |1 - t| ||\boldsymbol{a}|| + |t| ||\boldsymbol{b}||$$
>>
>>Since $t \in [0,1]$, we get:
>>
>>$$||\boldsymbol{a} + t(\boldsymbol{b} - \boldsymbol{a})|| \le (1 - t) ||\boldsymbol{a}|| + t ||\boldsymbol{b}||$$
>>
>>Since $\boldsymbol{a}, \boldsymbol{b} \in \mathcal{D}$, we know that $||\boldsymbol{a}|| \le 1$ and $||\boldsymbol{b}|| \le 1$. Therefore:
>>
>>$$||\boldsymbol{a} + t(\boldsymbol{b} - \boldsymbol{a})|| \le (1 - t) + t = 1$$
>>
>>and so $L = \{\boldsymbol{a} + t(\boldsymbol{b} - \boldsymbol{a}) \mid t \in [0, 1]\} \subseteq \mathcal{D}$.
>>
>>We see that $f$ is [continuous](../Continuity%20(Real%20Scalar%20Fields).md) on $L$ and [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) on $\operatorname{int} L$. Therefore, there exists some $\boldsymbol{\xi} \in \operatorname{int} L$ such that
>>
>>$$f(\boldsymbol{b}) - f(\boldsymbol{a}) = \nabla f(\boldsymbol{\xi}) \cdot (\boldsymbol{b} - \boldsymbol{a})$$
>>
>>For the [gradient](./Gradient%20(Real%20Scalar%20Fields).md) of $f$, we have
>>
>>$$\nabla f(x, y, z) = \begin{bmatrix} 2 x \\ -6 y \\ 1 \end{bmatrix}$$
>>
>>and so
>>
>>$$||\nabla f(x, y, z)|| = \sqrt{4x^2 + 36y^2 + 1} \le \sqrt{41}$$
>>
>>for all $x, y, z \in \operatorname{int} \mathcal{D}$. Specifically, $||\nabla f(\boldsymbol{\xi})|| \le \sqrt{41}$.
>>
>>By applying the [Cauchy-Schwarz inequality](../../../../Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md) to
>>
>>$$\nabla f(\boldsymbol{\xi}) \cdot (\boldsymbol{b} - \boldsymbol{a}),$$
>>
>>we get the following:
>>
>>$$|\nabla f(\boldsymbol{\xi}) \cdot (\boldsymbol{b} - \boldsymbol{a})| \le ||\nabla f(\boldsymbol{\xi})|| \, ||(\boldsymbol{b} - \boldsymbol{a})|| = \sqrt{41} ||\boldsymbol{b} - \boldsymbol{a}||$$
>>
>>Since $\nabla f(\boldsymbol{\xi}) \cdot (\boldsymbol{b} - \boldsymbol{a})  = f(\boldsymbol{b}) - f(\boldsymbol{a})$, we get:
>>
>>$$|f(\boldsymbol{b}) - f(\boldsymbol{a})| \le \sqrt{41} ||\boldsymbol{b} - \boldsymbol{a}||$$
>>
>
>>[!PROOF]-
>>
>>From the [mean value theorem via total differentials](./Total%20Differentiability%20(Real%20Scalar%20Fields).md), we know that there exists some $\boldsymbol{\xi} \in \operatorname{int} L$ such that
>>
>>$$f(\boldsymbol{b}) - f(\boldsymbol{a}) = \mathrm{d}f_{\boldsymbol{\xi}}(\boldsymbol{b} - \boldsymbol{a})$$
>>
>>Using the [matrix representation](../../../Functional%20Analysis/Linearity/Linearity%20(Functions).md#Matrix%20Representations) of the [total differential](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) $\mathrm{d}f_{\boldsymbol{\xi}}$, we get:
>>
>>$$f(\boldsymbol{b}) - f(\boldsymbol{a}) = J_f(\boldsymbol{\xi}) (\boldsymbol{b} - \boldsymbol{a})$$
>>
>>The [Jacobian matrix](../../Real%20Vector%20Functions/Differentiation/Jacobian%20Matrix.md) $J_f(\boldsymbol{\xi})$ is just the [transpose](../../../../Algebra/Matrices/Matrix%20Transposition.md) of the [gradient](./Gradient%20(Real%20Scalar%20Fields).md) $\nabla f(\boldsymbol{\xi})$:
>>
>>$$f(\boldsymbol{b}) - f(\boldsymbol{a}) = \nabla f(\boldsymbol{\xi})^{\mathsf{T}} (\boldsymbol{b} - \boldsymbol{a})$$
>>
>>$$f(\boldsymbol{b}) - f(\boldsymbol{a}) = \nabla f(\boldsymbol{\xi}) \cdot (\boldsymbol{b} - \boldsymbol{a})$$
>>
>

>[!THEOREM] Theorem: Gradient in Polar Coordinates
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^2 \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\mathcal{T}: (0, +\infty) \times (0, 2\uppi) \to \mathbb{R}^2$ be the [coordinate transformation](../../Euclidean%20Space/Coordinate%20Transformations.md) from [polar coordinates](../../Euclidean%20Space/Polar%20Coordinates.md):
>
>$$\mathcal{T}(\rho, \varphi) = \begin{bmatrix} \rho \cos \varphi \\ \rho \sin \varphi\end{bmatrix}$$
>
>Let $\tilde{f} = f \circ \mathcal{T}$ be the [polar coordinate representation](../Polar%20Coordinate%20Representations%20(Real%20Scalar%20Fields).md) of $f$.
>
>If $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\mathcal{T}(\rho, \varphi)$, then its [gradient](./Gradient%20(Real%20Scalar%20Fields).md) at $\mathcal{T}(\rho, \varphi)$ is expressed in the [normalized local coordinate basis](../../Euclidean%20Space/Local%20Coordinate%20Bases.md) of [polar coordinates](../../Euclidean%20Space/Polar%20Coordinates.md) using the [partial derivatives](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) of $\tilde{f}$ as follows:
>
>$$(\nabla f)(\mathcal{T}(\rho, \varphi)) = \partial_{\rho} \tilde{f}(\rho, \varphi) \boldsymbol{\hat{\rho}}(\rho, \varphi) + \frac{1}{\rho} \partial_{\varphi} \tilde{f} (\rho, \varphi)\boldsymbol{\hat{\varphi}}(\rho, \varphi)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Gradient in Cylindrical Coordinates
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^3 \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\mathcal{T}: (0,+\infty) \times (0,2\uppi) \times \mathbb{R} \to \mathbb{R}^3$ be the [coordinate transformation](../../Euclidean%20Space/Coordinate%20Transformations.md) from [cylindrical coordinates](../../Euclidean%20Space/Cylindrical%20Coordinates.md):
>
>$$\mathcal{T}(\rho, \varphi, z) = \begin{bmatrix}\rho \cos \varphi \\ \rho \sin \varphi \\ z\end{bmatrix}$$
>
>Let $\tilde{f} = f \circ \mathcal{T}$ be the [cylindrical coordinate representation](../Cylindrical%20Coordinate%20Representations%20(Real%20Scalar%20Fields).md) of $f$.
>
>If $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\mathcal{T}(\rho, \varphi, z)$, then its [gradient](./Gradient%20(Real%20Scalar%20Fields).md) at $\mathcal{T}(\rho, \varphi, z)$ is expressed in the [normalized local coordinate basis](../../Euclidean%20Space/Local%20Coordinate%20Bases.md) of [cylindrical coordinates](../../Euclidean%20Space/Cylindrical%20Coordinates.md) using the [partial derivatives](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) of $\tilde{f}$ as follows:
>
>$$(\nabla f)(\mathcal{T}(\rho, \varphi, z)) = \partial_{\rho} \tilde{f}(\rho, \varphi, z) \boldsymbol{\hat{\rho}}(\rho, \varphi, z) + \frac{1}{\rho} \partial_{\varphi} \tilde{f}(\rho, \varphi, z) \boldsymbol{\hat{\varphi}}(\rho, \varphi, z) + \partial_z \tilde{f}(\rho, \varphi, z)\boldsymbol{\hat{z}}(\rho, \varphi, z)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Gradient in Spherical Coordinates
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^3 \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\mathcal{T}: (0,+\infty) \times (0,\uppi) \times (0,2\uppi) \to \mathbb{R}^3$ be the  [coordinate transformation](../../Euclidean%20Space/Coordinate%20Transformations.md) from [spherical coordinates](../../Euclidean%20Space/Spherical%20Coordinates.md):
>
>$$\mathcal{T}(r, \theta, \varphi) = \begin{bmatrix}r \sin \theta \cos \varphi \\ r \sin \theta \sin \varphi \\ r \cos \theta\end{bmatrix}$$
>
>Let $\tilde{f} = f \circ \mathcal{T}$ be the [spherical coordinate representation](../Spherical%20Coordinate%20Representations%20(Real%20Scalar%20Fields).md) of $f$.
>
>If $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\mathcal{T}(r, \theta, \varphi)$, then its [gradient](./Gradient%20(Real%20Scalar%20Fields).md) at $\mathcal{T}(r, \theta, \varphi)$ is expressed in the [normalized local coordinate basis](../../Euclidean%20Space/Local%20Coordinate%20Bases.md) of [spherical coordinates](../../Euclidean%20Space/Spherical%20Coordinates.md) using $\tilde{f}$'s [partial derivatives](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) as follows:
>
>$$(\nabla f)(\mathcal{T}(r, \theta, \varphi)) = \partial_r \tilde{f}(r, \theta, \varphi) \boldsymbol{\hat{r}}(r, \theta, \varphi) + \frac{1}{r} \partial_{\theta} \tilde{f}(r, \theta, \varphi)\boldsymbol{\hat{\theta}}(r, \theta, \varphi) + \frac{1}{r \sin \theta} \partial_{\varphi} \tilde{f}(r, \theta, \varphi)\boldsymbol{\hat{\varphi}}(r, \theta, \varphi)$$
>
>>[!EXAMPLE]- Example: $\ln (x^2 + y^2 +z^2)$
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^3 \setminus \boldsymbol{0} \to \mathbb{R}$ defined as follows:
>>
>>$$f(x, y, z) \overset{\text{def}}{=}\ln (x^2 + y^2 + z^2)$$
>>
>>In [spherical coordinates](../../Euclidean%20Space/Spherical%20Coordinates.md), we have:
>>
>>$$\begin{aligned}\tilde{f}(r, \theta, \varphi) & = (f \circ \mathcal{T})(r, \theta, \varphi) \\ & = \ln \left(r^2 \sin^2 \theta \cos^2 \varphi + r^2 \sin^2 \theta \sin^2 \varphi + r^2 \cos^2 \theta \right) \\ & = \ln (r^2 \sin^2 \theta (\cos^2 \varphi + \sin^2 \varphi) + r^2 \cos^2 \theta) \\ & = \ln (r^2 \sin^2 \theta + r^2 \cos^2 \theta) \\ & = \ln (r^2) \\ & = 2 \ln r \end{aligned}$$
>>
>>For its [gradient](./Gradient%20(Real%20Scalar%20Fields).md), we have:
>>
>>$$\begin{aligned}\nabla f(\mathcal{T}(r, \theta, \varphi)) & = \frac{\partial \tilde{f}}{\partial r}(r, \theta, \varphi) \boldsymbol{\hat{r}}(r, \theta, \varphi) + \frac{1}{r} \frac{\partial \tilde{f}}{\partial \theta}(r, \theta, \varphi)\boldsymbol{\hat{\theta}}(r, \theta, \varphi) + \frac{1}{r \sin \theta} \frac{\partial \tilde{f}}{\partial \varphi}(r, \theta, \varphi)\boldsymbol{\hat{\varphi}}(r, \theta, \varphi) \\ & = \frac{2}{r} \cdot \boldsymbol{\hat{r}} + \frac{1}{r} \cdot 0 \cdot \boldsymbol{\hat{\theta}}(r, \theta, \varphi) + \frac{1}{r \sin \theta} \cdot 0 \cdot \boldsymbol{\hat{\varphi}}(r, \theta, \varphi) \\ & = \frac{2}{r} \boldsymbol{\hat{r}}(r, \theta, \varphi) \\ & = \frac{2}{r}\begin{bmatrix} \sin \theta \cos \varphi \\ \sin \theta \sin \varphi \\ \cos \theta \end{bmatrix} \end{aligned}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>