---
title: MMIX Processor
tags:
    - computer-science
---

# The MMIX Processor

The [MMIX architecture](./MMIX.md) features a simple 64-bit processor comprised of the following:
- 256 [registers](../../../Electrical%20Engineering/Digital%20Circuits/Registers.md) which are **general-purpose registers** and are labelled `$0`, `$1`, ..., `$255`. Each is 64 bits wide.
- 32 [registers](../../../Electrical%20Engineering/Digital%20Circuits/Registers.md) which are **special registers** and are labelled `rA`, `rB`, `rC`, ..., `rZ`, `rBB`, `rTT`, `rWW`, `rXX`, `rYY`, `rZZ`. Each is 64 bits wide.
- an **arithmetic-logic unit (ALU)** with two 64-bit inputs and one 64-bit output.

The two inputs of the [ALU](./The%20MMIX%20Processor.md) are connected to all [general-purpose registers](./The%20MMIX%20Processor.md) via a [multiplexer](../../../Electrical%20Engineering/Digital%20Circuits/Multiplexers.md) and its output is also connected to all [general-purpose registers](./The%20MMIX%20Processor.md) via a [demultiplexer](../../../Electrical%20Engineering/Digital%20Circuits/Demultiplexers.md).

## Data Organization

The [MMIX architecture](./MMIX.md) logically groups bits in the following way:
- 1 **byte** = 8 bits;
- 1 **wyde** = 2 [bytes](#Data%20Organization) = 16 bits;
- 1 **tetra** = 2 [wydes](#Data%20Organization) = 4 [bytes](#Data%20Organization) = 32 bits;
- 1 **octa** = 2 [tetras](#Data%20Organization) = 4 [wydes](#Data%20Organization) = 8 [bytes](#Data%20Organization) = 64 bits;

The [MMIX processor](./The%20MMIX%20Processor.md) is [big-endian](TODO), i.e. it always addresses the [most significant byte](TODO), while the rest of the bytes are stored at the subsequent, higher addresses.

## General-Purpose Registers

The [general-purpose registers](./The%20MMIX%20Processor.md) are connected via 64-bit [bus](TODO) to a [storage device](./The%20MMIX%20Storage.md) which contains $2^{64}$ cells, each 8-bit in size.

For the most part, they can be used for any purpose. However, they are divided into three groups, whose boundaries are determined by the 
- The **local registers** begin (inclusively) at `$0` and end (exclusively) with the [general-purpose register](#General-Purpose%20Registers) whose number is stored in the `rL` [special register](#Special%20Registers).
- The **marginal registers** begin (inclusively) with the [general-purpose register](#General-Purpose%20Registers) whose number is stored in the `rL` [special register](#Special%20Registers) and end (exclusively)  with the [general-purpose register](#General-Purpose%20Registers) whose number is stored in the `rG` [special register](#Special%20Registers).
- The **global registers** begin (inclusively) with the [general-purpose register](#General-Purpose%20Registers) whose number is stored in the `rG` [special register](#Special%20Registers) and end (inclusively) at `$255`.

![MMIX General-Purpose Registers](./res/MMIX%20General-Purpose%20Registers.svg)

The [global register](#General-Purpose%20Registers) `$0` contains `argc`, `$1` contains `argv` and `$255` contains the address of `main`.

## Special Registers

The values of the [special registers](./The%20MMIX%20Processor.md) are strictly determined by the state of the processor and the operations it is executing.