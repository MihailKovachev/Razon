---
tags:
  - linear-algebra
  - algebra
  - mathematics
---

# Matrix Invertibility

>[!DEFINITION] Definition: Identity Matrix
>
>The $n\times n$**-identity matrix** $I_n \in F^{n \times n}$ over some [field](../../Fields/Fields.md) $F$ is the [square matrix](./Square%20Matrices.md)  which has the [multiplicative identity](../../Fields/Fields.md) of $F$ as its entries on the diagonal and whose other entries are the [additive identity](../../Fields/Fields.md)  of $F$:
>
>$$
>I_n \overset{\text{def}}{=} \begin{bmatrix} 1_F & \cdots & 0_F \\ \vdots & \ddots & \vdots \\ 0_F & \cdots & 1_F\end{bmatrix}
>$$
>

>[!THEOREM] Theorem: Multiplication with the Identity Matrix
>
>The [product](../Matrices.md#Matrix%20Product) of any $m\times n$-[matrix](../Matrices.md) $A$ with the [identity matrix](#Identity%20Matrix) $I_m$ on the left or the [identity matrix](#Identity%20Matrix) $I_n$ is $A$ itself.
>
>$$
>I_m \cdot A = A = A \cdot I_n
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!DEFINITION] Definition: Invertible Matrix
>
>A [square matrix](./Square%20Matrices.md) $A \in F^{n \times n}$ is **invertible** if there exists a [square matrix](./Square%20Matrices.md) $A^{-1} \in F^{n \times n}$ such that the [matrix products](../Matrices.md#Matrix%20Products) $AA^{-1}$ and $A^{-1}A$ are equal to the [identity matrix](#Identity%20Matrix) $I_n$.
>
>$$
>AA^{-1} = A^{-1} A = I_n
>$$
>
>The matrices $A$ and $A^{-1}$ are called **inverses** of each other.
>

>[!THEOREM] Theorem: The Invertible Matrix Theorem
>
>The following statements are equivalent for every [square matrix](./Square%20Matrices.md) $A \in F^{n \times n}$: 
>- $A$ is [invertible](#Matrix%20Invertibility).
>- The [transpose](../Matrix%20Operations.md) of $A$ is [invertible](#Matrix%20Invertibility).
>- The [determinant](./Determinants.md) of $A$ is not zero, i.e. $\det(A) \ne 0_F$.
>- The [reduced row echelon form](../../Linear%20Algebra/Systems%20of%20Linear%20Equations/Row%20Echelon%20Forms.md) of $A$ is the [identity matrix](#Identity%20Matrix) $I_n$.
>- The [system of linear equations](../../Linear%20Algebra/Systems%20of%20Linear%20Equations/Systems%20of%20Linear%20Equations.md) $A \vec{x} = \vec{b}$ has a single [solution](../../Linear%20Algebra/Systems%20of%20Linear%20Equations/Systems%20of%20Linear%20Equations.md) for each $\vec{b} \in F^n$.
>- The [column space](../Matrices.md#Matrix%20Spaces) of $A$ is the [vector space](../Row%20and%20Column%20Vectors.md) $F^n$.
>- The [row space](../Matrices.md#Matrix%20Spaces) of $A$ is the [vector space](../Row%20and%20Column%20Vectors.md) $F^{1 \times n}$.
>- The [rank](../Matrices.md#Matrix%20Spaces) of $A$ is $n$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antidistributivity of Matrix Inversion
>
>[Matrix inversion](#Matrix%20Invertibility) is antidistributive over [matrix products](../Matrix%20Operations.md) - if $A, B \in F^{n \times}$ and their [matrix product](../Matrix%20Operations.md) $AB$ are [invertible](#Matrix%20Invertibility), then:
>
>$$
>(AB)^{-1} = B^{-1} A^{-1}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!ALGORITHM] Algorithm: Matrix Inversion
>
>To find the [inverse](#Matrix%20Invertibility) of an [invertible matrix](#Matrix%20Invertibility) $A \in F^{n \times n}$:
>1. Notate an $n\times 2n$-[matrix](../Matrices.md) $(A\mid I_n)$ by sticking the [identity matrix](#Identity%20Matrix) $I_n$ to the right of $A$.
>2. Perform [Gauss-Jordan elimination](../../Linear%20Algebra/Systems%20of%20Linear%20Equations/Systems%20of%20Linear%20Equations.md) on $(A \mid I_n)$. If $A$ is indeed [invertible](#Matrix%20Invertibility), the final result will be $(I_n \mid A^{-1})$.
>
>>[!EXAMPLE]-
>>
>>Let's find the inverse of $A = \begin{bmatrix}6 & 8 & 3 \\ 4 & 7 & 3 \\ 1 & 2 & 1\end{bmatrix}$. Notate
>>
>>$$
>>[A\mid I_3] = \left[\begin{array}{ccc|ccc}6 & 8 & 3 & 1 & 0 & 0\\ 4 & 7 & 3 & 0 & 1 & 0 \\ 1 & 2 & 1 & 0 & 0 & 1\end{array}\right]
>>$$
>>
>>Perform  [Gauss-Jordan elimination](../../Linear%20Algebra/Systems%20of%20Linear%20Equations/Systems%20of%20Linear%20Equations.md):
>>
>>$$
>>\left[\begin{array}{ccc|ccc}6 & 8 & 3 & 1 & 0 & 0\\ 4 & 7 & 3 & 0 & 1 & 0 \\ 1 & 2 & 1 & 0 & 0 & 1\end{array}\right] \approx \left[\begin{array}{ccc|ccc}1 & 2 & 1 & 0 & 0 & 1 \\ 6 & 8 & 3 & 1 & 0 & 0\\ 4 & 7 & 3 & 0 & 1 & 0 \end{array}\right] \approx \left[\begin{array}{ccc|ccc}1 & 2 & 1 & 0 & 0 & 1 \\ 0 & -4 & -3 & 1 & 0 & -6\\ 0 & -1 & -1 & 0 & 1 & -4 \end{array}\right]
>>$$
>>
>>$$
>>\left[\begin{array}{ccc|ccc}1 & 2 & 1 & 0 & 0 & 1 \\ 0 & -4 & -3 & 1 & 0 & -6\\ 0 & -1 & -1 & 0 & 1 & -4 \end{array}\right] \approx \left[\begin{array}{ccc|ccc}1 & 0 & -1 & 0 & 2 & -7 \\ 0 & 1 & 1 & 0 & -1 & 4\\ 0 & 0 & 1 & 1 & -4 & 10 \end{array}\right] \approx \left[\begin{array}{ccc|ccc}1 & 0 & 0 & 1 & -2 & 3 \\ 0 & 1 & 0 & -1 & 3 & -6\\ 0 & 0 & 1 & 1 & -4 & 10 \end{array}\right]
>>$$
>>
>>$$
>>A^{-1} = \begin{bmatrix}1 & -2 & 3 \\ -1 & 3 & -6 \\ 1 & -4 & 10\end{bmatrix}
>>$$
>>
>

>[!THEOREM] Theorem: Inverting $2\times2$-Matrices
>
>A $2\times 2$-[matrix](./Square%20Matrices.md) $A = \begin{bmatrix}a & b \\ c & d\end{bmatrix}$ is [invertible](#Matrix%20Invertibility) if and only if
>
>$$
>ad - bc \ne 0
>$$
>
>If $A$ is [invertible matrix](#Matrix%20Invertibility), then
>
>$$
>A^{-1} = \frac{1}{ad-bc}\begin{bmatrix}d & -b \\ -c & a\end{bmatrix}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>