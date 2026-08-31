---
tags:
    - analog-circuits
    - electrical-engineering
---

# Circulators

## Theoretical Model

>[!DEFINITION] Definition: Circulator
>
>TODO
>
>>[!NOTATION]
>>
>>The following symbol is used for the [circulator](#Theoretical%20Model):
>>
>>![Circulator Symbol](./res/Circulator%20Symbol.svg)
>>
>

>[!THEOREM] Theorem: Linearity
>
>Every [circulator](#Theoretical%20Model) is [linear](../Network%20Analysis/Strictly%20Linear%20Multiports.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Explicit Representations
>
>If a [circulator](#Theoretical%20Model) has [characteristic admittance](#Theoretical%20Model) $G$, then it has the following [admittance representation](../Network%20Analysis/Strictly%20Linear%20Multiports.md):
>
>$$
>\boldsymbol{i} = \boldsymbol{Y}\boldsymbol{v} \qquad \boldsymbol{Y} = \begin{bmatrix} 0 & G & -G \\ -G & 0 & G \\ G & -G & 0\end{bmatrix}
>$$
>
>If a [circulator](#Theoretical%20Model) has [characteristic impedance](#Theoretical%20Model) $R$, then it has the following [impedance representation](../Network%20Analysis/Strictly%20Linear%20Multiports.md):
>
>$$
>\boldsymbol{v} = \boldsymbol{Z}\boldsymbol{i} \qquad \boldsymbol{Z} = \begin{bmatrix} 0 & R & -R \\ -R & 0 & R \\ R & -R & 0\end{bmatrix}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Passivity
>
>Every [circulator](./Circulators.md) is [passive](../Network%20Analysis/Ports.md#Power).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Losslessness
>
>Every [circulator](./Circulators.md) is [lossless](../Network%20Analysis/Ports.md#Power).
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Implementation

>[!EXAMPLE] Example: Circulator via Gyrator
>
>A [circulator](./Circulators.md) can be easily implemented using a [gyrator](./Immittance%20Converters/Gyrators.md):
>
>![Circulator from Gyrator](./res/Circulator%20from%20Gyrator.svg)
>