>[!DEFINITION] Definition: Diagonalisable Matrix
>
>A [square matrix](../Square%20Matrix.md) $A \in F^{n \times n}$ is **diagonalisable** if it is [similar](../Matrix%20Similarity.md) to a [diagonal matrix](../Diagonal%20Matrices/Diagonal%20Matrix.md) $\Lambda \in F^{n \times n}$.
>
>>[!THEOREM] Theorem: Eigendecomposition
>>
>>A [square matrix](../Square%20Matrix.md) $A \in F^{n \times n}$ is [diagonalisable](Eigendecomposition.md) if and only if it has $n$ [linearly independent](../../../Vector%20Spaces/Linear%20Independence.md) [eigenvectors](Eigenvector.md) $\vec{e}_1, \cdots, \vec{e}_n$.
>>
>>In that case, $A$ can be written as a [matrix product](../../Matrix%20Operations/Matrix%20Product.md)
>>
>>$$
>>A = Q\Lambda Q^{-1},
>>$$
>>
>>where the $k$-th column of $Q$ is the $\vec{e}_k$ and $\Lambda = \operatorname{diag}(\lambda_1, \cdots, \lambda_n)$ is the [diagonal matrix](../Diagonal%20Matrices/Diagonal%20Matrix.md) whose $k$-th diagonal entry is the [eigenvalue](Eigenvalue.md) $\lambda_k$ to which $\vec{e}_k$ belongs.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>>>[!DEFINITION] Definition: Eigendecomposition
>>>
>>>The **eigendecomposition** of $A$ is the [product](../../Matrix%20Operations/Matrix%20Product.md) $Q\Lambda Q^{-1}$.
>>>
>>
>
