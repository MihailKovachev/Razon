---
tags:
    - digital-circuits
    - electrical-engineering
---

# XOR Gates

>[!DEFINITION] Definition: XOR Gate
>
>A **XOR gate** is a [logic gate](./Logic%20Gates.md) which computes the [exclusive disjunction](../../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Functions.md#Fundamental%20Connectives).
>
>>[!NOTATION]
>>
>>The following symbols are used for XOR gates:
>>
>>![XOR Gate Symbol](../res/XOR%20Gate%20Symbol.svg)
>>
>

Here is the [truth table](../../../Mathematics/Algebra/Boolean%20Algebra/Truth%20Tables.md) for this gate:

|$A$|$B$|$\mathop{\operatorname{XOR}}(A, B)$|
|:--:|:--:|:--:|
|$0$|$0$|$0$|
|$0$|$1$|$1$|
|$1$|$0$|$1$|
|$1$|$1$|$0$|

## CMOS Implementation

Implementing a [XOR gate](./XOR%20Gates.md) via [CMOS](../CMOS.md) is done using the following formula:

$$A \oplus B = \overline{(A+\overline{B})(\overline{A}+B)}$$

This formula is the [negation](../../../Mathematics/Algebra/Boolean%20Algebra/Negation.md) of the [function](../../../Mathematics/Algebra/Boolean%20Algebra/Boolean%20Functions.md) $(A+\overline{B})(\overline{A}+B)$. This means that we can follow the standard procedure for designing a [CMOS](../CMOS.md) which implements $(A+\overline{B})(\overline{A}+B)$, but we can omit the [inverter](./Inverters.md) at the end.

![CMOS XOR](./res/CMOS%20XOR.svg)