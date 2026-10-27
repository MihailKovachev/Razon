---
tags:
    - digital-circuits
    - electrical-engineering
---

# NAND Gates

>[!DEFINITION] Definition: NAND Gate
>
>A **NAND gate** is a [logic gate](./Logic%20Gates.md) which computes the [negation](../../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Functions.md#Fundamental%20Connectives) of a [conjunction](../../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Functions.md#Fundamental%20Connectives):
>
>$$\mathop{\operatorname{NOT}} \circ \mathop{\operatorname{AND}}$$
>
>>[!NOTATION]
>>
>>The following symbols are used for NAND gates:
>>
>>![NAND Gate Symbol](../res/NAND%20Gate%20Symbol.svg)
>>
>

Here is the [truth table](../../../Mathematics/Algebra/Boolean%20Algebra/Truth%20Tables.md) for this gate when $n = 2$:

|$A$|$B$|$\mathop{\operatorname{NAND}}(A, B)$|
|:--:|:--:|:--:|
|$0$|$0$|$1$|
|$0$|$1$|$1$|
|$1$|$0$|$1$|
|$1$|$1$|$0$|

## CMOS Implementation

A [NAND gate](./NAND%20Gates.md) can be implemented using [CMOS](../CMOS.md) in the following way:

>[!ALGORITHM] Algorithm: NAND Gate via CMOS
>
>A [NAND gate](#And%20Gates) with $n$ inputs is implemented via [CMOS](../CMOS.md) as follows:
>
>1. Create a top layer of $n$ [PMOS transistors](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) in parallel.
>
>    - Connect the [source](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) of each [PMOS](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) to the supply $V_{\text{DD}}$.
>    - Connect the [gate](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) of the $i$-th [PMOS](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) to the $i$-th input.
>
>2. Create a bottom layer of $n$ [NMOS transistors](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) in series.
>
>    - Connect the [source](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) of the bottom [NMOS](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) to [ground](TODO).
>    - Connect the [gate](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) of the $i$-th [NMOS](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) to the $i$-th input.
>
>3. Connect the [drains](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) of all [PMOS](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) to the [drain](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) of the top [NMOS](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) and drive this connection as the output.
>
>>[!EXAMPLE]- Example: 2-Input NAND
>>
>>![CMOS NAND](./res/CMOS%20NAND.svg)
>>
>
