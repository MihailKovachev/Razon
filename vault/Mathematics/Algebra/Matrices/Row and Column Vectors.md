---
tags:
  - linear-algebra
  - algebra
  - mathematics
---

# Row and Column Vectors

Two types of [matrices](./Matrices.md#Matrices) are very important for most of mathematics and physics.

>[!DEFINITION] Definition: Row Vector
>
>An $n$-dimensional **row vector** is an $1\times n$-[matrix](./Matrices.md#Matrices):
>
>$$
>\begin{bmatrix}v_1 & \cdots & v_m\end{bmatrix} \in F^{1\times n}
>$$
>
>>[!NOTATION] Bra-Notation
>>
>>Sometimes, a [row vector](./Row%20and%20Column%20Vectors.md) $\mathbf{v}$ can be written as $\left\langle v \right\vert$.  This is known as **bra-notation**.
>>
>

>[!DEFINITION] Definition: Column Vector
>
>An $m$-dimensional **column vector** is an $m\times 1$-[matrix](./Matrices.md#Matrices):
>
>$$
>\begin{bmatrix}v_1 \\ \vdots \\ v_m\end{bmatrix} \in F^{m\times 1}
>$$
>
>>[!NOTATION] Ket-Notation
>>
>>Sometimes, a [column vector](./Row%20and%20Column%20Vectors.md) $\mathbf{v}$ can be written as $\left\vert v \right\rangle$.  This is known as **ket-notation**.
>>
>
>>[!NOTATION]
>>
>>We usually denote the [set](../../Set%20Theory/Sets.md) of all $m$-dimensional column vectors by $F^m$ instead of $F^{m\times 1}$.
>>
>

>[!NOTATION]
>
>It is very common to denote row and column vectors with an arrow above a lowercase letter: $\vec{u}, \vec{v}$, etc.
>

>[!THEOREM] Theorem: Standard Basis
>
>If $(F^n, F, +, \cdot)$ is the [vector space](../Vector%20Spaces/Vector%20Spaces.md) of the $n$-dimensional [column vectors](./Row%20and%20Column%20Vectors.md) over some [field](../Fields/Fields.md) $F$, then the $n$-[tuple](../../Set%20Theory/Tuples.md)
>
>$$
>\left(\underset{n\text{ vectors}}{\underbrace{\vec{e}_1 = \begin{bmatrix}1_F \\ 0_F \\ \vdots \\ 0_F\end{bmatrix}, \vec{e}_2 = \begin{bmatrix}0_F \\ 1_F \\ \vdots \\ 0_F\end{bmatrix},\cdots, \vec{e}_n = \begin{bmatrix}0_F \\ 0_F \\ \vdots \\ 1_F\end{bmatrix}}}\right)
>$$
>
>is an [ordered basis](../Vector%20Spaces/Hamel%20Bases.md#Ordered%20Bases) for $(F^n, F, +, \cdot)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Standard Basis
>>
>>This [ordered basis](../Vector%20Spaces/Hamel%20Bases.md#Ordered%20Bases) is known as the **standard basis** of $(F^n, F, +, \cdot)$.
>>
>