---
tags:
    - analog-circuits
    - electrical-engineering
---

# Operational Amplifiers

>[!DEFINITION] Definition: Operational Amplifier
>
>A **operational amplifier** is a [finite-gain differential voltage amplifier](./Differential%20Voltage%20Amplifiers.md) such that the [currents](../../Current.md) $i_{-}$ and $i_{+}$ flowing [into](../../Network%20Analysis/Reference%20Directions.md) the $+$ and $-$ [inputs](../../Network%20Analysis/Lumped%20Elements.md), respectively, are always zero:
>
>$$
>\left\vert \begin{aligned} i_{-} &= 0 \\ i_{+} &= 0 \end{aligned}\right.
>$$
>
>>[!NOTATION]
>>
>>The symbol for an [operational amplifier](./Operational%20Amplifiers.md) is the same as the one for [finite-saturation differential voltage amplifier](./Differential%20Voltage%20Amplifiers.md). The fact that $i_{-}$ and $i_{+}$ are always zero needs to inferred from context:
>>
>>![Op-Amp Symbol](./res/Op-Amp%20Symbol.svg)
>>
>

>[!DEFINITION] Definition: Ideal Operational Amplifier
>
>An **ideal operational amplifier** (**ideal op-amp**) is an [infinite-gain differential voltage amplifier](./Differential%20Voltage%20Amplifiers.md) such that the [currents](../../Current.md) $i_{-}$ and $i_{+}$ flowing [into](../../Network%20Analysis/Reference%20Directions.md) the $+$ and $-$ [inputs](../../Network%20Analysis/Lumped%20Elements.md), respectively, are always zero:
>
>$$
>\left\vert \begin{aligned} i_{-} &= 0 \\ i_{+} &= 0 \end{aligned}\right.
>$$
>
>>[!NOTATION]
>>
>>The symbol for an [ideal operational amplifier](./Operational%20Amplifiers.md) is the same as the one for [infinite-gain differential voltage amplifiers](./Differential%20Voltage%20Amplifiers.md). The fact that $i_{-}$ and $i_{+}$ are always zero needs to inferred from context:
>>
>>![Ideal Op-Amp Symbol](./res/Ideal%20Op-Amp%20Symbol.svg)
>>
>

Of course, no physical component can get $i_{-}$ and $i_{+}$ to be exactly zero. However, we can get them to be *really* close to zero, on the order of a few tens of [nanoamperes](../../Current.md). 

>[!THEOREM] Theorem: Ideal Op-Amp Equivalent Models
>
>An [ideal op-amp](#Operational%20Amplifiers) is equivalent to:
>- an [open circuit](../../Network%20Analysis/One-Ports/Open%20Circuits.md) and an [independent voltage source](../Sources.md) with [voltage](TODO) $-V_{sat}$ when $v_d \lt 0$;
>- a [nullor](../../Network%20Analysis/Two-Ports/Nullors.md) when $v_d = 0$;
>- a [open circuit](../../Network%20Analysis/One-Ports/Open%20Circuits.md) and an [independent voltage source](../Sources.md) with [voltage](TODO) $+V_{sat}$ when $v_d \lt 0$.
>
>![Ideal Op-Amp Equivalents](./res/Ideal%20Op-Amp%20Equivalents.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>