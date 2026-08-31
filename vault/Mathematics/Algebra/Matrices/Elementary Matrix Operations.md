---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Elementary Matrix Operations

>[!DEFINITION] Definition: Elementary Matrix Operations
>
>The **elementary row / column operations** on a [matrix](./Matrices.md) $A \in F^{m \times n}$ are the following:
>
>    - swapping two rows / columns;
>    - multiplying a row / column by $\lambda \ne 0$;
>    - adding a row / column multiplied by $\mu \in F$ to another row / column.
>

>[!THEOREM] Theorem: Effects on Determinants
>
>[Elementary matrix operations](./Elementary%20Matrix%20Operations.md) have the following effects on the [determinant](./Square%20Matrices/Determinants.md) of a [square matrix](./Square%20Matrices/Square%20Matrices.md) $A \in F^{n \times n}$:
>
>    - Swapping two rows / columns flips the sign of the [determinant](./Square%20Matrices/Determinants.md).
>    - Multiplying a row / column by $\lambda \ne 0$ multiplies the [determinant](./Square%20Matrices/Determinants.md) by $\lambda$.
>    - Adding a row / column multiplied by $\mu \in F$ to another row / column does not affect the [determinant](./Square%20Matrices/Determinants.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Rank Preservation
>
>[Elementary matrix operations](./Elementary%20Matrix%20Operations.md) preserve [rank](./Matrices.md#Matrix%20Spaces).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Effects on Null Space
>
>[Elementary row operations](./Elementary%20Matrix%20Operations.md) preserve the [null space](./Matrices.md#Matrix%20Spaces) of a [matrix](./Matrices.md), but [elementary column operations](./Elementary%20Matrix%20Operations.md) only preserve [nullity](./Matrices.md#Matrix%20Spaces).
>
>>[!PROOF]-
>>
>>TODO
>>
>

### Elementary Matrices

Performing an [elementary matrix operation](./Elementary%20Matrix%20Operations.md) on a [matrix](./Matrices.md) $A \in F^{m \times n}$ can be represented as a [multiplication](TODO) of $A$ with a [square matrix](./Square%20Matrices/Square%20Matrices.md):

- For an [elementary row operation](./Elementary%20Matrix%20Operations.md), perform the [operation](./Elementary%20Matrix%20Operations.md) on the [identity matrix](./Square%20Matrices/Matrix%20Invertibility.md) $I_m$ to obtain the [square matrix](./Square%20Matrices/Square%20Matrices.md) $E_m$. Applying the same [elementary row operation](./Elementary%20Matrix%20Operations.md) to $A$ is equivalent to the [product](TODO) $E_mA$.
- For an [elementary column operation](./Elementary%20Matrix%20Operations.md), perform the [operation](./Elementary%20Matrix%20Operations.md) on the [identity matrix](./Square%20Matrices/Matrix%20Invertibility.md) $I_n$ to obtain the [square matrix](./Square%20Matrices/Square%20Matrices.md) $E_n$. Applying the same [elementary column operation](./Elementary%20Matrix%20Operations.md) to $A$ is the equivalent to the [product](TODO) $AE_n$.