---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Eigentheory

## Eigenvalues and Eigenvectors

>[!DEFINITION] Definition: Eigenvector
>
>Let $V$ be a [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) over a [field](../../../../Algebra/Fields/Fields.md) $F$ and let $f: V \to V$ be an [endomorphism](./Vector%20Space%20Endomorphisms.md).
>
>We say $\mathbf{v} \in V \setminus \{\boldsymbol{0}\}$ is an **eigenvector** of $f$ if there exists some $\lambda \in F$ such that
>
>$$f(\mathbf{v}) = \lambda \mathbf{v}.$$
>

>[!DEFINITION] Definition: Eigenvalues
>
>Let $V$ be a [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) over a [field](../../../../Algebra/Fields/Fields.md) $F$ and let $f: V \to V$ be an [endomorphism](./Vector%20Space%20Endomorphisms.md).
>
>We say that $\lambda \in F$ is an **eigenvalue** of $f$ if there exists some $\mathbf{v} \in V \setminus \{\mathbf{0}\}$ such that
>
>$$f(\mathbf{v}) = \lambda \mathbf{v}.$$
>
>>[!DEFINITION] Definition: Point Spectrum
>>
>>The **point spectrum** of $f$ is the [set](../../../../Set%20Theory/Sets.md) of its [eigenvalues](./Eigentheory.md).
>>
>

>[!THEOREM] Theorem: Number of Distinct Eigenvalues
>
>Let $V$ be a [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) over a [field](../../../../Algebra/Fields/Fields.md) $F$ and let $f: V \to V$ be an [endomorphism](./Vector%20Space%20Endomorphisms.md).
>
>If $V$ has [dimension](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Dimension) $n \in \mathbb{N}$, then $f$ has at most $n$ distinct [eigenvalues](./Eigentheory.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

One [eigenvalue](./Eigentheory.md) can be associated with multiple [eigenvectors](./Eigentheory.md), but every [eigenvector](./Eigentheory.md) is associated with a single [eigenvalue](./Eigentheory.md).

>[!THEOREM] Theorem: Different Eigenvalues $\implies$ Linear Independence
>
>Let $V$ be a [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) over a [field](../../../../Algebra/Fields/Fields.md) $F$ let $f: V \to V$ be an [endomorphism](./Vector%20Space%20Endomorphisms.md).
>
>Any [set](../../../../Set%20Theory/Sets.md) of [eigenvectors](./Eigentheory.md) in which each element is associated with a different [eigenvalue](./Eigentheory.md) of $f$ is [linearly independent](../../../../Algebra/Vector%20Spaces/Linear%20Combinations.md#Linear%20Independence).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Eigenvalue Invariance under Similarity
>
>Let $V$ be a [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) over a [field](../../../../Algebra/Fields/Fields.md) $F$ let $f: V \to V$ be an [endomorphism](./Vector%20Space%20Endomorphisms.md).
>
>If $\phi: V \to V$ is an [automorphism](./Vector%20Space%20Endomorphisms.md), then
>
>$$\tilde{f} \overset{\text{def}}{=} \phi^{-1} \circ f \circ \phi$$
>
>has the same [eigenvalues](#Eigenvalues%20and%20Eigenvectors) as $f$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Eigenspace
>
>Let $V$ be a [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) over a [field](../../../../Algebra/Fields/Fields.md) $F$, let $f: V \to V$ be an [endomorphism](./Vector%20Space%20Endomorphisms.md) and let $\lambda \in F$ be an [eigenvalue](./Eigentheory.md) of $f$.
>
>The [set](../../../../Set%20Theory/Sets.md) of all [eigenvectors](./Eigentheory.md) associated with $\lambda$ together with the [zero vector](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) is a [linear subspace](../../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) of $V$.
>
>>[!DEFINITION] Definition: Eigenspace
>>
>>This [subspace](../../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) is known as the **eigenspace** of $\lambda$.
>>
>>>[!NOTATION]
>>>
>>>$$\operatorname{Eig}_{\lambda} \qquad E_{\lambda}$$
>>>
>>
>
>>[!DEFINITION] Definition: Geometric Multiplicity
>>
>>The **geometric multiplicity** of $\lambda$ is the [dimension](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) of its [eigenspace](./Eigentheory.md).
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Eigenspace as Kernel
>
>Let $V$ be a [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) over a [field](../../../../Algebra/Fields/Fields.md) $F$, let $f: V \to V$ be an [endomorphism](./Vector%20Space%20Endomorphisms.md) and let $\lambda \in F$ be an [eigenvalue](./Eigentheory.md) of $f$.
>
>The [eigenspace](./Eigentheory.md) of $\lambda$ is the [kernel](../Linearity%20(Functions).md) of the [endomorphism](./Vector%20Space%20Endomorphisms.md) $f - \lambda \operatorname{id}$:
>
>$$E_{\lambda} = \ker (f - \lambda \operatorname{id})$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Intersection of Eigenspaces
>
>Let $V$ be a [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) over a [field](../../../../Algebra/Fields/Fields.md) $F$ and let $f: V \to V$ be an [endomorphism](./Vector%20Space%20Endomorphisms.md).
>
>If $\lambda_1$ and $\lambda_2$ are distinct [eigenvalues](./Eigentheory.md) of $f$, then the [intersection](../../../../Set%20Theory/Sets.md#Intersection) of their [eigenspaces](./Eigentheory.md) $E_{\lambda_1}$ and $E_{\lambda_2}$ is the [zero vector](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md):
>
>$$E_{\lambda_1} \cap E_{\lambda_2} = \{\mathbf{0}\}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Characteristic Polynomials

>[!DEFINITION] Definition: Characteristic Polynomial
>
>Let $V$ be a [finite-dimensional](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Dimension) [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) over a [field](../../../../Algebra/Fields/Fields.md) $F$ and let $f: V \to V$ be an [endomorphism](./Vector%20Space%20Endomorphisms.md).
>
>The **characteristic polynomial** of $f$ is the [polynomial](../../../../Algebra/Polynomials/Univariate%20Polynomials.md) given by the [determinant](../../../../Algebra/Matrices/Square%20Matrices/Determinants.md) of the [endomorphism](./Vector%20Space%20Endomorphisms.md) $f - \lambda \operatorname{id}$, where $\lambda$ is the variable:
>
>$$\det(f - \lambda \operatorname{id})$$
>
>>[!NOTATION]
>>
>>$$\chi_f (\lambda) = \det(f - \lambda \operatorname{id})$$
>>
>

>[!THEOREM] Theorem: Eigenvalues as Roots of the Characteristic Polynomial
>
>Let $V$ be a [finite-dimensional](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Dimension) [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) over a [field](../../../../Algebra/Fields/Fields.md) $F$ and let $f: V \to V$ be an [endomorphism](./Vector%20Space%20Endomorphisms.md).
>
>The [eigenvalues](./Eigentheory.md) of $f$ are precisely the [roots](../../../../Algebra/Polynomials/Univariate%20Polynomials.md) of its [characteristic polynomial](./Eigentheory.md).
>
>>[!DEFINITION] Definition: Algebraic Multiplicity
>>
>>The **algebraic multiplicity** of an [eigenvalue](./Eigentheory.md) is its [multiplicity](../../../../Algebra/Polynomials/Univariate%20Polynomials.md) as a [root](../../../../Algebra/Polynomials/Univariate%20Polynomials.md) of the [characteristic polynomial](./Eigentheory.md).
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Algebraic and Geometric Multiplicity
>
>Let $V$ be a [finite-dimensional](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Dimension) [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) over a [field](../../../../Algebra/Fields/Fields.md) $F$ and let $f: V \to V$ be an [endomorphism](./Vector%20Space%20Endomorphisms.md).
>
>The [geometric multiplicity](#Eigenvalues%20and%20Eigenvectors) and the [algebraic multiplicity](#Characteristic%20Polynomials) of each [eigenvalue](#Eigenvalues%20and%20Eigenvectors) $\lambda$ of $f$ are related as follows:
>
>$$1\le \operatorname{geo}(\lambda)\le \operatorname{alg}(\lambda)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Eigendecomposition

>[!DEFINITION] Definition: Diagonalizability
>
>Let $V$ be a [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md).
>
>An [endomorphism](./Vector%20Space%20Endomorphisms.md) $f: V \to V$ is **diagonalizable** if $V$ has a [Hamel basis](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) consisting entirely of [eigenvectors](./Eigentheory.md) of $f$.
>

>[!THEOREM] Theorem: Diagonalizability via Direct Sum
>
>Let $V$ be a [finite-dimensional](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Dimension) [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md).
>
>An [endomorphism](./Vector%20Space%20Endomorphisms.md) $f: V \to V$ is [diagonalizable](./Eigentheory.md) if and only if $V$ is the [direct sum](TODO) of the [eigenspaces](#Eigenvalues%20and%20Eigenvectors) of $f$'s [eigenvalues](#Eigenvalues%20and%20Eigenvectors).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Diagonalizability via Dimension
>
>Let $V$ be a [finite-dimensional](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Dimension) [vector space](../../../../Algebra/Vector%20Spaces/Vector%20Spaces.md).
>
>An [endomorphism](./Vector%20Space%20Endomorphisms.md) $f: V \to V$ is [diagonalizable](./Eigentheory.md) if and only if the sum of the [dimensions](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Dimension) of the [eigenspaces](#Eigenvalues%20and%20Eigenvectors) of $f$'s [eigenvalues](#Eigenvalues%20and%20Eigenvectors) is equal to the [dimension](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Dimension) of $V$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Self-Adjoint $\implies$ Diagonalizability
>
>Let $V$ be an [inner product space](../../../../Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md) and let $f: V \to V$ be an [endomorphism](./Vector%20Space%20Endomorphisms.md).
>
>If $V$ is [finite-dimensional](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Dimension) and $f$ is [self-adjoint](TODO) ($f = f^{\ast}$), then $f$ is [diagonalizable](./Eigentheory.md) and $V$ has an [orthonormal](../../../../Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md#Orthogonality) [basis](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) consisting of [eigenvectors](./Eigentheory.md) of $f$.
>
>>[!PROOF]-
>>
>>TODO
>>
>