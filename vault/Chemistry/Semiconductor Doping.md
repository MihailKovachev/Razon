---
tags:
    - material-science
    - chemistry
---

# Semiconductor Doping

>[!DEFINITION] Definition: Doping
>
>**Doping** is the process of introducing impurities in the [structure](TODO) of a [semiconductor](TODO).
>

[Doping](#Doping) is primarily done to change the properties of [semiconductors](TODO).

## P-Type Semiconductors

>[!DEFINITION] Definition: P-Type Semiconductor
>
>A **p-type semiconductor** is a [semiconductor](TODO) which has been [doped](#Doping) with an [element](TODO) which has fewer [valence electrons](TODO) than the [semiconductor](TODO) itself.
>

The [dopant](#Doping) is known as an **acceptor** in this case. In practice, the difference in [valence electrons](TODO) is rarely greater than one. If the [host](#Doping) has $N$ [valence electrons](TODO) and the [dopant](#Doping) has $N - 1$ [valence electrons](TODO), then the [dopant](#Doping) forms a [bond](TODO) with $N - 1$ of its neighboring [hosts](#Doping). However the [dopant](#Doping) cannot form a [bond](TODO) with the $N$-th neighboring [host](#Doping) because it lacks the necessary [valence electrons](TODO). This means that the [charge density](../Physics/Classical%20Electromagnetism/Electric%20Charge.md) between the [dopant](#Doping) and this neighboring [host](#Doping) is more positive than between it and its $N-1$ neighboring [hosts](#Doping). It turns out that these regions of more positive [charge density](../Physics/Classical%20Electromagnetism/Electric%20Charge.md) behave exactly like [electrons](TODO) but with a positive [charge](../Physics/Classical%20Electromagnetism/Electric%20Charge.md) and are thus called **electron holes**.

![P-Type Semiconductor Lattice 1](./res/P-Type%20Semiconductor%20Lattice%201.svg)

However, this configuration is unstable and small [energy](TODO) perturbations can cause an [electron](TODO) from one of the [bonds](TODO) between two neighboring [hosts](#Doping) to move so as to form a [bond](TODO) between the [dopant](#Doping) and its $N$-th neighbor, which moves the [electron hole](#P-Type%20Semiconductors). The [dopant](#Doping) becomes a fixed negative [ion](TODO). This process continues further between the [hosts](#Doping) many times as the [electron hole](#P-Type%20Semiconductors) moves randomly around the lattice.

![P-Type Semiconductor Lattice 2](./res/P-Type%20Semiconductor%20Lattice%202.svg)

>[!NOTATION] Notation: Doping Concentration
>
>We use different notations depending on the amount of [doping](#Doping):
>- $p^{-}$ means light [doping](#Doping);
>- $p$ means moderate [doping](#Doping);
>- $p^{+}$ means heavy [doping](#Doping).
>

Most commonly, [silicon](TODO) is [doped](#Doping) with [boron](TODO). 

## N-Type Semiconductors

>[!DEFINITION] Definition: N-Type Semiconductor
>
>An **n-type semiconductor** is a [semiconductor](TODO) which has been [doped](#Doping) with an [element](TODO) which has more [valence electrons](TODO) than the [semiconductor](TODO) itself.
>

The [dopant](#Doping) is known as a **donor** in this case. In practice, the difference in [valence electrons](TODO) is rarely greater than one. If the [host](#Doping) has $N$ [valence electrons](TODO) and the [dopant](#Doping) has $N + 1$ [valence electrons](TODO), then the [dopant](#Doping) forms a [bond](TODO) with all $N$ of its neighboring [hosts](#Doping). However, the [dopant](#Doping) has an extra [valence electron](TODO) left over which cannot form a [bond](TODO). This extra [electron](TODO) moves freely around the lattice, thus making the [dopant](#Doping) a positive [ion](TODO).

![N-Type Semiconductor Lattice](./res/N-Type%20Semiconductor%20Lattice.svg)

>[!NOTATION] Notation: Doping Concentration
>
>We use different notations depending on the amount of [doping](#Doping):
>- $n^{-}$ means light [doping](#Doping);
>- $n$ means moderate [doping](#Doping);
>- $n^{+}$ means heavy [doping](#Doping).
>

Most commonly, [silicon](TODO) is [doped](#Doping) with [phosphorus](TODO).

## P-N Junctions

A [p-type semiconductor](#P-Type%20Semiconductors) or [n-type semiconductor](#N-Type%20Semiconductors) can be additionally [doped](#Doping) with a [dopant](#Doping) of the opposite type, thus forming a [p-type region](#P-Type%20Semiconductors) and an [n-type region](#N-Type%20Semiconductors) which are in direct contact with one another. At the boundary between these two regions, free [electrons](TODO) from the [n-type region](#N-Type%20Semiconductors) flow into the [p-type region](#P-Type%20Semiconductors) to fill in [holes](#P-Type%20Semiconductors). However, the positive and negative [ions](TODO) are stuck in place. Therefore, a third region known as a **depletion region** or **p-n junction** forms at the boundary, where there are no free [charge](../Physics/Classical%20Electromagnetism/Electric%20Charge.md) carries but there is a difference in [charge density](../Physics/Classical%20Electromagnetism/Electric%20Charge.md) due to the [ions](TODO). This difference creates an [electric field](../Physics/Classical%20Electromagnetism/Electric%20Fields.md) throughout the [depletion region](#P-N%20Junction) which points from the [n-type region](#N-Type%20Semiconductors) to the [p-type region](#P-Type%20Semiconductors). In other words, [voltage](../Physics/Classical%20Electromagnetism/Electric%20Potential.md) forms across the [p-n junction](#P-N%20Junction).

![P-N Junction](../Electrical%20Engineering/Analog%20Circuits/Diodes/res/P-N%20Junction.svg)

The amount of [doping](./Semiconductor%20Doping.md) determines the properties of the [p-n junction](#P-N%20Junction). In particular, the [p-n junction](#P-N%20Junction) extends further into the region with *less* [doping](./Semiconductor%20Doping.md)  than into the region with more [doping](./Semiconductor%20Doping.md) because it must remain [electrically](../Physics/Classical%20Electromagnetism/Electric%20Charge.md) neutral as a whole and a larger region of lower [dopant](./Semiconductor%20Doping.md) concentration is necessary to accumulate the same [electric charge](../Physics/Classical%20Electromagnetism/Electric%20Charge.md) as a smaller region with a higher [dopant](./Semiconductor%20Doping.md) concentration.