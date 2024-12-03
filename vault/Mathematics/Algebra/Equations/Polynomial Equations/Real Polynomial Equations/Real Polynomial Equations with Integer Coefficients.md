>[!THEOREM] Theorem: Real Polynomial Equations with Integer Coefficients
>
>If the coefficients $a_0, \cdots, a_n$ of the [real polynomial equation](Real%20Polynomial%20Equation.md)
>
>$$
>a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0 = 0
>$$
>
>are [integers](TODO) and it has a [rational](TODO) [root](../../../Rings/Commutative%20Rings/Polynomials/Roots%20of%20a%20Polynomial.md) $x^\ast = \frac{p}{q}$ (where $p$ and $q$ are [coprime](TODO)), then $p$ is a [divisor](TODO) of $a_0$ and $q$ is a divisor of $a_n$.
>
>>[!PROOF]-
>>
>>**Proof that** $q$ **is a divisor of** $a_n$**:**
>>
>>If $x^\ast = \frac{p}{q}$ is a root of the polynomial equation, then
>>
>>$$
>>a_n \frac{p^n}{q^n} + a_{n-1} \frac{p^{n-1}}{q^{n-1}} + \cdots + a_1 \frac{p}{q} + a_0 = 0
>>$$
>>
>>Multiply by $q^{n-1}$.
>>
>>$$
>>a_n \frac{p^n}{q} + a_{n-1} p^{n-1} + \cdots + a_1 p q^{n-2} + a_0 q^{n-1} = 0
>>$$
>>
>>$$
>>a_n \frac{p^n}{q} = - a_{n-1} p^{n-1} - \cdots - a_1 p q^{n-2} - a_0 q^{n-1}
>>$$
>>
>>Since $p,q$ and $a_k$ are all integers, the right-hand side must be an integer as well. This means that $a_n \frac{p^n}{q}$ is an integer, but $p^n$ and $q$ have no common divisors, since they are coprime. This means that $q$ must divide $a_n$.
>>
>>**Proof that** $p$ **is a divisor of** $a_0$**:**
>>
>>If $x^\ast = \frac{p}{q}$ is a root of the polynomial equation, then
>>
>>$$
>>a_n \frac{p^n}{q^n} + a_{n-1} \frac{p^{n-1}}{q^{n-1}} + \cdots + a_1 \frac{p}{q} + a_0 = 0
>>$$
>>
>>Multiply by $q^n$.
>>
>>$$
>>a_n p^n + a_{n-1} p^{n-1} q + \cdots + a_1 p q^{n-1} + a_0 q^n = 0
>>$$
>>
>>Divide by $p$.
>>
>>$$
>>a_n p^n + a_{n-1} p^{n-1} q + \cdots + a_1 p q^{n-1} + a_0 q^n = 0
>>$$
>>
>>$$
>>a_n p^{n-1} + a_{n-1} p^{n-2} q + \cdots + a_1 q^{n-1} + a_0 \frac{q^n}{p} = 0
>>$$
>>
>>$$
>>a_0 \frac{q^n}{p} = - a_n p^{n-1} - a_{n-1} p^{n-2} q - \cdots - a_1 q^{n-1}
>>$$
>>
>>Once again, $p,q$ and $a_k$ are all integers and so the right-hand side must be an integer. This means that $a_0 \frac{q^n}{p}$ is an integer. The numbers $q^n$ and $p$ have no common divisors, since $q$ and $p$ are coprime. This means that $p$ must be a divisor of $a_0$.
>>
>