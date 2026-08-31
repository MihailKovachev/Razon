---
tags:
    - algebra
    - mathematics
---

# Rngs

>[!DEFINITION] Definition: Rng
>
>A **rng** $(R, +, \cdot)$ (pronounced "rung") is a [set](../../Set%20Theory/Sets.md) equppied with two [operations](../../Analysis/Functions/Functions.md) $+: R \times R \to R$ und $\cdot: R \times R \to R$ which have the following properties:
>
>1. Addition Properties
>	- Associativity: $(a + b) + c = a + (b + c)$ for all $a, b, c \in R$.
>	- Commutativity: $a + b = b + a$ for all $a, b \in R$.
>	- Identity: There exists some $0_R \in R$ such that  $a + 0_R = a$ for all $a \in R$.
>	- Invertibility: For each $a \in R$, there exists some $a' \in R$ such that $a + a' = 0_F$.
>2. Multiplication Properties
>	- Associativity: $(a\cdot b) \cdot c = a \cdot (b \cdot c)$ for all $a,b,c \in R$.
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
>