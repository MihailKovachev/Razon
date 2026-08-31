---
tags:
    - graph-theory
    - mathematics
---

# Graphs

>[!DEFINITION] Definition: Graph
>
>A **graph** $G$ is a [tuple](../Set%20Theory/Tuples.md) $(V, E, \tau, \phi)$ consisting of two [sets](../Set%20Theory/Sets.md) $V$ and $E$, where $V \cap E = \varnothing$, and two [functions](../Analysis/Functions/Functions.md) $\tau$ and $\phi$.
>
>>[!DEFINITION] Definition: Vertex
>>
>>Each $v \in V$ is known as a **vertex** or **node** of $G$.
>>
>
>>[!DEFINITION] Definition: Edges
>>
>>Each $e \in E$ is known as an **edge** of $G$.
>>
>
>>[!DEFINITION] Definition: Orientability Function
>>
>>The [function](../Analysis/Functions/Functions.md) $\tau: E \to \{0,1\}$ is known as the **orientability function**.
>>
>>>[!DEFINITION] Definition: Undirected Edge
>>>
>>>An [edge](#Graphs) $e \in E$ is **undirected** if $\tau(e) = 0$.
>>>
>>
>>>[!DEFINITION] Definition: Directed Edge
>>>
>>>An [edge](#Graphs) $e \in E$ is **directed** if $\tau(e) = 1$.
>>>
>>
>
>>[!DEFINITION] Definition: Incidence Function
>>
>>The [function](../Analysis/Functions/Functions.md) $\phi: E \to (V \times V) \cup \mathcal{S}_2(V)$ known as the **incidence function**, where $\mathcal{S}_2(V)$ denoting the [set](../Set%20Theory/Sets.md) of all [subsets](../Set%20Theory/Subsets.md) and [multisubsets](../Set%20Theory/Multisets.md) of $V$ with [cardinality](../Set%20Theory/Cardinality.md) $2$.
>>
>>It is such that $\phi(e) \in \mathcal{S}_2(V)$ for each [undirected edge](#Graphs) $e \in E$ and $\phi(e) \in V \times V$ for each [directed edge](#Graphs) $e \in E$.
>>
>>>[!DEFINITION] Definition: Vertices of Directed Edge
>>>
>>>If $e \in E$ is a [directed edge](#Graphs) with $\phi(e) = (v_1, v_2)$, then we call:
>>>
>>>    - $v_1$ the **source** / **tail** / **initial vertex** of $e$;
>>>    - $v_2$ the **target** / **head** / **terminal vertex** of $e$.
>>>
>>
>
