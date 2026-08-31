---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Total Differentiability (Real Vector Functions)

>[!DEFINITION] Definition: Total Differentiability of Real Vector Functions
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m\to \mathbb{R}^n$ be a [real vector function](../Real%20Vector%20Functions.md) and let $\boldsymbol{p}$ be an [interior point](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}$.
>
>We say that $f$ is **totally differentiable** at $\boldsymbol{p}$ if there exists a [linear](../../../Functional%20Analysis/Linearity/Linearity%20(Functions).md) [real vector function](../Real%20Vector%20Functions.md) $T_{\boldsymbol{p}}: \mathbb{R}^m \to \mathbb{R}^n$ such that $||f(\boldsymbol{p}+\boldsymbol{h}) - f(\boldsymbol{p}) - T_{\boldsymbol{p}}(\boldsymbol{h})||$ is [little o](../../Asymptotic%20Analysis/Bachmann-Landau%20Notation.md#Little%20o%20Notation) of $||\boldsymbol{h}||$ for $||\boldsymbol{h}|| \to 0$:
>
>$$||f(\boldsymbol{p}+\boldsymbol{h}) - f(\boldsymbol{p}) - T_{\boldsymbol{p}}(\boldsymbol{h})|| = o(||\boldsymbol{h}||) \qquad \text{for} \qquad ||\boldsymbol{h}|| \to 0$$
>
>In this case, $T_{\boldsymbol{p}}$ is known as the **total derivative** or **total differential** of $f$ at $\boldsymbol{p}$. 
>
>>[!NOTATION]
>>
>>We usually denote $T_{\boldsymbol{p}}$ by $\mathrm{d}f_{\boldsymbol{p}}$. When $\boldsymbol{p}$ is clear from context, we can also write just $\mathrm{d}f$.
>>
>
>If $f$ is [differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at every $\boldsymbol{p}$ in some $S \subseteq \mathbb{R}^m$, then we say that $f$ is **totally differentiable on** $S$. If $S = \mathcal{D}$, we can also just say that $f$ is **totally differentiable**. 
>

>[!THEOREM] Theorem: Uniqueness of the Total Derivative
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](../Real%20Vector%20Functions.md) and let $\boldsymbol{p}$ be an [interior point](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}$.
>
>If $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p}$, then its [total derivative](./Total%20Differentiability%20(Real%20Vector%20Functions).md) there is unique.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Total Differentiability via Limits
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](../Real%20Vector%20Functions.md) and let $\boldsymbol{p}$ be an [interior point](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}$.
>
>Then $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p}$ if and only if there exists a [linear](../../../Functional%20Analysis/Linearity/Linearity%20(Functions).md) [real vector function](../Real%20Vector%20Functions.md) $T_{\boldsymbol{p}}: \mathbb{R}^m \to \mathbb{R}^n$ such that the following [limit](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Limits%20(Real%20Scalar%20Fields).md) is zero:
>
>$$\lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{||f(\boldsymbol{x}) - f(\boldsymbol{p}) - T_{\boldsymbol{p}}(\boldsymbol{x} - \boldsymbol{p})||}{||\boldsymbol{x} - \boldsymbol{p}||} = 0$$
>
>In this case, $T_{\boldsymbol{p}}$ is the [total derivative](./Total%20Differentiability%20(Real%20Vector%20Functions).md) of $f$ at $\boldsymbol{p}$.
>
>>[!PROOF]-
>>
>>With the substitution $\boldsymbol{h} = \boldsymbol{x} - \boldsymbol{p}$, we get:
>>
>>$$\lim_{\boldsymbol{x} \to \boldsymbol{p}} \frac{||f(\boldsymbol{x}) - f(\boldsymbol{p}) - T_{\boldsymbol{p}}(\boldsymbol{x} - \boldsymbol{p})||}{||\boldsymbol{x} - \boldsymbol{p}||} = \lim_{\boldsymbol{h} \to \boldsymbol{0}} \frac{||f(\boldsymbol{x} + \boldsymbol{h}) - f(\boldsymbol{p}) - T_{\boldsymbol{p}}(\boldsymbol{h})||}{||\boldsymbol{h}||}$$
>>
>>Since $||\boldsymbol{h}|| \ne 0$ for $\boldsymbol{h} \ne \boldsymbol{0}$, this implies that $||f(\boldsymbol{p}+\boldsymbol{h}) - f(\boldsymbol{p}) - T_{\boldsymbol{p}}(\boldsymbol{h})||$ is [little o](../../Asymptotic%20Analysis/Bachmann-Landau%20Notation.md#Little%20o%20Notation) of $||\boldsymbol{h}||$ for $||\boldsymbol{h}|| \to 0$:
>>
>

>[!THEOREM] Theorem: Total Differentiability via Component Functions
>
>A [real vector function](../Real%20Vector%20Functions.md) $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ is [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p} \in \operatorname{int} \mathcal{D}$ if and only if all of its [component functions](../Real%20Vector%20Functions.md) are [totally differentiable](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Total%20Differentiability%20(Real%20Scalar%20Fields).md) there.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuous Partial Differentiability $\implies$ Total Differentiability
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](../Real%20Vector%20Functions.md), let $\boldsymbol{p}$ be an [interior point](../../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}$.
>
>If $f$ is [partially differentiable](./Partial%20Differentiability%20(Real%20Vector%20Functions).md) on an [open](../../../../Topology/Topological%20Spaces/Topological%20Space.md#Open%20Sets) [neighborhood](../../../../Topology/Topological%20Spaces/Topological%20Space.md#Neighborhood) of $\boldsymbol{p}$ and is [continuously partially differentiable](./Partial%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p}$, then $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Differentiability $\implies$ Continuity
>
>If a [real vector function](../Real%20Vector%20Functions.md) $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ is [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p} \in \operatorname{int} \mathcal{D}$, then it is also [continuous](../Continuity%20(Real%20Vector%20Functions).md) there.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Linearity of Differentiation
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^m \to \mathbb{R}^n$ and $g: \mathcal{D}_g \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be [real vector functions](../Real%20Vector%20Functions.md).
>
>If $f$ and $g$ are [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p} \in \operatorname{int}(\mathcal{D}_f \cap \mathcal{D}_g)$, then so is $\lambda f + \mu g$ for all $\lambda, \mu \in \mathbb{R}$:
>
>$$\mathop{\mathrm{d}(\lambda f + \mu g)_{\boldsymbol{p}}} = \lambda \mathop{\mathrm{d}f_{\boldsymbol{p}}} + \mu \mathop{\mathrm{d}g_{\boldsymbol{p}}}$$
>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Chain Rule
>
>Let $g: \mathcal{D}_g \subseteq \mathbb{R}^m \to \mathbb{R}^n$ and $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}^p$  be [real vector functions](../Real%20Vector%20Functions.md).
>
>If $g$ is [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p} \in \operatorname{int} \mathcal{D}_g$ and $f$ is [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at $g(\boldsymbol{p}) \in \operatorname{int} \mathcal{D}_f$, then $f \circ g$ is [totally differentiable](./Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{p}$:
>
>$$\mathrm{d}(f\circ g)_{\boldsymbol{p}} = \mathrm{d}f_{g(\boldsymbol{p})} \circ \mathrm{d}g_{\boldsymbol{p}}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>