---
tags:
    - real-analysis
    - vector-analysis
    - analysis
    - mathematics
---

# Laplacian (Real Vector Fields)

>[!DEFINITION] Definition: Laplacian (Real Vector Field)
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [real vector field](../Real%20Vector%20Fields.md) and let $\boldsymbol{x}$ be an [interior point](../../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $\mathcal{D}$ (in the [Euclidean topology](../../Euclidean%20Space/Euclidean%20Space.md)) such that $f$ is [totally differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{x}$.
>
>The **Laplacian** of $f$ at $\boldsymbol{x}$ is the difference between the [gradient](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Gradient%20(Real%20Scalar%20Fields).md) of the [divergence](./Divergence%20(Real%20Vector%20Fields).md) of $f$ and the [curl](./Curl%20(Real%20Vector%20Fields).md) of $f$'s [curl](./Curl%20(Real%20Vector%20Fields).md) there:
>
>$$\operatorname{grad} \operatorname{div} f(\boldsymbol{x}) - \operatorname{curl} \operatorname{curl} f(\boldsymbol{x})$$
>
>>[!NOTATION]
>>
>>$$\nabla^2 f(\boldsymbol{x}) \qquad \Delta f(\boldsymbol{x})$$
>>
>

>[!THEOREM] Theorem: Laplacian as Component-Wise Scalar Laplacian
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [real vector field](../Real%20Vector%20Fields.md) and let $\boldsymbol{x}$ be an [interior point](../../../../Topology/Topological%20Spaces/Interior%20(Topology).md) of $\mathcal{D}$ (in the [Euclidean topology](../../Euclidean%20Space/Euclidean%20Space.md)) such that $f$ is [totally differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\boldsymbol{x}$ and let $f_1, f_2, f_3$ be the [component functions](../../Real%20Vector-Valued%20Functions.md) of $f$.
>
>The components of the [Laplacian](./Laplacian%20(Real%20Vector%20Fields).md) of $f$ are the [Laplacians](../../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Differentiation/Laplacian%20(Real%20Scalar%20Fields).md) of $f_1, f_2, f_3$, respectively:
>
>$$\nabla^2 f(\boldsymbol{x}) = \begin{bmatrix} \nabla^2 f_1 (\boldsymbol{x}) \\ \nabla^2 f_2 (\boldsymbol{x}) \\ \nabla^2 f_3(\boldsymbol{x})\end{bmatrix}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>