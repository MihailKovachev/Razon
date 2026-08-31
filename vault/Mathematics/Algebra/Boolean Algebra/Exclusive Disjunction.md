---
tags:
    - boolean-algebra
    - algebra
    - mathematics
---

# Exclusive Disjunction

>[!DEFINITION] Definition: Exclusive Disjunction
>
>The **exclusive disjunction function** is the [Boolean operator](./Boolean%20Functions.md) $\mathop{\operatorname{XOR}}: \{0, 1\}^2 \to \{0,1\}$ defined in the following way:
>
>$$
>\mathop{\operatorname{XOR}}(x, y) \overset{\text{def}}{=} \begin{cases} 1 \qquad \text{if } x \ne y \\ 0 \qquad \text{otherwise}\end{cases}
>$$
>
>
>>[!NOTATION]
>>
>>It is much more common to write $\mathop{\operatorname{XOR}}(x, y)$ in the following way:
>>
>>$$
>>x \oplus y
>>$$
>>
>

>[!THEOREM] Theorem: Associativity of Exclusive Disjunction
>
>The [exclusive disjunction](./Exclusive%20Disjunction.md) is associative:
>
>$$
>(x \oplus y) \oplus z = x \oplus (y \oplus x)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Commutativity of Exclusive Disjunction
>
>The [exclusive disjunction](./Exclusive%20Disjunction.md) is commutative:
>
>$$
>x \oplus y = y \oplus x
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>