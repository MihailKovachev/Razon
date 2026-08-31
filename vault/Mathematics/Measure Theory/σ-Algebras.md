---
tags:
    - measure-theory
    - mathematics
---

# σ-Algebras

In [measure theory](./Measure%20Theory.md), we want to be able to "measure" aspects of the [subsets](../Set%20Theory/Subsets.md) of some [set](../Set%20Theory/Sets.md) $X$. In general, not all [subsets](../Set%20Theory/Subsets.md) have all aspects which we might want to measure, just like we cannot really measure the humidity of a sound. It simply does not make sense to speak of how humid a sound wave is. Similarly, some [subsets](../Set%20Theory/Subsets.md) might be measurable in certain aspects but not in others. Therefore, we need to know which things can be measured in the way we want, i.e. we need a notion of **measurable sets** in $X$.

>[!DEFINITION] Definition: σ-Algebra
>
>Let $X$ be a [set](../Set%20Theory/Sets.md).
>
>A **σ-algebra** over $X$ is a [collection](../Set%20Theory/Collections.md) $\Sigma$ of [subsets](../Set%20Theory/Subsets.md) of $X$ with the following properties:
>
>- The [empty set](../Set%20Theory/Sets.md) $\varnothing$ and $X$ itself are in $\Sigma$.
>- If a [subset](../Set%20Theory/Subsets.md) $S \subset X$ is in $\Sigma$, then so is its [complement](../Set%20Theory/Sets.md#Operations) $X \setminus S$.
>- If $\mathcal{S}$ is a [countable](../Set%20Theory/Cardinality.md) [subcollection](../Set%20Theory/Collections.md) of $\Sigma$, then its [union](../Set%20Theory/Unions.md) $\bigcup \mathcal{S}$ is also in $\Sigma$.
>
>The elements of $\Sigma$ are called **measurable sets**.
>

A [σ-algebra](./σ-Algebras.md) is just a selection of [subsets](../Set%20Theory/Subsets.md) with the aspects that we want to measure. The intuition behind the requirements of the definition is the following:

- Intuitively, $\varnothing$ should be in $\Sigma$ because measuring any aspect of "nothing" should simply result in zero. Otherwise, "nothing" would have "something" and so it would not really be "nothing". Furthermore, we want the "whole thing" $X$ itself to be measurable and so $X$ should be in $\Sigma$.
- If we can measure the whole thing $X$ and we can measure a part $S$, then we should intuitively be able to measure the remaining part $X \setminus S$ as well.
- The last requirement guarantees that if something is made of components which have the desired aspects, then it should itself have these aspects.

>[!THEOREM] Theorem: Countable Intersections in Σ-Algebras
>
>Let $X$ be a [set](../Set%20Theory/Sets.md) and let $\Sigma$ be a [σ-algebra](./σ-Algebras.md) on $X$.
>
>If $\mathcal{S}$ is a [countable](../Set%20Theory/Cardinality.md) [subcollection](../Set%20Theory/Collections.md) of $\Sigma$, then its [intersection](../Set%20Theory/Intersections.md) $\bigcap \mathcal{S}$ is also in $\Sigma$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem:
>
>Let $X$ be a [set](../Set%20Theory/Sets.md).
>
>If $\mathcal{C}$ is a [collection](../Set%20Theory/Collections.md) of [σ-algebras](./σ-Algebras.md) on $X$, then its [intersection](../Set%20Theory/Intersections.md) $\bigcap \mathcal{C}$ is also a [σ-algebra](./σ-Algebras.md) on $X$.
>
>>[!PROOF]-
>>
>>TODO
>>
>