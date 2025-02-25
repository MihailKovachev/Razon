---
title: Set Operations
tags:
  - set-theory
  - mathematics
---

# Union

>[!DEFINITION] Definition: Union
>
>The **union** of two [sets](Sets.md) $A$ and $B$ is the set which contains exactly the elements which are in $A$, in $B$ or in both $A$ and $B$.
>
>$$
>\{x \mid x\in A  \lor x\in B\}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>A \cup B
>>$$
>>
>

## Properties

>[!THEOREM] Theorem: Cardinality of the Set Union
>
>The [union](Set%20Operations.md#union) of two [sets](Sets.md) $A$ and $B$ has [cardinality](Cardinality/index.md)
>
>$$
>|A\cup B| = |A|+|B|-|A \cap B|
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Commutativity of the Set Union
>
>The [union](Set%20Operations.md#union) of two [sets](Sets.md) $A$ and $B$ is commutative.
>
>$$
>A\cup B = B \cup A
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Intersection

>[!DEFINITION] Definition: Intersection
>
>The **intersection** of two [sets](Sets.md) $A$ and $B$ is the set of all elements shared by $A$ and $B$.
>
>$$
>\{ x \mid x\in A \land x \in B\}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>A \cap B
>>$$
>>
>

## Properties

>[!THEOREM] Theorem: Commutativity of Set Intersection
>
>The [intersection](Set%20Operations.md#intersection) of two [sets](Sets.md) $A$ and $B$ is commutative.
>
>$$
>A \cap B = B \cap A
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Associativity of Set Intersection
>
>The [intersection](Set%20Operations.md#intersection) operation is associative for all [sets](Sets.md) $A, B, C$:
>
>$$
>(A\cap B)\cap C = A\cap(B\cap C)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Set Difference

>[!DEFINITION] Definition: Set Difference
>
>The **set difference** $A \setminus B$ of two [sets](Sets.md) $A$ and $B$ is the set which contains exactly the elements in $A$ which are not elements of $B$.
>
>$$
>\{x \mid x \in A \land x \notin B\}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>A \setminus B \qquad A - B
>>$$
>>
>

# Cartesian Product

>[!DEFINITION] Definition: Cartesian Product
>
>The **Cartesian product** $A \times B$ of two [sets](Sets.md) $A$ and $B$ is the [set](Sets.md) of all [ordered pairs](./Ordered%20Pairs.md) $(a;b)$ where $a \in A$ and $b \in B$.
>
>$$
>A\times B \overset{\text{def}}{=} \{(a; b)\mid a\in A \land b \in B\}
>$$
>

## Properties

>[!THEOREM] Theorem: Cardinality of the Cartesian Product
>
>The [Cartesian product](Set%20Operations.md#cartesian%20product) of two [sets](Sets.md) $A$ and $B$ has [cardinality](Cardinality/index.md)
>
>$$
>|A \times B| = |B \times A| = |A|\cdot |B|
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Distributive Laws

>[!THEOREM] Theorem: Distributive Laws for Set Operations
>
>The [intersection](Set%20Operations.md#intersection), [union](Set%20Operations.md#union) and [difference](Set%20Operations.md#set%20difference) of all [sets](../index.md) $A,B,C$ obey the following distributive laws:
>
>$$
>A\cup (B\cap C) = (A\cup B) \cap (A\cup C)
>$$
>
>$$
>A\cap(B\cup C) = (A\cap B)\cup(A\cap C)
>$$
>
>$$
>A\setminus(B\cup C) = (A\setminus B)\cap (A\setminus C)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>