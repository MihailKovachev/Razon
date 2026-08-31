---
tags:
    - network-analysis
    - electrical-engineering
---

# Lumped Elements

>[!DEFINITION] Definition: Lumped Element
>
>An $n$**-terminal lumped element** is a [dynamical system with latent variables](../../Mathematics/Systems%20Theory/Dynamical%20Systems.md) $(\mathbb{T}, \mathbb{W})$
>

>[!DEFINITION] Definition: Electrical Element
>
>An $n$-**terminal electrical element** is an abstract mathematical model of a [lumped](./Lumped%20Circuits.md) [electronic (sub)circuit](../Electronic%20Circuits.md) with $n$ accessible [terminals](../Electronic%20Circuits.md).
>
>>[!DEFINITION] Definition: Inputs and Outputs
>>
>>Some of the $n$ [terminals](../Electronic%20Circuits.md) may be called **inputs** and others may be called **outputs**.
>>
>

>[!DEFINITION] Definition: Current Vector
>
>The **current vector** of an $n$[-terminal network](./Lumped%20Elements.md) at time $t$ is defined as the [vector](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) whose components are the [currents](../Current.md) flowing [into](./Reference%20Directions.md) the $n$ [terminals](../Electronic%20Circuits.md) at time $t$:
>
>$$
>\begin{bmatrix} i_1(t) \\ \vdots \\ i_n(t) \end{bmatrix}
>$$
>
>>[!NOTATION]
>>
>>$$
>>\boldsymbol{i}(t) \qquad \mathbf{i}(t)
>>$$
>>
>

>[!DEFINITION] Definition: Potential Vector
>
>The **potential vector** of an $n$[-terminal network](./Lumped%20Elements.md) at time $t$ is defined as the [vector](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) whose components are the [electrostatic potentials](TODO) at the $n$ [terminals](../Electronic%20Circuits.md) at time $t$:
>
>$$
>\begin{bmatrix} \varphi_1(t) \\ \vdots \\ \varphi_n(t) \end{bmatrix}
>$$
>

>[!DEFINITION] Definition: Voltage Vector
>
>The **voltage vector** of an $n$[-terminal network](./Lumped%20Elements.md) at time $t$ is defined as the [vector](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) whose components are the [voltages](TODO) between the [terminals](../Electronic%20Circuits.md) and some reference point at time $t$:
>
>$$
>\begin{bmatrix} v_1(t) \\ \vdots \\ v_n(t) \end{bmatrix}
>$$
>
>Most commonly, this reference point is taken to be one of the [terminals](../Electronic%20Circuits.md).
>
>>[!NOTATION]
>>
>>$$
>>\boldsymbol{v}(t) \qquad \mathbf{v}(t)
>>$$
>>
>

## I-V Characteristic

>[!DEFINITION] Definition: I-V Characteristic
>
>The **I-V characteristic** of an $n$[-terminal network](./Lumped%20Elements.md) at time $t$ is the [set](../../Mathematics/Set%20Theory/Sets.md) $\mathcal{F}(t) \subseteq \mathbb{R}^{2n}$ of all pairs $(\boldsymbol{v}, \boldsymbol{i})$ of a [voltage vector](./Lumped%20Elements.md) and a [current vector](./Lumped%20Elements.md) which the [network](./Lumped%20Elements.md) is allowed to have at time $t$.
>



