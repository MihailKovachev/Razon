---
title: Complex-Valued Function
tags:
    - complex-analysis
    - analysis
    - mathematics
---

# Complex-Valued Functions

>[!DEFINITION] Definition: Complex-Valued Function
>
>A **complex-valued function** on a [set](../../Set%20Theory/Sets.md) $X$ is a [function](../Functions/index.md) $f: X \to \mathbb{C}$ from $X$ to the set of the [complex numbers](../../Algebra/Fields/The%20Complex%20Numbers/index.md).
>
>>[!DEFINITION] Definition: Real Part
>>
>>The **real part** of $f$ is the [real-valued function](../Real%20Analysis/Real-Valued%20Function.md) $\operatorname{Re} f: X \to \mathbb{R}$ which, for each $x \in X$, returns the [real part](../../Algebra/Fields/The%20Complex%20Numbers/index.md) of $f(x)$.
>>
>>$$
>>\operatorname{Re} f (x) \overset{\text{def}}{=} \operatorname{Re}(f(x)) \qquad \forall x \in X
>>$$
>>
>
>>[!DEFINITION] Definition: Imaginary Part
>>
>>The **imaginary part** of $f$ is the [real-valued function](../Real%20Analysis/Real-Valued%20Function.md) $\operatorname{Im} f: X \to \mathbb{R}$ which, for each $x \in X$, returns the [imaginary part](../../Algebra/Fields/The%20Complex%20Numbers/index.md) of $f(x)$.
>>
>>$$
>>\operatorname{Im} f (x) \overset{\text{def}}{=} \operatorname{Im}(f(x)) \qquad \forall x \in X
>>$$
>>
>

# Operations with Complex-Valued Functions

>[!DEFINITION] Definition: Function Operations
>
>Let $f: \mathcal{D}_f \to \mathbb{C}$ and $g: \mathcal{D}_g \to \mathbb{C}$ be [complex-valued functions](Complex-Valued%20Functions.md).
>
>- The **sum** of $f$ and $g$ is the [function](Complex-Valued%20Functions.md) $f + g: \mathcal{D}_f \cap \mathcal{D}_g \to \mathbb{C}$ defined as
>
>$$
>(f+g)(x) \overset{\text{def}}{=} f(x) + g(x) \qquad \forall x \in \mathcal{D}_f \cap \mathcal{D}_g 
>$$
>
>- The **product** of $f$ and $g$ is the [function](Complex-Valued%20Functions.md) $fg: \mathcal{D}_f \cap \mathcal{D}_g \to \mathbb{C}$ defined as
>
>$$
>(fg)(x) \overset{\text{def}}{=} f(x) \cdot g(x) \qquad \forall x \in \mathcal{D}_f \cap \mathcal{D}_g 
>$$
>
>- The **ratio** of $f$ and $g$ is the [function](Complex-Valued%20Functions.md) $fg: \mathcal{D}_f \cap \mathcal{D}_g \to \mathbb{C}$ defined as
>
>$$
>f/g (x) \overset{\text{def}}{=} \frac{f(x)}{g(x)} \qquad \forall x \in \mathcal{D}_f \cap \mathcal{D}_g 
>$$
>
