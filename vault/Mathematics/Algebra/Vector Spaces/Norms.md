---
tags:
  - linear-algebra
  - algebra
  - mathematics
---

# Norms

>[!DEFINITION] Definition: Norm
>
>A **norm** on a [complex](../Fields/The%20Complex%20Numbers/Complex%20Numbers.md) or a [real](../Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) [vector space](./Vector%20Spaces.md) $(V,F,+,\cdot)$, where $F$ is $\mathbb{C}$ or $\mathbb{R}$, is any [function](../../Analysis/Functions/Functions.md) $N: V \to \mathbb{R}$ with the following properties:
>
>- $N(\mathbf{v})\ge 0$ and $N(\mathbf{v})=0\iff \mathbf{v}=\mathbf{0}$ for all $\mathbf{v}\in V$
>- $N(\lambda\mathbf{v}) = |\lambda|\cdot N(\mathbf{v})$ for all $\lambda\in F,\mathbf{v}\in V$
>- $N(\mathbf{u}+\mathbf{v})\le N(\mathbf{u})+N(\mathbf{v})$ for all $\mathbf{u},\mathbf{v}\in V$ (triangle inequality)

>[!DEFINITION] Definition: Normed Vector Space
>
>A **normed vector space** is a [vector space](../../../index.md#Vector%20Spaces) equipped with a [norm](./Norms.md).
>

>[!DEFINITION] Definition: Unit Vector
>
>A **unit vector** in a [normed vector space](./Norms.md) is any [vector](../../../index.md#Vector%20Spaces) whose [norm](./Norms.md) is equal to $1$.
>
>>[!NOTATION] Notation
>>
>>Unit vectors are usually denoted with hats: $\mathbf{\hat{u}}, \mathbf{\hat{v}}$, etc.
>>
>