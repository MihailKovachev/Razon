---
tags:
    - complex-analysis
    - real-analysis
    - analysis
    - mathematics
---

# Partial Differentiability (Complex-Valued Functions of Multiple Real Variables)

>[!DEFINITION] Definition: Partial Differentiability (Real Scalar Fields)
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{C}$ be a [complex-valued functions of multiple real variables](./Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables.md), let $\boldsymbol{p} \in \mathcal{D}$ and let $k \in \{1, \dotsc, n\}$.
>
>We say that $f$ is **partially differentiable at $\boldsymbol{p}$ with respect to the $k$-th variable** if $f$ is [directionally differentiable](./Directional%20Differentiability%20(Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables).md) at $\boldsymbol{p}$ along the $k$-th [standard basis vector](../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $\boldsymbol{e}_k$. In this case, the corresponding [directional derivative](./Directional%20Differentiability%20(Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables).md) is known as $f$'s **partial derivative at $\boldsymbol{p}$ with respect to the $k$-th variable**.
>
>We say that $f$ is **partially differentiable at** $\boldsymbol{p}$ if $f$ is [partially differentiable](#Partial%20Differentiability%20(Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables)) at $\boldsymbol{p}$ with respect to all variables.
>
>Let $S \subseteq \mathcal{D}$.
>
>We say that $f$ is **partially differentiable on $S$ with respect to the $k$-th variable** if $f$ is [partially differentiable](#Partial%20Differentiability%20(Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables)) w.r.t. $k$-th variable at each $\boldsymbol{x} \in S$.
>
>We say that $f$ is **partially differentiable on $S$** if $f$ is [partially differentiable](#Partial%20Differentiability%20(Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables)) w.r.t. to all variables at each $\boldsymbol{x} \in S$.
>
>>[!NOTATION]
>>
>>In general, the [partial derivative](#Partial%20Differentiability%20(Complex-Valued%20Functions%20of%20Multiple%20Real%20Variables)) of $f$ at $\boldsymbol{p}$ w.r.t. the $k$-th variable is denoted as follows:
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
>>[!DEFINITION] Definition: Continuous Partial Differentiability
>>
>>We say that $f$ is **continuously partially differentiable at** $\boldsymbol{p}$ **w.r.t. the** $k$**-th  variable** if its respective [partial derivative](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) there is [continuous](../Continuity%20(Real%20Scalar%20Fields).md). If $k$ is not specified, then we assume it holds for all $k \in \{1, \dotsc, n\}$ and similarly for $\boldsymbol{p}$.
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
>The **$m$-th order partial derivative function** of $f$ **with respect to $(k_1, \dotsc, k_m)$** is the [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $\partial_{k_m} \cdots \partial_{k_1} f: \mathcal{D}_{k_1, \dotsc, k_m} \to \mathbb{R}$ whose [domain](../../../Functions/Functions.md) is the [set](../../../Set%20Theory/Sets.md) of all $\boldsymbol{x} \in \mathcal{D}$ at which $f$ is [partially differentiable](#Higher%20Order%20Partial%20Differentiability) w.r.t. $(k_1, \dotsc, k_m)$ and which maps each $\boldsymbol{x} \in \mathcal{D}_{k_1,\dotsc,k_m}$ to $f$'s [$m$-th order partial derivative](#Higher%20Order%20Partial%20Differentiability) w.r.t. $(k_1, \dotsc, k_m)$ at $\boldsymbol{x}$.
>
>We say that $f$ is **$m$-times partially differentiable at** $\boldsymbol{p}$ if $f$ is [partially differentiable](#Higher%20Order%20Partial%20Differentiability) at $\boldsymbol{p}$ w.r.t. to all $(k_1, \dotsc, k_m) \in \{1, \dotsc, n\}^m$. 
>
>We say that $f$ is **$m$-times partially differentiable on** $S \subseteq \mathcal{D}$ if $f$ is [partially differentiable](#Higher%20Order%20Partial%20Differentiability) on $S$ w.r.t. to all $(k_1, \dotsc, k_m) \in \{1, \dotsc, n\}^m$.
>

>[!THEOREM] Young's Theorem: Symmetry of Second-Order Partial Derivatives
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md), let $\boldsymbol{x} \in \operatorname{int} \mathcal{D}$ be an [interior point](../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $\mathcal{D}$ and let $i, j \in \{1, \dotsc, n\}$.
>
>If the [partial derivatives](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) $\partial_i f$ and $\partial_j f$ exist on a [neighborhood](../../../Topology/Topological%20Spaces/Neighborhoods.md) of $\boldsymbol{x}$ and are [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{x}$, then $\partial_i \partial_j f$ and $\partial_j \partial_i f$ are equal at $\boldsymbol{x}$: 
>
>$$\partial_i \partial_j f(\boldsymbol{x}) = \partial_j \partial_i f(\boldsymbol{x})$$
>
>>[!PROOF]-
>>
>>TODO
>>
>