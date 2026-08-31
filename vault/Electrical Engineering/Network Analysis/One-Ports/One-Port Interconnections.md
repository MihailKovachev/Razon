---
tags:
    - network-analysis
    - electrical-engineering
---

# One-Port Interconnections

## One-Ports in Parallel

>[!DEFINITION] Definition: One-Ports in Parallel
>
>A **parallel circuit** is an [electrical element](../Network%20Analysis.md) which consists of [one-ports](./One-Ports.md) whose [terminals](../Network%20Analysis.md) are connected at the same [nodes](../Network%20Analysis.md).
>
>![Parallel Circuit](./res/Parallel%20Circuit.svg)
>
>We also say that the [one-ports](./One-Ports.md) are **connected in parallel**.
>

>[!THEOREM] Theorem: Voltage across Parallel Circuits
>
>The [voltage](TODO) across all [one-ports](./One-Ports.md) in a [parallel circuit](./One-Port%20Interconnections.md) is the same.
>
>![Voltage across Parallel Circuit](./res/Voltage%20across%20Parallel%20Circuit.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Equivalence of Parallel Circuits
>
>Every [parallel circuit](./One-Port%20Interconnections.md) of [one-ports](../../../index.md) $\mathcal{F}_1, \dotsc, \mathcal{F}_n$ is equivalent to a single [one-port](../../../index.md) with [I-V characteristic](../../../index.md#I-V%20Characteristic) $\mathcal{F}$:
>
>$$
>\mathcal{F} = \{(V, I) \mid \exists I_1, \dotsc, I_n: (V, I_1) \in \mathcal{F}_1, \dotsc, (V, I_n) \in \mathcal{F}_n \text{ with } I = I_1 + \cdots + I_n\}
>$$
>
>![Equivalent Parallel Circuit](./res/Equivalent%20Parallel%20Circuit.svg)
>
>In other words, the [voltage](TODO) across the equivalent [one-port](../../../index.md) is still $V$, but the [current](../../Current.md) $I$ flowing through it is the sum of the [currents](../../Current.md) flowing through $\mathcal{F}_1, \dotsc, \mathcal{F}_n$:
>
>$$
>I = \sum_{k = 1}^n I_k
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!ALGORITHM] Algorithm: Graphical Determining of the I-V Characteristic
>>
>>We want to determine $\mathcal{F}$ graphically:
>>
>>1. Draw $\mathcal{F}_1, \dotsc, \mathcal{F}_n$ on the same I-V graph.
>>2. Pick some [voltage](TODO) $v$. Sum up the corresponding [currents](../../Current.md) $i_1, \dotsc, i_n$ of $\mathcal{F}_1, \dotsc, \mathcal{F}_n$. The point $(v, i_1 + \cdots + i_n)$ is then part of $\mathcal{F}$.
>>	- If any of $\mathcal{F}_1, \dotsc, \mathcal{F}_n$ is *not* defined for $v$, then $\mathcal{F}$ is also not defined for $v$!
>>3. Repeat step 2 a few times to get a few points of $\mathcal{F}$. From these points you can roughly draw the graph of $\mathcal{F}$.
>>
>>>[!EXAMPLE]-
>>>
>>>TODO
>>> 
>>
>

>[!THEOREM] Theorem: Duality of Parallel Circuits
>
>Every [parallel circuit](./One-Port%20Interconnections.md) with $n$ components is [one-ports](./One-Ports.md#Duality) to a [series circuit](./One-Port%20Interconnections.md) with $n$ components.
>
>>[!PROOF]-
>>
>>TODO
>>
>

## One-Ports in Series

>[!DEFINITION] Definition: Series Circuits
>
>A **series circuit** is an [electrical element](../Network%20Analysis.md) which consists of [one-ports](./One-Ports.md) whose terminals are sequentially connected to one another.
>
>![Series Circuit](./res/Series%20Circuit.svg)
>

>[!THEOREM] Theorem: Current through Series Circuit
>
>The [current](../../Current.md) flowing through each [one-port](../../../index.md) in a [series circuit](./Series%20Circuits.md) is the same.
>
>![Current through Series Circuit](./res/Current%20through%20Series%20Circuit.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Equivalence of Series Circuits
>
>Every [series circuit](./Series%20Circuits.md) of [one-ports](./One-Ports.md) $\mathcal{F}_1, \dotsc, \mathcal{F}_n$ is equivalent to a single [one-port](./One-Ports.md) with [V-I characteristic](../../../index.md#V-I%20Characteristics) $\mathcal{F}$:
>
>$$
>\mathcal{F} = \{(V, I) \mid \exists V_1, \dotsc, V_n: (V_1, I) \in \mathcal{F}_1, \dotsc, (V_n, I) \in \mathcal{F}_n \text{ with } V = V_1 + \cdots + V_n\}
>$$
>
>![Equivalent Series Circuit](./res/Equivalent%20Series%20Circuit.svg)
>
>In other words, the [current](../../Current.md) flowing through the equivalent [one-port](../../../index.md) is still $I$, but the [voltage](TODO) across it is the sum of the [voltages](TODO) across $\mathcal{F}_1, \dotsc, \mathcal{F}_n$:
>
>$$
>V = \sum_{k=1}^n V_k
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>>
>
>>[!ALGORITHM] Algorithm: Graphical Determining of the I-V Characteristic
>>
>>We want to determine $\mathcal{F}$ graphically:
>>
>>1. Draw $\mathcal{F}_1, \dotsc, \mathcal{F}_n$ on the same I-V graph.
>>2. Pick some [current](../../Current.md) $i$. Sum up the corresponding [voltages](TODO) $v_1, \dotsc, v_n$ of $\mathcal{F}_1, \dotsc, \mathcal{F}_n$. The point $(v_1 + \cdots + v_n, i)$ is then part of $\mathcal{F}$.
>>	- If any of $\mathcal{F}_1, \dotsc, \mathcal{F}_n$ is *not* defined for $i$, then $\mathcal{F}$ is also not defined for $i$!
>>3. Repeat step 2 a few times to get a few points of $\mathcal{F}$. From these points you can roughly draw the graph of $\mathcal{F}$.
>>
>>>[!EXAMPLE]-
>>>
>>>TODO
>>> 
>>
>

>[!THEOREM] Theorem: Duality of Series Circuits
>
>Every [series circuit](./One-Port%20Interconnections.md) with $n$ components is [dual](../../../index.md#Duality) to a [parallel circuit](./One-Port%20Interconnections.md) with $n$ components.
>
>>[!PROOF]-
>>
>>TODO
>>
>
