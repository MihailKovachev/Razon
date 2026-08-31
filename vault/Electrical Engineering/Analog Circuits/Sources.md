---
tags:
    - analog-circuits
    - electrical-engineering
---

# Sources

**Sources** are the [electronic components](../Electronic%20Circuits.md) which can supply [electronic circuits](../Electronic%20Circuits.md) with [power](TODO) that can be used to perform something useful. 

## Theoretical Model

>[!DEFINITION] Definition: Source
>
>A **source** is an [active](../Network%20Analysis/One-Ports/One-Ports.md#Power) [one-port](../Network%20Analysis/One-Ports/One-Ports.md).
>

This is a very general definition but it is very much true because any [active](../Network%20Analysis/One-Ports/One-Ports.md#Power) [one-port](../Network%20Analysis/One-Ports/One-Ports.md) can, by definition, be operated at a [current](../Current.md) and [voltage](TODO) which produce negative [power](TODO), i.e. they feed [energy](TODO) *into* the [network](../Network%20Analysis/Lumped%20Elements.md). However, we are usually interested in [one-ports](../Network%20Analysis/One-Ports/One-Ports.md) which can do this in specific ways.

### Ideal Current Sources

>[!DEFINITION] Definition: Ideal Current Source
>
>An **ideal current source** is a [one-port](../Network%20Analysis/One-Ports/One-Ports.md) whose [I-V characteristic](../Network%20Analysis/One-Ports/One-Ports.md#I-V%20Characteristics) $\mathcal{F}(t)$ at each time $t$ is given by
>
>$$
>\mathcal{F}(t) = \{(i, v): v \in \mathbb{R}, i = I(t)\},
>$$
>
>where $I$ is some [function](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) which is completely independent of all external factors as well as the [voltage](TODO) $v$.
>
>>[!NOTATION]
>>
>>The following symbol is used for [ideal current sources](#Ideal%20Current%20Sources):
>>
>>![Ideal Current Source Symbol 1](./res/Sources/Ideal%20Current%20Source%20Symbol%201.svg)
>>
>

An [ideal current source](#Ideal%20Current%20Sources) is an [independent](../Network%20Analysis/Lumped%20Elements.md) [source](./Sources.md) whose [current](../Current.md) $i$ is given by some [function](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) $I(t)$ at each moment $t$, regardless of everything else, including the [voltage](TODO) across it. This essentially means that at time $t$, the [ideal current source](#Ideal%20Current%20Sources) is injecting [current](../Current.md) $I(t)$, regardless of anything else that might be happening. 

In general, the graph of the [current](../Current.md) $i$ with respect to time might look like the following:

![Current-Time of Current Source](./res/Sources/Current-Time%20of%20Current%20Source.svg)

However, at each time $t$, the [I-V characteristic](../Network%20Analysis/One-Ports/One-Ports.md#I-V%20Characteristic) looks like some horizontal line because the [current](../Current.md) $i$ of the [ideal current source](#Ideal%20Current%20Sources) is independent of the [voltage](TODO) across it:

![I-V of Ideal Current Source](./res/Sources/I-V%20of%20Ideal%20Current%20Source.svg)

Depending on what the [function](../../Mathematics/Analysis/Functions/Functions.md) $I(t)$ is, we also define two special types of [ideal current sources](#Ideal%20Current%20Sources):

>[!DEFINITION] Definition: Direct Current Source
>
>A **direct current source** (**DC source**) is an [ideal current source](#Ideal%20Current%20Sources) for which $I(t) = I_{\text{DC}}$ for some constant $I_{\text{DC}} \in \mathbb{R}$, i.e. the [current](../Current.md) $i$ is always equal to $I_{\text{DC}}$ at all moments $t$:
>
>$$
>i = I(t) = I_{\text{DC}}
>$$
>
>>[!NOTATION]
>>
>>We denote [DC sources](#Ideal%20Current%20Sources) in one of the following ways:
>>
>>![DC Source Symbols](./res/Sources/DC%20Source%20Symbols.svg)
>>
>

>[!DEFINITION] Definition: Alternating Current Source
>
>An **alternating current source** (**AC source**) is an [ideal current source](#Ideal%20Current%20Sources) for which $I(t)$ satisfies the following conditions:
>- It is [periodic](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Periodicity.md) for some [period](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Periodicity.md) $T \in \mathbb{R}$.
>- The [integral](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md) $\int_{t_0}^{t_0 + T} I(t) \mathop{\mathrm{d}t}$ is zero for all $t_0 \in \mathbb{R}$.
>- The [integral](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md) $\int_{t_0}^{t_0 + T} |I(t)|^2 \mathop{\mathrm{d}t}$ is [finite](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md) for all $t_0 \in \mathbb{R}$.
>
>We call $f \overset{\text{def}}{=} \frac{1}{T}$ the **frequency** of the [AC source](#Ideal%20Current%20Sources).
>
>>[!NOTATION]
>>
>>We denote [AC sources](#Ideal%20Current%20Sources) in one of the following ways:
>>
>>![AC Source Symbols](./res/Sources/AC%20Source%20Symbols.svg)
>>
>
>>[!EXAMPLE]- Example: Sinusoidal AC Source
>>
>>Most commonly, [AC sources](#Ideal%20Current%20Sources) have a [function](../../Mathematics/Analysis/Functions/Functions.md) $I(t)$ which is given by some [sinusoidal wave](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Real%20Trigonometric%20Functions/Real%20Trigonometric%20Functions.md#The%20Real%20Sine%20Function):
>>
>>$$
>>I(t) = A \sin (\omega t + \phi)
>>$$
>>
>

### Controlled Current Sources

The [current](../Current.md) of an [ideal current source](#Ideal%20Current%20Sources) is completely independent of anything else. However, we often want this [current](../Current.md) to change based on some external parameter. The simplest way we model this is by coupling the [current](../Current.md) either to some other [current](../Current.md) or to some other [voltage](TODO) in the [network](../Network%20Analysis/Lumped%20Elements.md).

>[!DEFINITION] Definition: Current Controlled Current Source (CCCS)
>
>A **current controlled current source** (**CCCS**) is a [two-port](../Network%20Analysis/Two-Ports/Two-Ports.md) whose [input port](../Network%20Analysis/Two-Ports/Two-Ports.md) is a [short circuit](../Network%20Analysis/One-Ports/Short%20Circuits.md) and whose [output port](../Network%20Analysis/Two-Ports/Two-Ports.md) is an [ideal current source](#Ideal%20Current%20Source) for which there exists a [real function](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) $f: \mathbb{R} \to \mathbb{R}$ such that $i_2 = I(t)$, where $I(t) = f(i_1(t))$ for each moment $t$: 
>
>$$
>i_2 = I(t) = f(i_1(t)).
>$$
>
>>[!NOTATION]
>>
>>![CCCS Symbol](./res/Sources/CCCS%20Symbol.svg)
>>
>>Usually, the [input port](../Network%20Analysis/Two-Ports/Two-Ports.md) is not drawn explicitly but is rather understood through context.
>>
>

>[!EXAMPLE]- Example: CCCS with Linear $f$
>
>One very common type of [CCCS](#Controlled%20Current%20Sources) is one where $f$ is a [linear transformation](../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md):
>
>$$
>i_2 = \beta i_1 \qquad \beta \in \mathbb{R}
>$$
>
>>[!THEOREM] Theorem: Explicit Representations
>>
>>It has the following [hybrid representation](../Network%20Analysis/Two-Ports/Two-Ports.md#Representations):
>>
>>$$
>>\begin{bmatrix}v_1 \\ i_2\end{bmatrix} = \boldsymbol{H}\begin{bmatrix}i_1 \\ v_2\end{bmatrix} \qquad \boldsymbol{H} = \begin{bmatrix}0 & 0 \\ \beta & 0\end{bmatrix}
>>$$
>>
>>It has the following [forwards transmission representation](../Network%20Analysis/Two-Ports/Two-Ports.md#Representations):
>>
>>$$
>>\begin{bmatrix}v_1 \\ i_1\end{bmatrix} = \boldsymbol{T}\begin{bmatrix}v_2 \\ -i_2\end{bmatrix} \qquad \boldsymbol{T} = \begin{bmatrix}0 & 0 \\ 0 & -\frac{1}{\beta}\end{bmatrix}
>>$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

>[!DEFINITION] Definition: Voltage Controlled Current Source (VCCS)
>
>A **voltage controlled current source** (**VCCS**) is a [two-port](../Network%20Analysis/Two-Ports/Two-Ports.md) whose [input port](../Network%20Analysis/Two-Ports/Two-Ports.md) is an [open circuit](../Network%20Analysis/One-Ports/Open%20Circuits.md) and whose [output port](../Network%20Analysis/Two-Ports/Two-Ports.md) is an [ideal current source](#Ideal%20Current%20Source) for which there exists a [real function](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) $f: \mathbb{R} \to \mathbb{R}$ such that $i_2 = I(t)$, where $I(t) = f(v_1(t))$ for each moment $t$: 
>
>$$
>i_2 = I(t) = f(v_1(t))
>$$
>
>>[!NOTATION]
>>
>>![VCCS Symbol](./res/Sources/VCCS%20Symbol.svg)
>>
>>Usually, the [input port](../Network%20Analysis/Two-Ports/Two-Ports.md) is not drawn explicitly but is rather understood through context.
>>
>

>[!EXAMPLE]- Example: VCCS with Linear $f$
>
>One very common type of [VCCS](#Controlled%20Current%20Sources) is one where $f$ is a [linear transformation](../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md):
>
>$$
>i_2 = g v_1 \qquad g \in \mathbb{R}
>$$
>
>>[!THEOREM] Theorem: Explicit Representations
>>
>>It has the following [admittance representation](../Network%20Analysis/Two-Ports/Two-Ports.md#Representations):
>>
>>$$
>>\boldsymbol{i} = \boldsymbol{G}\boldsymbol{v} \qquad \boldsymbol{G} = \begin{bmatrix}0 & 0 \\ g & 0\end{bmatrix}
>>$$
>>
>>It has the following [forwards transmission representation](../Network%20Analysis/Two-Ports/Two-Ports.md#Representations):
>>
>>$$
>>\begin{bmatrix}v_1 \\ i_1\end{bmatrix} = \boldsymbol{T}\begin{bmatrix}v_2 \\ -i_2\end{bmatrix} \qquad \boldsymbol{T} = \begin{bmatrix}0 & -\frac{1}{g} \\ 0 & 0\end{bmatrix}
>>$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

### Ideal Voltage Sources

>[!DEFINITION] Definition: Ideal Voltage Source
>
>An **ideal voltage source** is a [one-port](../Network%20Analysis/One-Ports/One-Ports.md) whose [I-V characteristic](../Network%20Analysis/One-Ports/One-Ports.md#I-V%20Characteristics) $\mathcal{F}(t)$ at each time $t$ is given by
>
>$$
>\mathcal{F}(t) = \{(i, v): i \in \mathbb{R}, v = V(t)\},
>$$
>
>where $V$ is some [function](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) which is completely independent of all external factors as well as the [current](../Current.md) $i$.
>
>>[!NOTATION]
>>
>>The following symbol is used for [ideal voltage sources](#Ideal%20Voltage%20Sources):
>>
>>![Ideal Voltage Source Symbol](./res/Sources/Ideal%20Voltage%20Source%20Symbol.svg)
>>
>

An [ideal voltage source](#Ideal%20Voltage%20Sources) is an [independent](../Network%20Analysis/Lumped%20Elements.md) [source](./Sources.md) whose [voltage](TODO) $v$ is given by some [function](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) $V(t)$ at each moment $t$, regardless of everything else, including the [current](../Current.md) flowing through it. This essentially means that at time $t$, the [ideal voltage source](#Ideal%20Voltage%20Sources) creates [voltage](TODO) $V(t)$, regardless of anything else that might be happening. 

In general, the graph of the [voltage](TODO) $v$ with respect to time might look like the following:

![Voltage-Time of Ideal Voltage Source](./res/Sources/Voltage-Time%20of%20Ideal%20Voltage%20Source.svg)

However, at each time $t$, the [I-V characteristic](../Network%20Analysis/One-Ports/One-Ports.md#I-V%20Characteristic) looks like some vertical line because the [voltage](TODO) $v$ of the [ideal voltage source](#Ideal%20Voltage%20Sources) is independent of the [current](../Current.md) flowing through it:

![I-V of Ideal Voltage Source.drawio](./res/Sources/I-V%20of%20Ideal%20Voltage%20Source.drawio.svg)

### Controlled Voltage Sources

The [voltage](TODO) of an [ideal voltage source](#Ideal%20Voltage%20Sources) is completely independent of anything else. However, we often want this [voltage](TODO) to change based on some external parameter. The simplest way we model this is by coupling the [voltage](TODO) either to some other [current](../Current.md) or to some other [voltage](TODO) in the [network](../Network%20Analysis/Lumped%20Elements.md).

>[!DEFINITION] Definition: Current Controlled Voltage Source (CCVS)
>
>A **current controlled voltage source** (**CCVS**) is a [two-port](../Network%20Analysis/Two-Ports/Two-Ports.md) whose [input port](../Network%20Analysis/Two-Ports/Two-Ports.md) is a [short circuit](../Network%20Analysis/One-Ports/Short%20Circuits.md) and whose [output port](../Network%20Analysis/Two-Ports/Two-Ports.md) is an [ideal voltage source](#Ideal%20Voltage%20Source) for which there exists a [real function](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) $f: \mathbb{R} \to \mathbb{R}$ such that $v_2 = V(t)$, where $V(t) = f(i_1(t))$ for each moment $t$: 
>
>$$
>v_2 = V(t) = f(i_1(t))
>$$
>
>>[!NOTATION]
>>
>>![CCVS Symbol](./res/Sources/CCVS%20Symbol.svg)
>>
>>Usually, the [input port](../Network%20Analysis/Two-Ports/Two-Ports.md) is not drawn explicitly but is rather understood through context.
>>
>

>[!EXAMPLE]- Example: CCVS with Linear $f$
>
>One very common type of [CCVS](#Controlled%20Voltage%20Sources) is one where $f$ is a [linear transformation](../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md):
>
>$$
>v_2 = r i_1 \qquad r \in \mathbb{R}
>$$
>
>>[!THEOREM] Theorem: Explicit Representations
>>
>>It has the following [impedance representation](../Network%20Analysis/Two-Ports/Two-Ports.md#Representations):
>>
>>$$
>>\boldsymbol{v} = \boldsymbol{R}\boldsymbol{i} \qquad \boldsymbol{R} = \begin{bmatrix}0 & 0 \\ r & 0\end{bmatrix}
>>$$
>>
>>It has the following [forwards transmission representation](../Network%20Analysis/Two-Ports/Two-Ports.md#Representations):
>>
>>$$
>>\begin{bmatrix}v_1 \\ i_1\end{bmatrix} = \boldsymbol{T}\begin{bmatrix}v_2 \\ -i_2\end{bmatrix} \qquad \boldsymbol{T} = \begin{bmatrix}0 & 0 \\ \frac{1}{r} & 0\end{bmatrix}
>>$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>
>>[!EXAMPLE]- Example: Implementation with $r \lt 0$
>>
>>The simplest implementation of a [CCVS](#Controlled%20Voltage%20Sources) with $r \lt 0$ is just an [inverting](./Amplifiers/Differential%20Voltage%20Amplifiers.md) [finite-gain op-amp](./Amplifiers/Operational%20Amplifiers.md). In this case, $r$ is just equal to the [voltage gain](./Amplifiers/Differential%20Voltage%20Amplifiers.md) $A$:
>>
>>$$
>>r = A
>>$$
>>
>>If this is implemented via an [ideal op-amp](./Amplifiers/Operational%20Amplifiers.md) in the following way, then we have:
>>
>>$$
>>r = -\frac{R_0}{R_1}
>>$$
>>
>>![Inverting DVA via Op-Amp](./Amplifiers/res/Inverting%20DVA%20via%20Op-Amp.svg)
>>
>

>[!DEFINITION] Definition: Voltage Controlled Voltage Source (VCVS)
>
>A **voltage controlled voltage source** (**VCVS**) is a [two-port](../Network%20Analysis/Two-Ports/Two-Ports.md) whose [input port](../Network%20Analysis/Two-Ports/Two-Ports.md) is an [open circuit](../Network%20Analysis/One-Ports/Open%20Circuits.md) and whose [output port](../Network%20Analysis/Two-Ports/Two-Ports.md) is an [ideal voltage source](#Ideal%20Voltage%20Source) for which there exists a [real function](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) $f: \mathbb{R} \to \mathbb{R}$ such that $v_2 = V(t)$, where $V(t) = f(v_1(t))$ for each moment $t$: 
>
>$$
>v_2 = V(t) = f(v_1(t))
>$$
>
>>[!NOTATION]
>>
>>![VCVS Symbol](./res/Sources/VCVS%20Symbol.svg)
>>
>>Usually, the [input port](../Network%20Analysis/Two-Ports/Two-Ports.md) is not drawn explicitly but is rather understood through context.
>>
>

>[!EXAMPLE]- Example: VCVS with Linear $f$
>
>One very common type of [VCVS](#Controlled%20Voltage%20Sources) is one where $f$ is a [linear transformation](../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md):
>
>$$
>v_2 = \mu v_1 \qquad \mu \in \mathbb{R}
>$$
>
>>[!THEOREM] Theorem: Explicit Representations
>>
>>It has the following [inverse hybrid representation](../Network%20Analysis/Two-Ports/Two-Ports.md#Representations):
>>
>>$$
>>\begin{bmatrix}i_1 \\ v_2\end{bmatrix} = \boldsymbol{H}'\begin{bmatrix}v_1 \\ i_2\end{bmatrix} \qquad \boldsymbol{H}' = \begin{bmatrix}0 & 0 \\ \mu & 0\end{bmatrix}
>>$$
>>
>>It has the following [forwards transmission representation](../Network%20Analysis/Two-Ports/Two-Ports.md#Representations):
>>
>>$$
>>\begin{bmatrix}v_1 \\ i_1\end{bmatrix} = \boldsymbol{T}\begin{bmatrix}v_2 \\ -i_2\end{bmatrix} \qquad \boldsymbol{T} = \begin{bmatrix}\frac{1}{\mu} & 0 \\ 0 & 0\end{bmatrix}
>>$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>
>>[!EXAMPLE]- Example: Amplifier Implementation for $\mu \lt 0$
>>
>>A [VCVS](#Controlled%20Voltage%20Sources) can be implemented by connecting an [inverting DVA](./Amplifiers/Differential%20Voltage%20Amplifiers.md#Inverting%20Differential%20Voltage%20Amplifier) to an [op-amp](./Amplifiers/Operational%20Amplifiers.md) [voltage follower](./Amplifiers/Voltage%20Followers.md). In this case, $\mu$ is equal to the [voltage gain](./Amplifiers/Differential%20Voltage%20Amplifiers.md) $A$ of the [inverting DVA](./Amplifiers/Differential%20Voltage%20Amplifiers.md#Inverting%20Differential%20Voltage%20Amplifier):
>>
>>$$
>>\mu = A
>>$$
>>
>>This can be realized using [ideal op-amps](./Amplifiers/Operational%20Amplifiers.md) in the following way:
>>
>>![VCVS via Voltage Follower and Inverting DVA](./res/VCVS%20via%20Voltage%20Follower%20and%20Inverting%20DVA.svg)
>>
>
>>[!EXAMPLE]- Example: Amplifier Implementation for $\mu \gt 0$
>>
>>The simplest implementation of a [VCVS](#Controlled%20Voltage%20Sources) with $\mu \gt 0$ is a [non-inverting](./Amplifiers/Differential%20Voltage%20Amplifiers.md#Non-Inverting%20Differential%20Voltage%20Amplifier) [finite-gain op-amp](./Amplifiers/Operational%20Amplifiers.md). In this case, $\mu$ is equal to the [voltage gain](./Amplifiers/Differential%20Voltage%20Amplifiers.md) $A$.
>>
>>$$
>>\mu = A
>>$$
>>
>>If we implement this using the following [ideal op-amp](./Amplifiers/Operational%20Amplifiers.md) configuration, then we have $\mu = \frac{R_0}{R_1}$:
>>
>>![Non-Inverting DVA via Op-Amp](./Amplifiers/res/Non-Inverting%20DVA%20via%20Op-Amp.svg)
>>
>
