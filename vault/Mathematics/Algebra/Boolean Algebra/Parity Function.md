---
tags:
    - boolean-algebra
    - algebra
    - mathematics
---

# Parity Function

>[!DEFINITION] Definition: Parity Function
>
>The $n$-variable **parity function** is the [Boolean function](./Boolean%20Functions.md) $f: \{0,1\}^n \to \{0, 1\}$ defined in the following way:
>
>$$
>f(x_1, \dotsc, x_n) = \begin{cases}1 \qquad \text{if an odd number of } x_1, \dotsc, x_n \text{ are equal to one} \\ 0 \qquad \text{otherwise}\end{cases}
>$$
>

>[!THEOREM] Theorem: Parity Function via Exclusive Disjunction
>
>The [parity function](./Parity%20Function.md) $f: \{0,1\}^n \to \{0, 1\}$ can be expressed via the [exclusive disjunction](./Exclusive%20Disjunction.md) in the following way:
>
>$$
>f(x_1, \dotsc, x_n) = x_1 \oplus \cdots \oplus x_n
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>