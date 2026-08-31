---
title: Circuit Triggering
tags:
    - digital-circuits
    - electrical-engineering
---

# Introduction

We often want to limit when a [digital circuit](./Digital%20Circuits.md) can respond to its inputs.

>[!DEFINITION] Definition: Active Circuit
>
>A [digital circuit](./Digital%20Circuits.md) is **active** during a time period $\Delta t$, if its outputs can be affected by its inputs during $\Delta t$.
>

>[!DEFINITION] Definition: Inactive Circuit
>
>A [digital circuit](./Digital%20Circuits.md) is **inactive** during a time period $\Delta t$, if its outputs cannot be affected by its inputs during $\Delta t$.
>

The process of turning an [inactive circuit](./Circuit%20Triggering.md) into an [active circuit](./Circuit%20Triggering.md) is known as **triggering**. This is usually done by adding an additional input to the [circuit](./Digital%20Circuits.md), known as a **trigger**, which controls when the [circuit](./Digital%20Circuits.md) is active.

## Level Triggering

>[!DEFINITION] Definition: Level Triggering
>
>A [digital circuit](./Digital%20Circuits.md) is **level-triggered** if it is [active](./Circuit%20Triggering.md) only during the time when its [trigger](./Circuit%20Triggering.md) is in a specific, stable state.
>

In other words, a [level-triggered](#Level%20Triggering) [digital circuit](./Digital%20Circuits.md) is [active](./Circuit%20Triggering.md) when its [trigger](./Circuit%20Triggering.md) is either $0$ or$1$, but is [inactive](./Circuit%20Triggering.md) when its [trigger](./Circuit%20Triggering.md) is transitioning from $0$ to $1$ or vice versa. 

We have two types of [level triggering](#Level%20Triggering):

>[!DEFINITION] Definition: Positive Level Triggering
>
>A [level-triggered](#Level%20Triggering) [digital circuit](./Digital%20Circuits.md) has **positive level triggering** if it is [active](./Circuit%20Triggering.md) only when its [trigger](./Circuit%20Triggering.md) is set to a stable set of $1$.
>
>![Positive Level Triggering](./res/Positive%20Level%20Triggering.svg)
>

>[!DEFINITION] Definition: Negative Level Triggering
>
>A [level-triggered](#Edge%20Triggering) [digital circuit](./Digital%20Circuits.md) has **negative level triggering** if it is [active](./Circuit%20Triggering.md) only when its [trigger](./Circuit%20Triggering.md) is set to a stable set of $0$.
>
>![Negative Level Triggering](./res/Negative%20Level%20Triggering.svg)
>

## Edge Triggering

>[!DEFINITION] Definition: Edge Triggering
>
>A [digital circuit](./Digital%20Circuits.md) is **edge-triggered** if it is [active](./Circuit%20Triggering.md) only during the time when its [trigger](./Circuit%20Triggering.md) is transitioning between two stable states.
>

In other words, an [edge-triggered](#Edge%20Triggering) [digital circuit](./Digital%20Circuits.md) is [active](./Circuit%20Triggering.md) when its [trigger](./Circuit%20Triggering.md) is in the process of transitioning from $0$ to $1$ or vice versa, but is [inactive](./Circuit%20Triggering.md) when its [trigger](./Circuit%20Triggering.md) is in a stable state of $0$ or $1$.

We have two types of [edge triggering](#Edge%20Triggering):

>[!DEFINITION] Definition: Positive Edge Triggering
>
>An [edge-triggered](#edge%20Triggering) [digital circuit](./Digital%20Circuits.md) has **positive edge triggering** if it is [active](./Circuit%20Triggering.md) only when its [trigger](./Circuit%20Triggering.md) is transitioning from $0$ to $1$.
>
>![Positive Edge Triggering](./res/Positive%20Edge%20Triggering.svg)
>

>[!DEFINITION] Definition: Negative Edge Triggering
>
>An [edge-triggered](#Level%20Triggering) [digital circuit](./Digital%20Circuits.md) has **negative edge triggering** if it is [active](./Circuit%20Triggering.md) only when its [trigger](./Circuit%20Triggering.md) is transitioning from $1$ to $0$.
>
>![Negative Edge Triggering](./res/Negative%20Edge%20Triggering.svg)
>

In practice, ensuring the correct functioning of an [edge triggered](#Edge%20Triggering) [circuit](./Digital%20Circuits.md) requires that its inputs are held stable for a particular time period before as well as after each [trigger](./Circuit%20Triggering.md).

>[!DEFINITION] Definition: Setup Time
>
>The **setup time** $t_{\text{setup}}$ of an [edge triggered](#Edge%20Triggering) [circuit](./Digital%20Circuits.md) is the minimum duration for which its inputs need to be stable *before* each [trigger](./Circuit%20Triggering.md) to ensure proper function.
>

>[!DEFINITION] Definition: Hold Time
>
>The **hold time** $t_{\text{hold}}$ of an [edge triggered](#Edge%20Triggering) [circuit](./Digital%20Circuits.md) is the minimum duration for which its inputs need to be stable *after* each [trigger](./Circuit%20Triggering.md) to ensure proper function.
>