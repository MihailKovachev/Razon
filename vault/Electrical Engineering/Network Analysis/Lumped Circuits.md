---
tags:
  - network-analysis
  - electrical-engineering
---

# Lumped Circuits

Modelling [electronic circuits](../Electronic%20Circuits.md) using the full mathematical apparatus of [electromagnetism](../../Physics/Classical%20Electromagnetism/Electromagnetism.md) is very accurate but also incredibly complex and becomes infeasible for larger circuits. However, under certain fairly general conditions, assumptions can be made in order to greatly simplify theoretical modelling, while still maintaining good accuracy. These assumptions are what defines a **lumped-element model** of an [electronic circuit](../Electronic%20Circuits.md).

The first assumption, known as the **quasi-static approximation**, is that the size of the circuit allows changes in the [electric field](../../Physics/Classical%20Electromagnetism/Electric%20Fields.md) and the [magnetic field](../../Physics/Classical%20Electromagnetism/Magnetic%20Fields.md) to propagate through the circuit in a way which keeps all parts of the circuit "synchronized". Otherwise, different [components](../Electronic%20Components.md) will disagree about what the electric and the magnetic field look like, until the information about the change has spread throughout the entire circuit. Taking such desynchronization into account during analysis and design significantly complicates things and so we want it to be negligible (unless we plan to exploit it in a beneficial way). To quantify whether this condition is satisfied or not, we idealize the most rapid changes we expect to see in the circuit as [periodic](TODO) with [wavelength](TODO) $\lambda$. We then check if the greatest distance $d$ between any two points on the circuit is significantly smaller than $\lambda$:

$$d \ll \lambda$$

To get a reasonable estimate of the applicability of the first condition, $\lambda$ and $d$ should differ by at least a factor of $10$.

The second assumption is that all changing magnetic fields are bounded within the electronic components and do not leak outside. This ensures that the electric field is [conservative](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Fields/Conservative%20Vector%20Fields.md) and so [electric potential](../../Physics/Classical%20Electromagnetism/Electric%20Potential.md) is well defined. It is the foundation for [Kirchhoff's voltage law](#Kirchhoff's%20Voltage%20Law).

The third assumption is that [electric charge](../../Physics/Classical%20Electromagnetism/Electric%20Charge.md) cannot accumulate inside the wires of the circuit. More rigorously, if we draw any [closed](TODO) [surface](TODO) around a region of the circuit which contains only wires but no components, then for any amount of charge which enters inside the volume bounded by the surface, the same amount of charge must exit through the surface somewhere else. This assumption is what gives rise to [Kirchhoff's current law](#Kirchhoff's%20Current%20Law).

## Kirchhoff's Laws

The defining assumptions of a [lumped circuit](./Lumped%20Circuits.md), give rise to two rules which all [currents](../Current.md) and [voltages](../../Physics/Classical%20Electromagnetism/Electric%20Potential.md) obey. These are known as **Kirchhoff's laws**.

### Kirchhoff's Current Law

**Kirchhoff's current law** mandates that the sum of the [currents](../Current.md) simultaneously entering a given [node](../Electronic%20Circuits.md) in a [lumped circuit](./Lumped%20Circuits.md) must be equal to the sum of the currents leaving the node at that same time:

$$\sum i_{\text{in}}(t) = \sum i_{\text{out}}(t)$$

>[!EXAMPLE]+
>
>![KCL Example](./res/KCL%20Example.svg)
>
>From node 1:
>
>$$i_1(t) + i_3(t) = i_2(t) + i_4(t)$$
>
>From node 2:
>
>$$0 = i_5(t) + i_6(t)$$
>
>From node 3:
>
>$$i_7(t) = i_8(t)$$
>
>From node 4:
>
>$$i_9(t) + i_{10}(t) + i_{11}(t) + i_{12}(t) = 0$$
>

Alternatively, [Kirchhoff's current law](#Kirchhoff's%20Current%20Law) can be stated as follows: the signed sum of all [currents](../Current.md) entering or leaving a [node](../Electronic%20Circuits.md) at a given time in a [lumped circuit](./Lumped%20Circuits.md) is always zero, where in-flowing [currents](../Current.md)  are taken with a plus and out-flowing currents are taken with a minus (or, alternatively, in-flowing [currents](../Current.md) are taken with a minus and out-flowing [currents](../Current.md) are taken with a plus). This is just a consequence of the fact that in a given equation, we can move all terms either to the left or to the right.

>[!EXAMPLE]+
>
>![KCL Example](./res/KCL%20Example.svg)
>
>From node 1:
>
>$$i_1(t) - i_2(t) + i_3(t) - i_4(t) = 0$$
>
>Alternatively, from node 1:
>
>$$-i_1(t) + i_2(t) - i_3(t) + i_4(t) = 0$$
>
>From node 2:
>
>$$-i_5(t) - i_6(t) = 0$$
>
>Alternatively, from node 2:
>
>$$i_5(t) + i_6(t) = 0$$
>
>From node 3:
>
>$$i_7(t) - i_8(t) = 0$$
>
>Alternatively, from node 3:
>
>$$-i_7(t) + i_8(t) = 0$$
>
>From node 4:
>
>$$i_9(t) + i_{10}(t) + i_{11}(t) + i_{12}(t) = 0$$
>
>Alternatively, from node 4:
>
>$$-i_9(t) - i_{10}(t) - i_{11}(t) - i_{12}(t) = 0$$
>

### Kirchhoff's Voltage Law

For all practical purposes, the defining assumptions of a [lumped circuit](./Lumped%20Circuits.md) allow us to treat the [electric field](../../Physics/Classical%20Electromagnetism/Electric%20Fields.md) outside of the [electronic components](../Electronic%20Components.md) as [conservative](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector%20Fields/Conservative%20Vector%20Fields.md) and thus completely described by the [electric potential](../../Physics/Classical%20Electromagnetism/Electric%20Potential.md). **Kirchhoff's voltage law** tells us that given an [oriented](TODO) [closed](TODO) [loop](TODO) in a [lumped circuit](./Lumped%20Circuits.md), the sum of the [voltages](../../Physics/Classical%20Electromagnetism/Electric%20Potential.md) along the loop at a given time whose direction aligns with the chosen orientation is equal to the sum of the voltages along the loop at the same time whose direction opposes the assigned orientation.

$$\sum v_{\text{aligned}} = \sum v_{\text{opposite}}$$

>[!EXAMPLE]+
>
>![KVL Example](./res/KVL%20Example.svg)
>
>From loop 1:
>
>$$v_1(t) + v_2(t) + v_3(t) + v_4(t) = 0$$
>
>From loop 2:
>
>$$v_9(t) + v_8(t) + v_2(t) = v_5(t)$$
>
>From loop 3:
>
>$$v_4(t) + v_1(t) + v_5(t) + v_6(t) + v_3(t) = v_7(t) + v_9(t)$$
>

Alternatively, [Kirchhoff's voltage law](#Kirchhoff's%20Voltage%20Law) can be stated as follows: given an [oriented](TODO) [closed](TODO) [loop](TODO) in a [lumped circuit](./Lumped%20Circuits.md), the signed sum of the [voltages](../../Physics/Classical%20Electromagnetism/Electric%20Potential.md) along the loop at a given time is zero, where voltages whose direction aligns with the loop orientation are taken with a plus and voltages whose direction opposes the loop orientation are taken with a minus (or, alternatively, voltages whose direction aligns with the loop orientation are taken with a minus and voltages whose direction opposes the loop orientation are taken with a plus). This is just a consequence of the fact that in a given equation, we can move all terms either to the left or to the right.

>[!EXAMPLE]+
>
>![KVL Example](./res/KVL%20Example.svg)
>
>From loop 1:
>
>$$v_1(t) + v_2(t) + v_3(t) + v_4(t) = 0$$
>
>Alternatively, from loop 1:
>
>$$-v_1(t) - v_2(t) - v_3(t) - v_4(t) = 0$$
>
>From loop 2:
>
>$$v_2(t) - v_5(t) + v_8(t) + v_9(t) = 0$$
>
>Alternatively, from loop 2:
>
>$$-v_2(t) + v_5(t) - v_8(t) - v_9(t) = 0$$
>
>From loop 3:
>
>$$v_1(t) + v_3(t) + v_4(t) + v_5(t) + v_6(t) - v_7(t) - v_9(t) = 0$$
>
>Alternatively, from loop 3:
>
>$$-v_1(t) - v_3(t) - v_4(t) - v_5(t) - v_6(t) + v_7(t) + v_9(t) = 0$$
>