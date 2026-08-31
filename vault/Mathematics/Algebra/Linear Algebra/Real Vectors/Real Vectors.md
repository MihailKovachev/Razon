---
tags:
  - linear-algebra
  - algebra
  - mathematics
---

# Real Vectors

>[!DEFINITION] Definition: Real Column Vector
>
>A **real column vector** is a [column vector](../../Matrices/Row%20and%20Column%20Vectors.md) $\boldsymbol{v} \in \mathbb{R}^n$ over the [real numbers](../../Fields/The%20Real%20Numbers/The%20Real%20Numbers.md).
>

>[!DEFINITION] Definition: Real Row Vector
>
>A **real row vector** is a [row vector](../../Matrices/Row%20and%20Column%20Vectors.md) $\boldsymbol{v} \in \mathbb{R}^{n \times 1}$ over the [real numbers](../../Fields/The%20Real%20Numbers/The%20Real%20Numbers.md).
>

## Operations

### Dot Product

>[!DEFINITION] Definition: Real Dot Product
>
>The **dot product** of two [real column vectors](./Real%20Vectors.md) $\boldsymbol{u} = \begin{bmatrix} u_1 & \cdots & u_n \end{bmatrix}^\mathsf{T} \in \mathbb{R}^n$ and $\boldsymbol{v} = \begin{bmatrix} v_1 & \cdots & v_n \end{bmatrix}^\mathsf{T} \in \mathbb{R}^n$ is defined as:
>
>$$\boldsymbol{u} \cdot \boldsymbol{v} \overset{\text{def}}{=} \sum_{k = 1}^n u_k v_k$$
>
>>[!TIP]
>>
>>The dot product of two [real column vectors](./Real%20Vectors.md) is equivalent to the [matrix product](../../Matrices/Matrices.md#Matrix%20Product) of the [transpose](../../Matrices/Matrix%20Operations.md) of $\boldsymbol{u}$ with $\boldsymbol{v}$:
>>
>>$$
>>\boldsymbol{u} \cdot \boldsymbol{v} = \boldsymbol{u}^\mathsf{T} \boldsymbol{v}
>>$$
>>
>

>[!THEOREM] Theorem: Structure of the Real Vector Space
>
>The [dot product](#Dot%20Product) is an [inner product](../../Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md) on $\mathbb{R}^n$ $(\mathbb{R}^n, \mathbb{R},+,\cdot)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Orthonormality of the Real Standard Basis
>
>The [standard basis](./Real%20Vectors.md) of the [real vector space](./Real%20Vectors.md) $(\mathbb{R}^n, \mathbb{R}, +, \cdot)$ is [orthonormal](../../Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md#Orthogonality).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Dot Product and Transpose
>
>The [dot product](#Dot%20Product) has the following property for all $\boldsymbol{v}, \boldsymbol{w} \in \mathbb{R}^n$ ($n \ge 2$) and all [matrices](../../Matrices/Real%20Matrices/Real%20Matrices.md) $A \in \mathbb{R}^{n \times n}$:
>
>$$\boldsymbol{v} \cdot (A\boldsymbol{w}) = (A^{\mathsf{T}}\boldsymbol{v})\cdot \boldsymbol{w}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

