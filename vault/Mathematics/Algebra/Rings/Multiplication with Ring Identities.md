>[!THEOREM] Theorem: Multiplication with the Additive Identity
>
>Multiplying any element $a$ of a [ring](Ring.md) by its additive identity results in the additive identity.
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
>Multiplying any element $a$ of a [ring](Ring.md) by the additive inverse of the multiplicative identity results in the additive inverse of $a$.
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