---
tags:
    - network-analysis
    - electrical-engineering
---

# Tableau Analysis

Once we have a [basis](../../../Mathematics/Algebra/Vector%20Spaces/Hamel%20Bases.md) for all instances of [Kirchhoff's laws](../Lumped%20Circuits.md) within a given [network](../Lumped%20Networks.md) and we know the [characteristics](../Lumped%20Elements.md) of its [elements](../Lumped%20Elements.md), we can construct a system of equations which describes the behavior of the [network](../Lumped%20Networks.md).

>[!DEFINITION] Definition: Tableau System
>
>A **tableau system** of a [network](../Lumped%20Networks.md) is a system of equations which completely describes it.
>

>[!ALGORITHM] Algorithm: Tableau Analysis
>
>**Tableau analysis** is the process of finding a [tableau system](./Tableau%20Analysis.md) for a given [network](../Lumped%20Networks.md):
>
>1. Construct a [network graph](../Lumped%20Networks.md).
>
>2. Find a [basis](../../../Mathematics/Algebra/Vector%20Spaces/Hamel%20Bases.md) for all [KVLs](../Lumped%20Circuits.md) in the [network](../Lumped%20Networks.md) and write it in the form $\boldsymbol{B}\boldsymbol{v} = \boldsymbol{0}$ .
>    - [Fundamental loop analysis](./Fundamental%20Loop%20and%20Cut-Set%20Analysis.md) or [mesh-current analysis](./Mesh%20Current%20Analysis.md) can be used for this.
>
>3. Find a [basis](../../../Mathematics/Algebra/Vector%20Spaces/Hamel%20Bases.md) for all [KCLs](../Lumped%20Circuits.md) in the [network](../Lumped%20Networks.md) and write it in the form $\boldsymbol{A}\boldsymbol{i} = \boldsymbol{0}$.
>    - [Fundamental cut-set analysis](./Fundamental%20Loop%20and%20Cut-Set%20Analysis.md) or [node-voltage analysis](./Node%20Voltage%20Analysis.md) can be used for this.
>
>4. Combine the [implicit representations](TODO) of all [electrical elements](../Lumped%20Elements.md) into a single $f(\boldsymbol{v},\boldsymbol{i}) = \boldsymbol{0}$ by using the [branch voltage vector](../Lumped%20Networks.md) and [branch current network](../Lumped%20Networks.md).
>
>5. Combine the results from the previous steps to obtain a [tableau system](./Tableau%20Analysis.md):
>
>$$
>\left\vert \begin{aligned}\boldsymbol{B}\boldsymbol{v} & = \boldsymbol{0} \\ \boldsymbol{A}\boldsymbol{i} & = \boldsymbol{0} \\ f(\boldsymbol{v},\boldsymbol{i}) & = \boldsymbol{0}\end{aligned}\right.
>$$
>
>    - The first part can also be written in [matrix](../../../Mathematics/Algebra/Matrices/Matrices.md) form:
>
>$$
>\left\vert \begin{aligned} \begin{bmatrix} \boldsymbol{B} & \boldsymbol{0} \\ \boldsymbol{0} & \boldsymbol{A} \end{bmatrix} \begin {bmatrix}\boldsymbol{v} \\ \boldsymbol{i}\end{bmatrix} & = \boldsymbol{0} \\ f(\boldsymbol{v},\boldsymbol{i}) & = \boldsymbol{0}\end{aligned}\right.
>$$
>
>>[!INFO] Info: Non-Existent Implicit Representation
>>
>>Theoretically, it might be possible for some [elements](../Lumped%20Elements.md) to not have an [implicit representation](../Lumped%20Elements.md). 
>>
>

## Affine Networks

If a [network](../Lumped%20Networks.md) contains only [affine](TODO) [elements](../Lumped%20Elements.md), their [characteristics](../Lumped%20Elements.md) can be combined into a single [matrix](../../../Mathematics/Algebra/Matrices/Matrices.md) equation of the following form:

$$
\boldsymbol{M}\boldsymbol{v} + \boldsymbol{N}\boldsymbol{i} = \boldsymbol{e}
$$

We can then construct a [tableau system](./Tableau%20Analysis.md) of the following form:

$$
\begin{bmatrix} \boldsymbol{B} & \boldsymbol{0} \\ \boldsymbol{0} & \boldsymbol{A} \\ \boldsymbol{M} & \boldsymbol{N} \end{bmatrix} \begin {bmatrix}\boldsymbol{v} \\ \boldsymbol{i}\end{bmatrix} = \begin{bmatrix}\boldsymbol{0} \\ \boldsymbol{0} \\ \boldsymbol{e}\end{bmatrix}
$$

>[!DEFINITION] Definition: Tableau Matrix
>
>The [matrix](../../../Mathematics/Algebra/Matrices/Matrices.md)
>
>$$
>\begin{bmatrix} \boldsymbol{B} & \boldsymbol{0} \\ \boldsymbol{0} & \boldsymbol{A} \\ \boldsymbol{M} & \boldsymbol{N} \end{bmatrix}
>$$
>
>is known as a **tableau matrix**.
>
>>[!NOTATION]
>>
>>$$
>>\boldsymbol{T}
>>$$
>>
>

>[!EXAMPLE]- Example: Tableau Analysis of Affine Networks
>
>Consider the following [network](../Lumped%20Networks.md):
>
>![Tableau Analysis Affine Circuit](./res/Tableau%20Analysis%20Affine%20Circuit.svg)
>
>We use [fundamental loop and cut-set analysis](./Fundamental%20Loop%20and%20Cut-Set%20Analysis.md) to find a [basis](../../../Mathematics/Algebra/Vector%20Spaces/Hamel%20Bases.md) for [Kirchhoff's laws](../Lumped%20Circuits.md):
>
>![Affine Tableau Analysis Graph](./res/Affine%20Tableau%20Analysis%20Graph.svg)
>
>$$
>\left\vert \begin{aligned}-v_1 + v_2 + v_5 & = 0 \\ v_2 - v_3 + v_6 & = 0 \\ -v_4 + v_7 & = 0\end{aligned}\right. \implies \begin{bmatrix}-1 & 1 & 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & -1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \\ v_3 \\ v_4 \\ v_5 \\ v_6 \\ v_7 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}
>$$
>
>$$
>\left\vert \begin{aligned}i_1 + i_5 = 0 \\ i_2 - i_5 - i_6 = 0 \\ i_3 + i_6 = 0 \\ i_4 + i_7 = 0 \end{aligned}\right. \implies \begin{bmatrix} 1 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & -1 & -1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} i_1 \\ i_2 \\ i_3 \\ i_4 \\ i_5 \\ i_6 \\ i_7 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}
>$$
>
>We get the following from the [elements](../Lumped%20Elements.md):
>- $v_1 = v_0$ from the [voltage source](../../Analog%20Circuits/Sources.md#Ideal%20Voltage%20Sources);
>- $i_5 = 0$ and $v_5 = 0$ from the [nullator](../../Analog%20Circuits/Nullators.md);
>- $v_2 - R_{\text{e}}i_2 = 0$ from the [resistor](../../Analog%20Circuits/Resistors.md#Linear%20Resistors) $R_{\text{e}}$;
>- $v_3 - Nv_4 = 0$ and $Ni_3 + i_4 = 0$ from the [transformer](../../Analog%20Circuits/Immittance%20Converters/Transformers.md);
>- $v_7 - R_{\text{L}}i_7 = 0$ from the [resistor](../../Analog%20Circuits/Resistors.md#Linear%20Resistors) $R_{\text{L}}$.
>
>
>We can write these in the form
>
>$$
>\boldsymbol{M}\boldsymbol{v} + \boldsymbol{N}\boldsymbol{i} = \boldsymbol{0},
>$$
>
>where
>
>$$
>\begin{aligned}
>\boldsymbol{M} & = \begin{bmatrix} 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & -N & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 \end{bmatrix} \\ \boldsymbol{N} & = \begin{bmatrix} 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & -R_{\text{e}} & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & N & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & -R_{\text{L}} \end{bmatrix} \\ \boldsymbol{e} & = \begin{bmatrix} v_0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}
>\end{aligned}
>$$
>
>Combining all results, we get the following [tableau system](./Tableau%20Analysis.md):
>
>TODO
>

## Non-Affine Networks

For [networks](../Lumped%20Networks.md) which contain both [affine](TODO) and non-[affine](TODO) [elements](../Lumped%20Elements.md), we can combine the [characteristics](../Lumped%20Elements.md) of the [affine](TODO) [elements](../Lumped%20Elements.md) as before and combine the [characteristics](../Lumped%20Elements.md) of the non-[affine](TODO) [elements](../Lumped%20Elements.md) into $f_{\text{non-affine}} (\boldsymbol{v}, \boldsymbol{i}) = \boldsymbol{0}$. 

We can then construct a [tableau system](./Tableau%20Analysis.md) of the following form:

$$
\left\vert \begin{aligned} \begin{bmatrix} \boldsymbol{B} & \boldsymbol{0} \\ \boldsymbol{0} & \boldsymbol{A} \\ \boldsymbol{M}' & \boldsymbol{N}' \end{bmatrix} \begin {bmatrix}\boldsymbol{v} \\ \boldsymbol{i}\end{bmatrix} & = \begin{bmatrix}\boldsymbol{0} \\ \boldsymbol{0} \\ \boldsymbol{e}'\end{bmatrix} \\ f_{\text{non-affine}} (\boldsymbol{v}, \boldsymbol{i}) & = \boldsymbol{0} \end{aligned}\right.
$$