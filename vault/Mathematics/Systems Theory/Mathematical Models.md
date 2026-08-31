---
tags:
    - systems-theory
    - mathematics
---

# Mathematical Models

>[!DEFINITION] Definition: Mathematical Model
>
>A **mathematical model** is a [pair](../Set%20Theory/Tuples.md) $(\mathbb{U}, \mathfrak{B})$ of a [set](../Set%20Theory/Sets.md) $\mathbb{U}$ and a [subset](../Set%20Theory/Subsets.md) $\mathfrak{B} \subseteq \mathbb{U}$:
>
>    - We call $\mathbb{U}$ the **universum** and its elements **outcomes**.
>    - We call $\mathfrak{B}$ the **behavior**.
>

>[!DEFINITION] Definition: Mathematical Model with Latent Variables
>
>A **mathematical model with latent variables** is a [triple](../Set%20Theory/Tuples.md) $(\mathbb{U}, \mathbb{U}_{\text{latent}}, \mathfrak{B}_{\text{full}})$ of two [sets](../Set%20Theory/Sets.md) $\mathbb{U}$ and $\mathbb{U}_{\text{latent}}$ and a [subset](../Set%20Theory/Subsets.md) $\mathfrak{B}_{\text{full}} \subseteq \mathbb{U} \times \mathbb{U}_{\text{latent}}$ of their [Cartesian product](../Set%20Theory/Cartesian%20Product.md):
>
>    - We call $\mathbb{U}$ the **universum of manifest variables**.
>    - We call $\mathbb{U}_{\text{latent}}$ the **universum of latent variables**.
>    - We call $\mathfrak{B}_{\text{full}}$ the **full behavior**.
>
>>[!DEFINITION] Definition: Manifest Mathematical Model
>>
>>The **manifest mathematical model** of $(\mathbb{U}, \mathbb{U}_{\text{latent}}, \mathfrak{B}_{\text{full}})$ is the [mathematical model](./Mathematical%20Models.md) $(\mathbb{U}, \mathfrak{B})$ whose [behavior](./Mathematical%20Models.md) $\mathfrak{B}$ is defined as follows:
>>
>>$$\mathfrak{B} = \{u \in \mathbb{U} \mid \exists l \in \mathbb{U}_{\text{latent}} \text{ with } (u, l) \in \mathfrak{B}_{\text{full}}\}$$
>>
>>We call $\mathfrak{B}$ the **manifest behavior** / **external behavior** / **behavior** of $(\mathbb{U}, \mathbb{U}_{\text{latent}}, \mathfrak{B}_{\text{full}})$.
>>
>

>[!DEFINITION] Definition: Latent Variable Representation
>
>A **latent variable representation** of a [mathematical model](./Mathematical%20Models.md) $(\mathbb{U}, \mathfrak{B})$ is any [mathematical model with latent variables](./Mathematical%20Models.md) $(\mathbb{U}, \mathbb{U}_{\text{latent}}, \mathfrak{B}_{\text{full}})$ whose [manifest mathematical model](./Mathematical%20Models.md) is $(\mathbb{U}, \mathfrak{B})$.
>