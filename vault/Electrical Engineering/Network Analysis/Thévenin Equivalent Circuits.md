---
tags:
    - network-analysis
    - electrical-engineering
---

# Thévenin Equivalent Circuits

>[!THEOREM] Thévenin's Theorem
>
>Every [circuit](./Lumped%20Circuits.md) comprised of only [time-invariant](./Ports.md#I-V%20Characteristic) [linear resistors](../Analog%20Circuits/Resistors.md), [time-invariant](./Ports.md#I-V%20Characteristic) [voltage sources](../Analog%20Circuits/Sources.md#Voltage%20Sources) and [direct current sources](../Analog%20Circuits/Sources.md#Current%20Sources) is equivalent to one [time-invariant](./Ports.md#I-V%20Characteristic) [ideal voltage source](../Analog%20Circuits/Sources.md#Voltage%20Sources) and one [time-invariant](./Ports.md#I-V%20Characteristic) [linear resistor](../Analog%20Circuits/Resistors.md) connected in [series](./Series%20Circuits.md).
>
>![Thévenin Equivalent](./res/Thévenin%20Equivalent.svg)
>
>>[!DEFINITION] Definition: Internal Resistance
>>
>>We call $R_{\text{th}}$ the **internal resistance** of the circuit.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Thévenin Equivalent Resistance
>
>The [Thévenin equivalent resistance](./Thévenin%20Equivalent%20Circuits.md) is equal to the ratio of the [open-circuit voltage](TODO) and [short-circuit current](TODO):
>
>$$R_{\text{th}} = \frac{V_{\text{oc}}}{I_{\text{sc}}}$$
>
>>[!TIP] Tip: Determining Thévenin Equivalent Resistance
>>
>>To determine the [Thévenin equivalent resistance](./Thévenin%20Equivalent%20Circuits.md) replace all [ideal voltage sources](./Ideal%20Voltage%20Source.md) with a [short circuit](./One-Ports/Short%20Circuits.md) and all [ideal current sources](./Ideal%20Current%20Source.md) with an [open circuit](./One-Ports/Open%20Circuits.md).
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!ALGORITHM] Algorithm: Thévenin Equivalent Parameters
>
>1. Determine the 
>