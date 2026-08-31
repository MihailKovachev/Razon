---
tags:
    - analog-circuits
    - electrical-engineering
---

# Resistors

The term **resistor** is a bit misleading because [resistance](../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) is defined for every [electronic component](../Electronic%20Circuits.md). However, it is usually used to mean an [electronic component](../Electronic%20Circuits.md) whose [resistance](../Network%20Analysis/One-Ports/One-Ports.md#Resistance) exhibits one of the following specific behaviors.

## Linear Resistors

A **linear resistor** is an [electronic component](../Electronic%20Circuits.md) whose [voltage](TODO) scales [linearly](../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md) with the [current](../Current.md) flowing through and vice versa.

### Theoretical Model

>[!DEFINITION] Definition: Linear Resistor
>
>A **linear resistor** is a [one-port](../Network%20Analysis/One-Ports/One-Ports.md) whose [static resistance](../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) $R$ and [static conductance](../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) $G$ are [constant](../../Mathematics/Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md):
>
>$$
>V(t) = RI(t) \qquad \text{or} \qquad I(t) = GV(t)
>$$
>
>>[!DEFINITION] Definition: Ohm's Law
>>
>>The above equations are often called **Ohm's law**.
>>
>
>![I-V of Linear Resistor](./res/Resistors/I-V%20of%20Linear%20Resistor.svg)
>
>>[!NOTATION]
>>
>>The following symbols are used for [linear resistors](#Linear%20Resistors):
>>
>>![Linear Resistor Symbols](./res/Resistors/Linear%20Resistor%20Symbols.svg)
>>
>
>>[!DEFINITION] Definition: Ohmic Resistor
>>
>>An **Ohmic resistor** is a [linear resistor](#Linear%20Resistors) such that $R, G \gt 0$.
>>
>


>[!THEOREM] Theorem: Static = Dynamic
>
>[Static resistance](../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) and [dynamic resistance](../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) of a [linear resistor](./Resistors.md) are always the same, as are [static conductance](../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) and [dynamic conductance](../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance).
>
>>[!NOTE]
>>
>>This is why we just speak of "resistance" and "conductance" when talking about [linear resistors](./Resistors.md).
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Strict Linearity of Linear Resistors
>
>All [linear resistors](#Linear%20Resistors) are [strictly linear](../Network%20Analysis/One-Ports/Linear%20Resistive%20One-Ports.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Linear Resistors in Series
>
>If $n$ [linear resistors](#Linear%20Resistors) with [resistances](#Linear%20Resistors) $R_1, \dotsc, R_n$ or [conductances](#Linear%20Resistors) $G_1, \dotsc G_n$ connected in [series](../Network%20Analysis/One-Ports/One-Port%20Interconnections.md), then they are equivalent to a single [linear resistor](#Linear%20Resistors) with [resistance](#Linear%20Resistors) $R$ or [conductance](#Linear%20Resistors) $G$:
>
>$$
>R = \sum_{k=1}^n R_k \qquad \frac{1}{G} = \sum_{k = 1}^n \frac{1}{G_k}
>$$
>
>>[!PROOF]-
>>
>>Since they are connected in [series](./Series%20Circuits.md), they are equivalent to a single [one-port](../Network%20Analysis/One-Ports/One-Ports.md) whose [current](../Current.md) $I$ is the same, but whose [voltage](TODO) $V$ is the sum of the [voltages](TODO) $V_1$ and $V_2$ across the [resistors](#Linear%20Resistors):
>>
>>$$
>>V = V_1 + V_2
>>$$
>>
>>We know that $V_1 = R_1I$ and $V_2 = R_2 I$ and so
>>
>>$$
>>V = R_1 I + R_2 I= (R_1 + R_2)I.
>>$$
>>
>>Therefore, this equivalent [one-port](../../index.md) is an [linear resistor](#Linear%20Resistors) with [resistance](#Linear%20Resistors) $R_1 + R_2$.
>>
>>Similarly, since $I = G_1 V_1$ and $I = G_2 V_2$, we get that $V_1 = \frac{1}{G_1}I$ and $V_2 = \frac{1}{G_2} I$. Therefore,
>>
>>$$
>>V = \frac{1}{G_1}I + \frac{1}{G_2}I = \left(\frac{1}{G_1} + \frac{1}{G_2}\right)I
>>$$
>>
>>$$
>>I = \frac{1}{\frac{1}{G_1} + \frac{1}{G_2}}V
>>$$
>>
>>Therefore, this equivalent [one-port](../../index.md) is an [linear resistor](#Linear%20Resistors) with [conductance](#Linear%20Resistors) $G = \frac{1}{\frac{1}{G_1} + \frac{1}{G_2}}$. By taking the reciprocal of $G$, we obtain the original result:
>>
>>$$
>>\frac{1}{G} = \frac{1}{G_1} + \frac{1}{G_2}
>>$$
>>
>

>[!THEOREM] Theorem: Linear resistors in Parallel
>
>If $n$ [linear resistors](#Linear%20Resistors) with [resistances](../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) $R_1, \dotsc, R_n$ or [conductances](../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) $G_1, \dotsc G_n$ connected in [parallel](../Network%20Analysis/One-Ports/One-Port%20Interconnections.md), then they are equivalent to a single [linear resistor](#Linear%20Resistors) with [resistance](../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) $R$ or [conductance](../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) $G$:
>
>$$
>\frac{1}{R} = \sum_{k=1}^n \frac{1}{R_k} \qquad G = \sum_{k = 1}^n G_k
>$$
>
>>[!PROOF]-
>>
>>Since they are connected in [parallel](../Network%20Analysis/One-Ports/One-Port%20Interconnections.md), they are equivalent to a single [one-port](../Network%20Analysis/One-Ports/One-Ports.md) whose [voltage](TODO) $V$ is the same, but whose [current](../Current.md) $I$ is the sum of the [currents](../Current.md) $I_1$ and $I_2$ flowing through the [resistors](#Linear%20Resistors):
>>
>>$$
>>I = I_1 + I_2
>>$$
>>
>>We know that $I_1 = G_1U$ and $I_2 = G_2 V$ and so
>>
>>$$
>>I = G_1 V + G_2 V = (G_1 + G_2)V.
>>$$
>>
>>Therefore, this equivalent [one-port](../Network%20Analysis/One-Ports/One-Ports.md) is a [linear resistor](#Linear%20Resistors) with [conductance](../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) $G_1 + G_2$.
>>
>>Similarly, since $V = R_1 I_1$ and $V = R_2 I_2$, we get that $I_1 = \frac{1}{R_1}V$ and $I_2 = \frac{1}{R_2} V$. Therefore,
>>
>>$$
>>I = \frac{1}{R_1}V + \frac{1}{R_2}V = \left(\frac{1}{R_1} + \frac{1}{R_2}\right)V
>>$$
>>
>>$$
>>V = \frac{1}{\frac{1}{R_1} + \frac{1}{R_2}}I
>>$$
>>
>>Therefore, this equivalent [one-port](../Network%20Analysis/One-Ports/One-Ports.md) is an [linear resistor](#Linear%20Resistors) with [resistance](../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) $R = \frac{1}{\frac{1}{R_1} + \frac{1}{R_2}}$. By taking the reciprocal of $R$, we obtain the original result:
>>
>>$$
>>\frac{1}{R} = \frac{1}{R_1} + \frac{1}{R_2}
>>$$
>>
>

>[!THEOREM] Theorem: Duality of Linear Resistors
>
>[Linear resistors](#Linear%20Resistors) are [dual](../Network%20Analysis/One-Ports/One-Ports.md#Duality) to [linear resistors](#Linear%20Resistors).
>
>>[!PROOF]-
>>
>>TODO
>>
>

### Implementation

[Ohmic resistors](#Linear%20Resistors) are really easy to create physically because they require nothing more than an [insulating material](TODO).

>[!EXAMPLE] Example: Non-Ohmic Linear Resistor via NIC
>
>A [linear resistor](#Linear%20Resistors) with negative [resistance](../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) / [conductance](../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) can be implemented by connecting an [Ohmic resistor](#Linear%20Resistors) to a [negative immittance converter](./Immittance%20Converters/Negative%20Immittance%20Converters.md):
>
>![Negative Linear Resistor](./res/Resistors/Negative%20Linear%20Resistor.svg)
>

## Piecewise Linear Resistors

**Piecewise linear resistors** are [electronic components](../Electronic%20Circuits.md) which behave like [linear resistors](#Linear%20Resistors) but with different [resistance](../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) / [conductance](../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) depending on the range of the [voltage](TODO) or [current](../Current.md) in which they are operated.

### Theoretical Model

>[!DEFINITION] Definition: Piecewise Linear Resistor
>
>A **piecewise linear resistor** is a [one-port](../Network%20Analysis/One-Ports/One-Ports.md) whose [I-V characteristic](../Network%20Analysis/One-Ports/One-Ports.md) can be represented as
>
>TODO
>

### Concave Resistors

#### Theoretical Model

>[!DEFINITION] Definition: Concave Resistor
>
>A **concave resistor** is a [piecewise linear resistor](#Piecewise%20Linear%20Resistors) whose [I-V characteristic](../Network%20Analysis/One-Ports/One-Ports.md) can be represented as
>
>$$i = \begin{cases}0 & \text{if } v \lt V \\ Gv & \text{if } v \ge V\end{cases}$$
>
>for some $G, V \in \mathbb{R}$.
>
>![I-V Concave Resistor](./res/Resistors/I-V%20Concave%20Resistor.svg)
>
>>[!NOTATION]
>>
>>The following symbol is used for [concave resistors](#Piecewise%20Linear%20Resistors#Concave%20Resistors).
>>
>>![Concave Resistor Symbol](./res/Resistors/Concave%20Resistor%20Symbol.svg)
>>
>

#### Implementation

>[!EXAMPLE] Example: Concave Resistor via Ideal Diode
>
>A [concave resistor](#Piecewise%20Linear%20Resistors#Concave%20Resistors) can be realized using a [series circuit](../Network%20Analysis/One-Ports/One-Port%20Interconnections.md) of an [ideal diode](./Diodes/Ideal%20Diodes.md), a [voltage source](./Sources.md) with constant [voltage](TODO) $V$ and an [Ohmic resistor](#Linear%20Resistors) with [conductance](../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) $G$:
>
>![Concave Resistor Implementation](./res/Resistors/Concave%20Resistor%20Implementation.svg)
>

### Convex Resistors

#### Theoretical Model

>[!DEFINITION] Definition: Convex Resistor
>
>A **convex resistor** is a [piecewise linear resistor](#Piecewise%20Linear%20Resistors) whose [I-V characteristic](../Network%20Analysis/One-Ports/One-Ports.md) can be represented as
>
>$$v = \begin{cases}0 & \text{if } i \lt I \\ Rv & \text{if } i \ge I\end{cases}$$
>
>for some $R, V \in \mathbb{R}$.
>
>![I-V Convex Resistor](./res/Resistors/I-V%20Convex%20Resistor.svg)
>
>>[!NOTATION]
>>
>>The following symbol is used for [convex resistors](#Piecewise%20Linear%20Resistors#Convexx%20Resistors).
>>
>>![Convex Resistor Symbol](./res/Resistors/Convex%20Resistor%20Symbol.svg)
>>
>

#### Implementation

>[!EXAMPLE] Example: Convex Resistor via Ideal Diode
>
>A [convex resistor](#Piecewise%20Linear%20Resistors#Concave%20Resistors) can be realized using a [parallel circuit](../Network%20Analysis/One-Ports/One-Port%20Interconnections.md) of an [ideal diode](./Diodes/Ideal%20Diodes.md), a [current source](./Sources.md) with constant [current](../Current.md) $I$ and an [Ohmic resistor](#Linear%20Resistors) with [resistance](../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) $R$:
>
>![Convex Resistor Implementation](./res/Resistors/Convex%20Resistor%20Implementation.svg)
>