---
tags:
    - measure-theory
    - mathematics
---

# Singularity (Measures)

>[!DEFINITION] Definition: Singularity
>
>Let $(X, \Sigma)$ be a [measurable space](./Measurable%20Space.md) and let $\mu: \Sigma \to [0,\infty]$ and $\nu: \Sigma \to [0,\infty]$ be [measures](./Measures.md) on $(X, \Sigma)$.
>
>We say that $\mu$ and $\nu$ are **singular to each other** if there exist [disjoint](../Set%20Theory/Intersections.md) [measurable](./Measurable%20Space.md) [sets](../Set%20Theory/Sets.md) $M, N \in \Sigma$ whose [union](../Set%20Theory/Unions.md) is $X$ such that $\mu$ is zero on all [measurable](./Measurable%20Space.md) [subsets](../Set%20Theory/Subsets.md) of $M$ and $\nu$ is zero on all [measurable](./Measurable%20Space.md) [subsets](../Set%20Theory/Subsets.md) of $N$.
>
>>[!NOTATION]
>>
>>$$\mu \perp \nu \qquad \nu \perp \mu$$
>>
>

>[!THEOREM] Theorem: Singularity
>
>Let $(X, \Sigma)$ be a [measurable space](./Measurable%20Space.md) and let $\mu: \Sigma \to [0,\infty]$ and $\nu: \Sigma \to [0,\infty]$ be [measures](./Measures.md) on $(X, \Sigma)$.
>
>Then $\mu$ and $\nu$ are [singular](./Singularity%20(Measures).md) if and only if there exist [disjoint](../Set%20Theory/Intersections.md) [measurable](./Measurable%20Space.md) [sets](../Set%20Theory/Sets.md) $M, N \in \Sigma$ whose [union](../Set%20Theory/Unions.md) is $X$ such that $\mu(M) = 0$ and $\nu(N) = 0$:
>
>$$\mu \perp \nu \iff \exists M, N \in \Sigma: M \cap N = \varnothing, M \cup N = X, \mu(M) = 0, \nu(N) = 0$$
>
>>[!PROOF]-
>>
>>TODO
>>
>