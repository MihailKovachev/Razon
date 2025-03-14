---
title: The Empty Set
tags:
    - set-theory
    - mathematics
---

>[!AXIOM] Axiom: Existence of an Empty Set
>
>There exists a [set](Sets.md) with no elements.
>
>$$
>\exists A \forall x(x \notin A)
>$$
>
>>[!NOTATION]-
>>
>>$$
>>\varnothing \qquad \emptyset \qquad \{\}
>>$$
>>
>
>^empty-set
>

>[!THEOREM] Theorem: Uniqueness of the Empty Set
>
>There is only one empty set.
>
>>[!PROOF]-
>>
>>Let $A$ and $B$ be two empty sets. They have no elements and so the statement
>>
>>$$
>>x \in A \iff x \in B
>>$$
>>
>>is vacuously true. Therefore, $A = B$.
>>
>

>[!THEOREM] Theorem
>
>The empty set is a [subset](Sets.md) of all [sets](Sets.md).
>
>>[!PROOF]-
>>
>>Let $A$ be a set.
>>
>>Suppose that the empty set $\varnothing$ is *not* a subset of $A$. Then there must exist an element $e \in \varnothing$ which is not an element of $A$, i.e. $e \notin A$. This is a contradiction, since the empty set contains no elements.
>>
>
>^empty-set-is-subsets-of-every-set
>