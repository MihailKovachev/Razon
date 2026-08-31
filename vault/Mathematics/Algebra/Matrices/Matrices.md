---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Matrices

>[!DEFINITION] Definition: Matrix
>
>Let $S$ be a [set](../../Set%20Theory/Sets.md) and let $m,n \in \mathbb{N}_{\ge 1}$.
>
>An $m \times n$**-matrix** over $S$ is a [function](../../Analysis/Functions/Functions.md) of the following form:
>
>$$A: \{1, \dotsc, m\} \times \{1, \dotsc n\} \to S$$
>
>>[!NOTATION]
>>
>>[Matrices](./Matrices.md) are usually denoted using uppercase Latin letters: $A, B, C, \dotsc$.
>>
>>Given $i \in \{1, \dotsc, m\}$ and $j \in \{1, \dotsc n\}$ we write $A_{ij}$ or $A_{i,j}$ instead of $A(i,j)$.
>>
>>Furthermore, we often specify $A$ as a rectangular array with $m$ rows and $n$ columns, where $A_{i,j}$ is the **entry** or **component** of $A$ at the $i$-th row and $j$-th column:
>>
>>$$\begin{bmatrix}A_{1,1} & A_{1,2} & \cdots & A_{1,n} \\ A_{2,1} & A_{2,2} & \cdots & A_{2,n} \\ \vdots & \vdots & \ddots & \vdots \\  A_{m,1} & A_{m,2} & \cdots & A_{m,n}\end{bmatrix}$$
>>
>>It is common to also write $a_{i,j}$ instead of $A_{i,j}$.
>>
>>The [set](../../Set%20Theory/Sets.md) of all [$m\times n$-matrices](./Matrices.md) over $S$ is denoted by $S^{m \times n}$ or $\text{Mat}(m,n,S)$.
>>
>

>[!DEFINITION] Definition: Matrix Addition and Subtraction
>
>The **addition** and **subtraction** of two $m\times n$-[matrices](#Matrices) $A, B \in F^{m \times n}$ over the same [field](../Fields/Fields.md) $F$ is another $m\times n$-[matrix](#Matrices) $C \in F^{m \times n}$ such that $c_{ij} = a_{ij} \pm b_{ij}$:
>
>$$
>A \pm B = \begin{bmatrix} a_{11} & \cdots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1} & \cdots & a_{mn} \end{bmatrix} \pm \begin{bmatrix} b_{11} & \cdots & b_{1n} \\ \vdots & \ddots & \vdots \\ b_{m1} & \cdots & b_{mn} \end{bmatrix} \overset{\text{def}}{=} \begin{bmatrix} a_{11} \pm b_{11} & \cdots & a_{1n} \pm b_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1} \pm b_{m1}  & \cdots & a_{mn} \pm b_{mn} \end{bmatrix} = C
>$$
>

>[!DEFINITION] Definition: Scalar Multiplication
>
>The **scalar multiplication** of a [matrix](#Matrices) $A \in F^{m \times n}$ with a [field](../Fields/Fields.md) element $\mu \in F$ is another $m\times n$-[matrix](#Matrices) whose elements are the elements of $A$ multiplied by $\mu$:
>
>$$\mu \cdot A = \mu \cdot \begin{bmatrix}a_{11} & \cdots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1} & \cdots & a_{mn}\end{bmatrix} \overset{\text{def}}{=} \begin{bmatrix} \mu \cdot a_{11} & \cdots & \mu \cdot a_{1n} \\ \vdots & \ddots & \vdots \\ \mu \cdot a_{m1} & \cdots & \mu \cdot a_{mn}\end{bmatrix} \in F^{m \times n}$$
>
>>[!NOTATION]
>>
>>The dot ($\cdot$) is usually omitted, i.e. $\mu A$ instead of $\mu \cdot A$.
>>
>

>[!THEOREM] Theorem: Vector Space of Matrices
>
>The [set](../../Set%20Theory/Sets.md) $F^{m\times n}$ of all $m \times n$-[matrices](./Matrices.md) and the [field](../Fields/Fields.md) $F$ form a [vector space](../Vector%20Spaces/Vector%20Spaces.md) $(F^{m\times n}, F, +, \cdot)$ together with the [matrix addition](#Matrix%20Operations) and [scalar multiplication](#Matrix%20Operations) operations.
>
>>[!TIP] Tip: Zero Vector
>>
>>The [zero](../Vector%20Spaces/Vector%20Spaces.md) of $(F^{m\times n}, F, +, \cdot)$ is the [zero matrix](./Matrices.md) of $F^{m\times n}$.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>


We are mostly interested in [matrices](#Matrices) over the [real numbers](../Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) (**real matrices**) or in  [matrices](#Matrices) over the [complex numbers](../Fields/The%20Complex%20Numbers/Complex%20Numbers.md) (**complex matrices**).

## Matrix Spaces

>[!DEFINITION] Definition: Row Space
>
>The **row space** of an $m\times n$-[matrix](#Matrices)
>
>$$
>A = \begin{bmatrix} - & \mathbf{a}_1 & - \\ - & \vdots & - \\ - & \mathbf{a}_m & - \end{bmatrix}
>$$
>
>is the [span](../Vector%20Spaces/Span.md) $\langle \mathbf{a}_1, \cdots, \mathbf{a}_m \rangle$ of its [rows](./Row%20and%20Column%20Vectors.md).
>

>[!DEFINITION] Definition: Column Space
>
>The **column space** of an $m\times n$-[matrix](#Matrices)
>
>$$
>A = \begin{bmatrix}\mid & \mid & \mid \\ \mathbf{a}_1 & \cdots & \mathbf{a}_n \\ \mid & \mid & \mid\end{bmatrix}
>$$
>
>is the [span](../Vector%20Spaces/Span.md) $\langle \mathbf{a}_1, \cdots, \mathbf{a}_n \rangle$ of its [columns](./Row%20and%20Column%20Vectors.md).
>

>[!DEFINITION] Definition: Null Space
>
>The **null space** of an $m\times n$-[matrix](#Matrices) $A \in F^{m \times n}$ is the [set](../../Set%20Theory/Sets.md) of all [column vectors](./Row%20and%20Column%20Vectors.md) $\mathbf{v} \in F^n$ such that the [matrix product](./Matrix%20Operations.md#Matrix%20Product) $A\mathbf{v}$ is the [zero vector](../Vector%20Spaces/Vector%20Spaces.md) of $F^n$:
>
>$$
>\{\mathbf{v}\in F^{n} \mid A\mathbf{v}=\mathbf{0}_F\}
>$$
>
>>[!NOTATION]
>>
>>$$
>>\operatorname{Null}(A) \qquad \operatorname{N}(A)
>>$$
>>
>

>[!THEOREM] Theorem: Rank Equality
>
>The [row space](#Matrix%20Spaces) and the [column space](#Matrix%20Spaces) of a given [matrix](#Matrix%20Spaces) always have the same [dimension](../Vector%20Spaces/Hamel%20Bases.md#Dimension).
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Rank
>>
>>This [dimension](../Vector%20Spaces/Hamel%20Bases.md#Dimension) is known as the **rank** of the [matrix](#Matrix%20Spaces).
>>
>