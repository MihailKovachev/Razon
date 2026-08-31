---
tags:
    - matrices
    - algebra
    - mathematics
---

# Jordan Blocks

>[!DEFINITION] Definition: Jordan Block
>
>Let $F$ be a [field](../../Fields/Fields.md).
>
>A **Jordan block** is a [matrix](../Matrices.md) $A \in F^{n \times n}$ with the following properties:
>
>- All diagonal entries have the same value $\lambda \in F$: $a_{i,i} = \lambda$ for $1 \le i \le n$.
>- All entries directly above the diagonal are equal to one: $a_{i, i+1} = 1$ for $1 \le i \le n - 1$.
>- All other entries are zero: $a_{i,j} = 0$ otherwise.
>
>$$A = \begin{bmatrix} \lambda & 1 & 0 & \cdots & 0 \\ 0 & \lambda & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda & 1 \\ 0 & 0 & \cdots & 0 & \lambda \end{bmatrix}$$
>
>>[!NOTATION]
>>
>>Such a [Jordan block](./Jordan%20Blocks.md) is often denoted as $J_{n}(\lambda)$.
>>
>

It is obvious that each [Jordan block](./Jordan%20Blocks.md) is a [square matrix](./Square%20Matrices.md), specifically an [upper triangular matrix](./Upper%20Triangular%20Matrices.md)
