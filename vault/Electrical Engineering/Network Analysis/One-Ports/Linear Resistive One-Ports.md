---
tags:
    - network-analysis
    - electrical-engineering
---

# Linear One-Ports

>[!DEFINITION] Definition: Strictly Linear One-Port
>
>A [linear one-port](#Linear%20One-Ports) is **strictly linear** if its [V-I characteristic](./One-Ports.md#V-I%20Characteristic) can be written as
>
>$$
>aU + bI = 0
>$$
>
>>[!THEOREM] Theorem: Equivalent Definition
>>
>>A [one-port](./One-Ports.md) is [strictly linear](#Strictly%20Linear%20One-Ports) if and only if its [V-I characteristic](./One-Ports.md#V-I%20Characteristic) $\mathcal{F}$ simultaneously has the following properties:
>>- If $(U, I)$ is in $\mathcal{F}$, then so is $(\lambda U, \lambda I)$ for all $\lambda \in \mathbb{R}$.
>>- If $(U_1, I_1)$ and $(U_2, I_2)$ are in $\mathcal{F}$, then so is $(U_1 + U_2, I_1 + I_2)$.
>>
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

Graphically, the [V-I characteristic](./One-Ports.md#V-I%20Characteristic) of a [strictly linear one-port](#Strictly%20Linear%20One-Ports) is a straight line passing through the origin $(0, 0)$:

![V-I of Strictly Linear One-Ports](./res/V-I%20of%20Strictly%20Linear%20One-Ports.svg)

>[!THEOREM] Theorem: Polarity of Strictly Linear One-Ports
>
>All [strictly linear one-ports](./Linear%20Resistive%20One-Ports.md) are [unpolarized](./One-Ports.md#Polarity).
>
>>[!PROOF]-
>>
>>TODO
>>
>

