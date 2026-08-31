---
tags:
    - real-analysis
    - analysis
    - measure-theory
    - mathematics
---

# Peano-Jordan Measure

>[!DEFINITION] Definition: Peano-Jordan Measure
>
>The **Peano-Jordan measure** of a [closed cuboid](TODO) $R = [a_1, b_1] \times \cdots \times [a_n, b_n]$ inside the [Euclidean space](../Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md) $\mathbb{R}^n$ is the following product:
>
>$$\mu(R) \overset{\text{def}}{=} \prod_{k=1}^n (b_k - a_k)$$
>

TODO

>[!THEOREM] Theorem: Jordan-Measurability via Riemann Integrals
>
>A [subset](../Set%20Theory/Subsets.md) $S \subseteq \mathbb{R}^n$ is [Jordan-measurable](./Peano-Jordan%20Measure.md) if and only if there exists a [compact rectangular region](../Analysis/Real%20Analysis/Euclidean%20Space/Euclidean%20Space.md) $R \subset \mathbb{R}^n$ [containing](../Set%20Theory/Subsets.md) $S$ such that the [indicator function](../Analysis/Real%20Analysis/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $\mathbf{1}_S : \mathbb{R}^n \to \mathbb{R}$
>
>$$\mathbf{1}_S(\boldsymbol{x}) = \begin{cases}0 & \text{if} & \boldsymbol{x} \notin S \\ 1 & \text{if} & \boldsymbol{x} \in S\end{cases}$$
>
>is [Riemann-integrable](../Analysis/Real%20Analysis/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Integration/Riemann%20Integrals%20(Real%20Scalar%20Fields).md) on $R$. In this case, the value of this [integral](../Analysis/Real%20Analysis/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Integration/Riemann%20Integrals%20(Real%20Scalar%20Fields).md) is the [Peano-Jordan measure](./Peano-Jordan%20Measure.md) of $S$.
>
>>[!PROOF]-
>>
>>TODO
>>
>