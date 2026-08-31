---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Multilinear Transformations

>[!DEFINITION] Definition: Multilinear Transformation
>
>Let $V_1, \dotsc, V_m, W$ be [vector spaces](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) over the same [field](../../../Algebra/Fields/Fields.md) $F$.
>
>A [function](../../Functions/Functions.md) $f: V_1 \times \cdots \times V_m \to W$ is **multilinear** if for each $i \in \{1, \dotsc, m\}$ and all $\mathbf{v}_j \in V_j$ ($j \ne i$), the [function](../../Functions/Functions.md) $f(\mathbf{v}_1,\dotsc,\mathbf{v}_{i-1},\cdot,\mathbf{v}_{i+1},\dotsc,\mathbf{v}_m): V_i \to W$ is [linear](./Linearity%20(Functions).md).
>
>>[!INTUITION]
>>
>>A [multilinear transformation](./Multilinear%20Transformations.md) is a [function](../../Functions/Functions.md) which is [linear](./Linearity%20(Functions).md) in each of its arguments.
>>
>
>>[!EXAMPLE]- Example: Matrix Product
>>
>>The [matrix product](../../../Algebra/Matrices/Matrix%20Operations.md#Matrix%20Product) $f: F^{m \times n} \times F^{n \times p} \to F^{m \times p}$ is [bilinear](./Multilinear%20Transformations.md).
>>
>

