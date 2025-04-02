---
title: The Empty Set
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

## Specifying Sets

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

## Equality

>[!DEFINITION] Definition: Equality
>
>Two [sets](Sets.md) are **equal** iff they contain the same elements.
>

# Subsets

>[!DEFINITION] Definition: Subset
>
>A [set](Sets.md) $A$ is a **subset** of the [set](Sets.md) $B$ if all elements of $A$ are also elements of $B$.
>
>$$
>a \in A \implies a \in B
>$$
>
>>[!NOTATION]-
>>
>>If $A$ is a subset of $B$, we write $A \subseteq B$.
>>
>>If $A$ is *not* a subset of $B$, we write $A \not\subseteq B$.
>>
>
>>[!DEFINITION] Definition: True Subset
>>
>>A [set](Sets.md) $A$ is a **true subset** of the [set](Sets.md) $B$ if $A \subseteq B$ and $A \ne B$.
>>
>>$$
>>(a\in A \implies a\in B) \land (\exists b \in B : b \notin A)
>>$$
>>
>>In other words, there are elements in $B$ which are *not* elements of $A$.
>>
>>>[!NOTATION]-
>>>
>>>If $A$ is a true subset of $B$, we write $A \subset B$.
>>>
>>>If $A$ is a subset, but not a *true* subset, of $B$, we write $A \subsetneq B$.
>>>
>>
>>>[!NOTE]
>>>
>>>True subset are also known as **strict subsets**.
>>>
>>
>

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