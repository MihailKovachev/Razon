---
tags:
    - graph-theory
    - mathematics
---

>[!DEFINITION] Definition: Undirected Graph
>
>An **undirected graph** $(V, E)$ consists of a [set](../../Set%20Theory/Sets.md) $V$ and a [collection](../../Set%20Theory/Collections.md) $E$ of [unordered pairs](../../Set%20Theory/Sets.md) of elements of $V$:
>
>- The elements of $V$ are called **vertices** or **nodes**;
>- The elements of $E$ are called **edges** or **branches**. Each [edge](./Undirected%20Graphs.md) $e \in E$ is a [set](../../Set%20Theory/Sets.md) $\{u, v\}$ of two distinct [vertices](./Undirected%20Graphs.md) $u, v \in V$.
>
>For $e = \{u, v\} \in E$:
>- We say that $u$ and $v$ are **adjacent** or **neighbors**.
>- We say that $e$ is **incident** to $u$ and $v$.
>

>[!DEFINITION] Definition: Subgraph
>
>Let $G = (V, E)$ be an [undirected graph](./Undirected%20Graphs.md).
>
>A **subgraph** of $G$ is an [undirected graph](./Undirected%20Graphs.md) $G' = (V', E')$ with the following properties:
>
>- $V' \subseteq V$;
>- $E' \subseteq E$.
>

>[!DEFINITION] Definition: Walk
>
>A **walk** in an [undirected graph](./Undirected%20Graphs.md) $G = (V, E)$ is an alternating [sequence](../../Analysis/Functional%20Analysis/Sequences/Sequences.md)
>
>$$
>(v_0, e_1, v_1, e_2, v_2, \dotsc, e_k, v_k)
>$$
>
>of [vertices](./Undirected%20Graphs.md) and [edges](./Undirected%20Graphs.md) such that $e_i = \{v_{i-1}, v_i\}$ for all $1 \le i \le k$.
>
>>[!DEFINITION] Definition: Length
>>
>>We call $k \in \mathbb{N}_0$ the **length** of the [walk](./Undirected%20Graphs.md).
>>
>

>[!DEFINITION] Definition: Path
>
>A **path** is a [walk](./Undirected%20Graphs.md)
>
>$$
>(v_0, e_1, v_1, e_2, v_2, \dotsc, e_k, v_k)
>$$
>
>such that $v_i \ne v_j$ for all distinct $i, j \in \{0, \dotsc, k\}$.
>

>[!DEFINITION] Definition: Connectedness
>
>An [undirected graph](./Undirected%20Graphs.md) is **connected** if for every pair of distinct [vertices](./Undirected%20Graphs.md) $u$ and $v$ there exists a [path](#Connectedness) between $u$ and $v$.
>