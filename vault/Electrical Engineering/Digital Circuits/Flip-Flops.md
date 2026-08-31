---
tags:
    - digital-circuits
    - electrical-engineering
---

# Flip-Flops

>[!DEFINITION] Definition: Flip-Flop
>
>A **flip-flop** is an [edge-triggered](./Circuit%20Triggering.md#Edge%20Triggering) [digital circuit](./Digital%20Circuits.md) which store a single bit of information by switching between two stable states of its outputs.
>

# D Flip-Flops

A **D flip-flop** is a [flip-flop](./Flip-Flops.md) implemented using two [D latches](./Latches.md#D%20Latches) in the so called **master-slave configuration**:

![D Flip-Flops](./res/Flip-Flops/D%20Flip-Flops.svg)

The left [D latch](./Latches.md#D%20Latches) is known as the **master latch**, while the right [D latch](./Latches.md#D%20Latches) is called the **slave latch**.

For the [D flip-flop](#D%20Flip-Flops) with a [positive edge trigger](./Circuit%20Triggering.md#Edge%20Triggering):
- When $Clk$ is in a stable state of $0$, the [inverter](./Logic%20Gates/Logic%20Gates.md) makes the master [active](./Circuit%20Triggering.md) and its output is the same as $D$. However, the slave is blocked because $Clk = 0$, so the final output remains unchanged and does not yet reflect the input $D$.
- When $Clk$ transitions from $0$ to $1$, the [inverter](./Logic%20Gates/Logic%20Gates.md) switches from $1$ to $0$, blocking the master latch (which freezes the current value of $D$). Simultaneously, the slave becomes [active](./Circuit%20Triggering.md) and the output of the master can now propagate to the final output.
- When $Clk$ is in a stable state of $1$, the slave is [active](./Circuit%20Triggering.md) and its output is equal to the output of the master latch. However, the master is blocked by the [inverter](./Logic%20Gates/Logic%20Gates.md), which means changes in input $D$ do not affect the stored value in the master or the final output.
- When $Clk$ transitions from $1$ to $0$, the slave becomes blocked (holding the final output stable) while the [inverter](./Logic%20Gates/Logic%20Gates.md) makes the master [active](./Circuit%20Triggering.md), allowing it to track the input $D$ again.

For the [D flip-flop](#D%20Flip-Flops) with a [negative edge trigger](./Circuit%20Triggering.md#Edge%20Triggering):
- When $Clk$ is in a stable state of $0$, the [inverter](./Logic%20Gates/Logic%20Gates.md) makes the slave [active](./Circuit%20Triggering.md) and its output is equal to the **output** of the master latch. However, it is not possible to change the output of the master latch because it is blocked, since $Clk = 0$.
- When $Clk$ transitions from $0$ to $1$, it enables the master latch which updates its output to $D$, but the [inverter](./Logic%20Gates/Logic%20Gates.md) switches from $1$ to $0$, blocking the slave.
- When $Clk$ is in a stable state of $1$, the master is [active](./Circuit%20Triggering.md) and its output is the same as $D$. However, the [inverter](./Logic%20Gates/Logic%20Gates.md) blocks the slave which means that it cannot update its final output.
- When $Clk$ transitions from $1$ to $0$, the master becomes blocked (latching the current value) while the [inverter](./Logic%20Gates/Logic%20Gates.md) makes the slave [active](./Circuit%20Triggering.md), allowing the output of the master to propagate to the final outputs.

>[!NOTATION]
>
>The following symbols are used for [D flip-flops](#D%20Flip-Flopts):
>
>![D Flip-Flop Symbols](./res/Flip-Flops/D%20Flip-Flop%20Symbols.svg)
>
>Whether the [D flip-flop](#D%20Flip-Flopts) has a [positive edge trigger](./Circuit%20Triggering.md#Edge%20Triggering) or a [negative edge trigger](./Circuit%20Triggering.md#Edge%20Triggering) must be inferred from context.
>

In practice, [D flip-flops](#D%20Flip-Flops) almost always have a [positive edge trigger](./Circuit%20Triggering.md#Edge%20Triggering).
