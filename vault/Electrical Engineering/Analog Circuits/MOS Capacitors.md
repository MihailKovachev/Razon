---
tags:
    - analog-circuits
    - electrical-engineering
---

# MOS Capacitors

## Structure

A **metal-oxide-semiconductor capacitor** (**MOS capacitor**) is an [electronic component](../Electronic%20Circuits.md) made up of three superimposed layers:
- The top layer is the **metal layer** also known as the **M layer** or the **gate**. Historically, it was made of [aluminium](TODO), but the modern standard is heavily [doped](../../Chemistry/Semiconductor%20Doping.md) [silicon](TODO). However, for cutting-edge [components](../Electronic%20Circuits.md) on the scale of a few nanometers, manufacturers again use [metals](TODO) like [tantalum](TODO).
- The middle layer is the **insulation layer** or **oxide layer**. It is usually made up of [silicon dioxide](TODO) $\mathrm{SiO}_2$.
- The **bulk layer** or **substrate layer** is the third layer and is made up of [doped](../../Chemistry/Semiconductor%20Doping.md) [semiconductor](../../Chemistry/Electrical%20Conductivity.md), most commonly [silicon](TODO). 

![MOS Capacitor](./res/MOS%20Capacitors/MOS%20Capacitor.svg)


## Operation

Applying a [voltage](../../Physics/Classical%20Electromagnetism/Electric%20Potential.md) across a [MOS capacitor](./MOS%20Capacitors.md) influences the [charge distribution](../../Physics/Classical%20Electromagnetism/Electric%20Charge.md) inside its [substrate](./MOS%20Capacitors.md) and its behavior.

### Accumulation

Applying a negative [voltage](../../Physics/Classical%20Electromagnetism/Electric%20Potential.md) $V_{\text{GB}} \lt 0$ to the [gate](./MOS%20Capacitors.md) of a [MOS capacitor](./MOS%20Capacitors.md) with a [p-type](../../Chemistry/Semiconductor%20Doping.md#P-Type%20Semiconductors) [substrate](./MOS%20Capacitors.md) or a positive [voltage](../../Physics/Classical%20Electromagnetism/Electric%20Potential.md) $V_{\text{GB}} \gt 0$ to the [gate](./MOS%20Capacitors.md) of a [MOS capacitor](./MOS%20Capacitors.md) with an [n-type](../../Chemistry/Semiconductor%20Doping.md#N-Type%20Semiconductors) [substrate](./MOS%20Capacitors.md) causes it to enter **accumulation mode**. 

![MOS Capacitor Accumulation](./res/MOS%20Capacitors/MOS%20Capacitor%20Accumulation.svg)

The [holes](../../Chemistry/Semiconductor%20Doping.md#P-Type%20Semiconductors) / free [electrons](TODO) are attracted to the [gate](./MOS%20Capacitors.md) by the [voltage](../../Physics/Classical%20Electromagnetism/Electric%20Potential.md) and accumulate under it.

### Depletion

Applying a positive [voltage](../../Physics/Classical%20Electromagnetism/Electric%20Potential.md) $V_{\text{GB}} \gt 0$ to the [gate](./MOS%20Capacitors.md) of a [MOS capacitor](./MOS%20Capacitors.md) with a [p-type](../../Chemistry/Semiconductor%20Doping.md#P-Type%20Semiconductors) [substrate](./MOS%20Capacitors.md) or a negative [voltage](../../Physics/Classical%20Electromagnetism/Electric%20Potential.md) $V_{\text{GB}} \lt 0$ to the [gate](./MOS%20Capacitors.md) of a [MOS capacitor](./MOS%20Capacitors.md) with an [n-type](../../Chemistry/Semiconductor%20Doping.md#N-Type%20Semiconductors) [substrate](./MOS%20Capacitors.md) causes it to enter **depletion mode** as long as this [voltage](../../Physics/Classical%20Electromagnetism/Electric%20Potential.md) does not exceed a particular threshold $V_{\text{th}}$. 


![MOS Capacitor Depletion](./res/MOS%20Capacitors/MOS%20Capacitor%20Depletion.svg)

The [holes](../../Chemistry/Semiconductor%20Doping.md#P-Type%20Semiconductors) / free [electrons](TODO) are pushed away from the [gate](./MOS%20Capacitors.md) and a region devoid of mobile [charge](../../Physics/Classical%20Electromagnetism/Electric%20Charge.md) carriers forms under it.

### Inversion

If the applied [voltage](../../Physics/Classical%20Electromagnetism/Electric%20Potential.md) exceeds the threshold ($|V_{\text{GB}}| \gt |V_{\text{th}}|$), it becomes strong enough to not only push away the characteristic [charge](../../Physics/Classical%20Electromagnetism/Electric%20Charge.md) carriers of each [doped](../../Chemistry/Semiconductor%20Doping.md) [semiconductor](../../Chemistry/Electrical%20Conductivity.md) but to also attract the small number of thermically released [charge](../../Physics/Classical%20Electromagnetism/Electric%20Charge.md) carriers of the opposite type.

![MOS Capacitor Inversion](./res/MOS%20Capacitors/MOS%20Capacitor%20Inversion.svg)

A region of mobile [electrons](TODO) forms under the [gate](./MOS%20Capacitors.md) of a [MOS capacitor](./MOS%20Capacitors.md) with a [p-type](../../Chemistry/Semiconductor%20Doping.md#P-Type%20Semiconductors) [substrate](./MOS%20Capacitors.md) and a region of mobile [holes](../../Chemistry/Semiconductor%20Doping.md#P-Type%20Semiconductors) forms under the [gate](./MOS%20Capacitors.md) of a [MOS capacitor](./MOS%20Capacitors.md) with an [n-type](../../Chemistry/Semiconductor%20Doping.md#N-Type%20Semiconductors) [substrate](./MOS%20Capacitors.md). Within this region, the [semiconductor](../../Chemistry/Electrical%20Conductivity.md) essentially behaves as if it were [doped](../../Chemistry/Semiconductor%20Doping.md) in the opposite way.