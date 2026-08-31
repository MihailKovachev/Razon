---
tags:
    - graph-theory
    - mathematics
---

# Cyclicity (Undirected Graphs)

>[!DEFINITION] Definition: Cycle
>
>A **cycle** in an [undirected graph](./Undirected%20Graphs.md) is a [walk](./Undirected%20Graphs.md)
>
>$$(v_0, e_1, v_1, e_2, v_2, \dotsc, e_k, v_k)$$
>
>of [length](./Undirected%20Graphs.md) $k \ge 3$ such that $v_0 = v_k$ and $v_i \ne v_j$ for all distinct $i, j \in \{0, \dotsc, k-1\}$.
>

>[!DEFINITION] Definition: Cyclicity
>
>An [undirected graph](./Undirected%20Graphs.md) is **cyclic** if it contains at least one [cycle](./Cyclicity%20(Undirected%20Graphs).md) and is **acyclic** otherwise.
>