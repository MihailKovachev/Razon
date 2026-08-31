---
tags:
    - network-analysis
    - electrical-engineering
---

# Affine Two-Ports

>[!THEOREM] Theorem: Strictly Linear Decomposition
>
>Let $\mathcal{F}$ be an [affine](./Affine%20Two-Ports.md) [two-port](./Two-Ports.md).
>
>If $\mathcal{F}$ has an [explicit representation](./Two-Ports.md)
>
>$$
>\begin{bmatrix}p_1 \\ p_2\end{bmatrix} = \boldsymbol{M}\begin{bmatrix}q_1 \\ q_2\end{bmatrix} + \begin{bmatrix}P_1 \\ P_2\end{bmatrix},
>$$
>
>then it is equivalent to a [strictly linear](./Linear%20Two-Ports.md) [two-port](./Two-Ports.md) $\mathcal{F}'$ whose corresponding [representation matrix](./Linear%20Two-Ports.md) is $\boldsymbol{M}$ and which has [independent time-invariant ideal sources](../../Analog%20Circuits/Sources.md) attached to it in the following configuration:
>- If $p_k$ is the [current](../../Current.md) flowing *into* the $j$-th [port](../Ports.md) of $\mathcal{F}$, then a [DC source](../../Analog%20Circuits/Sources.md) is attached at the $j$-th [port](../Ports.md) so that the [current](../../Current.md) flowing *into* the $j$-th [port](../Ports.md) of $\mathcal{F}'$ is $i_j - P_k$.
>- If $p_k$ is the [voltage](TODO) across the $j$-th [port](../Ports.md) of $\mathcal{F}$, then a [voltage source](../../Analog%20Circuits/Sources.md) is attached at the $j$-th [port](../Ports.md) so that the [voltage](TODO) across the $j$-th [port](../Ports.md) of $\mathcal{F}'$ is $v_j - P_k$.
>
>![Linear Two-Port Decomposition](./res/Linear%20Two-Port%20Decomposition.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>