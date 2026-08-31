---
tags:
    - printed-circuit-boards
    - electrical-engineering
---

# Traces

A **trace** in a [PCB](./Printed%20Circuit%20Board.md) is a thin segment of conductive material in a [conductive layer](./Printed%20Circuit%20Board.md) (typically copper) which connects [electronic components](../Electronic%20Components.md).

![PCB Traces Photo](./res/PCB%20Traces%20Photo.png)

The three most important physical characteristics of a [trace](./Traces.md) are its length, width and thickness and they play a great role in determining the electrical properties of the [trace](./Traces.md).

![PCB Trace Dimensions](./res/PCB%20Trace%20Dimensions.svg)

>[!TIP]- Tip: Trapezoidal Cross-Section
>
>The manufacturing process actually makes [traces](./Traces.md) with a trapezoidal cross-section but we can treat it as rectangular to a great approximation. 
>
>![PCB Trace Cross-Section](./res/PCB%20Trace%20Cross-Section.svg)
>

The thickness of a [trace](./Traces.md) is the [copper weight](./Printed%20Circuit%20Board.md) of the [conductive layer](./Printed%20Circuit%20Board.md) in which it resides. The only way to change it is to use a different [build-up](./Printed%20Circuit%20Board.md#Build-Up), but this is rarely a good strategy. Instead, one should rely on varying the width and the length to achieve the desired goals.

A typical width can range anywhere from 0.1 mm to 1.0 mm. Each manufacturer has their own minimum width which they support, but this limit should be avoided because it comes with increased costs and lower yields. The width for a given [trace](./Traces.md) should be chosen according to its purpose. Common widths are in the range of 0.2 mm - 0.3 mm (~10 mils) for signal [traces](./Traces.md) and 0.5 mm - 1.0 mm (~20 mils) for power [traces](./Traces.md) (including [ground](./Ground.md)), but these are only rough guidelines. In fact, certain applications like [controlled impedance](TODO) require the strict calculation of a specific width.

The length of a [trace](./Traces.md) also has a great effect on its electrical properties. In the vast majority of cases, [traces](./Traces.md) should be kept as short as possible because additional length increases the emission of and susceptibility to interference. However, artificially increasing the length of a [trace](./Traces.md) is commonly done when specific signal timing requirements need to be met.

## Current Handling 

[Traces](./Traces.md) heat up as [current](../Current.md) passes through them and it is often necessary to keep their temperature within a given range. This is done by calculating an appropriate [trace](./Traces.md) width based on the maximum continuous [current](../Current.md) the [trace](./Traces.md) needs to sustain and the maximum permissible temperature rise. There are many online calculators which can do this. 

Furthermore, each [trace](./Traces.md) itself has an absolute maximum continuous [current](../Current.md) which it can sustain, mainly based on its physical dimensions. Exceeding this limit can cause such a high temperature that the [trace](./Traces.md) itself can start melting or burn up.

## Theoretical Modelling

Despite the physical simplicity of [traces](./Traces.md), modelling their electrical properties is actually fairly complicated. In the simplest of designs, a [trace](./Traces.md) can be modelled as a [short circuit](../Network%20Analysis/One-Ports/Short%20Circuits.md), but this model reaches its limit really quickly.

A more accurate model treats the [trace](./Traces.md) as an [RL series circuit](../Network%20Analysis/RL%20Series%20Circuit.md) between the two connected [components](../Electronic%20Components.md):

TODO: Diagram

The [resistance](../Network%20Analysis/One-Ports/Strictly%20Linear%20Resistive%20One-Ports.md) $R$ is given by the [resistivity](TODO) $\rho$ of copper, the cross-sectional area $A$ of the [trace](./Traces.md) as well as its length $l$. By treating the cross-section as a rectangle, its area $A$ can be approximated using the [trace](./Traces.md)'s width $w$ and thickness $h$:

$$R = \frac{\rho \cdot l}{A} =  \frac{\rho \cdot l}{w \cdot h}$$

Calculating the [inductance](../Network%20Analysis/One-Ports/Strictly%20Linear%20Inductive%20One-Ports.md) $L$ is more involved but for frequencies of up to a few MHz, $L$ can be approximated using the Rosa-Grover formula:

$$L = 0.2\cdot l \left( 0.5 + \frac{0.2235 \cdot (w + h)}{l} + \ln \frac{2l}{w + h} \right)$$

Here, $L$ is nH, while the width $w$, length $l$ and thickness $h$ are in mm. We see that $L$ is dominated by $h$: a longer [trace](./Traces.md) as more [inductance](../Network%20Analysis/One-Ports/Strictly%20Linear%20Inductive%20One-Ports.md).