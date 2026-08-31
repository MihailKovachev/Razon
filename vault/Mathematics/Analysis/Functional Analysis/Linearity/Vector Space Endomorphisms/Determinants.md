---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Determinants

>[!DEFINITION] Definition: Determinant Form
>
>A **determinant form** is a non-trivial [alternating multilinear form](../Alternating%20Multilinear%20Forms.md).
>

>[!THEOREM] Theorem: Existence of a Determinant Form
>
>Every $n$-[dimensional](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) ($n \ge 1$) [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) $(V, F)$ has at least one [determinant form](./Determinants.md) $f: V^n \to F$.
>
>>[!PROOF]-
>>
>>The proof is by [induction](../../../../Logic/Mathematical%20Induction.md).
>>
>>**Base case:** $n = 1$
>>
>>This is trivial because every [linear form](../Multilinear%20Forms.md) $f: V \to F$ is [alternating](../Alternating%20Multilinear%20Forms.md) by definition.
>>
>>**Induction hypothesis:** TODO
>>
>

>[!THEOREM] Theorem: Determinant Form Scaling
>
>Let $(V, F)$ be an $n$-[dimensional](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Dimension) $(n \ge 1)$ [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md).
>
>If $\omega_1: V^n \to F$ is a non-zero  [determinant form](#Determinants) and $\omega_2: V^n \to F$ is any other [determinant form](#Determinants), then there exists a unique $\lambda \in F$ such that
>
>$$
>\omega_2 = \lambda \omega_1.
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Determinant
>
>Let $(V, F)$ be an $n$-[dimensional](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Dimension) $(n \ge 1)$ [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md).
>
>If $f: V \to V$ is an [endomorphism](../Linearity%20(Functions).md), then there exists a unique scalar $\mu \in F$ such that
>
>$$
>\mu \cdot \omega (\mathbf{v}_1, \dotsc, \mathbf{v}_n) = \omega (f(\mathbf{v}_1), \dotsc, f(\mathbf{v}_n))
>$$
>
>for all $\mathbf{v}_1, \dotsc, \mathbf{v}_n \in V$ and all [determinant forms](#Determinants) $\omega$.
>
>>[!DEFINITION] Definition: Determinant
>>
>>We call $\mu$ the **determinant** of $f$.
>>
>>>[!NOTATION]
>>>
>>>We denote the [determinant](#Determinants) of $f$ by $\det f$.
>>>
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Determinant of Composition
>
>Let $(V, F)$ be an $n$-[dimensional](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Dimension) $(n \ge 1)$ [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) and let $f, g: V \to V$ be [endomorphisms](./Vector%20Space%20Endomorphisms.md).
>
>The [determinant](#Determinants) of the [composition](../../../Functions/Functions.md) $f \circ g$ is equal to the [product](../../../../Algebra/Fields/Fields.md) of the  [determinants](#Determinants) of $f$ and $g$:
>
>$$\det f \circ g = \det f \cdot \det g$$
>
>>[!PROOF]-
>>
>>By definition we have
>>
>>$$\begin{aligned}(\det f \circ g) \cdot \omega & = \omega(f(g(\cdot)), \dotsc, f(g(\cdot))) \\ & = (\det f)\cdot \omega(g(\cdot), \dotsc, g(\cdot)) \\ & = (\det f) \cdot ((\det g)\cdot \omega) \\ & = (\det f \cdot \det g) \cdot \omega\end{aligned}$$
>>
>>for all [determinant forms](#Determinants) $\omega$. Therefore:
>>
>>$$\det f \circ g = \det f \cdot \det g$$
>>
>

>[!THEOREM] Theorem: Bijectivity via Determinants
>
>Let $(V, F)$ be a [finite dimensional](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Dimension) [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) with $\dim V \ge 1$.
>
>An [endomorphism](./Vector%20Space%20Endomorphisms.md) $f: V \to V$ is [bijective](../../../Functions/Injections,%20Surjections%20and%20Bijections.md#Bijections) if and only if its [determinant](#Determinants) $\det f$ is not zero.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Eigenvalues and Determinant
>
>Let $(V, F)$ be a [finite-dimensional](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Dimension) [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) and let $f: V \to V$ be an [endomorphism](./Vector%20Space%20Endomorphisms.md).
>
>If $f$ has $l$ distinct [eigenvalues](./Eigentheory.md) $\lambda_1, \dotsc, \lambda_l$ and the sum of their [algebraic multiplicities](./Eigentheory.md) is equal to $\dim V$, then the [determinant](#Determinants) of $f$ is given as follows:
>
>$$\det f = \prod_{k=1}^l \lambda_k ^{\operatorname{alg} (\lambda_k)}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>