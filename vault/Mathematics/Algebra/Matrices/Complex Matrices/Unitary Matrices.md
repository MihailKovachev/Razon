---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Unitary Matrices

>[!DEFINITION] Definition: Unitary Matrix
>
>A **unitary matrix** is a [complex matrix](./Complex%20Matrices.md) $A \in \mathbb{C}^{n\times n}$ which is the [matrix representation](../../../Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md#Matrix%20Representations) of some [unitary transformation](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Unitary%20Transformations.md) $T: \mathbb{C}^n \to \mathbb{C}^n$ with respect to the [standard basis](../../Linear%20Algebra/Complex%20Vectors/Complex%20Vectors.md) of $\mathbb{C}^n$:
>
>$$A = {}_{E_n}[T]_{E_n}$$
>

>[!THEOREM] Theorem: Length Preservation $\implies$ Unitary Matrices
>
>A [complex](./Complex%20Matrices.md) [square matrix](../Square%20Matrices/Square%20Matrices.md) is [unitary](./Unitary%20Matrices.md) if and only if multiplying a [complex vector](../../Linear%20Algebra/Complex%20Vectors/Complex%20Vectors.md) $v \in \mathbb{C}^n$ by it preserves its [length](../../Linear%20Algebra/Complex%20Vectors/Complex%20Vectors.md):
>
>$$||Av|| = ||v||$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Inverses of Unitary Matrices
>
>If $A \in \mathbb{C}^{n \times n}$ is an [unitary matrix](./Unitary%20Matrices.md), then it is [invertible](../Square%20Matrices/Matrix%20Invertibility.md) and its [inverse](../Square%20Matrices/Matrix%20Invertibility.md) is its [Hermitian transpose](./Hermitian%20Transpose.md):
>
>$$A^{-1} = A^{\ast}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Determinants of Unitary Matrices
>
>The [determinant](../Square%20Matrices/Determinants.md) of an [unitary matrix](./Unitary%20Matrices.md) is either $+1$ or $-1$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Orthonormal Bases from an Unitary Matrix
>
>If $A\in \mathbb{C}^{n \times n}$ is a [unitary matrix](./Unitary%20Matrices.md), then:
>
>    - the columns of $A$ form an [orthonormal](../../Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md#Orthogonality) [basis](../../Vector%20Spaces/Hamel%20Bases.md) of the [complex vector space](../../Linear%20Algebra/Complex%20Vectors/Complex%20Vectors.md) $\mathbb{C}^n$;
>    - the rows of $A$ also form an [orthonormal](../../Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md#Orthogonality) [basis](../../Vector%20Spaces/Hamel%20Bases.md) of the [complex vector space](../../Linear%20Algebra/Complex%20Vectors/Complex%20Vectors.md) $\mathbb{C}^n$.
>
>>[!PROOF]-
>>
>>TODO
>>
>