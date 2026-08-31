---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Complex Vectors

>[!DEFINITION] Definition: Complex Column Vector
>
>A **complex column vector** is a [column vector](../../Matrices/Row%20and%20Column%20Vectors.md) $\vec{v} \in \mathbb{C}^n$ over the [complex numbers](../../Fields/The%20Complex%20Numbers/Complex%20Numbers.md).
>

>[!DEFINITION] Definition: Complex Row Vector
>
>A **complex row vector** is a [row vector](../../Matrices/Row%20and%20Column%20Vectors.md) $\vec{v} \in \mathbb{C}^{1\times n}$ over the [complex numbers](../../Fields/The%20Complex%20Numbers/Complex%20Numbers.md).
>

## Operations

### Dot Product

>[!DEFINITION] Definition: Complex Dot Product
>
>The **dot product** of two [complex column vectors](./Complex%20Vectors.md) $\vec{u} = \begin{bmatrix} u_1 & \cdots & u_n \end{bmatrix}^\mathsf{T} \in \mathbb{C}^n$ and $\vec{v} = \begin{bmatrix} v_1 & \cdots & v_n \end{bmatrix}^\mathsf{T} \in \mathbb{C}^n$ is defined as:
>
>$$
>\vec{u} \cdot \vec{v} \overset{\text{def}}{=} \sum_{k = 1}^n \overline{u_k} v_k
>$$
>


The [dot product](#Dot%20Product) $\vec{u}\cdot \vec{v}$ of two [complex column vectors](./Complex%20Vectors.md) is equivalent to the [matrix product](../../Matrices/Matrices.md#Matrix%20Product) of the [Hermitian transpose](../../Matrices/Complex%20Matrices/Complex%20Matrices.md) of $\vec{u}$ with $\vec{v}$:

$$
\vec{u} \cdot \vec{v} = \vec{u}^\dagger \vec{v}
$$

>[!NOTATION] Bra-Ket Notation
>
>The [dot product](#Dot%20Product) $\vec{u} \cdot \vec{v}$ can be written using [bra-ket notation](../../Matrices/Row%20and%20Column%20Vectors.md) in the following way:
>
>$$
>\left\langle u \vert v \right\rangle
>$$
>

>[!THEOREM] Theorem: Structure of the Real Vector Space
>
>The [dot product](#Dot%20Product) is an [inner product](../../Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md) on $(\mathbb{C}^n, \mathbb{C},+,\cdot)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

### Outer Product

>[!DEFINITION] Definition: Outer Product
>
>Let $\mathbf{u} = \begin{bmatrix} u_1 & \cdots & u_m \end{bmatrix}^{\mathsf{T}} \in \mathbb{C}^m$ and $\mathbf{v} = \begin{bmatrix} v_1 & \cdots & v_n \end{bmatrix}^{\mathsf{T}}  \in \mathbb{C}^n$ be [complex column vectors](./Complex%20Vectors.md).
>
>The **outer product** $\mathbf{u} \otimes \mathbf{v}$ is the $m\times n$-[ matrix](../../Matrices/Complex%20Matrices/Complex%20Matrices.md) whose entry at the $i$-the row and the $j$-th column is the product of $u$'s $i$-th component and the [complex conjugate](../../Fields/The%20Complex%20Numbers/Complex%20Numbers.md#Operations) of $v$'s $j$-th component:
>
>$$
>\mathbf{u} \otimes \mathbf{v} = \begin{bmatrix} u_1 \\ \vdots \\ u_m \end{bmatrix} \otimes \begin{bmatrix} v_1 \\ \vdots \\ v_n \end{bmatrix} \overset{\text{def}}{=} \begin{bmatrix} u_{1} \bar{v}_{1} & u_{1} \bar{v}_{2} & \cdots & u_{1} \bar{v}_{n} \\ u_{2} \bar{v}_{1} & u_{2} \bar{v}_{2} & \cdots & u_{2} \bar{v}_{n}\\\vdots & \vdots & \ddots & \vdots \\ u_{m} \bar{v}_{1} & u_{m} \bar{v}_{2} & \cdots & u_{m} \bar{v}_{n} \end{bmatrix}
>$$
>

The [outer product](#Outer%20Product) is equivalent to the [matrix product](../../Matrices/Matrices.md#Matrix%20Product) of $\mathbf{u}$ with the [Hermitian transpose](../../Matrices/Complex%20Matrices/Complex%20Matrices.md#Operations) of $\mathbf{v}$:

$$
\mathbf{u} \otimes \mathbf{v} = \mathbf{u}\mathbf{v}^{\dagger}
$$

>[!NOTATION] Bra-Ket Notation
>
>The [outer product](#Outer%20Product) $\mathbf{u} \otimes \mathbf{v}$ can be written using [bra-ket notation](../../Matrices/Row%20and%20Column%20Vectors.md) in the following way:
>
>$$
>\left\vert u \right\rangle \left\langle v \right\vert
>$$
>

>[!THEOREM] Theorem: Rank of the Outer Product
>
>The [outer product](#Outer%20Product) of two non-zero [complex vectors](./Complex%20Vectors.md) has [rank](../../Matrices/Matrices.md#Matrix%20Spaces) $1$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Sesqulinearity of the Outer Product
>
>The [outer product](#Outer%20Product) is linear in the first argument:
>
>$$
>(\lambda \mathbf{u}_1 + \mu \mathbf{u}_2) \otimes \mathbf{v} = \lambda \cdot (\mathbf{u}_1 \otimes \mathbf{v}) + \mu \cdot (\mathbf{u}_2 \otimes \mathbf{v})
>$$
>
>The [outer product](#Outer%20Product) is conjugate-linear in the second argument:
>
>$$
>\mathbf{u} \otimes (\lambda \mathbf{v}_1 + \mu \mathbf{v}_2) = \bar{\lambda} \cdot (\mathbf{u} \otimes \mathbf{v}_1) + \bar{\mu} \cdot (\mathbf{u} \otimes \mathbf{v}_2) 
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Hermitian Transpose of the Outer Product
>
>The [Hermitian transpose](../../Matrices/Complex%20Matrices/Complex%20Matrices.md#Operations) of the [outer product](#Outer%20Product) reverses the order:
>
>$$
>(\mathbf{u} \otimes \mathbf{v})^{\dagger} = \mathbf{v} \otimes \mathbf{u}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>