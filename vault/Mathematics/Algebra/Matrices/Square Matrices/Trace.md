---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Trace

>[!DEFINITION] Definition: Trace
>
>The **trace** of a [square matrix](./Square%20Matrices.md) $A = (a_{ij}) \in F^{n\times n}$ is the sum of the entries on its diagonal:
>
>$$\sum_{k=1}^n a_{k,k}$$
>
>>[!NOTATION]
>>
>>$$\operatorname{tr}(A)$$
>>
>

>[!THEOREM] Theorem: Independence of Product Order
>
>Let $A, B \in F^{n \times n}$ be [square](./Square%20Matrices.md) [matrices](../Matrices.md).
>
>The [trace](./Trace.md) of the [matrix product](../Matrix%20Product.md) $AB$ is the same as the [trace](./Trace.md) of the [matrix product](../Matrix%20Product.md) $BA$:
>
>$$\operatorname{tr}(AB) = \operatorname{tr}(BA)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Similar Matrices $\implies$ Equal Trace
>
>If two [square](./Square%20Matrices.md) [matrices](../Matrices.md) $A, B \in F^{n \times n}$ are [similar](./Matrix%20Similarity.md), then they have the same [trace](./Trace.md):
>
>$$B = S^{-1} A S \implies \operatorname{tr}(B) = \operatorname{tr}(A)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Trace and Eigenvalues
>
>If a [square matrix](./Square%20Matrices.md) $A \in F^{n \times n}$ has $l$ distinct [eigenvalues](./Eigentheory.md) $\lambda_1, \cdots, \lambda_l$ and the sum of their [algebraic multiplicities](./Eigentheory.md) is $n$, then the [trace](./Trace.md) of $A$ is given as follows:
>
>$$\operatorname{tr}(A) = \sum_{k=1}^l \lambda_k \cdot \operatorname{alg} (\lambda_k)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>