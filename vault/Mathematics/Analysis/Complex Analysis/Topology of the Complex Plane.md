---
title: Topology of the Complex Plane
tags:
    - complex-analysis
    - topology
    - mathematics
---

# Topology of the Complex Plane

>[!THEOREM] Theorem: Topology of the Complex Plane
>
>The function $d: \mathbb{C} \times \mathbb{C} \to \mathbb{R}$ defined as
>
>$$
>d(z_1, z_2) = |z_2 - z_1|
>$$
>
>is a [metric](../../Topology/Metric%20Spaces/index.md) on the [complex numbers](../../Algebra/Fields/The%20Complex%20Numbers/index.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!NOTE]
>>
>>As a metric, $d$ induces a [topology](../../Topology/Metric%20Spaces/index.md#The%20Metric%20Topology) on $\mathbb{C}$ and, unless otherwise specified, all topology-related terminology relates to this induced topology.
>>
>

## Neighborhoods

>[!DEFINITION] Definition: $r$-Neighborhood
>
>Let $r \gt 0$ and $z \in \mathbb{R}$.
>
>The $r$-**neighborhood** of $z$ is the [open ball](../../Topology/Metric%20Spaces/index.md) $B_r(z)$, i.e. 
>
>$$
>B_r(z) = \{x \in \mathbb{C} \mid |x - z| \lt r\}
>$$
>

>[!DEFINITION] Definition: Deleted $r$-Neighborhood
>
>Let $r \gt 0$ and $z \in \mathbb{R}$.
>
>The **deleted** $r$**-neighborhood** of $z$ is its $r$-[neighborhood](Topology%20of%20the%20Complex%20Plane.md) without $z$ itself:
>
>$$
>B_r(z) \setminus \{z\} = \{x \in \mathbb{C} \mid 0 \lt |x - z| \lt r \}
>$$
>

### Properties

>[!THEOREM] Theorem: Boundary and Interior of Neighborhoods
>
>Let $r \gt 0$ and $z \in \mathbb{C}$.
>
>The [boundary](../../Topology/Interior,%20Boundary,%20Exterior/Boundary.md) of the $r$-[neighborhood](Topology%20of%20the%20Complex%20Plane.md#Neighborhoods) and the deleted $r$-[neighborhood](Topology%20of%20the%20Complex%20Plane.md#Neighborhoods) of $z$ is the disk
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