---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Multilinear Forms

>[!DEFINITION] Definition: Linear Form
>
>Let $V$ be a [vector space](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) over a [field](../../../Algebra/Fields/Fields.md) $F$.
>
>A $k$**-linear form** of over $V$ is a [multilinear transformation](./Multilinear%20Transformations.md) of the following form:
>
>$$f: V^k \to F$$
>
>For $k=1$ we also say that $f$ is just a **linear form** and for $k=2$ we say that $f$ is a **bilinear form**. In general, we call $f$ a **multilinear form**.
>
>>[!EXAMPLE]- Example: $\mathbf{v}^{\mathsf{T}} M \mathbf{w}$
>>
>>Any [function](../../Functions/Functions.md) $f: F^{n} \times F^{n} \to F$ defined as
>>
>>$$
>>f(\mathbf{v}, \mathbf{w}) = \mathbf{v}^{\mathsf{T}}M\mathbf{w}
>>$$
>>
>>for some [symmetric](../../../Algebra/Matrices/Square%20Matrices/Symmetric%20Matrices.md) [square matrix](../../../Algebra/Matrices/Square%20Matrices/Square%20Matrices.md) $M \in F^{n\times n}$ is a [bilinear form](./Multilinear%20Forms.md).
>>
>
>>[!EXAMPLE]- Example: $\int_0^1 f(x) g(x) \mathop{\mathrm{d}x}$
>>
>>The [Riemann-integral](../../Real%20Analysis/Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md#Riemann%20Integration) $\int_0^1 f(x) g(x) \mathop{\mathrm{d}x}$ is a [bilinear form](./Multilinear%20Forms.md) on the [vector space](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) of all [continuous](../../Real%20Analysis/Real%20Functions/Continuity%20(Real%20Functions).md) [real functions](../../Real%20Analysis/Real%20Functions/Real%20Functions.md) on $[0;1]$.
>>
