---
tags:
    - network-analysis
    - electrical-engineering
---

# One-Port Linearity

>[!DEFINITION] Definition: One-Port Linearity
>
>
>

>[!THEOREM] Theorem: Linear One-Port
>
>A [one-port](./One-Ports.md) is [linear](../Strictly%20Linear%20Multiports.md) if and only if its [V-I characteristic](./One-Ports.md#V-I%20Characteristic) can be written as
>
>$$
>av + bi + c = 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

Graphically, the [I-V characteristic](./One-Ports.md#V-I%20Characteristic) of a [linear one-port](#Linear%20One-Ports) is a straight line:

![I-V Linear One-Port](./res/I-V%20Linear%20One-Port.svg)

>[!THEOREM] Theorem: Thévenin Equivalent
>
>The [Thévenin equivalent](../Thévenin%20and%20Norton%20Equivalents.md) of a [linear one-port](./Linear%20Resistive%20One-Ports.md) with [I-V characteristic](./One-Ports.md#V-I%20Characteristic) $v = Ri + V$ is a [series circuit](./One-Port%20Interconnections.md) of an [ideal voltage source](../../Analog%20Circuits/Sources.md#Ideal%20Voltage%20Source) and a [linear resistor](../../Analog%20Circuits/Resistors.md#Linear%20Resistors) with [resistance](../../Analog%20Circuits/Resistors.md#Linear%20Resistors) $R$:
>
>![Thévenin Equivalent of Linear One-Port](./res/Thévenin%20Equivalent%20of%20Linear%20One-Port.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Norton Equivalent
>
>The [Norton equivalent](../Thévenin%20and%20Norton%20Equivalents.md) of a [linear one-port](./Linear%20Resistive%20One-Ports.md) with [I-V characteristic](./One-Ports.md#V-I%20Characteristic) $i = Gv + I$ is a [parallel circuit](./One-Port%20Interconnections.md) of an [ideal current source](../../Analog%20Circuits/Sources.md#Ideal%20Voltage%20Source) and a [linear resistor](../../Analog%20Circuits/Resistors.md#Linear%20Resistors) with [conductance](../../Analog%20Circuits/Resistors.md#Linear%20Resistors) $G$:
>
>![Norton Equivalent of Linear One-Port](./res/Norton%20Equivalent%20of%20Linear%20One-Port.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Linearization

Non-linear [one-ports](./One-Ports.md) can have very complicated [I-V characteristics](./One-Ports.md#I-V%20Characteristic), which often makes their analysis in the context of a particular [circuit](../../Electronic%20Circuits.md) difficult. However, if we know that the [one-port](./One-Ports.md) will only be operated within a small region around a specific point on its [I-V characteristic](./One-Ports.md#I-V%20Characteristic), then it can be approximated very well as a [linear one-port](./Linear%20Resistive%20One-Ports.md).

>[!DEFINITION] Definition: Linearization
>
>Suppose we have a non-linear [one-port](./One-Ports.md) with [I-V characteristic](./One-Ports.md#I-V%20Characteristic) $\mathcal{F}_{\text{non-linear}}$ and a point $(v, i) \in \mathcal{F}_{\text{non-linear}}$.
>
>**Linearization** is the process of finding a [linear one-port](./Linear%20Resistive%20One-Ports.md) whose [I-V characteristic](./One-Ports.md#I-V%20Characteristic) $\mathcal{F}_{\text{linear}}$ resembles $\mathcal{F}_{\text{non-linear}}$ as much as possible around the point $(v, i)$.
>

>[!THEOREM] Theorem: Linearization via Implicit Representation
>
>Suppose we have a non-linear [one-port](./One-Ports.md) with [I-V characteristic](./One-Ports.md#I-V%20Characteristic) $\mathcal{F}_{\text{non-linear}}$ and let $(v, i) \in \mathcal{F}_{\text{non-linear}}$.
>
>If $\mathcal{F}_{\text{non-linear}}$ has an [implicit representation](./One-Ports.md#I-V%20Characteristic) $f(V, I) = 0$, then the [I-V characteristic](./One-Ports.md#I-V%20Characteristic) $\mathcal{F}_{\text{linear}}$ of the [linear one-port](./Linear%20Resistive%20One-Ports.md) which best approximates $\mathcal{F}_{\text{non-linear}}$ around $(v, i)$ has an [implicit representation](./One-Ports.md#I-V%20Characteristic) which can be obtained using $f$'s [partial derivatives](../../../Mathematics/Analysis/Real%20Analysis/Real%20Scalar%20Fields/Differentiation%20of%20Real%20Scalar%20Fields.md#Partial%20Differentiability):
>
>$$
>\frac{\partial f}{\partial V}(v, i) \cdot (V - v) + \frac{\partial f}{\partial I}(v, i) \cdot (I - i) = 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Linearization via Explicit Representation
>
>Suppose we have a non-linear [one-port](./One-Ports.md) with [I-V characteristic](./One-Ports.md#I-V%20Characteristic) $\mathcal{F}_{\text{non-linear}}$ and let $(v, i) \in \mathcal{F}_{\text{non-linear}}$.
>
>If $\mathcal{F}_{\text{non-linear}}$ has an [explicit representation](./One-Ports.md#I-V%20Characteristic) $I = G(V)$, then the [I-V characteristic](./One-Ports.md#I-V%20Characteristic) $\mathcal{F}_{\text{linear}}$ of the [linear one-port](./Linear%20Resistive%20One-Ports.md) which best approximates $\mathcal{F}_{\text{non-linear}}$ around $(v, i)$ has an [explicit representation](./One-Ports.md#I-V%20Characteristic) which can be obtained using $G$'s [derivative](../../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Differentiability%20(Real%20Functions).md):
>
>$$
>I = G'(v) \cdot (V - v) + i 
>$$
>
>If $\mathcal{F}_{\text{non-linear}}$ has an [explicit representation](./One-Ports.md#I-V%20Characteristic) $V = R(I)$, then the [I-V characteristic](./One-Ports.md#I-V%20Characteristic) $\mathcal{F}_{\text{linear}}$ of the [linear one-port](./Linear%20Resistive%20One-Ports.md) which best approximates $\mathcal{F}_{\text{non-linear}}$ around $(v, i)$ has an [explicit representation](./One-Ports.md#I-V%20Characteristic) which can be obtained using $R$'s [derivative](../../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Differentiability%20(Real%20Functions).md):
>
>$$
>V = R'(i) \cdot (I - i) + v
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>