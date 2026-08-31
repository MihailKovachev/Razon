---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Partial Differentiability (Real Vector Functions)

>[!DEFINITION] Definition: Partial Differentiability
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](../Real%20Vector%20Functions.md) and let $\boldsymbol{p}$ and let be an [interior point](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}$.
>
>We say that $f$ is **partially differentiable at** $\boldsymbol{p}$ **w.r.t. the** $k$**-th variable** ($k \in \{1, \dotsc, n\}$) if $f$ is [directionally differentiable](./Directional%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p}$ along the $k$-th [standard basis vector](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $\boldsymbol{e}_k$. 
>
>>[!DEFINITION] Definition: Partial Derivative
>>
>>The corresponding [directional derivative](./Directional%20Differentiability%20(Real%20Vector%20Functions).md) is known as $f$'s **partial derivative at** $\boldsymbol{p}$ **w.r.t.** $k$**-th variable**:
>>
>>$$\lim_{h \to 0} \frac{f(\boldsymbol{p} + h\boldsymbol{e}_k) - f(\boldsymbol{p})}{h}$$
>>
>>>[!NOTATION]
>>>
>>>In general, the [partial derivative](./Partial%20Differentiability%20(Real%20Vector%20Functions).md) of $f$ at $\boldsymbol{p}$ w.r.t. the $k$-th variable is denoted as follows:
>>>
>>>$$\partial_k f(\boldsymbol{p})$$
>>>
>>>If labels (for example $x_1, \dotsc, x_n$) are introduced for the components of $\boldsymbol{p}$, we also use the following notations:
>>>
>>>$$\partial_{x_k}f(x_1, \dotsc, x_n) \qquad \partial_{x_k}f(x_1, \dotsc, x_n) \qquad \frac{\partial f}{\partial x_k}(x_1, \dotsc, x_n)$$
>>>
>>>The labels $x, y$ and $x, y, z$ are very common for $\mathbb{R}^2$ and $\mathbb{R}^3$, respectively.
>>>
>>
>>We also use the term **partial derivative** for each [real vector function](../Real%20Vector%20Functions.md) which maps each $\boldsymbol{p}$ to $f$'s respective [partial derivative](./Partial%20Differentiability%20(Real%20Vector%20Functions).md).
>>
>

>[!THEOREM] Theorem: Partial Differentiability via Component Functions
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](../Real%20Vector%20Functions.md) and let $\boldsymbol{p}$ be an [interior point](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}$.
>
>Then $f$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p}$ w.r.t. the $k$-th variable if and only if all of its [component functions](../Real%20Vector%20Functions.md) $f_1, \dotsc, f_n$ are [partially differentiable](./Partial%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p}$ w.r.t. the $k$-th variable. In this case:
>
>$$\partial_{k} f(\boldsymbol{p}) = \begin{bmatrix} \partial_{k}f_1 (\boldsymbol{p}) \\ \vdots \\ \partial_{k}f_n (\boldsymbol{p})\end{bmatrix}$$
>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Chain Rule for Partial Derivatives
>
>Let $g: \mathcal{D}_g \subseteq \mathbb{R}^l \to \mathbb{R}^m$ and $f: \mathcal{D}_f \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be [real vector functions](../Real%20Vector%20Functions.md) with [component functions](../Real%20Vector%20Functions.md) $g_1, \dotsc, g_m$ and $f_1, \dotsc, f_n$, respectively. Let $\boldsymbol{p}$ be an [interior point](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}_g$ such that $g(\boldsymbol{p})$ is an [interior point](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}_f$.
>
>If $g$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p}$ w.r.t. the $k$-th variable ($k \in \{1, \dotsc, l\}$) and $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at $g(\boldsymbol{p})$, then $f \circ g$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p}$ w.r.t. the $k$-th variable:
>
>$$\partial_k (f \circ g)(\boldsymbol{p}) = \begin{bmatrix} \sum_{j=1}^m \partial_j f_1(g(\boldsymbol{p})) \partial_k g_j(\boldsymbol{p}) \\ \vdots \\ \sum_{j=1}^m \partial_j f_n(g(\boldsymbol{p})) \partial_k g_j(\boldsymbol{p}) \end{bmatrix}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>