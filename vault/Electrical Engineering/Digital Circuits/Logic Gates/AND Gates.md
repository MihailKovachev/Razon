---
tags:
    - digital-circuits
    - mathematics
---

# AND Gates

>[!DEFINITION] Definition: AND Gate
>
>An $n$-input **AND gate** is a [logic gate](./Logic%20Gates.md) which computes a [conjunction](../../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Functions.md#Fundamental%20Connectives) $\mathop{\mathrm{AND}}: \{0,1\}^n \to \{0, 1\}$.
>
>>[!NOTATION]
>>
>>The following symbols are used for AND gates:
>>
>>![AND Gate Symbol](../res/AND%20Gate%20Symbol.svg)
>>
>

Here is the [truth table](../../../Mathematics/Algebra/Boolean%20Algebra/Truth%20Tables.md) for this gate when $n = 2$:

|$A$|$B$|$\mathop{\operatorname{AND}}(A, B)$|
|:--:|:--:|:--:|
|$0$|$0$|$0$|
|$0$|$1$|$0$|
|$1$|$0$|$0$|
|$1$|$1$|$1$|

## CMOS Implementation

>[!ALGORITHM] Algorithm: AND Gate via CMOS
>
>An [AND gate](#And%20Gates) with $n$ inputs is implemented via [CMOS](../CMOS.md) as follows:
>
>1. Create a top layer of $n$ [PMOS transistors](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) in parallel.
>
>    - Connect the [source](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of each [PMOS](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) to the supply $V_{\text{DD}}$.
>    - Connect the [gate](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of the $i$-th [PMOS](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) to the $i$-th input.
>
>2. Create a bottom layer of $n$ [NMOS transistors](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) in series.
>
>    - Connect the [source](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of the bottom [NMOS](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) to [ground](TODO).
>    - Connect the [gate](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of the $i$-th [NMOS](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) to the $i$-th input.
>
>3. Connect the [drains](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of all [PMOS](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) to the [drain](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of the top [NMOS](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) and drive this connection into the input of an [inverter](./Inverters.md#CMOS%20Implementation).
>
>    - The output of this final [inverter](./Inverters.md#CMOS%20Implementation) is the output of the original [AND gate](#And%20Gates).
>
