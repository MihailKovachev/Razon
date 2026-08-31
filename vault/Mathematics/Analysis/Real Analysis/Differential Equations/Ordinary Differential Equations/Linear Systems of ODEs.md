---
tags:
    - algebra
    - real-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Linear Systems of ODEs

>[!THEOREM] Theorem: Basis for Solutions with
>
>Consider the following [linear system of ODEs](./Linear%20Systems%20of%20ODEs.md)
>
>$$\boldsymbol{y}'(t) = \boldsymbol{A} \boldsymbol{y}(t)$$
>
>with the [real](../../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) [matrix](../../../../Algebra/Matrices/Square%20Matrices/Square%20Matrices.md) $\boldsymbol{A} \in \mathbb{R}^{n \times n}$.
>
>If $\boldsymbol{A}$ is [diagonalizable](../../../../Algebra/Matrices/Square%20Matrices/Eigendecomposition.md) as a [complex matrix](../../../../Algebra/Matrices/Complex%20Matrices/Complex%20Matrices.md), then a [basis](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) for its [solution space](./Linear%20Systems%20of%20ODEs.md) can be generated as follows:
>
>- Each [real](../../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) [eigenvalue](../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) $\lambda$ with a corresponding [eigenvector](../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) $\boldsymbol{v}$ yields the [basis element](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) $\mathrm{e}^{\lambda t}\boldsymbol{v}$.
>- Each pair of [complex conjugate](../../../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md) [eigenvalues](../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) $\lambda = \alpha \pm \beta \mathrm{i}$ with corresponding [eigenvectors](../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md) $\boldsymbol{v} = \boldsymbol{a} \pm \boldsymbol{b}\mathrm{i}$ yields the [basis elements](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) $\mathrm{e}^{\alpha t} (\cos(\beta t) \boldsymbol{a} - \sin (\beta t) \boldsymbol{b})$ and $\mathrm{e}^{\alpha t} (\sin(\beta t) \boldsymbol{a} + \cos (\beta t) \boldsymbol{b})$.
>
>>[!EXAMPLE]-
>>
>>Consider the following [linear system of ODEs](./Linear%20Systems%20of%20ODEs.md):
>>
>>$$\boldsymbol{y}'(t) = \begin{bmatrix}1 & -2 \\ 2 & 1\end{bmatrix} \boldsymbol{y}$$
>>
>>We have:
>>
>>$$\boldsymbol{A} = \begin{bmatrix}1 & -2 \\ 2 & 1\end{bmatrix}$$
>>
>>This is [diagonalizable](../../../../Algebra/Matrices/Square%20Matrices/Eigendecomposition.md) as a [complex matrix](../../../../Algebra/Matrices/Complex%20Matrices/Complex%20Matrices.md) with the following [eigenvalues](../../../../Algebra/Matrices/Square%20Matrices/Eigentheory.md):
>>
>>$$\lambda = 1 + 2\mathrm{i} \qquad \overline{\lambda} = 1 - 2\mathrm{i}$$
>>
>>We thus get $\alpha = 1$ and $\beta = 2$. One [eigenvector](../../../Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Eigentheory.md) of $\lambda$ is the following:
>>
>>$$\boldsymbol{v} = \begin{bmatrix} \mathrm{i} \\ 1 \end{bmatrix} = \begin{bmatrix}0 \\ 1\end{bmatrix} + \mathrm{i} \cdot \begin{bmatrix}1 \\ 0\end{bmatrix}$$
>>
>>We thus get:
>>
>>$$\boldsymbol{a} = \begin{bmatrix}0 \\ 1\end{bmatrix} \qquad \boldsymbol{b} = \begin{bmatrix}1 \\ 0\end{bmatrix}$$
>>
>>Therefore, we obtain the following [basis](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md):
>>
>>$$\left\{ \mathrm{e}^{\alpha t} (\cos(\beta t) \boldsymbol{a} - \sin (\beta t) \boldsymbol{b}), \mathrm{e}^{\alpha t} (\sin(\beta t) \boldsymbol{a} + \cos (\beta t) \boldsymbol{b}) \right\}$$
>>
>>$$\left\{ \mathrm{e}^{t} \left(\cos (2t) \begin{bmatrix}0 \\ 1\end{bmatrix} - \sin(2t) \begin{bmatrix}1 \\ 0\end{bmatrix}\right), \mathrm{e}^{t} \left(\sin (2t) \begin{bmatrix}0 \\ 1\end{bmatrix} + \cos(2t) \begin{bmatrix}1 \\ 0\end{bmatrix}\right) \right\}$$
>>
>>$$\left\{ \mathrm{e}^t \begin{bmatrix}-\sin(2t) \\ \cos (2t)\end{bmatrix}, \mathrm{e}^t \begin{bmatrix}\cos (2t) \\ \sin(2t)\end{bmatrix}\right\}$$
>>
>>The general [solution](./Linear%20Systems%20of%20ODEs.md) is thus the following:
>>
>>$$\boldsymbol{y}(t) = c_1 \mathrm{e}^t \begin{bmatrix}-\sin(2t) \\ \cos (2t)\end{bmatrix} + c_2 \mathrm{e}^t \begin{bmatrix}\cos (2t) \\ \sin(2t)\end{bmatrix} \qquad c_1, c_2 \in \mathbb{R}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>