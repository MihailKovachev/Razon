>[!THEOREM] Theorem: Roots of Univariate Polynomials
>
>Let $A(x)$ be a [univariate polynomial](Univariate%20Polynomial.md) over a [commutative ring](../../Commutative%20Ring.md) $R$.
>
>An element $p \in R$ is a [root](../Roots%20of%20a%20Polynomial.md) of $A$ if and only if $A$ is [divisible](Polynomial%20Division.md) by $x - p$.
>
>>[!PROOF]-
>>
>>**In the forward direction:** Suppose that $p$ is a root of $A$, i.e. $A(p) = 0$. The [polynomial remainder theorem](Polynomial%20Remainder%20Theorem.md) then tells us that the remainder of the division of $A$ by $x-p$ is zero, i.e. $A$ is divisible by $x - p$.
>>
>>**In the backward direction:** Suppose that $A$ is divisible by $x-p$. This means that $A(x) = (x-p)Q(x)$ for some polynomial $Q$. Plugging in $p$ gives us $A(p) = (p - p)Q(p) = 0\cdot Q(p) = 0$ and so $p$ is a root of $A$.
>>
>

>[!THEOREM] Theorem: Number of Roots of Univariate Polynomials
>
>If $P(x)$ is a [polynomial](Univariate%20Polynomial.md) $P(x)$ over an [integral domain](../../Integral%20Domains/Integral%20Domain.md), then the maximum number of distinct [roots](../Roots%20of%20a%20Polynomial.md) which $P$ can have is equal its [degree](../Degree%20of%20a%20Polynomial.md) $\deg(P)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>