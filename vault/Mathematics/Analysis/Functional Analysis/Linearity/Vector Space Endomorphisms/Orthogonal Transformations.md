---
tags:
    - linear-algebra
    - algebra
    - mathematics
---

# Orthogonal Transformations

>[!DEFINITION] Definition: Orthogonal Transformation
>
>Let $(V, \langle \cdot, \cdot \rangle)$ be a [real inner product space](../../../../Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md).
>
>An [endomorphism](./Vector%20Space%20Endomorphisms.md) $f: V \to V$ is **orthogonal** if it preserves the [real inner product](../../../../Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md):
>
>$$\langle f(v), f(w) \rangle = \langle v, w \rangle \qquad \forall v,w \in V$$
>

>[!THEOREM] Theorem: Length Preservation $\iff$ Orthogonal Transformation
>
>Let $(V, \langle \cdot, \cdot \rangle)$ be a [real inner product space](../../../../Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md).
>
>An [endomorphism](./Vector%20Space%20Endomorphisms.md) $f: V \to V$ is an [orthogonal transformation](./Orthogonal%20Transformations.md) if and only if it preserves the [induced norm](../../../../Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md#Geometry):
>
>$$||f(v)|| = ||v|| \qquad \forall v \in V$$
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>
>>- (I) If $f$ is an [orthogonal transformation](./Orthogonal%20Transformations.md), then it preserves the [induced norm](../../../../Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md#Geometry).
>>- (II) If $f$ preserves the [induced norm](../../../../Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md#Geometry), then it is an [orthogonal transformation](./Orthogonal%20Transformations.md).
>>
>>**Proof of (I):**
>>
>>Since $f$ is an [orthogonal transformation](./Orthogonal%20Transformations.md), we have
>>
>>$$\langle f(v), f(v) \rangle = \langle v, v\rangle$$
>>
>>$$||f(v)||^2 = ||v||^2$$
>>
>>Since $||f(v)||$ and $||v||$ are non-negative by definition, we have:
>>
>>$$||f(v)|| = ||v||$$
>>
>>**Proof of (II):**
>>
>>We apply the [polarization identity](../../../../Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md) to $\langle f(v), f(w) \rangle$:
>>
>>$$\langle f(v), f(w) \rangle = \frac{1}{2}(||f(v)+f(w)||^2-||f(v)||^2-||f(w)||^2)$$
>>
>>Since $f$ is [linear](../Linearity%20(Functions).md), we have:
>>
>>$$\langle f(v), f(w) \rangle = \frac{1}{2}(||f(v+w)||^2-||f(v)||^2-||f(w)||^2)$$
>>
>>Since $f$ preserves the [induced norm](../../../../Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md#Geometry), we have:
>>
>>$$\langle f(v), f(w) \rangle = \frac{1}{2}(||v+w||^2-||v||^2-||w||^2)$$
>>
>>The right-hand side is just the [polarization identity](../../../../Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md) for $\langle v, w \rangle$:
>>
>>$$\langle f(v), f(w) \rangle = \frac{1}{2}(||v+w||^2-||v||^2-||w||^2) = \langle v, w \rangle$$
>>
>

>[!THEOREM] Theorem: Orthonormal Basis to Orthonormal Basis
>
>Let $(V, \langle \cdot, \cdot \rangle)$ be a [finite-dimensional](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Dimension) [real inner product space](../../../../Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md) and let $f: V \to V$ be an [endomorphism](./Vector%20Space%20Endomorphisms.md).
>
>If $b_1, \dotsc, b_n$ is an [orthonormal](../../../../Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md) [basis](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) of $V$ and $f$ is an [orthogonal transformation](./Orthogonal%20Transformations.md), then $f(b_1), \dotsc, f(b_n)$ is also an [orthonormal](../../../../Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md#Orthogonality) [basis](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) of $V$.
>
>Conversely, if $b_1, \dotsc, b_n$ and $f(b_1), \dotsc, f(b_n)$ are both [orthonormal](../../../../Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md#Orthogonality) [bases](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) of $V$, then $f$ is an [orthogonal transformation](./Orthogonal%20Transformations.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Bijectivity of Orthogonal Transformations
>
>Every [orthogonal transformation](./Orthogonal%20Transformations.md) on a [finite-dimensional](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Dimension) [inner product space](../../../../Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md) is [bijective](../../../Functions/Injections,%20Surjections%20and%20Bijections.md#Bijections).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Adjoint as Inverse of Orthogonal Transformation
>
>Let $(V, \langle \cdot, \cdot \rangle)$ be a [real inner product space](../../../../Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md) and let $f: V \to V$ be an [orthogonal transformation](./Orthogonal%20Transformations.md).
>
>If $f$ is [bijective](../../../Functions/Injections,%20Surjections%20and%20Bijections.md#Bijections) and its [adjoint](../Algebraic%20Adjoints.md) $f^{\ast}$ exists, then $f$'s [inverse](../../../Functions/Injections,%20Surjections%20and%20Bijections.md#Injections) is $f^{\ast}$:
>
>$$f^{-1} = f^{\ast}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Determinants of Orthogonal Transformations
>
>Let $(V, \langle \cdot, \cdot \rangle)$ be a [finite-dimensional](../../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Dimension) [real inner product space](../../../../Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Inner%20Product%20Spaces.md).
>
>If $f: V \to V$ is an [orthogonal transformation](./Orthogonal%20Transformations.md), then its [determinant](./Vector%20Space%20Endomorphisms.md#Determinants) is either $+1$ or $-1$.
>
>>[!PROOF]-
>>
>>TODO
>>
>