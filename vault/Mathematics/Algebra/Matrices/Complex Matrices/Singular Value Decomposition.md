---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Singular Value Decomposition

>[!DEFINITION] Definition: Singular Values
>
>Let $A \in \mathbb{C}^{m \times n}$ be a [complex matrix](./Complex%20Matrices.md).
>
>The **singular values** of $A$ are the [square roots](TODO) of the [eigenvalues](../Square%20Matrices/Eigentheory.md) of the [matrix product](../Matrix%20Product.md) $A^{\ast} A$ between $A$ and its [Hermitian transpose](./Hermitian%20Transpose.md).
>

>[!THEOREM] Theorem: Singular Value Decomposition
>
>Every [complex matrix](./Complex%20Matrices.md) $A \in \mathbb{C}^{m \times n}$ can be expressed as the [product](../Matrix%20Product.md) of a [unitary matrix](./Unitary%20Matrices.md) $U \in \mathbb{C}^{m \times m}$, a [diagonal matrix](../Square%20Matrices/Diagonal%20Matrices.md) $\Sigma \in \mathbb{C}^{m \times n}$ and the [Hermitian transpose](./Hermitian%20Transpose.md) of a [unitary matrix](./Unitary%20Matrices.md) $V \in \mathbb{C}^{n \times n}$:
>
>$$A = U\Sigma V^{\ast}$$
>
>Moreover, the entries on $\Sigma$'s diagonal are precisely the (not necessarily distinct) [singular values](./Singular%20Value%20Decomposition.md) of $A$. If $\sigma_{j} = \sqrt{\lambda_j}$ is the diagonal entry on the $j$-th column of $\Sigma$, then the $j$-th column of $V$ is an [eigenvector](../Square%20Matrices/Eigentheory.md) of $A^{\ast}A$ which corresponds to $\lambda_j$.
>
>>[!PROOF]-
>>
>>TODO
>>
>