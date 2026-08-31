---
tags:
    - digital-circuits
    - electrical-engineering
---

# NOR Gates

>[!DEFINITION] Definition: NOR Gate
>
>A **NOR gate** is a [logic gate](./Logic%20Gates.md) which computes the [negation](../../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Functions.md#Fundamental%20Connectives) of a [disjunction](../../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Functions.md#Fundamental%20Connectives):
>
>$$\mathop{\operatorname{NOT}} \circ \mathop{\operatorname{OR}}$$
>
>>[!NOTATION]
>>
>>The following symbols are used for NOR gates:
>>
>>![NOR Gate Symbol](../res/NOR%20Gate%20Symbol.svg)
>>
>

Here is the [truth table](../../../Mathematics/Algebra/Boolean%20Algebra/Truth%20Tables.md) for this gate when $n = 2$:

|$A$|$B$|$\mathop{\operatorname{NOR}}(A, B)$|
|:--:|:--:|:--:|
|$0$|$0$|$1$|
|$0$|$1$|$0$|
|$1$|$0$|$0$|
|$1$|$1$|$0$|

## CMOS Implementation

>[!ALGORITHM] Algorithm: NOR Gate via CMOS
>
>A [NOR gate](#NOR%20Gates) with $n$ inputs is implemented via [CMOS](../CMOS.md) as follows:
>
>1. Create a top layer of $n$ [PMOS transistors](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) in series.
>
>    - Connect the [source](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of the top [PMOS](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) to the supply $V_{\text{DD}}$.
>    - Connect the [gate](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of the $i$-th [PMOS](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) to the $i$-th input.
>
>2. Create a bottom layer of $n$ [NMOS transistors](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) in parallel.
>
>    - Connect the [source](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of each [NMOS](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) to [ground](TODO).
>    - Connect the [gate](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of the $i$-th [NMOS](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) to the $i$-th input.
>
>3. Connect the [drain](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of the bottom [PMOS](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) to the [drain](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of each [NMOS](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) and drive this connection as the output.
>
>>[!EXAMPLE]- Example: 2-Input NOR
>>
>>![CMOS NOR](./res/CMOS%20NOR.svg)
>>
>

