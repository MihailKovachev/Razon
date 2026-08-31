---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Real Symmetric Matrices

>[!THEOREM] The Spectral Theorem
>
>Every [real symmetric matrix](./Real%20Symmetric%20Matrices.md) is [diagonalizable](../Square%20Matrices/Eigentheory.md) and [eigenvectors](../Square%20Matrices/Eigentheory.md) which belong to different [eigenvalues](../Square%20Matrices/Eigentheory.md) are always [orthogonal](../../Linear%20Algebra/Real%20Vectors/Dot%20Product.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Spectral Norm of Real Symmetric Matrices
>
>If a [real](./Real%20Matrices.md) [square matrix](../Square%20Matrices/Square%20Matrices.md) is [symmetric](../Square%20Matrices/Symmetric%20Matrices.md), then its [spectral norm](../Spectral%20Norm.md) is the maximum of the [absolute values](TODO) of its [eigenvalues](../Square%20Matrices/Eigentheory.md):
>
>$$||A||_2 = \max \{|\lambda|: \lambda \text{ is an eigenvalue of } A\}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Definiteness Criteria
>
>A [real symmetric matrix](./Real%20Symmetric%20Matrices.md) $M \in \mathbb{R}^{n \times n}$ is
>
>- [positive definite](../Square%20Matrices/Symmetric%20Matrices.md#Definiteness) if and only if all of its [eigenvalues](../Square%20Matrices/Eigentheory.md) are positive;
>- [positive semi-definite](../Square%20Matrices/Symmetric%20Matrices.md#Definiteness) if and only if all of its [eigenvalues](../Square%20Matrices/Eigentheory.md) are non-negative;
>- [negative definite](../Square%20Matrices/Symmetric%20Matrices.md#Definiteness) if and only if all of its [eigenvalues](../Square%20Matrices/Eigentheory.md) are negative;
>- [negative semi-definite](../Square%20Matrices/Symmetric%20Matrices.md#Definiteness) if and only if all of its [eigenvalues](../Square%20Matrices/Eigentheory.md) are non-positive;
>- [indefinite](../Square%20Matrices/Symmetric%20Matrices.md#Definiteness) if and only if it has both positive and negative [eigenvalues](../Square%20Matrices/Eigentheory.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Symmetry and Bounds
>
>Let $M \in \mathbb{R}^{n \times n}$ be a [real symmetric matrix](./Real%20Symmetric%20Matrices.md) with [eigenvalues](../Square%20Matrices/Eigentheory.md) $\lambda_n \ge \cdots \ge \lambda_1$.
>
>For all $\boldsymbol{x} \in \mathbb{R}^n$, we have:
>
>$$\lambda_1 ||\boldsymbol{x}||^2 \le \boldsymbol{x}^{\mathsf{T}}M\boldsymbol{x} \le \lambda_n ||\boldsymbol{x}||^2$$
>
>>[!PROOF]-
>>
>>By the [spectral theorem](./Real%20Symmetric%20Matrices.md), we know that $M$ can be [diagonalized](../Square%20Matrices/Eigentheory.md#Eigendecomposition) into
>>
>>$$M = Q\Lambda Q^{\mathsf{T}},$$
>>
>>where $Q$ is [orthogonal](./Orthogonal%20Matrices.md). Therefore:
>>
>>$$\boldsymbol{x}^{\mathsf{T}}M\boldsymbol{x} = \boldsymbol{x}^{\mathsf{T}}(Q\Lambda Q^{\mathsf{T}})\boldsymbol{x} = (\boldsymbol{x}^{\mathsf{T}}Q)\Lambda (Q^{\mathsf{T}}\boldsymbol{x})$$
>>
>>Let $\boldsymbol{y} = Q^{\mathsf{T}}\boldsymbol{x}$. We get:
>>
>>$$\boldsymbol{x}^{\mathsf{T}}M\boldsymbol{x} = \boldsymbol{y}^{\mathsf{T}} \Lambda \boldsymbol{y}$$
>>
>>Since $\Lambda$ is [diagonal](../Square%20Matrices/Diagonal%20Matrices.md) with $\Lambda = \operatorname{diag}(\lambda_1, \dotsc, \lambda_n)$, we get:
>>
>>$$\boldsymbol{y}^{\mathsf{T}} \Lambda \boldsymbol{y} = \boldsymbol{y}^{\mathsf{T}} (\Lambda \boldsymbol{y}) = \boldsymbol{y}^{\mathsf{T}} \begin{bmatrix}\lambda_1 y_1 \\ \vdots \\ \lambda_n y_n\end{bmatrix} = \sum_{i = 1}^n \lambda_i y_i^2$$
>>
>>For the bounds in terms of $\boldsymbol{y}$:
>>
>>$$\sum_{i = 1}^n \lambda_i y_i^2 \ge \sum_{i = 1}^n \lambda_1 y_i^2 = \lambda_1 \sum_{i = 1}^n y_i^2 = \lambda_1 ||\boldsymbol{y}||^2$$
>>
>>$$\sum_{i = 1}^n \lambda_i y_i^2 \le \sum_{i = 1}^n \lambda_n y_i^2 = \lambda_n \sum_{i = 1}^n y_i^2 = \lambda_n ||\boldsymbol{y}||^2$$
>>
>>Therefore:
>>
>>$$\lambda_1 ||\boldsymbol{y}||^2 \le \boldsymbol{y}^{\mathsf{T}} \Lambda \boldsymbol{y} \le \lambda_n ||\boldsymbol{y}||^2$$
>>
>>Express $||\boldsymbol{y}||^2$ in terms of $\boldsymbol{x}$:
>>
>>$$||\boldsymbol{y}||^2 = \boldsymbol{y}^{\mathsf{T}}\boldsymbol{y} = (Q^{\mathsf{T}}\boldsymbol{x})^{\mathsf{T}}(Q^{\mathsf{T}}\boldsymbol{x}) = \boldsymbol{x}^{\mathsf{T}}(QQ^{\mathsf{T}}) \boldsymbol{x} = \boldsymbol{x}^{\mathsf{T}}\boldsymbol{x} = ||\boldsymbol{x}||^2$$
>>
>>We thus get:
>>
>>$$\lambda_1 ||\boldsymbol{x}||^2 \le \boldsymbol{y}^{\mathsf{T}} \Lambda \boldsymbol{y} \le \lambda_n ||\boldsymbol{x}||^2$$
>>
>>Since $\boldsymbol{x}^{\mathsf{T}}M\boldsymbol{x} = \boldsymbol{y}^{\mathsf{T}} \Lambda \boldsymbol{y}$, we get:
>>
>>$$\lambda_1 ||\boldsymbol{x}||^2 \le \boldsymbol{x}^{\mathsf{T}}M\boldsymbol{x} \le \lambda_n ||\boldsymbol{x}||^2$$
>>
>