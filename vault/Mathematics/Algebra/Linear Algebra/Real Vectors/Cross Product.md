---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Cross Product

>[!DEFINITION] Definition: Cross Product
>
>The **cross product** $\boldsymbol{a} \times \boldsymbol{b}$ of two [real column vectors](./Real%20Vectors.md) $\boldsymbol{a} = \begin{bmatrix} a_x & a_y & a_z\end{bmatrix}^\mathsf{T}$ and $\boldsymbol{b} = \begin{bmatrix} b_x & b_y & b_z\end{bmatrix}^\mathsf{T}$ in $\mathbb{R}^3$ is defined as the following [real column vector](./Real%20Vectors.md):
>
>$$\boldsymbol{a} \times \boldsymbol{b} \overset{\text{def}}{=} \begin{bmatrix}a_y b_z - a_z b_y \\ a_z b_x - a_x b_z \\ a_x b_y - a_y b_x \end{bmatrix}$$
>

>[!THEOREM] Theorem: Magnitude of the Cross Product
>
>The [Euclidean norm](./Dot%20Product.md) of the [cross product](#Cross%20Product) $\boldsymbol{v} \times \boldsymbol{w}$ is given the product of the [real sine function](../../../Analysis/Real%20Analysis/Real%20Functions/Real%20Trigonometric%20Functions/Real%20Trigonometric%20Functions.md) and the [Euclidean norms](./Dot%20Product.md) of $v$ and $w$ as
>
>$$
>||\boldsymbol{v} \times \boldsymbol{w}|| = ||\boldsymbol{v}|| \, ||\boldsymbol{w}|| \sin \theta,
>$$
>
>where $\theta$ is the [angle](../../Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md) between $\boldsymbol{v}$ and $\boldsymbol{w}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Direction of the Cross Product
>
>If $v, w \in \mathbb{R}^3$ are [real vectors](./Real%20Vectors.md), then the [cross product](./Cross%20Product.md) $v \times w$ is [orthogonal](../../Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md) to both $v$ and $w$ with respect to the [dot product](./Dot%20Product.md):
>
>$$(v \times w) \cdot v = (v \times w) \cdot w = 0$$
>
>>[!TIP] Tip: Right-Hand Rule
>>
>>The direction of $v \times w$ can be determined by the right-hand rule - if you point your index finger in the direction of $v$ and your middle finger in the direction of $w$ and then your thumb will point in the direction of $v \times w$ if you stick it out.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Self-Product of the Cross Product
>
>The [cross product](#Cross%20Product) of a [vector](./Real%20Vectors.md) $\boldsymbol{v} \in \mathbb{R}^3$ with itself is $\boldsymbol{0}$.
>
>$$
>\boldsymbol{v} \times \boldsymbol{v} = \boldsymbol{0}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Linear Independence via Cross Product
>
>The [cross product](./Cross%20Product.md) $\boldsymbol{v} \times \boldsymbol{w}$ is non-zero if and only if $\boldsymbol{v}$ and $\boldsymbol{w}$ are [linearly independent](../../Vector%20Spaces/Linear%20Combinations.md#Linear%20Independence).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Anticommutativity of the Cross Product
>
>The [cross product](#Cross%20Product) is anticommutative:
>
>$$\boldsymbol{v} \times \boldsymbol{w} = - (\boldsymbol{w}\times \boldsymbol{v})$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Jacobi Property of the Cross Product (Non-Associativity)
>
>The [cross product](#Cross%20Product) is *not* associative but satisfies the Jacobi property:
>
>$$
>\boldsymbol{a} \times (\boldsymbol{b} \times \boldsymbol{c}) - \boldsymbol{b} \times (\boldsymbol{a} \times \boldsymbol{c}) + \boldsymbol{c} \times (\boldsymbol{a} \times \boldsymbol{b}) = \boldsymbol{0}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Distributivity of the Cross Product
>
>The [cross product](#Cross%20Product) is distributive over addition:
>
>$$
>\boldsymbol{a} \times (\boldsymbol{b} + \boldsymbol{c}) = \boldsymbol{a} \times \boldsymbol{b} + \boldsymbol{a} \times \boldsymbol{c}
>$$
>
>$$
>(\boldsymbol{b} + \boldsymbol{c}) \times \boldsymbol{a} = \boldsymbol{b} \times \boldsymbol{a} + \boldsymbol{c} \times \boldsymbol{a}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Compatibility of the Cross Product
>
>The [cross product](#Cross%20Product) is compatible with [matrix products](../../Matrices/Matrices.md#Matrix%20Product):
>
>$$
>(\lambda \boldsymbol{a}) \times \boldsymbol{b} = \boldsymbol{a} \times (\lambda \boldsymbol{b}) = \lambda (\boldsymbol{a} \times \boldsymbol{b})
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
