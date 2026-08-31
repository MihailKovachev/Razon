---
tags:
    - algebra
    - mathematics
---

# Monoids

>[!DEFINITION] Definition: Monoid
>
>A **monoid** $(M, v)$ is a [set](../Set%20Theory/Sets.md) $M$ equipped with an [operation](../Analysis/Functions/Functions.md) $v: M \times M \to M$ which satisfies the following:
>
>- Associativity: $v(v(a, b), c) = v(a, v(b,c))$ for all $a,b,c \in M$.
>- Existence of a neutral element: There is some $e \in M$ such that $v(e,a) = v(a,e) = a$ for all $a \in M$.
>

>[!THEOREM] Theorem: Monoids are Semigroups
>
>Every [monoid](./Monoids.md) is a [semigroup](./Groups/Groups.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>