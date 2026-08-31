---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Orthogonal Complements

>[!DEFINITION] Definition: Orthogonal Complement
>
>Let $U$ be a [linear subspace](../Linear%20Subspaces.md) of an [inner product space](./Inner%20Product%20Spaces.md) $(V, \langle \cdot, \cdot \rangle)$.
>
>The **orthogonal complement** of $U$ is the [set](../../../Set%20Theory/Sets.md) of all [vectors](../Vector%20Spaces.md) in $V$ which are [orthogonal](./Inner%20Product%20Spaces.md#Orthogonality) to each [vector](../Vector%20Spaces.md) in $U$.
>
>$$\{v\in V \mid \langle v, u\rangle = 0, \forall u\in U\}$$
>
>>[!NOTATION]
>>
>>$$U^{\perp}$$
>>
>

>[!THEOREM] Theorem: Direct Sum of Complements
>
>Let $(V, \langle \cdot, \cdot \rangle)$ be a [finite-dimensional](../Hamel%20Bases.md#Dimension) [inner product space](./Inner%20Product%20Spaces.md).
>
>If $U$ is a [linear subspace](../Linear%20Subspaces.md) of $V$, then $V$ is the [direct sum](../Linear%20Subspaces.md#Sum) of $U$ and its [orthogonal complement](./Orthogonal%20Complements.md) $U^{\perp}$:
>
>$$V = U \oplus U^{\perp}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Orthogonal Complement is Kernel of Orthogonal Projection
>
>If the [orthogonal projection](./Orthogonal%20Projections.md) $\pi_U$ onto a [linear subspace](../Linear%20Subspaces.md) $U$ exists, then the [orthogonal complement](./Orthogonal%20Complements.md) of $U$ is the [kernel](../../../Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md) of $\pi_U$:
>
>$$U^{\perp} = \ker \pi_U$$
>
>>[!PROOF]-
>>
>>TODO
>>
>