---
tags:
    - digital-circuits
    - electrical-engineering
---

# Pipelining

**Pipelining** is a technique which allows us to increase [clock frequencies](./Circuit%20Timing.md#Synchronization). It works by splitting long [combinational](./Combinational%20Circuits.md) paths using [registers](./Registers.md). By doing this split correctly, it is often possible to increase [clock frequencies](./Circuit%20Timing.md#Synchronization) because the slowest [combinational](./Combinational%20Circuits.md) paths between each stage of [registers](./Registers.md) become shorter than the original slowest [combinational](./Combinational%20Circuits.md) path. Therefore, the [setup constraint](./Circuit%20Timing.md#Synchronization) is weakened.
