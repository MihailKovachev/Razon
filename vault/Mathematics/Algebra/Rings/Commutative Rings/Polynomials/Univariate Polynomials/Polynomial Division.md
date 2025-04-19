>[!THEOREM] Theorem: Polynomial Division
>
>Let $R$ be a [commutative ring](../../index.md) and let $A(x)$ and $B(x)$ be two [univariate polynomials](./index.md) over $R$ such that the [degree](../Polynomials.md) of $A$ is greater than or equal to the degree of $B$.
>
>If $B(x)$ is [nonzero](../Polynomials.md), then there exist unique polynomials $Q(x)$ and $R(x)$ such that
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
>The [remainder](Polynomial%20Division.md) $R$ upon the [division](Polynomial%20Division.md) of a [polynomial](./index.md) $A(x)$ with a polynomial $B(x) = x - p$ is the [value](../Polynomials.md) of $A$ at $p$.
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
>>Since the [degree](../Polynomials.md) of $B(x)$ is $1$, the degree of $R$ must either be $1$, i.e. $R$ is a constant and contains no variables or $R$ must be [zero](../Polynomials.md). We can therefore denote $R(x)$ as just $R$. For $x = p$ we obtain 
>>
>>$$
>>A(p) = (p-p)Q(p) + R = 0 + R = R
>>$$
>>
>

>[!ALGORITHM] Algorithm: Horner's Method
>
>Horner's method is a way to easily [divide](Polynomial%20Division.md) a [polynomial](../Polynomials.md) $A(x)$ by a [polynomial](../Polynomials.md) $B(x)$ of [degree](../Polynomials.md) one.
> 
>1. Write $B(x)$ as $B(x) = x - p$. Since $\deg(B) = 1$, the [remainder](Polynomial%20Division.md) $R$ is just a [real number](../../../../Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) because $\deg (R) \lt \deg(B) \implies \deg (R) = 0$. This means that we have
>
>$$
>A(x) = (x-p)Q(x) + R
>$$
>
>2. To determine $Q(x)$ and $R$, construct the following table:
> 
>||$a_n$|$a_{n-1}$|$\cdots$|$a_1$|$a_0$|
>|:--:|:--:|:--:|:--:|:--:|:--:|
>|$p$|$q_{n-1} = a_n$|$q_{n-2} = pq_{n-1} + a_{n-1}$|$\cdots$|$q_0 = pq_1 + a_1$|$R = pq_0 + a_0$|
>
>- We calculate the table from left to right.
>- The first coefficient $q_{n-1}$ of $Q(x)$ is equal to the first coefficient of $A(x)$, i.e. $q_{n-1} = a_n$.
> - For all other coefficients of $Q(x)$ we have $q_i = pq_{i+1} + a_{i-1}$.
> - At the end of the calculation, the right-most cell will contain $R$.
>
>>[!EXAMPLE]-
>>
>>Let $A(x) = 2x^5+3x^3-11x^2+6$ and $B(x) = x-3$. Create the table.
>>
>>||$2$|$0$|$3$|$-11$|$0$|$6$|
>>|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
>>|$p = 3$|||||||
>>
>>Perform the algorithm step by step.
>> 
>>||$2$|$0$|$3$|$-11$|$0$|$6$|
>>|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
>>|$p = 3$|2||||||
>> 
>>||$2$|$0$|$3$|$-11$|$0$|$6$|
>>|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
>>|$p = 3$|2|6|||||
>>
>>||$2$|$0$|$3$|$-11$|$0$|$6$|
>>|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
>>
>