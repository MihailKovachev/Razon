>[!DEFINITION] Definition: Real Cross Product
>
>The **cross product** $\vec{a} \times \vec{b}$ of two [real vectors](Real%20Vector.md) $\vec{a} = \begin{bmatrix} a_x & a_y & a_z\end{bmatrix}^\mathsf{T}$ and $\vec{a} = \begin{bmatrix} b_x & b_y & b_z\end{bmatrix}^\mathsf{T}$ in $\mathbb{R}^3$ is defined as the vector
>
>$$
>\vec{a} \times \vec{b} \overset{\text{def}}{=} \begin{bmatrix}a_y b_z - a_z b_y \\ a_z b_x - a_x b_z \\ a_x b_y - a_y b_x \end{bmatrix}
>$$
>
>>[!THEOREM] Theorem: Magnitude of the Cross Product
>>
>>The [magnitude](../../../Vector%20Spaces/Inner%20Product%20Spaces/Canonical%20Norm.md) of the [cross product](Real%20Cross%20Product.md) $\vec{a} \times \vec{b}$ is
>>
>>$$||\vec{a} \times \vec{b}|| = ||\vec{a}|| \, ||\vec{b}|| \sin \theta,$$
>>
>>where $\theta$ is the [angle](../../../Vector%20Spaces/Inner%20Product%20Spaces/Angle.md) between $\vec{a}$ and $\vec{b}$.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>
>>[!THEOREM] Theorem: Direction of the Cross Product
>>
>>The [cross product](Real%20Cross%20Product.md) $\vec{a}\times \vec{b}$ is [orthogonal](../../../Vector%20Spaces/Inner%20Product%20Spaces/Orthogonality.md)  to both $\vec{a}$ and $\vec{b}$.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>>>[!TIP] Tip: Right-Hand Rule
>>>
>>>The direction of the cross product $\vec{a} \times \vec{b}$ can be determined by the right-hand rule - if you point your index finger in the direction of $\vec{a}$ and your middle finger in the direction of $\vec{b}$ and then your thumb will point in the direction of $\vec{a} \times \vec{b}$ if you stick it out.
>>>
>>
>

>[!THEOREM] Theorem: Self-Product of the Cross Product
>
>The [real cross product](Real%20Cross%20Product.md) of a [vector](Real%20Vector.md) $\vec{a} \in \mathbb{R}^3$ with itself is $\vec{0}$.
>
>$$
>\vec{a} \times \vec{a} = \vec{0}
>$$
>
>>[!PROOF]-
>>
>>$$
>>\vec{a} \times \vec{a} = \begin{bmatrix}a_y a_z - a_z a_y \\ a_z a_x - a_x a_z \\ a_x a_y - a_y a_x \end{bmatrix} = \begin{bmatrix}0 \\ 0 \\ 0\end{bmatrix}
>>$$
>>
>

>[!THEOREM] Theorem: Anticommutativity of the Cross Product
>
>The [real cross product](Real%20Cross%20Product.md) is anticommutative:
>
>$$
>\vec{a} \times \vec{b} = - (\vec{b}\times \vec{a})
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Jacobi Property of the Cross Product (Non-Associativity)
>
>The [real cross product](Real%20Cross%20Product.md) is *not* associative but satisfies the Jacobi property:
>
>$$
>\vec{a} \times (\vec{b} \times \vec{c}) - \vec{b} \times (\vec{a} \times \vec{c}) + \vec{c} \times (\vec{a} \times \vec{b}) = \vec{0}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Distributivity of the Cross Product
>
>The [real cross product](Real%20Cross%20Product.md) is distributive over [vector addition](../../Matrix%20Operations/Matrix%20Addition.md):
>
>$$
>\vec{a} \times (\vec{b} + \vec{c}) = \vec{a} \times \vec{b} + \vec{a} \times \vec{c}
>$$
>
>$$
>(\vec{b} + \vec{c}) \times \vec{a} = \vec{b} \times \vec{a} + \vec{c} \times \vec{a}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Compatibility of the Cross Product
>
>The [real cross product](Real%20Cross%20Product.md) is compatible with [scalar multiplication](../../Matrix%20Operations/Scalar%20Multiplication.md):
>
>$$(\lambda \vec{a}) \times \vec{b} = \vec{a} \times (\lambda \vec{b}) = \lambda (\vec{a} \times \vec{b})$$
>
>>[!PROOF]-
>>
>>TODO
>>
>