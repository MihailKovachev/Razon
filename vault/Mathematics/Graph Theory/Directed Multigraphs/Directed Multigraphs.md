---
tags:
    - graph-theory
    - mathematics
---

# Directed Multigraphs

>[!DEFINITION] Definition: Directed Multigraphs
>
>A **directed multigraph** $G$ is a 3-[tuple](../../Set%20Theory/Tuples.md) $(V, E, \phi)$ consisting of the following:
>- a [set](../../Set%20Theory/Sets.md) $V$ whose elements are called **vertices** or **nodes**;
>- a [set](../../Set%20Theory/Sets.md) $E$ whose elements are called **edges** or **arcs**;
>- a [function](../../Analysis/Functions/Functions.md) $\phi: E \to V \times V$ called an **incidence function**.
>
>The [incidence function](./Directed%20Multigraphs.md) $\phi: E \to V \times V$ can be alternatively described by two [functions](../../Analysis/Functions/Functions.md)  $s: E \to V$ and $t: E \to V$ such that $\phi(e) = (s(e), t(e))$ for all $e \in E$:
>- We call $s$ the **source function**.
>- We call $t$ the **target function**.
>
>If $s(e) = t(e)$, then we say that $e$ is a **loop**.
>
>For $e \in E$ with $\phi(e) = (v_1, v_2)$:
>- We call $v_1$ the **source**, **tail** or **initial vertex** of $e$.
>- We call $v_1$ and $v_2$ the **head**, **target** or **terminal vertex** of $e$.
>- We say that $e$ is **directed from** $v_1$ **to** $v_2$.
>

>[!DEFINITION] Definition: Underlying Multigraph
>
>The **underlying multigraph** of a [directed multigraph](./Directed%20Multigraphs.md) $(V, E, s, t)$ is the [undirected multigraph](../Undirected%20Multigraphs/Undirected%20Multigraphs.md) $(V, E, \phi)$ such that $\phi(e) \overset{\text{def}}{=} \{s(e), t(e)\}$.
>

>[!DEFINITION] Definition: Subgraph
>
>Let $G = (V, E, s, t)$ be a [directed multigraph](./Directed%20Multigraphs.md).
>
>A **subgraph** of $G$ is a [directed multigraph](./Directed%20Multigraphs.md) $S = (V', E', s', t')$ with the following properties:
>
>- $V' \subseteq V$;
>- $E' \subseteq E$;
>- $s'$ is the [restriction](../../Analysis/Functions/Functions.md) of $s$ to $E'$;
>- $t'$ is the [restriction](../../Analysis/Functions/Functions.md) of $t$ to $E'$.
>

## Connectedness

>[!DEFINITION] Definition: Walk
>
>A **walk** in a [directed multigraph](./Directed%20Multigraphs.md) $(V, E, s, t)$ is an alternating [sequence](../../Analysis/Functional%20Analysis/Sequences/Sequences.md)
>
>$$
>(v_0, e_1, v_1, e_2, v_2, \dotsc, e_k, v_k)
>$$
>
>of [vertices](./Directed%20Multigraphs.md) and [edges](./Directed%20Multigraphs.md) such that $s(e_i) = v_{i_1}$ and $t(e_i) = v_i$ for all $1 \le i \le k$.
>
>>[!DEFINITION] Definition: Length
>>
>>We call $k \in \mathbb{N}_0$ the **length** of the [walk](./Directed%20Multigraphs.md).
>>
>

>[!DEFINITION] Definition: Path
>
>A **path** is a [walk](./Directed%20Multigraphs.md) 
>
>$$
>(v_0, e_1, v_1, e_2, v_2, \dotsc, e_k, v_k)
>$$
>
>such that $v_i \ne v_j$ for all distinct $i, j \in \{0, \dotsc, k\}$.
>

>[!DEFINITION] Definition: Weak Connectedness
>
>A [directed multigraph](./Directed%20Multigraphs.md) is **weakly connected** if for every pair of distinct [vertices](./Directed%20Multigraphs.md) $u$ and $v$ there exists a [path](#Connectedness) from $u$ to $v$ or from $v$ to $u$.
>

>[!DEFINITION] Definition: Weak Connectedness
>
>A [directed multigraph](./Directed%20Multigraphs.md) $G = (V, E, \phi)$ is **weakly connected** if for each pair of distinct [vertices](./Directed%20Multigraphs.md) $u$ and $v$, there exists a [sequence](../../Analysis/Functional%20Analysis/Sequences/Sequences.md)
>
>$$
>(v_0, e_1, v_1, \dotsc, e_k, v_k)
>$$
>
>of [vertices](./Directed%20Multigraphs.md) and [edges](./Directed%20Multigraphs.md), where $v_0 = u$ and $v_k = v$, such that for each $1 \le i \le k$, we have $\phi(e_i) = (v_{i-1}, v_i)$ or $\phi(e_i) = (v_i, v_{i-1})$.
>

>[!DEFINITION] Definition: Strong Connectedness
>
>A [directed multigraph](./Directed%20Multigraphs.md) is **strongly connected** if for every pair of distinct [vertices](./Directed%20Multigraphs.md) $u$ and $v$ there exists a [path](#Connectedness) from $u$ to $v$ and a [path](#Connectedness) from $v$ to $u$.
>

## Incidence Matrix

>[!DEFINITION] Definition: Incidence Matrix
>
>Let  $G = (V, E, s, t)$ be a [directed multigraph](./Directed%20Multigraphs.md) such that $V = \{v_1, \dotsc, v_m\}$ and $E = \{e_1, \dotsc, e_n\}$ are [finite](../../Set%20Theory/Cardinality.md).
>
>The **incidence matrix** of $G$ is the $m\times n$-[matrix](../../Algebra/Matrices/Real%20Matrices/Real%20Matrices.md) $B$ defined in the following way:
>
>$$
>b_{ij} = \begin{cases} +1 & \text{if } v_i = s(e_j) \text{ and } v_i \ne t(e_j) \\ -1 & \text{if } v_i \ne s(e_j) \text{ and } v_i = t(e_j) \\ 0 & \text{otherwise} \end{cases}
>$$
>

The [incidence matrix](#Incidence%20Matrix) is a complete description of how the [vertices](./Directed%20Multigraphs.md) are connected by the [edges](./Directed%20Multigraphs.md):
- The $i$-th row corresponds to the $i$-th [vertex](./Directed%20Multigraphs.md) $v_i$. If the $j$-th entry of this row is $+1$, then $v_i$ is the [source](./Directed%20Multigraphs.md) of the [edge](./Directed%20Multigraphs.md) $e_j$. If it is $-1$, then $v_i$ is the [target](./Directed%20Multigraphs.md) of the [edge](./Directed%20Multigraphs.md) $e_j$.
- The $j$-th column corresponds to the $j$-th [edge](./Directed%20Multigraphs.md) $e_j$. If the $i$-th entry of this column is $+1$, then $e_j$ begins at the [vertex](./Directed%20Multigraphs.md) $v_i$. If it is $-1$, then $e_j$ ends at the [vertex](./Directed%20Multigraphs.md) $v_i$. If all entries in the column are $0$, then $e_j$ is a [loop](./Directed%20Multigraphs.md).

