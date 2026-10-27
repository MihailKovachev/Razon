---
tags:
    - digital-circuits
    - electrical-engineering
---

# SR Latch

## SR NOR Latch

|State|$R$|$S$|$Q$|$\overline{Q}$|Description|
|:--:|:--:|:--:|:--:|:--:|:--:|
|Hold|$0$|$0$|$Q_{\text{old}}$|$\overline{Q}_{\text{old}}$|Holds the previous state.|
|Set|$0$|$1$|$1$|$0$|$Q = 1$ and $\overline{Q} = 0$.|
|Reset|$1$|$0$|$0$|$1$|Sets $Q = 0$ and $\overline{Q} = 1$.|
|Invalid|$1$|$1$|$0$|$0$|Invalid because $Q = \overline{Q}$.|

![SR NOR Latch](./res/Latches/SR%20NOR%20Latch.svg)

>[!NOTATION]
>
>![SR NOR Latch Symbol](./res/Latches/SR%20NOR%20Latch%20Symbol.svg)
>

### Controlled SR NOR Latch

## SR NAND Latch

![SR NAND Latch](./res/Latches/SR%20NAND%20Latch.svg)

>[!NOTATION]
>
>![SR NAND Latch Symbol](./res/Latches/SR%20NAND%20Latch%20Symbol.svg)
>

### Controlled SR NAND Latch