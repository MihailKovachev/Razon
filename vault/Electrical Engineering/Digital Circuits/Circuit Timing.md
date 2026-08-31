---
tags:
    - digital-circuits
    - electrical-engineering
---

# Circuit Timing

Nothing in the physical world happens instantaneously and this applies to [digital circuits](./Digital%20Circuits.md) as well. There are always delays involved between the changes in the inputs of a [digital circuit](./Digital%20Circuits.md) and the corresponding changes in its outputs. Moreover, a signal itself cannot instantaneously switch between $0$ and $1$ or vice-versa. This transition also takes time.

These delays must be taken into account to ensure that a [digital circuit](./Digital%20Circuits.md) will function properly.

## Transition Times

The transition of a signal from a LOW to a HIGH state or vice-versa is very fast, but still gradual and takes time.

>[!DEFINITION] Definition: Transition Time
>
>The time it takes for a signal to change from one state to another is known as **transition time**.
>

In practice, it matters whether the signal goes from a LOW to a HIGH state or from a HIGH to a LOW state and so we usually have two different [transition times](#Transition%20Times) for each signal.

>[!DEFINITION] Definition: Rise Time
>
>The **rise time** is the time it takes for a signal to go from a LOW state, to a HIGH state.
>
>>[!NOTE]
>>
>>Most commonly, rise time is measured as the time it takes for the signal to go from 10% to 90% of the final [voltage](TODO).
>>
>>![Signal Rise Time](./res/Signal%20Rise%20Time.svg)
>>
>

>[!DEFINITION] Definition: Fall Time
>
>The **fall time** is the time it takes for a signal to go from a HIGH state to a LOW state.
>
>>[!NOTE]
>>
>>Most commonly, rise time is measured as the time it takes for the signal to go from 90% to 10% of the final [voltage](TODO).
>>
>>![Signal Fall Time](./res/Signal%20Fall%20Time.svg)
>>
>

# Contamination and Propagation

[Digital circuits](./Digital%20Circuits.md) are really fast but still operate at a finite speed, which introduces delays. As the complexity of a [circuit](./Digital%20Circuits.md) grow, the paths between its inputs and outputs get more complicated and the delays from their components begin to add up. This means that it takes more time for a change in the inputs to be reflected in the outputs.

>[!DEFINITION] Definition: Contamination Delay
>
>Let $C$ be a [digital circuit](./Digital%20Circuits.md) with $m$ inputs $I_1, \dotsc, I_m$ and $n$ outputs $O_1, \dotsc, O_n$.
>
>The ****
>

>[!DEFINITION] Definition: Propagation Delay
>
>Let $C$ be a [digital circuit](./Digital%20Circuits.md) with $m$ inputs $I_1, \dotsc, I_m$ and $n$ outputs $O_1, \dotsc, O_n$.
>
>The **high-to-low propagation delay** between $I_j$ and $O_k$ is the time elapsed between $I_j$ transitioning $50 \%$ and the output $O_k$ transitioning $50 \%$.
>
>>[!NOTATION]
>>
>>$$
>>
>>$$
>>
>

>[!DEFINITION] Definition: Contamination Delay
>
>The **contamination delay** of a [digital circuit](./Digital%20Circuits.md) is the minimum time it takes for an output to *begin* transitioning into a stable after a change in the input.
>

>[!DEFINITION] Definition: Propagation Delay
>
>The **propagation delay** of a [digital circuit](./Digital%20Circuits.md) is the maximum time it takes for an output to *finish* transitioning into a stable state after a change in the input.
>

In practice, [contamination delays](#Contamination%20and%20Propagation) and [propagation delays](#Contamination%20and%20Propagation) are measured starting when the input transition is at $50 \%$ until the output transition is also at $50 \%$. 

![Contamination and Propagation](./res/Contamination%20and%20Propagation.svg)

We also usually have two different [contamination delays](#Contamination%20and%20Propagation) and two different [propagation delays](#Contamination%20and%20Propagation) depending on whether the output is switching from LOW to HIGH or vice-versa. Moreover, in reality each path in a [digital circuit](./Digital%20Circuits.md) has its own LOW-to-HIGH and HIGH-to-LOW [contamination delay](#Contamination%20and%20Propagation) and its own LOW-to-HIGH and HIGH-to-LOW [propagation delays](#Contamination%20and%20Propagation). The [contamination delays](#Contamination%20and%20Propagation) and [propagation delays](#Contamination%20and%20Propagation) of the entire [circuit](./Digital%20Circuits.md) are then the minimum and maximum of these delays, respectively.

>[!NOTATION]
>
>We denote the [contamination delays](#Contamination%20and%20Propagation) by $t_{\text{cLH}}$ and $t_{\text{cHL}}$ and the [propagation delays](#Contamination%20and%20Propagation) by $t_{\text{pLH}}$ and $t_{\text{pHL}}$.
>

Essentially, the [contamination delay](#Contamination%20and%20Propagation) of a [digital circuit](./Digital%20Circuits.md) is the *minimum* possible delay before any of its outputs begins changing. We have to wait for [contamination delay](#Contamination%20and%20Propagation) to see any change in the output. Otherwise we would just be reading its old state, which is not particularly useful.

By contrast, the [propagation delay](#Contamination%20and%20Propagation) of a [digital circuit](./Digital%20Circuits.md) is the *maximum* possible delay before all its outputs have settled into a stable state. Once the [propagation delay](#Propagation%20Delays) has passed, we are guaranteed to have a meaningful state for the outputs, but not before that. 

Trying to read off the output of a [digital circuit](./Digital%20Circuits.md) in the time interval between its [contamination delay](#Contamination%20and%20Propagation) and [propagation delay](#Contamination%20and%20Propagation) can therefore result in an invalid or spurious state for the output. This is why the [propagation delay](#Contamination%20and%20Propagation)ultimately limits the maximum speed at which the [digital circuit](./Digital%20Circuits.md) can operate: we *must* wait for the [propagation delay](#Contamination%20and%20Propagation) to pass, lest we run the risk of encountering a bad output state.

# Synchronization

>[!DEFINITION] Definition: Synchronous Circuit
>
>A [digital circuit](./Digital%20Circuits.md) is **synchronous** if it is made up of [edge triggered](./Circuit%20Triggering.md#Edge%20Triggering) devices whose [active period](./Circuit%20Triggering.md) is tied to a common [signal](./Digital%20Circuits.md).
>

Usually, this common [signal](./Digital%20Circuits.md) is a [clock signal](./Digital%20Circuits.md) with a specific period $T_{\text{clk}}$. 

To operate a [synchronous](#Synchronization) [circuit](./Digital%20Circuits.md) correctly, the timing parameters of its components must be taken into account.

>[!IMPORTANT] Important: Setup Constraint
>
>The timing parameters of a [synchronous](#Synchronization) [circuit](./Digital%20Circuits.md) are subject to the **setup constraint**
>
>$$
>T_{\text{clk}} \ge t_{\text{setup}} + t_{\text{logic,max}} + t_{\text{c2q}},
>$$
>
>where:
>- $T_{\text{clk}}$ is the period of the common [clock signal](./Digital%20Circuits.md);
>- $t_{\text{logic,max}}$ is the [propagation delay](./Circuit%20Timing.md) of the slowest [combinational](./Combinational%20Circuits.md) path between two components [triggered](./Circuit%20Triggering.md#Edge%20Triggering) by the [clock signal](./Digital%20Circuits.md);
>- $t_{\text{setup}}$ is the [setup time](./Circuit%20Triggering.md#Edge%20Triggering) of the sourceof this path;
>- $t_{\text{c2q}}$ is the [propagation delay](./Circuit%20Timing.md) of the destination of this path.
>

>[!IMPORTANT] Important: Hold Constraint
>
>The timing parameters of a [synchronous](#Synchronization) [circuit](./Digital%20Circuits.md) are subject to the **hold constraint**
>
>$$
>t_{\text{hold}} \le t_{\text{logic,min}} + t_{c2q},
>$$
>
>where:
>- $t_{\text{logic,min}}$ is the [propagation delay](./Circuit%20Timing.md) of the fastest [combinational](./Combinational%20Circuits.md) path between two components [triggered](./Circuit%20Triggering.md#Edge%20Triggering) by the [clock signal](./Digital%20Circuits.md);
>- $t_{\text{hold}}$ is the [hold time](./Circuit%20Triggering.md#Edge%20Triggering) of the source of this path;
>- $t_{\text{c2q}}$ is the [propagation delay](./Circuit%20Timing.md) of the destination of this path.
>