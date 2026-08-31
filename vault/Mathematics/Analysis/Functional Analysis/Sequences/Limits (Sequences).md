---
tags:
    - analysis
    - mathematics
---

# Limits (Sequences)

>[!DEFINITION] Definition: Limit (Sequences)
>
>Let $X$ be a [topological space](../../../Topology/Topological%20Spaces/Topological%20Space.md) and let $(x_n)_{n \in \mathcal{I}}$ be a [sequence](./Sequences.md) of points in $X$.
>
>A **limit** of $(x_n)_{n \in \mathcal{I}}$ is any $L \in X$ such that for each [neighborhood](../../../Topology/Topological%20Spaces/Neighborhoods.md) $N_L$ of $L$ there is some $N \in \mathcal{I}$ such that $x_n \in N_L$ for all $n \in \mathcal{I}$ with $n \ge N$.
>
>>[!NOTATION]
>>
>>We express the idea that some $L \in X$ is a [limit](./Limits%20(Sequences).md) of $(x_n)_{n \in \mathcal{I}}$ in one of the following ways:
>>
>>$$x_n \to L$$
>>
>>If $L$ is the one and only [limit](./Limits%20(Sequences).md), we can write the following:
>>
>>$$\lim x_n = L$$
>>
>>If $(x_n)_{n \in \mathcal{I}}$ is [infinite](./Sequences.md) and $L$ is its one and only [limit](./Limits%20(Sequences).md), then we often write the following:
>>
>>$$\lim_{n \to \infty} x_n = L$$
>>
>

>[!THEOREM] Theorem: Final Element is Limit of Finite Sequence
>
>Let $X$ be a [topological space](../../../Topology/Topological%20Spaces/Topological%20Space.md) and let $(x_n)_{n \in \mathcal{I}}$ be a [sequence](./Sequences.md) of points in $X$.
>
>If $(x_n)_{n \in \mathcal{I}}$ is [finite](./Sequences.md), then its last element is a [limit](./Limits%20(Sequences).md).
>
>$$x_n \to x_{\max \mathcal{I}}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: Finite Sequence with Multiple Limits
>>
>>Let $X = \{A, B, C\}$ be the [topological space](../../../Topology/Topological%20Spaces/Topological%20Space.md) whose [open sets](../../../Topology/Topological%20Spaces/Open%20Sets.md) are precisely the following:
>>
>>$$\{\varnothing, \{A, B\}, \{C\}, \{A, B, C\}\}$$
>>
>>Let $\mathcal{I} = \{1\}$ and let $(x_n)_{n \in \mathcal{I}}$ be the following [sequence](./Sequences.md):
>>
>>$$x_1 = A$$
>>
>>Since $A$ is the final element of $(x_n)_{n \in \mathcal{I}}$, we know that $A$ is a [limit](./Limits%20(Sequences).md).
>>
>>Let's check if $B$ is a [limit](./Limits%20(Sequences).md). In this [topological space](../../../Topology/Topological%20Spaces/Topological%20Space.md), $B$ has exactly the following [neighborhoods](../../../Topology/Topological%20Spaces/Neighborhoods.md):
>>
>>$$\{A, B\} \qquad \{A, B, C\}$$ 
>>
>>For the [neighborhood](../../../Topology/Topological%20Spaces/Neighborhoods.md) $N_B \overset{\text{def}}{=} \{A, B\}$ we have $x_n \in N_B$ for all $n \in \mathcal{I}$ with $n \ge N$, where $N \overset{\text{def}}{=} 1$.  For the [neighborhood](../../../Topology/Topological%20Spaces/Neighborhoods.md) $N_B \overset{\text{def}}{=} \{A, B, C\}$ we have $x_n \in N_B$ for all $n \in \mathcal{I}$ with $n \ge N$, where $N \overset{\text{def}}{=} 1$. Therefore, $B$ is also a [limit](./Limits%20(Sequences).md).
>>
>