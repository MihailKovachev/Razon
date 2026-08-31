---
title: Nullors
tags:
    - circuit-theory
    - electrical-engineering
---

# Nullors

>[!DEFINITION] Definition: Nullor
>
>A **nullor** is a [strictly linear two-port](./Linear%20Two-Ports.md#Strictly%20Linear%20Two-Ports) which has the following [implicit representation](../Ports.md#Representations):
>
>$$
>\begin{bmatrix}1 & 0 \\ 0 & 0\end{bmatrix}\boldsymbol{v} + \begin{bmatrix}0 & 0 \\ 1 & 0\end{bmatrix}\boldsymbol{i} = \boldsymbol{0}
>$$
>
>>[!NOTATION]
>>
>>The symbol for the [nullor](./Nullors.md) is the following:
>>
>>![Nullor Symbol](./res/Nullor%20Symbol.svg)
>>
>>It looks like this because a [nullor](./Nullors.md) is equivalent to a [nullator](../../Analog%20Circuits/Nullators.md) and a [norator](../../Analog%20Circuits/Norators.md), since $v_1 = 0$ and $i_1 = 0$, but we don't know anything about $v_2$ and $i_2$.
>

>[!INFO] Info: Transmission Representation
>
>The [transmission representation](./Two-Ports.md#Representations) of the [nullor](./Nullors.md) is the following:
>
>$$
>\begin{bmatrix}v_1 \\ i_1\end{bmatrix} = \boldsymbol{T} \begin{bmatrix}v_2 \\ -i_2\end{bmatrix} \qquad \boldsymbol{T} = \begin{bmatrix}0 & 0 \\0 & 0\end{bmatrix}
>$$
>
>It is the *only* [explicit representation](./Two-Ports.md#Representations) which exists for the [nullor](./Nullors.md). 
>