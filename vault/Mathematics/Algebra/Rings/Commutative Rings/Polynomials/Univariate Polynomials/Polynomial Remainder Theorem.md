>[!THEOREM] Polynomial Remainder Theorem (Little Bézout's Theorem)
>
>The [remainder](Polynomial%20Division.md) $R$ upon the [division](Polynomial%20Division.md) of a [polynomial](Univariate%20Polynomial.md) $A(x)$ with a polynomial $B(x) = x - p$ is the [value](../Evaluation%20of%20a%20Polynomial.md) of $A$ at $p$.
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
>>Since the [degree](../Degree%20of%20a%20Polynomial.md) of $B(x)$ is $1$, the degree of $R$ must either be $1$, i.e. $R$ is a constant and contains no variables or $R$ must be [zero](../Zero%20Polynomial.md). We can therefore denote $R(x)$ as just $R$. For $x = p$ we obtain 
>>
>>$$
>>A(p) = (p-p)Q(p) + R = 0 + R = R
>>$$
>>
>