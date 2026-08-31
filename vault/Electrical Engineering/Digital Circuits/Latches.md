---
tags:
    - digital-circuits
    - electrical-engineering
---

# Latches

>[!DEFINITION] Definition: Latch
>
>A **latch** is a [level-triggered](./Circuit%20Triggering.md#Level%20Triggering) [digital circuit](./Digital%20Circuits.md) which can switch between two stable states of its outputs.
>

The word "asynchronously" means that a [latch](./Latches.md) can change its state at any time and does not depend on a clock signal.

# SR NOR Latches

An **SR NOR latch** is a [latch](./Latches.md) consisting of two cross-coupled [NOR gates](./Logic%20Gates/Logic%20Gates.md):

![SR NOR Latch](./res/Latches/SR%20NOR%20Latch.svg) 

The inputs are labelled $R$ and $S$ because the [SR NOR latch](#SR%20NOR%20Latches) exhibits **active high behavior**, i.e. the desired behavior occurs at $R = 1$ or $S = 1$. 

The [SR NOR latch](#SR%20NOR%20Latches) can be in one of the following states:

|State|$R$|$S$|$Q$|$\overline{Q}$|Description|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Memory|$0$|$0$|$Q_{prev}$|$\overline{Q}_{prev}$|Maintains the previous state.|
|Set|$0$|$1$|$1$|$0$|Sets $Q = 1$ and $\overline{Q} = 0$.|
|Reset|$1$|$0$|$0$|$1$|Sets $Q = 0$ and $\overline{Q} = 1$.|
|Invalid|$1$|$1$|$0$|$0$|Invalid because $Q = \overline{Q}$.|

The problem with the invalid state is that the [SR NOR latch](#SR%20NOR%20Latches) cannot safely enter the memory state from it. It is perfectly safe to enter the set or reset state from the invalid state, but trying to directly enter the memory state by simultaneously setting $R = 0$ and $S = 0$ results in unpredictable behavior. 

>[!NOTATION]
>
>[SR NOR latches](#SR%20NOR%20Latches) are typically labeled as $SR$ and are represented by the following symbol:
>
>![SR NOR Latch Symbol](./res/Latches/SR%20NOR%20Latch%20Symbol.svg)
>
>When the output $\overline{Q}$ is not used, we can also omit it.
>

# SR NAND Latches

An **SR NAND latch** is a [latch](./Latches.md) consisting of two cross-coupled [NAND gates](./Logic%20Gates/Logic%20Gates.md):

![SR NAND Latch](./res/Latches/SR%20NAND%20Latch.svg) 

The inputs are labelled $\overline{R}$ and $\overline{S}$ because the [SR NAND latch](#SR%20NAND%20Latches) exhibits **active low behavior**, i.e. the desired behavior occurs at $\overline{R} = 0$ or $\overline{S} = 0$. 

The [SR NAND latch](#SR%20NAND%20Latches) can be in one of the following states:

|State|$\overline{R}$|$\overline{S}$|$Q$|$\overline{Q}$|Description|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Memory|$1$|$1$|$Q_{prev}$|$\overline{Q}_{prev}$|Maintains the previous state.|
|Set|$1$|$0$|$1$|$0$|Sets $Q = 1$ and $\overline{Q} = 0$.|
|Reset|$0$|$1$|$0$|$1$|Sets $Q = 0$ and $\overline{Q} = 1$.|
|Invalid|$0$|$0$|$1$|$1$|Invalid because $Q = \overline{Q}$.|

The problem with the invalid state is that the [SR NAND latch](#SR%20NAND%20Latches) cannot safely enter the memory state from it. It is perfectly safe to enter the set or reset state from the invalid state, but trying to directly enter the memory state by simultaneously setting $\overline{R} = 1$ and $\overline{S} = 1$ results in unpredictable behavior. 

>[!NOTATION]
>
>[SR NAND latches](#SR%20NAND%20Latches) are typically labeled as $\overline{S}\overline{R}$ and are represented by the following symbol:
>
>![SR NAND Latch Symbol](./res/Latches/SR%20NAND%20Latch%20Symbol.svg)
>
>When the output $\overline{Q}$ is not used, we can also omit it.
>

# Controlled SR Latches

To determine **when** an [SR NOR latch](#SR%20NOR%20Latches) or an [SR NAND latch](#SR%20NAND%20Latches) is allowed to change state, we can limit its ability to react to inputs by introducing a third input known as a **control** or **enable** bit ($C$ or $En$).

## Controlled SR NOR Latches

To implement [control](#Controlled%20SR%20Latches) for an [SR NOR latch](#SR%20NOR%20Latches), we can use two additional [AND gates](./Logic%20Gates/Logic%20Gates.md):

![Controlled SR NOR Latch](./res/Latches/Controlled%20SR%20NOR%20Latch.svg)

If $C = 0$, the inputs $R$ and $S$ have no effect.

If $C = 1$, then the [controlled SR NOR latch](#Controlled%20SR%20NOR%20Latches) can be in one of the following states:

|State|$S$|$R$|$Q$|$\overline{Q}$|Description|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Memory|$0$|$0$|$Q_{prev}$|$\overline{Q}_{prev}$|Maintains the previous state.|
|Set|$1$|$0$|$1$|$0$|Sets $Q = 1$ and $\overline{Q} = 0$.|
|Reset|$0$|$1$|$0$|$1$|Sets $Q = 0$ and $\overline{Q} = 1$.|
|Invalid|$1$|$1$|$0$|$0$|Invalid because $Q = \overline{Q}$.|

Unfortunately, this does not completely solve the problem because the latch still enters the invalid state if $C = S = R = 1$ at the same time.

>[!NOTATION]
>
>[Controlled SR NOR latches](#Controlled%20SR%20NOR%20Latches) are represented using one of the following symbols:
>
>![Controlled SR Latch Symbol](./res/Latches/Controlled%20SR%20Latch%20Symbol.svg)
>
>When the output $\overline{Q}$ is not used, we can also omit it.
>

## Controlled SR NAND Latches

To implement [control](#Controlled%20SR%20Latches) for an [SR NAND latch](#SR%20NAND%20Latches), we can use two additional [NAND gates](./Logic%20Gates/Logic%20Gates.md):

![Controlled SR NAND Latch](./res/Latches/Controlled%20SR%20NAND%20Latch.svg)

We immediately notice that the inputs are now labelled with $S$ and $R$ instead of $\overline{S}$ and $\overline{R}$ because [controlled SR NAND latches](#Controlled%20SR%20NAND%20Latches) exhibit **active high behavior**, i.e. the desired behavior is achieved when $S = 1$ or $R = 1$.

When $C = 0$, the inputs $S$ and $R$ have no effect.

When $C = 1$, the [controlled SR NAND latch](#Controlled%20SR%20NAND%20Latches) can be in one of the following states:

|State|$S$|$R$|$Q$|$\overline{Q}$|Description|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Memory|$0$|$0$|$Q_{prev}$|$\overline{Q}_{prev}$|Maintains the previous state.|
|Set|$1$|$0$|$1$|$0$|Sets $Q = 1$ and $\overline{Q} = 0$.|
|Reset|$0$|$1$|$0$|$1$|Sets $Q = 0$ and $\overline{Q} = 1$.|
|Invalid|$1$|$1$|$1$|$1$|Invalid because $Q = \overline{Q}$.|

Unfortunately, this does not completely solve the problem because the latch still enters the invalid state if $C = S = R = 1$ at the same time.

>[!NOTATION]
>
>[Controlled SR NAND latches](#Controlled%20SR%20NAND%20Latches) are represented using one of the following symbols:
>
>![Controlled SR Latch Symbol](./res/Latches/Controlled%20SR%20Latch%20Symbol.svg)
>
>When the output $\overline{Q}$ is not used, we can also omit it.
>

Functionally, a [controlled SR NAND latch](#Controlled%20SR%20NAND%20Latches) differs from a [controlled SR NOR latch](#Controlled%20SR%20NOR%20Latches) only by the invalid state:
- The invalid state of a [controlled SR NAND latch](#Controlled%20SR%20NAND%20Latches) is $Q = \overline{Q} = 1$.
- The invalid state of a [controlled SR NOR latch](#Controlled%20SR%20NOR%20Latches) is $Q = \overline{Q} = 0$.

# D Latches

A **D latch** is a [latch](./Latches.md) based either on a [controlled SR NOR latch](#Controlled%20SR%20NOR%20Latches) or a [controlled SR NAND latch](#Controlled%20SR%20NAND%20Latches) which completely eliminates the problem of an invalid state. The trick is to couple the inputs $S$ and $R$ so that they are always opposite:

![D Latch](./res/Latches/D%20Latch.svg)

The two implementations are completely identical.

If $C = 0$, then $D$ has no effect.

If $C = 1$, then $D$ is transferred to $Q$ and its negation $\overline{D}$ is transferred to $\overline{Q}$.

>[!NOTATION]
>
>[D latches](#D%20Latches) are represented by the following symbols:
>
>![D Latch Symbols](./res/Latches/D%20Latch%20Symbols.svg)
>
>When the output $\overline{Q}$ is not used, we can also omit it.
>
