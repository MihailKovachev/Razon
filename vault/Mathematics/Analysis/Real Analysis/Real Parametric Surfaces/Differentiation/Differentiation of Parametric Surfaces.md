---
title: Smoothness of Parametric Surfaces
tags:
  - real-analysis
  - vector-analysis
  - mathematical-analysis
  - mathematics
---

# Tangent Space

>[!DEFINITION] Definition: Tangent Space
>
>Let $S: \mathcal{D} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ be a [parametric surface](../Real%20Parametric%20Surfaces.md) which is [differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\mathbf{a} \in \mathcal{D}$.
>
>The **tangent space** of $S$ at $\mathbf{a}$ is the [span](../../../../Algebra/Vector%20Spaces/Linear%20Combinations.md#Span) of its [partial derivatives](../../Real%20Vector%20Fields/Differentiation%20of%20Real%20Vector%20Fields.md) at $\mathbf{a}$ with respect to [Cartesian coordinates](../../Euclidean%20Space/Cartesian%20Coordinate%20System.md):
>
>$$
>\mathop{\operatorname{span}}\left(\frac{\partial S}{\partial x}(\mathbf{a}), \frac{\partial S}{\partial y}(\mathbf{a})\right)
>$$
>
>>[!NOTATION]
>>
>>$$
>>T_S(\mathbf{a}) \qquad T_{S(\mathbf{a})}S
>>$$
>>
>

>[!THEOREM] Theorem: Dimension of the Tangent Space
>
>Let $S: \mathcal{D} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ be a [parametric surface](../Real%20Parametric%20Surfaces.md) which is [differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\mathbf{a} \in \mathcal{D}$.
>
>The [tangent space](#Tangent%20Spaces) of $S$ at $\mathbf{a}$ is at most $2$-[dimensional](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Normal Spaces

>[!DEFINITION] Definition: Normal Space
>
>Let $S: \mathcal{D} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ be a [parametric surface](../Real%20Parametric%20Surfaces.md) which is [differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\mathbf{a} \in \mathcal{D}$.
>
>The **normal space** of $S$ at $\mathbf{a}$ is the [orthogonal complement](../../../../Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md#Orthogonality) of $S$'s [tangent plane](#Tangent%20Planes) at $\mathbf{a}$.
>
>$$
>N_S(\mathbf{a}) \qquad N_{S(\mathbf{a})}S
>$$
>
>>[!DEFINITION] Definition: Surface Normals
>>
>>The elements of the [normal space](#Normal%20Spaces) $N_{S(\mathbf{a})}S$ are known as the **surface normals** or **normal vectors** of $S$ at $\mathbf{a}$.
>>
>

>[!THEOREM] Theorem: Surface Normals in 3D
>
>Let $S: \mathcal{D} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ be a [parametric surface](../Real%20Parametric%20Surfaces.md) which is [differentiable](../../Real%20Vector%20Functions/Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md) at $\mathbf{a} \in \mathcal{D}$.
>
>If $n = 3$, then the [normal space](#Normal%20Spaces) of $S$ at $\mathbf{a}$ is [spanned](../../../../Algebra/Vector%20Spaces/Linear%20Combinations.md#Span) by the [cross product](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md#Cross%20Product) of $S$'s [partial derivatives](../../Real%20Vector%20Fields/Differentiation%20of%20Real%20Vector%20Fields.md) at $\mathbf{a}$ with respect to [Cartesian coordinates](../../Euclidean%20Space/Cartesian%20Coordinate%20System.md):
>
>$$
>N_S(\mathbf{a}) = \mathop{\operatorname{span}}\left\{\frac{\partial S}{\partial x}(\mathbf{a})\times\frac{\partial S}{\partial y}(\mathbf{a})\right\}
>$$
>
>>[!NOTE] Note
>>
>>When dealing with parametric surfaces in 3D, it is very common to use the terms "surface normal" and "normal vector" for this [cross product](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md#Cross%20Product). 
>>
>>>[!NOTATION]
>>>
>>>In such cases, we denote this [cross product](../../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md#Cross%20Product) by $\mathbf{N}(\mathbf{a})$ and its [normalization](../../../../Algebra/Vector%20Spaces/Norms.md) by $\mathbf{n}(\mathbf{a})$
>>>
>>
>
>>[!PROOF]-
>>
>>TODO
>
>



>[!DEFINITION] Definition: Surface Area
>
>Let $s: \mathcal{D} \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ be a [parametric surfaces](../Real%20Parametric%20Surfaces.md).
>
>If $s$ is [differentiable](../../Real%20Vector%20Fields/Differentiation%20of%20Real%20Vector%20Fields.md#Differentiability) on $\mathcal{D}$, then its **surface area** is the [double integral](../Real%20Scalar%20Fields/Integration/Integration%20of%20Real%20Scalar%20Fields.md#Double%20Integrals) of the magnitude of its [normal vector](./Differentiation%20of%20Parametric%20Surfaces.md):
>
>$$
>\iint_{\mathcal{D}} ||\mathbf{N}||
>$$
>