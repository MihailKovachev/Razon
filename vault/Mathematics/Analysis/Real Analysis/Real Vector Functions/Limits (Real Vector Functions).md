---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Limits (Real Vector Functions)

>[!DEFINITION] Definition: Limit (Real Vector Functions)
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be a [real vector function](./Real%20Vector%20Functions.md) and let $\boldsymbol{p}$ be a [limit point](../../../Topology/Accumulation%20Points.md) of $\mathcal{D}$.
>
>We say that $\boldsymbol{L} \in \mathbb{R}^n$ is the **limit** of $f$ at $\boldsymbol{p}$ if for each $\varepsilon \gt 0$, there exists some $\delta \gt 0$ such that for all $\boldsymbol{x} \in \mathcal{D}$, we have the following:
>
>$$0 \lt ||\boldsymbol{x} - \boldsymbol{p}||_{\mathbb{R}^m} \lt \delta \implies ||f(\boldsymbol{x}) - \boldsymbol{L}||_{\mathbb{R}^n} \lt \varepsilon$$
>
>>[!NOTATION]
>>
>>$$\lim_{x \to \boldsymbol{p}} f(\boldsymbol{x}) = \boldsymbol{L}$$
>>
>

>[!THEOREM] Theorem: Limit via Component Functions
>
>The [limit](./Limits%20(Real%20Vector%20Functions).md) of a [real vector function](./Real%20Vector%20Functions.md) $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ at an [accumulation point](../../../Topology/Accumulation%20Points.md) $\boldsymbol{p}$ of $\mathcal{D}$ is $\boldsymbol{L} = \begin{bmatrix}L_1 & \cdots & L_n\end{bmatrix}^{\mathsf{T}} \in \mathbb{R}^n$ if and only if the [limits](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Limits%20(Real%20Scalar%20Fields).md) of its [component functions](./Real%20Vector%20Functions.md) $f_1, \dotsc, f_n$ are $L_1, \dotsc, L_n$, respectively:
>
>$$\lim_{\boldsymbol{x}\to \boldsymbol{p}} f(\boldsymbol{x}) = \boldsymbol{L} \iff \lim_{\boldsymbol{x}\to \boldsymbol{p}} f_k(\boldsymbol{x}) = L_k \qquad \forall k \in \{1,\dotsc,n\}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Linearity of the Limit Operator
>
>If $f, g: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ have [limits](./Limits%20(Real%20Vector%20Functions).md) for $\mathbf{x} \to \mathbf{p}$, then for all $\lambda, \mu \in \mathbb{R}$:
>
>$$\lim_{\mathbf{x} \to \mathbf{p}} [\lambda f(\mathbf{x}) + \mu g(\mathbf{x})] = \lambda \lim_{\mathbf{x} \to \mathbf{p}} f(\mathbf{x}) + \mu \lim_{\mathbf{x} \to \mathbf{p}} g(\mathbf{x})$$
>
>>[!PROOF]-
>>
>>TODO
>>
>