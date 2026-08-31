---
tags:
    - network-analysis
    - electrical-engineering
---

# Lumped Networks

A **lumped network** is a general name for the model of a [lumped circuit](./Lumped%20Circuits.md).



## Network Graphs

>[!DEFINITION] Definition: Network Graph
>
>The **network graph** of an [electronic circuit](../Electronic%20Circuits.md) is a [directed multigraph](../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md) which represents the physical structure of the [circuit](../Electronic%20Circuits.md).
>
>>[!NOTATION]
>>
>>We often denote the [number](../../Mathematics/Set%20Theory/Cardinality.md) of [branches](../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md) by $b$ and the [number](../../Mathematics/Set%20Theory/Cardinality.md) of [nodes](../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md) by $n$.
>>
>

>[!DEFINITION] Definition: Branch Voltage Vector
>
>Let $\mathcal{G} = (N, B, s, t)$ be a [network graph](./Lumped%20Networks.md).
>
>The **branch voltage vector** is the [vector](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) whose components are the [voltages](TODO) across $\mathcal{G}$'s [branches](../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md):
>
>$$
>\boldsymbol{v} \overset{\text{def}}{=} \begin{bmatrix}v_1 \\ \vdots \\ v_b\end{bmatrix} \in \mathbb{R}^{b}
>$$
>

>[!DEFINITION] Definition: Branch Current Vector
>
>Let $\mathcal{G} = (N, B, s, t)$ be a [network graph](./Lumped%20Networks.md).
>
>The **branch current vector** is the [vector](../../Mathematics/Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) whose components are the [currents](../Current.md) flowing along $\mathcal{G}$'s [branches](../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Directed%20Multigraphs.md):
>
>$$
>\boldsymbol{i} \overset{\text{def}}{=} \begin{bmatrix}i_1 \\ \vdots \\ i_b\end{bmatrix} \in \mathbb{R}^{b}
>$$
>

The [network graph](./Lumped%20Networks.md) must be constructed in a specific way:



>[!THEOREM] Tellegen's Theorem
>
>Let $\mathcal{G}$ be a [network graph](./Lumped%20Networks.md).
>
>If $\boldsymbol{v}(t)$ is the [branch voltage vector](./Lumped%20Networks.md) of $\mathcal{G}$ at some time $t$ and $\boldsymbol{i}(t^{\ast})$ is the [branch current vector](./Lumped%20Networks.md) of $\mathcal{G}$ at some time $t^{\ast}$, then $\boldsymbol{v}(t)$ and $\boldsymbol{i}(t^{\ast})$ are [orthogonal](../../Mathematics/Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md#Orthogonality):
>
>$$
>\boldsymbol{v}(t) \cdot \boldsymbol{i}(t^{\ast}) = 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Duality

>[!DEFINITION] Definition: Networks
>
>Let $\boldsymbol{v}$, $\boldsymbol{i}$ be the [branch voltage vector](#Network%20Topology) and [branch current vector](#Network%20Topology) of a [network](./Lumped%20Networks.md) $\mathcal{N}$ and let $\boldsymbol{v}^d$, $\boldsymbol{i}^d$ be the [branch voltage vector](#Network%20Topology) and [branch current vector](#Network%20Topology) of a [network](./Lumped%20Networks.md) $\mathcal{N}^d$.
>
>We say that $\mathcal{N}$ and $\mathcal{N}^d$ are **dual** if there exists some $R_d \in \mathbb{R}$ such that
>
>$$\boldsymbol{v}^d = R_d \boldsymbol{i} \qquad \boldsymbol{i}^d = \frac{1}{R_d}\boldsymbol{v}.$$
>

>[!ALGORITHM] Algorithm: Constructing Duals
>
>We are given a [planar](../../Mathematics/Graph%20Theory/Directed%20Multigraphs/Planarity.md) [network](./Lumped%20Networks.md) $\mathcal{N}$ and want to find its [dual](#Duality) $\mathcal{N}^d$ with respect to the [duality constant](#Duality) $R_d$.
>
>1. Every [mesh](TODO) in $\mathcal{N}$ corresponds to a [node](TODO) in $\mathcal{N}^d$.
>
>    - The outside of $\mathcal{N}$ also corresponds to a [node](TODO) in $\mathcal{N}^d$.
>
>2. If a [one-port](./One-Ports/One-Ports.md) in $\mathcal{N}$ is on the boundary between two [meshes](TODO) or a [mesh](TODO) and the outside, then its [dual](./One-Ports/One-Ports.md#Duality) is connected to the corresponding [dual nodes](TODO) in $\mathcal{N}^d$.
>
>3. Determine the directions for the dual currents and voltages:
>
>    - Assign an identical orientation to each [mesh](TODO) and the outside of $\mathcal{N}$ (either everything clockwise or everything counter-clockwise).
>    - Each [current](../Current.md) $i$ in $\mathcal{N}$ is adjacent to exactly two [meshes](TODO) or is adjacent to a [mesh](TODO) and the outside. The [dual](#Duality) $v^d$ points away from the [dual node](TODO) of the region whose orientation aligns with the direction of $i$ and points into the [dual node](TODO) the region whose orientation opposes the direction of $i$.
>    - Each [voltage](../../Physics/Classical%20Electromagnetism/Electric%20Potential.md) $v$ in $\mathcal{N}$ is adjacent to exactly two [meshes](TODO) or is adjacent to a [mesh](TODO) and the outside. The [dual](#Duality) $i^d$ points away from the [dual node](TODO) of the region whose orientation aligns with the direction of $v$ and points into the [dual node](TODO) of the region whose orientation opposes the direction of $v$.
>
