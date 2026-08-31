---
tags:
    - electrical-engineering
---

# Diodes

**Diodes** are a general class of [electronic components](../../Electronic%20Components.md) whose main function is restricting [current](../../Current.md) flow to a single direction. However, many [diodes](./Diodes.md) can be used for a much wider range of purposes such as limiting [voltage](TODO), emitting light, generating electricity from light and more.

>[!DEFINITION] Definition: Diodes
>
>A **diode** is a [one-port](../../../index.md) used to restrict the flow of [current](../../Current.md) to only one direction.
>
>>[!DEFINITION] Definition: Anode
>>
>>The **anode** is the [terminal](../../Network%20Analysis/Network%20Analysis.md) of the [diode](./Diodes.md) *from* which [current](../../Current.md) is allowed to flow.
>>
>
>>[!DEFINITION] Definition: Cathode
>>
>>The **cathode** is the [terminal](../../Network%20Analysis/Network%20Analysis.md) of the [diode](./Diodes.md) *into* which [current](../../Current.md) is allowed to flow.
>>
>

## p-n Diodes

A **p-n diode** is built from two layers of semiconducting materials. Most commonly, silicon is used:
- The p-layer is obtained by doping silicon with an element which has less than four electrons in its valence shell such as boron, which has only three. Since silicon has four electrons and boron has three, each silicon atom can only form three bonds. Statistically, this means that the p-layer has electrons missing from its structure.
- The n-layer is obtained by doping silicon with an element which has more than four electrons in its valence shell such as phosphorus, which has five. Each Since silicon has four electrons and phosphorus has five, each silicon atom can will form only four bonds. Statistically, this means that the n-layer has extra electrons in its structure.

When the two layers are physically brought together, electrons move spontaneously across the boundary from the n-layer to the p-layer in order to fill the gaps. The n-layer now contains positive phosphorus ions, while the p-layer contains negative boron ions. Since these ions are stable, the charges no longer want to move around. This in turn introduces a [potential](TODO) difference at the boundary between the two layers, which we call the **depletion region** because it is devoid of free charges. 

This [potential](TODO) difference biases the p-n diode:
- If an external [voltage](TODO) is applied so as to oppose the internal [voltage](TODO), e.g. by connecting the positive (+) terminal of a [battery](TODO) to the p-layer and the negative (-) terminal to the n-layer, the barrier is lowered, thus allowing [current](../../Current.md) to easily flow.
- If an external [voltage](TODO) is applied so as to combine with the internal [voltage](TODO), e.g. by connecting the positive (+) terminal of a [battery](TODO) to the n-layer and the negative (-) terminal to the p-layer, the barrier is increased, thus making it harder for [current](../../Current.md) to flow.

>[!NOTATION]
>
>In [circuit diagrams](../../Network%20Analysis/Network%20Analysis.md#Circuit%20Digrams), [p-n diodes](#p-n%20Diodes) are denoted by the following symbol:
>
>![p-n Diode Symbol](../../Network%20Analysis/One-Ports/res/p-n%20Diode%20Symbol.svg)
>
>The arrow always points from the [anode](#Diodes) (p-layer) to the [cathode](#Diodes) (n-layer).
>

>[!IMPORTANT] Important: V-I Characteristics of p-n Diodes
>
>Each [p-n diode](#p-n%20Diodes) is characterized by a **threshold voltage** $U_{\text{threshold}}$, which is usually between $0.6 \mathop{\mathrm{V}}$ and $0.7 \mathop{\mathrm{V}}$, and a **breakdown voltage** $U_{\text{breakdown}} \ll 0$:
>- If the external [voltage](TODO) $U$ is larger than $U_{\text{threshold}}$, the [p-n diode](#p-n%20Diodes) lets [current](../../Current.md) through which grows [exponentially](../../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Real%20Exponentiation.md#The%20Real%20Exponential%20Function) as $U$ increases. The [p-n diode](#p-n%20Diodes) is in the **forward bias region** ($U \gt U_{\text{threshold}}$).
>- If $U$ is lower than $U_{\text{threshold}}$, only a tiny [current](../../Current.md) $I_S$ flows but in the opposite direction, which we call **reverse saturation current**. The [p-n diode](#p-n%20Diodes) is in the **reverse bias region** ($U \gt U_{\text{threshold}}$).
>- If $U$ also becomes lower than $U_{\text{breakdown}}$, the [voltage](TODO) becomes strong enough to cause a chain reaction by accelerating charges which rapidly collide with other charges and so on. Thus, a large [current](../../Current.md) starts flowing but in the opposite direction. This often destroys the [p-n diode](#p-n%20Diodes). 
>
>![p-n Diode V-I Characteristic](../../Network%20Analysis/One-Ports/res/p-n%20Diode%20V-I%20Characteristic.svg)
>
>>[!THEOREM] Theorem: V-I Characteristics of p-n Diodes
>>
>>The [explicit V-I characteristic](../../../index.md#V-I%20Characteristic) of an ideal [p-n diode](#p-n%20Diodes) with $U_{\text{threshold}} = 0$ and $U_{\text{breakdown}} = -\infty$ is:
>>
>>$$
>>I = |I_S| \left(\mathrm{e}^{\frac{U}{U_T}} - 1\right) \qquad U = U_T \ln \left(\frac{I}{|I_s|} + 1\right),
>>$$
>>
>>where $I_S$ is the [reverse saturation current](#p-n%20Diodes) and $U_T$ is the **thermal voltage** of the [p-n diode](#p-n%20Diodes) defined as
>>
>>$$
>>U_T = \frac{k_B T}{e},
>>$$
>>
>>where $k_B = 1.380649 \times 10^{-23} \frac{\mathrm{J}}{\mathrm{K}}$ is [Boltzmann's constant](TODO), $T$ is the [temperature](TODO) of the [p-n diode](#p-n%20Diodes) and $e = 1.602176634 \times 10^{−19} \mathop{\mathrm{C}}$ is the [elementary electric charge](../../../Physics/Classical%20Electromagnetism/Electric%20Charge.md).
>>
>>>[!NOTE]
>>>
>>>The [thermal voltage](#p-n%20Diodes) $U_T$ has nothing to do with $U_{\text{threshold}}$ and is around $25 \mathop{\mathrm{mV}}$ at [room temperature](TODO).
>>>
>>
>>![I-V of p-n Diode Characteristic](../../Network%20Analysis/One-Ports/res/I-V%20of%20p-n%20Diode%20Characteristic.svg)
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

>[!THEOREM] Theorem: Polarity of p-n Diodes
>
>Every ideal [p-n diode](#p-n%20Diodes) is [polarized](../../../index.md#Polarity).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Power of p-n Diodes
>
>Every ideal [p-n diode](#p-n%20Diodes) is [passive](../../../index.md#Polar).
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Zener Diodes

>[!DEFINITION] Definition: Zener Diodes
>
>A **Zener diode** is a [p-n diodes](#p-n%20Diodes) designed to operate beyond its [breakdown voltage](#p-n%20Diodes) without getting destroyed.
>
>
>>[!NOTATION] Notation
>>
>>In circuit diagrams, [Zener diodes](#Zener%20Diodes) are denoted by
>>
>>![Zener Diode Symbol](../../Network%20Analysis/One-Ports/res/Zener%20Diode%20Symbol.svg)
>>
>

## Photodiodes

**Photodiodes** are special [diodes](./Diodes.md) which are sensitive to [light](TODO). When a [photon](TODO) with sufficient [frequency](TODO) lands on the [diode](./Diodes.md), it strikes off an [electron](TODO) from the [nucleus](TODO) it is attached to. If this happens inside or close to the [depletion region](#p-n%20Diodes), the [electrons](TODO) move from the [n-layer](#p-n%20Diodes) ([cathode](./Diodes.md)) to the [p-layer](#p-n%20Diodes) ([anode](./Diodes.md)) which causes a [current](../../Current.md) $I_L$ opposite the direction in which the [diode](./Diodes.md) is supposed to let [current](../../Current.md) through. Thus, the overall [current](../../Current.md) flowing through the [diode](./Diodes.md) is reduced.

In the absence of [light](TODO), [photodiodes](#Photodiodes) behave very similarly to [p-n diodes](#p-n%20Diodes) but their [V-I characteristics](../../../index.md#V-I%20Characteristic). 

>[!DEFINITION] Definition: Dark Current
>
>The **dark current** $I_D$ of a [photodiode](#Photodiodes) is the [current](../../Current.md) which flows through it in the absence of [light](TODO).
>

When [light](TODO) of sufficient [frequency](TODO) is present, the [V-I characteristic](../../../index.md#V-I%20Characteristic) is shifted downwards due to the [current](../../Current.md) $I_L$ in the opposite direction:

>[!THEOREM] Theorem: V-I Characteristics of Photodiodes
>
>The [V-I characteristic](../../../index.md#V-I%20Characteristic) of a [photodiodes](#Photodiodes) is given by
>
>$$
>I(t) = I = |I_S| \left(\mathrm{e}^{\frac{U(t)}{U_T}} - 1\right) - |I_L(t)|,
>$$
>
>where $U_T$ is the [thermal voltage](#p-n%20Diodes) of the [diode](#Photodiodes).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!NOTATION] Notation
>
>In circuit diagrams, [photodiodes](./Diodes.md) are denoted by
>
>![Photodiode Symbol](../../Network%20Analysis/One-Ports/res/Photodiode%20Symbol.svg)
>

[Photodiodes](#Photodiodes) are used as [light](TODO) sensors whenever they are operated above $U_{\text{threshold}}$ and as solar cells for producing energy when operated below $U_{\text{threshold}}$.

## Tunnel Diodes

**Tunnel diodes** are special [diodes](./Diodes.md) which for certain [voltage](TODO) regions can exhibit a decrease in [current](../../Current.md) for an increase in [voltage](TODO).

![Tunnel Diode V-I Characteristic](../../Network%20Analysis/One-Ports/res/Tunnel%20Diode%20V-I%20Characteristic.svg)

>[!NOTATION] Notation
>
>In circuit diagrams, [tunnel diodes](#Tunnel%20Diodes) are denoted by
>
>![Tunnel Diode Symbol](../../Network%20Analysis/One-Ports/res/Tunnel%20Diode%20Symbol.svg)
>