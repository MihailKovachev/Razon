---
title: Gyrators
tags:
    - circuit-theory
    - electrical-engineering
---

# Gyrators

**Gyrators** are [electronic components](../../Electronic%20Circuits.md) which are capable of emulating [duals](../../Network%20Analysis/Lumped%20Elements.md#Duality).

## Theoretical Model

>[!DEFINITION] Definition: Gyrator
>
>A **gyrator** is a [time-invariant](../../Network%20Analysis/Lumped%20Elements.md) [two-port](../../Network%20Analysis/Two-Ports/Two-Ports.md) for which there exists some $R_g \in \mathbb{R}$ or $G_g \in \mathbb{R}$ with the following property:
>
>$$
>\left\vert\begin{aligned}v_1 &= -R_g i_2 \\ v_2 &= R_g i_1\end{aligned}\right. \qquad \text{or} \qquad \left\vert\begin{aligned}i_1 &= G_g v_2 \\ i_2 &= -G_g v_1\end{aligned}\right.
>$$
>
>We call $R_g$ the **gyration resistance** and $G_g$ the **gyration conductance**.
>
>>[!NOTATION]
>>
>>The following symbol is used for the [gyrator](./Gyrators.md):
>>
>>![Gyrator Symbol](../res/Gyrators/Gyrator%20Symbol.svg)
>>
>>The arrow is optional. When it is present, the convention is that it connects the [current](../../Current.md) at its tail to the [voltage](TODO) at its head.
>>
>

>[!THEOREM] Theorem: Strict Linearity
>
>Every [gyrator](#Theoretical%20Model) is [strictly linear](../../Network%20Analysis/Two-Ports/Linear%20Two-Ports.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Reciprocity of $R_g$ and $G_g$
>
>If a [gyrator](#Theoretical%20Model) has both a [gyration resistance](#Theoretical%20Model) $R_g$ and a [gyration conductance](#Theoretical%20Model) $G_g$, then they are reciprocal:
>
>$$
>R_g = \frac{1}{G_g} \qquad G_g = \frac{1}{R_g}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Implicit Representations
>
>If a [gyrator](#Theoretical%20Model) has [gyration resistance](#Theoretical%20Model) $R_g$, then it has the following [implicit representation](../../Network%20Analysis/Ports.md#Representations):
>
>$$
>\begin{bmatrix}1 & 0 \\ 0 & 1\end{bmatrix}\boldsymbol{v} + \begin{bmatrix}0 & R_g \\ -R_g & 0\end{bmatrix}\boldsymbol{i} = \boldsymbol{0}
>$$
>
>If a [gyrator](#Theoretical%20Model) has [gyration conductance](#Theoretical%20Model) $G$, then it has the following [implicit representation](../../Network%20Analysis/Ports.md#Representations):
>
>$$
>\begin{bmatrix}0 & -G_g \\ G_g & 0\end{bmatrix}\boldsymbol{v} + \begin{bmatrix}1 & 0 \\ 0 & 1\end{bmatrix}\boldsymbol{i} = \boldsymbol{0}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Explicit Representations
>
>If a [gyrator](#Theoretical%20Model) has [gyration conductance](#Theoretical%20Model) $G_g$, then it has the following [admittance representation](../../Network%20Analysis/Ports.md#Representations):
>
>$$
>\boldsymbol{i} = \boldsymbol{G}\boldsymbol{v} \qquad \boldsymbol{G} = \begin{bmatrix}0 & G_g \\ -G_g & 0\end{bmatrix}
>$$
>
>If a [gyrator](#Theoretical%20Model) has [gyration resistance](#Theoretical%20Model) $R_g$, then it has the following [impedance representation](../../Network%20Analysis/Ports.md#Representations):
>
>$$
>\boldsymbol{v} = \boldsymbol{R}\boldsymbol{i} \qquad \boldsymbol{R} = \begin{bmatrix}0 & -R_g \\ R_g & 0\end{bmatrix}
>$$
>
>[Gyrators](#Theoretical%20Model) have neither [hybrid representations](../../Network%20Analysis/Ports.md#Representations) nor [inverse hybrid representations](../../Network%20Analysis/Ports.md#Representations).
>
>If a [gyrator](#Theoretical%20Model) has both [gyration conductance](#Theoretical%20Model) $G_g$ and [gyration resistance](#Theoretical%20Model) $R_g$, then it has the following [forwards transmission representation](../../Network%20Analysis/Two-Ports/Two-Ports.md#Representations):
>
>$$
>\begin{bmatrix}v_1 \\ i_1\end{bmatrix} = \boldsymbol{T}\begin{bmatrix}v_2 \\ -i_2\end{bmatrix} \qquad \boldsymbol{T} = \begin{bmatrix}0 & R_g \\ G_g & 0\end{bmatrix}
>$$
>
>If a [gyrator](#Theoretical%20Model) has both [gyration conductance](#Theoretical%20Model) $G_g$ and [gyration resistance](#Theoretical%20Model) $R_g$, then it has the following [backwards transmission representation](../../Network%20Analysis/Two-Ports/Two-Ports.md#Representations):
>
>$$
>\begin{bmatrix}v_2 \\ i_2\end{bmatrix} = \boldsymbol{T}'\begin{bmatrix}v_1 \\ -i_1\end{bmatrix} \qquad \boldsymbol{T}' = \begin{bmatrix}0 & -R_g \\ -G_g & 0\end{bmatrix}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Losslessness of the Gyrator
>
>[Gyrators](#Theoretical%20Model) are [lossless](../../Network%20Analysis/Ports.md#Power).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Positive Immitance Inverter
>
>The [gyrator](./Gyrators.md) is a [positive immitance inverter (PII)](../../Network%20Analysis/Electrical%20Elements/Two-Ports/Impedance%20Inverters.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Dual of the Gyrator
>
>A [gyrator](#Theoretical%20Model) with [gyration resistance](#Theoretical%20Model) is [dual](../../Network%20Analysis/Ports.md#Duality) to a [gyrator](#Theoretical%20Model).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antisymmetry of Gyrators
>
>[Gyrators](./Gyrators.md) are [antisymmetrical](../../Network%20Analysis/Two-Ports/Two-Ports.md#Symmetry).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Gyrator as One-Port Dual Converter
>
>If the [output](../../Network%20Analysis/Two-Ports/Two-Ports.md) of a [gyrator](#Theoretical%20Model) with [gyration resistance](./Gyrators.md) $R_g$ is connected to a [one-port](../../Network%20Analysis/One-Ports/One-Ports.md) $\mathcal{F}$, then its [input](../../Network%20Analysis/Two-Ports/Two-Ports.md) becomes the [dual](../../Network%20Analysis/One-Ports/One-Ports.md#Duality) of $\mathcal{F}$ with [duality constant](../../Network%20Analysis/One-Ports/One-Ports.md#Duality) $R_g$:
>
>![Gyrator as One-Port Dual Converter](../res/Gyrators/Gyrator%20as%20One-Port%20Dual%20Converter.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Gyrator as Two-Port Dual Converter
>
>The [chaining](../../Network%20Analysis/Two-Ports/Two-Port%20Interconnections.md) of a [two-port](../../Network%20Analysis/Two-Ports/Two-Ports.md) $\mathcal{F}$ with [gyrators](./Gyrators.md) with [gyration resistance](./Gyrators.md) $R_g$ on its [input](../../Network%20Analysis/Two-Ports/Two-Ports.md) and [output](../../Network%20Analysis/Two-Ports/Two-Ports.md), results in its [dual](../../Network%20Analysis/Ports.md#Duality) [two-port](../../Network%20Analysis/Two-Ports/Two-Ports.md) $\mathcal{F}^d$ with [duality constant](../../Network%20Analysis/Ports.md#Duality) $R_g$:
>
>![Gyrator as Two-Port Dual Converter](../res/Gyrators/Gyrator%20as%20Two-Port%20Dual%20Converter.svg)
>
>>[!PROOF]-
>>
>>TODO
>>
>