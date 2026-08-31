---
tags:
    - network-analysis
    - electrical-engineering
---

# Mesh Current Analysis

**Mesh current analysis** is a technique for finding a [basis](../../../Mathematics/Algebra/Vector%20Spaces/Hamel%20Bases.md) for [Kirchhoff's voltage laws](../Lumped%20Circuits.md) within an [electronic circuit](../../Electronic%20Circuits.md) as well as a way to express the [branch currents](../Lumped%20Networks.md) inside it in terms of other, fictitious [currents](../../Current.md).

>[!ALGORITHM] Algorithm: Mesh Current Analysis
>
>1. Construct a [planar](../../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Planarity.md) [network graph](../Lumped%20Networks.md) $\mathcal{G} = (B, N, s, t)$ of the [circuit](../../Electronic%20Circuits.md).
>2. Assign an orientation to each [mesh](TODO) in $\mathcal{G}$.
>3. Construct an a [matrix](../../../Mathematics/Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) whose rows correspond to the [meshes](TODO) and whose columns correspond to the [branches](../../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md) in $\mathcal{G}$ in the following way:
>
>$$b_{kj} = \begin{cases} +1 & \text{if branch } j \text{ is in mesh } k \text{ and their orientations are the same} \\ -1 & \text{if branch } j \text{ is in mesh } k \text{ and their orientations are opposite} \\ 0 & \text{if branch } j \text{ is not part of mesh } k \end{cases}$$
>
>>[!DEFINITION] Definition: Mesh Incidence Matrix
>>
>>The result from step 3 is known as a **mesh incidence matrix**.
>>
>>>[!NOTATION]
>>>
>>>$$\boldsymbol{B}$$
>>>
>>
>
>4. The [homogenous system](../../../Mathematics/Algebra/Linear%20Algebra/Systems%20of%20Linear%20Equations/Systems%20of%20Linear%20Equations.md) obtained by the [product](../../../Mathematics/Algebra/Matrices/Matrix%20Operations.md#Matrix%20Product) of $\boldsymbol{B}$ and the [branch voltage vector](../Lumped%20Networks.md) $\boldsymbol{v}$ is a [basis](../../../Mathematics/Algebra/Vector%20Spaces/Hamel%20Bases.md) for all instances of [Kirchhoff's voltage law](../Lumped%20Circuits.md) in the original [circuit](../../Electronic%20Circuits.md):
>
>$$\boldsymbol{B}\boldsymbol{v} = \boldsymbol{0}$$
>
>5. For each [mesh](TODO) $m_j$, define the **mesh current** $i_{m,j}$ as a fictitious [current](../../Current.md) circulating around the loop.
>
>6. Multiplying the [transpose](../../../Mathematics/Algebra/Matrices/Matrix%20Operations.md#Transposition) of $\boldsymbol{B}$ by the [vector](../../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) of [mesh currents](./Mesh%20Current%20Analysis.md) results in the [branch current vector](../Lumped%20Networks.md):
>
>$$\boldsymbol{i} = \boldsymbol{B}^{\mathsf{T}} \boldsymbol{i}_{\text{m}}$$
>
>    - The [branch current](../Lumped%20Networks.md) is given as the algebraic sum of the [mesh currents](./Mesh%20Current%20Analysis.md) of all [meshes](TODO) in which the [branch](../../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md) participates, where each [mesh current](./Mesh%20Current%20Analysis.md) is taken with a plus if its orientation is aligned with the [branch current](../Lumped%20Networks.md) and with a minus if their orientations are opposite.
>
>>[!EXAMPLE]- Example
>>
>>Consider an [electronic circuit](../../Electronic%20Circuits.md) with the following [network graph](../Lumped%20Networks.md):
>>
>>![Analysis Example Graph](./res/Analysis%20Example%20Graph.svg)
>>
>>There are three [meshes](TODO) inside and we can define the corresponding [mesh currents](./Mesh%20Current%20Analysis.md):
>>
>>![Mesh Currents Example](./res/Mesh%20Currents%20Example.svg)
>>
>>We now construct the [mesh incidence matrix](./Mesh%20Current%20Analysis.md):
>>
>>$$\boldsymbol{B} = \begin{bmatrix}+1 & -1 & +1 & 0 & 0 & 0 & 0 \\ 0 & 0 & -1 & 1 & -1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & +1 & -1\end{bmatrix}$$
>>
>>We now have a [basis](../../../Mathematics/Algebra/Vector%20Spaces/Hamel%20Bases.md) for [Kirchhoff's voltage laws](../Lumped%20Circuits.md):
>>
>>$$\boldsymbol{B}\boldsymbol{v} = \boldsymbol{0}$$
>>
>>$$\begin{bmatrix}+1 & -1 & +1 & 0 & 0 & 0 & 0 \\ 0 & 0 & -1 & 1 & -1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & +1 & -1\end{bmatrix}\begin{bmatrix}v_1 \\ v_2 \\ v_3 \\ v_4 \\ v_5 \\ v_6 \\ v_7 \end{bmatrix} = \begin{bmatrix}0 \\ 0 \\ 0\end{bmatrix}$$
>>
>>Multiplying $\boldsymbol{B}^{\mathsf{T}}$ by the [vector](../../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) of [mesh currents](./Mesh%20Current%20Analysis.md) results in the [branch current vector](../Lumped%20Networks.md):
>>
>>$$\boldsymbol{i} = \boldsymbol{B}^{\mathsf{T}} \begin{bmatrix}i_{\text{m1}} \\ i_{\text{m2}} \\ i_{\text{m3}}\end{bmatrix} = \begin{bmatrix} +1 & 0 & 0 \\ -1 & 0 & 0 \\ +1 & -1 & 0 \\ 0 & +1 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & +1 \\ 0 & 0 & -1 \end{bmatrix}\begin{bmatrix}i_{\text{m1}} \\ i_{\text{m2}} \\ i_{\text{m3}}\end{bmatrix}$$
>>
>>$$\left\vert\begin{aligned}i_1 & = i_{\text{m1}} \\ i_2 & = -i_{\text{m1}} \\ i_3 & = i_{\text{m1}} - i_{\text{m2}} \\ i_4 & = i_{\text{m2}} \\ i_5 & = -i_{\text{m2}} \\ i_6 & = i_{\text{m3}} \\ i_7 & = -i_{\text{m3}}\end{aligned}\right.$$
>>
>

## Reduced Mesh-Current Analysis

When a [network](../Lumped%20Networks.md) contains only [current-controlled](../Lumped%20Elements.md) [elements](../Lumped%20Elements.md), the [branch voltage vector](../Lumped%20Networks.md) can be expressed in terms of the [branch current vector](../Lumped%20Networks.md) in the following way:

$$\boldsymbol{v} = r(\boldsymbol{i})$$

If we use [mesh current analysis](./Mesh%20Current%20Analysis.md), we can construct a system of equations in terms of the [mesh currents](./Mesh%20Current%20Analysis.md) and the [mesh incidence matrix](./Mesh%20Current%20Analysis.md)

$$\boldsymbol{B} r(\boldsymbol{B}^{\mathsf{T}}\boldsymbol{i}_{\text{m}}) = \boldsymbol{0}$$

Solving this system yields the [mesh currents](./Mesh%20Current%20Analysis.md) and subsequently the [branch currents](../Lumped%20Networks.md) and [branch voltages](../Lumped%20Networks.md).

Moreover, if the [elements](../Lumped%20Elements.md) are also [affine](TODO), the [branch voltage vector](../Lumped%20Networks.md) can be expressed in terms of the [branch current vector](../Lumped%20Networks.md) in the following way:

$$\boldsymbol{v} = -\boldsymbol{M}^{-1}\boldsymbol{N}\boldsymbol{i} + \boldsymbol{M}^{-1}\boldsymbol{e}$$

The aforementioned system can then be written as

$$\boldsymbol{Z}_{m}\boldsymbol{i}_{\text{m}} = \boldsymbol{v}_{\text{q}},$$

where $\boldsymbol{Z}_m = -\boldsymbol{B}\boldsymbol{M}^{-1}\boldsymbol{N}\boldsymbol{B}^{\mathsf{T}}$ is called the **mesh impedance matrix** and $\boldsymbol{v}_{\text{q}} = -\boldsymbol{B}\boldsymbol{M}^{-1}\boldsymbol{e}$ is known as the **mesh voltage source vector**.