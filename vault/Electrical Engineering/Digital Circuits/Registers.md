---
title: Registers
tags:
    - digital-circuits
    - electrical-engineering
---

# Registers

TODO

# Shift Registers

>[!DEFINITION] Definition: Shift Register
>
>A **shift register** is a [register](./Registers.md) capable of shifting the data in each of its cells to the neighboring cell in a specified direction.
>

>[!DEFINITION] Definition: Right Shift Register
>
>A **right shift register** is a [shift register](./Registers.md) $SR$ whose bits are shifted from the most significant bit to the least significant bit:
>
>$$
>SR[k] \to SR[k-1]
>$$
>

>[!DEFINITION] Definition: Left Shift Register
>
>A **left shift register** is a [shift register](./Registers.md) $SR$ whose bits are shifted from the least significant bit to the most significant bit:
>
>$$
>SR[k] \to SR[k+1]
>$$
>

## Parallel Shift Registers

We can construct an $n$-bit [parallel](./Registers.md) [shift register](#Shift%20Registers) using an $n$-bit [parallel register](./Registers.md) $R$ and a [multiplexer](./Multiplexers.md).

For a [right shift register](#Shift%20Registers), the [multiplexer](./Multiplexers.md) essentially selects between the [load bus](./Registers.md) $L[0], \dotsc, L[n-1]$ and either the bits $R[1],\dotsc, R[n-1]$. An additional input $b$ determines what value to assign to the most significant bit $R[n-1]$ when shifting:

![Right Shift Register](./res/Right%20Shift%20Register.svg)
