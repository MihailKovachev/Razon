---
tags:
    - analysis
    - mathematics
---

# Limit (Functions)

>[!DEFINITION] Definition: Limit (Function)
>
>Let $X$ and $Y$ be [topological spaces](../../Topology/Topological%20Spaces/Topological%20Space.md), let $f: \mathcal{D} \subseteq X \to Y$ be a [function](../Functions/Functions.md) and let $p \in X$ be an [accumulation point](../../Topology/Accumulation%20Points.md) of $\mathcal{D}$.
>
>A **limit** of $f$ is any $L \in Y$ such that for each [neighborhood](../../Topology/Topological%20Spaces/Neighborhoods.md) $V$ of $L$, there exists some [neighborhood](../../Topology/Topological%20Spaces/Neighborhoods.md) $U$ of $p$ in $X$ with
>
>$$x \in U \implies f(x) \in V$$
>
>for all $x \in \mathcal{D} \setminus \{p\}$.
>
>>[!NOTATION]
>>
>>To indicate that $L$ is a [limit](./Limit%20(Functions).md) of $f$ at $p$, we write:
>>
>>$$f(x) \overset{x \to p}{\to} L$$
>>
>>If $L$ is the only [limit](./Limit%20(Functions).md) of $f$ at $p$, we also use the following notation:
>>
>>$$\lim_{x \to p} f(x) = L$$
>>
>

>[!THEOREM] Theorem: Limit Uniqueness in Hausdorff Spaces
>
>Let $X$ and $Y$ be [topological spaces](../../Topology/Topological%20Spaces/Topological%20Space.md), let $f: \mathcal{D} \subseteq X \to Y$ be a [function](../Functions/Functions.md) and let $p \in X$ be an [accumulation point](../../Topology/Accumulation%20Points.md) of $\mathcal{D}$.
>
>If $Y$ is a [Hausdorff space](../../Topology/Hausdorff%20Space.md) and $L$ and $L'$ are [limits](./Limit%20(Functions).md) of $f$ at $p$, then $L = L'$.
>
>>[!PROOF]-
>>
>>TODO
>>
>