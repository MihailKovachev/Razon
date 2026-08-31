---
tags:
  - linear-algebra
  - algebra
  - mathematics
---

# Eigendecomposition

>[!DEFINITION] Definition: Diagonalizability
>
>A [square matrix](./Square%20Matrices.md) $A \in F^{n \times n}$ is **diagonalizable** if the [endomorphism](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Vector%20Space%20Endomorphisms.md) $f: F^n \to F^n$ whose [matrix representation](../../../Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md#Matrix%20Representations) with respect to the [standard basis](../Row%20and%20Column%20Vectors.md) of $F^n$ is $A$ is [diagonalizable](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Eigentheory.md).
>

>[!THEOREM] Theorem: Diagonalizability
>
>A [square matrix](./Square%20Matrices.md) $A \in F^{n \times n}$ is [diagonalizable](#Eigendecomposition) if and only if there exists an [invertible](./Matrix%20Invertibility.md) [matrix](./Square%20Matrices.md) $P \in F^{n \times n}$ such that
>
>$$D = P^{-1} A P$$
>
>is a [diagonal matrix](./Diagonal%20Matrices.md). 
>
>In this case, if $\lambda_1, \dotsc, \lambda_n$ are the (potentially not distinct) [eigenvalues](./Eigentheory.md) of $A$, then the $j$-th entry on the diagonal of $D$ is $\lambda_j$ and the $j$-th [column](../Matrices.md) of $P$ is an [eigenvector](./Eigentheory.md) of $A$ associated with $\lambda_j$.
>
>>[!PROOF]-
>>
>>TODO
>>
>