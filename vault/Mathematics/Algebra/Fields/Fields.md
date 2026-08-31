---
title: Fields
tags:
  - field-theory
  - abstract-algebra
  - algebra
  - mathematics
---

# Fields

>[!DEFINITION] Definition: Field
>
>A **field** $(F, +, \cdot)$ is a [set](../../Set%20Theory/Sets.md) $F$ equipped with two [operations](../../Analysis/Functions/Functions.md), **addition** $+: F \times F \to F$ and **multiplication** $\cdot: F \times F \to F$, which have the following properties:
>
>1. Addition Properties
>	- Associativity: $(a + b) + c = a + (b + c)$ for all $a, b, c \in F$.
>	- Commutativity: $a + b = b + a$ for all $a, b \in F$.
>	- Identity: There exists some $0_F \in F$ such that  $a + 0_F = a$ for all $a \in F$.
>	- Invertibility: For each $a \in F$, there exists some $a' \in F$ such that $a + a' = 0_F$.
>2. Multiplication Properties
>	- Associativity: $(a\cdot b) \cdot c = a \cdot (b \cdot c)$ for all $a,b,c \in R$.
>	- Commutativity: $a \cdot b = b \cdot a$ for all $a, b \in F$
>	- Identity: There exists some $1_F \in F$ such that $a \cdot 1_F = 1_F \cdot a = a$ for all $a \in F$.
>	- Invertibility: For each $a \in F$ with $a \ne 0_F$ there exists some $a' \in 0_F$ such that $a \cdot a' = 1_F$.
>3. Distributivity Properties
>	- Addition over Multiplication: $a \cdot (b + c) = a \cdot b + a \cdot c$ for all $a,b,c \in F$
>	- Multiplication over Addition: $(a+b) \cdot c = a\cdot c + b \cdot c$ for all $a,b,c \in F$
>	  
>>[!NOTATION]
>>
>>Let $a, b \in F$.
>>
>>We denote the additive inverse of $b \in F$ with $-b$ and write just $a - b$ instead of $a + (-b)$.
>>
>>We denote the multiplicative inverse of $b \in F$ with $b^{-1}$ and use any of the following for $a \cdot b^{-1}$:
>>
>>$$
>>a \div b \qquad a / b \qquad \frac{a}{b}
>>$$
>>
>

>[!THEOREM] Theorem: Field $\implies$ Ring
>
>Every [field](./Fields.md) $(F, +, \cdot)$ is also a [ring](../Rings/Rings.md) $(F, +, \cdot)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Field $\implies$ Abelian Group
>
>If $(F, +, \cdot)$ is a [field](./Fields.md), then $(F, \cdot)$ is an [abelian group](../Groups/Abelian%20Groups.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!EXAMPLE]-
>
>The [set](../../Set%20Theory/Sets.md) $\mathbb{Z}_p = \{0,1,\dotsc, p-1\}$ with [addition modulo](../Modular%20Arithmetic.md) $p$ and [multiplication modulo](../Modular%20Arithmetic.md) $p$ is a [field](./Fields.md).
>