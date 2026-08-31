---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Orthogonal Projections

>[!DEFINITION] Definition: Orthogonal Projection
>
>Let $U$ be a [finite-dimensional](../Hamel%20Bases.md#Dimension) [linear subspace](../Linear%20Subspaces.md) of an [inner product space](./Inner%20Product%20Spaces.md) $(V, \langle \cdot, \cdot \rangle)$ and let $u_1, \dotsc, u_n$ be an [orthonormal](./Inner%20Product%20Spaces.md#Orthogonality) [basis](../Hamel%20Bases.md) of $U$.
>
>The **orthogonal projection** onto $U$ is the [function](../../../Analysis/Functions/Functions.md) $\pi_U: V \to U$ defined as
>
>$$\pi_U (v) = \sum_{i = 1}^n \langle v, u_i\rangle u_i$$
>
>for all $v \in V$.
>
>>[!EXAMPLE]-
>>
>>Consider the [real vector space](../../Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $\mathbb{R}^3$ with the [dot product](../../Linear%20Algebra/Real%20Vectors/Real%20Vectors.md#Dot%20Product) and consider its [subspace](../Linear%20Subspaces.md) $U$ defined as the [span](../Span.md) of $u_1$ and $u_2$, where
>>
>>$$u_1 = \begin{bmatrix}\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \\ 0\end{bmatrix} \qquad u_2 = \begin{bmatrix}0 \\ 0 \\ 1\end{bmatrix}.$$
>>
>>We see that $u_1$ and $u_2$ are [orthonormal](./Inner%20Product%20Spaces.md#Orthogonality) and are thus an [orthonormal](./Inner%20Product%20Spaces.md#Orthogonality) [basis](../Hamel%20Bases.md) of $U$.
>>
>>We want to determine $\pi_U(v)$ for $v = \begin{bmatrix}1 & 2 & 3\end{bmatrix}^{\mathsf{T}}$:
>>
>>$$\begin{aligned}\pi_U(v)  & = \sum_{i = 1}^n (v \cdot u_i) u_i \\ & = (v \cdot u_1)u_1 + (v \cdot u_2)u_2 \\ & = \left(1\times \frac{1}{\sqrt{2}}+2\times \frac{1}{\sqrt{2}}+3\times 0\right)u_1 + (1 \times 0 + 2 \times 0 + 3 \times 1)u_2 \\ & = \frac{3}{\sqrt{2}}u_1 + 3 u_2 \\ & = \frac{3}{\sqrt{2}}\begin{bmatrix}\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \\ 0\end{bmatrix}+ 3 \begin{bmatrix}0 \\ 0 \\ 1\end{bmatrix} \\ & = \begin{bmatrix}\frac{3}{2} \\ \frac{3}{2} \\ 3\end{bmatrix}\end{aligned}$$
>>
>

>[!THEOREM] Theorem: Basis Independence
>
>The [orthogonal projection](./Orthogonal%20Projections.md) onto a [linear subspace](../Linear%20Subspaces.md) is independent of the choice of [orthonormal](./Inner%20Product%20Spaces.md#Orthogonality) [basis](../Hamel%20Bases.md) for it.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Linearity of Orthogonal Projections
>
>The [orthogonal projection](./Orthogonal%20Projections.md) onto a [linear subspace](../Linear%20Subspaces.md) is [linear](../../../Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md).
>
>>[!PROOF]-
>>
>>TODO
>>
>