---
title: Load Line Analysis
tags:
    - network-analysis
    - electrical-engineering
---

# Load Line Analysis

**Load line analysis** is a technique for analyzing [circuits](../../Electronic%20Circuits.md) which are reducible to a [time-invariant](../Ports.md#I-V%20Characteristic) [linear source](../../Analog%20Circuits/Sources.md) and a [time-invariant](../Ports.md#I-V%20Characteristic) non-linear [one-port](../One-Ports/One-Ports.md) connected in [parallel](../One-Ports/One-Port%20Interconnections.md):

![Load Line Circuit](./res/Load%20Line%20Circuit.svg)

We are interested in what [current](../../Current.md) flows through the two [one-ports](../One-Ports/One-Ports.md) and what the [voltage](TODO) across them is. 

We begin by choosing the  a [reference direction](../Network%20Analysis.md) for the [voltage](TODO):

![Load Line Analysis Voltage](./res/Load%20Line%20Analysis%20Voltage.svg)

Since we have a [source](../../Analog%20Circuits/Sources.md), the standard is to use the [active sign convention](../One-Ports/One-Ports.md) for it, but we keep the [passive sign convention](../One-Ports/One-Ports.md) for the non-linear [one-port](../One-Ports/One-Ports.md):

![Load Line Analysis Current](./res/Load%20Line%20Analysis%20Current.svg)

>[!DEFINITION] Definition: Operating Point
>
>An **operating point** of this [circuit](../../Electronic%20Circuits.md) is any pair $(v, i)$ of values for $V$ and $I$ such that
>
>$$
>(v, i) \in \mathcal{F}_{\text{non-linear}} \qquad \text{and} \qquad (v, -i) \in \mathcal{F}_{\text{source}}
>$$
>

An [operating point](./Load%20Line%20Analysis.md) is essentially any configuration of [voltage](TODO) and [current](../../Current.md) at which both the [source](../../Analog%20Circuits/Sources.md) and the non-linear [one-port](../One-Ports/One-Ports.md) can operate.

>[!INFO] Info: Why the Minus?
>
>The negative sign for the [source](../../Analog%20Circuits/Sources.md) is there because [I-V characteristics](../Ports.md#I-V%20Characteristic) are always given in terms of the [passive sign convention](../One-Ports/One-Ports.md). However, the standard for [sources](../../Analog%20Circuits/Sources.md) is to use the [active sign convention](../One-Ports/One-Ports.md) when analyzing them in the context of a particular [circuit](../../Electronic%20Circuits.md), which is why we chose the [current](../../Current.md) $I$ to flow *out of* the [positive terminal](../One-Ports/One-Ports.md) of the [source](../../Analog%20Circuits/Sources.md). The [I-V characteristic](../Ports.md#I-V%20Characteristic) $\mathcal{F}_{\text{source}}$ is thus given in terms of the *negative* of $I$.
>
>If we define $I' \overset{\text{def}}{=} -I$, we would get the following equivalent description:
>
>![Reverse Current Line Load Analysis](../One-Ports/res/Reverse%20Current%20Line%20Load%20Analysis.svg)
>

There are three possibilities for the [operating points](./Load%20Line%20Analysis.md):
- There may be *no* [operating points](./Load%20Line%20Analysis.md). This means that the [circuit](../../Electronic%20Circuits.md) cannot function. What exactly happens *physically*, however, is impossible to predict. The [circuit](../../Electronic%20Circuits.md) might explode, it might do nothing or it might behave unexpectedly.
- There may be *exactly one* [operating point](./Load%20Line%20Analysis.md). In this case, the [circuit](../../Electronic%20Circuits.md) will settle into this point.
- There may be *multiple* [operating point](./Load%20Line%20Analysis.md). In this case, the [circuit](../../Electronic%20Circuits.md) will settle into one of these points, but it is not generally possible to predict which one.

**Load line analysis** is a technique to determine how many [operating points](./Load%20Line%20Analysis.md) there are and what they are.

  >[!ALGORITHM] Algorithm: Algebraic Load Line Analysis
  >
  >If $\mathcal{F}_{\text{non-linear}}$ and $\mathcal{F}_{\text{source}}$ have [implicit representations](../One-Ports/One-Ports.md#I-V%20Characteristic) $f_{\text{non-linear}}$ and $f_{\text{source}}$, respectively, then the [operating points](./Load%20Line%20Analysis.md) of the [circuit](../../Electronic%20Circuits.md) are precisely the solutions to the following system of equations:
>
>$$
>\left\vert
>\begin{aligned}
>f_{\text{non-linear}}(V, I) &= 0 \\
>f_{\text{source}}(V, -I) &= 0
>\end{aligned}
>\right.
>$$
>

>[!ALGORITHM] Algorithm: Geometric Load Line Analysis
>
>We can find the [operating points](./Load%20Line%20Analysis.md) graphically by looking at the graphs of the [I-V characteristics](../One-Ports/One-Ports.md#I-V%20Characteristic) $\mathcal{F}_{\text{non-linear}}$ and $\mathcal{F}_{\text{source}}$.
>
>1. Draw the graphs of the [I-V characteristics](../One-Ports/One-Ports.md#I-V%20Characteristic) $\mathcal{F}_{\text{non-linear}}$ and $\mathcal{F}_{\text{source}}$:
>
>![Load Line Analysis - I-V Characteristic](./res/Load%20Line%20Analysis%20-%20I-V%20Characteristic.svg)
>
>- We use $I'$ and $V'$ for $\mathcal{F}_{\text{source}}$ to make it clear that we take into account the [active sign convention](../One-Ports/One-Ports.md), i.e. that $I'$ corresponds to $-I$. We use the label $V'$ for consistency, but $V'$ is still the same as $V$.
>
>2. Draw $\mathcal{F}_{\text{source}}$ on the same graph as $\mathcal{F}_{\text{non-linear}}$. When doing this, we need to reflect $\mathcal{F}_{\text{source}}$ across the $V$ axis, since $I = -I'$.
>
>![Load Line Analysis Graphical](./res/Load%20Line%20Analysis%20Graphical.svg)
>
>- This reflected line is known as the **load line**. The points where it intersects $\mathcal{F}_{\text{non-linear}}$ are precisely the [operating points](./Load%20Line%20Analysis.md).
>