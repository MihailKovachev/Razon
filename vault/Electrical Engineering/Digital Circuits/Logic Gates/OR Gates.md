---
tags:
    - digital-circuits
    - electrical-engineering
---

# OR Gates

>[!DEFINITION] Definition: OR Gate
>
>An $n$-input **OR gate** is a [logic gate](./Logic%20Gates.md) which computes a [disjunction](../../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Functions.md#Fundamental%20Connectives) $\mathop{\mathrm{OR}}: \{0,1\}^n \to \{0, 1\}$.
>
>>[!NOTATION]
>>
>>The following symbols are used for OR gates:
>>
>>![OR Gate Symbol](../res/OR%20Gate%20Symbol.svg)
>>
>

Here is the [truth table](../../../Mathematics/Algebra/Boolean%20Algebra/Truth%20Tables.md) for this gate when $n = 2$:

|$A$|$B$|$\mathop{\operatorname{OR}}(A, B)$|
|:--:|:--:|:--:|
|$0$|$0$|$0$|
|$0$|$1$|$1$|
|$1$|$0$|$1$|
|$1$|$1$|$1$|

## CMOS Implementation

>[!ALGORITHM] Algorithm: OR Gate via CMOS
>
>An [OR gate](#OR%20Gates) with $n$ inputs is implemented via [CMOS](../CMOS.md) as follows:
>
>1. Create a top layer of $n$ [PMOS transistors](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) in series.
>
>    - Connect the [source](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) of the top [PMOS](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) to the supply $V_{\text{DD}}$.
>    - Connect the [gate](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) of the $i$-th [PMOS](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) to the $i$-th input.
>
>2. Create a bottom layer of $n$ [NMOS transistors](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) in parallel.
>
>    - Connect the [source](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) of each [NMOS](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) to [ground](TODO).
>    - Connect the [gate](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) of the $i$-th [NMOS](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) to the $i$-th input.
>
>3. Connect the [drain](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) of the bottom [PMOS](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) to the [drain](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) of each [NMOS](../../Transistors/Enhancement-Mode%20Metal-Oxide-Semiconductor%20Field-Effect%20Transistor.md#Enhancement-Mode%20MOSFET) and drive this connection into the input of an [inverter](./Inverters.md#CMOS%20Implementation).
>
>    - The output of this final [inverter](./Inverters.md#CMOS%20Implementation) is the output of the original [OR gate](#OR%20Gates).
>
