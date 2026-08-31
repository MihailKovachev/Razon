---
tags:
    - functional-mathematical-analysis
    - mathematical-analysis
    - linear-algebra
    - mathematics
---

# Matrix Sequences

>[!DEFINITION] Definition: Matrix Sequence
>
>A **matrix sequence** is a [sequence](../Sequences/Sequences.md) of [matrices](../../../Algebra/Matrices/Matrices.md).
>

## Convergence

To get a sense of what it means for a [matrix sequence](./Matrix%20Sequences.md) $(\boldsymbol{A}_k)_{k \in \mathcal{D}} \subseteq F^{m \times n}$ of $m\times n$-[matrices](../../../Algebra/Matrices/Matrices.md) to approach a specific [matrix](../../../Algebra/Matrices/Matrices.md) $\boldsymbol{L} \in F^{m \times n}$, we need a way to quantify how different two [matrices](../../../Algebra/Matrices/Matrices.md), i.e. we need to measure the "distance" between them. If the distance between $\boldsymbol{A}_k$ and $\boldsymbol{L}$ approaches $0$, for $k \to \infty$, then we can say that $A_k$ approaches $\boldsymbol{L}$. To quantify this distance we can use a [matrix norms](../../../Algebra/Matrices/Matrix%20Norms.md). Luckily, the specific choice for a [matrix norms](../../../Algebra/Matrices/Matrix%20Norms.md) is irrelevant because if the distance approaches $0$ with respect to one [matrix norm](../../../Algebra/Matrices/Matrix%20Norms.md), then it does so for all [matrix norms](../../../Algebra/Matrices/Matrix%20Norms.md).

>[!THEOREM] Theorem: Matrix Convergence via Component Conversion
>
>Let $(\boldsymbol{A}_k)_{k \in \mathcal{D}} \subseteq F^{m \times n}$ be a [sequence](./Matrix%20Sequences.md) of $m\times n$-[matrices](../../../Algebra/Matrices/Matrices.md) over the same [topological field](TODO) $F$.
>
>The [limit](../Sequences/Convergence%20(Sequences.md) of $(\boldsymbol{A}_k)_{k \in \mathcal{D}}$ is $\boldsymbol{L} \in F^{m \times n}$ if and only if the [limits](TODO) of $\boldsymbol{A}_k$'s entries are the entries of $\boldsymbol{L}$:
>
>$$\lim_{k \to \infty} \boldsymbol{A}_k = \boldsymbol{L} \iff \lim_{k \to \infty} (\boldsymbol{A}_k)_{ij} = \boldsymbol{L}_{ij} \text{ for all } 1 \le i \le m \text{ and all } 1 \le j \le n$$
>
>>[!EXAMPLE]-
>>
>>Consider the [matrix sequence](./Matrix%20Sequences.md) defined as follows:
>>
>>$$\boldsymbol{A}_k = \begin{bmatrix} \frac{4k + 1}{2k} & 1 + \frac{(-1)^k}{k} \\ \mathrm{e}^{-3k} & 5\end{bmatrix}$$
>>
>>It has the following [limit](#Convergence):
>>
>>$$\boldsymbol{L} = \begin{bmatrix}2 & 1 \\ 0 & 5\end{bmatrix}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Matrix Norm Equivalence
>
>Let $(\boldsymbol{A}_k)_{k \in \mathcal{D}} \subseteq F^{m \times n}$ be a [sequence](./Matrix%20Sequences.md) of $m\times n$-[matrices](../../../Algebra/Matrices/Matrices.md) over the same [field](../../../Algebra/Fields/Fields.md) $F$, let $\boldsymbol{L} \in F^{m \times n}$ and let $N_1$ and $N_2$ be [norms](../../../Algebra/Vector%20Spaces/Norms.md) on $F^{m \times n}$.
>
>The [limit](../../Real%20Analysis/Real%20Sequences.md#Convergence) of $N_1(\boldsymbol{A}_k - \boldsymbol{L})$ for $k \to \infty$ is zero if and only if the [limit](../../Real%20Analysis/Real%20Sequences.md#Convergence) of $N_2(\boldsymbol{A}_k - \boldsymbol{L})$ for $k \to \infty$ is also zero:
>
>$$\lim_{k \to \infty} N_1(\boldsymbol{A}_k - \boldsymbol{L}) = 0 \iff \lim_{k \to \infty} N_2(\boldsymbol{A}_k - \boldsymbol{L}) = 0$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Limits via Norms
>
>Let $(\boldsymbol{A}_k)_{k \in \mathcal{D}} \subseteq F^{m \times n}$ be a [sequence](./Matrix%20Sequences.md) of $m\times n$-[matrices](../../../Algebra/Matrices/Matrices.md) over the same [topological field](TODO) $F$.
>
>The [limit](../Sequences/Convergence%20(Sequences.md) of $(\boldsymbol{A}_k)_{k \in \mathcal{D}}$ is $\boldsymbol{L} \in F^{m \times n}$ if and only if the [limit](../../Real%20Analysis/Real%20Sequences.md#Convergence) of any [norm](../../../Algebra/Vector%20Spaces/Norms.md) of the difference between $\boldsymbol{A}_k$ and $\boldsymbol{L}$ is zero:
>
>$$\lim_{k \to \infty} ||\boldsymbol{A}_k - \boldsymbol{L}|| = 0$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

