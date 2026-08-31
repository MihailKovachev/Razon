---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Continuity (Real Scalar Fields)

In the case of [real scalar fields](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md), the definition of [continuity](../Real%20Vector%20Functions/Continuity%20(Real%20Vector%20Functions).md) reduces to the following.

>[!THEOREM] Theorem: Continuity of Real Scalar Fields
>
>A [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ is [continuous](../Real%20Vector%20Functions/Continuity%20(Real%20Vector%20Functions).md) at $\mathbf{p} \in \mathcal{D}$ if and only if its [limit](./Limits%20(Real%20Scalar%20Fields).md) at $\mathbf{p}$ is $f(\mathbf{p})$ or $\mathbf{p}$ is an [isolated point](../../../Topology/Isolated%20Points.md) of $\mathcal{D}$:
>
>$$\lim_{\boldsymbol{x} \to \mathbf{p}} f(\boldsymbol{x}) = f(\mathbf{p})$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!EXAMPLE]- Example: $f(\boldsymbol{x}) = \mathbf{a}^{\mathsf{T}} \boldsymbol{x}$
>
>Consider the [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^n \to \mathbb{R}$ defined as
>
>$$f(\boldsymbol{x}) = \mathbf{a}^{\mathsf{T}} \boldsymbol{x},$$
>
>where $\mathbf{a} \in \mathbb{R}^n$ is some fixed [real vector](../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md).
>
>It is [continuous](./Continuity%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^n$.
>

>[!EXAMPLE]- Example: $f(\boldsymbol{x}) = \boldsymbol{x}^{\mathsf{T}} A\boldsymbol{x}$
>
>Consider the [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^n \to \mathbb{R}$ defined as
>
>$$f(\boldsymbol{x}) = \boldsymbol{x}^{\mathsf{T}} A\boldsymbol{x},$$
>
>where $A \in \mathbb{R}^{n \times n}$ is some fixed [real matrix](../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md).
>
>It is [continuous](./Continuity%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^n$.
>

>[!EXAMPLE]-
>
>Consider the [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f: \mathbb{R}^2 \to \mathbb{R}$ defined as follows:
>
>$$f(x, y) = \begin{cases}\frac{2xy}{x^2 + y^2} & \text{if} & \begin{bmatrix}x & y\end{bmatrix}^{\mathsf{T}} \ne \mathbf{0} \\ 2 & \text{if} & \begin{bmatrix}x & y\end{bmatrix}^{\mathsf{T}} = \mathbf{0} \end{cases}$$
>
>It is [continuous](./Continuity%20(Real%20Scalar%20Fields).md) on $\mathbb{R}^2 \setminus \{\mathbf{0}\}$. To see this, we examine the following [sequence](../Real%20Vector%20Sequences.md) $(\mathbf{z}_k)_{k \in \mathbb{N}}$:
>
>$$\mathbf{z}_k = \begin{bmatrix}\frac{1}{k} \\ \frac{1}{k}\end{bmatrix}$$
>
>For $k \to \infty$, we see that $(\mathbf{z}_k)_{k \in \mathbb{N}}$ [converges](../Real%20Vector%20Sequences.md#Convergence) to $\mathbf{0}$:
>
>$$\lim_{k \to \infty} \mathbf{z}_k = \lim_{k \to \infty} \begin{bmatrix}\frac{1}{k} \\ \frac{1}{k}\end{bmatrix} = \begin{bmatrix}0 \\ 0\end{bmatrix}$$
>
>The [sequence](../Real%20Vector%20Sequences.md) $(f(\mathbf{z}_k))_{k \in \mathbb{N}}$ [converges](../Real%20Vector%20Sequences.md#Convergence) to $1$:
>
>$$\lim_{k \to \infty} f(\mathbf{z}_k) = \lim_{k \to \infty} \frac{2 \times \frac{1}{k} \times \frac{1}{k}}{\left(\frac{1}{k}\right)^2 + \left(\frac{1}{k}\right)^2} = \lim_{k \to \infty} \frac{\frac{2}{k^2}}{\frac{2}{k^2}} = 1 \ne 2$$
>
>This means that the [limit](./Limits%20(Real%20Scalar%20Fields).md) of $f$ at $\mathbf{0}$ cannot be $2$ and so $f$ cannot be [continuous](./Continuity%20(Real%20Scalar%20Fields).md) there.
>

>[!THEOREM] Theorem: Continuity of Sums, Products and Quotients
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ and let $g: \mathcal{D}_g \subseteq \mathbb{R}^n \to \mathbb{R}$ be [real scalar fields](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md).
>
>If $f$ and $g$ are [continuous](./Continuity%20(Real%20Scalar%20Fields).md) on $S \subseteq \mathcal{D}_f \cap \mathcal{D}_g$, then:
>
>- $\lambda f + \mu g$ is also [continuous](./Continuity%20(Real%20Scalar%20Fields).md) on $S$ for all $\lambda, \mu \in \mathbb{R}$.
>- $fg$ is also [continuous](./Continuity%20(Real%20Scalar%20Fields).md) on $S$.
>- $f / g$ is also [continuous](./Continuity%20(Real%20Scalar%20Fields).md) on $S$ provided that $g(\boldsymbol{x}) \ne 0$ for all $\boldsymbol{x} \in S$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] The Extreme Value Theorem for Real Scalar Fields
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](./Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md).
>
>If $f$ is [continuous](./Continuity%20(Real%20Scalar%20Fields).md) on $S \subseteq \mathcal{D}$ and $S$ is [compact](../../../Topology/Compactness.md), then there exist at least one $\mathbf{x}_{\text{of min}} \in S$ and at least one $\mathbf{x}_{\text{of max}} \in S$ such that
>
>$$f(\mathbf{x}_{\text{of min}}) \le f(\boldsymbol{x}) \le f(\mathbf{x}_{\text{of max}})$$
>
>for all $\boldsymbol{x} \in S$.
>
>>[!PROOF]-
>>
>>TODO
>>
>