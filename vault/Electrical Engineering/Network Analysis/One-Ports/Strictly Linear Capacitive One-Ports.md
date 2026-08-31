---
tags:
    - network-analysis
    - electrical-engineering
---

# Strictly Linear Capacitive One-Ports

## Time Invariance

>[!TIP] Tip: Time Invariance
>
>A [time-invariant](./Capacitive%20One-Ports.md) [capacitive](./Capacitive%20One-Ports.md) [one-port](./One-Ports.md) is [strictly linear](./Strictly%20Linear%20Capacitive%20One-Ports.md) if and only if its [capacitive characteristic](./Capacitive%20One-Ports.md) is a [linear subspace](../../../Mathematics/Algebra/Vector%20Spaces/Linear%20Subspaces.md) of $\mathbb{R}^2$.
>

>[!THEOREM] Theorem: Work with Time-Invariant Strictly Linear Capacitive One-Ports
>
>Let $\mathcal{C}$ be a [time-invariant](./Capacitive%20One-Ports.md) [strictly linear](./Strictly%20Linear%20Capacitive%20One-Ports.md) [capacitive](./Capacitive%20One-Ports.md) [one-port](./One-Ports.md)  with [capacitance](./Strictly%20Linear%20Capacitive%20One-Ports.md) $C \ne 0$.
>
>The [work](TODO) needed to change the [charge](./One-Ports.md) of $\mathcal{C}$ from $Q_{\text{initial}}$ to $Q_{\text{final}}$ is the following:
>
>$$\frac{1}{2C}(Q_{\text{final}}^2 - Q_{\text{initial}}^2)$$
>
>The [work](TODO) needed to change the [voltage](./One-Ports.md) across $\mathcal{C}$ from $V_{\text{initial}}$ to $V_{\text{final}}$ is the following:
>
>$$\frac{1}{2}C(V_{\text{final}}^2 - V_{\text{initial}}^2)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Strictly Linear Capacitive One-Ports in Series
>
>If $n$ [strictly linear capacitive one-ports](./Strictly%20Linear%20Capacitive%20One-Ports.md) with [elastances](./Strictly%20Linear%20Capacitive%20One-Ports.md) $S_1, \dotsc, S_n$ and [capacitances](./Strictly%20Linear%20Capacitive%20One-Ports.md) $C_1, \dotsc, C_n$, respectively, are connected in [series](./One-Port%20Series%20Circuits.md), then they are equivalent to a single [strictly linear capacitive one-port](./Strictly%20Linear%20Capacitive%20One-Ports.md) whose [elastance](./Strictly%20Linear%20Capacitive%20One-Ports.md) $S$ and [capacitance](./Strictly%20Linear%20Capacitive%20One-Ports.md) $C$ are given as follows:
>
>$$S = \sum_{i=1}^n S_i = S_1 + S_2 + \cdots + S_n$$
>
>$$\frac{1}{C} = \sum_{i=1}^n \frac{1}{C_i} = \frac{1}{C_1} + \frac{1}{C_2} + \cdots + \frac{1}{C_n}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Strictly Linear Capacitive One-Ports in Parallel
>
>If $n$ [strictly linear capacitive one-ports](./Strictly%20Linear%20Capacitive%20One-Ports.md) with [capacitances](./Strictly%20Linear%20Capacitive%20One-Ports.md) $C_1, \dotsc, C_n$ and [elastances](./Strictly%20Linear%20Capacitive%20One-Ports.md) $S_1, \dotsc, S_n$, respectively, are connected in [parallel](./One-Port%20Parallel%20Circuits.md), then they are equivalent to a single [strictly linear capacitive one-port](./Strictly%20Linear%20Capacitive%20One-Ports.md) whose [capacitance](./Strictly%20Linear%20Capacitive%20One-Ports.md) $C$ and [elastance](./Strictly%20Linear%20Capacitive%20One-Ports.md) $S$ are given as follows:
>
>$$C = \sum_{i=1}^n C_i = C_1 + C_2 + \cdots + C_n$$
>
>$$\frac{1}{S} = \sum_{i=1}^n \frac{1}{S_i} = \frac{1}{S_1} + \frac{1}{S_2} + \cdots + \frac{1}{S_n}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>