>[!DEFINITION] Definition: Monomial Multiplication
>
>Let $R$ be a [commutative ring](../../Commutative%20Ring.md) and let $M = m x_n^{p_n} x_{n-1}^{p_{n-1}}\cdots x_2^{p_2}x_1^{p_1}$ and $M' = m' x_n^{p_n'} x_{n-1}^{p_{n-1}'}\cdots x_2^{p_2'}x_1^{p_1'}$ be two [monomials](Monomial.md) over $R$.
>
>The **product** of a $M$ with $M'$ is defined as the monomial
>
>$$
>\begin{align*}MM' \overset{\text{def}}{=} (mm') x_n^{p_n + p_n'} x_{n-1}^{p_{n-1}+p_{n-1}'} \cdots x_2^{p_2 + p_2'}x_1^{p_1 + p_1'}\end{align*}
>$$
>
>>[!INTUITION]-
>>
>>Monomial multiplication is defined in this in order to follow the commutativity and associativity laws for the underlying ring.
>>
>
>>[!EXAMPLE]-
>>
>>$$
>>(3 x^4 y) \cdot (2 x^4 y) = (2\cdot 3) x^{4+4} y^{1 + 1} = 6 x^8 y^2
>>$$
>>
>>$$
>>(11 x^3 y^2 z)\cdot(2 y z^2) = (11 x^3 y^2 z)\cdot( 2 x^0 y z^2) = (11 \cdot 2)(x^{3 + 0} y^{2 + 1} z^{1 + 2}) = 22 x y^3 z^3
>>$$
>>
>>$$
>>(x^3 y)(y z^3) = (x^3 y z^0)(x^0 y z^3) = (1 \cdot 1) (x^{3+0} y^{1+1} z^{0+3}) = x^3 y^2 z^3
>>$$
>>
>