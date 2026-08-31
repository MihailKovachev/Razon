---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Span

>[!DEFINITION] Definition: Span
>
>Let $(V, F, +, \cdot)$ be a [vector space](./Vector%20Spaces.md#Vector%20Spaces) and let $S \subseteq V$.
>
>The **span** of $S$ is the [set](../../Set%20Theory/Sets.md) of all [linear combinations](#Linear%20Combinations) which can be constructed from [vectors](./Vector%20Spaces.md#Vector%20Spaces) in $S$:
>
>$$
>\{c_1 \mathbf{v}_1 + \cdots + c_n \mathbf{v}_n \mid n \ge 1, c_k \in F, \mathbf{v}_k \in S\}
>$$
>
>Let $\mathbf{v}_1, \mathbf{v}_2, \dotsc$ be [vectors](./Vector%20Spaces.md#Vector%20Spaces) in a [vector space](./Vector%20Spaces.md#Vector%20Spaces) $(V, F, +, \cdot)$.
>
>>[!NOTATION] Notation
>>
>>$$
>>\langle S \rangle \qquad \mathop{\operatorname{span}} (S)
>>$$
>>
>>If $S$ contains only [countably many](../../Set%20Theory/Cardinality.md) elements $\mathbf{s}_1, \mathbf{s}_2, \dotsc$, we can also write
>>
>>$$
>>\langle \{ \mathbf{s}_1, \mathbf{s}_1, \cdots \} \rangle \qquad \langle \mathbf{s}_1, \mathbf{s}_1, \cdots \rangle \qquad \operatorname{span}(\{ \mathbf{s}_1, \mathbf{s}_1, \cdots \}) \qquad \operatorname{span}( \mathbf{s}_1, \mathbf{s}_1, \cdots)
>>$$
>>
>>If $S$ contains only [finitely many](../../Set%20Theory/Cardinality.md) elements $\mathbf{s}_1, \dotsc, \mathbf{s}_n$, we can also write
>>
>>$$
>>\langle \{ \mathbf{s}_1, \dotsc, \mathbf{s}_n \} \rangle \qquad \langle \mathbf{s}_1, \dotsc, \mathbf{s}_n \rangle \qquad \operatorname{span}(\{ \mathbf{s}_1, \dotsc, \mathbf{s}_n \}) \qquad \operatorname{span}( \mathbf{s}_1, \dotsc, \mathbf{s}_n)
>>$$
>>
>
>>[!THEOREM] Theorem: Equivalent Definition
>>
>>The [span](#Span) of $S$ is the [intersection](../../Set%20Theory/Collections.md) of all [subspaces](./Vector%20Spaces.md#Subspaces) containing $S$:
>>
>>$$
>>\mathop{\operatorname{span}}(S) = \bigcap \{U \mid U \text{ is a subspace of } V \text{ and } S \subseteq U \}
>>$$
>>
>>>[!PROOF]-
>>>
>>>Let $L$ be the [set](../../Set%20Theory/Sets.md) of all [linear combinations](#Linear%20Combinations) which can be constructed from [vectors](./Vector%20Spaces.md#Vector%20Spaces) in $S$:
>>>
>>>$$
>>>L = \{c_1 \mathbf{v}_1 + \cdots + c_n \mathbf{v}_n \mid n \ge 1, c_k \in F, \mathbf{v}_k \in S\}
>>>$$
>>>
>>>Let $I$ be the [intersection](../../Set%20Theory/Collections.md) of all [subspaces](./Vector%20Spaces.md#Subspaces) containing $S$:
>>>
>>>$$
>>>I = \bigcap \{U \mid U \text{ is a subspace of } V \text{ and } S \subseteq U \}
>>>$$
>>>
>>>TODO
>>>
>>
>

>[!THEOREM] Theorem: Span is a Subspace
>
>If $S$ is a [subset](../../Set%20Theory/Sets.md) of a [vector space](./Vector%20Spaces.md) $V$, then the [span](./Span.md) of $S$ is a [subspace](./Linear%20Subspaces.md) of $(V, F, +, \cdot)$.
>
>>[!PROOF]-
>>
>>**Non-emptiness:**
>>
>>Obviously, $\mathbf{0} \in \operatorname{\mathop{span}}(S)$.
>>
>>**Closure under vector addition:**
>>
>>Let $\mathbf{u}, \mathbf{v} \in \operatorname{\mathop{span}}(S)$. By definition, we have $\mathbf{u}, \mathbf{v} \in U$ for all [subspaces](./Linear%20Subspaces.md) $U$ of $V$ with $S \subseteq U$. Since these are [subspaces](./Linear%20Subspaces.md) we know that $\mathbf{u} + \mathbf{v} \in U$ for all [subspaces](./Linear%20Subspaces.md) $U$ of $V$ with $S \subseteq U$. Since $\mathbf{u} + \mathbf{v}$ belongs to *all* such [subspaces](./Linear%20Subspaces.md), it must also belong to their [intersection](../../Set%20Theory/Collections.md):
>>
>>$$
>>\mathbf{u}, \mathbf{v} \in \bigcap_{S \subseteq U} U = \operatorname{\mathop{span}}(S)
>>$$
>>
>>**Closure under scalar multiplication:**
>>
>>Let $\mathbf{u} \in \operatorname{\mathop{span}}(S)$. By definition, we have $\mathbf{u} \in U$ for all [subspaces](./Linear%20Subspaces.md) $U$ of $V$ with $S \subseteq U$. Since these are [subspaces](./Linear%20Subspaces.md) we know that $\lambda \mathbf{u} \in U$ for all [subspaces](./Linear%20Subspaces.md) $U$ of $V$ with $S \subseteq U$. Since $\lambda \mathbf{u}$ belongs to *all* such [subspaces](./Linear%20Subspaces.md), it must also belong to their [intersection](../../Set%20Theory/Collections.md):
>>
>>$$
>>\lambda \mathbf{u} \in \bigcap_{S \subseteq U} U = \operatorname{\mathop{span}}(S)
>>$$
>>
>>We have thus shown that $\operatorname{\mathop{span}}(S)$ satisfies the definition of a [subspace](./Linear%20Subspaces.md).
>>
>

>[!THEOREM] Theorem: Span of Subset is Subset of Span
>
>Let $V$ be a [vector space](./Vector%20Spaces.md) and let $S, T \subseteq V$.
>
>If $S$ is a [subset](../../Set%20Theory/Sets.md#Subsets) of $T$, then the [span](./Linear%20Combinations.md) of $S$ is a [subset](../../Set%20Theory/Sets.md#Subsets) of the [span](./Linear%20Combinations.md) of $T$:
>
>$$
>S \subseteq T \implies \mathop{\operatorname{span}} S \subseteq \mathop{\operatorname{span}} T
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Span of Subspace Union
>
>If $U_1, \dotsc, U_n$ are [subspaces](./Linear%20Subspaces.md) of a [vector space](./Vector%20Spaces.md) $V$, then the [span](./Span.md) of their [union](../../Set%20Theory/Sets.md) is equal to their [sum](./Linear%20Subspaces.md#Sum):
>
>$$
>\mathop{\operatorname{span}}(U_1 \cup \cdots \cup U_n) = U_1 + \cdots U_n
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Spanning Sets

>[!DEFINITION] Definition: Spanning Set (Generator)
>
>Let $(V,F,+,\cdot)$ be a [vector space](../../../index.md#Vector%20Spaces).
>
>A [subset](../../Set%20Theory/Sets.md) $S \subseteq V$ is a **spanning set** (or a **generator**) of $(V,F,+,\cdot)$ if the [span](#Span) of $S$ is $V$:
>
>$$
>\operatorname{span}(S) = V
>$$
>
>>[!TIP]
>>
>>This essentially means that each [vector](./Vector%20Spaces.md) in $V$ can be expressed as a [linear combination](./Linear%20Combinations.md) of some [vectors](./Vector%20Spaces.md) in $S$.
>>
>
>>[!DEFINITION] Definition: Minimality
>>
>>A [spanning set](#Spanning%20Sets) $S$ is **minimal** if there is no vector $\mathbf{v} \in S$ such that $S \setminus \{\mathbf{v}\}$ is still a [spanning set](#Spanning%20Sets).
>>
>>>[!TIP]
>>>
>>>This means that there is no way to remove a vector from a minimal spanning set and still obtain a spanning set of the vector space.
>>>
>>
>

>[!DEFINITION] Definition: Finitely Generated Vector Space
>
>A [vector space](./Vector%20Spaces.md) is **finitely generated** if there exists a [finite](../../Set%20Theory/Cardinality.md) [spanning set](#Spanning%20Sets) for it.
>

