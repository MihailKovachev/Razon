---
tags:
    - digital-circuits
    - electrical-engineering
---

# Inverters

>[!DEFINITION] Definition: Inverter
>
>An **inverter** or **NOT gate** is a [logic gate](./Logic%20Gates.md) which computes [negation](../../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Functions.md#Fundamental%20Connectives).
>
>>[!NOTATION]
>>
>>The following symbols are use for inverters:
>>
>>![Inverter Gate Symbol](../res/Inverter%20Gate%20Symbol.svg)
>>
>

Here is the [truth table](../../../Mathematics/Algebra/Boolean%20Algebra/Truth%20Tables.md) for this gate:

|$A$|$\mathop{\operatorname{NOT}}(A)$|
|:--:|:--:|
|$0$|$1$|
|$1$|$0$|


## CMOS Inverter

An [inverter](./Inverters.md) can be implemented using [CMOS](../CMOS.md) in the following way:

![CMOS Inverter](./res/CMOS%20Inverter.svg)

The [source](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of the [PMOS](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) is connected to a [voltage source](../../Analog%20Circuits/Sources.md) which ideally supplies a constant [voltage](../../../Physics/Classical%20Electromagnetism/Electric%20Potential.md), while the [source](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of the [NMOS](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) is connected to [ground](TODO). The [drains](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) of the [MOSFETs](../../Analog%20Circuits/Transistors/MOSFET.md#Enhancement-Mode%20MOSFET) are connected to another. 

To see why this [circuit](../Digital%20Circuits.md) behaves like an [inverter](./Inverters.md), we need to analyze it:

![CMOS Inverter Analysis](./res/CMOS%20Inverter%20Analysis.svg)

TODO: Analog Analysis

![CMOS Inverter VTC](./res/CMOS%20Inverter%20VTC.svg)

In summary, the [digital](../Digital%20Circuits.md) behavior is the following:

|$V_{\text{in}}$|PMOS|NMOS|$V_{\text{out}}$|
|:--:|:--:|:--:|:--:|
|$0$|conducting|non-conducting|$1$|
|$1$|non-conducting|conducting|$0$|