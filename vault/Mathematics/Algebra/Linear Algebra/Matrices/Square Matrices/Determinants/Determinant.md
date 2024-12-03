>[!DEFINITION] Definition: Determinant
>
>The **determinant** of a [matrix](../../Matrix.md) $A \in F^{n \times n}$ is an element in $F$ which is calculated recursively from the coefficients of $A$:
>
>$$
>\det(A) = \begin{cases}a_{11}, \text{ if } n = 1 \\ \displaystyle\sum_{i=1}^n (-1)^{1+j}a_{1j}\det(A_{1j}), \text{ if } n\gt 1\end{cases}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>|A| \qquad \det(A)
>>$$
>>
>

>[!THEOREM] Theorem: Distributivity of the Determinant
>
>The [determinant](Determinant.md) is distributive over [matrix products](../../Matrix%20Operations/Matrix%20Product.md):
>
>$$
>\det(AB) = \det(A) \det(B) = \det(B) \det(A) = \det(BA)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Determinant of the Transpose
>
>The [determinant](Determinant.md) of the [transpose](../../Matrix%20Operations/Matrix%20Transposition.md) of a $A$ is the same as the [determinant](Determinant.md) of $A$.
>
>$$
>\det(A^\mathsf{T}) = \det(A)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Determinant of the Inverse
>
>If $A$ is [invertible](../Invertibility/Invertibility.md), then the [determinant](Determinant.md) of $A^{-1}$ is the reciprocal of $A$'s [determinant](Determinant.md):
>
>$$
>\det(A^{-1}) = \frac{1}{\det(A)}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Determinant of Scalar Multiplication
>
>For the [determinant](Determinant.md) of every [square matrix](../Square%20Matrix.md) $A \in F^{n \times n}$ and every $\alpha \in F$:
>
>$$
>\det(\alpha A) = \alpha^n \det (A)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>