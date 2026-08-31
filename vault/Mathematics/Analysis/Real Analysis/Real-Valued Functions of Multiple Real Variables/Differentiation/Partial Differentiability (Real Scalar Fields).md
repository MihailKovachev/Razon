---
tags:
    - real-analysis
    - vector-analysis
    - analysis
    - mathematics
---

# Partial Differentiability (Real Scalar Fields)

>[!DEFINITION] Definition: Partial Differentiability (Real Scalar Fields)
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md), let $\boldsymbol{p} \in \mathcal{D}$ and let $k \in \{1, \dotsc, n\}$.
>
>We say that $f$ is **partially differentiable at $\boldsymbol{p}$ with respect to the $k$-th variable** if $f$ is [directionally differentiable](./Directional%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$ along the $k$-th [standard basis vector](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $\boldsymbol{e}_k$. In this case, the corresponding [directional derivative](./Directional%20Differentiability%20(Real%20Scalar%20Fields).md) is known as $f$'s **partial derivative at $\boldsymbol{p}$ with respect to the $k$-th variable**.
>
>We say that $f$ is **partially differentiable at** $\boldsymbol{p}$ if $f$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$ with respect to all variables.
>
>Let $S \subseteq \mathcal{D}$.
>
>We say that $f$ is **partially differentiable on $S$ with respect to the $k$-th variable** if $f$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) w.r.t. $k$-th variable at each $\boldsymbol{x} \in S$.
>
>We say that $f$ is **partially differentiable on $S$** if $f$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) w.r.t. to all variables at each $\boldsymbol{x} \in S$.
>
>>[!NOTATION]
>>
>>In general, the [partial derivative](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) of $f$ at $\boldsymbol{p}$ w.r.t. the $k$-th variable is denoted as follows:
>>
>>$$\partial_k f(\boldsymbol{p})$$
>>
>>If labels (for example $x_1, \dotsc, x_n$) are introduced for the components of $\boldsymbol{p}$, we also use the following notations:
>>
>>$$\partial_{x_k}f(x_1, \dotsc, x_n) \qquad \partial_{x_k}f(x_1, \dotsc, x_n) \qquad \frac{\partial f}{\partial x_k}(x_1, \dotsc, x_n)$$
>>
>>The labels $x, y$ and $x, y, z$ are very common for $\mathbb{R}^2$ and $\mathbb{R}^3$, respectively.
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
>>$$\frac{\partial f}{\partial x} \left(x, y)\right) = 2x y^3 + 1 \qquad \frac{\partial f}{\partial y} \left(x, y\right) = 3 x^2 y^2$$
>>
>
>>[!EXAMPLE]- Example: $f(\boldsymbol{x}) = \boldsymbol{a}^{\mathsf{T}}\boldsymbol{x}$
>>
>>Consider the [real scalar ield](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^n \to \mathbb{R}$ defined as
>>
>>$$f(\boldsymbol{x}) = \boldsymbol{a}^{\mathsf{T}}\boldsymbol{x}$$
>>
>>for some fixed [real vector](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $\boldsymbol{a} = \begin{bmatrix} a_1 & \cdots & a_n \end{bmatrix}^{\mathsf{T}}\in \mathbb{R}^n$.
>>
>>It is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^n$:
>>
>>$$\partial_k f(\boldsymbol{x})= a_k$$
>>
>
>>[!EXAMPLE]- Example: $f(\boldsymbol{x}) = \boldsymbol{x}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{x}$
>>
>>Consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^n \to \mathbb{R}$ defined as
>>
>>$$f(\boldsymbol{x}) = \boldsymbol{x}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{x}$$
>>
>>for some [real matrix](../../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) $\boldsymbol{A} \in \mathbb{R}^{n \times n}$.
>>
>>For its [directional derivative](./Directional%20Differentiability%20(Real%20Scalar%20Fields).md) along the $k$-th [standard basis vector](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $\boldsymbol{e}_k$, we have:
>>
>>$$\begin{aligned}\frac{\partial f}{\partial \boldsymbol{e}_k} (\boldsymbol{x}) & = \lim_{h \to 0} \frac{f(\boldsymbol{x} + h\boldsymbol{e}_k) - f(\boldsymbol{x})}{h} \\ & = \lim_{h \to 0} \frac{(\boldsymbol{x} + h\boldsymbol{e}_k)^{\mathsf{T}}\boldsymbol{A}(\boldsymbol{x} + h\boldsymbol{e}_k) - \boldsymbol{x}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{x}}{h} \\ & = \lim_{h \to 0}\frac{(\boldsymbol{x}^{\mathsf{T}}+ h\boldsymbol{e}_k^{\mathsf{T}})(\boldsymbol{A}\boldsymbol{x} + h\boldsymbol{A}\boldsymbol{e}_k) - \boldsymbol{x}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{x}}{h} \\ & = \lim_{h \to 0} \frac{ \boldsymbol{x}^{\mathsf{T}} \boldsymbol{A}\boldsymbol{x} + h\boldsymbol{x}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{e}_k + h\boldsymbol{e}_k^{\mathsf{T}}\boldsymbol{A}\boldsymbol{x} + h^2 \boldsymbol{e}_k^{\mathsf{T}} \boldsymbol{A} \boldsymbol{e}_k - \boldsymbol{x}^{\mathsf{T}} \boldsymbol{A} \boldsymbol{x}}{h} \\ & = \lim_{h \to 0} \frac{h\boldsymbol{x}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{e}_k + h\boldsymbol{e}_k^{\mathsf{T}}\boldsymbol{A}\boldsymbol{x} + h^2 \boldsymbol{e}_k^{\mathsf{T}} \boldsymbol{A} \boldsymbol{e}_k}{h} \\ & = \lim_{h \to 0} \boldsymbol{x}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{e}_k + \boldsymbol{e}_k^{\mathsf{T}}\boldsymbol{A}\boldsymbol{x} + h \boldsymbol{e}_k^{\mathsf{T}} \boldsymbol{A} \boldsymbol{e}_k \\ & = \boldsymbol{x}^{\mathsf{T}}\boldsymbol{A}\boldsymbol{e}_k + \boldsymbol{e}_k^{\mathsf{T}}\boldsymbol{A}\boldsymbol{x} \\ & = (\boldsymbol{e}_k^{\mathsf{T}}\boldsymbol{A}^{\mathsf{T}}\boldsymbol{x})^{\mathsf{T}} + \boldsymbol{e}_k^{\mathsf{T}}\boldsymbol{A}\boldsymbol{x} \\ & = \boldsymbol{e}_k^{\mathsf{T}}\boldsymbol{A}^{\mathsf{T}}\boldsymbol{x} + \boldsymbol{e}_k^{\mathsf{T}}\boldsymbol{A}\boldsymbol{x} \\ & = \boldsymbol{e}_k^{\mathsf{T}}(\boldsymbol{A}^{\mathsf{T}} + \boldsymbol{A})\boldsymbol{x}\end{aligned}$$
>>
>>Therefore, $f$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md):
>>
>>$$\partial_k f(\boldsymbol{x}) = \boldsymbol{e}_k^{\mathsf{T}}(\boldsymbol{A}^{\mathsf{T}} + \boldsymbol{A})\boldsymbol{x}$$
>>
>>
>
>>[!DEFINITION] Definition: Continuous Partial Differentiability
>>
>>We say that $f$ is **continuously partially differentiable at** $\boldsymbol{p}$ **w.r.t. the** $k$**-th  variable** if its respective [partial derivative](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) there is [continuous](../Continuity%20(Real%20Scalar%20Fields).md). If $k$ is not specified, then we assume it holds for all $k \in \{1, \dotsc, n\}$ and similarly for $\boldsymbol{p}$.
>>
>

>[!THEOREM] Theorem: Chain Rule for Partial Derivatives
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](../../Real%20Functions/Real%20Functions.md), let $g: \mathcal{D}_g \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\boldsymbol{p}$ be an [interior point](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}_g$ such that $g(\boldsymbol{p})$ is an [interior point](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}_f$.
>
>If $g$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$ w.r.t. the $k$-th variable and $f$ is [differentiable](../../Real%20Functions/Differentiability%20(Real%20Functions).md) at $g(\boldsymbol{p})$, then the [composition](../../../Functions/Functions.md) $f\circ g$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$ w.r.t. the $k$-th variable:
>
>$$\partial_k (f\circ g)(\boldsymbol{p}) = f'(g(\boldsymbol{p})) \partial_k g(\boldsymbol{p})$$
>
>>[!EXAMPLE]-
>>
>>Let $f: \mathbb{R}_{\gt 0} \to \mathbb{R}$ be a [real function](../../Real%20Functions/Real%20Functions.md) which is [differentiable](../../Real%20Functions/Differentiability%20(Real%20Functions).md) on $\mathbb{R}_{\gt 0}$ and consider the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f(||\boldsymbol{x}||)$.
>>
>>We have:
>>
>>$$f(||\boldsymbol{x}||) = f\left(\sqrt{\sum_{i=1}^n x_i^2}\right)$$
>>
>>For the [partial derivative](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) of $\sqrt{\sum_{i=1}^n x_i^2}$ w.r.t. to the $k$-th variable, we have the following:
>>
>>$$\begin{aligned}\partial_k \sqrt{\sum_{i=1}^n x_i^2} = \frac{2 x_k}{2\sqrt{\sum_{i=1}^n x_i^2}} = \frac{x_k}{||\boldsymbol{x}||}\end{aligned}$$
>>
>>Since $f$ is [differentiable](../../Real%20Functions/Differentiability%20(Real%20Functions).md) on $\mathbb{R}_{\gt 0}$, we know that $f(||\boldsymbol{x}||)$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^n \setminus \{\boldsymbol{0}\}$ and for all $k \in \{1, \dotsc, n\}$ its [partial derivatives](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) are the following:
>>
>>$$\begin{aligned}\partial_k f(||\boldsymbol{x}||) = f'(||\boldsymbol{x}||) \frac{x_k}{||\boldsymbol{x}||}\end{aligned}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Higher Order Partial Differentiability

>[!DEFINITION] Definition: Higher Order Partial Differentiability (Real Scalar Fields)
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $m \in \mathbb{N}_{\ge 0}$.
>
>For $m = 0$: We say that $f$ is **0-times partially differentiable at** each $\boldsymbol{p} \in \mathcal{D}$ and **0-times partially differentiable on** each $S \subseteq \mathcal{D}$. The **0-th order partial derivative function** of $f$ is $f$ itself.
>
>For $m \ge 1$:
>
>Let $(k_1, \dotsc, k_m) \in \{1, \dotsc, n\}^m$. We say that $f$ is **partially differentiable with respect to $(k_1, \dotsc, k_m)$** if $f$'s [partial derivative function](#Higher%20Order%20Partial%20Differentiability) $\partial_{k_{m-1}} \cdots \partial_{k_1} f: \mathcal{D}_{k_1, \dotsc, k_{m-1}} \to \mathbb{R}$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$ with respect to the $k_m$-th variable. In this case, the [partial derivative](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) $\partial_{k_m}(\partial_{k_{m-1}} \cdots \partial_{k_1} f)(\boldsymbol{p})$ is known as $f$'s **$m$-th order partial derivative at $\boldsymbol{p}$ with respect to $(k_1, \dotsc, k_m)$**.
>
>For $S \subseteq \mathcal{D}$, we say that $f$ is **partially differentiable on $S$ with respect to $(k_1, \dotsc, k_m)$** if $f$ is [partially differentiable](#Higher%20Order%20Partial%20Differentiability) w.r.t. $(k_1, \dotsc, k_m)$ at each $\boldsymbol{x} \in S$.
>
>The **$m$-th order partial derivative function** of $f$ **with respect to $(k_1, \dotsc, k_m)$** is the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $\partial_{k_m} \cdots \partial_{k_1} f: \mathcal{D}_{k_1, \dotsc, k_m} \to \mathbb{R}$ whose [domain](../../../Functions/Functions.md) is the [set](../../../../Set%20Theory/Sets.md) of all $\boldsymbol{x} \in \mathcal{D}$ at which $f$ is [partially differentiable](#Higher%20Order%20Partial%20Differentiability) w.r.t. $(k_1, \dotsc, k_m)$ and which maps each $\boldsymbol{x} \in \mathcal{D}_{k_1,\dotsc,k_m}$ to $f$'s [$m$-th order partial derivative](#Higher%20Order%20Partial%20Differentiability) w.r.t. $(k_1, \dotsc, k_m)$ at $\boldsymbol{x}$.
>
>We say that $f$ is **$m$-times partially differentiable at** $\boldsymbol{p}$ if $f$ is [partially differentiable](#Higher%20Order%20Partial%20Differentiability) at $\boldsymbol{p}$ w.r.t. to all $(k_1, \dotsc, k_m) \in \{1, \dotsc, n\}^m$. 
>
>We say that $f$ is **$m$-times partially differentiable on** $S \subseteq \mathcal{D}$ if $f$ is [partially differentiable](#Higher%20Order%20Partial%20Differentiability) on $S$ w.r.t. to all $(k_1, \dotsc, k_m) \in \{1, \dotsc, n\}^m$.
>

>[!THEOREM] Young's Theorem: Symmetry of Second-Order Partial Derivatives
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md), let $\boldsymbol{x} \in \operatorname{int} \mathcal{D}$ be an [interior point](../../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $\mathcal{D}$ and let $i, j \in \{1, \dotsc, n\}$.
>
>If the [partial derivatives](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) $\partial_i f$ and $\partial_j f$ exist on a [neighborhood](../../../../Topology/Topological%20Spaces/Neighborhoods.md) of $\boldsymbol{x}$ and are [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{x}$, then $\partial_i \partial_j f$ and $\partial_j \partial_i f$ are equal at $\boldsymbol{x}$: 
>
>$$\partial_i \partial_j f(\boldsymbol{x}) = \partial_j \partial_i f(\boldsymbol{x})$$
>
>>[!PROOF]-
>>
>>TODO
>>
>