---
tags:
    - boolean-algebra
    - algebra
    - mathematics
---

# Boolean Expressions

TODO

>[!DEFINITION] Definition: Literal
>
>A **literal** in a [boolean expression](./Boolean%20Expressions.md) is either a [variable](./Boolean%20Expressions.md) or its [negation](./Negation.md).
>

>[!DEFINITION] Definition: Product Term
>
>A **product term** is a [conjunction](./Conjunction.md) of [literals](./Boolean%20Expressions.md).
>
>>[!EXAMPLE]
>>
>>$$
>>xy \qquad \overline{x}yz \qquad \overline{x}\overline{y} 
>>$$
>>
>

>[!DEFINITION] Definition: Clause
>
>A **clause** is a [disjunction](./Disjunction.md) of [literals](./Boolean%20Expressions.md).
>
>>[!EXAMPLE]
>>
>>$$
>>x + y \qquad \overline{x}+y+z \qquad \overline{x}+\overline{y} 
>>$$
>>
>

>[!DEFINITION] Definition: Minterm
>
>Given $n$ [variables](./Boolean%20Expressions.md), a **minterm** is a [conjunction](./Conjunction.md) in which each [variable](./Boolean%20Expressions.md) or its [negation](./Negation.md) appears exactly once.
>
>>[!EXAMPLE]
>>
>>If we have the [variables](./Boolean%20Expressions.md) $x, y, z$, then $x\overline{y}z$ and $\overline{x}\overline{y}\overline{z}$ are [minterms](./Boolean%20Expressions.md), but $xy$ is not.
>>
>
>>[!NOTATION]
>>
>>If we have $n$ [variables](./Boolean%20Expressions.md) $x_0, \dotsc, x_{n-1}$, we can give each [minterm](./Boolean%20Expressions.md) a unique label $m_k$, where $k$ is a non-negative integer which tells us what the [minterm](./Boolean%20Expressions.md) looks like. This is done by interpreting the [minterm](./Boolean%20Expressions.md) as a sequence of bits $b_0\cdots b_{n-1}$, where $b_i = 1$ if the [minterm](./Boolean%20Expressions.md) contains $x_i$ and $b_i = 0$ if it contains $\neg x_i$.
>>
>>>[!EXAMPLE]
>>>
>>>The [minterm](./Boolean%20Expressions.md) $m_3$ is $x_1x_0$, since $3_{10} = 11_{2}$. 
>>>
>>>The [minterm](./Boolean%20Expressions.md) $x_3 \overline{x_2} x_1 x_0$ has the label $m_{11}$, since $1011_{2} = 11_{10}$.
>>>
>>
>

>[!DEFINITION] Definition: Maxterm
>
>Given $n$ [variables](./Boolean%20Expressions.md), a **maxterm** is a [disjunction](./Disjunction.md) in which each [variable](./Boolean%20Expressions.md) or its [negation](./Negation.md) appears exactly once.
>
>>[!EXAMPLE]-
>>
>>If we have the [variables](./Boolean%20Expressions.md) $x, y, z$, then $x+\overline{y}+z$ and $\overline{x}+\overline{y}+\overline{z}$ are [maxterms](./Boolean%20Expressions.md), but $x+y$ is not.
>>
>
>>[!NOTATION]
>>
>>If we have $n$ [variables](./Boolean%20Expressions.md) $x_0, \dotsc, x_{n-1}$, we can give each [maxterm](./Boolean%20Expressions.md) a unique label $M_k$, where $k$ is a non-negative integer which tells us what the [maxterm](./Boolean%20Expressions.md) looks like. This is done by interpreting the [maxterm](./Boolean%20Expressions.md) as a sequence of bits $b_0\cdots b_{n-1}$, where $b_i = 1$ if the [maxterm](./Boolean%20Expressions.md) contains $\neg x_i$ and $b_i = 0$ if it contains $x_i$.
>>
>>>[!EXAMPLE]
>>>
>>>The [maxterm](./Boolean%20Expressions.md) $M_3$ is $\overline{x_1} + \overline{x_0}$, since $3_{10} = 11_{2}$. 
>>>
>>>The [maxterm](./Boolean%20Expressions.md) $\overline{x_3} + x_2 + \overline{x_1} + \overline{x_0}$ has the label $M_{13}$, since $1011_{2} = 11_{10}$.
>>>
>>
>

>[!DEFINITION] Definition: Conjunctive Normal Form
>
>A **conjunctive normal form** or **product of sums** is a [conjunction](./Conjunction.md) of one or more [clauses](./Boolean%20Expressions.md).
>
>>[!EXAMPLE]
>>
>>$$
>>(x + y)(y + z)(z + w) \qquad (x + y + z)z
>>$$
>>
>

>[!DEFINITION] Definition: Disjunctive Normal Form
>
>A **conjunctive normal form** or **sum of products** is a [disjunction](./Disjunction.md) of one or more [product terms](./Boolean%20Expressions.md).
>
>>[!EXAMPLE]
>>
>>$$
>>xy + yz + zw \qquad xyz + z
>>$$
>>
>