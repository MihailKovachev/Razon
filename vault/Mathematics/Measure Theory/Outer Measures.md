---
title: Outer Measures
tags:
    - measure-theory
    - mathematics
---

# Outer Measures

>[!DEFINITION] Definition: Outer Measure
>
>Let $X$ be a [set](../Set%20Theory/Sets.md).
>
>An **outer measure** on $X$ is a [function](../Analysis/Functions/Functions.md) $\mu: \mathcal{P}(X) \to [0,\infty]$ from the [power set](../Set%20Theory/Power%20Set.md) of $X$ to the [subspace](../Topology/Topological%20Subspaces.md) of the [non-negative extended real number line](../Analysis/Real%20Analysis/Extended%20Real%20Number%20Line.md) with the following properties:
>
>    - $\mu(\varnothing) = 0$.
>    - For all $A, B \in \mathcal{P}(X)$, if $A$ is a [subset](../Set%20Theory/Subsets.md) of $B$, then $\mu(A)$ is less than or equal to $\mu(B)$.
>
>$$\forall A, B \in \mathcal{P}(X): A \subseteq B \implies \mu^{\ast}(A) \le \mu^{\ast}(B)$$
>
>- For all [countable](../Set%20Theory/Cardinality.md) [subcollections](../Set%20Theory/Collections.md) $\{S_i\}_{i = 1}^{\infty}$ of $\mathcal{P}(X)$, we have
>
>$$
>\mu^{\ast} \left(\bigcup_{i=1}^{\infty} S_i \right) \le \sum_{i = 1}^{\infty} \mu^{\ast}(S_i)
>$$
>
>>[!NOTATION]
>>
>>We usually write $\mathbb{R}_{\ge 0} \cup \{\infty\}$ as $[0, \infty]$.
>>
>
>>[!WARNING]
>>
>>An [outer measure](./Outer%20Measures.md) is not necessarily a [measure](Measure%20Spaces.md) on $(X, \mathcal{P}(X))$.
>>
>

>[!THEOREM] Theorem: Alternative Definition
>
>Let $X$ be a [set](../Set%20Theory/Sets.md).
>
>A [function](../Analysis/Functions/Functions.md) $\mu^{\ast}: \mathcal{P}(X) \to \mathbb{R}_{\ge 0} \cup \{\infty\}$ from the [powerset](../Set%20Theory/Sets.md#Subsets) of $X$ to the [non-negative extended real numbers](../Algebra/Extended%20Real%20Numbers.md) is an [outer measure](./Outer%20Measures.md) on $X$ if and only if $\mu^{\ast}$ has the following properties:
>- $\mu^{\ast}(\varnothing) = 0$
>- For all [subsets](../Set%20Theory/Sets.md#Subsets) $A \subseteq X$ and all [countable](../Set%20Theory/Cardinality.md) [subcollections](../Set%20Theory/Collections.md) $\{S_i\}_{i = 1}^{\infty}$ of $\mathcal{P}(X)$ we have
>
>$$
>A \subseteq \bigcup_{i = 1}^{\infty} S_i \implies \mu^{\ast}(A) \le \sum_{i = 1}^{\infty} \mu^{\ast}(S_i)
>$$
>
>>[!PROOF]-
>>
>>**Proof of (1):**
>>
>>TODO
>>
>>**Proof of (2):**
>>
>>TODO
>>
>
