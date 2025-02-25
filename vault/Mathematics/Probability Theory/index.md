---
title: Probability Theory
tags:
  - probability-theory
  - mathematics
---

# Probability Theory

**Probability theory** is the branch of mathematics which studies randomness.

>[!DEFINITION] Definition: Randomness
>
>**Randomness** is an expression of the limits of our knowledge about future events.
>

The mathematical framework for studying randomness and its properties is built upon the foundations of [set theory](../Set%20Theory/index.md). We usually frame this study in the terminology of [experiments](Ex[experiments](./index.md)m an experiment, it has a particular outcome. We group all possible outcomes in the so-called [sample space](E[sample space](./index.md)e how often each outcome or a combination of outcomes (also known as an [event](Experime[event](./index.md) sample space to determine [probabilities](Probability.md).

# Experiments

>[!DEFINITION] Definition: Experiment
>
>An **experiment** in [probability theory](./index.md) is a process whose outcome is always clearly distinguishable from all other outcomes.
>

>[!DEFINITION] Definition: Sample Space
>
>The **sample space** of an [experiment](./index.md#experiments) is the [set](../Set%20Theory/index.md) of all possible outcomes of said experiment.
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

>[!DEFINITION] Definition: Event
>
>An **event** is any [subset](../Set%20Theory/index.md) of the [sample space](./index.md#experiments) of an [experiment](./index.md#experiments).
>
>>[!INTUITION]-
>>
>>Defined in this way, mathematical events allow us to closely model real-world conditions. However, we need a way to translate between the mathematical formalism of events and their physical reality. Hence, we say that an event has **occurred** if the outcome of the experiment is an element of the event.
>>
>
>>[!TIP]- Tip: Union of Events
>>
>>The [union](../Set%20Theory/Collections/Operations%20with%20Collections.md) of a [collection](../Set%20Theory/Collections/index.md) of [events](./index.md#experiments) is the event which occurs if and only if at least one of the events in the collection occurs.
>>
>
>>[!TIP]- Tip: Intersection of Events
>>
>>The [intersection](../Set%20Theory/Collections/Operations%20with%20Collections.md) of a [collection](../Set%20Theory/Collections/index.md) of [events](./index.md#experiments) is the event which occurs if and only if all of the events in the collection occur.
>>
>
>>[!TIP]- Tip: Complement of an Event
>>
>>The [complement](../Set%20Theory/Complement.md) of an event $E$ is the event which occurs if and only if $E$ does *not* occur.
>>
>

>[!DEFINITION] Definition: Mutual Exclusiveness
>
>Two [events](./index.md#experiments) are **mutually exclusive** iff their [intersection](../Set%20Theory/Set%20Operations.md) is the [empty set](../Set%20Theory/The%20Empty%20Set.md).
>