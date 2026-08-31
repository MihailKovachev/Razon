---
tags:
    - analog-circuits
    - electrical-engineering
---

# Negative Immittance Converters

**Negative immittance converters** (**NICs**) are [circuits](../Analog%20Circuits.md) capable of transferring the [voltage](TODO) and [current](../../Current.md) of an [electronic component](../../Electronic%20Circuits.md), whilst reversing the direction of one or the other and potentially scaling them:

- A [negative immittance converter](./Negative%20Immittance%20Converters.md) which reverses the direction of [current](../../Current.md), whilst retaining the direction of [voltage](TODO), is known as a **current inversion negative immittance converter** (**INIC**);
- A [negative immittance converter](./Negative%20Immittance%20Converters.md) which reverses the direction of [voltage](TODO), whilst retaining the direction of [current](../../Current.md), is known as a **voltage inversion negative immittance converter** (**VNIC**).

[Negative immittance converters](./Negative%20Immittance%20Converters.md) are extremely useful because they can be used for many purposes:

- Reversing the [current](../../Current.md) or [voltage](TODO) direction results in the reversal of the sign of the [resistance](../../Network%20Analysis/One-Ports/One-Ports.md#Resistance) / [conductance](../../Network%20Analysis/One-Ports/One-Ports.md#Resistance) (both [static](../../Network%20Analysis/One-Ports/One-Ports.md#Resistance) and [dynamic](../../Network%20Analysis/One-Ports/One-Ports.md#Resistance)) of the [electronic component](../../Electronic%20Circuits.md). This allows us to physically realize [resistors](../Resistors.md) with negative [resistance](../../Network%20Analysis/One-Ports/One-Ports.md#Resistance).

TODO

## Theoretical Model

>[!DEFINITION] Definition: Negative Immittance Converter
>
>A **negative immittance converter** is a [two-port](../../Network%20Analysis/Two-Ports/Two-Ports.md) whose [I-V characteristic](../../Network%20Analysis/Ports.md) is
>
>$$\left\vert\begin{aligned}v_1 &= -k v_2 \\ i_1 &= -\frac{1}{k} i_2 \end{aligned}\right.$$
>
>for some constant $k \in \mathbb{R}_{\ne 0}$ known as the **conversion ratio**.
>

A [negative immittance converter](#Negative%20Immittance%20Converters) is:

- an [INIC](./Negative%20Immittance%20Converters.md) when $k \lt 0$;
- a [VNIC](./Negative%20Immittance%20Converters.md) when $k \gt 0$.

>[!THEOREM] Theorem: Strict Linearity
>
>Every [negative immittance converter](#Negative%20Immittance%20Converters) is [strictly linear](../../Network%20Analysis/Strictly%20Linear%20Multiports.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Implicit Representations
>
>If a [negative immittance converter](#Negative%20Immittance%20Converters) has a [conversion ratio](#Negative%20Immittance%20Converters) $k$, then
>
>$$\begin{bmatrix}1 & k \\ 0 & 0\end{bmatrix}\boldsymbol{v} + \begin{bmatrix}0 & 0 \\ k & 1\end{bmatrix}\boldsymbol{i} = \boldsymbol{0}$$
>
>is an [implicit representation](../../Network%20Analysis/Ports.md#Representations) of it.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Explicit Representations
>
>The [negative immittance converter](#Negative%20Immittance%20Converters) has neither an [admittance representation](../../Network%20Analysis/Ports.md#Representations) nor an [impedance representation](../../Network%20Analysis/Ports.md#Representations).
>
>It has the following [hybrid representation](../../Network%20Analysis/Two-Ports/Two-Ports.md#Representations) and [inverse hybrid representation](../../Network%20Analysis/Two-Ports/Two-Ports.md#Representations):
>
>$$\begin{bmatrix}v_1 \\ i_2\end{bmatrix} = \boldsymbol{H} \begin{bmatrix}i_1 \\ v_2\end{bmatrix} \qquad \boldsymbol{H} = \begin{bmatrix}0 & -k \\ -k & 0\end{bmatrix}$$
>
>$$\begin{bmatrix}i_1 \\ v_2\end{bmatrix} = \boldsymbol{H}' \begin{bmatrix}v_1 \\ i_2\end{bmatrix} \qquad \boldsymbol{H}' = \begin{bmatrix}0 & -\frac{1}{k} \\ -\frac{1}{k} & 0\end{bmatrix}$$
>
>It has the following [forwards transmission representation](../../Network%20Analysis/Two-Ports/Two-Ports.md#Representations) and [backwards transmission representation](../../Network%20Analysis/Two-Ports/Two-Ports.md#Representations):
>
>$$\begin{bmatrix}v_1 \\ i_1\end{bmatrix} = \boldsymbol{T} \begin{bmatrix} v_2 \\ -i_2 \end{bmatrix} \qquad \boldsymbol{T} = \begin{bmatrix}-k & 0 \\ 0 & \frac{1}{k}\end{bmatrix}$$
>
>$$\begin{bmatrix}v_2 \\ i_2\end{bmatrix} = \boldsymbol{T}'\begin{bmatrix}v_1 \\ -i_1\end{bmatrix} \qquad \boldsymbol{T}' = \begin{bmatrix}-\frac{1}{k} & 0 \\ 0 & k\end{bmatrix}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Activity of NICs
>
>[Negative immittance converters](./Negative%20Immittance%20Converters.md) are [active](../../Network%20Analysis/Ports.md#Power).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antireciprocity of NICs
>
>[Negative immittance converter](./Negative%20Immittance%20Converters.md) are always [antireciprocal](../../Network%20Analysis/Two-Ports/Two-Ports.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Symmetry Condition for NICs
>
>A [negative immittance converter](./Negative%20Immittance%20Converters.md) is [symmetrical](../../Network%20Analysis/Two-Ports/Two-Ports.md#Symmetry) if and only if $|k| = 1$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Implementation

>[!EXAMPLE] Example: INIC from Nullor
>
>A [INIC](./Negative%20Immittance%20Converters.md) can be constructed using a [nullor](../../Network%20Analysis/Two-Ports/Nullors.md) and two identical [Ohmic resistors](../Resistors.md):
>
>![INIC from Nullor](./res/INIC%20from%20Nullor.svg)
>
>The [voltage](TODO) across the [nullator](../Nullators.md) is zero and so [Kirchhoff's voltage law](../../Network%20Analysis/Lumped%20Circuits.md) gives us the following:
>
>$$v_1 = v_2$$
>
>Similarly, applying [Kirchhoff's voltage law](../../Network%20Analysis/Lumped%20Circuits.md) to the [nullator](../Nullators.md) and the two [Ohmic resistors](../Resistors.md), we get that $R i_1 = R i_2$. We therefore have:
>
>$$i_1 = i_2$$
>
>We have obtained the equations of a [negative immittance converter](#Negative%20Immittance%20Converters)
>
>$$\left\vert\begin{aligned}v_1 &= -k v_2 \\ i_1 &= -\frac{1}{k} i_2 \end{aligned}\right.$$
>
>with $k = -1$.
>
>TODO FIX
>

>[!EXAMPLE] Example: VNIC from Nullor
>
>A [VNIC](./Negative%20Immittance%20Converters.md) be constructed using a [nullor](../../Network%20Analysis/Two-Ports/Nullors.md) and two identical [Ohmic resistors](../Resistors.md):
>
>![VNIC from Nullor](./res/VNIC%20from%20Nullor.svg)
>
>The [voltage](TODO) across the [nullator](../Nullators.md) is zero and so [Kirchhoff's voltage law](../../Network%20Analysis/Lumped%20Circuits.md) gives us the following:
>
>$$v_1 = -v_2$$
>
>Similarly, there is no [current](../../Current.md) flowing through the [nullator](../Nullators.md) and so the two [Ohmic resistors](../Resistors.md) and the [norator](../Norators.md) form a [parallel circuit](../../Network%20Analysis/One-Ports/One-Port%20Interconnections.md). This immediately makes them a [one-port](../../Network%20Analysis/One-Ports/One-Ports.md) and we get the following:
>
>$$i_2 = -i_1$$
>
>We therefore obtain the equations of a [negative immittance converter](#Negative%20Immittance%20Converters)
>$$
>\left\vert\begin{aligned}v_1 &= -k v_2 \\ i_1 &= -\frac{1}{k} i_2 \end{aligned}\right.$$
>
>with $k = +1$.
>
>TODO FIX
>

>[!EXAMPLE] Example: NIC from Op-Amp
>
>A [negative immittance converter](#Negative%20Immittance%20Converter) can be constructed using an [ideal operational amplifier](../Amplifiers/Operational%20Amplifiers.md) and [Ohmic resistors](../Resistors.md):
>
>![NIC from Ideal Op-Amp](./res/NIC%20from%20Ideal%20Op-Amp.svg)
>
>As long as the [ideal op-amp](../Amplifiers/Operational%20Amplifiers.md) is operated in its [linear region](../Amplifiers/Differential%20Voltage%20Amplifiers.md), the above circuit behaves like a [negative immittance converter](#Negative%20Immittance%20Converter) with $k = -1$.
>
>To ensure that the [ideal op-amp](../Amplifiers/Operational%20Amplifiers.md) is indeed operated in its [linear region](../Amplifiers/Differential%20Voltage%20Amplifiers.md), we need to have $v_1 - R i_1 \in [-V_{\text{sat}}; +V_{\text{sat}}]$.
>
>We can see this by analyzing the [network](../../Network%20Analysis/Lumped%20Elements.md).
>
>**Linear region:**
>
>When the [ideal op-amp](../Amplifiers/Operational%20Amplifiers.md) is operated in its [linear region](../Amplifiers/Differential%20Voltage%20Amplifiers.md), we know that it is equivalent to a [nullor](../../Network%20Analysis/Two-Ports/Nullors.md). In this case, it would be connected in such a way so as to act as a [NIC](#Negative%20Immittance%20Converters) with $k = -1$
>
>**Saturation regions:**
>
>When the [ideal op-amp](../Amplifiers/Operational%20Amplifiers.md) is operated outside its [linear region](../Amplifiers/Differential%20Voltage%20Amplifiers.md), we know that $v_d \ne 0$. The differential voltage is given by $v_d = v_+ - v_- = v_2 - v_1$.
>
>According to [Kirchhoff's voltage law](../../Network%20Analysis/Lumped%20Circuits.md), the relationships between the port voltages and currents still hold:
>
>$$\left\vert\begin{aligned}v_1 &= v_{\text{out}} + R i_1 \\ v_2 &= v_{\text{out}} + R i_2\end{aligned}\right.$$
>
>By substituting these into the expression for $v_d$, we can determine the saturation conditions based on the currents:
>
>$$v_d = (v_{\text{out}} + R i_2) - (v_{\text{out}} + R i_1) = R(i_2 - i_1)$$
>
>When the [ideal op-amp](../Amplifiers/Operational%20Amplifiers.md) is operated in its [negative saturation region](../Amplifiers/Differential%20Voltage%20Amplifiers.md), we have $v_d \lt 0$ and $v_{\text{out}} = -V_{\text{sat}}$:
>
>$$R(i_2 - i_1) \lt 0 \implies i_2 \lt i_1$$
>
>In this state, the voltage at port 1 is clamped relative to the current:
>
>$$v_1 = -V_{\text{sat}} + R i_1$$
>
>By contrast, when the [ideal op-amp](../Amplifiers/Operational%20Amplifiers.md) is operated in its [positive saturation region](../Amplifiers/Differential%20Voltage%20Amplifiers.md), we have $v_d \gt 0$ and $v_{\text{out}} = +V_{\text{sat}}$:
>
>$$R(i_2 - i_1) \gt 0 \implies i_2 \gt i_1$$
>
>In this state, the voltage at port 1 is clamped as follows:
>
>$$v_1 = +V_{\text{sat}} + R i_1$$
>