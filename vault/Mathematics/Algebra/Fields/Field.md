> [!DEFINITION] Definition: Field
>A **field** $(F, +, \cdot)$ is an [integral domain](../Rings/Commutative%20Rings/Integral%20Domains/Integral%20Domain.md) where each nonzero element has a multiplicative inverse, i.e. for each $a \in F, a\ne 0$ there exists an element $a^{-1} \in F$ such that
>
>$$
>a \cdot a^{-1} = a^{-1} \cdot a = 1
>$$
>
>>[!THEOREM]- Theorem: Uniqueness of Multiplicative Inverses
>>
>>The multiplicative inverse of an element $a$ in a [field](Field.md) is unique.
>>
>>>[!PROOF]-
>>>
>>>Suppose there were two multiplicative inverses $a^{-1}$ and $a^{-1}{'}$.
>>>
>>>Since $a^{-1}$ is a multiplicative inverse, we have
>>>
>>>$$
>>>a \cdot a^{-1} = 1
>>>$$
>>>
>>>Similarly, since $a^{-1}{'}$ is a multiplicative inverse, we have
>>>
>>>$$
>>>a \cdot a^{-1}{'} = 1
>>>$$
>>>
>>>Combining the two equations, we obtain
>>>
>>>$$
>>>a \cdot a^{-1} = a \cdot a^{-1}{'}
>>>$$
>>>
>>>Multiply both sides by $a^{-1}$ - it does not matter whether we multiply from the left or from the right, since multiplication in integral domains is commutative.
>>>
>>>$$
>>>a^{-1} \cdot (a \cdot a^{-1}) = a^{-1} \cdot (a \cdot a^{-1}{'})
>>>$$
>>>
>>>We now avail ourselves of the associativity of multiplication.
>>>
>>>$$
>>>(a^{-1} \cdot a) \cdot a^{-1} = (a^{-1} \cdot a) \cdot a^{-1}{'}
>>>$$
>>>
>>>$$
>>>1 \cdot a^{-1} = 1 \cdot a^{-1}{'}
>>>$$
>>>
>>>$$
>>>a^{-1} = a^{-1}{'}
>>>$$
>>>
>>
>
