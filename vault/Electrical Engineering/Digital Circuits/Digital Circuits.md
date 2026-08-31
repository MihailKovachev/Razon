---
tags:
  - digital-circuits
  - electrical-engineering
---

# Introduction

**Digital circuits** are [electronic circuits](../Electronic%20Circuits.md) designed to operate with discrete values. 

The idea is to build the [circuits](../Electronic%20Circuits.md) so that they behave differently whenever [voltage](TODO) falls within different ranges but behave identically whenever it lies within the same range. One naive way to implement this is to define a **digital signal** as a logical $1$ whenever the [voltage](TODO) $v(t)$ at some point is greater that some fixed value $V'$ and to define it as a logical $0$ whenever $v(t)$ is lower than $V'$:

$$
\mathrm{dig} (t) = \begin{cases} 1 \qquad \text{when } v(t) \gt V' \\ 0 \qquad \text{when } v(t) \lt V'\end{cases}
$$

Unfortunately, physical imperfections in [electronic circuits](../Electronic%20Circuits.md) make it so that $v(t)$ often experiences perturbations and if this happens when $v(t)$ is around $V'$, the behavior of the [circuit](../Electronic%20Circuits.md) will drastically change as $v(t)$ temporarily crosses the boundary between the two regions. This is obviously undesirable.

>[!DEFINITION] Definition: Digital Signal
>
>The **digital signal** at a point $p$ is a [function](../../Mathematics/Analysis/Functions/Functions.md) $\mathrm{dig}_p: \mathbb{R} \to \{0, 1, \text{non-logical}\}$ which at each time $t$ is defined using the [voltage](TODO) $v_p(t)$ at $p$:
>
>$$
>\mathrm{dig}_p(t) \overset{\text{def}}{=} \begin{cases} 0 & \text{if} & v_p(t) \lt V_{\text{low}} \\ \text{non-logical} & \text{if} & v_p(t) \in [V_{\text{low}}; V_{\text{high}}] \\ 1 & \text{if} & v_p(t) \gt V_{\text{high}}\end{cases}
>$$
>
>where $0 \mathop{\mathrm{V}} \lt V_{\text{low}} \lt V_{\text{high}}$.
>
>>[!DEFINITION] Definition: Logical Signal
>>
>>We say that $\mathrm{dig}_p$ is **logical** at time $t$ if $\mathrm{dig}_p(t) \in \{0,1\}$.
>>
>
>>[!DEFINITION] Definition: Stable Signal
>>
>>We say that $\mathrm{dig}_p$ is **stable** during $[t_1; t_2]$ if $\mathrm{dig}_p(t) = 0$ for all $t \in [t_1; t_2]$ or $\mathrm{dig}_p(t) = 1$ for all $t \in [t_1; t_2]$.
>>
>

## Noise

The way we defined a [digital signal](./Digital%20Circuits.md) deals with fluctuations at a single point. However, as [voltage](TODO) changes propagate, they also accumulate noise $\mathcal{N}(t)$ due to imperfections in wires or the presence of external fields. This might result in a [digital signal](./Digital%20Circuits.md) which was originally [logical](./Digital%20Circuits.md) might become [non-logical](./Digital%20Circuits.md) by the time it reaches its destination. The solution is to use separate thresholds for inputs and outputs:

>[!DEFINITION] Definition: Source Digital Signal
>
>The **source digital signal** at some [input](../Network%20Analysis/Lumped%20Elements.md) of a [network](../Network%20Analysis/Lumped%20Elements.md) is a [function](../../Mathematics/Analysis/Functions/Functions.md) $\mathrm{dig}_{\text{in}}: \mathbb{R} \to \{0, 1, \text{non-logical}\}$ which at each time $t$ is defined using the [voltage](TODO) $v_{\text{in}}(t)$ at the [input](../Network%20Analysis/Lumped%20Elements.md):
>
>$$
>\mathrm{dig}_{\text{in}}(t) \overset{\text{def}}{=} \begin{cases} 0 & \text{if} & v_{\text{in}}(t) \lt V_{\text{in, low}} \\ \text{non-logical} & \text{if} & v_{\text{in}}(t) \in [V_{\text{in, low}}; V_{\text{in, high}}] \\ 1 & \text{if} & v_{\text{in}}(t) \gt V_{\text{in, high}}\end{cases}
>$$
>
>where $0 \mathop{\mathrm{V}} \lt V_{\text{in, low}} \lt V_{\text{in, high}}$.
>

>[!DEFINITION] Definition: Destination Digital Signal
>
>The ** digital signal** at some [input](../Network%20Analysis/Lumped%20Elements.md) of a [network](../Network%20Analysis/Lumped%20Elements.md) is a [function](../../Mathematics/Analysis/Functions/Functions.md) $\mathrm{dig}_{\text{out}}: \mathbb{R} \to \{0, 1, \text{non-logical}\}$ which at each time $t$ is defined using the [voltage](TODO) $v_{\text{out}}(t)$ at the [input](../Network%20Analysis/Lumped%20Elements.md):
>
>$$
>\mathrm{dig}_{\text{out}}(t) \overset{\text{def}}{=} \begin{cases} 0 & \text{if} & v_{\text{out}}(t) \lt V_{\text{out, low}} \\ \text{non-logical} & \text{if} & v_{\text{out}}(t) \in [V_{\text{out, low}}; V_{\text{out, high}}] \\ 1 & \text{if} & v_{\text{out}}(t) \gt V_{\text{out, high}}\end{cases}
>$$
>
>where $0 \mathop{\mathrm{V}} \lt V_{\text{out, low}} \lt V_{\text{out, high}}$.
>

For this model to be useful, however, the thresholds $V_{\text{in, low}}$, $V_{\text{in, high}}$, $V_{\text{out, low}}$ and $V_{\text{out, high}}$ must be chosen appropriately.

In particular, they must obey the following:

$$
V_{\text{out, low}} \lt V_{\text{in, low}} \lt V_{\text{in, high}} \lt V_{\text{out, high}}
$$

>[!DEFINITION] Definition: Noise Margins
>
>The values $V_{\text{in, low}} - V_{\text{out, low}}$ and $V_{\text{out, high}} - V_{\text{in, high}}$ are called **noise margins**.
>

As long as the noise falls within the [noise margins](./Digital%20Circuits.md), the [input digital signals](./Digital%20Circuits.md) 

>[!THEOREM] Theorem: 

>[!DEFINITION] Definition: Fan-In
>
>The **fan-in** of a component in a [digital circuit](./Digital%20Circuits.md) is the number of its inputs.
>

>[!DEFINITION] Definition: Fan-Out
>
>The **fan-out** of a component in a [digital circuit](./Digital%20Circuits.md) is the total number of components its to which its outputs are connected.
>

## Combinational Circuits

>[!DEFINITION] Definition: Combinational Circuits
>
>A **combinational circuit** is a [digital circuit](./Digital%20Circuits.md) whose outputs depend solely on the current inputs and nothing else.
>

In particular, [combinational circuits](./Digital%20Circuits.md) have no memory. Their behavior is not influenced by the past. All that is relevant for the outputs are the current inputs.

## Sequential Circuits

>[!DEFINITION] Definition: Sequential Circuits
>
>A **sequential circuit** is a [digital circuit](./Digital%20Circuits.md) whose outputs depend on the current inputs but also on past events.
>

[Sequential circuits](./Digital%20Circuits.md) can be thought of as having memory because their current behavior is influenced by their past.