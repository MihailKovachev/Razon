---
tags:
    - real-analysis
    - vector-analysis
    - mathematical-analysis
    - analysis
---

# Reparametrization

>[!DEFINITION] Definition: Reparametrization
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^m \to \mathbb{R}^n$ and $g: \mathcal{D}_g \subseteq \mathbb{R}^m \to \mathbb{R}^n$ be [real vector functions](./Real%20Vector%20Functions.md).
>
>A **reparametrization** between $f$ and $g$ consists of a [bijective](../../Functions/Bijections.md) [function](./Real%20Vector%20Functions.md) $h_{\mathcal{D}_f \to \mathcal{D}_g}: \mathcal{D}_f \to \mathcal{D}_g$ and its [inverse](../../Functions/Bijections.md) $h_{\mathcal{D}_g \to \mathcal{D}_f}: \mathcal{D}_g \to \mathcal{D}_f$ with the following properties:
>
>$$\begin{aligned}f & = g \circ h_{\mathcal{D}_f \to \mathcal{D}_g} \\ g & = f \circ h_{\mathcal{D}_g \to \mathcal{D}_f}\end{aligned}$$
>

The above is the most general definition for [reparametrization](./Reparametrization.md). However, it is quite common to require that both $h_{\mathcal{D}_f \to \mathcal{D}_g}: \mathcal{D}_f \to \mathcal{D}_g$ and $h_{\mathcal{D}_g \to \mathcal{D}_f}: \mathcal{D}_g \to \mathcal{D}_f$ have additional properties such as [continuity](./Continuity%20(Real%20Vector%20Functions).md), [total differentiability](./Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md), etc. In those cases, when we say that a [reparametrization](./Reparametrization.md) has some property, we mean that both $h_{\mathcal{D}_f \to \mathcal{D}_g}: \mathcal{D}_f \to \mathcal{D}_g$ and $h_{\mathcal{D}_g \to \mathcal{D}_f}: \mathcal{D}_g \to \mathcal{D}_f$ have this property.

## Equivalence

In general, it is not always possible to find a [reparametrization](./Reparametrization.md) between two arbitrary [real vector functions](./Real%20Vector%20Functions.md).

>[!DEFINITION] Definition: Equivalence of Real Vector Functions
>
>Two [real vector functions](./Real%20Vector%20Functions.md) are **equivalent** if there exists a [reparametrization](./Reparametrization.md) between them.
>

Again, this is the most general definition of [equivalence](#Equivalence) for [real vector functions](./Real%20Vector%20Functions.md) and the term "equivalent" is used very broadly here. On its own, [equivalence](#Equivalence) does not guarantee many useful properties because the [reparametrization](./Reparametrization.md) is allowed to be arbitrary. When we want to emphasize the existence of a [reparametrization](./Reparametrization.md) with specific properties such as [continuity](./Continuity%20(Real%20Vector%20Functions).md), [total differentiability](./Differentiation/Total%20Differentiability%20(Real%20Vector%20Functions).md), etc., we say that the [functions](./Real%20Vector%20Functions.md) are **equivalent up to a "PROPERTY" reparametrization**.

>[!THEOREM] Theorem: Equivalence $\implies$ Equal Images
>
>If two [real vector functions](./Real%20Vector%20Functions.md) are [equivalent](#Equivalence), then they have the same [image](../../Functions/Functions.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>