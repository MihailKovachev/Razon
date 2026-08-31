---
tags:
  - ring-theory
  - algebra
  - mathematics
---

# Rings

>[!DEFINITION] Definition: Ring
>
>A **ring** $(R, +, \cdot)$ is a [set](../../Set%20Theory/Sets.md) equppied with two [operations](../../Analysis/Functions/Functions.md) $+: R \times R \to R$ und $\cdot: R \times R \to R$ which have the following properties:
>
>1. Addition Properties
>	- Associativity: $(a + b) + c = a + (b + c)$ for all $a, b, c \in R$.
>	- Commutativity: $a + b = b + a$ for all $a, b \in R$.
>	- Identity: There exists some $0_R \in R$ such that  $a + 0_R = a$ for all $a \in R$.
>	- Invertibility: For each $a \in R$, there exists some $a' \in R$ such that $a + a' = 0_F$.
>2. Multiplication Properties
>	- Associativity: $(a\cdot b) \cdot c = a \cdot (b \cdot c)$ for all $a,b,c \in R$.
>	- Identity: There exists some $1_R \in R$ such that $a \cdot 1_R = 1_R \cdot a = a$ for all $a \in R$.
>3. Distributivity Properties
>	- Addition over Multiplication: $a \cdot (b + c) = a \cdot b + a \cdot c$ for all $a,b,c \in R$
>	- Multiplication over Addition: $(a+b) \cdot c = a\cdot c + b \cdot c$ for all $a,b,c \in R$
>
>>[!NOTATION]
>>
>>When it is clear from context which ring we are talking about, we can write simply $0$ and $1$ for the additive and multiplicative identities, respectively.
>>
>>Multiplication is often denoted as $ab$ or $a\times b$ instead of $a\cdot b$.
>>
>>Multiplying an element by itself $n$ times is denoted as
>>
>>$$
>>a^n = \underset{n \text{ times}}{\underbrace{a \times \cdots \times a}}
>>$$
>>
>>We also define $a^0 = 1_R$ for every $a \in R, a \ne 0$.
>>
>
>>[!WARNING] Warning: Ring vs Rng
>>
>>In older texts, [rings](./Rings.md) may be defined without a multiplicative identity, i.e. equivalently to [rngs](./Rngs.md).
>>
>


>[!THEOREM] Theorem: Ring $\implies$ Abelian Group
>
>If $(R, +, \cdot)$ is a [ring](./Rings.md), then $(R, +)$ is an [abelian group](../Groups/Abelian%20Groups.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Ring $\implies$ Semigroup
>
>If $(R, +, \cdot)$ is a [ring](./Rings.md), then $(R, \cdot)$ is a [semigroup](../Groups/Groups.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!EXAMPLE]- Example: 
>
>We structures $(\mathbb{Z}, +, \cdot)$, $(\mathbb{Q},+,\cdot)$ and $(\mathbb{R}, +, \cdot)$ are [rings](./Rings.md).
>

>[!EXAMPLE]- Example
>
>The [set](../../Set%20Theory/Sets.md) of all [polynomials](./Commutative%20Rings/Polynomials/Polynomials.md) with [polynomial addition](TODO) and [polynomial multiplication](TODO) is a [ring](./Rings.md).
>

>[!THEOREM] Theorem: Multiplication with the Additive Identity
>
>Multiplying any element $a$ of a [ring](../../../index.md) by its additive identity results in the additive identity.
>
>$$
>a \cdot 0 = 0 \cdot a = 0
>$$
>
>>[!PROOF]-
>>
>>The property of the additive identity tells us that $0 = 0 + 0$ and so
>>
>>$$
>>a \cdot 0 = a \cdot (0 + 0)
>>$$
>>
>>The distributivity of multiplication gives us
>>
>>$$
>>a \cdot (0 + 0) = a \cdot 0 + a \cdot 0
>>$$
>>
>>$$
>>a \cdot 0 = a \cdot 0 + a \cdot 0
>>$$
>>
>>By the existence of additive inverses we obtain
>>
>>$$
>>(1) \qquad a \cdot 0 + (- (a \cdot 0)) = (a \cdot 0 + a \cdot 0) + (- (a \cdot 0))
>>$$
>>
>>Associativity entails
>>
>>$$
>>(2) \qquad (a \cdot 0 + a \cdot 0) + (- (a \cdot 0)) = a \cdot 0 + (a \cdot 0 + (- (a \cdot 0)))
>>$$
>>
>>Combining $(1)$ and $(2)$ we get
>>
>>$$
>>a \cdot 0 + (- (a \cdot 0)) = a \cdot 0 + (a \cdot 0 + (- (a \cdot 0)))
>>$$
>>
>>The property of the additive identity also tells us that
>>
>>$$
>>a \cdot 0 + (- (a \cdot 0)) = 0
>>$$
>>
>>Therefore,
>>
>>$$
>>a \cdot 0 + (- (a \cdot 0)) = a \cdot 0 + (a \cdot 0 + (- (a \cdot 0)))
>>$$
>>
>>$$
>>0 = a \cdot 0 + 0 = a \cdot 0
>>$$
>>
>>The proof for $0 \cdot a$ is analogous.
>>
>

>[!THEOREM] Theorem: Multiplication with the Additive Inverse of the Multiplicative Identity
>
>Multiplying any element $a$ of a [ring](../../../index.md) by the additive inverse of the multiplicative identity results in the additive inverse of $a$.
>
>$$
>(-1)\cdot a = a \cdot (-1) = -a
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>