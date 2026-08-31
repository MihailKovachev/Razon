---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Matrix Norms

Since [matrices](./Matrices.md) of the same dimensionality form a [vector space](../Vector%20Spaces/Vector%20Spaces.md), it is possible to define [norms](../Vector%20Spaces/Norms.md) on them.

>[!DEFINITION] Definition: Submultiplicativity
>
>A [norm](../Vector%20Spaces/Norms.md) $||\cdot||: F^{n \times n} \to \mathbb{R}$ on the [square matrices](./Square%20Matrices/Square%20Matrices.md) in $F^{n \times n}$ is **submultiplicative** if
>
>$$||AB|| \le ||A||\,||B||$$
>
>for all $A, B \in F^{n \times n}$.
>

>[!DEFINITION] Definition: Compatibility
>
>We say that a [norm](../Vector%20Spaces/Norms.md) $||\cdot||_{F^n}: F^n \to \mathbb{R}$ on the [vectors](./Row%20and%20Column%20Vectors.md) in $F^{n}$ is **compatible** with a [norm](../Vector%20Spaces/Norms.md) $||\cdot||_{F^{n\times n}}: F^{n \times n} \to \mathbb{R}$ on the [matrices](./Square%20Matrices/Square%20Matrices.md) in $F^{n \times n}$ if
>
>$$||A v||_{F^n} \le ||A||_{F^{n\times n}} \cdot ||v||_{F^n}$$
>
>for all $v \in F^n$ and all $A \in F^{n \times n}$.
>

## Induced Norms

>[!THEOREM] Theorem: Vector Norm induces Matrix Norm
>
>If $||\cdot||_{F^n}: F^n \to \mathbb{R}$ is a [norm](../Vector%20Spaces/Norms.md) on the [vectors](./Row%20and%20Column%20Vectors.md) in $F^{n}$, then $||\cdot||_{F^{n \times n}}: F^{n \times n} \to \mathbb{R}$ defined as the [supremum](../../Set%20Theory/Orderings/Partially%20Ordered%20Set.md)
>
>$$||A||_{F^{n \times n}} \overset{\text{def}}{=} \sup_{\mathbf{v} \in F^{n} \setminus \{\mathbf{0}\}}\frac{||A\mathbf{v}||_{F^n}}{||\mathbf{v}||_{F^n}}$$
>
>for all [matrices](./Matrices.md) $A \in F^{n \times n}$ is a [norm](../Vector%20Spaces/Norms.md) on $F^{n \times n}$.
>
>>[!DEFINITION] Definition: Induced Norm
>>
>>We call $||A||_{F^{n \times n}}$ the **norm induced by** $||\cdot||_{F^n}: F^n \to \mathbb{R}$ **on** $F^{n \times n}$.
>>
>
>>[!EXAMPLE]- Example: The Norm Induced by $l^1$
>>
>>The [norm](../Vector%20Spaces/Norms.md) [induced](#Inducedd%20Norms) on the [real matrices](./Real%20Matrices/Real%20Matrices.md) in $\mathbb{R}^{n \times n}$ by the $l^1$-[norm](../Linear%20Algebra/Real%20Vectors/P-Norms.md) of $\mathbb{R}^n$ is the maximum sum of absolute values entries in a single column:
>>
>>$$||A||_1 = \max_{1 \le i \le n}\sum_{j = 1}^n |a_{ji}|$$
>>
>
>>[!EXAMPLE]- Example: The Norm Induced by $l^{\infty}$
>>
>>The [norm](../Vector%20Spaces/Norms.md) [induced](#Inducedd%20Norms) on the [real matrices](./Real%20Matrices/Real%20Matrices.md) in $\mathbb{R}^{n \times n}$ by the [maximum norm](../Linear%20Algebra/Real%20Vectors/Maximum%20Norm.md) of $\mathbb{R}^n$ is the maximum sum of absolute values of entries in a single row:
>>
>>$$||A||_{\infty} = \max_{1 \le i \le n} \sum_{j = 1}^n |a_{ij}|$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Submultiplicativity of Induced Norms
>
>All [induced norms](#Induced%20Norms) are [submultiplicative](./Matrix%20Norms.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Compatibility of Induced Norms
>
>If $||\cdot||_M$ is [induced](#Induced%20Norms) by $||\cdot||_V$, then $||\cdot||_M$ and $||\cdot||_V$ are [compatible](./Matrix%20Norms.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>