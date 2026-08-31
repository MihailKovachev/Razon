---
tags:
  - linear-algebra
  - algebra
  - mathematics
---

# Determinants

>[!DEFINITION] Definition: Determinant
>
>The **determinant** of a [square matrix](./Square%20Matrices.md) $M \in F^{n \times n}$ is the [determinant](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Vector%20Space%20Endomorphisms.md) of the [linear transformation](../../../Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md) $f: F^n \to F^n$ defined as $f(\mathbf{v}) = M\mathbf{v}$.
>
>>[!NOTATION]
>>
>>$$\det M \qquad |M|$$
>>
>
>>[!EXAMPLE]-
>>
>>Let $M = \begin{bmatrix} 1 & 2 \\ 3 & 4\end{bmatrix}$ be a [real matrix](../Real%20Matrices/Real%20Matrices.md). We use the [determinant form](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Vector%20Space%20Endomorphisms.md#Determinants) $\delta: F^2 \times F^2 \to F$ defined on the [standard basis](../Row%20and%20Column%20Vectors.md) as $\delta (\mathbf{e}_1, \mathbf{e}_2) = 1$.
>>
>>By the definition of a [determinant](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Vector%20Space%20Endomorphisms.md), we have:
>>
>>$$\det M \cdot \delta (\mathbf{e}_1, \mathbf{e}_2) = \delta (f(\mathbf{e}_1), f(\mathbf{e}_2))$$
>>
>>Since $\delta (\mathbf{e}_1, \mathbf{e}_2) = 1$ by definition, we have:
>>
>>$$\begin{aligned}\det M & = \delta (f(\mathbf{e}_1), f(\mathbf{e}_2)) \\ & = \delta \left( M\begin{bmatrix}1 \\ 0\end{bmatrix}, M \begin{bmatrix}0 \\ 1\end{bmatrix} \right) \\ & = \delta \left(\begin{bmatrix}1 \\ 3\end{bmatrix}, \begin{bmatrix}2 \\ 4\end{bmatrix}\right)\end{aligned}$$
>>
>>We now use the fact that $\delta$ is [multilinear](../../../Analysis/Functional%20Analysis/Linearity/Multilinear%20Transformations.md):
>>
>>$$\begin{aligned} \delta \left(\begin{bmatrix}1 \\ 3\end{bmatrix}, \begin{bmatrix}2 \\ 4\end{bmatrix}\right) & = \delta(1 \cdot \mathbf{e}_1 + 3 \cdot \mathbf{e}_2, 2\cdot \mathbf{e}_1 + 4 \cdot \mathbf{e}_2) \\ & = 1 \cdot \delta (\mathbf{e}_1, 2\cdot \mathbf{e}_1 + 4 \cdot \mathbf{e}_2) + 3 \cdot \delta (\mathbf{e}_2, 2\cdot \mathbf{e}_1 + 4 \cdot \mathbf{e}_2) \\ & = 1 \cdot 2 \cdot \delta(\mathbf{e}_1, \mathbf{e}_1) + 1 \cdot 4 \cdot \delta(\mathbf{e}_1, \mathbf{e}_2) + 3\cdot 2 \cdot \delta(\mathbf{e}_2, \mathbf{e}_1) + 3 \cdot 4 \cdot \delta (\mathbf{e}_2, \mathbf{e}_2) \end{aligned}$$
>>
>>Now we use the fact that $\delta$ is [alternating](../../../Analysis/Functional%20Analysis/Linearity/Alternating%20Multilinear%20Forms.md):
>>
>>$$\begin{aligned}1 \cdot 2 \cdot \delta(\mathbf{e}_1, \mathbf{e}_1) + 1 \cdot 4 \cdot \delta(\mathbf{e}_1, \mathbf{e}_2) + 3\cdot 2 \cdot \delta(\mathbf{e}_2, \mathbf{e}_1) + 3 \cdot 4 \cdot \delta (\mathbf{e}_2, \mathbf{e}_2) & = 1 \cdot 2 \cdot 0 + 1 \cdot 4 \cdot \delta(\mathbf{e}_1, \mathbf{e}_2) + 3\cdot 2 \cdot \delta(\mathbf{e}_2, \mathbf{e}_1) + 3 \cdot 4 \cdot 0 \\ & = 0 + 4 -6 + 0 \\ & = -2\end{aligned}$$
>>
>

>[!THEOREM] Theorem: Determinant of Matrix Product
>
>
>The [determinant](./Determinants.md) of the [product](../Matrix%20Operations.md#Matrix%20Product) of two [square matrices](./Square%20Matrices.md) $A, B \in F^{n \times n}$ is the [product](../../Fields/Fields.md) of the [determinants](./Determinants.md) of $A$ and $B$:
>
>$$\det(AB) = \det(A) \det(B) = \det(B) \det(A) = \det(BA)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Determinant of the Transpose
>
>The [determinant](./Determinants.md) of a [square matrix](./Square%20Matrices.md) is equal to the [determinant](./Determinants.md) of its [transpose](../Matrix%20Operations.md#Transposition):
>
>$$\det(A) = \det(A^\mathsf{T})$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Determinant of the Inverse
>
>If $A \in F^{n \times n}$ is [invertible](./Matrix%20Invertibility.md), then the [determinant](./Determinants.md) of $A^{-1}$ is the reciprocal of $A$'s [determinants](./Determinants.md):
>
>$$\det(A^{-1}) = \frac{1}{\det(A)}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Determinant of Scalar Multiplication
>
>The [determinant](./Determinants.md) has the following property for all [square matrices](./Square%20Matrices.md) $A \in F^{n \times n}$ and all $\alpha \in F$:
>
>$$\det(\alpha A) = \alpha^n \det (A)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Determinant via Columns
>
>Let $A \in F^{n \times n}$ be a [square matrix](./Square%20Matrices.md) and let $\delta: (F^n)^n \to F$ be the [determinant form](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Vector%20Space%20Endomorphisms.md#Determinants) defined on the [standard basis](../Row%20and%20Column%20Vectors.md) as $\delta(\mathbf{e}_1, \dotsc, \mathbf{e}_n) = 1$.
>
>If $\mathbf{a}_1, \dotsc, \mathbf{a}_n$ are the [columns](../Row%20and%20Column%20Vectors.md) of $A$, then the [determinant](./Determinants.md) of $A$ is equal to $\delta(\mathbf{a}_1, \dotsc, \mathbf{a}_n)$:
>
>$$\det A = \delta(\mathbf{a}_1, \dotsc, \mathbf{a}_n)$$
>
>>[!TIP] Tip: Row and Column Operations
>>
>>From this and the fact that $\det A = \det A^{\mathsf{T}}$ we can immediately derive the effects of row and column operations on the [determinant](./Determinants.md) of $A$:
>>- Swapping any two columns or any two rows switches the sign of the [determinant](./Determinants.md).
>>- Multiplying a row or column by some $\lambda \in F$, results in the [determinant](./Determinants.md) of $A$ being multiplied by $\lambda$.
>>- Adding a non-zero multple of a row / column to another row / column has no effect.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Eigenvalues and Determinant
>
>Let $A \in F^{n \times n}$ be a [square matrix](./Square%20Matrices.md)
>
>If $A$ has $l$ distinct [eigenvalues](./Eigentheory.md) $\lambda_1, \dotsc, \lambda_l$ and the sum of their [algebraic multiplicities](./Eigentheory.md) is equal to $n$, then the [determinant](#Determinants) of $A$ is given as follows:
>
>$$\det A = \prod_{k=1}^l \lambda_k ^{\operatorname{alg} (\lambda_k)}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Determinant of a $2\times 2$-Matrix
>
>The [determinant](./Determinants.md) of every $2\times 2$-[matrix](./Square%20Matrices.md) $A = \begin{bmatrix}a & b \\ c & d\end{bmatrix}$ is given by
>
>$$\det A = ad - bc$$
>
>>[!PROOF]-
>>
>>We use the [determinant form](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Vector%20Space%20Endomorphisms.md#Determinants) $\delta: F^2 \times F^2 \to F$ defined on the [standard basis](../Row%20and%20Column%20Vectors.md) as $\delta (\mathbf{e}_1, \mathbf{e}_2) = 1$.
>>
>>By the definition of a [determinant](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Vector%20Space%20Endomorphisms.md), we have:
>>
>>$$\det A \cdot \delta (\mathbf{e}_1, \mathbf{e}_2) = \delta (f(\mathbf{e}_1), f(\mathbf{e}_2))$$
>>
>>Since $\delta (\mathbf{e}_1, \mathbf{e}_2) = 1$ by definition, we have:
>>
>>$$\begin{aligned}\det A & = \delta (f(\mathbf{e}_1), f(\mathbf{e}_2)) \\ & = \delta \left( A\begin{bmatrix}1 \\ 0\end{bmatrix}, A \begin{bmatrix}0 \\ 1\end{bmatrix} \right) \\ & = \delta \left(\begin{bmatrix}a \\ c\end{bmatrix}, \begin{bmatrix}b \\ d\end{bmatrix}\right)\end{aligned}$$
>>
>>We now use the fact that $\delta$ is [multilinear](../../../Analysis/Functional%20Analysis/Linearity/Multilinear%20Transformations.md):
>>
>>$$\begin{aligned} \delta \left(\begin{bmatrix}a \\ c\end{bmatrix}, \begin{bmatrix}b \\ d\end{bmatrix}\right) & = \delta(a \cdot \mathbf{e}_1 + c \cdot \mathbf{e}_2, b\cdot \mathbf{e}_1 + d \cdot \mathbf{e}_2) \\ & = a \cdot \delta (\mathbf{e}_1, b\cdot \mathbf{e}_1 + d \cdot \mathbf{e}_2) + c \cdot \delta (\mathbf{e}_2, b\cdot \mathbf{e}_1 + d \cdot \mathbf{e}_2) \\ & = a \cdot b \cdot \delta(\mathbf{e}_1, \mathbf{e}_1) + a \cdot d \cdot \delta(\mathbf{e}_1, \mathbf{e}_2) + c\cdot b \cdot \delta(\mathbf{e}_2, \mathbf{e}_1) + c \cdot d \cdot \delta (\mathbf{e}_2, \mathbf{e}_2) \end{aligned}$$
>>
>>Now we use the fact that $\delta$ is [alternating](../../../Analysis/Functional%20Analysis/Linearity/Alternating%20Multilinear%20Forms.md) (specifically that $\delta(\mathbf{e}_i, \mathbf{e}_i)=0$ and $\delta(\mathbf{e}_2, \mathbf{e}_1) = -\delta(\mathbf{e}_1, \mathbf{e}_2)$):
>>
>>$$\begin{aligned}a \cdot b \cdot \delta(\mathbf{e}_1, \mathbf{e}_1) + a \cdot d \cdot \delta(\mathbf{e}_1, \mathbf{e}_2) + c\cdot b \cdot \delta(\mathbf{e}_2, \mathbf{e}_1) + c \cdot d \cdot \delta (\mathbf{e}_2, \mathbf{e}_2) & = a \cdot b \cdot 0 + a \cdot d \cdot (1) + c\cdot b \cdot (-1) + c \cdot d \cdot 0 \\ & = 0 + ad - cb + 0 \\ & = ad - bc\end{aligned}$$
>>
>

>[!THEOREM] Theorem: Determinant of a $3\times 3$-Matrix
> 
>The [determinant](./Determinants.md) of every $3 \times 3$-[matrix](./Square%20Matrices.md) $A = \begin{bmatrix}a & b & c \\ d & e & f \\ g & h & i\end{bmatrix}$ is given by
>
>$$\left|\begin{matrix}a & b & c \\ d & e & f \\ g & h & i\end{matrix}\right| = a(ei - fh) - b(di - fg) + c(dh - ge)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Leibniz Formula for Determinants
>
>Let $A = (a_{i,j}) \in F^{n \times n}$ be a [square matrix](./Square%20Matrices.md) and let $S_n$ be the [symmetric group](../../../Combinatorics/Permutations.md) on $\{1, \dotsc, n\}$.
>
>The [determinant](./Determinants.md) of $A$ is given by
>
>$$\det A = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma)\prod_{i = 1}^n a_{\sigma(i), i} = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma)\prod_{i = 1}^n a_{i, \sigma(i)},$$
>
>where $\operatorname{sgn}(\sigma)$ is the [sign](../../../Combinatorics/Permutations.md#Parity) of $\sigma$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Laplace Expansion (Cofactor Expansion)
>
>Let $A = (a_{ij}) \in F^{n \times n}$ be a [square matrix](./Square%20Matrices.md).
>
>>[!NOTATION] Notation
>>
>>We use $A_{ij}$ to denote the [square matrix](./Square%20Matrices.md) $A_{ij} \in F^{(n-1)\times (n-1)}$ obtained by removing the $i$-th row and the $j$-th column of $A$ and then sticking the rest of $A$'s rows and columns together.
>>
>
>The [determinant](./Determinants.md) of $A$ is given by the following:
>
>$$\begin{aligned} \det A & = \sum_{i = 1}^n (-1)^{i+j} a_{i,j} \det A_{ij} \qquad \text{(expansion along the } j \text{-th column)} \\ \det A & = \sum_{i = 1}^n (-1)^{i+j} a_{j,i} \det A_{ji} \qquad \text{(expansion along the } j \text{-th row)}\end{aligned}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
