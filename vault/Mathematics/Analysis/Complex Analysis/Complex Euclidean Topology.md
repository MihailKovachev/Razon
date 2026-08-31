---
tags:
    - complex-analysis
    - analysis
    - topology
    - mathematics
---

# Complex Euclidean Topology

A 

>[!THEOREM] Theorem: Topology of the Complex Plane
>
>The [function](../Functions/Functions.md) $d: \mathbb{C} \times \mathbb{C} \to \mathbb{R}$ defined as
>
>$$
>d(z_1, z_2) = |z_2 - z_1|
>$$
>
>is a [metric](../../Topology/Metric%20Spaces/Metric%20Spaces.md) on the [complex numbers](../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!NOTE]
>>
>>As a metric, $d$ induces a [topology](../../Topology/Metric%20Spaces/Metric%20Spaces.md#The%20Metric%20Topology) on $\mathbb{C}$ and, unless otherwise specified, all topology-related terminology relates to this induced topology.
>>
>


>[!DEFINITION] Definition: $r$-Neighborhood
>
>Let $r \gt 0$ and $z \in \mathbb{R}$.
>
>The $r$-**neighborhood** of $z$ is the [open ball](../../../index.md) $B_r(z)$, i.e. 
>
>$$
>B_r(z) = \{x \in \mathbb{C} \mid |x - z| \lt r\}
>$$
>

>[!DEFINITION] Definition: Deleted $r$-Neighborhood
>
>Let $r \gt 0$ and $z \in \mathbb{R}$.
>
>The **deleted** $r$**-neighborhood** of $z$ is its $r$-[neighborhood](./Complex%20Euclidean%20Topology.md) without $z$ itself:
>
>$$
>B_r(z) \setminus \{z\} = \{x \in \mathbb{C} \mid 0 \lt |x - z| \lt r \}
>$$
>

>[!THEOREM] Theorem: Boundary and Interior of Neighborhoods
>
>Let $r \gt 0$ and $z \in \mathbb{C}$.
>
>The [boundary](../../Topology/Interior,%20Boundary,%20Exterior.md) of the $r$-[neighborhood](#Neighborhoods) and the deleted $r$-[neighborhood](#Neighborhoods) of $z$ is the disk
>
>$$
>\{ x \in \mathbb{C} \mid |x - z| = r \}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>