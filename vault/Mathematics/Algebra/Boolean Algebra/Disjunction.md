---
tags:
    - boolean-algebra
    - algebra
    - mathematics
---

# Disjunction

>[!DEFINITION] Definition: Disjunction
>
>The **disjunction function**  is the [Boolean function](./Boolean%20Functions.md) $\mathop{\operatorname{OR}}: \{0, 1\}^n \to \{0,1\}$ defined in the following way:
>
>$$
>\mathop{\operatorname{OR}}(x_1, \dotsc, x_n) \overset{\text{def}}{=} \begin{cases} 0 \qquad \text{if } x_1 = \cdots = x_n = 0 \\ 1 \qquad \text{otherwise}\end{cases}
>$$
>
>
>>[!NOTATION]
>>
>>It is much more common to write $\mathop{\operatorname{OR}}(x, y)$ in one of the following ways:
>>
>>$$
>>x \lor y \qquad x + y
>>$$
>>
>

>[!DEFINITION] Definition: Maxterm
>
>A [logical connective](../../../index.md) $f: \{0,1\}^n \to \{0,1\}$ is a **maxterm** if it can be expressed as the [disjunction](../../../index.md#Disjunction) of a combination of $n$ [negations](../../../index.md#Negations) and identity functions
>
>$$
>f(x_1, \dotsc, x_n) = \mathop{\operatorname{OR}}(x_1', \dotsc, x_n'),
>$$
>
>where $x_k'$ is either equal to $x_k$ or to its [negation](../../../index.md#Negations) $\neg x_k$.
>

>[!THEOREM] Theorem: Commutativity of Conjunction
>
>The [disjunction](./Disjunction.md) $\mathop{\operatorname{OR}}: \{0, 1\}^n \to \{0,1\}$ is commutative - if $y_1, \dotsc, y_n$ is any [permutation](TODO) of $x_1, \dotsc, x_n$, then
>
>$$
>\mathop{\operatorname{OR}}(y_1, \dotsc, y_n) = \mathop{\operatorname{OR}}(x_1, \dotsc, x_n)
>$$
>
>>[!TIP] Tip: Binary Disjunction
>>
>>In particular, we have:
>>
>>$$
>>x_1 \lor x_2 = x_2 \lor x_1
>>$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Associativity of Conjunction
>
>The [disjunction](./Disjunction.md) $\mathop{\operatorname{OR}}: \{0,1\}^2 \to \{0,1\}$ is associative:
>
>$$
>(x \lor y) \lor z = x \lor (y \lor z)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: General Disjunction from Binary Disjunction
>
>Any [disjunction](./Disjunction.md) $\mathop{\operatorname{OR}}: \{0, 1\}^n \to \{0,1\}$ can be obtained via [composition](../../Analysis/Functions/Functions.md) of binary [disjunctions](./Disjunction.md) $\mathop{\operatorname{OR}}: \{0,1\}^2 \to \{0,1\}$:
>
>$$
>\mathop{\operatorname{OR}}(x_1, \dotsc, x_n) = \mathop{\operatorname{OR}}(x_1, \mathop{\operatorname{OR}}(x_2, \mathop{\operatorname{OR}}(\cdots)))
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>


