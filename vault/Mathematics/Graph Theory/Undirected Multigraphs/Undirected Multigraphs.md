---
tags:
    - graph-theory
    - mathematics
---

>[!DEFINITION] Definition: Undirected Multigraph
>
>An **undirected multigraph** (or just **multigraph**) is a 3[-tuple](../../Set%20Theory/Tuples.md) $G = (V, E, \phi)$ consisting of the following:
>
>- a [set](../../Set%20Theory/Sets.md) $V$ whose elements are called **vertices** or **nodes**;
>- a [set](../../Set%20Theory/Sets.md) $E$ whose elements are called **edges** or **arcs**;
>- a [function](../../Analysis/Functions/Functions.md) $\phi: E \to \{\{x, y\} \mid x, y \in V\}$ called an **incidence function**.
>

>[!DEFINITION] Definition: Loop
>
>An [edge](./Undirected%20Multigraphs.md) $e$ in an [undirected multigraph](./Undirected%20Multigraphs.md) $(V, E, \phi)$ is a **loop** if $|\phi(e)| = 1$.
>