---
tags:
  - linear-algebra
  - algebra
  - mathematics
---

# Linearity (Functions)

>[!DEFINITION] Definition: Linearity
>
>
>
>A **linear transformation** or **vector space homomorphism** from a [vector space](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) $(V,F,+_V,\cdot_{FV})$ to a [vector space](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) $(W,F,+_W,\cdot_{FW})$ is a [function](../../Functions/Functions.md) $T: V \to W$ which has the following property for all $\lambda, \mu \in F$ and all $\mathbf{u}, \mathbf{v} \in V$:
>
>$$
>T(\lambda \mathbf{u} + \mu \mathbf{v}) = \lambda T(\mathbf{u}) + \mu T (\mathbf{v})
>$$
>
>>[!EXAMPLE]- Example: Linearity of Identity
>>
>>The [identity function](../../Functions/Functions.md) on any [vector space](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) $(V, F, +, \cdot)$ is [linear](./Linearity%20(Functions).md).
>>
>
>>[!EXAMPLE]- Example: Linearity of Zero Function
>>
>>Let $(V,F,+_V,\cdot_{FV})$ and $(W,F,+_W,\cdot_{FW})$ be [vector spaces](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md).
>>
>>The [function](../../Functions/Functions.md) $f: V \to W$ defined as
>>
>>$$
>>f(\mathbf{v}) = \mathbf{0}_W \qquad \forall \mathbf{v} \in V
>>$$
>>
>>is [linear](./Linearity%20(Functions).md).
>>
>
>>[!EXAMPLE]- Example: Linear Real Function
>>
>>Every [real function](../../Real%20Analysis/Real%20Functions/Real%20Functions.md) $f: \mathbb{R} \to \mathbb{R}$ defined as
>>
>>$$
>>f(x) = ax,
>>$$
>>
>>where $a \in \mathbb{R}$, is [linear](./Linearity%20(Functions).md).
>>
>>However, every [real function](../../Real%20Analysis/Real%20Functions/Real%20Functions.md) $g: \mathbb{R} \to \mathbb{R}$ defined as
>>
>>$$
>>g(x) = ax + b,
>>$$
>>
>>where $a \in \mathbb{R}$ and $b \in \mathbb{R} \setminus \{0\}$, is *not* [linear](./Linearity%20(Functions).md).
>>
>
>>[!EXAMPLE]- Example: Linearity of Differentiation
>>
>>Let $C^{\infty}$ be the [set](../../../Set%20Theory/Sets.md) of all [smooth](../../Real%20Analysis/Real%20Functions/Differentiability%20(Real%20Functions).md) [real functions](../../Real%20Analysis/Real%20Functions/Real%20Functions.md). It can be shown that $C^{\infty}$ is a [vector space](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md). The [function](../../Functions/Functions.md) which maps each $f \in C^{\infty}$ to its [derivative](../../Real%20Analysis/Real%20Functions/Differentiability%20(Real%20Functions).md) $f'$ is [linear](./Linearity%20(Functions).md).
>>
>

>[!DEFINITION] Definition: Kernel
>
>Let $(V, F, +_V, \cdot_{FV})$ and $(W, F, +_W, \cdot_{FW})$ be [vector spaces](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md).
>
>The **kernel** of a [linear transformation](./Linearity%20(Functions).md) $T: V \to W$ is the [set](../../../Set%20Theory/Sets.md) of all [vectors](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) $\mathbf{v} \in V$ which the transformation sends to the zero vector in $W$:
>
>$$
>\{\mathbf{v} \in V \mid T(\mathbf{v}) = \mathbf{0}_W\}
>$$
>
>>[!NOTATION] Notation
>>
>>$$
>>\ker(T)
>>$$
>>
>

>[!THEOREM] Theorem: Zero Vector to Zero Vector
>
>Every [linear transformation](./Linearity%20(Functions).md) $T: V \to W$ always transforms the [zero vector](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) of $V$ to the [zero vector](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) of $W$:
>
>$$
>T(\mathbf{0}_V) = \mathbf{0}_W
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Subspace Preservation
>
>Let $f: V \to W$ be a [linear transformation](./Linearity%20(Functions).md) from the [vector space](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) $V$ to the [vector space](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) $W$.
>
>If $U$ is a [subspace](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) of $V$, then $f(U)$ is a [subspace](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) of $W$.
>
>If $\tilde{U}$ is a [subspace](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) of $W$, then its [inverse image](../../Functions/Functions.md) $f^{-1}(\tilde{U})$ is a [subspace](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) of $V$.
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (I) If $U$ is a [subspace](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) of $V$, then $f(U)$ is a [subspace](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) of $W$.
>>- (II) If $\tilde{U}$ is a [subspace](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) of $W$, then the [inverse image](../../Functions/Functions.md) $f^{-1}(\tilde{U})$ is a [subspace](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) of $V$.
>>
>>**Proof of (I):**
>>
>>Obviously, $\mathbf{0}_W \in f(U)$, since $f$ is [linear](./Linearity%20(Functions).md).
>>
>>Let $\mathbf{w}_1, \mathbf{w}_2 \in f(U)$ and $\mathbf{u}_1, \mathbf{u}_2 \in U$ be such that $\mathbf{w}_1 = f(\mathbf{u}_1)$ and $\mathbf{w}_2 = f(\mathbf{u}_2)$. Since $\mathbf{u}_1 \in U$ and $\mathbf{u}_2 \in U$, we know that $\mathbf{u}_1 + \mathbf{u}_2 \in U$ and so $f(\mathbf{u}_1 + \mathbf{u}_2) \in f(U)$. Since $f$ is [linear](./Linearity%20(Functions).md), we have
>>
>>$$
>>f(\mathbf{u}_1 + \mathbf{u}_2) = f(\mathbf{u}_1) + f(\mathbf{u}_2) = \mathbf{w}_1 + \mathbf{w}_2 \in f(U).
>>$$
>>
>>Similarly, let $\mathbf{w} \in f(U)$ and $\mathbf{u} \in U$ be such that $\mathbf{w} = f(\mathbf{u})$. Since $U$ is a [subspace](../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md), we know that $\lambda \mathbf{u} \in U$ for all $\lambda \in F$ and so $f(\lambda \mathbf{u}) \in f(U)$. Since $f$ is [linear](./Linearity%20(Functions).md), we have
>>
>>$$
>>f(\lambda \mathbf{u}) = \lambda f(\mathbf{u}) = \lambda \mathbf{w} \in f(U)
>>$$
>>
>>**Proof of (II):**
>>
>>TODO
>>
>
>>[!EXAMPLE] Example: Kernel is a Subspace
>>
>>The [kernel](./Linearity%20(Functions).md) of a [linear transformation](./Linearity%20(Functions).md) $f: V \to W$ is always a [subspace](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) of $V$.
>>
>>>[!DEFINITION] Definition: Nullity
>>>
>>>The **nullity** of $f$ is the [dimension](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) of its [kernel](./Linearity%20(Functions).md):
>>>
>>>$$
>>>\dim \ker f
>>>$$
>>>
>>
>
>>[!EXAMPLE] Example: Image is a Subspace
>>
>>The [image](../../Functions/Functions.md) of a [linear transformation](./Linearity%20(Functions).md) $f: V \to W$ is always a [subspace](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) of $W$.
>>
>>>[!DEFINITION] Definition: Rank
>>>
>>>The **rank** of $f$ is the [dimension](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) of its  [image](../../Functions/Functions.md):
>>>
>>>$$
>>>\mathop{\operatorname{Rank}} f \overset{\text{def}}{=} \dim f(V)
>>>$$
>>>
>>
>

>[!THEOREM] Theorem: Rank-Nullity Theorem
>
>Let $V$ and $W$ be [finite dimensional](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) [vector spaces](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) and let $f: V \to W$.
>
>If $f$ is [linear](./Linearity%20(Functions).md), then the [dimension](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Dimension) of $V$ is equal to the sum of $f$'s [nullity](./Linearity%20(Functions).md) and $f$'s [rank](./Linearity%20(Functions).md):
>
>$$
>\dim V = \dim \ker f + \mathop{\operatorname{Rank}} f
>$$
>
>>[!PROOF]-
>>
>>Let $\mathbf{v}_1,\dotsc,\mathbf{v}_k$ be a [basis](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) for $\ker f$. We [extend](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) it to a [basis](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) $\mathbf{v}_1,\dotsc,\mathbf{v}_k, \mathbf{v}_{k+1},\dotsc,\mathbf{v}_n$ for $V$.
>>
>>Since $V$ is the [span](../../../Algebra/Vector%20Spaces/Span.md) of $\mathbf{v}_1, \dotsc, \mathbf{v}_n$, the [image](../../Functions/Functions.md) of $f$ is the following:
>>
>>$$
>>f(V) = f(\operatorname{span}(\mathbf{v}_1, \dotsc, \mathbf{v}_n))
>>$$
>>
>>Since the [image of a span is the span of the image](./Linearity%20(Functions).md), we have the following:
>>
>>$$
>>f(V) = \operatorname{span}(f(\mathbf{v}_1), \dotsc, f(\mathbf{v}_n))
>>$$
>>
>>However, since $\mathbf{v}_1,\dotsc,\mathbf{v}_k \in \ker f$, we know that $f(\mathbf{v}_1) = \cdots = f(\mathbf{v}_k) = \mathbf{0}$ and so $\mathbf{v}_1,\dotsc,\mathbf{v}_k$ don't contribute anything to the above [span](../../../Algebra/Vector%20Spaces/Span.md):
>>
>>$$
>>\operatorname{span}(f(\mathbf{v}_1), \dotsc, f(\mathbf{v}_n)) = \operatorname{span}(f(\mathbf{v}_{k+1}), \dotsc, f(\mathbf{v}_n))
>>$$
>>
>>Therefore, the [image](../../Functions/Functions.md) of $f$ is the [span](../../../Algebra/Vector%20Spaces/Span.md) of $f(\mathbf{v}_{k+1}), \dotsc, f(\mathbf{v}_n)$:
>>
>>$$
>>f(V) = \operatorname{span}(f(\mathbf{v}_{k+1}), \dotsc, f(\mathbf{v}_n))
>>$$
>>
>>Since $\mathbf{0}_W \in f(V)$, we know that
>>
>>$$
>>\mathbf{0}_W = \lambda_{k+1}f(\mathbf{v}_{k+1}) + \cdots + \lambda_n f(\mathbf{v}_n)
>>$$
>>
>>for some $\lambda_{k+1}, \dotsc, \lambda_n$. However, $f$ is [linear](./Linearity%20(Functions).md) and so we have:
>>
>>$$
>>\mathbf{0}_W = \lambda_{k+1}f(\mathbf{v}_{k+1}) + \cdots + \lambda_n f(\mathbf{v}_n) = f(\lambda_{k+1}\mathbf{v}_{k+1} + \cdots + \lambda_n\mathbf{v}_n)
>>$$
>>
>>This means that $\lambda_{k+1}\mathbf{v}_{k+1} + \cdots + \lambda_n\mathbf{v}_n \in \ker f$. But since $\mathbf{v}_{k+1},\dotsc,\mathbf{v}_{n}$ are [linearly independent](../../../Algebra/Vector%20Spaces/Linear%20Combinations.md#Linear%20Independence), this implies that $\lambda_{k+1} = \cdots = \lambda_n = 0$. Therefore, $\lambda_{k+1}f(\mathbf{v}_{k+1}), \dotsc, \lambda_n f(\mathbf{v}_n)$ are also [linearly independent](../../../Algebra/Vector%20Spaces/Linear%20Combinations.md#Linear%20Independence) and, since the are a [spanning set](../../../Algebra/Vector%20Spaces/Span.md#Spanning%20Sets) of $f(V)$, they are a [basis](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) for $f(V)$. Therefore, the [rank](./Linearity%20(Functions).md) of $f$ is $n - k$ and we have
>>
>>$$
>>\dim V = n = k + (n - k) = \dim \ker f + \mathop{\operatorname{Rank}} f
>>$$
>>
>

>[!THEOREM] Theorem: Span of Image is Image of Span
>
>Let $f: V \to W$ be a [linear transformation](./Linearity%20(Functions).md) from the [vector space](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) $V$ to the [vector space](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) $W$.
>
>If $S \subseteq V$, then the [span](../../../Algebra/Vector%20Spaces/Linear%20Combinations.md) of the [image](../../Functions/Functions.md) $f(S)$ is equal to the [image](../../Functions/Functions.md) of the [span](../../../Algebra/Vector%20Spaces/Linear%20Combinations.md) of $S$:
>
>$$
>\mathop{\operatorname{span}}(f(S)) = f(\mathop{\operatorname{span}}(S))
>$$
>
>>[!PROOF]-
>>
>>Since $f$ is [linear](./Linearity%20(Functions).md) and $\mathop{\operatorname{span}}(S)$ is a [subspace](../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) of $V$, we know that its [image](../../Functions/Functions.md) $f(\mathop{\operatorname{span}}(S))$ is a [subspace](../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) of $W$. Since $S \subseteq \mathop{\operatorname{span}}(S)$, we know that $f(S) \subseteq f(\mathop{\operatorname{span}}(S))$. By the definition of [span](../../../Algebra/Vector%20Spaces/Span.md), we know that if $U$ is a [subspace](../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) which contains $T$, then $\mathop{\operatorname{span}}(T) \subseteq U$, i.e we have $\mathop{\operatorname{span}}(f(S)) \subseteq f(\mathop{\operatorname{span}}(S))$ because $f(\mathop{\operatorname{span}}(S))$ is a [subspace](../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) which contains $f(S)$.
>>
>>Similarly, since $f$ is [linear](./Linearity%20(Functions).md) and $\mathop{\operatorname{span}}(f(S))$ is a [subspace](../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) of $W$, we know that the [inverse image](../../Functions/Functions.md) $f^{-1}(\mathop{\operatorname{span}}(f(S)))$ is a [subspace](../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) of $V$. Since $f(S) \subseteq \mathop{\operatorname{span}}(f(S))$, we know that $S \subseteq f^{-1}(\mathop{\operatorname{span}}(f(S)))$. By the definition of [span](../../../Algebra/Vector%20Spaces/Span.md), we know that if $U$ is a [subspace](../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) which contains $T$, then $\mathop{\operatorname{span}}(T) \subseteq U$, i.e. we have $\mathop{\operatorname{span}}(S) \subseteq f^{-1}(\mathop{\operatorname{span}}(f(S)))$ because $f^{-1}(\mathop{\operatorname{span}}(f(S)))$ is a [subspace](../../../Algebra/Vector%20Spaces/Linear%20Subspaces.md) which contains $S$. Since $\mathop{\operatorname{span}}(S) \subseteq f^{-1}(\mathop{\operatorname{span}}(f(S)))$, we have that $f(\mathop{\operatorname{span}}(S)) \subseteq f(\mathop{\operatorname{span}}(f(S)))$.
>>
>>We have shown that $\mathop{\operatorname{span}}(f(S)) \subseteq f(\mathop{\operatorname{span}}(S))$ and $f(\mathop{\operatorname{span}}(S)) \subseteq f(\mathop{\operatorname{span}}(f(S)))$, i.e. $\mathop{\operatorname{span}}(f(S)) = f(\mathop{\operatorname{span}}(S))$.
>>
>
>>[!EXAMPLE]- Example
>>
>>The [function](../../Real%20Analysis/Real%20Vector%20Functions/Real%20Vector%20Functions.md) $f: \mathbb{R}^3 \to \mathbb{R}^4$ with
>>
>>$$
>>f \left(\begin{bmatrix}x \\ y \\ z\end{bmatrix}\right) = \begin{bmatrix}x + z \\ x + 2y \\ y - z \\ x + y + z\end{bmatrix}
>>$$
>>
>>is [linear](./Linearity%20(Functions).md).
>>
>>Suppose
>>
>>$$
>>S = \left\{\begin{bmatrix}1 \\ 0 \\ 0\end{bmatrix}, \begin{bmatrix}1 \\ 1 \\ 0\end{bmatrix}\right\}.
>>$$
>>
>>The [span](../../../Algebra/Vector%20Spaces/Linear%20Combinations.md#Span) of $S$ is
>>
>>$$
>>\begin{aligned}
>>\mathop{\operatorname{span}} S &= \left\{\lambda \begin{bmatrix}1 \\ 0 \\ 0\end{bmatrix} + \mu \begin{bmatrix}1 \\ 1 \\ 0\end{bmatrix}: \lambda, \mu \in \mathbb{R}\right\} \\ &= \left\{\begin{bmatrix}\lambda \\ 0 \\ 0\end{bmatrix} + \begin{bmatrix}\mu \\ \mu \\ 0\end{bmatrix}: \lambda, \mu \in \mathbb{R}\right\} \\ &= \left\{\begin{bmatrix}\lambda + \mu \\ \mu \\ 0\end{bmatrix}: \lambda, \mu \in \mathbb{R}\right\} \\ &= \left\{\begin{bmatrix}r \\ s \\ 0\end{bmatrix}: r, s \in \mathbb{R}\right\} 
>>\end{aligned}
>>$$
>>
>>Therefore, $f(\mathop{\operatorname{span}}(S))$ is
>>
>>$$
>>\begin{aligned}
>>f(\mathop{\operatorname{span}}(S)) &= f\left( \left\{\begin{bmatrix}r \\ s \\ 0\end{bmatrix}: r, s \in \mathbb{R}\right\} \right) \\ &= \left\{f\left(\begin{bmatrix}r \\ s \\ 0\end{bmatrix}\right) : r, s \in \mathbb{R} \right\} \\ &= \left\{\begin{bmatrix}r \\ r + 2s \\ s \\ r+s\end{bmatrix}: r, s \in \mathbb{R}\right\}
>>\end{aligned}
>>$$
>>
>>The [image](../../Functions/Functions.md) of $S$ is the following:
>>
>>$$
>>f(S) = \left\{f\left(\begin{bmatrix}1 \\ 0 \\ 0\end{bmatrix}\right), f\left(\begin{bmatrix}1 \\ 1 \\ 0 \\ 1\end{bmatrix}, \begin{bmatrix}1 \\ 3 \\ 1 \\ 2\end{bmatrix}\right)\right\}
>>$$
>>
>>Its [span](../../../Algebra/Vector%20Spaces/Span.md) is the following:
>>
>>$$
>>\begin{aligned}
>>\mathop{\operatorname{span}}(f(S)) &= \left\{ \lambda \begin{bmatrix}1 \\ 1 \\ 0 \\ 1\end{bmatrix} + \mu \begin{bmatrix}1 \\ 3 \\ 1 \\ 2\end{bmatrix}: \lambda, \mu \in \mathbb{R}\right\} \\
>>&= \left\{\begin{bmatrix}\lambda + \mu \\ (\lambda + \mu) + 2\mu \\ \mu \\ (\lambda + \mu) + \mu\end{bmatrix}: \lambda, \mu \in \mathbb{R}\right\} \\
>>&= \left\{\begin{bmatrix}r \\ r + 2s \\ s \\ r+s\end{bmatrix}: r, s \in \mathbb{R}\right\}
>>\end{aligned}
>>$$
>>
>

>[!THEOREM] Theorem: Linearity of Composition
>
>If $f: V \to U$ and $g: f(V) \to W$ are [linear transformations](./Linearity%20(Functions).md), then their [composition](../../Functions/Functions.md) $g \circ f$ is also a [linear transformation](./Linearity%20(Functions).md) $g \circ f: V\to W$.
>
>>[!PROOF]-
>>
>>$$
>>\begin{aligned}g\circ f(\lambda \mathbf{u} +\mu\mathbf{v}) &= g(f(\lambda \mathbf{u} +\mu\mathbf{v}))\\ &= g(\lambda f(\mathbf{u}) + \mu f(\mathbf{v})) \\ &= g(\lambda f(\mathbf{u})) + g(\mu f(\mathbf{v})) \\ &= \lambda g(f(\mathbf{u})) +\mu g(f(\mathbf{v}))\\ &= \lambda g\circ f(\mathbf{u})+\mu g\circ f (\mathbf{v})\end{aligned}
>>$$
>>
>

>[!THEOREM] Theorem: Linearity of Inverse Transformations
>
>If $T$ is a [bijective](../../Functions/Injections,%20Surjections%20and%20Bijections.md#Bijections) [linear transformation](./Linearity%20(Functions).md), then its [inverse](../../Functions/Injections,%20Surjections%20and%20Bijections.md#Injections) $T^{-1}$ is also a [bijective](../../Functions/Injections,%20Surjections%20and%20Bijections.md#Bijections) [linear transformation](./Linearity%20(Functions).md).
>
>>[!DEFINITION] Definition: Vector Space Isomorphism
>>
>>[Bijective](../../Functions/Injections,%20Surjections%20and%20Bijections.md#Bijections) [linear transformations](./Linearity%20(Functions).md) are known as **vector space isomorphisms**.
>>
>>>[!DEFINITION] Definition: Automorphism
>>>
>>>An **automorphism** is a [bijective](../../Functions/Injections,%20Surjections%20and%20Bijections.md#Bijections) [endomorphism](./Linearity%20(Functions).md).
>>>
>>
>
>>[!PROOF]-
>>
>>Let $f: V \to W$ be a [bijective](../../Functions/Injections,%20Surjections%20and%20Bijections.md#Bijections) [linear transformation](./Linearity%20(Functions).md) and let $\mathbf{w}_1, \mathbf{w}_2 \in W$. Since $f$ is [bijective](../../Functions/Injections,%20Surjections%20and%20Bijections.md#Bijections), there exist $\mathbf{v}_1, \mathbf{v}_2 \in V$ such that
>>
>>$$
>>\mathbf{w}_1 = f(\mathbf{v}_1) \qquad \text{and} \qquad \mathbf{w}_2 = f(\mathbf{v}_2).
>>$$
>>
>>Furthermore, 
>>
>>$$
>>f^{-1}(\mathbf{w}_1 + \mathbf{w}_2) = f^{-1}(f(\mathbf{v}_1) + f(\mathbf{v}_2)) = f^{-1}(f(\mathbf{v}_1 + \mathbf{v}_2)) = \mathbf{v}_1 + \mathbf{v}_2.
>>$$
>>
>>Let $\mathbf{w} \in W$ and $\mathbf{v} \in V$ with $\mathbf{w} = f(\mathbf{v})$. We have the following:
>>
>>$$
>>f^{-1}(\lambda \mathbf{w}) = f^{-1}(\lambda f(\mathbf{v})) = f^{-1}(f(\lambda \mathbf{v})) = \lambda \mathbf{v} = \lambda f^{-1}(f(\mathbf{v})) = \lambda f^{-1}(\mathbf{w})
>>$$
>>
>

>[!THEOREM] Theorem: Basis Transformation
>
>Let $(V, F)$ and $(W, F)$ be [finite dimensional](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) [vector spaces](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md), let $\mathbf{v}_1,  \dotsc, \mathbf{v}_n$ be a [basis](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) of $V$ and let $\mathbf{w}_1,  \dotsc, \mathbf{w}_n \in W$ be arbitrary.
>
>There exists exactly one [linear transformation](./Linearity%20(Functions).md) $f: V \to W$ such that $f(\mathbf{v}_i) = \mathbf{w}_i$ for all $i \in \{1, \dotsc, n\}$. Moreover, $f$ is [bijective](../../Functions/Injections,%20Surjections%20and%20Bijections.md) if and only if $\mathbf{w}_1, \dotsc, \mathbf{w}_n$ is a [basis](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) of $W$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Injectivity Condition for Linear Transformations
>
>A [linear transformation](./Linearity%20(Functions).md) $f: V \to W$ is [injective](../../Functions/Injections,%20Surjections%20and%20Bijections.md) if and only if $\mathbf{0}_V$ is the only element of its [kernel](./Linearity%20(Functions).md).
>
>$$
>\ker f = \{\mathbf{0}_V\}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Injectivity $\implies$ Bijectivity for Equal Finite Dimensions
>
>Let $f: V \to W$ be a [linear transformation](./Linearity%20(Functions).md).
>
>If $f$ is [injective](../../Functions/Injections,%20Surjections%20and%20Bijections.md) and the [dimensions](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Dimension) of $V$ and $W$ are finite and equal, then $f$ is [bijective](../../Functions/Injections,%20Surjections%20and%20Bijections.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Matrix Representations

>[!THEOREM] Theorem: Matrix Representation of a Linear Transformation
>
>Let $(V,F,+,\cdot)$ and $(W,F,+,\cdot)$ be [vector spaces](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) and let $B_V$ and $B_W$ be [ordered bases](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Ordered%20Bases) of $V$ and $W$, respectively.
>
>If $T: V \to W$ is a [linear transformation](./Linearity%20(Functions).md), then there exists a unique [matrix](../../../Algebra/Matrices/Matrices.md) ${}_{B_W} [T]_{B_V}\in F^{\dim(W)\times \dim(V)}$ such that the [coordinate vector](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Ordered%20Bases) $[T(\mathbf{v})]_{B_W}$ is equal to the [product](../../../Algebra/Matrices/Matrix%20Operations.md) of ${}_{B_W} [T]_{B_V}$ and the [coordinate vector](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Ordered%20Bases) $[\mathbf{v}]_{B_V}$ for every $\mathbf{v} \in V$:
> 
>$$
>[T(\mathbf{v})]_{B_W} = {}_{B_W} [T]_{B_V}\cdot [\mathbf{v}]_{B_V},
>$$
>
>>[!WARNING] Warning: Dependence on the Choice of Bases
>>
>>The coefficients of the [matrix](../../../Algebra/Matrices/Matrices.md) ${}_{B_W} [T]_{B_V}$ depend on the choice of $B_V$ and $B_W$, i.e. different [ordered bases](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Ordered%20Bases) will make the coefficients of the [matrix representation](../../../Algebra/Matrices/Matrices.md) of $T$ different.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: Matrix Representation of Differentiation
>>
>>Let $P_n$ be the [vector space](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) of all [real polynomial function](../../Real%20Analysis/Real%20Functions/Real%20Polynomial%20Functions.md) expressible via a [polynomial](../../../Algebra/Polynomials/Univariate%20Polynomials.md) of [degree](../../../Algebra/Polynomials/Univariate%20Polynomials.md) $\le n$:
>>
>>$$
>>P_n = \{f: \mathbb{R} \to \mathbb{R} \mid f \text{ is polynomial and } \deg (f) \le n\}
>>$$
>>
>>We know that $(1, x^1, x^2, x^3)$ is an [ordered basis](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Ordered%20Bases) for $P_3$ and $(1, x^1, x^2)$ is an [ordered basis](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Ordered%20Bases) for $P_2$. The [matrix representation](#Matrix%20Representations) of the [differentiation operator](../../Real%20Analysis/Real%20Functions/Differentiability%20(Real%20Functions).md) with respect to $P_3$ and $P_2$ is the following:
>>
>>$$
>>{}_{P_2} [D]_{P_3} = \begin{bmatrix}0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3\end{bmatrix}
>>$$
>>
>>Consider $f(x) = -2x^3 +x^2$ with $D(f(x)) = -6x^2 + 2x$. We have:
>>
>>$$
>>[f]_{P_3} = \begin{bmatrix}0 \\ 0 \\ 1 \\ -2\end{bmatrix} \qquad [D(f(x))]_{P_2} = \begin{bmatrix}0 \\ 2 \\ -6\end{bmatrix}
>>$$
>>
>>One can easily very the following:
>>
>>$$
>>\begin{aligned}[D(f(x))]_{P_2} &= {}_{P_2} [D]_{P_3} \cdot [f]_{P_3} \\ \begin{bmatrix}0 \\ 2 \\ -6\end{bmatrix} &= \begin{bmatrix}0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3\end{bmatrix} \begin{bmatrix}0 \\ 0 \\ 1 \\ -2\end{bmatrix}\end{aligned}
>>$$
>>
>

>[!THEOREM] Theorem: Input Basis Change
>
>Let $(V,F,+,\cdot)$ and $(W,F,+,\cdot)$ be [vector spaces](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md), let $B_V$ and $B_V'$ be [ordered bases](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Ordered%20Bases) of $V$, let $B_W$ be an [ordered basis](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Ordered%20Bases) of $W$ and let $T: V \to W$  be a [linear transformation](./Linearity%20(Functions).md).
>
>If the [matrix representation](#Matrix%20Representations) of $T$ with respect to $B_V$ and $B_W$ is ${}_{B_W} [T]_{B_V}$, then its [matrix representation](#Matrix%20Representations) with respect to $B_V'$ is the [product](../../../Algebra/Matrices/Matrix%20Operations.md) of ${}_{B_W} [T]_{B_V}$ with the [matrix representation](#Matrix%20Representations) of the [identity function](../../Functions/Functions.md) of $V$ with respect to $B_V$ and $B_V'$:
>
>$$
>{}_{B_W} [T]_{B_V'} = {}_{B_W} [T]_{B_V} \cdot {}_{B_V} [\operatorname{id}]_{B_V'}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Output Basis Change
>
>Let $(V,F,+,\cdot)$ and $(W,F,+,\cdot)$ be [vector spaces](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md), let $B_V$ be an [ordered basis](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Ordered%20Bases) of $V$, let $B_W$ and $B_W'$ be [ordered bases](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Ordered%20Bases) of $W$ and let $T: V \to W$  be a [linear transformation](./Linearity%20(Functions).md).
>
>If the [matrix representation](#Matrix%20Representations) of $T$ with respect to $B_V$ and $B_W$ is ${}_{B_W} [T]_{B_V}$, then its [matrix representation](#Matrix%20Representations) with respect to $B_W'$ is the [product](../../../Algebra/Matrices/Matrix%20Operations.md) of the [matrix representation](#Matrix%20Representations) of the [identity function](../../Functions/Functions.md) of $V$ (with respect to $B_W$ and $B_W'$) and ${}_{B_W} [T]_{B_V}$:
>
>$$
>{}_{B_W'} [T]_{B_V} = {}_{B_W'} [\operatorname{id}]_{B_W} \cdot {}_{B_W} [T]_{B_V}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]-
>>
>>Let $P_n$ be the [vector space](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) of all [real polynomial function](../../Real%20Analysis/Real%20Functions/Real%20Polynomial%20Functions.md) expressible via a [polynomial](../../../Algebra/Polynomials/Univariate%20Polynomials.md) of [degree](../../../Algebra/Polynomials/Univariate%20Polynomials.md) $\le n$:
>>
>>$$
>>P_n = \{f: \mathbb{R} \to \mathbb{R} \mid f \text{ is polynomial and } \deg (f) \le n\}
>>$$
>>
>>We know that $(1, x, x^2, x^3)$ is an [ordered basis](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Ordered%20Bases) for $P_3$ and $(1, x, x^2)$ is an [ordered basis](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Ordered%20Bases) for $P_2$. The [matrix representation](#Matrix%20Representations) of the [differentiation operator](../../Real%20Analysis/Real%20Functions/Differentiability%20(Real%20Functions).md) with respect to $P_3$ and $P_2$ is the following:
>>
>>$$
>>{}_{P_2} [D]_{P_3} = \begin{bmatrix}0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3\end{bmatrix}
>>$$
>>
>>We want to find the [matrix representation](#Matrix%20Representations) of the [differentiation operator](../../Real%20Analysis/Real%20Functions/Differentiability%20(Real%20Functions).md) with respect to $P_3$ and the [ordered basis](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Ordered%20Bases) $P_2' = (1, x+1, x^2 + x + 1)$. We have the following:
>>
>>$$
>>{}_{P_2'} [D]_{P_3} = {}_{P_2'} [\operatorname{id}]_{P_2} \cdot {}_{P_2} [D]_{P_3}
>>$$
>>
>>Since $\operatorname{id}$ is the [identity function](../../Functions/Functions.md), we know that ${}_{P_2'} [\operatorname{id}]_{P_2}$ is just the [inverse](../../../Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md) of ${}_{P_2} [\operatorname{id}]_{P_2'}$:
>>
>>$$
>>{}_{P_2'} [\operatorname{id}]_{P_2} = ({}_{P_2} [\operatorname{id}]_{P_2'})^{-1}
>>$$
>>
>>Finding ${}_{P_2} [\operatorname{id}]_{P_2'}$ is easy using the usual algorithm:
>>
>>$$
>>\begin{aligned}
>>{}_{P_2} [\operatorname{id}]_{P_2'} &= \begin{bmatrix}\vert & \vert & \vert \\ [\operatorname{id}(1)]_{P_2} & [\operatorname{id}(x+1)]_{P_2} & [\operatorname{id}(x^2 + x + 1)]_{P_2} \\ \vert & \vert & \vert\end{bmatrix} \\ &= \begin{bmatrix}\vert & \vert & \vert \\ [1]_{P_2} & [x+1]_{P_2} & [x^2 + x + 1]_{P_2} \\ \vert & \vert & \vert\end{bmatrix} \\ &= \begin{bmatrix}1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1\end{bmatrix}\end{aligned}
>>$$
>>
>>Its [inverse](../../../Algebra/Matrices/Square%20Matrices/Matrix%20Invertibility.md) is:
>>
>>$$
>>({}_{P_2} [\operatorname{id}]_{P_2'})^{-1} = \begin{bmatrix}1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1\end{bmatrix}^{-1} = \begin{bmatrix}1 & -1 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 1\end{bmatrix}
>>$$
>>
>>We therefore have
>>
>>$$
>>{}_{P_2'} [\operatorname{id}]_{P_2} = \begin{bmatrix}1 & -1 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 1\end{bmatrix}
>>$$
>>
>>and can finally calculate ${}_{P_2'} [D]_{P_3}$:
>>
>>$$
>>{}_{P_2'} [D]_{P_3} = \begin{bmatrix}1 & -1 & 0 \\ 0 & 1 & -1 \\ 0 & 0 & 1\end{bmatrix} \begin{bmatrix}0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3\end{bmatrix} = \begin{bmatrix}0 & 1 & -2 & 0 \\ 0 & 0 & 2 & -3 \\ 0 & 0 & 0 & 3\end{bmatrix}
>>$$
>>
>

>[!ALGORITHM] Algorithm: Finding the Matrix Representation
>
>Let $(V,F,+,\cdot)$ and $(W,F,+,\cdot)$ be [vector spaces](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) and let $T: V \to W$ be a [linear transformation](./Linearity%20(Functions).md).
>
>We want to find the [matrix representation](./Linearity%20(Functions).md) ${}_{B_W}[T]_{B_V}$ with respect to two [ordered bases](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Ordered%20Bases) of our choice: $B_V = (\mathbf{b}_1^V,\cdots,\mathbf{b}_m^V)$ for $V$ and $B_W = (\mathbf{b}_1^W,\cdots,\mathbf{b}_n^W)$ for $W$. 
> 
>1. Determine the effect of $T$ on the elements of the input basis $B_V$, i.e. determine $\mathbf{w}_1, \dotsc, \mathbf{w}_m$ by applying $T$ to $\mathbf{b}_1^V,\cdots,\mathbf{b}_m^V$:
>
>$$
>\mathbf{w}_1 = T(\mathbf{b}_1^V) \qquad \cdots \qquad \mathbf{w}_m = T(\mathbf{b}_m^V)
>$$
>
>2. Determine the [coordinate vectors](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md#Ordered%20Bases) $[\mathbf{w}_1]_{B_W},\cdots,[\mathbf{w}_m]_{B_W}$ of the resulting vectors with respect to the output basis $B_W$.
>	- The specific calculation depends on the nature of the [vector space](../../../Algebra/Vector%20Spaces/Vector%20Spaces.md) (e.g., solving a linear system of equations).
>
>3. Construct ${}_{B_W}[T]_{B_V}$ by using these [coordinate vectors](../../../Algebra/Vector%20Spaces/Hamel%20Bases.md) as the columns of the matrix:
>
>$$
>{}_{B_W}[T]_{B_V} = \begin{bmatrix}\vert & \vert & \vert \\ [\mathbf{w}_1]_{B_W} & \cdots & [\mathbf{w}_m]_{B_W} \\ \vert & \vert & \vert \end{bmatrix} = \begin{bmatrix}\vert & \vert & \vert \\ [T(\mathbf{b}_1^V)]_{B_W} & \cdots & [T(\mathbf{b}_m^V)]_{B_W} \\ \vert & \vert & \vert \end{bmatrix}
>$$
>