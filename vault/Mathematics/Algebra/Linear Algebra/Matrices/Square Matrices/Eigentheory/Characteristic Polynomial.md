>[!DEFINITION] Definition: Characteristic Polynomial
>
>The **characteristic polynomial** $p_A(x)$ of a [square matrix](../Square%20Matrix.md) $A \in F^{n \times n}$ the [univariate polynomial](../../../../Rings/Commutative%20Rings/Polynomials/Univariate%20Polynomials/index.md) obtained through the [determinant](../Determinants/Determinant.md) and the [identity matrix](../Identity%20Matrix.md) $I_n$ in the following way:
>
>$$
>p_A(x) \overset{\text{def}}{=} \det(A - x I_n)
>$$
>

>[!THEOREM] Theorem: Degree of the Characteristic Polynomial
>
>The [degree](../../../../Rings/Commutative%20Rings/Polynomials/Polynomials.md) of the [characteristic polynomial](Characteristic%20Polynomial.md) of a [square matrix](../Square%20Matrix.md) $A \in F^{n \times n}$ is $n$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Finding Eigenvalues
>
>The [eigenvalues](Eigenvalue.md) of a [square matrix](../Square%20Matrix.md) $A \in F^{n \times n}$ are precisely the roots of its [characteristic polynomial](Characteristic%20Polynomial.md).
>
>$$
>\det (A - x I_n) = 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Algebraic Multiplicity
>>
>>If the [characteristic polynomial](Characteristic%20Polynomial.md) of $A$ has a linear factorisation
>>
>>$$
>>p_A(x) = (x - \lambda_1)^{k_1} \cdots (x - \lambda_r)^{k_r}
>>$$ 
>>
>>over the [field](../../../../Fields/index.md) $F$, where $\lambda_1,\cdots,\lambda_r \, (r \le n)$ are the distinct [eigenvalues](Eigenvalue.md) of $A$, then we call $k_i$ the **algebraic multiplicity** of $\lambda_i$.
>>
>>>[!NOTATION]-
>>>
>>>$$
>>>\operatorname{alg}(\lambda_i)
>>>$$
>>>
>>
>