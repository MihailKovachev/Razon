---
tags:
    - real-analysis
    - vector-analysis
    - analysis
    - mathematics
---

# Total Differentiability (Real Scalar Fields)

TODO

>[!THEOREM] Theorem: Total Differentiability via Bachmann-Landau
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\boldsymbol{p} \in \operatorname{int} \mathcal{D}$.
>
>Then $f$ is [totally differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p}$ if and only if there exists some [real vector](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $\boldsymbol{v}$ such that $f(\boldsymbol{p} + \boldsymbol{h}) - f(\boldsymbol{p}) - \boldsymbol{v}^{\mathsf{T}}\boldsymbol{h}$ is [little o](../../Asymptotic%20Analysis/Bachmann-Landau%20Notation.md#Little%20o%20Notation) of $||\boldsymbol{h}||$ for $\boldsymbol{h} \to \boldsymbol{0}$:
>
>$$f(\boldsymbol{p} + \boldsymbol{h}) - f(\boldsymbol{p}) - \boldsymbol{v}^{\mathsf{T}}\boldsymbol{h} = o(||\boldsymbol{h}||) \qquad \text{for} \qquad \boldsymbol{h} \to \boldsymbol{0}$$
>
>In this case, $\boldsymbol{v}$ is the [gradient](./Gradient%20(Real%20Scalar%20Fields).md) $\nabla f(\boldsymbol{p})$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuous Partial Differentiability $\implies$ Total Differentiability
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\boldsymbol{p}$ be an [interior point](../../../../Topology/Interior,%20Boundary,%20Exterior.md).
>
>If $f$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) on an [open](../../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) [neighborhood](../../../../Topology/Topological%20Spaces/Topological%20Space.md#Neighborhoods) of $\boldsymbol{p}$ and is [continuously partially differentiable](./Partial%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$, then $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{p}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Mean Value Theorem via Total Differential (Real Scalar Fields)
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\boldsymbol{a}, \boldsymbol{b} \in \mathcal{D}$ such that $L = \{\boldsymbol{a} + t(\boldsymbol{b} - \boldsymbol{a}) \mid t \in [0,1]\} \subseteq \mathcal{D}$.
>
>If $f$ is [continuous](../Continuity%20(Real%20Scalar%20Fields).md) on $L$ and [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) on $\operatorname{int} L$, then there exists some $\boldsymbol{\xi} \in \operatorname{int} L$ such that $f(\boldsymbol{b}) - f(\boldsymbol{a})$ is equal to $f$'s [total differential](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) at $\boldsymbol{\xi}$ applied to $\boldsymbol{b} - \boldsymbol{a}$:
>
>$$f(\boldsymbol{b}) - f(\boldsymbol{a}) = \mathrm{d}f_{\boldsymbol{\xi}}(\boldsymbol{b} - \boldsymbol{a})$$
>
>>[!PROOF]-
>>
>>We define a [real function](../../Real%20Functions/Real%20Functions.md) $g: [0,1] \to \mathbb{R}$ as follows:
>>
>>$$g(t) = f(\boldsymbol{a} + t(\boldsymbol{b} - \boldsymbol{a}))$$
>>
>>Since $f$ is [continuous](../Continuity%20(Real%20Scalar%20Fields).md) on $L$ and the [curve](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\gamma(t) = \boldsymbol{a} + t(\boldsymbol{b} - \boldsymbol{a})$ is [continuous](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Continuity%20(Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable).md) on $[0,1]$, we know that $g$ must be [continuous](../../Real%20Functions/Continuity%20(Real%20Functions).md) on $[0,1]$. Since $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Scalar%20Fields).md) on $\operatorname{int} L$ and $\gamma(t)$ is [differentiable](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) on $(0,1)$, we know that $g$ must be [differentiable](../../Real%20Functions/Differentiability%20(Real%20Functions).md) on $(0,1)$ with the following "[total differential](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md)" due to the [chain rule](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md):
>>
>>$$\mathrm{d}_t g = \mathrm{d}_{\gamma(t)}f \circ \mathrm{d}_t \gamma$$
>>
>>The [total differentials](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) are [functions](../../Real%20Vector%20Functions/Real%20Vector%20Functions.md), specifically, $\mathrm{d}_t g: \mathbb{R} \to \mathbb{R}$, $\mathrm{d}_{\gamma(t)}f: \mathbb{R}^n \to \mathbb{R}$ and $\mathrm{d}_t \gamma: \mathbb{R} \to \mathbb{R}^n$. Therefore, we have
>>
>>$$\mathrm{d}_t g(h) = \mathrm{d}_{\gamma(t)}f (\mathrm{d}_t \gamma(h))$$
>>
>>for all $h \in \mathbb{R}$.
>>
>>The left-hand side can be expressed using $g$'s [derivative](../../Real%20Functions/Differentiability%20(Real%20Functions).md) as $\mathrm{d}_t g(h) = g'(t) h$. The [total differential](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) $\mathrm{d}_t \gamma$ can be express using $\gamma$'s [derivative](../../Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) as $\mathrm{d}_t \gamma(h) = \gamma'(t) h$. Therefore:
>>
>>$$g'(t) h = \mathrm{d}_{\gamma(t)}f (\gamma'(t)h)$$
>>
>>Since $\gamma'(t) = \boldsymbol{b} - \boldsymbol{a}$, we have:
>>
>>$$g'(t) h = \mathrm{d}_{\gamma(t)}f ((\boldsymbol{b} - \boldsymbol{a})h)$$
>>
>>This must hold for $h = 1$ and we get:
>>
>>$$g'(t) = \mathrm{d}_{\gamma(t)}f (\boldsymbol{b} - \boldsymbol{a})$$
>>
>>Since $g$ is [continuous](../../Real%20Functions/Continuity%20(Real%20Functions).md) on $[0,1]$ and [differentiable](../../Real%20Functions/Differentiability%20(Real%20Functions).md) on $(0,1)$, we can use the [mean value theorem](../../Real%20Functions/Differentiability%20(Real%20Functions).md) for $g$. Specifically, there exists some $\xi \in (0,1)$ such that
>>
>>$$g(1) - g(0) = g'(\xi)(1 - 0) = g'(\xi)$$
>>
>>$$g(1) - g(0) = g'(\xi)$$
>>
>>Evaluating $g$ at $1$ and $0$ gives us $g(1) = f(\boldsymbol{b})$ and $g(0) = f(\boldsymbol{a})$. Evaluating $g'(\xi)$ gives us $\mathrm{d}_{\gamma(\xi)}f (\boldsymbol{b} - \boldsymbol{a})$ We thus have:
>>
>>$$f(\boldsymbol{b}) - f(\boldsymbol{a}) = \mathrm{d}_{\gamma(\xi)}f (\boldsymbol{b} - \boldsymbol{a}) = \mathrm{d}f_{\boldsymbol{\xi}} (\boldsymbol{b} - \boldsymbol{a})$$
>>
>>with $\boldsymbol{\xi} = \gamma(\xi)$. Finally, since $\xi \in (0,1)$ and since $\gamma$ is [injective](../../../Functions/Injections,%20Surjections%20and%20Bijections.md), we know that $\boldsymbol{\xi} \in \operatorname{int} L$.
>>
>