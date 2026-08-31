---
tags:
    - systems-theory
    - mathematics
---

# Dynamical Systems with Latent Variables

>[!DEFINITION] Definition: Dynamical System with Latent Variables
>
>A **dynamical system** is a $4$-[tuple](../Set%20Theory/Tuples.md) $(\mathbb{T}, \mathbb{W}, \mathbb{L}, \mathfrak{B}_{\text{full}})$ of:
>
>- a [subset](../Set%20Theory/Subsets.md) $\mathbb{T} \subseteq \mathbb{R}$ of the [real numbers](../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md), known as the **time axis**;
>- a [set](../Set%20Theory/Sets.md) $\mathbb{W}$, known as the **(manifest) signal space**;
>- a [set](../Set%20Theory/Sets.md) $\mathbb{L}$, known as the **latent variable space**;
>- a [subset](../Set%20Theory/Subsets.md) $\mathfrak{B}_{\text{full}} \subseteq (\mathbb{W} \times \mathbb{L})^{\mathbb{T}}$ of the [set](../Set%20Theory/Sets.md) of all [functions](../Analysis/Functions/Functions.md) from $\mathbb{T}$ to the [Cartesian product](../Set%20Theory/Cartesian%20Product.md) $\mathbb{W} \times \mathbb{L}$, known as the **full behavior**.
>
>>[!DEFINITION] Definition: Manifest Dynamical System
>>
>>The **manifest dynamical system** of $(\mathbb{T}, \mathbb{W}, \mathbb{L}, \mathfrak{B}_{\text{full}})$ is the [dynamical system](./Dynamical%20Systems.md) $(\mathbb{T}, \mathbb{W}, \mathfrak{B})$ whose [behavior](./Dynamical%20Systems.md) $\mathfrak{B}$ is defined as follows:
>>
>>$$\mathfrak{B} = \{w: \mathbb{T} \to \mathbb{W} \mid \exists l: \mathbb{T} \to \mathbb{L} \text{ with } (w, l) \in \mathfrak{B}_{\text{full}}\}$$
>>
>