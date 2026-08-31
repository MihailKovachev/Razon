---
tags:
    - analog-circuits
    - electrical-engineering
---

# Voltage Followers

>[!DEFINITION] Definition: Voltage Follower
>
>A **voltage follower** is a [differential voltage amplifier](./Differential%20Voltage%20Amplifiers.md) whose [voltage gain](./Differential%20Voltage%20Amplifiers.md) $A$ is $1$:
>
>$$
>A = 1
>$$
>

>[!EXAMPLE] Example: Voltage Follower
>
>A [voltage follower](#Voltage%20Followers) can be constructed using an [ideal operational amplifier](./Operational%20Amplifiers.md) by connecting the output directly to the inverting input:
>
>![Voltage Follower via Op-Amp](./res/Voltage%20Follower%20via%20Op-Amp.svg)
>
>As long as the [ideal op-amp](./Operational%20Amplifiers.md) is operated in its [linear region](#Voltage%20Followers), the above circuit behaves like a [voltage follower](#Voltage%20Followers) with the following [voltage gain](#Differential%20Voltage%20Amplifiers):
>
>$$
>A = \frac{v_{\text{out}}}{v_{\text{in}}} = 1
>$$
>
>To ensure that the [ideal op-amp](./Operational%20Amplifiers.md) is indeed operated in its [linear region](#Voltage%20Followers), we need to have $v_{\text{in}} \in \left[-V_{\text{sat}}; +V_{\text{sat}}\right]$. Moreover, the resulting [voltage follower](./Voltage%20Followers.md) is itself an [operational amplifier](./Operational%20Amplifiers.md), since $i_{-} = i_{+} = 0$.
>
>We can see this by analyzing the [network](../../Network%20Analysis/Lumped%20Elements.md).
>
>**Linear region:**
>
>When the [ideal op-amp](./Operational%20Amplifiers.md) is operated in its [linear region](#Voltage%20Followers), we know that $v_d = 0$, i.e. $v_{-} = v_{+}$.
>
>From the circuit diagram, the input and output voltages are connected to the amplifier terminals as follows:
>
>$$
>\left\vert\begin{aligned}v_{+} &= v_{\text{in}} \\ v_{-} &= v_{\text{out}}\end{aligned}\right.
>$$
>
>Since $v_{-} = v_{+}$, we can equate the two expressions to obtain the following:
>
>$$
>v_{\text{out}} = v_{\text{in}} \implies \frac{v_{\text{out}}}{v_{\text{in}}} = 1
>$$
>
>**Saturation regions:**
>
>When the [ideal op-amp](./Operational%20Amplifiers.md) is operated outside its [linear region](#Voltage%20Followers), we know that $v_d \ne 0$.
>
>By definition of the differential voltage, we have the following expression for $v_d$:
>
>$$
>v_d = v_{+} - v_{-}
>$$
>
>Substituting the connections from the [network](../../Network%20Analysis/Lumped%20Elements.md) ($v_{+} = v_{\text{in}}$ and $v_{-} = v_{\text{out}}$), we obtain:
>
>$$
>v_d = v_{\text{in}} - v_{\text{out}}
>$$
>
>When the [ideal op-amp](./Operational%20Amplifiers.md) is operated in its [negative saturation region](./Differential%20Voltage%20Amplifiers.md), we have $v_d \lt 0$ and $v_{\text{out}} = -V_{\text{sat}}$:
>
>$$
>v_d = v_{\text{in}} - (-V_{\text{sat}}) = v_{\text{in}} + V_{\text{sat}} \lt 0
>$$
>
>By performing some equivalent transformations, we get the following:
>
>$$
>v_{\text{in}} \lt -V_{\text{sat}}
>$$
>
>Therefore, we know that the [ideal op-amp](./Operational%20Amplifiers.md) is operated in its [negative saturation region](./Differential%20Voltage%20Amplifiers.md) whenever $v_{\text{in}} \lt -V_{\text{sat}}$.
>
>By contrast, when the [ideal op-amp](./Operational%20Amplifiers.md) is operated in its [positive saturation region](./Differential%20Voltage%20Amplifiers.md), we have $v_d \gt 0$ and $v_{\text{out}} = +V_{\text{sat}}$:
>
>$$
>v_d = v_{\text{in}} - V_{\text{sat}} \gt 0
>$$
>
>By performing some equivalent transformations, we get the following:
>
>$$
>v_{\text{in}} \gt +V_{\text{sat}}
>$$
>
>Therefore, we know that the [ideal op-amp](./Operational%20Amplifiers.md) is operated in its [positive saturation region](./Differential%20Voltage%20Amplifiers.md) whenever $v_{\text{in}} \gt +V_{\text{sat}}$.
>
