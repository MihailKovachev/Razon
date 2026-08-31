---
tags:
    - functional-mathematical-analysis
    - mathematical-analysis
    - linear-algebra
    - mathematics
---

# Matrix Series

>[!DEFINITION] Definition: Partial Sum
>
>Let $(\boldsymbol{A}_k)_{k \in \mathcal{D}}$ be a [sequence](./Matrix%20Sequences.md) of $m \times n$-[matrices](../../../Algebra/Matrices/Matrices.md) over the same [topological field](TODO) $F$.
>
>The $p$-th **partial sum** of $(\boldsymbol{A}_k)_{k \in \mathcal{D}}$ is the sum of the first $p$ [matrices](../../../Algebra/Matrices/Matrices.md) in the [sequence](./Matrix%20Sequences.md):
>
>$$\sum_{\substack{j \in \mathcal{D} \\ j \le p}} \boldsymbol{A}_j$$
>

>[!DEFINITION] Definition: Matrix Series
>
>A **matrix series** is the [sequence](./Matrix%20Sequences.md) of the [partial sums](./Matrix%20Series.md) of some [matrix sequence](./Matrix%20Sequences.md).
>
>>[!EXAMPLE]-
>>
>>Consider the following [matrix sequence](./Matrix%20Sequences.md) $(\boldsymbol{A}_k)_{k \in \mathbb{N}_0}$:
>>
>>$$\boldsymbol{A}_k = \begin{bmatrix}\frac{1}{k!} & 0 \\ \frac{1}{2^k} & \frac{1}{5^k}\end{bmatrix}$$
>>
>>The corresponding [matrix series](./Matrix%20Series.md) is the following:
>>
>>$$\begin{aligned}\sum_{k = 0}^{\infty} \boldsymbol{A}_k & = \sum_{k = 0}^{\infty}\begin{bmatrix}\frac{1}{k!} & 0 \\ \frac{1}{2^k} & \frac{1}{5^k}\end{bmatrix} \\ & = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} + \begin{bmatrix} 1 & 0 \\ \frac{1}{2} & \frac{1}{5} \end{bmatrix} + \begin{bmatrix} \frac{1}{2} & 0 \\ \frac{1}{4} & \frac{1}{25} \end{bmatrix} + \begin{bmatrix} \frac{1}{6} & 0 \\ \frac{1}{8} & \frac{1}{125} \end{bmatrix} + \cdots\end{aligned}$$
>>
>
>>[!EXAMPLE]-
>>
>>Consider the following [matrix sequence](./Matrix%20Sequences.md) $(\boldsymbol{A}_k)_{k \in \mathbb{N}}$:
>>
>>$$\boldsymbol{A}_k = \begin{bmatrix}\frac{2^k}{k!} & \frac{1}{k} \\ \frac{1}{2^k} & \frac{1}{5^k}\end{bmatrix}$$
>>
>>The corresponding [matrix series](./Matrix%20Series.md) is the following:
>>
>>$$\begin{aligned}\sum_{k = 1}^{\infty} \boldsymbol{A}_k & = \sum_{k = 1}^{\infty}\begin{bmatrix}\frac{2^k}{k!} & \frac{1}{k} \\ \frac{1}{2^k} & \frac{1}{5^k}\end{bmatrix} \\ & = \begin{bmatrix} 2 & 1 \\ \frac{1}{2} & \frac{1}{5} \end{bmatrix} + \begin{bmatrix} 2 & \frac{1}{2} \\ \frac{1}{4} & \frac{1}{25} \end{bmatrix} + \begin{bmatrix} \frac{4}{3} & \frac{1}{3} \\ \frac{1}{8} & \frac{1}{125} \end{bmatrix} + \cdots\end{aligned}$$
>>
>

## Convergence

Since a [matrix series](./Matrix%20Series.md) is just a [matrix sequence](./Matrix%20Sequences.md), the notion of [convergence](./Matrix%20Sequences.md#Convergence) carries over directly.

>[!EXAMPLE]-
>
>Consider the following [matrix series](./Matrix%20Series.md) of [real matrices](../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md):
>
>$$\begin{aligned}\sum_{k = 0}^{\infty}\begin{bmatrix}\frac{1}{k!} & 0 \\ \frac{1}{2^k} & \frac{1}{5^k}\end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} + \begin{bmatrix} 1 & 0 \\ \frac{1}{2} & \frac{1}{5} \end{bmatrix} + \begin{bmatrix} \frac{1}{2} & 0 \\ \frac{1}{4} & \frac{1}{25} \end{bmatrix} + \begin{bmatrix} \frac{1}{6} & 0 \\ \frac{1}{8} & \frac{1}{125} \end{bmatrix} + \cdots\end{aligned}$$
>
>It is [convergent](#Convergence):
>
>$$\sum_{k = 0}^{\infty}\begin{bmatrix}\frac{1}{k!} & 0 \\ \frac{1}{2^k} & \frac{1}{5^k}\end{bmatrix} = \begin{bmatrix} \sum_{k = 0}^{\infty} \frac{1}{k!} & \sum_{k = 0}^{\infty} 0 \\ \sum_{k = 0}^{\infty} \frac{1}{2^k} & \sum_{k = 0}^{\infty} \frac{1}{5^k}\end{bmatrix} = \begin{bmatrix}\mathrm{e} & 0 \\ 2 & \frac{5}{4}\end{bmatrix}$$
>

>[!EXAMPLE]-
>
>Consider the following [matrix series](./Matrix%20Series.md) of [real matrices](../../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md):
>
>$$\sum_{k = 1}^{\infty}\begin{bmatrix}\frac{2^k}{k!} & \frac{1}{k} \\ \frac{1}{2^k} & \frac{1}{5^k}\end{bmatrix} = \begin{bmatrix} 2 & 1 \\ \frac{1}{2} & \frac{1}{5} \end{bmatrix} + \begin{bmatrix} 2 & \frac{1}{2} \\ \frac{1}{4} & \frac{1}{25} \end{bmatrix} + \begin{bmatrix} \frac{4}{3} & \frac{1}{3} \\ \frac{1}{8} & \frac{1}{125} \end{bmatrix} + \cdots$$
>
>It is [divergent](#Convergence) because $\sum_{k = 1}^{\infty} \frac{1}{k}$ is [divergent](../../Real%20Analysis/Real%20Series.md#Convergence).
>

>[!DEFINITION] Definition: Absolute Convergence
>
>A [matrix series](./Matrix%20Series.md) $\sum_{k \in \mathcal{D}} \boldsymbol{A}_k$ is **absolutely convergent** if the [real series](../../Real%20Analysis/Real%20Series.md) $\sum_{k \in \mathcal{D}} ||\boldsymbol{A}_k||$ of any of its [norms](../../../Algebra/Matrices/Matrix%20Norms.md) is [convergent](../../Real%20Analysis/Real%20Series.md#Convergence).
>

>[!THEOREM] Theorem: Absolute Convergence $\implies$ Convergence
>
>If a [matrix series](./Matrix%20Series.md) is [absolutely convergent](#Convergence), then it is also [convergent](#Convergence).
>
>>[!PROOF]-
>>
>>TODO
>>
>