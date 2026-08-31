---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Linear Subspaces

>[!DEFINITION] Definition: Linear Subspace
>
>Let $(V,F,+,\cdot)$ be a [vector space](./Vector%20Spaces.md).
>
>We say that $U \subseteq V$ is a **linear subspace** of $(V,F,+,\cdot)$ if the following conditions hold simultaneously:
>- $U \ne \varnothing$;
>- $\mathbf{u}+\mathbf{u}' \in U$ for all $\mathbf{u}, \mathbf{u}' \in U$;
>- $c\mathbf{u}\in U$ for all $\mathbf{u} \in U$ and all $c \in F$.
>
>>[!NOTATION]
>>
>>If $U$ is a [linear subspace](./Linear%20Subspaces.md) of $V$, we often write $U \le V$.
>>
>
>>[!EXAMPLE]-
>>
>>If $\mathbf{v} \in V$, then the [set](../../Set%20Theory/Sets.md)
>>
>>$$
>>U_{\mathbf{v}} \overset{\text{def}}{=} \{\lambda \mathbf{v} \mid \lambda \in F\}
>>$$
>>
>>is a [subspace](./Linear%20Subspaces.md) of $V$.
>>
>>TODO
>>
>
>>[!THEOREM] Theorem: Alternative Definition
>>
>>A [subset](../../Set%20Theory/Sets.md) $U \subseteq V$ is a [subspace](./Linear%20Subspaces.md) of $V$ if and only if it is equal to its own [span](./Span.md):
>>
>>$$
>>U = \mathop{\operatorname{span}}(U)
>>$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

>[!THEOREM] Theorem: Non-Subspace Criterion
>
>Let $(V,F,+,\cdot)$ be a [vector space](./Vector%20Spaces.md) and let $U \subseteq V$.
>
>If $U$ does not contain the [zero vector](./Vector%20Spaces.md), then it is *not* a [subspace](#Subspaces). 
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Subspace Intersection is a Subspace
>
>Let $(V,F,+,\cdot)$ be a [vector space](./Vector%20Spaces.md).
>
>If $\mathcal{U}$ is a [collection](../../Set%20Theory/Collections.md) of [subspaces](./Linear%20Subspaces.md) of $V$, then its [intersection](../../Set%20Theory/Collections.md) $\bigcap \mathcal{U}$ is also a [subspace](./Linear%20Subspaces.md) of $V$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Union of Subspaces
>
>Let $(V,F,+,\cdot)$ be a [vector space](./Vector%20Spaces.md) and let $\mathcal{U}$ be a [collection](../../Set%20Theory/Collections.md) of [subspaces](./Linear%20Subspaces.md) of $V$.
>
>The [union](../../Set%20Theory/Collections.md) $\bigcup \mathcal{U}$ is a [subspace](#Subspaces) of $V$ if and only if $U_i \subseteq U_j$ or $U_j \subseteq U_i$ for all $U_i, U_j \in \mathcal{U}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Subspace Dimension
>
>If $U$ is a [subspace](./Linear%20Subspaces.md) of [finite dimensional](./Hamel%20Bases.md) [vector space](./Vector%20Spaces.md) $V$, then $\dim U \le \dim V$ with $\dim U = \dim V$ if and only if $U = V$.
>
>>[!DEFINITION] Definition: Codimension
>>
>>The difference $\dim V - \dim U$ is known as the **codimension** of $U$.
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\mathop{\operatorname{codim}} U
>>>$$
>>>
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

### Sum

>[!DEFINITION] Definition: Sum
>
>Let $U_1, \dotsc, U_n$ be [subspaces](#Subspaces) of a [vector space](./Vector%20Spaces.md) $(V, F, +, \cdot)$.
>
>The **sum** of $U_1, \dotsc, U_n$ is the following [set](../../Set%20Theory/Sets.md):
>
>$$
>U_1 + \cdots U_n \overset{\text{def}}{=} \{\mathbf{u}_1 + \cdots + \mathbf{u}_n \mid \mathbf{u}_1 \in U_1, \dotsc, \mathbf{u}_n \in U_n\}
>$$
>

>[!THEOREM] Theorem: Sum is Subspace
>
>If $U_1, \dotsc, U_n$ are [subspaces](#Subspaces) of a [vector space](./Vector%20Spaces.md) $V$, then their [sum](#Sum) $U_1 + \cdots + U_n$ is also a [subspace](#Subspaces) $V$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!DEFINITION] Definition: Direct Sum
>
>Let $U_1, \dotsc, U_n$ be [subspaces](#Subspaces) of a [vector space](#Vector%20Spaces) $(V, F, +, \cdot)$.
>
>We say that $V$ is the **direct sum** of $U_1, \dotsc, U_n$ if the following conditions are simultaneously true:
>- $U_1 \cap \cdots \cap U_n = \{\mathbf{0}\}$.
>- For each $\mathbf{v} \in V$, there exist $\mathbf{u}_1 \in U_1, \dotsc, \mathbf{u}_n \in U_n$ such that $\mathbf{v} = \mathbf{u}_1 + \cdots + \mathbf{u}_n$.
>
>>[!NOTATION]
>>
>>$$
>>V = U_1 \oplus \cdots \oplus U_n
>>$$
>>
>

>[!THEOREM] Theorem: Uniqueness of Direct Sum Representation
>
>If a [vector space](#Vector%20Spaces) $(V, F, +, \cdot)$ is a [direct sum](#Subspaces) of the [subspaces](#Subspaces) $(U_1, F, +, \cdot), \dotsc, (U_n, F, +, \cdot)$, then the [direct sum representation](./Vector%20Spaces.md) of each $\mathbf{v} \in V$ is unique.
>
>>[!PROOF]-
>>
>>TODO
>>
>
