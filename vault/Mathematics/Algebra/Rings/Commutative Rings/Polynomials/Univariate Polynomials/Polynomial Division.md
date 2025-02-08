>[!THEOREM] Theorem: Polynomial Division
>
>Let $R$ be a [commutative ring](../../index.md) and let $A(x)$ and $B(x)$ be two [univariate polynomials](./index.md) over $R$ such that the [degree](../index.md) of $A$ is greater than or equal to the degree of $B$.
>
>If $B(x)$ is [nonzero](../Zero%20Polynomial.md), then there exist unique polynomials $Q(x)$ and $R(x)$ such that
>
>$$
>A(x) = Q(x)B(x) + R(x),
>$$
>
>where 
>- $\deg(Q) = \deg(A) - \deg(B)$
>- $\deg(R) \lt \deg(B)$ or $R(x)$ is the zero polynomial.
>
>We call $A$ the **dividend**, $B$ the **divisor**, $Q$ the **quotient** and $R$ the **remainder**.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Divisibility
>>
>>If $R(x) = 0$, then we say that $A$ is **divisible** by $B$.
>>
>

>[!THEOREM] Polynomial Remainder Theorem (Little Bézout's Theorem)
>
>The [remainder](Polynomial%20Division.md) $R$ upon the [division](Polynomial%20Division.md) of a [polynomial](./index.md) $A(x)$ with a polynomial $B(x) = x - p$ is the [value](../index.md) of $A$ at $p$.
>
>$$
>R = A(p)
>$$
>
>>[!PROOF]-
>>
>>The polynomial division theorem tells us that
>>
>>$$
>>A(x) = (x-p)Q(x) + R(x)
>>$$
>>
>>Since the [degree](../index.md) of $B(x)$ is $1$, the degree of $R$ must either be $1$, i.e. $R$ is a constant and contains no variables or $R$ must be [zero](../Zero%20Polynomial.md). We can therefore denote $R(x)$ as just $R$. For $x = p$ we obtain 
>>
>>$$
>>A(p) = (p-p)Q(p) + R = 0 + R = R
>>$$
>>
>