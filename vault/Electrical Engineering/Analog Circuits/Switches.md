---
tags:
    - analog-circuits
    - electrical-engineering
---

# Switches

>[!DEFINITION] Definition: Switch
>
>A **switch** is a [one-port](../../index.md) which can behave either as an [open circuit](../Network%20Analysis/One-Ports/Open%20Circuits.md) or a [short circuit](../Network%20Analysis/One-Ports/Short%20Circuits.md).
>
>>[!NOTATION]
>>
>>When a [switch](./Switches.md) behaves like an [open circuit](../Network%20Analysis/One-Ports/Open%20Circuits.md), it is denoted by
>>
>>![Open Switch Symbol](../Network%20Analysis/One-Ports/res/Open%20Switch%20Symbol.svg)
>>
>>When it behaves like a [short circuit](../Network%20Analysis/One-Ports/Short%20Circuits.md), it is denoted by
>>
>>![Closed Switch Symbol](./res/Closed%20Switch%20Symbol.svg)
>>
>

We often model [switches](./Switches.md) using a [function](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) $S(t)$ defined in the following way:

$$
S(t) \overset{\text{def}}{=} \begin{cases} 1 \qquad \text{when the switch is closed} \\ 0 \qquad \text{when the switch is open}\end{cases}
$$

>[!THEOREM] Theorem: Duality of Switches
>
>The [dual](../../index.md#Duality) of a [switch](./Switches.md) $S$ is the [switch](./Switches.md) $S_d$ which is open when $S$ is closed and is closed when $S$ is open:
>
>$$
>S_d(t) = 1 - S(t)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>