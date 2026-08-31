---
tags:
    - topology
    - mathematics
---

# Neighborhoods



>[!DEFINITION] Definition: Neighborhood Filter
>
>Let $X$ be a [set](../../Set%20Theory/Sets.md) and let $x \in X$.
>
>A **neighborhood filter** of $x$ is a [non-empty](../../Set%20Theory/Sets.md) [collection](../../Set%20Theory/Collections.md) $\mathcal{N}$ of [subsets](../../Set%20Theory/Subsets.md) of $X$, called **neighborhoods** of $x$, with the following properties:
>
>    - If $N \in \mathcal{N}$, then $x \in N$.
>    - If $N \in \mathcal{N}$ and $N \subseteq M \subseteq X$, then $M \in \mathcal{N}$.
>    - If $N_1, \dotsc, N_p \in \mathcal{N}$ for some $p \in \mathbb{N}_0$, then $N_1 \cap \cdots \cap N_p \in \mathcal{N}$.
>

A [neighborhood](./Neighborhoods.md) of $x$ is a [subset](../../Set%20Theory/Subsets.md) which "surrounds" $x$. To properly reflect our intuitive notions of what it means to surround something, [neighborhoods](./Neighborhoods.md) must have the additional properties outlined in the above definition:

- Every [neighborhood](./Neighborhoods.md) of $x$ must contain $x$ itself, since $x$ is intuitively contained in all of its surroundings.
- If a [neighborhood](./Neighborhoods.md) $N$ is [contained](../../Set%20Theory/Subsets.md) in some larger [subset](../../Set%20Theory/Subsets.md) $M \subseteq X$, then we also consider the entire $M$ to be a [neighborhood](./Neighborhoods.md) of $x$. In other words, if $N$ surrounds $x$ and is [contained](../../Set%20Theory/Subsets.md) in some larger $M$, then $M$ itself must surround $x$.
- Finally, the [intersection](../../Set%20Theory/Intersections.md) of [finitely](../../Set%20Theory/Cardinality.md) many [neighborhoods](./Neighborhoods.md) should itself be a [neighborhood](./Neighborhoods.md). After all, if some areas surround $x$, then the area where they [intersect](../../Set%20Theory/Intersections.md) surely also surrounds $x$.

A [neighborhood filter](./Neighborhoods.md) of $x$ defines the surroundings of a single $x \in X$, but we want to do this for each point in $X$.

>[!DEFINITION] Definition: Neighborhood System
>
>A **neighborhood system** on a [set](../../Set%20Theory/Sets.md) $X$ is a [function](../../Analysis/Functions/Functions.md) $\mathcal{N}: X \to \mathcal{P}(\mathcal{P}(X))$ which to each $x \in X$ assigns a [neighborhood filter](./Neighborhoods.md) $\mathcal{N}(x)$ of $x$ such that if $N \in \mathcal{N}(x)$, then there exists some $M \in \mathcal{N}(x)$ with $M \subseteq N$ and $N \in \mathcal{N}(y)$ for each $y \in M$.
>

A [neighborhood system](./Neighborhoods.md) is then just a choice for a [neighborhood filter](./Neighborhoods.md) for each $x \in X$. However, this choice needs to be made in a consistent way, since, on its own, the [neighborhood filter](./Neighborhoods.md) of each specific $x$ is unaware and bears no relation to the [neighborhoods](./Neighborhoods.md) of any other points in $X$. The condition thus links the [collections of neighborhoods](./Neighborhoods.md) together and ensures that if a local area $N$ surrounds $x$, then it is always possible to find a smaller local area $M$ surrounding $x$ such that all points $y$ in this area $M$ are surrounded by the larger area $N$.
