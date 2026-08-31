---
title: The Binomial Theorem
tags:
    - complex-numbers
    - algebra
---

# The Binomial Theorem

>[!THEOREM] The Binomial Theorem
>
>The expansion of the [complex polynomial](./Complex%20Polynomials.md) $(x+y)^n$ is the following:
>
>$$
>(x+y)^n = \sum_{k=0}^n \binom{n}{k} x^{n-k} y^k = \sum_{k=0}^n \binom{n}{k} x^{k} y^{n-k},
>$$
>
>where
>
>$$
>\binom{n}{k} \overset{\text{def}}{=} \frac{n!}{k! (n-k)!}.
>$$
>
>>[!DEFINITION] Definition: Binomial Coefficient
>>
>>The numbers $\binom{n}{k}$ are known as **binomial coefficients**.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Symmetry of Binomial Coefficients
>
>The [binomial coefficients](./The%20Binomial%20Theorem.md) have the following property:
>
>$$
>\binom{n}{k} = \binom{n}{n-k}
>$$
>
>>[!PROOF]-
>>
>>By definition:
>>
>>$$
>>\begin{aligned}
>>\binom{n}{k} &= \frac{n!}{k! (n-k)!} \\
>>\binom{n}{n-k} &= \frac{n!}{(n-k)!(n-(n-k))!} = \frac{n!}{(n-k)!k!}
>>\end{aligned}
>>$$
>>
>

>[!THEOREM] Theorem: Recursion of Binomial Coefficients
>
>The [binomial coefficients](./The%20Binomial%20Theorem.md) have the following recursive property:
>
>$$
>\binom{n + 1}{k} = \binom{n}{k} + \binom{n}{k-1}
>$$
>
>>[!PROOF]-
>>
>>We write out the right-hand side:
>>
>>$$
>>\binom{n}{k} + \binom{n}{k-1} = \frac{n!}{k! (n-k)!} + \frac{n!}{(k-1)!(n-k+1)!}
>>$$
>>
>>We now use the definition of the [factorial](TODO):
>>
>>$$
>>\begin{aligned}
>>&\frac{n!}{k! (n-k)!} + \frac{n!}{(k-1)!(n-k+1)!} \\ &= \frac{n!}{k(k-1)!(n-k)!} + \frac{n!}{(k-1)!(n-k+1)(n-k)!} \\
>>&= \frac{n!(n-k+1) + n!k}{k(k-1)!(n-k)(n-k+1)} \\
>>&= \frac{n!(n+1)}{k!(n+1-k)!}
>>\end{aligned}
>>$$
>>
>>This is equal to the definition of the left-hand side:
>>
>>$$
>>\binom{n+1}{k} = \frac{(n+1)!}{k!(n+1-k)!}
>>$$
>>
>

>[!THEOREM] Theorem: Sum of Binomial Coefficients
>
>The sum of the [binomial coefficients](./The%20Binomial%20Theorem.md) $\binom{n}{k}$ from $0$ to $n$ is $2^n$:
>
>$$
>\sum_{k = 0}^n \binom{n}{k} = 2^n
>$$
>
>>[!PROOF]-
>>
>>We use the [binomial theorem](./The%20Binomial%20Theorem.md) itself:
>>
>>$$
>>(x+y)^n = \sum_{k=0}^n \binom{n}{k} x^{n-k} y^k
>>$$
>>
>>Set $x = 1$ and $y = 1$:
>>
>>$$
>>\begin{aligned}
>>(1 + 1)^n &= \sum_{k=0}^n \binom{n}{k} \cdot 1^{n-k} \cdot 1^k \\
>>2^n &= \sum_{k=0}^n \binom{n}{k}
>>\end{aligned}
>>$$
>>
>