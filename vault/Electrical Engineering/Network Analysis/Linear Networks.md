---
tags:
    - network-analysis
    - electrical-engineering
---

# Linear Networks

## Superposition Principle

>[!THEOREM] Theorem: The Superposition Principle
>
>Let $\mathcal{N}$ be a [linear](./Linear%20Networks.md) [network](./Lumped%20Networks.md) with
>
>$$\boldsymbol{M}\boldsymbol{v}(t) + \boldsymbol{N}\boldsymbol{i}(t) = \boldsymbol{e}(t).$$
>
>Each component of the [branch voltage vector](./Lumped%20Networks.md) and each component of the [branch current vector](./Lumped%20Networks.md) can be expressed as a [linear combination](../../Mathematics/Algebra/Vector%20Spaces/Linear%20Combinations.md) of the components of $\boldsymbol{e}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

The [superposition principle](#Superposition%20Principle) is powerful because it allows us to look at all [ideal sources](../Analog%20Circuits/Sources.md) one by one and ignore the rest. The overall result is the sum of these partial results.

>[!ALGORITHM] Algorithm: The Superposition Principle
>
>1. For each [ideal source](../Analog%20Circuits/Sources.md) $j$, calculate the [branch voltage vector](./Lumped%20Networks.md) $\boldsymbol{v}^{(j)}$ and the [branch current vector](./Lumped%20Networks.md) $\boldsymbol{i}^{(j)}$ by assuming that all other [ideal sources](../Analog%20Circuits/Sources.md) are zero.
>
>    - [Ideal voltage sources](../Analog%20Circuits/Sources.md#Ideal%20Voltage%20Sources) become [short circuits](./One-Ports/Short%20Circuits.md).
>    - [Ideal current sources](../Analog%20Circuits/Sources.md#Ideal%20Current%20Sources) become [open circuits](./One-Ports/Open%20Circuits.md).
>    - [Controlled sources](../Analog%20Circuits/Sources.md) remain unaffected!
>
>2. The real [branch voltage vector](./Lumped%20Networks.md) $\boldsymbol{v}$ is the sum of the [branch voltage vectors](./Lumped%20Networks.md) $\boldsymbol{v}^{(j)}$ and the real [branch current vector](./Lumped%20Networks.md) $\boldsymbol{i}$ is the sum of the [branch current vectors](./Lumped%20Networks.md)  $\boldsymbol{i}^{(j)}$.
>
>$$\boldsymbol{v} = \sum_j \boldsymbol{v}^{(j)} \qquad \boldsymbol{i} = \sum_j \boldsymbol{i}^{(j)}$$
>

## One-Port Equivalents

>[!THEOREM] Theorem: Hemholtz-Thévenin Equivalent
>
>Every [linear](./Linear%20Networks.md) [resistive](./Linear%20Networks.md) [network](./Linear%20Networks.md) with only two accessible [terminals](./Linear%20Networks.md) which form a [port](./Ports.md) is equivalent to an [ideal voltage source](../Analog%20Circuits/Sources.md#Ideal%20Voltage%20Sources) and a [linear resistor](../Analog%20Circuits/Resistors.md) [in series](./One-Ports/One-Port%20Interconnections.md#One-Ports%20in%20Series).
>
>![Hemholtz-Thévenin Equivalent](./res/Hemholtz-Thévenin%20Equivalent.svg)
>
>>[!DEFINITION] Definition: Internal Resistance
>>
>>We call $R_{\text{H-T}}$ the **internal resistance** of the [network](./Linear%20Networks.md).
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Mayer-Norton Equivalent
>
>Every [linear](./Linear%20Networks.md) [resistive](./Linear%20Networks.md) [network](./Linear%20Networks.md) with only two accessible [terminals](./Linear%20Networks.md) which form a [port](./Ports.md) is equivalent to an [ideal current source](../Analog%20Circuits/Sources.md#Ideal%20Current%20Sources) and a [linear resistor](../Analog%20Circuits/Resistors.md) [in parallel](./One-Ports/One-Port%20Interconnections.md#One-Ports%20in%20Series).
>
>![Mayer-Norton Equivalent](./res/Mayer-Norton%20Equivalent.svg)
>
>>[!DEFINITION] Definition: Internal Conductance
>>
>>We call $G_{\text{M-N}}$ the **internal conductance** of the [network](./Linear%20Networks.md).
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem:
>
>The [internal resistance](./Linear%20Networks.md) and [internal conductance](./Linear%20Networks.md) of a [linear network](./Linear%20Networks.md) are related as follows:
>
>$$R_{\text{H-T}} = - \frac{v_{\text{H-T}}(t)}{i_{\text{M-N}}(t)} \qquad G_{\text{M-N}} = - \frac{i_{\text{M-N}}(t)}{v_{\text{H-T}}(t)}$$
>
>$$R_{\text{H-T}} = \frac{1}{G_{\text{M-N}}} \qquad G_{\text{M-N}} = \frac{1}{R_{\text{H-T}}}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>