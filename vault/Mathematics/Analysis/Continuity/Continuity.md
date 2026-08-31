---
tags:
    - analysis
    - topology
    - mathematics
---

# Continuity 

>[!DEFINITION] Definition: Continuity
>
>Let $X$ and $Y$ be [topological spaces](../../Topology/Topological%20Spaces/Topological%20Space.md).
>
>A [function](../Functions/Functions.md) $f: X \to Y$ is **continuous** at $p \in X$, if for each [neighborhood](../../Topology/Topological%20Spaces/Neighborhoods.md) $V$ of $f(p)$, there exists a [neighborhood](../../Topology/Topological%20Spaces/Neighborhoods.md) $U$ of $p$ with $f(x) \in V$ for all $x \in U$:
>
>$$\forall x \in X: x \in U \implies f(x) \in V$$
>
>If $f$ is [continuous](./Continuity.md) at every $p \in X$, then we simply say that $f$ is **continuous**.
>
>>[!DEFINITION] Definition: Continuity on Subspaces
>>
>>Let $S$ be a [subspace](../../Topology/Topological%20Subspaces.md) of $X$.
>>
>>We say that $f$ is **continuous on** $S$ if its [restriction](TODO) $f\vert_S: S \to Y$ is [continuous](./Continuity.md).
>>
>

>[!THEOREM] Theorem: Local Continuity and Global Continuity
>
>Let $X$ and $Y$ be [topological spaces](../../Topology/Topological%20Spaces/Topological%20Space.md).
>
>A [function](../Functions/Functions.md) $f: X \to Y$ is [continuous](./Continuity.md) if and only if each $p \in X$ has a [neighborhood](../../Topology/Topological%20Spaces/Neighborhoods.md) $N(p)$ on which $f$ is [continuous](./Continuity.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity via Open Sets
>
>Let $X$ and $Y$ be [topological spaces](../../Topology/Topological%20Spaces/Topological%20Space.md).
>
>A [function](../Functions/Functions.md) $f: X \to Y$ is [continuous](./Continuity.md) if and only if the [inverse image](../Functions/Functions.md) of each [open subset](../../Topology/Topological%20Spaces/Open%20Sets.md) of $Y$ is an [open subset](../../Topology/Topological%20Spaces/Open%20Sets.md) of $X$:
>
>$$V \subseteq Y \text{ open} \implies f^{-1}(V) \subseteq X \text{ open}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity via Closed Sets
>
>Let $X$ and $Y$ be [topological spaces](../../Topology/Topological%20Spaces/Topological%20Space.md).
>
>A [function](../Functions/Functions.md) $f: X \to Y$ is [continuous](./Continuity.md) if and only if the [inverse image](../Functions/Functions.md) of each [closed subset](../../Topology/Topological%20Spaces/Closed%20Sets.md) of $Y$ is a [closed subset](../../Topology/Topological%20Spaces/Closed%20Sets.md) of $X$.
>
>$$C \subseteq Y \text{ closed} \implies f^{-1}(C) \subseteq X \text{ closed}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Extreme Value Theorem
>
>Let $(X,\tau_X)$ and $(Y,\tau_Y)$ be [topological spaces](../../Topology/Topological%20Spaces/Topological%20Space.md).
>
>If $(X,\tau_X)$ is [compact](../../Topology/Compactness.md), then its [image](../Functions/Functions.md) $f(X)$ under every [continuous](./Continuity.md) [function](../Functions/Functions.md) $f: X \to Y$ is also [compact](../../Topology/Compactness.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity of Composition
>
>Let $X, Y, Z$ be [topological spaces](../../Topology/Topological%20Spaces/Topological%20Space.md).
>
>If $f: X \to Y$ and $g: Y \to Z$ are [continuous](./Continuity.md), then so is their [composition](../Functions/Functions.md) $g \circ f: X \to Z$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Intermediate Value Theorem
>
>Let $(X,\tau_X)$ and $(Y,\tau_Y)$ be [topological spaces](../../Topology/Topological%20Spaces/Topological%20Space.md).
>
>If $(X, \tau_X)$ is [connected](../../Topology/Connectedness.md), then its [image](../Functions/Functions.md) $f(X)$ under every [continuous](./Continuity.md) [function](../Functions/Functions.md) $f: X \to Y$ is also [connected](../../Topology/Connectedness.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>