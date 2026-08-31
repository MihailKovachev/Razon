---
tags:
    - analog-circuits
    - electrical-engineering
---

# MOSFET

A **metal-oxide-semiconductor field-effect transistor** is a [field-effect transistor](./Transistors.md) which functions by exploiting the properties of [MOS capacitors](../MOS%20Capacitors.md) and [p-n junctions](../../../Chemistry/Semiconductor%20Doping.md#P-N%20Junctions).

## Enhancement-Mode MOSFET

### Structure

An [enhancement-mode MOSFET](#Enhancement-Mode%20MOSFET) has the same structure as a [MOS capacitor](../MOS%20Capacitors.md#Structure) except that the [substrate](../MOS%20Capacitors.md#Structure) is embedded with two regions of heavily [doped](../../../Chemistry/Semiconductor%20Doping.md) [semiconductor](../../../Chemistry/Electrical%20Conductivity.md) of the opposite [type](../../../Chemistry/Semiconductor%20Doping.md) which are lateral to the [gate](../MOS%20Capacitors.md#Structure):

- In a **p-channel** [enhancement-mode MOSFET](#Enhancement-Mode%20MOSFET) (**PMOS**), the [substrate](../MOS%20Capacitors.md#Structure) is made of [n-type semiconductor](../../../Chemistry/Semiconductor%20Doping.md#N-Type%20Semiconductors) and the lateral regions are made of [p-type semiconductor](../../../Chemistry/Semiconductor%20Doping.md#P-Type%20Semiconductors).
- In an **n-channel** [enhancement-mode MOSFET](#Enhancement-Mode%20MOSFET) (**NMOS**), the [substrate](../MOS%20Capacitors.md#Structure) is made of [p-type semiconductor](../../../Chemistry/Semiconductor%20Doping.md#P-Type%20Semiconductors) and the lateral regions are made of [n-type semiconductor](../../../Chemistry/Semiconductor%20Doping.md#N-Type%20Semiconductors).

Each of the lateral regions is connected to a [terminal](../../Electronic%20Circuits.md), either the **source** or the **drain**.

![Enh MOSFET Structure](./res/Enh%20MOSFET%20Structure.svg)

The most important dimensional parameters of a [MOSFET](#Enhancement-Mode%20MOSFET) are the physical distance (**channel length**) $L$ between the [source](#Enhancement-Mode%20MOSFET) and the [drain](#Enhancement-Mode%20MOSFET), the **width** $W$ and the thickness $t_{\text{ox}}$ of the [insulator layer](../MOS%20Capacitors.md). 

We want $L$ to be as small as possible, usually being around 60 nm - 70 nm. The value of $t_{\text{ox}}$ is usually around 50 times smaller than $L$, i.e. between 1.5 nm and 2 nm. The width $W$ can vary widely, ranging from a couple hundred nanometers to tens of micrometers.

>[!NOTATION]
>
>The following symbols are used for [enhancement-mode MOSFETs](#Enhancement-Mode%20MOSFET) to explicitly indicate that the [bulk](#Enhancement-Mode%20MOSFET) and [source](#Enhancement-Mode%20MOSFET) are connected:
>
>|NMOS|PMOS|
>|:--:|:--:|
>|![Enh NMOS Symbol Bulk to Source](./res/Enh%20NMOS%20Symbol%20Bulk%20to%20Source.svg)|![Enh PMOS Symbol Bulk to Source](./res/Enh%20PMOS%20Symbol%20Bulk%20to%20Source.svg)|
>
>The following symbols are used for [enhancement-mode MOSFETs](#Enhancement-Mode%20MOSFET) to explicitly indicate that the [bulk](#Enhancement-Mode%20MOSFET) and [source](#Enhancement-Mode%20MOSFET) are not connected:
>
>|NMOS|PMOS|
>|:--:|:--:|
>|![Enh NMOS Symbol Bulk Open](./res/Enh%20NMOS%20Symbol%20Bulk%20Open.svg)|![Enh PMOS Bulk Open](./res/Enh%20PMOS%20Bulk%20Open.svg)|
>
>The following symbols are also used for [enhancement-mode MOSFETs](#Enhancement-Mode%20MOSFET) but give no information whether the [bulk](#Enhancement-Mode%20MOSFET) and [source](#Enhancement-Mode%20MOSFET) are connected or not:
>
>|NMOS|PMOS|
>|:--:|:--:|
>|![Enh NMOS No Bulk Symbol 1](./res/Enh%20NMOS%20No%20Bulk%20Symbol%201.svg)|![Enh PMOS No Bulk Symbol 1](./res/Enh%20PMOS%20No%20Bulk%20Symbol%201.svg)|
>|![Enh NMOS No Bulk Symbol 2](./res/Enh%20NMOS%20No%20Bulk%20Symbol%202.svg)|![Enh PMOS No Bulk Symbol 2](./res/Enh%20PMOS%20No%20Bulk%20Symbol%202.svg)|
>

The combination of [NMOS](#Enhancement-Mode%20MOSFET) and [PMOS](#Enhancement-Mode%20MOSFET) for the implementation of [digital circuits](../../Digital%20Circuits/Digital%20Circuits.md) is known as **complementary MOS** (**CMOS**).

### Physical Characteristics

Each [enhancement-mode MOSFET](#Enhancement-Mode%20MOSFET) is characterized by a few fixed constants which stem from the physical properties of its elements and their configuration:

|Constant|Description|
|:--:|:--:|
|$\varepsilon_{\text{ox}}$|The [relative electric permittivity](TODO) $\varepsilon_{\text{ox}}$ of the [insulation layer](../MOS%20Capacitors.md).|
|$\mu$ (usually $\mu_n$ for [NMOS](#Enhancement-Mode%20MOSFET) and $\mu_p$ for [NMOS](#Enhancement-Mode%20MOSFET))|Measures how easily [charge](../../../Physics/Classical%20Electromagnetism/Electric%20Charge.md) carriers can move around.|

$$\mu_n \approx 3 \mu_p$$

$$C_{\text{ox}} = \frac{\varepsilon_{\text{ox}}\varepsilon_{0}}{t_{\text{ox}}}$$

The **process transconductance parameter**:

$$k' = \mu C_{\text{ox}} = \frac{\mu \cdot \varepsilon_{\text{ox}} \cdot \varepsilon_0}{t_{\text{ox}}}$$

The **total gate capacitance**:

$$C_{\text{G}} = \frac{\varepsilon_{\text{ox}}\cdot \varepsilon_0 \cdot W \cdot L}{t_{\text{ox}}}$$

The **threshold voltage** $V_{\text{th}}$ - positive for [NMOS](#Enhancement-Mode%20MOSFET) and negative for [PMOS](#Enhancement-Mode%20MOSFET).

### Operation

The following variables are used to characterize the operation of an [enhancement-mode MOSFET](#Enhancement-Mode%20MOSFET):

- the [voltage](../../../Physics/Classical%20Electromagnetism/Electric%20Potential.md) $V_{\text{GS}}$ between the [gate](#Enhancement-Mode%20MOSFET) and the [source](#Enhancement-Mode%20MOSFET): $V_{\text{GS}} = \phi_{\text{G}} - \phi_{\text{S}}$;
- the [voltage](../../../Physics/Classical%20Electromagnetism/Electric%20Potential.md) $V_{\text{DS}}$ between the [drain](#Enhancement-Mode%20MOSFET) and the [source](#Enhancement-Mode%20MOSFET): $V_{\text{DS}} = \phi_{\text{D}} - \phi_{\text{S}}$;
- the [current](../../Current.md) $I_\text{D}$ flowing from the [drain](#Enhancement-Mode%20MOSFET) to the [source](#Enhancement-Mode%20MOSFET).

![Enh MOSFET Variables](./res/Enh%20MOSFET%20Variables.svg)

In an [NMOS](#Enhancement-Mode%20MOSFET), the [source](#Enhancement-Mode%20MOSFET) is always at a lower [potential](../../../Physics/Classical%20Electromagnetism/Electric%20Potential.md) than the [drain](#Enhancement-Mode%20MOSFET): $\phi_{\text{S}} \lt \phi_{\text{D}}$.

In a [PMOS](#Enhancement-Mode%20MOSFET), the [source](#Enhancement-Mode%20MOSFET) is always at a higher [potential](../../../Physics/Classical%20Electromagnetism/Electric%20Potential.md) than the [drain](#Enhancement-Mode%20MOSFET): $\phi_{\text{S}} \gt \phi_{\text{D}}$.

This, combined with the above convention, which is used for both [PMOS](#Enhancement-Mode%20MOSFET) and [NMOS](#Enhancement-Mode%20MOSFET), ultimately determines the algebraic signs of the aforementioned quantities:

||NMOS|PMOS|
|:--:|:--:|:--:|
|$V_{\text{GS}}$|$\gt 0$|$\lt 0$|
|$V_{\text{DS}}$|$\gt 0$|$\lt 0$|
|$I_{\text{D}}$|$\gt 0$|$\lt 0$|

The operation of a [MOSFET](#Enhancement-Mode%20MOSFET) is divided into three **modes** or **regions** depending on the relationship between $V_{\text{GS}}$, $V_{\text{DS}}$ and $V_{\text{th}}$:

- $|V_{\text{GS}}| \lt |V_{\text{th}}|$ (**cutoff region**);
- $|V_{\text{GS}}| \gt |V_{\text{th}}|$  and $|V_{\text{DS}}| \lt |V_{\text{GS}}| - |V_{\text{th}}|$ (**triode region** or **linear region**);
- $|V_{\text{GS}}| \gt |V_{\text{th}}|$ and $|V_{\text{DS}}| \ge ​|V_{\text{GS}}|-|V_{\text{th}}|$ (**saturation region**).

The most common theoretical model for the dependence of $I_{\text{D}}$ on $V_{\text{GS}}$ and $V_{\text{DS}}$ is the following:

$$I_{\text{D}, \text{NMOS}} = \begin{cases}0, & 0 \le V_{\text{GS}} \lt V_{\text{th}} \text{ and } V_{\text{DS}} \ge 0 & \text{(cutoff)} \\ \beta \left(V_{\text{GS}} - V_{\text{th}} - \frac{V_{\text{DS}}}{2}\right)V_{\text{DS}}, & V_{\text{GS}} \gt V_{\text{th}} \text{ and } 0 \lt V_{\text{DS}} \lt V_{\text{GS}} - V_{\text{th}} & \text{(linear)} \\ \frac{\beta}{2}(V_{\text{GS}}-V_{\text{th}})^2, & V_{\text{GS}} \gt V_{\text{th}} \text{ and } V_{\text{DS}} \gt V_{\text{GS}} - V_{\text{th}} & \text{(saturation)}\end{cases}$$

$$I_{\text{D}, \text{PMOS}} = \begin{cases}0, & 0 \ge V_{\text{GS}} \gt V_{\text{th}} \text{ and } V_{\text{DS}} \le 0 & \text{(cutoff)} \\ -\beta \left(V_{\text{GS}} - V_{\text{th}} - \frac{V_{\text{DS}}}{2}\right)V_{\text{DS}}, & V_{\text{GS}} \lt V_{\text{th}} \text{ and } 0 \gt V_{\text{DS}} \gt V_{\text{GS}} - V_{\text{th}} & \text{(linear)} \\ -\frac{\beta}{2}(V_{\text{GS}}-V_{\text{th}})^2, & V_{\text{GS}} \lt V_{\text{th}} \text{ and } V_{\text{DS}} \lt V_{\text{GS}} - V_{\text{th}} & \text{(saturation)}\end{cases}$$

$$\beta = \frac{\mu C_{G}}{L^2} = k_n'\frac{W}{L}$$

#### Transfer Characteristic

The [voltage](../../../Physics/Classical%20Electromagnetism/Electric%20Potential.md) $V_{\text{GS}}$ between the [gate](#Enhancement-Mode%20MOSFET) and the [source](#Enhancement-Mode%20MOSFET) controls the [resistance](../../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) between the [drain](#Enhancement-Mode%20MOSFET) and the [source](#Enhancement-Mode%20MOSFET).

The **transfer characteristic** of an [enhancement-mode MOSFET](#Enhancement-Mode%20MOSFET) describes the relationship between the [current](../../Current.md) $I_D$ and $V_{\text{GS}}$ for a fixed $V_{\text{DS}}$. It is divided into three regions.

In the **cutoff region** ($|V_{\text{GS}}| \lt |V_{\text{th}}|$), the two [p-n junctions](../../../Chemistry/Semiconductor%20Doping.md#P-N%20Junctions) cause very high [resistance](../../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) and the [current](../../Current.md) $I_{\text{D}}$ is effectively zero ($I_D \approx 0$).

![Enh MOSFET Cutoff](./res/Enh%20MOSFET%20Cutoff.svg)

In the **saturation region** ($V_{\text{th}} \lt V_{\text{GS}} \lt V_{\text{th}} + V_{\text{DS}}$), the [MOS structure](../MOS%20Capacitors.md#Structure) enters [inversion mode](../MOS%20Capacitors.md#Inversion) and the [drain](#Enhancement-Mode%20MOSFET) and the [source](#Enhancement-Mode%20MOSFET) become connected by a channel which contains the same type of mobile [charge](../../../Physics/Classical%20Electromagnetism/Electric%20Charge.md) carriers as them, effectively bypassing the [p-n junctions](../../../Chemistry/Semiconductor%20Doping.md#P-N%20Junctions). This causes the [resistance](../../Network%20Analysis/One-Ports/One-Ports.md#Resistance%20and%20Conductance) between the [drain](#Enhancement-Mode%20MOSFET) and the [source](#Enhancement-Mode%20MOSFET) to drop, since [current](../../Current.md) $I_D$ can now flow between the [drain](#Enhancement-Mode%20MOSFET) to the [source](#Enhancement-Mode%20MOSFET) via this channel. The [current](../../Current.md) $I_D$ increases quadratically with $V_{\text{DS}}$.

![MOSFET Conducting](./res/MOSFET%20Conducting.svg)
 
 In the **triode region** or **linear region** ($|V_{\text{GS}}| \gt |V_{\text{DS}}| + |V_{\text{th}}|$), the [current](../../Current.md) $I_D$ increases linearly with $V_{\text{DS}}$.

![Enh MOSFEET Linear Region](./res/Enh%20MOSFEET%20Linear%20Region.svg)

#### Output Characteristic

The **output characteristic** or **drain characteristic** of an [enhancement-mode MOSFET](#Enhancement-Mode%20MOSFET) describes the relationship between the [current](../../Current.md) $I_D$ and $V_{\text{DS}}$ for a fixed $V_{\text{GS}}$.

When the [MOSFET](#Enhancement-Mode%20MOSFET) is in the [cutoff region](#Transfer%20Characteristic) ($V_{\text{GS}} \lt V_{\text{th}}$), the [current](../../Current.md) $I_D$ is effectively zero, regardless of $V_{\text{DS}}$. 

When the [MOSFET](#Enhancement-Mode%20MOSFET) is in the [triode region](#Transfer%20Characteristic) ($V_{\text{GS}} \gt V_{\text{th}}$ and $V_{\text{DS}} \lt V_{\text{GS} - V_{\text{th}}}$), the dependence between $I_D$ and $V_{\text{DS}}$ is [linear](../../../Mathematics/Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md).

When the [MOSFET](#Enhancement-Mode%20MOSFET) is in the [saturation region](#Transfer%20Characteristic) ($V_{\text{GS}} \gt V_{\text{th}}$ and $V_{\text{DS}} \ge V_{\text{GS} - V_{\text{th}}}$), the [current](../../Current.md) $I_D$ remains constant, regardless of how much $V_{\text{DS}}$ increases.