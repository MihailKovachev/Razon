---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Schur Decomposition

>[!THEOREM] Theorem: Schur Decomposition
>
>Every [complex](./Complex%20Matrices.md) [square matrix](../Square%20Matrices/Square%20Matrices.md) $A \in \mathbb{C}^{n \times n}$ is [similar](../Square%20Matrices/Matrix%20Similarity.md) to an [upper triangular matrix](../Square%20Matrices/Triangular%20Matrices.md) $R$ with a [unitary](./Unitary%20Matrices.md) [transition matrix](../Square%20Matrices/Matrix%20Similarity.md):
>
>$$A = U R U^{\ast}$$
>
>>[!DEFINITION] Definition: Schur Normal Form
>>
>>We call $R$ the **Schur normal form** of $A$.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!ALGORITHM] Algorithm: Schur Decomposition via Deflation Method
>
>We want to find the [Schur decomposition](./Schur%20Decomposition.md)
>
>$$A = URU^{\ast}$$
>
>of a [complex matrix](./Complex%20Matrices.md) [square matrix](../Square%20Matrices/Square%20Matrices.md) $A \in \mathbb{C}^{n \times n}$.
>
>1. Define $A_0 = A$.
>
>2. For all $j \in \{0, 1, \cdots, n-2\}$:
>
>    - Find an [eigenvalue](../Square%20Matrices/Eigentheory.md) $\lambda_j$ of $A_j$ and a corresponding [eigenvector](../Square%20Matrices/Eigentheory.md) $\mathbf{u}_j^{(1)}$ which is [normalized](../../Vector%20Spaces/Norms.md) with respect to the [induced norm](../../Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md) of the [dot product](../../Linear%20Algebra/Complex%20Vectors/Complex%20Dot%20Product.md).
>    - Extend $\mathbf{u}_j^{(1)}$ to an [orthonormal](../../Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md#Orthogonality) [basis](../../Vector%20Spaces/Hamel%20Bases.md) $\mathbf{u}_j^{(1)}, \mathbf{u}_j^{(2)}, \dotsc, \mathbf{u}_j^{(n-j)}$ of $\mathbb{C}^{n-j}$ and construct the [unitary matrix](./Unitary%20Matrices.md) $\hat{U}_j \in \mathbb{C}^{(n-j) \times (n-j)}$ whose [columns](../Matrices.md) are $\mathbf{u}_j^{(1)}, \mathbf{u}_j^{(2)}, \dotsc, \mathbf{u}_j^{(n-j)}$.
>
>    $$\hat{U}_j = \begin{bmatrix} \vert & \vert & \vert \\ \mathbf{u}_j^{(1)} & \cdots & \mathbf{u}_j^{(n-j)} \\ \vert & \vert & \vert\end{bmatrix}$$
>
>    - Extend $\hat{U}_j$ to an $n\times n$ [complex](./Complex%20Matrices.md) [square matrix](../Square%20Matrices/Square%20Matrices.md) $U_j$ using the [identity matrix](../Square%20Matrices/Matrix%20Invertibility.md) $I_j$ as follows (We have $U_0 = \hat{U}_0$).
>
>    $$U_j = \begin{bmatrix} I_j & \mathbf{0} \\ \mathbf{0} & \hat{U}_j\end{bmatrix}$$
>
>    - Define $A_{j+1}$ as the $(n - j - 1) \times (n - j -1)$ [complex](./Complex%20Matrices.md) [square matrix](../Square%20Matrices/Square%20Matrices.md) obtained by removing the first row and first column of the [product](../Matrix%20Product.md) $\hat{U}_j^{\ast} A_j \hat{U}_j$ (Skip this for the last $j = n - 2$).
>
>    $$\hat{U}_j^{\ast} A_j \hat{U}_j = \begin{bmatrix}\lambda_j & \ast \\ \mathbf{0} & A_{j+1}\end{bmatrix}$$
>
>3. Compile the [Schur decomposition](./Schur%20Decomposition.md) $A = URU^{\ast}$:
>
>    - The [unitary matrix](./Unitary%20Matrices.md) $U$ is the [product](../Matrix%20Product.md) of $U_0, U_1, \dotsc, U_{n-2}$.
>
>    $$U = U_0 U_1 \cdots U_{n-2}$$
>
>    - The [Schur normal form](./Schur%20Decomposition.md) $R$ is the [product](../Matrix%20Product.md) $U^{\ast}AU$.
>
>    $$R = U^{\ast}AU$$
>
>>[!EXAMPLE]- Example:
>>
>>We want to find the [Schur decomposition](./Schur%20Decomposition.md) of the following [complex](./Complex%20Matrices.md) [square matrix](../Square%20Matrices/Square%20Matrices.md) $A = URU^{\ast}$:
>>
>>$$A = \begin{bmatrix}3 & 0 & 0 \\ 1 & 1 & 2 \\ 1 & 0 & 2\end{bmatrix}$$
>>
>>From the second column, we immediately see that $\begin{bmatrix}0 & 1 & 0\end{bmatrix}^{\mathsf{T}}$ is an [eigenvector](../Square%20Matrices/Eigentheory.md) with [eigenvalue](../Square%20Matrices/Eigentheory.md) $1$. We can easily extend it to the following [orthonormal basis](../../Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md) of $\mathbb{C}^3$:
>>
>>$$\left\{ \begin{bmatrix}0 \\ 1 \\ 0\end{bmatrix}, \begin{bmatrix}1 \\ 0 \\ 0\end{bmatrix}, \begin{bmatrix}0 \\ 0 \\ 1\end{bmatrix} \right\}$$
>>
>>We thus have:
>>
>>$$\hat{U}_0 = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
>>
>>Therefore:
>>
>>$$U_0 = \hat{U}_0 = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$
>>
>>Furthermore,
>>
>>$$\hat{U}_0^{\ast} A_0 U_0 = \begin{bmatrix}1 & 1 & 2 \\ 0 & 3 & 0 \\ 0 & 1 & 2\end{bmatrix}$$
>>
>>and so
>>
>>$$A_1 = \begin{bmatrix}3 & 0 \\ 1 & 2\end{bmatrix}.$$
>>
>>From the second column of $A_1$, we see that $\begin{bmatrix}0 & 1\end{bmatrix}^{\mathsf{T}}$ is an [eigenvector](../Square%20Matrices/Eigentheory.md) with [eigenvalue](../Square%20Matrices/Eigentheory.md) $2$. We can easily extend it to the following [orthonormal basis](../../Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md) of $\mathbb{C}^2$:
>>
>>$$\left\{ \begin{bmatrix}0 \\ 1\end{bmatrix}, \begin{bmatrix}1 \\ 0\end{bmatrix} \right\}$$
>>
>>We thus have:
>>
>>$$\hat{U}_1 = \begin{bmatrix} 0 & 1 \\ 1 & 0\end{bmatrix}$$
>>
>>Therefore:
>>
>>$$U_1 = \begin{bmatrix} I_1 & \mathbf{0} \\ \mathbf{0} & \hat{U}_j\end{bmatrix} = \begin{bmatrix}1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0\end{bmatrix}$$
>>
>>At last, we have:
>>
>>$$U = U_0 U_1 = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix}1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0\end{bmatrix} = \begin{bmatrix}0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0\end{bmatrix}$$
>>
>>$$\begin{aligned} R & = U^{\ast}AU \\ & = \begin{bmatrix}0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0\end{bmatrix} \begin{bmatrix}3 & 0 & 0 \\ 1 & 1 & 2 \\ 1 & 0 & 2\end{bmatrix} \begin{bmatrix}0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0\end{bmatrix} \\ & = \begin{bmatrix}1 & 2 & 1 \\ 0 & 2 & 1 \\ 0 & 0 & 3\end{bmatrix} \end{aligned}$$
>>
>