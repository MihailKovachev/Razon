---
tags:
    - boolean-algebra
    - algebra
    - mathematics
---

# Conjunction

>[!DEFINITION] Definition: Conjunction
>
>A **conjunction function** is a [Boolean operator](./Boolean%20Functions.md) $\mathop{\operatorname{AND}}: \{0, 1\}^n \to \{0,1\}$ defined in the following way:
>
>$$
>\mathop{\operatorname{AND}}(x_1, \dotsc, x_n) \overset{\text{def}}{=} \begin{cases} 1 \qquad \text{if } x_1 = \cdots = x_n = 1 \\ 0 \qquad \text{otherwise}\end{cases}
>$$
>
>
>>[!NOTATION]
>>
>>It is much more common to write $\mathop{\operatorname{AND}}(x, y)$ in one of the following ways:
>>
>>$$
>>x \land y \qquad x \cdot y \qquad xy
>>$$
>>
>

>[!THEOREM] Theorem: Commutativity of Conjunction
>
>The [conjunction](./Conjunction.md) $\mathop{\operatorname{AND}}: \{0, 1\}^n \to \{0,1\}$ is commutative - if $y_1, \dotsc, y_n$ is any [permutation](TODO) of $x_1, \dotsc, x_n$, then
>
>$$
>\mathop{\operatorname{AND}}(y_1, \dotsc, y_n) = \mathop{\operatorname{AND}}(x_1, \dotsc, x_n)
>$$
>
>>[!TIP] Tip: Binary Conjunction
>>
>>In particular, we have:
>>
>>$$
>>x_1 \land x_2 = x_2 \land x_1
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
>The [conjunction](./Conjunction.md) $\mathop{\operatorname{AND}}: \{0,1\}^2 \to \{0,1\}$ is associative:
>
>$$
>(x \land y) \land z = x \land (y \land z)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: General Conjunction from Binary Conjunction
>
>Any [conjunction](./Conjunction.md) $\mathop{\operatorname{AND}}: \{0, 1\}^n \to \{0,1\}$ can be obtained via [composition](../../Analysis/Functions/Functions.md) of binary [conjunctions](./Conjunction.md) $\mathop{\operatorname{AND}}: \{0,1\}^2 \to \{0,1\}$:
>
>$$
>\mathop{\operatorname{AND}}(x_1, \dotsc, x_n) = \mathop{\operatorname{AND}}(x_1, \mathop{\operatorname{AND}}(x_2, \mathop{\operatorname{AND}}(\cdots)))
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

