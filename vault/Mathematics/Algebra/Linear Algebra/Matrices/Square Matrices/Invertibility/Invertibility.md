>[!DEFINITION] Definition: Invertible Matrix
>
>A [square matrix](../Square%20Matrix.md) $A \in F^{n \times n}$ is **invertible** if there is a [square matrix](../Square%20Matrix.md) $A^{-1} \in F^{n \times n}$ such that the [matrix products](../../Matrix%20Operations/Matrix%20Product.md) $AA^{-1}$ and $A^{-1}A$ are equal to the [identity matrix](../Identity%20Matrix.md) $I_n$.
>
>$$
>AA^{-1} = A^{-1} A = I_n
>$$
>
>The matrices $A$ and $A^{-1}$ are called **inverses** of each other.
>

>[!THEOREM] Theorem: Antidistributivity of Matrix Inversion
>
>[Matrix inversion](Invertibility.md) is antidistributive over [matrix products](../../Matrix%20Operations/Matrix%20Product.md) - if $A, B \in F^{n \times}$ and their [product](../../Matrix%20Operations/Matrix%20Product.md) $AB$ are [invertible](Invertibility.md), then:
>
>$$
>(AB)^{-1} = B^{-1} A^{-1}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Invertible Matrix Theorem
>
>The following statements are equivalent for every [square matrix](../Square%20Matrix.md) $A \in F^{n \times n}$: 
>- $A$ is [invertible](Invertibility.md).
>- The [transpose](../../Matrix%20Operations/Matrix%20Transposition.md) of $A$ is [invertible](Invertibility.md).
>- The [determinant](../Determinants/Determinant.md) of $A$ is not zero, i.e. $\det(A) \ne 0$.
>- The [reduced row echelon form](../../../Systems%20of%20Linear%20Equations/Row%20Echelon%20Form.md) of $A$ is the [identity matrix](../Identity%20Matrix.md) $I_n$.
>- The [system of linear equations](../../../Systems%20of%20Linear%20Equations/Augmented%20Matrix.md) $A \vec{x} = \vec{b}$ has a single [solution](../../../Systems%20of%20Linear%20Equations/Solvability%20of%20a%20System%20of%20Linear%20Equations.md) for every $\vec{b} \in F^n$.
>- The [column space](../../Column%20Space.md) of $A$ is the [vector space](../../Vector%20Space%20of%20Matrices.md) $F^n$.
>- The [row space](../../Row%20Space.md) of $A$ is the [vector space](../../Vector%20Space%20of%20Matrices.md) $F^{1 \times n}$.
>- The [rank](../../../Systems%20of%20Linear%20Equations/Rank.md) of $A$ is $n$.
>
>>[!PROOF]-
>>
>>TODO
>>
>