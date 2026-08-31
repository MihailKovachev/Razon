---
tags:
    - systems-theory
    - mathematics
---

# Dynamical Systems

>[!DEFINITION] Definition: Dynamical System
>
>A **dynamical system** is a $3$-[tuple](../Set%20Theory/Tuples.md) $(\mathbb{T}, \mathbb{W}, \mathfrak{B})$ of:
>
>    - a [subset](../Set%20Theory/Subsets.md) $\mathbb{T} \subseteq \mathbb{R}$ of the [real numbers](../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md), known as the **time axis**;
>    - a [set](../Set%20Theory/Sets.md) $\mathbb{W}$, known as the **signal space**;
>    - a [subset](../Set%20Theory/Subsets.md) $\mathfrak{B} \subseteq \mathbb{W}^{\mathbb{T}}$ of the [set](../Set%20Theory/Sets.md) of all [functions](../Analysis/Functions/Functions.md) from $\mathbb{T}$ to $\mathbb{W}$, known as the **behavior**.
>
>Each element of $\mathfrak{B}$ is called a **trajectory**.
>

>[!DEFINITION] Definition: Latent Variable Representation
>
>A **latent variable representation** of a [dynamical system](./Dynamical%20Systems.md) $(\mathbb{T}, \mathbb{W}, \mathfrak{B})$ is any [dynamical system with latent variables](./Dynamical%20Systems.md) $(\mathbb{T}, \mathbb{W}, \mathbb{L}, \mathfrak{B}_{\text{full}})$ whose [manifest dynamical system](./Dynamical%20Systems.md) is $(\mathbb{T}, \mathbb{W}, \mathfrak{B})$.
>