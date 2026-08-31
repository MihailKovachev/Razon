---
tags:
    - graph-theory
    - mathematics
---

# Cyclicity

>[!DEFINITION] Definition: Cycle
>
>A **cycle** in a [directed multigraph](./Directed%20Multigraphs.md) is a [walk](./Directed%20Multigraphs.md) 
>
>$$
>(v_0, e_1, v_1, e_2, v_2, \dotsc, e_k, v_k)
>$$
>
>of [length](./Directed%20Multigraphs.md) $k \ge 1$ such that $v_0 = v_k$ and $v_i \ne v_j$ for all distinct $i, j \in \{0, \dotsc, k-1\}$.
>

>[!DEFINITION] Definition: Cyclicity
>
>A [directed multigraph](./Directed%20Multigraphs.md) is **cyclic** if it contains at least one [cycle](./Cyclicity.md) and is **acyclic** otherwise.
>