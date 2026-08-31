---
tags:
    - analog-circuits
    - electrical-engineering
---

# Ideal Diodes

An **ideal diode** is an idealization of a [diode](./Diodes.md) which perfectly prevents the flow of [current](../../Current.md) in one direction, while allowing arbitrary [currents](../../Current.md) in the other.

>[!DEFINITION] Definition: Ideal Diode
>
>An **ideal diode** is a [one-port](../../../index.md) with the following [V-I characteristic](../../../index.md#V-I%20Characteristic):
>
>$$\begin{aligned}i & = 0 \qquad \text{when} \qquad v \le 0 \\ v & = 0 \qquad \text{when} \qquad i \ge 0 \end{aligned}$$
>
>![I-V of Ideal Diode](./res/I-V%20of%20Ideal%20Diode.svg)
>
>>[!NOTATION]
>>
>>The following symbol is used for [ideal diodes](./Ideal%20Diodes.md):
>>
>>![Ideal Diode Symbol](./res/Ideal%20Diode%20Symbol.svg)
>>
>

Of course, [ideal diodes](#Ideal%20Diodes) do not exist in practice, but they can be closely approximated by other, existing electrical components.

>[!EXAMPLE]- Example: Ideal Diode via Op-Amp
>
>An [ideal diode](#Ideal%20Diodes) can be constructed using an [ideal operational amplifier](../Amplifiers/Operational%20Amplifiers.md) and a [p-n diode](./Diodes.md):
>
>![Ideal Diode via Op-Amp and pn-Diode](./res/Ideal%20Diode%20via%20Op-Amp%20and%20pn-Diode.svg)
>
>As long as the [ideal op-amp](../Amplifiers/Operational%20Amplifiers.md) is operated in its [linear region](../Amplifiers/Differential%20Voltage%20Amplifiers.md), the above circuit behaves like a short circuit ($v=0$). When the op-amp saturates, the circuit behaves like an open circuit ($i=0$). This results in the characteristic behavior of an [ideal diode](#Ideal%20Diodes):
>
>$$
>\left\vert\begin{aligned} v &= 0 \quad \text{for } i \le 0 \\ i &= 0 \quad \text{for } v \le 0 \end{aligned}\right.
>$$
>
>To ensure that the [ideal op-amp](../Amplifiers/Operational%20Amplifiers.md) is operated in its [linear region](../Amplifiers/Operational%20Amplifiers.md), the input current must be positive ($i > 0$), forcing the internal [diode](./Diodes.md) to conduct.
>
>We can see this by analyzing the [network](../../Network%20Analysis/Lumped%20Elements.md).
>
>**Linear region (Conducting State):**
>
>When the input current $i$ is positive ($i > 0$), the voltage at the inverting terminal $v_{-}$ tends to rise. The [ideal op-amp](../Amplifiers/Operational%20Amplifiers.md) reacts by driving its output voltage $v_{\text{out}}$ negative. This forward-biases the internal diode (Anode at $v_{-}$, Cathode at $v_{\text{out}}$), closing the feedback loop.
>
>When the feedback loop is closed, the op-amp operates in its [linear region](../Amplifiers/Differential%20Voltage%20Amplifiers.md), ensuring $v_d = 0$, i.e., $v_{-} = v_{+}$.
>
>According to [Kirchhoff's voltage law](../../Network%20Analysis/Lumped%20Circuits.md), since the non-inverting terminal is grounded ($v_{+} = 0$), we have:
>
>$$
>v = v_{-} = v_{+} = 0
>$$
>
>Therefore, for any positive current $i$, the voltage across the port is maintained at zero. The current $i$ flows through the diode and sinks into the op-amp output.
>
>**Saturation region (Blocking State):**
>
>When the input voltage $v$ is negative ($v < 0$), the potential at the inverting terminal is lower than the non-inverting terminal ($v_{-} < v_{+}$).
>
>The [ideal op-amp](../Amplifiers/Operational%20Amplifiers.md) amplifies this difference, driving the output voltage to its positive saturation limit ($v_{\text{out}} = +V_{\text{sat}}$).
>
>We can analyze the voltage across the internal diode:
>
>$$
>v_{\text{diode}} = v_{\text{anode}} - v_{\text{cathode}} = v - V_{\text{sat}}
>$$
>
>Since $v < 0$ and $V_{\text{sat}} > 0$, the diode voltage is strictly negative ($v_{\text{diode}} < 0$). Consequently, the diode is reverse-biased and blocks current.
>
>According to [Kirchhoff's current law](../../Network%20Analysis/Lumped%20Circuits.md), the input current is the sum of the current entering the op-amp inputs and the diode current:
>
>$$
>i = i_{-} + i_{\text{diode}}
>$$
>
>However, $i_{-}$ is zero for an [ideal operational amplifier](../Amplifiers/Operational%20Amplifiers.md), and $i_{\text{diode}}$ is zero because the diode is reverse-biased. Therefore:
>
>$$
>i = 0
>$$
>
>Thus, whenever $v < 0$, the circuit acts as an open circuit.
>