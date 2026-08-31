---
tags:
    - measure-theory
    - mathematics
---

# Carathéodory Extension

>[!DEFINITION] Definition: Carathéodory Measurability
>
>Let $X$ be a [set](../Set%20Theory/Sets.md) and let $\mu^{\ast}: \mathcal{P}(X) \to [0,\infty]$ be an [outer measure](./Outer%20Measures.md) on $X$.
>
>A [subset](../Set%20Theory/Subsets.md) $E \subseteq X$ is **Carathéodory-measurable with respect to** $\mu^{\ast}$ 
>
>$$\mu^{\ast}(S) = \mu^{\ast}(S \cap E) + \mu^{\ast} (S \setminus E)$$
>
>for every [subset](../Set%20Theory/Sets.md#Subsets) $S \subseteq X$.
>

>[!THEOREM] Carathéodory's Extension Theorem
>
>Let $X$ be a [set](../Set%20Theory/Sets.md) and let $\mu^{\ast}: \mathcal{P}(X) \to [0,\infty]$ be an [outer measure](./Outer%20Measures.md) on $X$.
>
>- The [collection](../Set%20Theory/Collections.md) of all $\mu^{\ast}$[-measurable](./Carathéodory%20Extension.md) [subsets](../Set%20Theory/Subsets.md) of $X$ is a [σ-algebra](./σ-Algebras.md) $\Sigma$ on $X$.
>- The [restriction](../Analysis/Functions/Functions.md) of $\mu^{\ast}$ on $\Sigma$ is a [measure](./Measures.md) on the [measurable space](./Measurable%20Space.md) $(X, \Sigma)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>