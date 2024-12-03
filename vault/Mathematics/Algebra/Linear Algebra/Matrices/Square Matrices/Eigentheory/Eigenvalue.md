>[!DEFINITION] Definition: Eigenvalue
>
>Let $A \in F^{n \times n}$ be a [square matrix](../Square%20Matrix.md).
>
>We say that $\lambda \in F$ is an **eigenvalue** of $A$ if there is a non-zero [vector](../../Row%20and%20Column%20Vectors/Column%20Vector.md) $\vec{v} \in F^n$ such that
>
>$$
>A \vec{v} = \lambda \vec{v}
>$$
>
>In this case, we also say that $\lambda$ has the [eigenvector](Eigenvector.md) $\vec{v}$.
>
>>[!NOTE]
>>
>>An [eigenvalue](Eigenvalue.md) can have multiple [eigenvectors](Eigenvector.md).
>>
>

>[!THEOREM] Theorem: Count of Eigenvalues
>
>A [square matrix](../Square%20Matrix.md) $A \in F^{n \times n}$ has at most $n$ different [eigenvalues](Eigenvalue.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Algebraic and Geometric Multiplicity
>
>The [geometric multiplicity](Eigenspace.md) and the [algebraic multiplicity](Characteristic%20Polynomial.md) of every [eigenvalue](Eigenvalue.md) $\lambda$ of a [square matrix](../Square%20Matrix.md) $A \in F^{n \times n}$ obey the following inequality:
>
>$$
>1\le \operatorname{geo}(\lambda)\le \operatorname{alg}(\lambda)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Sum of the Eigenvalues
>
>The distinct [eigenvalues](Eigenvalue.md) $\lambda_1, \cdots, \lambda_r$ of a [square matrix](../Square%20Matrix.md) $A \in F^{n \times n}$ and their [algebraic multiplicities](Characteristic%20Polynomial.md) can be used to calculate the [trace](../Trace.md) of $A$:
>
>$$
>\sum_{k=1}^r \lambda_k \cdot \operatorname{alg} (\lambda_k) = \operatorname{Tr}(A)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Product of the Eigenvalues
>
>The distinct [eigenvalues](Eigenvalue.md) $\lambda_1, \cdots, \lambda_r$ of a [square matrix](../Square%20Matrix.md) $A \in F^{n \times n}$ and their [algebraic multiplicities](Characteristic%20Polynomial.md) can be used to calculate the [determinant](../Determinants/Determinant.md) of $A$:
>
>$$
>\prod_{k=1}^r \lambda_k^{\operatorname{alg} (\lambda_k)} = \det(A)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>