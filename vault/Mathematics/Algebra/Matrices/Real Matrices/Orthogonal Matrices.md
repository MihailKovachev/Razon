---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Orthogonal Matrices

>[!DEFINITION] Definition: Orthogonal Matrix
>
>An **orthogonal matrix** is a [real matrix](./Real%20Matrices.md) $A \in \mathbb{R}^{n\times n}$ which is the [matrix representation](../../../Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md#Matrix%20Representations) of some [orthogonal transformation](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Orthogonal%20Transformations.md) $T: \mathbb{R}^n \to \mathbb{R}^n$ with respect to the [standard basis](../../Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) of $\mathbb{R}^n$:
>
>$$A = {}_{E_n}[T]_{E_n}$$
>

>[!THEOREM] Theorem: Length Preservation $\implies$ Orthogonal Matrices
>
>A [real](./Real%20Matrices.md) [square matrix](../Square%20Matrices/Square%20Matrices.md) is [orthogonal](./Orthogonal%20Matrices.md) if and only if multiplying a [real column vector](../../Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $v \in \mathbb{R}^n$ by it preserves its [length](../../Linear%20Algebra/Real%20Vectors/Real%20Vectors.md):
>
>$$||Av|| = ||v||$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Inverses of Orthogonal Matrices
>
>If $A \in \mathbb{R}^{n \times n}$ is an [orthogonal matrix](./Orthogonal%20Matrices.md), then it is [invertible](../Square%20Matrices/Matrix%20Invertibility.md) and its [inverse](../Square%20Matrices/Matrix%20Invertibility.md) is its [transpose](../Matrix%20Transposition.md):
>
>$$A^{-1} = A^{\mathsf{T}}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Determinants of Orthogonal Matrices
>
>The [determinant](../Square%20Matrices/Determinants.md) of an [orthogonal matrix](./Orthogonal%20Matrices.md) is either $+1$ or $-1$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Orthonormal Bases from an Orthogonal Matrix
>
>If $A\in \mathbb{R}^{n \times n}$ is an [orthogonal matrix](./Orthogonal%20Matrices.md), then:
>
>    - the columns of $A$ form an [orthonormal](../../Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md#Orthogonality) [basis](../../Vector%20Spaces/Hamel%20Bases.md) of the [real vector space](../../Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $\mathbb{R}^n$;
>    - the columns of its [transpose](../Matrix%20Transposition.md) $A^\mathsf{T}$ form an [orthonormal](../../Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md#Orthogonality) [basis](../../Vector%20Spaces/Hamel%20Bases.md) of the [real vector space](../../Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $\mathbb{R}^n$.
>
>>[!PROOF]-
>>
>>TODO
>>
>