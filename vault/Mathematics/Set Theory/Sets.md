---
tags:
  - set-theory
  - mathematics
---

# Sets

>[!DEFINITION] Definition: Set
>
>A **set** is a collection of well-defined objects, called **elements**. 
>
>>[!NOTATION]-
>>
>>The notation $a \in A$ means that $a$ is an element of the set $A$.
>>
>>The notation $a \notin A$ means that $a$ is *not* an element of the set $A$.
>>
>
>>[!NOTE]
>>
>>- A set can contain pretty much anything - numbers, letters, cars, sentences, people, colours and even other sets.
>>- A set  can contain either finitely many or infinitely many elements.
>

>[!DEFINITION] Definition: Singleton
>
>A **singleton** is a [set](./Sets.md) with exactly one element.
>

>[!DEFINITION] Definition: Equality
>
>Two [set](./Sets.md) are **equal** if they contain the same elements.
>

>[!AXIOM] Axiom: Existence of an Empty Set
>
>There exists a [set](./Sets.md) with no elements.
>
>$$
>\exists A: \forall x:x \notin A
>$$
>
>>[!NOTATION]
>>
>>$$
>>\varnothing \qquad \emptyset \qquad \{\}
>>$$
>>
>

>[!THEOREM] Theorem: Uniqueness of the Empty Set
>
>There is only one [empty set](./Sets.md).
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

>[!THEOREM] Theorem: Empty Set as Subset of all Sets
>
>The [empty set](./Sets.md) is a [subset](./Sets.md) of all [set](./Sets.md).
>
>>[!PROOF]-
>>
>>Let $A$ be a set.
>>
>>Suppose that the empty set $\varnothing$ is *not* a subset of $A$. Then there must exist an element $e \in \varnothing$ which is not an element of $A$, i.e. $e \notin A$. This is a contradiction, since the empty set contains no elements.
>>
>

There are three main ways to represent and define sets.

The *descriptive form* uses words to describe a set. For example, the set $S$ is the set of all odd natural numbers which are less than 12.

The *set-builder form* defines a set by specifying a condition that all of its members satisfies and looks like this:

$$
\text{set} = \{\text{ placeholder }|\text{ condition }\}
$$

The placeholder is simply there so you can use it to more easily write the condition. The `|` character can be read as "such that". For example, specifying the aforementioned set $S$ using set-builder notation will look like the following.

$$
S = \{s|s \text{ is an odd number and } 0 \lt s \lt 12\}
$$

The final way to define a set is simply by listing all of its elements or listing enough of them, so that whoever is reading the definition can easily establish the pattern they follow. For example, the aforementioned set will be written as

$$
S = \{1,3,5,7,9,11\}
$$

# Subsets

>[!DEFINITION] Definition: Subset
>
>A [set](./Sets.md) $A$ is a **subset** of another [set](./Sets.md) $B$ if all elements of $A$ are also elements of $B$.
>
>$$
>a \in A \implies a \in B
>$$
>
>>[!NOTATION]
>>
>>If $A$ is a subset of $B$, we write $A \subseteq B$. Some people also write $A \subset B$, but this notation can be ambiguous.
>>
>>If $A$ is *not* a subset of $B$, we write $A \not\subseteq B$ or $A \not \subset B$.
>>
>
>>[!DEFINITION] Definition: True Subset
>>
>>A [set](./Sets.md) $A$ is a **true subset** / **strict subset** of another [set](./Sets.md) $B$ $B$ if $A \subseteq B$ and $A \ne B$.
>>
>>$$
>>(a\in A \implies a\in B) \land (\exists b \in B : b \notin A)
>>$$
>>
>>>[!NOTATION]
>>>
>>>If $A$ is a true subset of $B$, we write $A \subsetneq B$. Some people also write $A \subset B$, but this notation can be ambiguous.
>>>
>>
>
>>[!DEFINITION] Definition: (Strict) Superset
>>
>>A [set](./Sets.md) $A$ is a **(strict) superset** of another [set](./Sets.md) $B$ if $B$ is a [(strict) subset](#Subsets) of $A$.
>>
>>>[!NOTATION]
>>>
>>>$$
>>>A \supseteq B \qquad A \supset B
>>>$$
>>>
>>
>

>[!DEFINITION] Definition: Power Set
>
>The **power set** of a [set](./Sets.md) $M$ is the [collection](./Collections.md) of all [subsets](#Subsets) of $M$.
>
>$$
>\{T \mid T \subseteq M\}
>$$
>
>>[!NOTATION]
>>
>>$$
>>\mathscr{P}(M) \qquad \mathcal{P}(M) \qquad \mathsf{P}(M) \qquad P(M) \qquad \mathbb{P}(M) \qquad 2^M
>>$$
>>
>

>[!DEFINITION] Definition: Indicator Function
>
>Let $S$ be a [subset](#Subsets) of a [set](./Sets.md) $X$.
>
>The **indicator function** of $S$ is the [function](../Analysis/Functions/Functions.md) $\mathbf{1}_S: X \to \{0, 1\}$ defined as
>
>$$
>\mathbf{1}_S(x) = \begin{cases} 1 \qquad \text{if } x \in S \\ 0 \qquad \text{if } x \notin S \end{cases}
>$$
>

# Operations

>[!DEFINITION] Definition: Union
>
>The **union** of two [sets](./Sets.md) $A$ and $B$ is the [set](./Sets.md) which contains exactly the elements which are in $A$, in $B$ or in both $A$ and $B$.
>
>$$
>\{x \mid x\in A  \lor x\in B\}
>$$
>
>>[!NOTATION]
>>
>>$$
>>A \cup B
>>$$
>>
>

>[!DEFINITION] Definition: Intersection
>
>The **intersection** of two [sets](./Sets.md) $A$ and $B$ is the [set](./Sets.md) of all elements which are both in $A$ and in $B$.
>
>$$
>\{ x \mid x\in A \land x \in B\}
>$$
>
>>[!NOTATION]
>>
>>$$
>>A \cap B
>>$$
>>
>
>>[!DEFINITION] Definition: Disjoint Sets
>>
>>We say that $A$ and $B$ are **disjoint** if their [intersection](#Operations) is the [empty set](./Sets.md).
>>
>>$$
>>A \cap B = \varnothing
>>$$
>>
>

>[!DEFINITION] Definition: Set Difference
>
>The **set difference** $A \setminus B$ of two [sets](./Sets.md) $A$ and $B$ is the [set](./Sets.md) which contains exactly the elements in $A$ which are not elements of $B$.
>
>$$
>\{x \mid x \in A \land x \notin B\}
>$$
>
>>[!NOTATION]
>>
>>$$
>>A \setminus B \qquad A - B
>>$$
>>
>
>>[!DEFINITION] Definition: Complement
>>
>>Let $B$ be a [subset](./Sets.md) of a [set](./Sets.md) $A$.
>>
>>The **complement** of $B$ in $A$ is the [difference](#Operation) $A \setminus B$.
>>
>

>[!DEFINITION] Definition: Symmetric Difference
>
>The **symmetric difference** of two [sets](./Sets.md) $A$ and $B$ is the [set](./Sets.md) of all elements which are only in $A$ and those elements which are only in $B$:
>
>$$
>(A \cup B) \setminus (A \cap B)
>$$
>
>>[!NOTATION]
>>
>>$$
>>A \triangle B \qquad A \oplus B
>>$$
>>
>

>[!DEFINITION] Definition: Cartesian Product
>
>Let $A_1, \dotsc, A_n$ be [non-empty](./Sets.md) [sets](./Sets.md).
>
>The **Cartesian product** $A \times \cdots \times A_n B$ is the [set](./Sets.md) of all [ordered pairs](./Tuples.md) $(a_1, \dotsc, a_n)$ such that $a_i \in A_i$:
>
>$$
>A\times B \overset{\text{def}}{=} \{(a; b)\mid a\in A \land b \in B\}
>$$
>

>[!THEOREM] Theorem: Cardinality of the Set Union
>
>The [union](#Operations) of two [finite](./Cardinality.md) [sets](./Sets.md) $A$ and $B$ has [cardinality](./Cardinality.md)
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
>The [union](#Operations) of two [sets](./Sets.md) $A$ and $B$ is commutative:
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

>[!THEOREM] Theorem: Commutativity of Set Intersection
>
>The [intersection](#Operations) of two [sets](./Sets.md) $A$ and $B$ is commutative:
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
>The [intersection](#Operations) of [sets](./Sets.md) is associative:
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

>[!THEOREM] Theorem: Cardinality of the Cartesian Product
>
>The [Cartesian product](#Operations) of two [finite](./Cardinality.md) [sets](./Sets.md) $A$ and $B$ has [cardinality](./Cardinality.md)
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

>[!THEOREM] Theorem: Distributive Laws for Set Operations
>
>The [set operations](#Operations) have the following properties:
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

