---
tags:
    - network-analysis
    - electrical-engineering
---

# Small-Signal Analysis

**Small-signal analysis** is a technique for analyzing [circuits](../../Electronic%20Circuits.md) which contain [time-variant](../Ports.md) components, provided that [currents](../../Current.md) / [voltages](TODO) deviate only slightly from some fixed base values. 

Given such a [time-variant](../Ports.md) component, the idea is to represent its signal $S(t)$ (where $S(t)$ is a label for either the [current](../../Current.md) $I(t)$ or the [voltage](TODO) $V(t)$) into the sum of this constant base value and a time-dependent part:

$$
S(t) = S_Q + \Delta S(t)
$$

>[!ALGORITHM] Algorithm: Small-Signal Analysis
>
>1. Write the signals $S_1, \dotsc, S_n$ of all [time-variant](../Ports.md#I-V%20Characteristic) components as sums like above:
>
>$$
>\begin{aligned}
>S_1 &= S_{1,Q} + \Delta S_1(t) \\
>&\vdots \\
>S_n &= S_{n, Q} + \Delta S_n(t)
>\end{aligned}
>$$
>
>2. Analyze the [circuit](../../Electronic%20Circuits.md) under the assumption that $\Delta S_1(t), \dotsc, \Delta S_n(t)$ are always zero. The solutions for the [circuit](../../Electronic%20Circuits.md) under this assumption are known as the [circuit](../../Electronic%20Circuits.md)'s **DC inputs**, **DC bias point** or **quiescent point** (**Q point**).
>
>3. Analyze the [circuit](../../Electronic%20Circuits.md) under the assumption that $S_{1,Q}, \dotsc, S_{n, Q}$ are all zero.
>

When we perform [small-signal analysis](./Small-Signal%20Analysis.md) on a [circuit](../../Electronic%20Circuits.md), we get two descriptions of its behavior:
- The [DC bias point](./Small-Signal%20Analysis.md) tells us how the [circuit](../../Electronic%20Circuits.md) would behave when there are no temporal deviations from the constant [signals](./Small-Signal%20Analysis.md) $S_{1,Q}, \dotsc, S_{n, Q}$.
- The second description tells us how the [circuit](../../Electronic%20Circuits.md) reacts to the deviations $S_1(t), \dotsc, S_n(t)$.

>[!TIP]
>
>[Small-signal analysis](./Small-Signal%20Analysis.md) becomes really powerful when combined with [load line analysis](./Load%20Line%20Analysis.md) and [linearization](../One-Ports/Linear%20Resistive%20One-Ports.md#Linearization).
>

>[!EXAMPLE]- Example: Small-Signal Analysis
>
>We want to perform [small-signal analysis](./Small-Signal%20Analysis.md) on the following [circuit](../../Electronic%20Circuits.md):
>
>![Small-Signal Analysis Example](./res/Small-Signal%20Analysis%20Example.svg)
>
>We are given that $R = 100 \mathop{\mathrm{\Omega}}$ and that the [I-V characteristic](../One-Ports/One-Ports.md#I-V%20Characteristic) of the [p-n diode](../../Analog%20Circuits/Diodes/Diodes.md) is
>
>$$
>I(t) = I_S \cdot \exp \left({\frac{V_D(t)}{V_T}}\right) - I_S,
>$$
>
>where $I_s = 10 \mathop{\mathrm{pA}}$ and $V_T = 25 \mathop{\mathrm{mV}}$.
>
>1. We write out the signals of a time-independent and a time-dependent part:
>
>$$
>\begin{aligned}
>V(t) &= V_Q + \Delta V(t) \\ \\
>V_R(t) &= V_{R,Q} + \Delta V_R(t) \\ \\
>V_D(t) &= V_{D, Q} + \Delta V_D(t) \\ \\
>I(t) &= I_Q + \Delta I(t)
>\end{aligned}
>$$
>
>2. We perform [load line analysis](./Load%20Line%20Analysis.md) on the [circuit](../../Electronic%20Circuits.md) under the assumption that $\Delta V(t)$, $\Delta V_R(t)$, $\Delta V_D(t)$ and $\Delta I(t)$ are all zero:
>
>![Small-Signal Analysis Example Bias Point](./res/Small-Signal%20Analysis%20Example%20Bias%20Point.svg)
>
>The [series circuit](../One-Ports/One-Port%20Interconnections.md) of the [Ohmic resistor](../../Analog%20Circuits/Resistors.md) and the [ideal voltage source](../../Analog%20Circuits/Sources.md) is equivalent to a [linear source](../../Analog%20Circuits/Sources.md#Linear%20Sources) whose [I-V characteristic](../One-Ports/One-Ports.md) is
>
>$$
>V' = RI_Q' + V_Q,
>$$
>
>where $I_Q' = -I_Q$ because of the [sign convention](../One-Ports/One-Ports.md). This equivalent [linear source](../../Analog%20Circuits/Sources.md#Linear%20Sources) and the [diode](../../Analog%20Circuits/Diodes/Diodes.md) are connected in [parallel](../One-Ports/One-Port%20Interconnections.md), so we know that $V' = V_{D,Q}$. Then, the [operating points](./Load%20Line%20Analysis.md) must obey the following system of equations:
>
>$$
>\begin{aligned}
>I_Q &= 10 \mathop{\mathrm{pA}} \cdot \exp \left({\frac{V_{D,Q}}{25 \mathop{\mathrm{mV}}}}\right) - 10 \mathop{\mathrm{pA}} \text{ (from the diode's I-V characteristic)} \\ \\
>V_{D, Q} &= -100\mathop{\mathrm{\Omega}} \cdot I_Q + V_Q \text{ (from the source's I-V characteristic)}
>\end{aligned}
>$$
>
>For example, if we were given that $V_Q = 1 \mathop{\mathrm{V}}$ and solved the system, we would obtain the following [operating point](./Load%20Line%20Analysis.md):
>
>$$
>\begin{aligned}
>I_Q &= 10 \mathop{\mathrm{mA}} \\
>V_{D, Q} &= V' = 0.5 \mathop{\mathrm{V}} \\ 
>V_{R, Q} &= -0.5 \mathop{\mathrm{V}}
>\end{aligned}
>$$
>
>3. We analyze the [circuit](../../Electronic%20Circuits.md) under the assumption that $V_Q$, $V_{R,Q}$, $V_{D,Q}$ and $I_Q$ are all zero:
>
>![Small-Signal Analysis Example Time](./res/Small-Signal%20Analysis%20Example%20Time.svg)
>
>We can apply the same method of simplification as we did in step 2 in order to obtain the following system of equations:
>
>$$
>\begin{aligned}
>\Delta I(t) &= 10 \mathop{\mathrm{pA}} \cdot \exp \left({\frac{\Delta V_D(t)}{25 \mathop{\mathrm{mV}}}}\right) - 10 \mathop{\mathrm{pA}} \text{ (from the diode's I-V characteristic)} \\ \\
>\Delta V_D(t) &= -100 \mathop{\mathrm{\Omega}} \cdot \Delta I(t) + \Delta V(t) \text{ (from the source's I-V characteristic)}
>\end{aligned}
>$$
>
>If we were given an expression for $\Delta V(t)$, we would be able to obtain expressions for the other signals as well.
>


