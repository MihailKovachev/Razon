---
tags:
    - functional-mathematical-analysis
    - mathematical-analysis
    - linear-algebra
    - mathematics
---

# Matrix Exponential

>[!THEOREM] Theorem: Convergence of the Matrix Exponential
>
>Let $F$ be the [field](../../../Algebra/Fields/Fields.md) of the [real numbers](../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) or the [field](../../../Algebra/Fields/Fields.md) of the [complex numbers](../../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md).
>
>The [matrix power series](./Matrix%20Power%20Series.md)
>
>$$\sum_{k = 0}^{\infty} \frac{1}{k!}\boldsymbol{A}^k = I_n + \boldsymbol{A} + \frac{1}{2}\boldsymbol{A}^2 + \frac{1}{3!}\boldsymbol{A}^3 + \cdots$$
>
>is [convergent](./Matrix%20Power%20Series.md#Convergence) for all [square matrices](../../../Algebra/Matrices/Square%20Matrices/Square%20Matrices.md) $\boldsymbol{A} \in F^{n \times n}$.
>
>>[!DEFINITION] Definition: Matrix Exponential Function
>>
>>The **matrix exponential function** is the [matrix function](./Matrix%20Functions.md) defined by the aforementioned [power series](./Matrix%20Power%20Series.md):
>>
>>$$\exp: F^{n \times n} \to F^{n \times n} \qquad \exp(\boldsymbol{A}) = \sum_{k = 0}^{\infty} \frac{1}{k!}\boldsymbol{A}^k$$
>>
>>>[!NOTATION]
>>>
>>>$$\mathrm{e}^{\boldsymbol{A}} \qquad \exp (\boldsymbol{A})$$
>>>
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Matrix Exponential of Diagonal Matrices
>
>The [matrix exponential](./Matrix%20Exponential.md) of a [real](../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) [diagonal matrix](../../../Algebra/Matrices/Square%20Matrices/Diagonal%20Matrices.md) $\boldsymbol{A} = \operatorname{diag}(a_1, \dotsc, a_n) \in \mathbb{R}^{n \times n}$ is the [real](../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) [diagonal matrix](../../../Algebra/Matrices/Square%20Matrices/Diagonal%20Matrices.md) of the [real exponentials](../../Real%20Analysis/Real%20Functions/Real%20Exponentiation.md) of $\boldsymbol{A}$'s diagonal entries:
>
>$$\mathrm{e}^{\operatorname{diag}(a_1, \dotsc, a_n)} = \operatorname{diag}(\mathrm{e}^{a_1}, \dotsc, \mathrm{e}^{a_n})$$
>
>$$\boldsymbol{A} = \begin{bmatrix}a_1 & 0 & \cdots & 0 \\ 0 & a_2 & \ddots & \vdots \\ \vdots & \ddots & \ddots & 0 \\ 0 & \cdots & 0 & a_n\end{bmatrix} \implies \mathrm{e}^{\boldsymbol{A}} = \begin{bmatrix}\mathrm{e}^{a_1} & 0 & \cdots & 0 \\ 0 & \mathrm{e}^{a_2} & \ddots & \vdots \\ \vdots & \ddots & \ddots & 0 \\ 0 & \cdots & 0 & \mathrm{e}^{a_n}\end{bmatrix}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Matrix Exponential of Nilpotent Matrices
>
>If a [real](../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) [square matrix](../../../Algebra/Matrices/Square%20Matrices/Square%20Matrices.md) $\boldsymbol{A} \in \mathbb{R}^{n \times n}$ is [nilpotent](TODO) with $\boldsymbol{A}^r = \boldsymbol{0}$, then its [matrix exponential](./Matrix%20Exponential.md) is given by the following sum:
>
>$$\mathrm{e}^{\boldsymbol{A}} = \sum_{k = 0}^{r-1} \frac{1}{k!} \boldsymbol{A}^k$$
>
>>[!EXAMPLE]- Example
>>
>>Consider the following $\boldsymbol{A} \in \mathbb{R}^{n \times n}$:
>>
>>$$\boldsymbol{A} = \begin{bmatrix} 0 & 1 \\ 0 & 0\end{bmatrix}$$
>>
>>It is [nilpotent](TODO), since $\boldsymbol{A}^k = \boldsymbol{0}$ for all $k \ge 2$. Its [matrix exponential](./Matrix%20Exponential.md) is thus the following:
>>
>>$$\begin{aligned}\mathrm{e}^{\boldsymbol{A}} & = \sum_{k = 0}^1 \frac{1}{k!}\boldsymbol{A}^k \\ & = \frac{1}{0!}\boldsymbol{A}^0 + \frac{1}{1!} \boldsymbol{A}^1 \\ & = \boldsymbol{I}_n + \boldsymbol{A} \\ & = \begin{bmatrix} 1 & 0 \\ 0 & 1\end{bmatrix} + \begin{bmatrix}0 & 1 \\ 0 & 0\end{bmatrix} \\ & = \begin{bmatrix}1 & 1 \\ 0 & 1 \end{bmatrix}\end{aligned}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Matrix Exponential of Diagonalizable Matrices
>
>If a [square matrix](../../../Algebra/Matrices/Square%20Matrices/Square%20Matrices.md) $\boldsymbol{A} \in F^{n \times n}$ is [diagonalizable](../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) with $\boldsymbol{A} = \boldsymbol{P} \boldsymbol{D} \boldsymbol{P}^{-1}$, where $\boldsymbol{D} = \operatorname{diag}(\lambda_1, \dotsc, \lambda_n)$, then its [matrix exponential](./Matrix%20Exponential.md) is the following:
>
>$$\mathrm{e}^{\boldsymbol{A}} = \boldsymbol{P} \mathrm{e}^{\boldsymbol{D}}\boldsymbol{P}^{-1}$$
>
>>[!EXAMPLE]-
>>
>>Consider the following [real](../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) [square matrix](../../../Algebra/Matrices/Square%20Matrices/Square%20Matrices.md):
>>
>>$$\boldsymbol{A} = \begin{bmatrix} 1 & 2 \\ 2 & 1\end{bmatrix}$$
>>
>>It has the [eigenvalues](../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) $\lambda_1 = 3$ and $\lambda_2 = -1$ with the following corresponding [eigenvectors](../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md):
>>
>>$$\boldsymbol{v}_1 = \begin{bmatrix}1 \\ 1\end{bmatrix} \qquad \boldsymbol{v}_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$$
>>
>>It is thus [diagonalizable](../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md):
>>
>>$$\boldsymbol{P} = \begin{bmatrix} 1 & 1 \\ 1 & -1\end{bmatrix} \qquad \boldsymbol{D} = \begin{bmatrix}3 & 0 \\ 0 & -1\end{bmatrix} \qquad \boldsymbol{P}^{-1} = \begin{bmatrix}\frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & -\frac{1}{2}\end{bmatrix}$$
>>
>>Its [matrix exponential](./Matrix%20Exponential.md) is thus the following:
>>
>>$$\begin{aligned}\mathrm{e}^{\boldsymbol{A}} & = \boldsymbol{P} \mathrm{e}^{\boldsymbol{D}}\boldsymbol{P}^{-1} \\ & = \begin{bmatrix} 1 & 1 \\ 1 & -1\end{bmatrix} \begin{bmatrix}\mathrm{e}^3 & 0 \\ 0 & \mathrm{e}^{-1}\end{bmatrix} \begin{bmatrix}\frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & -\frac{1}{2} \end{bmatrix} \\ & = \frac{1}{2}\begin{bmatrix} \mathrm{e}^3 + \mathrm{e}^{-1} & \mathrm{e}^3 - \mathrm{e}^{-1} \\ \mathrm{e}^3 - \mathrm{e}^{-1} & \mathrm{e}^3 + \mathrm{e}^{-1}\end{bmatrix}\end{aligned}$$
>>
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Exponential of Sum
>
>Let $\boldsymbol{A}, \boldsymbol{B} \in \mathbb{R}^{n \times n}$ be [real](../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) [square matrix](../../../Algebra/Matrices/Square%20Matrices/Square%20Matrices.md).
>
>If the [matrix product](../../../Algebra/Matrices/Matrix%20Product.md) of $\boldsymbol{A}$ and $\boldsymbol{B}$ is [commutative](TODO), i.e. $\boldsymbol{A}\boldsymbol{B} = \boldsymbol{B} \boldsymbol{A}$, then the [exponential](./Matrix%20Exponential.md) of their sum is the [product](../../../Algebra/Matrices/Matrix%20Product.md) of their [exponentials](./Matrix%20Exponential.md):
>
>$$\mathrm{e}^{\boldsymbol{A} + \boldsymbol{B}} = \mathrm{e}^{\boldsymbol{A}}\mathrm{e}^{\boldsymbol{B}}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Invertibility of the Matrix Exponential
>
>The [matrix exponential](./Matrix%20Exponential.md) is [invertible](../../../Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md):
>
>$$(\mathrm{e}^{\boldsymbol{A}})^{-1} = \mathrm{e}^{-\boldsymbol{A}}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>