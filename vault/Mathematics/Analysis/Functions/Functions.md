---
title: Restriction
tags:
  - functions
  - analysis
  - mathematics
---

>[!DEFINITION] Definition: Function
>
>A **function** $f: \mathcal{D} \to C$ from a [set](../../Set%20Theory/Sets.md) $\mathcal{D}$ to a [set](../../Set%20Theory/Sets.md) $C$ is a [right-unique](../../Set%20Theory/Relations.md) [relation](../../Set%20Theory/Relations.md) $f \subseteq \mathcal{D} \times C$.
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
>>The **image** of $f$ is the [set](../../Set%20Theory/Sets.md) of all $y \in C$ for which there is at least one $x \in \mathcal{D}$ such that $y = f(x)$.
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
>>>f(\mathcal{D}) \qquad f[\mathcal{D}]
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
>>A function $f$ is just a rule which to each $x \in \mathcal{D}$ assigns a single $f(x) \in C$.
>>
>

>[!DEFINITION] Definition: Inverse Image
>
>Let $f: X \to Y$ be a [function](Functions.md).
>
>The **inverse image** of a [subset](../../Set%20Theory/Subsets.md) $S \subseteq Y$ under $f$ is the subset of $X$ defined as
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

>[!DEFINITION] Definition: Restriction
>
>Let $f: X \to Y$ be a [function](Functions.md).
>
>The **restriction** of $f$ on a [subset](../../Set%20Theory/Subsets.md) $S \subseteq X$ is the function $f\big|_S: S \to Y$ defined as
>
>$$
>f\big|_S (x) = f(x) \qquad \forall x \in S
>$$
>