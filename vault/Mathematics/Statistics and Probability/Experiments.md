---
title: Experiments
tags:
  - probability-theory
  - mathematics
---

# Experiments

>[!DEFINITION] Definition: Experiment
>
>An **experiment** in [probability theory](index.md) is a process with the following properties:
>- The process can occur multiple times;
>- All possible outcomes are known and unambiguously defined;
>- It is always one and only one of the outcomes which happens.
>

>[!DEFINITION] Definition: Sample Space
>
>The **sample space** of an [experiment](Experiments.md#Experiments) is the [set](../Set%20Theory/Sets.md) of all possible outcomes of said experiment.
>
>>[!NOTATION]
>>
>>Sample spaces are often denoted by $\Omega$.
>>
>
>>[!EXAMPLE]- Example: Flipping a Coin
>>
>>Flipping a coin is a very simple experiment whose sample space $S$ contains only two possible outcomes - the coin falls heads-up or the coin falls tails-up. Hence, $S$ is just
>>
>>$$
>>S = \{\mathrm{heads}, \mathrm{tails}\}
>>$$
>>
>
>>[!EXAMPLE]- Example: Rolling a Die
>>
>>Another common experiment is the roll of a single six-sided die. There are six possible outcomes - the number on the die is 1, 2, 3, 4, 5 or 6. Hence, the sample space is
>>
>>$$
>>S = \{1, 2, 3, 4, 5, 6\}
>>$$
>>
>
>>[!EXAMPLE]- Example: Flipping Two Coins
>>
>>
>>
>

## Events

>[!DEFINITION] Definition: Event
>
>An **event** is any [subset](../Set%20Theory/Sets.md) of the [sample space](index.md#experiments) of an [experiment](index.md#experiments).
>

Defined in this way, mathematical events allow us to closely model real-world conditions. However, we need a way to translate between the mathematical formalism of events and their physical reality. Hence, we say that an event has **occurred** if the outcome of the experiment is an element of the event.

>[!TIP] Tip: Union of Events
>
>The [union](../Set%20Theory/Collections/Operations%20with%20Collections.md) of a [collection](../Set%20Theory/Collections/Collections.md) of [events](index.md#experiments) is the event which occurs if and only if at least one of the events in the collection occurs.
>

>[!TIP] Tip: Intersection of Events
>
>The [intersection](../Set%20Theory/Collections/Operations%20with%20Collections.md) of a [collection](../Set%20Theory/Collections/Collections.md) of [events](index.md#experiments) is the event which occurs if and only if all of the events in the collection occur.
>

>[!TIP] Tip: Complement of an Event
>
>The [complement](../Set%20Theory/Complement.md) of an event $E$ is the event which occurs if and only if $E$ does *not* occur.
>

>[!DEFINITION] Definition: Mutual Exclusiveness
>
>A [collection](../Set%20Theory/Collections/Collections.md) of [events](Experiments.md#experiments) are **mutually exclusive** if and only if every [intersection](../Set%20Theory/Set%20Operations.md) between two of the [events](Experiments.md#experiments) is [empty](../Set%20Theory/The%20Empty%20Set.md).
>