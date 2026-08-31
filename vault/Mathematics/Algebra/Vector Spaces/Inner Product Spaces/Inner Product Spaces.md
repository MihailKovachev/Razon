---
tags:
  - linear-algebra
  - algebra
  - mathematics
---

# Inner Product Spaces

## Inner Products

>[!DEFINITION] Definition: Real Inner Product
>
>Let $(V, \mathbb{R})$ be a [vector space](../Vector%20Spaces.md) over the [real numbers](../../Fields/The%20Real%20Numbers/The%20Real%20Numbers.md).
>
>A **real inner product** on $V$ is a [function](../../../Analysis/Functions/Functions.md) $\langle \cdot, \cdot \rangle: V \times V \to \mathbb{R}$ with the following properties:
>
>- The [function](../../../Analysis/Functions/Functions.md) $\langle \cdot, \cdot \rangle$ is a [bilinear form](../../../Analysis/Functional%20Analysis/Linearity/Multilinear%20Forms.md):
>
>    - $\langle \mathbf{u} + \mathbf{v}, \mathbf{w} \rangle = \langle \mathbf{u}, \mathbf{w} \rangle + \langle \mathbf{v}, \mathbf{w} \rangle$
>    - $\langle \mathbf{u}, \mathbf{v} + \mathbf{w} \rangle = \langle \mathbf{u}, \mathbf{v} \rangle + \langle \mathbf{u}, \mathbf{w} \rangle$
>    - $\langle \lambda \mathbf{u}, \mathbf{v} \rangle = \lambda \langle\mathbf{u}, \mathbf{v}\rangle$
>    - $\langle \mathbf{u}, \lambda \mathbf{v} \rangle = \lambda \langle\mathbf{u}, \mathbf{v}\rangle$
>
>- The [function](../../../Analysis/Functions/Functions.md) $\langle \cdot, \cdot \rangle$ is [symmetric](../../../Analysis/Functional%20Analysis/Linearity/Symmetric%20Multilinear%20Forms.md): $\langle \mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{v}, \mathbf{u} \rangle$.
>
>- The [function](../../../Analysis/Functions/Functions.md) $\langle \cdot, \cdot \rangle$ is [positive definite](../../../Analysis/Functional%20Analysis/Linearity/Symmetric%20Multilinear%20Forms.md#Definiteness): $\langle \mathbf{v}, \mathbf{v} \rangle \ge 0$ for all $\mathbf{v} \in V$ and $\langle \mathbf{v}, \mathbf{v} \rangle = 0 \iff \mathbf{v} = \mathbf{0}$.
>
>>[!EXAMPLE]-
>>
>>The [dot product](../../Linear%20Algebra/Real%20Vectors/Real%20Vectors.md#Dot%20Product) on $\mathbb{R}^n$ is an [inner product](./Inner%20Product%20Spaces.md).
>>
>
>>[!EXAMPLE]-
>>
>>The [Riemann integral](../../../Analysis/Real%20Analysis/Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md#Riemann%20Integrals)
>>
>>$$\frac{1}{\pi}\int_0^{2\pi} f(x) g(x) \,\mathrm{d}x$$
>>
>>is an [inner product](./Inner%20Product%20Spaces.md) on the [vector space](../Vector%20Spaces.md) of all [real functions](../../../Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) which are [continuous](../../../Analysis/Real%20Analysis/Real%20Functions/Continuity%20(Real%20Functions).md) on $[0; 2\pi]$.
>>
>

>[!DEFINITION] Definition: Real Inner Product Space
>
>A **real inner product space** is a [vector space](../Vector%20Spaces.md) over the [real numbers](../../Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) equipped with a [real inner product](#Inner%20Products).
>

>[!DEFINITION] Definition: Complex Inner Product
>
>Let $(V, \mathbb{R})$ be a [vector space](../Vector%20Spaces.md) over the [complex numbers](../../Fields/The%20Complex%20Numbers/Complex%20Numbers.md).
>
>A **complex inner product** on $V$ is a [function](../../../Analysis/Functions/Functions.md) $\langle \cdot, \cdot \rangle: V \times V \to \mathbb{C}$ with the following properties:
>
>- The [function](../../../Analysis/Functions/Functions.md) $\langle \cdot, \cdot \rangle$ is a [sesquilinear form](TODO):
>
>    - $\langle \mathbf{u} + \mathbf{v}, \mathbf{w} \rangle = \langle \mathbf{u}, \mathbf{w} \rangle + \langle \mathbf{v}, \mathbf{w} \rangle$
>    - $\langle \mathbf{u}, \mathbf{v} + \mathbf{w} \rangle = \langle \mathbf{u}, \mathbf{v} \rangle + \langle \mathbf{u}, \mathbf{w} \rangle$
>    - $\langle \lambda \mathbf{u}, \mathbf{v} \rangle = \lambda \langle\mathbf{u}, \mathbf{v}\rangle$
>    - $\langle \mathbf{u}, \lambda \mathbf{v} \rangle = \bar{\lambda} \langle\mathbf{u}, \mathbf{v}\rangle$
>
>- The [function](../../../Analysis/Functions/Functions.md) $\langle \cdot, \cdot \rangle$ is [Hermitian](TODO): $\langle \mathbf{u}, \mathbf{v} \rangle = \overline{\langle \mathbf{v}, \mathbf{u} \rangle}$.
>
>- The [function](../../../Analysis/Functions/Functions.md) $\langle \cdot, \cdot \rangle$ is [positive definite](../../../Analysis/Functional%20Analysis/Linearity/Symmetric%20Multilinear%20Forms.md#Definiteness): $\langle \mathbf{v}, \mathbf{v} \rangle \ge 0$ for all $\mathbf{v} \in V$ and $\langle \mathbf{v}, \mathbf{v} \rangle = 0 \iff \mathbf{v} = \mathbf{0}$.
>

>[!DEFINITION] Definition: Complex Inner Product Space
>
>A **complex inner product space** is a [vector space](../Vector%20Spaces.md) over the [complex numbers](../../Fields/The%20Complex%20Numbers/Complex%20Numbers.md) equipped with a [complex inner product](#Inner%20Products).
>

>[!DEFINITION] Definition: Inner Product Space
>
>An [inner product space](./Inner%20Product%20Spaces.md) is either a [real inner product space](./Inner%20Product%20Spaces.md) or a [complex inner product space](./Inner%20Product%20Spaces.md).
>

>[!THEOREM] Theorem: The Adjoint Property
>
>Let $(V, \langle \cdot, \cdot \rangle)$ be an [inner product space](./Inner%20Product%20Spaces.md) and let $f: V \to V$ be an [endomorphism](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Vector%20Space%20Endomorphisms.md).
>
>If the [adjoint](../../../Analysis/Functional%20Analysis/Linearity/Algebraic%20Adjoints.md) $f^{\ast}$ of $f$ exists, then it is the only [endomorphism](../../../Analysis/Functional%20Analysis/Linearity/Vector%20Space%20Endomorphisms/Vector%20Space%20Endomorphisms.md) such that
>
>$$\langle f(v), w\rangle = \langle v, f^{\ast}(w)\rangle$$
>
>for all $v, w \in V$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Geometry

>[!DEFINITION] Definition: Induced Norm
>
>Let $(V, F, +, \cdot)$ be an [inner product space](./Inner%20Product%20Spaces.md).
>
>The [function](../../../Analysis/Functions/Functions.md) $||\cdot||: V \to \mathbb{R}$ defined as
>
>$$||\mathbf{v}|| \overset{\text{def}}{=} \sqrt{\langle\mathbf{v},\mathbf{v}\rangle}$$
>
>is called the **induced norm** on $V$.
>
>We call $||\mathbf{v}||$ the **length** of $\mathbf{v}$.
>
>>[!PROOF]- Proof: Induced Norm is a Norm
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Parallelogram Law
>
>Let $(V, \langle \cdot, \cdot \rangle)$ be a [real inner product space](./Inner%20Product%20Spaces.md).
>
>The [induced norm](#Geometry) has the following property:
>
>$$||v||^2 + ||w||^2 = \frac{||v+w||^2 + ||v-w||^2}{2}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Cauchy-Schwarz Inequality
>
>Let $(V, F, +, \cdot)$ be an [inner product space](./Inner%20Product%20Spaces.md).
>
>The [induced norm](#Geometry) has the following property for all $v, w \in V$:
>
>$$|\langle v, w \rangle| \le ||v||\, ||w||$$
>
>>[!PROOF]-
>>
>>If $w = 0$, then the inequality is trivially satisfied.
>>
>>If $w \ne 0$, then we have:
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Polarization Identity
>
>Let $(V, F, +, \cdot)$ be an [inner product space](./Inner%20Product%20Spaces.md).
>
>The [inner product](./Inner%20Product%20Spaces.md) can be expressed via the [induced norm](#Geometry) in the following way:
>
>$$\langle v, w \rangle = \frac{1}{4}(||v + w||^2 - ||v - w||)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!DEFINITION] Definition: Euclidean Metric
>
>Let $(V, F, +, \cdot)$ be an [inner product space](./Inner%20Product%20Spaces.md).
>
>The [function](../../../Analysis/Functions/Functions.md) $d: V \times V \to \mathbb{R}$ defined as
>
>$$d(\mathbf{u}, \mathbf{v}) \overset{\text{def}}{=} ||\mathbf{u} - \mathbf{v}||$$
>
>is called the **Euclidean metric** on $V$.
>
>We call $d(\mathbf{u}, \mathbf{v})$ the **Euclidean distance** between $\mathbf{u}$ and $\mathbf{v}$.
>
>>[!PROOF]- Proof: The Euclidean Metric is a Metric
>>
>>TODO
>>
>

>[!DEFINITION] Definition: Angle
>
>The **angle** between two nonzero vectors $\mathbf{u}$ and $\mathbf{v}$ of an [inner product space](./Inner%20Product%20Spaces.md) is defined using the [induced norm](#Geometry) and the [real arccosine function](../../../Analysis/Real%20Analysis/Real%20Functions/Real%20Trigonometric%20Functions/Inverse%20Real%20Trigonometric%20Functions.md#The%20Real%20Arccosine%20Function) as follows:
>
>$$\arccos\left(\frac{\langle\mathbf{u},\mathbf{v}\rangle}{||\mathbf{u}||\, ||\mathbf{v}||}\right)$$
>
>>[!NOTATION]
>>
>>$$\angle(\mathbf{u},\mathbf{v})$$
>>
>

### Orthogonality

>[!DEFINITION] Definition: Orthogonal Vectors
>
>Let $(V, \langle \cdot, \cdot \rangle)$ be an [inner product space](./Inner%20Product%20Spaces.md).
>
>The [vectors](../Vector%20Spaces.md) $v_1, \dotsc, v_n \in V$ are **orthogonal** if
>
>$$\langle v_i, v_j \rangle = 0$$
>
>for all $i \ne j$.
>
>>[!NOTATION]
>>
>>If $u, v \in V$ are [orthogonal](#Orthogonality), we write $u \perp v$.
>>
>

>[!DEFINITION] Definition: Orthonormal Vectors
>
>Let $(V, \langle \cdot, \cdot \rangle)$ be an [inner product space](./Inner%20Product%20Spaces.md).
>
>The [vectors](../Vector%20Spaces.md) $v_1, \dotsc, v_n \in V$ are **orthonormal** if
>
>$$\langle v_i, v_j \rangle = \begin{cases}0 & \text{if} & i \ne j \\ 1 & \text{if} & i = j\end{cases}$$
>
>for all $i, j \in \{1, \dotsc, n\}$.
>
>>[!THEOREM] Theorem: Orthonormality via Orthogonality and induced norm
>>
>>The [vectors](../Vector%20Spaces.md) $v_1, \dotsc, v_n \in V$ are [orthonormal](#Orthogonality) if and only if they are [orthogonal](#Orthogonality) and the [induced norm](#Geometry) of each is $1$.
>>
>>>[!PROOF]-
>>>
>>>We need to prove two things:
>>>
>>>    - (I) If $v_1, \dotsc, v_n \in V$ are [orthonormal](#Orthogonality), then they are [orthogonal](#Orthogonality) and the [induced norm](#Geometry) of each is $1$.
>>>    - (II) If $v_1, \dotsc, v_n \in V$ are [orthogonal](#Orthogonality) and the [induced norm](#Geometry) of each is $1$, then they are [orthonormal](#Orthogonality).
>>>
>>>**Proof of (I):**
>>>
>>>Since $\langle v_i, v_j \rangle = 0$ for all $i \ne j$, we know that $v_1, \dotsc, v_n$ are [orthogonal](#Orthogonality). The [induced norm](#Geometry) of $v_i$ is given by $||v_i|| = \sqrt{\langle v_i, v_i \rangle}$. Since $\langle v_i, v_j \rangle = 1$ whenever $i = j$, we have
>>>
>>>$$||v_i|| = \sqrt{1} = 1.$$
>>>
>>>**Proof of (II):**
>>>
>>>Since $\langle v_i, v_j \rangle = 0$ are [orthogonal](#Orthogonality), we have $\langle v_i, v_j \rangle = 0$ for all $i \ne j$. Since the [induced norm](#Geometry) of each is $1$, we have
>>>
>>>$$\langle v_i, v_j \rangle = ||v_i||^2 = 1^2 = 1$$
>>>
>>>whenever $i = j$.
>>>
>>
>

>[!ALGORITHM] Algorithm: Gram-Schmidt Orthonormalization
>
>Let $(V, \langle \cdot, \cdot \rangle)$ be an [inner product space](./Inner%20Product%20Spaces.md).
>
>Given $n$ [linearly independent](../Linear%20Combinations.md#Linear%20Independence) [vectors](../Vector%20Spaces.md) $v_1, \dotsc, v_n$, we can use **Gram-Schmidt orthonormalization** to obtain $n$ [linearly independent](../Linear%20Combinations.md#Linear%20Independence) [vectors](../Vector%20Spaces.md) $w_1, \dotsc, w_n$ which are [orthonormal](#Orthogonality) and whose [span](../Span.md) is the same as the [span](../Span.md) of $v_1, \dotsc, v_n$:
>
>1. The first [vector](../Vector%20Spaces.md) $w_1$ is just the normalized version of $v_1$ (with respect to the [induced norm](#Geometry)):
>
>$$w_1 = \frac{1}{||v_1||}v_1$$
>
>2. For each $j \in \{2, \dotsc, n\}$, define $\tilde {w}_j$ as
>
>$$\tilde{w}_j = v_{j}-\sum_{i = 1}^{j-1} \langle v_{j}, w_i\rangle w_i$$
>
>3. For each $j \in \{2, \dotsc, n\}$, the [vector](../Vector%20Spaces.md) $w_j$ is the normalization of $\tilde{w}_j$ (with respect to the [induced induced norm](#Geometry)):
>
>$$w_j = \frac{1}{||\tilde{w}_j||}\tilde{w}_j$$
>
>>[!EXAMPLE]-
>>
>>Consider the [real vectors](../../Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $v_1, v_2, v_3 \in \mathbb{R}^3$ and the standard [dot product](../../Linear%20Algebra/Real%20Vectors/Real%20Vectors.md):
>>
>>$$v_1 = \begin{bmatrix}1 \\ 1 \\ 0\end{bmatrix} \qquad v_2 = \begin{bmatrix}0 \\ 1 \\ 0\end{bmatrix} \qquad v_3 = \begin{bmatrix}1 \\ 1 \\ 1\end{bmatrix}$$
>>
>>We have
>>
>>$$w_1 = \frac{1}{||v_1||} v_1 = \frac{1}{\sqrt{1^2 + 1^2 + 0^2}} \begin{bmatrix}1 \\ 1 \\ 0\end{bmatrix} = \frac{1}{\sqrt{2}}\begin{bmatrix}1 \\ 1 \\ 0\end{bmatrix} = \begin{bmatrix}\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \\ 0\end{bmatrix}.$$
>>
>>For $\tilde{w}_2$, we have:
>>
>>$$\begin{aligned}\tilde{w}_2 & = v_2 - \sum_{i = 1}^{1} (v_2 \cdot w_i) w_i \\ & = v_2 - (v_2 \cdot w_1) w_1 \\ & = v_2 - \left(0\times \frac{1}{\sqrt{2}} + 1 \times \frac{1}{\sqrt{2}} + 0 \times 0\right) w_1 \\ & = v_2 - \frac{1}{\sqrt{2}}w_1 \\ & = \begin{bmatrix}0 \\ 1 \\ 0\end{bmatrix} - \begin{bmatrix}\frac{1}{2} \\ \frac{1}{2} \\ 0\end{bmatrix} = \begin{bmatrix}-\frac{1}{2} \\ \frac{1}{2} \\ 0\end{bmatrix}. \end{aligned}$$
>>
>>Now we normalize $\tilde{w}_2$ to obtain $w_2$:
>>
>>$$||\tilde{w}_2|| = \sqrt{\left(-\frac{1}{2}\right)^2 + \left(\frac{1}{2}\right)^2 + 0^2} = \sqrt{\frac{1}{4} + \frac{1}{4}} = \sqrt{\frac{1}{2}} = \frac{1}{\sqrt{2}}$$
>>
>>$$w_2 = \frac{1}{||\tilde{w}_2||}\tilde{w}_2 = \sqrt{2}\begin{bmatrix}-1/2 \\ 1/2 \\ 0\end{bmatrix} = \begin{bmatrix}-\frac{\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} \\ 0\end{bmatrix} = \begin{bmatrix}-\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \\ 0\end{bmatrix}.$$
>>
>>For $\tilde{w}_3$, we have:
>>
>>$$\begin{aligned}\tilde{w}_3 & = v_3 - \sum_{i = 1}^{2} (v_3 \cdot w_i) w_i \\ & = v_3 - (v_3 \cdot w_1) w_1 - (v_3 \cdot w_2) w_2\end{aligned}$$
>>
>>$$(v_3 \cdot w_1) = 1\left(\frac{1}{\sqrt{2}}\right) + 1\left(\frac{1}{\sqrt{2}}\right) + 1(0) = \frac{2}{\sqrt{2}} = \sqrt{2}$$
>>
>>$$(v_3 \cdot w_2) = 1\left(-\frac{1}{\sqrt{2}}\right) + 1\left(\frac{1}{\sqrt{2}}\right) + 1(0) = 0$$
>>
>>Substituting these back into the expression for $\tilde{w}_3$:
>>
>>$$\begin{aligned}\tilde{w}_3 & = \begin{bmatrix}1 \\ 1 \\ 1\end{bmatrix} - (\sqrt{2}) \begin{bmatrix}\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \\ 0\end{bmatrix} - (0) w_2 \\ & = \begin{bmatrix}1 \\ 1 \\ 1\end{bmatrix} - \begin{bmatrix}1 \\ 1 \\ 0\end{bmatrix} \\ & = \begin{bmatrix}0 \\ 0 \\ 1\end{bmatrix}\end{aligned}$$
>>
>>Normalizing $\tilde{w}_3$ to obtain $w_3$:
>>
>>$$w_3 = \frac{1}{||\tilde{w}_3||}\tilde{w}_3 = \frac{1}{1}\begin{bmatrix}0 \\ 0 \\ 1\end{bmatrix} = \begin{bmatrix}0 \\ 0 \\ 1\end{bmatrix}.$$
>>
>

>[!DEFINITION] Definition: Orthogonal Basis
>
>An **orthogonal basis** of an [inner product space](./Inner%20Product%20Spaces.md) is a [basis](../Hamel%20Bases.md) whose elements are [orthogonal](#Orthogonality).
>

>[!DEFINITION] Definition: Orthonormal Basis
>
>An **orthonormal basis** of an [inner product space](./Inner%20Product%20Spaces.md) is a [basis](../Hamel%20Bases.md) whose elements are [orthonormal](#Orthogonality).
>

>[!THEOREM] Theorem: Vector Representation through an Orthonormal Basis
>
>Let $(V, \langle \cdot, \cdot \rangle)$ be a [finite-dimensional](../Hamel%20Bases.md#Dimension) [inner product space](./Inner%20Product%20Spaces.md) and let $v \in V$.
>
>If $B = \{b_1, \dotsc, b_n\}$ is an [orthonormal](#Orthogonality) [basis](../Hamel%20Bases.md) of $V$, then
>
>$$v = \sum_{i=1}^n \langle v, b_i\rangle b_i.$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

