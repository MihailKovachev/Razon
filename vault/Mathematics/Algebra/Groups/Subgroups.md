---
tags:
    - group-theory
    - algebra
    - mathematics
---

# Subgroups

>[!DEFINITION] Definition: Subgroup
>
>Let $(G, \cdot)$ be a [group](../../../index.md) and let $S \subseteq G$.
>
>We say that $S$ is a **subgroup** of $(G, \cdot)$ if $S$ is itself a [group](../../../index.md) $(S, \cdot)$ under the operation $\cdot$.
>

>[!EXAMPLE]- Example: Trivial Subgroups
>
>Every [group](../../../index.md) is a [subgroup](./Subgroups.md) of itself. 
>
>If $e$ is the [identity element](../../../index.md) of a [group](../../../index.md), then $\{e\}$ is a [subgroup](./Subgroups.md) of it.
>

>[!EXAMPLE]- Example
>
>If $k \in \mathbb{N}_0$, then $\{kx \mid x \in \mathbb{Z}\}$ is a [subgroup](./Subgroups.md) of $(\mathbb{Z}, +)$.
>

>[!EXAMPLE]-
>
>If $a, b \in \mathbb{R}$, then $\{(xa, xb) \in \mathbb{R}^2 \mid x \in \mathbb{R}\}$  is a [subgroup](./Subgroups.md) of $(\mathbb{R}^2, +)$
>

>[!THEOREM] Theorem: Equivalent Definition
>
>Let $(G, \cdot)$ be a [group](../../../index.md) and let $S \subseteq G$.
>
>Then $(S, \cdot)$ is a [subgroup](./Subgroups.md) of $(G, \cdot)$ if and only if
>
>$$
>a, b \in S \implies a^{-1} \in S \qquad \text{and} \qquad ab \in S
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>