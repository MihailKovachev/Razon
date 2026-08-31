---
tags:
    - network-analysis
    - electrical-engineering
---

# Node-Voltage Analysis

**Node-voltage analysis** is a technique for finding a [basis](../../../Mathematics/Algebra/Vector%20Spaces/Hamel%20Bases.md) for [Kirchhoff's current laws](../Lumped%20Circuits.md) within a given [electronic circuit](../../Electronic%20Circuits.md) as well as a way to express the [branch voltages](../Lumped%20Networks.md) inside it in terms of [voltages](TODO) with respect to a chosen reference.

>[!ALGORITHM] Algorithm: Node-Voltage Analysis
>
>1. Construct a [network graph](../Lumped%20Networks.md) $\mathcal{G} = (B, N, s, t)$ of the [circuit](../../Electronic%20Circuits.md).
>2. Pick some [node](../../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md) $\mathcal{N} \in N$ as a reference.
>3. Construct the [incidence matrix](../../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md) of $\mathcal{G}$ but remove the row corresponding to $\mathcal{N}$.
>
>>[!DEFINITION] Definition: Reduced Incidence Matrix
>>
>>The result from step 3 is known as the **reduced incidence matrix**.
>>
>>>[!NOTATION]
>>>
>>>$$\boldsymbol{A}$$
>>>
>>
>
>4. The [homogenous system](../../../Mathematics/Algebra/Linear%20Algebra/Systems%20of%20Linear%20Equations/Systems%20of%20Linear%20Equations.md) obtained by the [product](../../../Mathematics/Algebra/Matrices/Matrix%20Operations.md#Matrix%20Product) of $\boldsymbol{A}$ and the [branch current vector](../Lumped%20Networks.md) $\boldsymbol{i}$ is a [basis](../../../Mathematics/Algebra/Vector%20Spaces/Hamel%20Bases.md) for all instances of [Kirchhoff's current law](../Lumped%20Circuits.md) in the original [circuit](../../Electronic%20Circuits.md):
>
>$$\boldsymbol{A}\boldsymbol{i} = \boldsymbol{0}$$
>
>5. For each [node](../../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md) $n_j \in N \setminus \mathcal{N}$, define the **node-voltage** $v_{\text{k}, j}$ as the [potential difference](TODO)  $v_{\text{k},j} = \phi_j - \phi_{\mathcal{N}}$.
>
>6. Multiplying the [transpose](../../../Mathematics/Algebra/Matrices/Matrix%20Operations.md#Transposition) of $\boldsymbol{A}$ by the [vector](../../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) of [node-voltages](./Node%20Voltage%20Analysis.md) results in the [branch voltage vector](../Lumped%20Networks.md):
>
>$$\boldsymbol{v} = \boldsymbol{A}^{\mathsf{T}}\boldsymbol{v}_{\text{k}}$$
>
>>[!EXAMPLE]- Example
>>
>>Consider an [electronic circuit](../../Electronic%20Circuits.md) with the following [network graph](../Lumped%20Networks.md):
>>
>>![Analysis Example Graph](./res/Analysis%20Example%20Graph.svg)
>>
>>We construct the [incidence matrix](../../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md):
>>
>>$$\begin{bmatrix} +1 & +1 & 0 & 0 & 0 & 0 & 0 \\ -1 & 0 & +1 & +1 & 0 & 0 & 0 \\ 0 & -1 & -1 & 0 & +1 & 0 & 0 \\ 0 & 0 & 0 & -1 & -1 & -1 & -1 \\ 0 & 0 & 0 & 0 & 0 & +1 & +1 \end{bmatrix}$$
>>
>>We choose [node](../../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md) 4 as reference and remove the corresponding row to obtain the [reduced incidence matrix](./Node%20Voltage%20Analysis.md):
>>
>>$$\boldsymbol{A} = \begin{bmatrix}+1 & +1 & 0 & 0 & 0 & 0 & 0 \\ -1 & 0 & +1 & +1 & 0 & 0 & 0 \\ 0 & -1 & -1 & 0 & +1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & +1 & +1 \end{bmatrix}$$
>>
>>From $\boldsymbol{A}\boldsymbol{i} = \boldsymbol{0}$, we obtain a [basis](../../../Mathematics/Algebra/Vector%20Spaces/Hamel%20Bases.md) for the [Kirchhoff's current laws](../Lumped%20Circuits.md):
>>
>>$$\left\vert\begin{aligned} i_1 + i_2 & = 0 \\ -i_1 + i_3 + i_4 & = 0 \\ -i_2 - i_3 + i_5 & = 0\\ i_6 + i_7 & = 0 \end{aligned}\right.$$
>>
>>We now define the [node-voltages](./Node%20Voltage%20Analysis.md):
>>
>>![Node Voltages Example](./res/Node%20Voltages%20Example.svg)
>>
>>Multiplying $\boldsymbol{A}^{\mathsf{T}}$ by the [vector](../../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) of [node-voltages](./Node%20Voltage%20Analysis.md) results in the [branch voltage vector](../Lumped%20Networks.md):
>>
>>$$\boldsymbol{v} = \boldsymbol{A}^{\mathsf{T}}\begin{bmatrix} \vert \\ \boldsymbol{v}_{\text{k}} \\ \vert \end{bmatrix} = \begin{bmatrix} +1 & -1 & 0 & 0 \\ +1 & 0 & -1 & 0 \\ 0 & +1 & -1 & 0 \\ 0 & +1 & 0 & 0 \\ 0 & 0 & +1 & 0 \\ 0 & 0 & 0 & +1 \\ 0 & 0 & 0 & +1 \end{bmatrix} \begin{bmatrix} v_{\text{k},1} \\ v_{\text{k},2} \\ v_{\text{k},3} \\ v_{\text{k},5} \end{bmatrix}$$
>>
>>$$\left\vert\begin{aligned} v_1 & = v_{\text{k},1} - v_{\text{k},2} \\ v_2 &= v_{\text{k},1} - v_{\text{k},3} \\ v_3 &= v_{\text{k},2} - v_{\text{k},3} \\ v_4 & = v_{\text{k},2} \\ v_5 & = v_{\text{k},3} \\ v_6 & = v_{\text{k},5} \\ v_7 & = v_{\text{k},5} \end{aligned}\right.$$
>>
>

## Reduced Node-Voltage Analysis

When a [network](../Lumped%20Networks.md) contains only [voltage-controlled](../Lumped%20Elements.md) [elements](../Lumped%20Elements.md), the [branch current vector](../Lumped%20Networks.md) can be expressed in terms of the [branch voltage vector](../Lumped%20Networks.md) in the following way:

$$\boldsymbol{i} = g(\boldsymbol{v})$$

If we use [node-voltage analysis](./Node%20Voltage%20Analysis.md), we can construct a system of equations in terms of the [node voltages](./Node%20Voltage%20Analysis.md) and the [reduced incidence matrix](./Node%20Voltage%20Analysis.md):

$$\boldsymbol{A} g(\boldsymbol{A}^{\mathsf{T}}\boldsymbol{v}_{\text{k}}) = \boldsymbol{0}$$

Solving this system yields the [node voltages](./Node%20Voltage%20Analysis.md) and subsequently the [branch currents](../Lumped%20Networks.md) and [branch voltages](../Lumped%20Networks.md).

Moreover, if the [elements](../Lumped%20Elements.md) are also [affine](TODO), the [branch current vector](../Lumped%20Networks.md) can be expressed in terms of the [branch voltage vector](../Lumped%20Networks.md) in the following way:

$$\boldsymbol{i} = -\boldsymbol{N}^{-1}\boldsymbol{M}\boldsymbol{v} + \boldsymbol{N}^{-1}\boldsymbol{e}$$

The aforementioned system can then be written as

$$\boldsymbol{G}_{k}\boldsymbol{v}_{\text{k}} = \boldsymbol{i}_{\text{q}},$$

where $\boldsymbol{G}_k = -\boldsymbol{A}\boldsymbol{N}^{-1}\boldsymbol{M}\boldsymbol{A}^{\mathsf{T}}$ is called the **node admittance matrix** and $\boldsymbol{i}_{\text{q}} = -\boldsymbol{A}\boldsymbol{N}^{-1}\boldsymbol{e}$ is known as the **node current source vector**.

>[!THEOREM] Theorem: Node Current Source Vector
>
>The $k$-th component of the [node current source vector](#Reduced%20Node%20Voltage%20Analysis) $\boldsymbol{i}_{\text{q}}$ (skipping reference) is the algebraic sum of all [currents](../../Current.md) which are flowing into or out of the corresponding [node](./Node%20Voltage%20Analysis.md) and are caused by [ideal current sources](../../Analog%20Circuits/Sources.md#Ideal%20Current%20Sources), where in-flowing [currents](../../Current.md) are positive and out-flowing [currents](../../Current.md) are negative.
>
>>[!EXAMPLE]-
>>
>>![Reduced Node Voltage Analysis Source Vector](./res/Reduced%20Node%20Voltage%20Analysis%20Source%20Vector.svg)
>>
>>$$\boldsymbol{i}_{\text{q}} = \begin{bmatrix}I_{\text{CS},1} - I_{\text{CS},2} \\ -I_{\text{CS},1}\end{bmatrix}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!ALGORITHM] Algorithm: Node Admittance Matrix
>
>Initialize the [node admittance matrix](#Reduced%20Node%20Voltage%20Analysis) to zero.
>
>If a [branch current](../Lumped%20Networks.md) $i_{\alpha \to \beta}$ (flowing out of the [node](../Lumped%20Networks.md) $\alpha$ into the [node](../Lumped%20Networks.md) $\beta$) is given by the [node voltages](./Node%20Voltage%20Analysis.md) $v_{\text{k},\gamma}$ and $v_{\text{k},\delta}$ as
>
>$$i_{\alpha \to \beta} = g\cdot (v_{\text{k},\gamma} - v_{\text{k},\delta}),$$
>
>then $g$ contributes to the elements $g_{i,j}$ of the [node admittance matrix](#Reduced%20Node%20Voltage%20Analysis) as follows:
>
>- Add $g$ to row $\alpha$, column $\gamma$ and to row $\beta$, column $\delta$.
>
>$$\begin{aligned}g_{\alpha, \gamma} & \leftarrow g_{\alpha, \gamma} + g \\ g_{\beta, \delta} & \leftarrow g_{\beta, \delta} + g\end{aligned}$$
>
>- Subtract $g$ from row $\alpha$, column $\delta$ and from row $\beta$, column $\gamma$.
>
>$$\begin{aligned}g_{\alpha, \delta} & \leftarrow g_{\alpha, \delta} - g \\ g_{\beta, \gamma} & \leftarrow g_{\beta, \gamma} - g\end{aligned}$$
>
>- If $\alpha$, $\beta$, $\gamma$ or $\delta$ is the reference, then do not perform the operations in which it participates.
>
