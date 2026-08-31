---
tags:
    - linear-algebra
    - algebra
    - mathematics
---
# Symmetric Matrices

>[!DEFINITION] Definition: Symmetric Matrix
>
>A [square matrix](./Square%20Matrices.md) $M \in F^{n \times n}$ is **symmetric** if the [bilinear form](../../../Analysis/Functional%20Analysis/Linearity/Multilinear%20Forms.md) $f: F^n \times F^n \to F$ defined as
>
>$$f(\boldsymbol{x}, \boldsymbol{y}) = \boldsymbol{x}^{\mathsf{T}} M \boldsymbol{y}$$
>
>for all $\boldsymbol{x}, \boldsymbol{y} \in F^n$ is [symmetric](../../../Analysis/Functional%20Analysis/Linearity/Symmetric%20Multilinear%20Forms.md).
>

>[!THEOREM] Theorem: Symmetry via Transpose
>
>A [square matrix](./Square%20Matrices.md) $M \in F^{n \times n}$ is [symmetric](./Symmetric%20Matrices.md) if and only if it is equal to its own [transpose](../Matrix%20Transposition.md):
>
>$$M = M^{\mathsf{T}}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Symmetry of Inverse
>
>If a [symmetric](./Symmetric%20Matrices.md) [matrix](./Square%20Matrices.md) is [invertible](./Matrix%20Invertibility.md)  , then its [inverse](./Matrix%20Invertibility.md) is also [symmetric](./Symmetric%20Matrices.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Definiteness

>[!DEFINITION] Definition: Definiteness
>
>Let $F$ be an [ordered](TODO) [field](../../Fields/Fields.md), let $M \in F^{n \times n}$ be [symmetric](./Symmetric%20Matrices.md) and let $f: F^n \times F^n \to F$ be the [symmetric](../../../Analysis/Functional%20Analysis/Linearity/Symmetric%20Multilinear%20Forms.md) [bilinear form](../../../Analysis/Functional%20Analysis/Linearity/Multilinear%20Forms.md) defined as
>
>$$f(\boldsymbol{x}, \boldsymbol{y}) = \boldsymbol{x}^{\mathsf{T}} M \boldsymbol{y}$$
>
>for all $\boldsymbol{x}, \boldsymbol{y} \in F^n$.
>
>We say that $M$ is **positive definite** / **positive semi-definite** / **negative definite** / **negative semi-definite** / **indefinite** if $f$ is [positive definite](../../../Analysis/Functional%20Analysis/Linearity/Symmetric%20Multilinear%20Forms.md#Definiteness) / [positive semi-definite](../../../Analysis/Functional%20Analysis/Linearity/Symmetric%20Multilinear%20Forms.md#Definiteness) / [negative definite](../../../Analysis/Functional%20Analysis/Linearity/Symmetric%20Multilinear%20Forms.md#Definiteness) / [negative semi-definite](../../../Analysis/Functional%20Analysis/Linearity/Symmetric%20Multilinear%20Forms.md#Definiteness) / [indefinite](../../../Analysis/Functional%20Analysis/Linearity/Symmetric%20Multilinear%20Forms.md#Definiteness).
>