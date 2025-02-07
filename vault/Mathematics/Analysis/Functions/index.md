---
title: Functions
tags:
    - functions
    - analysis
    - mathematics
---

>[!DEFINITION] Definition: Function
>
>A **function** $f: D \to C$ from a [set](../../Set%20Theory/Set.md) $D$ to a [set](../../Set%20Theory/Set.md) $C$ is a [right-unique](../../Set%20Theory/Relations/Right-Unique%20Relation.md) [relation](../../Set%20Theory/Relations/Relation.md) $f \subseteq D\times C$.
>
>![](res/Function.drawio.svg)
>
>>[!DEFINITION] Definition: Domain
>>
>>We call $\mathcal{D}$ the **domain** of $f$.
>>
>
>>[!DEFINITION] Definition: Codomain
>>
>>We call $C$ the **codomain** of $f$.
>>
>
>>[!DEFINITION] Definition: Image
>>
>>The **image** of $f$ is the [set](../../Set%20Theory/Set.md) of all $y \in C$ for which there is at least one $x \in \mathcal{D}$ such that $y = f(x)$.
>>
>>$$
>>\{f(x) \mid x \in D\}
>>$$
>>
>>![](res/Image.svg)
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>f(D) \qquad f[D]
>>>$$
>>>
>>
>>>[!INTUITION]-
>>>
>>>The image of a function is essentially the set of all values in $C$ which $f$ can produce.
>>>
>>
>
>>[!INTUITION]-
>>
>>A function $f$ is just a rule which to each $x \in D$ assigns a single $f(x) \in C$.
>>
>

>[!DEFINITION] Definition: Inverse Image
>
>Let $f: X \to Y$ be a [function](index.md).
>
>The **inverse image** of a [subset](../../Set%20Theory/Subset.md) $S \subseteq Y$ under $f$ is the subset of $X$ defined as
>
>$$
>\{x \in X \mid f(x) \in S \}
>$$
>
>>[!NOTATION]-
>>
>>$$
>>f^{-1} [S] \qquad f^{-1}(S) \qquad f^{-}(S)
>>$$
>>
>
