---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Real Vector Sequences

>[!DEFINITION] Definition: Real Vector Sequence
>
>A **real vector sequence** in the [Euclidean space](./Euclidean%20Space/Euclidean%20Space.md) $\mathbb{R}^n$ is a [sequence](../Functional%20Analysis/Sequences/Sequences.md) of [real vectors](../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) in $\mathbb{R}^n$.
>

## Convergence

>[!THEOREM] Theorem: Convergence via Metric
>
>A [real vector sequence](../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $(\mathbf{x})_{k \in \mathcal{D}}$ in $\mathbb{R}^n$ [converges](../Functional%20Analysis/Sequences/Convergence%20(Sequences.md) to the [limit](../Functional%20Analysis/Sequences/Convergence%20(Sequences.md) $\mathbf{L} \in \mathbb{R}^n$ if and only the [real sequence](./Real%20Sequences.md) of the [Euclidean distance](./Euclidean%20Space/Euclidean%20Space.md) between $\mathbf{x}_k$ and $\mathbf{L}$ [converges](./Real%20Sequences.md#Convergence) to zero:
>
>$$\lim_{k \to \infty} \mathbf{x}_k = \mathbf{L} \qquad \iff \qquad \lim_{k \to \infty} ||\mathbf{x}_k - \mathbf{L}|| = 0$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Convergence via Component Convergence
>
>A [real vector sequence](../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $(\mathbf{x})_{k \in \mathcal{D}}$ in $\mathbb{R}^n$ [converges](../Functional%20Analysis/Sequences/Convergence%20(Sequences.md) to the [limit](../Functional%20Analysis/Sequences/Convergence%20(Sequences.md) $\mathbf{L} = \begin{bmatrix}L^1, \dotsc, L^n\end{bmatrix}^{\mathsf{T}} \in \mathbb{R}^n$ if and only if the [real sequences](./Real%20Sequences.md) $(x^1)_{k \in \mathcal{D}}, \dotsc, (x^n)_{k \in \mathcal{D}}$ of its components [converge](./Real%20Sequences.md#Convergence) to $L^1, \dotsc, L^n$, respectively:
>
>$$\lim_{k \to \infty} \mathbf{x}_k = \mathbf{L} \qquad \iff \qquad  \lim_{k \to \infty} {x^i}_k = L_i \text{ for all } i \in \{1, \dotsc, n\}$$
>
>>[!EXAMPLE]-
>>
>>Consider the [real vector sequence](./Real%20Vector%20Sequences.md) $(\mathbf{x}_k)_{k \in \mathbb{N}}$ in $\mathbb{R}^2$ defined as follows:
>>
>>$$\mathbf{x}_k = \begin{bmatrix}1 + \frac{(-1)^k}{k} \\ \frac{3}{k^2}\end{bmatrix}$$
>>
>>The [real sequences](./Real%20Sequences.md) $(x^1)_{k \in \mathbb{N}}$ and $(x^2)_{k \in \mathbb{N}}$ of its components are given as follows:
>>
>>$${x^1}_k = 1 + \frac{(-1)^k}{k}$$
>>
>>$${x^2}_k = \frac{3}{k^2}$$
>>
>>They [converge](./Real%20Sequences.md#Convergence) to the following [limits](./Real%20Sequences.md#Convergence), respectively:
>>
>>$$\lim_{k \to \infty} {x^1}_k = \lim_{k \to \infty} 1 + \frac{(-1)^k}{k} = 1$$
>>
>>$$\lim_{k \to \infty} {x^2}_k = \lim_{k \to \infty} \frac{3}{k^2} = 0$$
>>
>>Therefore, the [real vector sequence](./Real%20Vector%20Sequences.md) $(\mathbf{x}_k)_{k \in \mathbb{N}}$ [converges](#Convergence) to $\begin{bmatrix}1 & 0\end{bmatrix}^{\mathsf{T}}$:
>>
>>$$\lim_{k \to \infty} \mathbf{x}_k = \lim_{k \to \infty} \begin{bmatrix}1 + \frac{(-1)^k}{k} \\ \frac{3}{k^2}\end{bmatrix} = \begin{bmatrix}1 \\ 0\end{bmatrix}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>