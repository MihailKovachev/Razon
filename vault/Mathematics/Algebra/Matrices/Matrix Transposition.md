---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Matrix Transposition

>[!DEFINITION] Definition: Matrix Transposition
>
>The **transpose** of a [matrix](./Matrices.md) $A \in F^{m\times n}$ is the [matrix](./Matrices.md#Matrices) $A^\mathsf{T} \in F^{n \times m}$ obtained by switching the rows and the columns of $A$, i.e. the $i$-th row of $A$ is the $i$-th column of $A^\mathsf{T}$ and vice versa:
>
>$$
>\begin{bmatrix}a_{11} & \cdots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1} & \cdots & a_{mn}\end{bmatrix}^\mathsf{T} \overset{\text{def}}{=} \begin{bmatrix}a_{11} & \cdots & a_{m1} \\ \vdots & \ddots & \vdots \\ a_{1n} & \cdots & a_{mn}\end{bmatrix}
>$$
>
>>[!TIP]
>>
>>The entry in the $i$-th row and the $j$-th column of $A$ is the entry in the $j$-th row and the $i$-th column of $A^\mathsf{T}$.
>>
>
>>[!TIP]
>>
>>The number of rows in $A^\mathsf{T}$ is equal to the number columns in $A$ and the number of columns in $A^\mathsf{T}$ is equal to the number of rows in $A$.
>>
>

>[!THEOREM] Theorem: Distributivity of Transposition
>
>[Matrix transposition](./Matrix%20Transposition.md) is distributive over [matrix addition](./Matrix%20Operations.md) and [scalar multiplication](./Matrices.md#Matrix%20Operations):
>
>$$(A + B)^\mathsf{T} = A^\mathsf{T} + B^\mathsf{T}$$
>
>$$(\lambda A)^\mathsf{T} = \lambda A^\mathsf{T}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antidistributivity of Transposition
>
>[Matrix transposition](./Matrix%20Transposition.md) is antidistributive over [matrix products](./Matrices.md#Matrix%20Product):
>
>$$(AB)^\mathsf{T} = B^\mathsf{T} A^\mathsf{T}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>