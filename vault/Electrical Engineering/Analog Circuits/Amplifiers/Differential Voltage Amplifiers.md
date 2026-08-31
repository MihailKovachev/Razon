---
tags:
    - analog-circuits
    - electrical-engineering
---

# Differential Voltage Amplifiers

>[!DEFINITION] Definition: Finite-Gain Differential Voltage Amplifier
>
>A **finite-gain differential voltage amplifier** is a $5$[-terminal network](../../Network%20Analysis/Lumped%20Elements.md)$\mathcal{A}$ consisting of the following:
>
>    - an **inverting input terminal** ($-$) whose [voltage](TODO) is $v_{-}$ and whose [in-flowing](../../Network%20Analysis/Reference%20Directions.md) [current](../../Current.md) is $i_{-}$;
>    - a **non-inverting input terminal** ($+$) whose [voltage](TODO) is $v_{+}$ and whose [in-flowing](../../Network%20Analysis/Reference%20Directions.md) [current](../../Current.md) is $i_{+}$;
>    - an **output terminal** ($\text{out}$) whose [voltage](TODO) is $v_{\text{out}}$ and whose [in-flowing](../../Network%20Analysis/Reference%20Directions.md) [current](../../Current.md) is $i_{\text{out}}$;
>    - a **negative power supply terminal** ($EE$) whose [voltage](TODO) is $-v_{\text{EE}}$;
>    - a **positive power supply terminal** ($CC$) whose [voltage](TODO) is $+v_{\text{CC}}$.
>
>>[!DEFINITION] Definition: Differential Voltage
>>
>>We call $v_d \overset{\text{def}}{=} v_{+} - v_{-}$ the **differential voltage**.
>>
>
>>[!DEFINITION] Definition: Saturation Voltages
>>
>>We call $-v_{EE}$ the **negative saturation voltage** and $+v_{CC}$ the **positive saturation voltage**.
>>
>
>The [voltage](TODO) $v_{\text{out}}$ is given as
>
>$$v_{\text{out}} = \begin{cases} -v_{EE} & \text{if } A v_d \in (-\infty; -v_{EE}) & \text{(negative saturation region)} \\ A v_d & \text{if } A v_d \in [-v_{EE};v_{CC}] & \text{(linear region)} \\ +v_{CC} & \text{if } A v_d \in (+v_{CC};+\infty) & \text{(positive saturation region)}\end{cases}$$
>
>for some constant $A \in \mathbb{R}$.
>
>>[!DEFINITION] Definition: Voltage Gain
>>
>>The constant $A$ is known as the **voltage gain**.
>>
>
>>[!NOTATION]
>>
>>The symbol for a [differential voltage amplifier with finite saturation](./Differential%20Voltage%20Amplifiers.md) is the following:
>>
>>![Finite-Gain DVA Symbol](./res/Finite-Gain%20DVA%20Symbol.svg)
>>
>


The [saturation voltages](./Differential%20Voltage%20Amplifiers.md) model the fact that amplification requires energy and so [differential voltage amplifiers](./Differential%20Voltage%20Amplifiers.md) cannot amplify beyond certain limits imposed by the energy restrictions.

Physical [differential voltage amplifiers](./Differential%20Voltage%20Amplifiers.md) operated in their [linear region](./Differential%20Voltage%20Amplifiers.md) can have huge [voltage gains](./Differential%20Voltage%20Amplifiers.md), on the order of $10^5$. Moreover, their [differential voltage](./Differential%20Voltage%20Amplifiers.md) is typically very small, so we can essentially model the [voltage gain](./Differential%20Voltage%20Amplifiers.md) as being infinite in comparison.

>[!DEFINITION] Definition: Infinite-Gain Differential Voltage Amplifier
>
>An **infinite-gain differential voltage amplifier** is a $5$[-terminal network](../../Network%20Analysis/Lumped%20Elements.md)$\mathcal{A}$ consisting of the following:
>
>    - an **inverting input terminal** ($-$) whose [voltage](TODO) is $v_{-}$ and whose [in-flowing](../../Network%20Analysis/Reference%20Directions.md) [current](../../Current.md) is $i_{-}$;
>    - a **non-inverting input terminal** ($+$) whose [voltage](TODO) is $v_{+}$ and whose [in-flowing](../../Network%20Analysis/Reference%20Directions.md) [current](../../Current.md) is $i_{+}$;
>    - an **output terminal** ($\text{out}$) whose [voltage](TODO) is $v_{\text{out}}$ and whose [in-flowing](../../Network%20Analysis/Reference%20Directions.md) [current](../../Current.md) is $i_{\text{out}}$;
>    - a **negative power supply terminal** ($EE$) whose [voltage](TODO) is $-v_{\text{EE}}$;
>    - a **positive power supply terminal** ($CC$) whose [voltage](TODO) is $+v_{\text{CC}}$.
>
>>[!DEFINITION] Definition: Differential Voltage
>>
>>We call $v_d \overset{\text{def}}{=} v_{+} - v_{-}$ the **differential voltage**.
>>
>
>>[!DEFINITION] Definition: Saturation Voltages
>>
>>We call $-v_{EE}$ the **negative saturation voltage** and $+v_{CC}$ the **positive saturation voltage**.
>>
>
>The **transfer characteristic** is what characterizes $v_{\text{out}}$ in terms of $v_d$:
>
>$$\left\vert \begin{aligned} v_{\text{out}} &= -v_{\text{EE}} & \text{if } v_d \lt 0 & \qquad \text{(negative saturation region)} \\ v_{\text{out}} &\in [-v_{\text{EE}}; +v_{\text{CC}}] & \text{if } v_d = 0 & \qquad \text{(linear region)} \\ v_{\text{out}} &= +v_{\text{CC}} & \text{if } v_d \gt 0 & \qquad \text{(positive saturation region)} \end{aligned}\right.$$
>
>>[!NOTATION]
>>
>>The following symbol is used for [infinite-gain differential voltage amplifiers](#Differential%20Voltage%20Amplifiers):
>>
>>![Infinite-Gain DVA Symbol](./res/Infinite-Gain%20DVA%20Symbol.svg)
>>
>

The graph of the [transfer characteristic](#Differential%20Voltage%20Amplifiers) for an [infinite-gain differential voltage amplifier](#Differential%20Voltage%20Amplifiers) looks like the following:

![Infinite-Gain DVA Transfer Characteristic](./res/Infinite-Gain%20DVA%20Transfer%20Characteristic.svg)

## Four-Terminal DVAs

In practice, the [saturation voltages](./Differential%20Voltage%20Amplifiers.md) of a [DVA](./Differential%20Voltage%20Amplifiers.md) are constant and usually equal but opposite in sign, i.e. $v_{EE} = v_{CC} = V_{\text{sat}}$. We can model this by connecting the [power supply terminals](./Differential%20Voltage%20Amplifiers.md) to  [time-invariant](../../Network%20Analysis/Ports.md#I-V%20Characteristic) [ideal voltage sources](../Sources.md):

![DVA Connected Power Rails](./res/DVA%20Connected%20Power%20Rails.svg)

When this is the case, all the [voltages](TODO) are given with reference to the common connection point of these [ideal voltage sources](../Sources.md).

>[!NOTATION] Notation: Four-Terminal DVAs
>
>The above configurations are denoted by the following symbols:
>
>![Four-Terminal DVA Symbols](./res/Four-Terminal%20DVA%20Symbols.svg)
>

## Non-Inverting Differential Voltage Amplifiers

>[!DEFINITION] Definition: Non-Inverting Differential Voltage Amplifier
>
>A [differential voltage amplifier](./Differential%20Voltage%20Amplifiers.md) is **non-inverting** if its [voltage gain](./Differential%20Voltage%20Amplifiers.md) $A$ is positive:
>
>$$A \gt 0$$
>

>[!EXAMPLE] Example: Non-Inverting Differential Voltage Amplifier via Op-Amp
>
>A [non-inverting differential voltage amplifier](#Non-Inverting%20Differential%20Voltage%20Amplifiers) can be constructed using an [ideal operational amplifier](./Operational%20Amplifiers.md) and [Ohmic resistors](../Resistors.md):
>
>![Non-Inverting DVA via Op-Amp](./res/Non-Inverting%20DVA%20via%20Op-Amp.svg)
>
>As long as the [ideal op-amp](./Operational%20Amplifiers.md) is operated in its [linear region](#Non-Inverting%20Differential%20Voltage%20Amplifiers), the above circuit behaves like a [non-inverting differential voltage amplifier](#Non-Inverting%20Differential%20Voltage%20Amplifiers) with the following [voltage gain](#Differential%20Voltage%20Amplifiers):
>
>$$A = \frac{v_{\text{out}}}{v_{\text{in}}} = 1 + \frac{R_0}{R_1}$$
>
>To ensure that the [ideal op-amp](./Operational%20Amplifiers.md) is indeed operated in its [linear region](#Non-Inverting%20Differential%20Voltage%20Amplifiers), we need to have $v_{\text{in}} \in \left[-\frac{R_1}{R_0 + R_1}V_{\text{sat}}; +\frac{R_1}{R_0 + R_1}V_{\text{sat}}\right]$.
>
>![Non-Inverting DVA Example Graph](./res/Non-Inverting%20DVA%20Example%20Graph.svg)
>
>We can see this by analyzing the [network](../../Network%20Analysis/Lumped%20Elements.md).
>
>**Linear region:**
>
>When the [ideal op-amp](./Operational%20Amplifiers.md) is operated in its [linear region](#Non-Inverting%20Differential%20Voltage%20Amplifiers), we know that $v_d = 0$, i.e. $v_{-} = v_{+}$.
>
>According to [Kirchhoff's voltage law](../../Network%20Analysis/Lumped%20Circuits.md), noting that $v_{+} = v_{\text{in}}$, we have the following:
>
>$$\left\vert\begin{aligned}v_{\text{in}} &= R_1 i_1 \\ v_{\text{out}} &= R_1 i_1 + R_0 i_0\end{aligned}\right.$$
>
>However, $i_{-}$ is zero, since we have an [ideal operational amplifier](./Operational%20Amplifiers.md). Therefore, [Kirchhoff's current law](../../Network%20Analysis/Lumped%20Circuits.md) tells us that $i_0 = i_1$. Substituting this into the second equation and taking the ratio of the two equations, we obtain the following:
>
>$$\frac{v_{\text{out}}}{v_{\text{in}}} = \frac{R_1 i_1 + R_0 i_1}{R_1 i_1} = \frac{(R_1 + R_0) i_1}{R_1 i_1} = 1 + \frac{R_0}{R_1}$$
>
>**Saturation regions:**
>
>When the [ideal op-amp](./Operational%20Amplifiers.md) is operated outside its [linear region](#Non-Inverting%20Differential%20Voltage%20Amplifiers), we know that $v_d \ne 0$. Recall that $v_d = v_{+} - v_{-}$.
>
>According to [Kirchhoff's voltage law](../../Network%20Analysis/Lumped%20Circuits.md), and given $v_{+} = v_{\text{in}}$, we have the following:
>
>$$\left\vert\begin{aligned}v_{\text{in}} &= R_1 i_1 + v_d \\ v_{\text{out}} &= R_1 i_1 + R_0 i_0\end{aligned}\right.$$
>
>Rearranging the first equation, we get an expression for $i_1$:
>
>$$i_1 = \frac{1}{R_1}(v_{\text{in}}-v_d)$$
>
>However, $i_{-}$ is zero, since we have an [ideal operational amplifier](./Operational%20Amplifiers.md). Therefore, [Kirchhoff's current law](../../Network%20Analysis/Lumped%20Circuits.md) tells us that $i_0 = i_1$. We can thus substitute the above expression into the second equation:
>
>$$v_{\text{out}} = (R_1 + R_0)i_1 = \left(1 + \frac{R_0}{R_1}\right)(v_{\text{in}}-v_d)$$
>
>By performing some simple algebraic manipulations, we can obtain an expression for $v_d$:
>
>$$v_d = v_{\text{in}} - \frac{R_1}{R_1 + R_0}v_{\text{out}}$$
>
>When the [ideal op-amp](./Operational%20Amplifiers.md) is operated in its [negative saturation region](./Differential%20Voltage%20Amplifiers.md), we have $v_d \lt 0$ and $v_{\text{out}} = -V_{\text{sat}}$:
>
>$$v_d = v_{\text{in}} - \frac{R_1}{R_1 + R_0}(-V_{\text{sat}}) \lt 0$$
>
>By performing some equivalent transformations, we get the following:
>
>$$v_{\text{in}} \lt -\frac{R_1}{R_1 + R_0} V_{\text{sat}}$$
>
>Therefore, we know that the [ideal op-amp](./Operational%20Amplifiers.md) is operated in its [negative saturation region](./Differential%20Voltage%20Amplifiers.md) whenever $v_{\text{in}} \lt -\frac{R_1}{R_1 + R_0} V_{\text{sat}}$.
>
>By contrast, when the [ideal op-amp](./Operational%20Amplifiers.md) is operated in its [positive saturation region](./Differential%20Voltage%20Amplifiers.md), we have $v_d \gt 0$ and $v_{\text{out}} = +V_{\text{sat}}$:
>
>$$v_d = v_{\text{in}} - \frac{R_1}{R_1 + R_0}(V_{\text{sat}}) \gt 0$$
>
>By performing some equivalent transformations, we get the following:
>
>$$v_{\text{in}} \gt \frac{R_1}{R_1 + R_0} V_{\text{sat}}$$
>
>Therefore, we know that the [ideal op-amp](./Operational%20Amplifiers.md) is operated in its [positive saturation region](./Differential%20Voltage%20Amplifiers.md) whenever $v_{\text{in}} \gt \frac{R_1}{R_1 + R_0} V_{\text{sat}}$.

## Inverting Differential Voltage Amplifiers

>[!DEFINITION] Definition: Non-Inverting Differential Voltage Amplifier
>
>A [differential voltage amplifier](./Differential%20Voltage%20Amplifiers.md) is **inverting** if its [voltage gain](./Differential%20Voltage%20Amplifiers.md) $A$ is negative:
>
>$$A \lt 0$$
>

>[!EXAMPLE] Example: Inverting Differential Voltage Amplifier
>
>An [inverting differential voltage amplifier](#Inverting%20Differential%20Voltage%20Amplifiers) can be constructed using an [ideal operational amplifier](./Operational%20Amplifiers.md) and [Ohmic resistors](../Resistors.md):
>
>![Inverting DVA via Op-Amp](./res/Inverting%20DVA%20via%20Op-Amp.svg)
>
>As long as the [ideal op-amp](./Operational%20Amplifiers.md) is operated in its  [linear region](#Inverting%20Differential%20Voltage%20Amplifiers), the above circuit behaves like an [inverting differential voltage amplifier](#Inverting%20Differential%20Voltage%20Amplifiers) with the following [voltage gain](#Differential%20Voltage%20Amplifiers):
>
>$$A = \frac{v_{\text{out}}}{v_{\text{in}}} =  -\frac{R_0}{R_1}$$
>
>To ensure that the [ideal op-amp](./Operational%20Amplifiers.md) is indeed operated in its [linear region](#Inverting%20Differential%20Voltage%20Amplifiers), we need to have $v_{\text{in}} \in \left[-\frac{R_1}{R_0}V_{\text{sat}}; +\frac{R_1}{R_0}V_{\text{sat}}\right]$.
>
>![Inverting DVA Example Graph](./res/Inverting%20DVA%20Example%20Graph.svg)
>
>We can see this by analyzing the [network](../../Network%20Analysis/Lumped%20Elements.md).
>
>**Linear region:**
>
>When the [ideal op-amp](./Operational%20Amplifiers.md) is operated in its [linear region](#Inverting%20Differential%20Voltage%20Amplifiers), we know that $v_d = 0$, i.e. $v_{-} = v_{+}$.
>
>According to [Kirchhoff's voltage law](../../Network%20Analysis/Lumped%20Circuits.md), we have the following:
>
>$$\left\vert\begin{aligned}v_{\text{in}} &= R_1 i_1 \\ v_{\text{out}} &= -R_0 i_0\end{aligned}\right.$$
>
>However, $i_{-}$ is zero, since we have an [ideal operational amplifier](./Operational%20Amplifiers.md). Therefore, [Kirchhoff's current law](../../Network%20Analysis/Lumped%20Circuits.md) tells us that $i_0 = i_1$. Taking the ratio of the two previous equations, we obtain the following:
>
>$$\frac{v_{\text{out}}}{v_{\text{in}}} = \frac{R_1 i_1}{-R_0 i_0} = -\frac{R_1 i_1}{R_0 i_1} = -\frac{R_1}{R_0}$$
>
>**Saturation regions:**
>
>When the [ideal op-amp](./Operational%20Amplifiers.md) is operated outside its [linear region](#Inverting%20Differential%20Voltage%20Amplifiers), we know that $v_d \ne 0$.
>
>According to [Kirchhoff's voltage law](../../Network%20Analysis/Lumped%20Circuits.md), we have the following:
>
>$$\left\vert\begin{aligned}v_{\text{in}} &= R_1 i_1 - v_d \\ v_{\text{out}} &= -v_d -R_0 i_0\end{aligned}\right.$$
>
>Rearranging the first equation, we get an expression for $i_1$:
>
>$$i_1 = \frac{1}{R_1}(v_{\text{in}}+v_d)$$
>
>However, $i_{-}$ is zero, since we have an [ideal operational amplifier](./Operational%20Amplifiers.md). Therefore, [Kirchhoff's current law](../../Network%20Analysis/Lumped%20Circuits.md) tells us that $i_0 = i_1$. We can thus substitute the above expression into the second equation:
>
>$$v_{\text{out}} = -v_d - \frac{R_0}{R_1}(v_{\text{in}}+v_d)$$
>
>By performing some simple algebraic manipulations, we can obtain an expression for $v_d$:
>
>$$v_d = -\frac{1}{R_1 + R_0}\left(R_1 v_{\text{out}} + R_0 v_{\text{in}}\right)$$
>
>When the [ideal op-amp](./Operational%20Amplifiers.md) is operated in its [negative saturation region](./Differential%20Voltage%20Amplifiers.md), we have $v_d \lt 0$ and $v_{\text{out}} = -V_{\text{sat}}$:
>
>$$v_d = -\frac{1}{R_1 + R_0}\left(-R_1 V_{\text{sat}} + R_0 v_{\text{in}}\right) \lt 0$$
>
>By performing some equivalent transformations, we get the following:
>
>$$v_{\text{in}} \gt \frac{R_1}{R_0} V_{\text{sat}}$$
>
>Therefore, we know that the [ideal op-amp](./Operational%20Amplifiers.md) is operated in its [negative saturation region](./Differential%20Voltage%20Amplifiers.md) whenever $v_{\text{in}} \gt \frac{R_1}{R_0} V_{\text{sat}}$.
>
>By contrast, when the [ideal op-amp](./Operational%20Amplifiers.md) is operated in its [positive saturation region](./Differential%20Voltage%20Amplifiers.md), we have $v_d \lt 0$ and $v_{\text{out}} = +V_{\text{sat}}$:
>
>$$v_d = -\frac{1}{R_1 + R_0}\left(R_1 V_{\text{sat}} + R_0 v_{\text{in}}\right) \gt 0$$
>
>By performing some equivalent transformations, we get the following:
>
>$$v_{\text{in}} \lt -\frac{R_1}{R_0} V_{\text{sat}}$$
>
>Therefore, we know that the [ideal op-amp](./Operational%20Amplifiers.md) is operated in its [positive saturation region](./Differential%20Voltage%20Amplifiers.md) whenever $v_{\text{in}} \lt -\frac{R_1}{R_0} V_{\text{sat}}$.
>
