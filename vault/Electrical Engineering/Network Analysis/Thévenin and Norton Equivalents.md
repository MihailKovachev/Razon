---
title: Thévenin and Norton Equivalents
tags:
    - electrical-engineering
---

# Thévenin and Norton Equivalents

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

>[!THEOREM] Norton's Theorem
>
>Every [circuit](./Lumped%20Circuits.md) comprised of only [time-invariant](./Ports.md#I-V%20Characteristic) [linear resistors](../Analog%20Circuits/Resistors.md), [time-invariant](./Ports.md#I-V%20Characteristic) [voltage sources](../Analog%20Circuits/Sources.md#Voltage%20Sources) and [direct current sources](../Analog%20Circuits/Sources.md#Current%20Sources) is equivalent to one [direct current source](../Analog%20Circuits/Sources.md#Current%20Sources) and one [time-invariant](./Ports.md#I-V%20Characteristic) [linear resistor](../Analog%20Circuits/Resistors.md) connected in [parallel](./One-Ports/One-Port%20Interconnections.md).
>
>![Norton Equivalent](./res/Norton%20Equivalent.svg)
>
>>[!DEFINITION] Definition: Internal Conductance
>>
>>We call $G_{\text{no}}$ the **internal conductance** of the circuit.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Thévenin-Norton Conversion
>
>The quantities in the [Thévenin equivalent](./Thévenin%20and%20Norton%20Equivalents.md) and the [Norton equivalent](./Thévenin%20and%20Norton%20Equivalents.md) are related as follows:
>
>$$
>R_{\text{th}} = \frac{1}{G_{\text{no}}} \qquad V_{\text{th}} = R_{\text{th}} I_{\text{no}} 
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>