---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Kronecker Product

>[!DEFINITION] Definition: Kronecker Product
>
>Let $A = (a_{ij}) \in F^{m \times n}$ be an $m \times n$-[matrix](./Matrices.md) and let $B = (b_{ij}) \in F^{p \times q}$ be a $p \times q$-[matrix](./Matrices.md).
>
>The **Kronecker product** of $A$ with $B$ is a $pm \times nq$-[matrix](./Matrices.md) defined as
>
>$$
>\begin{bmatrix}
>a_{11} B & \cdots & a_{1n} B \\
>\vdots & \ddots & \vdots \\
>a_{m1} B & \cdots & a_{mn} B
>\end{bmatrix}
>$$
>
>>[!NOTATION]
>>
>>The [Kronecker product](./Matrices.md#Kronecker%20Product) is written in one of the following ways:
>>
>>$$A \otimes B \qquad A \otimes_{\text{Kron}} B$$
>>
>

>[!EXAMPLE]-
>
>$$\begin{aligned}\begin{bmatrix}1 & 2 & 3 \\ 4 & 5 & 6\end{bmatrix}
>\otimes
>\begin{bmatrix}
>-1 & -2 & -3 \\
>-4 & -5 & -6 \\
>-7 & -8 & -9
>\end{bmatrix}
>&=
>\begin{bmatrix}
>1 \cdot \begin{bmatrix} -1 & -2 & -3 \\ -4 & -5 & -6 \\ -7 & -8 & -9 \end{bmatrix} & 2 \cdot \begin{bmatrix} -1 & -2 & -3 \\ -4 & -5 & -6 \\ -7 & -8 & -9 \end{bmatrix} & 3 \cdot \begin{bmatrix} -1 & -2 & -3 \\ -4 & -5 & -6 \\ -7 & -8 & -9 \end{bmatrix} \\
>4 \cdot \begin{bmatrix} -1 & -2 & -3 \\ -4 & -5 & -6 \\ -7 & -8 & -9 \end{bmatrix} & 5 \cdot \begin{bmatrix} -1 & -2 & -3 \\ -4 & -5 & -6 \\ -7 & -8 & -9 \end{bmatrix} & 6 \cdot \begin{bmatrix} -1 & -2 & -3 \\ -4 & -5 & -6 \\ -7 & -8 & -9 \end{bmatrix}
>\end{bmatrix} \\
>&= 
>\begin{bmatrix}
>1 \cdot (-1) & 1 \cdot (-2) & 1 \cdot (-3) & 2 \cdot (-1) & 2 \cdot (-2) & 2 \cdot (-3) & 3 \cdot (-1) & 3 \cdot (-2) & 3 \cdot (-3) \\
>1 \cdot (-4) & 1 \cdot (-5) & 1 \cdot (-6) & 2 \cdot (-4) & 2 \cdot (-4) & 2 \cdot (-6) & 3 \cdot (-4) & 3 \cdot (-5) & 3 \cdot (-6) \\
>1 \cdot (-7) & 1 \cdot (-8) & 1 \cdot (-9) & 2 \cdot (-7) & 2 \cdot (-8) & 2 \cdot (-9) & 3 \cdot (-7) & 3 \cdot (-8) & 3 \cdot (-9) \\
>4 \cdot (-1) & 4 \cdot (-2) & 4 \cdot (-3) & 5 \cdot (-1) & 5 \cdot (-2) & 5 \cdot (-3) & 6 \cdot (-1) & 6 \cdot (-2) & 6 \cdot (-3) \\
>4 \cdot (-4) & 4 \cdot (-5) & 4 \cdot (-6) & 5 \cdot (-4) & 5 \cdot (-4) & 5 \cdot (-6) & 6 \cdot (-4) & 6 \cdot (-5) & 6 \cdot (-6) \\
>4 \cdot (-7) & 4 \cdot (-8) & 4 \cdot (-9) & 5 \cdot (-7) & 5 \cdot (-8) & 5 \cdot (-9) & 6 \cdot (-7) & 6 \cdot (-8) & 6 \cdot (-9)
>\end{bmatrix} \\
>&=
>\begin{bmatrix}
>-1 & -2 & -3 & -2 & -4 & -6 & -3 & -6 & -9 \\
>-4 & -5 & -6 & -8 & -10 & -12 & -12 & -15 & -18 \\
>-7 & -8 & -9 & -14 & -16 & -18 & -21 & -24 & -27 \\
>-4 & -8 & -12 & -5 & -10 & -15 & -6 & -12 & -18 \\
>-16 & -20 & -24 & -20 & -25 & -30 & -24 & -30 & -36 \\
>-28 & -32 & -36 & -35 & -40 & -45 & -42 & -48 & -54
>\end{bmatrix} 
>\end{aligned}
>$$
>

>[!THEOREM] Theorem: Associativity of the Kronecker Product
>
>The [Kronecker product](./Matrices.md#Kronecker%20Product) is associative:
>
>$$(A \otimes B) \otimes C = A \otimes (B \otimes C)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Bilinearity of the Kronecker Product
>
>The [Kronecker product](./Matrices.md#Kronecker%20Product) is bilinear:
>
>$$\begin{aligned}A \otimes (\lambda B + \mu C) &= \lambda \cdot (A \otimes B) + \mu \cdot (A \otimes C) \\ (\lambda A + \mu B) \otimes C &= \lambda \cdot (A \otimes C) + \mu \cdot (B \otimes C) \end{aligned}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Mixed-Product Property
>
>The [Kronecker product](./Matrices.md#Kronecker%20Product) has the following property whenever the [matrix products](./Matrices.md#Matrix%20Product) $AC$ and $BD$ are possible:
>
>$$(A \otimes B) (C \otimes D) = (AC) \otimes (BD)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

