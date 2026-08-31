---
title: Relations
tags:
  - set-theory
  - mathematics
---

# Relations

>[!DEFINITION] Definition: Relation
>
>A **relation** $R \subseteq A \times B$ between two [sets](Sets.md#Sets) $A$ and $B$ is any [subset](Sets.md#Subsets) of the [Cartesian product](Sets.md#Operations) $A\times B$.
>
>>[!NOTATION]
>>
>>For any $a \in A$ and any $b \in B$, if $(a;b) \in R$, then we write
>>
>>$$
>>a\,\, R\,\, b
>>$$
>>
>
>>[!INTUITION]
>>
>>The statement $a \,\, R\,\, b$ translates to "there is a relationship between $a$ and $b$ which is expressed by $R$".
>>
>
>>[!EXAMPLE]-
>>
>>Let $R \subseteq \mathbb{N} \times \mathbb{N}$ be the relation
>>
>>$$
>>R = \{(a;b)\mid a,b \in \mathbb{N} \text{ and } b \text{ is a divisor of a} \}
>>$$
>>
>>For any $x,y \in \mathbb{N}$, the statement $x\,\, R\,\, y$ means that $(x,y) \in R$ which in this case translates to "$y$ is a divisor of $b$".
>>
>

>[!DEFINITION] Definition: Reflexive Relation
>
>A [relation](Relations.md) $R \subseteq A \times A$ is **reflexive** iff
>
>$$
>x\,\, R\,\, x
>$$
>
>is true for all $x\in A$.
>

>[!DEFINITION] Definition: Irreflexive Relation
>
>A [relation](Relations.md) $R \subseteq A \times A$ is **irreflexive** if there is no $x \in A$ such that
>
>$$
>x\,\, R\,\, x
>$$
>
>>[!NOTE]
>>
>>Irreflexive relations are also called **anti-reflexive** or **aliorelative**.
>>
>

>[!DEFINITION] Definition: Right-Unique Relation
>
>A [relation](Relations.md) $R\subseteq A\times B$ is **right-unique**, if for all $a \in A$ and all $b_1, b_2 \in B$
>
>$$
>((a\,\, R\,\, b_1)\land(a\,\, R\,\, b_1)) \implies b_1 = b_2
>$$
>

>[!DEFINITION] Definition: Symmetric Relation
>
>A [relation](Relations.md) $R \subseteq A \times A$ is **symmetric** if
>
>$$
>x\,\, R\,\, y \implies y\,\, R\,\, x
>$$
>
>for all $x,y \in A$.
>

>[!DEFINITION] Definition: Asymmetric Relation
>
>A [relation](Relations.md) $R \subseteq A \times A$ is **asymmetric** if
>
>$$
>((x\,\, R\,\, y) \land (y\,\, R \,\, x)) \implies x=y
>$$
>
>for all $x,y, \in A$
>

>[!DEFINITION] Definition: Transitivity
>
>A [relation](Relations.md) $R \subseteq A \times A$ is **transitive** iff
>
>$$
>((x\,\, R\,\, y) \land (y\,\, R \,\, z)) \implies x\,\, R \,\, z
>$$
>
>for all $x,y,z \in A$.
>

>[!DEFINITION] Definition: Equivalence Relation
>
>An **equivalence relation** on a [set](Sets.md) $A$ is any [relation](Relations.md) $R \subseteq A \times A$ which is [reflexive](Relations.md), [transitive](Relations.md) and [symmetric](Relations.md).
>
>>[!NOTATION]
>>
>>Equivalence relations are usually denoted with $\sim$ instead of $R$.
>>
>
>>[!INTUITION]
>>
>>The statement $x\sim y$ means that $x$ is equal to $y$ in the sense of $\sim$.
>>
>
>
>>[!DEFINITION] Definition: Equivalence Class
>>
>>Let $A$ be a [set](Sets.md) with an [equivalence relation](Relations.md) $\sim$.
>>
>>The **equivalence class** of an element $a \in A$ formed by $\sim$ is the [set](Sets.md) of all $x \in A$ such that $x \sim a$.
>>
>>
>>$$
>>\{x\in A\mid a\sim x\}
>>$$
>>
>>>[!NOTATION]
>>>
>>>$$
>>>[a]_\sim
>>>$$
>>>
>>
>