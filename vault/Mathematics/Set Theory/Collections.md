---
title: Collections
tags:
  - set-theory
  - mathematics
---

# Collections

>[!DEFINITION] Definition: Collection
>
>A **collection** / **set system** / **family of sets** is a [set](Sets.md) whose elements are only [set](Sets.md).
>
>

>[!DEFINITION] Definition: Subcollection
>
>A **subcollection** of a [collection](Collections.md) $\mathcal{C}$ is just a [subset](Sets.md#Subsets) of $\mathcal{C}$.
>

# Operations

>[!DEFINITION] Definition: Union of a Collection
>
>The **union** of a [collection](Collections.md) $\mathcal{C}$ is the [set](Sets.md#Sets) of all elements which belong to at least one of the [sets](Sets.md#Sets) in $\mathcal{C}$.
>
>$$
>\{x \mid \exists E\in \mathcal{C}  : x\in E \}
>$$
>
>>[!NOTATION]
>>
>>Usually, the union of a collection is denoted by
>>
>>$$
>>\bigcup \mathcal{C}
>>$$
>>
>>However, an alternative notation is more useful when we need to consider specific elements of $\mathcal{C}$. In this case, indexing notation using an [index set](Indexing.md) $I$ for $\mathcal{C}$ is used.
>>
>>$$
>>\bigcup_{i \in I} \mathcal{C}_i
>>$$
>>
>

>[!DEFINITION] Definition: Intersection of a Collection
>
>The **intersection** of a [collection](Collections.md) $\mathcal{C}$ is the [set](Sets.md#Sets) of elements which belong simultaneously to every [set](Sets.md#Sets) of $\mathcal{C}$.
>
>$$
>\{x \mid \forall E \in \mathcal{C}:  x \in \mathcal{C}\}
>$$
>
>>[!NOTATION]
>>
>>Usually, the intersection of a collection is denoted by
>>
>>$$
>>\bigcap \mathcal{C}
>>$$
>>
>>However, an alternative notation is more useful when we need to consider specific elements of $\mathcal{C}$. In this case, indexing notation using an [index set](Indexing.md) $I$ for $\mathcal{C}$ is used.
>>
>>$$
>>\bigcap_{i \in I} \mathcal{C}_i
>>$$
>>
>