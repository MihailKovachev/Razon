---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Limits (Real Scalar Fields)

In the case of [real scalar fields](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md), the definition of a [limit](../Real%20Vector%20Functions/Limits%20(Real%20Vector%20Functions).md) reduces to the following.

>[!DEFINITION] Definition: Limit of a Real Scalar Field
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\mathbf{a} \in \mathbb{R}^n$ be an [accumulation point](../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}$.
>
>A [numbers](../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) $L \in \mathbb{R}$ is the  [limit](../Real%20Vector%20Functions/Limits%20(Real%20Vector%20Functions).md) of $f$ for $\mathbf{x} \to \mathbf{a}$ if and only if for each $\varepsilon \gt 0$ there exists some [open ball](../Euclidean%20Space/Euclidean%20Space.md) $B_{\delta}(\mathbf{a})$ around $\mathbf{a}$ such that for all $\mathbf{x} \in \mathcal{D}$ different from $\mathbf{a}$, 
>
>$$
>\mathbf{x} \in B_{\delta}(\mathbf{a}) \implies |f(\mathbf{x}) - L| \lt \varepsilon
>$$
>
>>[!NOTATION]
>>
>>$$
>>\lim_{\mathbf{x}\to \mathbf{a}} f(\mathbf{x}) = L
>>$$
>>
>

>[!THEOREM] Theorem: Heine Definition of Convergence
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\mathbf{p} \in \mathbb{R}^n$ be an [accumulation point](../../../Topology/Accumulation%20Points.md) of $\mathcal{D}_f$.
>
>The [limit](../Real%20Vector%20Functions/Limits%20(Real%20Vector%20Functions).md) of $f$ at $\mathbf{p}$ is $L \in \mathbb{R}$ if and only if for each [real vector sequence](../Real%20Vector%20Sequences.md) $(\mathbf{x}_k)_{k \in \mathcal{I}}$ in $\mathcal{D}_f \setminus \{\mathbf{p}\}$ which [converges](../Real%20Vector%20Sequences.md#Convergence) to $\mathbf{p}$, the [sequence](../Real%20Vector%20Sequences.md) $(f(\mathbf{x}_k))_{k \in \mathcal{I}}$ [converges](../Real%20Vector%20Sequences.md#Convergence) to $L$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Algebraic Properties
>
>Let $f, g: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be [real scalar fields](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md).
>
>If the [limits](./Limits%20(Real%20Scalar%20Fields).md) of $f$ and $g$ for $\mathbf{x} \to \mathbf{a}$ exist, then
>
>$$
>\lim_{\mathbf{x} \to \mathbf{a}} [f(\mathbf{x}) g(\mathbf{x})] = \left(\lim_{\mathbf{x} \to \mathbf{a}} f(\mathbf{x}) \right) \cdot \left( \lim_{\mathbf{x} \to \mathbf{a}} g(\mathbf{x}) \right)
>$$
>
>Furthermore, if $g(\mathbf{x}) \ne 0$ for all $\mathbf{x} \in \mathcal{D}$ and $\displaystyle \lim_{\mathbf{x} \to \mathbf{a}} g(\mathbf{x}) \ne 0$, then
>
>$$
>\lim_{ \mathbf{x} \to \mathbf{a} } \frac{ f(\mathbf{x}) }{ g(\mathbf{x}) } = \frac{ \displaystyle \lim_{ \mathbf{x} \to \mathbf{a} } f(\mathbf{x}) }{ \displaystyle \lim_{ \mathbf{x} \to \mathbf{a} } g(\mathbf{x}) }
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Squeeze Theorem
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$, $g: \mathcal{D}_g \subseteq \mathbb{R}^n \to \mathbb{R}$ and $h: \mathcal{D}_h \subseteq \mathbb{R}^n \to \mathbb{R}$ be [real scalar fields](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\boldsymbol{p} \in \mathbb{R}^n$.
>
>If there exists some [deleted neighborhood](../Euclidean%20Space/Euclidean%20Space.md) of $\boldsymbol{p}$ on which $f(\boldsymbol{x}) \le h(\boldsymbol{x}) \le g(\boldsymbol{x})$ and the [limits](./Limits%20(Real%20Scalar%20Fields).md) of $f$ and $g$ at $\boldsymbol{p}$ are both equal to $L \in \mathbb{R}$, then the [limit](./Limits%20(Real%20Scalar%20Fields).md) of $h$ at $\boldsymbol{p}$ is also $L$:
>
>>[!PROOF]-
>>
>>TODO
>>
>