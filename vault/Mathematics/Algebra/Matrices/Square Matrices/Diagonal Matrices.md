---
tags:
  - linear-algebra
  - algebra
  - mathematics
---

# Diagonal Matrices

>[!DEFINITION] Definition: Diagonal Matrix
>
>A **diagonal matrix** is a [square matrix](./Square%20Matrices.md) $M \in F^{n \times n}$ which has non-zero entries only on its diagonal.
>
>$$
>\begin{bmatrix}\mu_1 & \cdots & 0_F \\ \vdots & \ddots & \vdots \\ 0_F & \cdots & \mu_n\end{bmatrix}
>$$
>
>>[!NOTATION] Notation
>>
>>$$
>>\operatorname{diag}(\mu_1, \cdots, \mu_n)
>>$$
>>
>

>[!THEOREM] Theorem: Inverting a Diagonal Matrix
>
>A [diagonal matrix](./Diagonal%20Matrices.md) $\operatorname{diag}(\mu_1, \cdots, \mu_n)$ is [invertible](./Matrix%20Invertibility.md#Matrix%20Invertibility) if and only if none of its diagonal entries are zeroes.
>
>If $\operatorname{diag}(\mu_1, \cdots, \mu_n)$ is [invertible](./Matrix%20Invertibility.md#Matrix%20Invertibility), then its [inverse](./Matrix%20Invertibility.md#Matrix%20Invertibility) is $\operatorname{diag}(\mu_1^{-1}, \cdots, \mu_n^{-1})$.
>
>>[!PROOF]-
>>
>>TODO
>>
>