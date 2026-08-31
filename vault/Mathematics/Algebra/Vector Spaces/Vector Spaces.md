---
tags:
  - linear-algebra
  - algebra
  - mathematics
---

# Vector Spaces

>[!DEFINITION] Definition: Vector Space
>
>A **vector space** $(V,F,+,\cdot)$ consists of a non-[empty](../../Set%20Theory/Sets.md) [set](../../Set%20Theory/Sets.md) $V$ and a [field](../Fields/Fields.md) $F$ which are equipped with two [operations](../../Analysis/Functions/Functions.md), **vector addition** $+: V \times V \to V$ and a **scalar multiplication** $\cdot: V \times F \to V$, which have the following properties:
>
>- Commutativity: $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$ for all $\mathbf{u},\mathbf{v} \in V$.
>- Associativity I: $\mathbf{u} + (\mathbf{v} + \mathbf{w}) = (\mathbf{u} + \mathbf{v}) + \mathbf{w}$ for all $\mathbf{u},\mathbf{v}, \mathbf{w} \in V$.
>- Associativity II: $(\lambda\mu)\mathbf{u} = \lambda(\mu\mathbf{u})$ for all $\lambda,\mu\in F$ and all $\mathbf{u} \in V$.
>- Distributivity I: $\lambda (\mathbf{u} + \mathbf{v}) = \lambda\mathbf{u}+\lambda\mathbf{v}$ for all $\mathbf{u},\mathbf{v} \in V$ and all $\lambda \in F$.
>- Distributivity II: $(\lambda + \mu)\mathbf{v} = \lambda\mathbf{v}+\mu\mathbf{v}$ for all $\lambda,\mu \in F$ and all $\mathbf{v}\in V$.
>- Existence of a zero vector: There is an element $\mathbf{0} \in V$ such that $\mathbf{v} + \mathbf{0} = \mathbf{v}$ for all $\mathbf{v} \in V$.
>- Existence of the identity element: There is an element $1 \in F$ such that $1 \cdot \mathbf{u} = \mathbf{u}$ for all $\mathbf{u}\in V$.
>- Existence of vector inverses: For every $\mathbf{v} \in V$ there exists some $-\mathbf{v} \in V$ such that $\mathbf{v} + (-\mathbf{v}) = \mathbf{0}$.
>
>The elements of $V$ are called **vectors**.
>
>>[!NOTATION]
>>
>>Vectors are usually denoted in one of the following ways: 
>>
>>$$
>>\mathbf{v} \qquad \boldsymbol{v} \qquad \vec{v}
>>$$
>>
>>The following notations are also used, albeit less often:
>>
>>$$
>>\underline{v} \qquad \overline{v}
>>$$
>>
>
>>[!NOTATION] Notation: Vector Subtraction
>>
>>For any two vectors $\mathbf{u}$ and $\mathbf{v}$, where $-\mathbf{v}$ is the vector inverse of $\mathbf{v}$, we denote $\mathbf{u} + (-\mathbf{v})$ as simply $\mathbf{u} - \mathbf{v}$.
>>
>

>[!THEOREM] Theorem: Vector Space $\implies$ Abelian Group
>
>If $(V, F, +, \cdot)$ is a [vector space](#Vector%20Spaces), then $(V, +)$ is an [abelian group](../Groups/Abelian%20Groups.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Uniqueness of the Zero Vector
>
>Every [vector space](#Vector%20Spaces) has exactly one zero vector.
>
>>[!PROOF]-
>>
>>Suppose that the vector space $(V,F,+,\cdots)$ had two zero vectors $\mathbf{0}, \mathbf{0}' \in V$, i.e. $\mathbf{v}+ \mathbf{0} = \mathbf{v}$ $\mathbf{v}+ \mathbf{0}'= \mathbf{v}$ for all $\mathbf{v} \in V$.
>>
>>It follows then that
>>
>>$$
>>\mathbf{0} + \mathbf{0}' = \mathbf{0}
>>$$
>>
>>$$
>>\mathbf{0}' + \mathbf{0} = \mathbf{0}'
>>$$
>>
>>But vector addition is commutative and so $\mathbf{0} + \mathbf{0}' = \mathbf{0}' + \mathbf{0}$ which means that $\mathbf{0} = \mathbf{0}'$.
>>
>

>[!THEOREM] Theorem: Uniqueness of Vector Inverses
>
>For every vector $\mathbf{v} \in V$ in a [vector space](#Vector%20Spaces) $(V,F,+,\cdot)$ there is exactly one inverse vector $-\mathbf{v} \in V$ such that
>
>$$
>\mathbf{v} + (-\mathbf{v}) = \mathbf{0}
>$$
>
>>[!PROOF]-
>>
>>Suppose that there was another vector $\mathbf{v}' \in V$ such that
>>
>>$$
>>\mathbf{v} + \mathbf{v}' = \mathbf{0}
>>$$
>>
>>It then follows that
>>
>>$$
>>-\mathbf{v} + (\mathbf{v}+\mathbf{v}') = -\mathbf{v}+\mathbf{0}=-\mathbf{v}
>>$$
>>
>>and so
>>
>>$$
>>\mathbf{v}' = (-\mathbf{v}+\mathbf{v})+\mathbf{v}'=-\mathbf{v}+(\mathbf{v}+\mathbf{v}')=-\mathbf{v}+\mathbf{0}=-\mathbf{v}
>>$$
>>
>

>[!EXAMPLE]- Example: Field as a Vector Space
>
>Let $(F, +_F, \cdot_F)$ be a [field](../Fields/Fields.md).
>
>For each $n \in \mathbb{N}_{\ge 1}$ we define a **scalar multiplication** $\cdot: F \times F^n \to F^n$ on the [direct product](../Groups/Direct%20Product.md) $F^n$ of the [abelian groups](../Groups/Abelian%20Groups.md) $(F,+_F)$:
>
>$$
>\lambda \cdot (x_1, \dotsc, x_n) \overset{\text{def}}{=} (\lambda \cdot_F x_1, \dotsc, \lambda \cdot_F x_n)
>$$
>
>The object $(F^n, F, +_{F^n}, \cdot)$ is a [vector space](./Vector%20Spaces.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!DEFINITION] Definition: Subset Sum
>
>Let $(V,F,+,\cdot)$ be a [vector space](./Vector%20Spaces.md) and let $S_1, \dotsc, S_n \subseteq V$.
>
>The **sum** of $S_1, \dotsc, S_n \subseteq V$ is the following [set](../../Set%20Theory/Sets.md):
>
>$$
>\{\mathbf{v} \in V \mid \mathbf{v} = \mathbf{s}_1 + \cdots + \mathbf{s}_n, \mathbf{s}_k \in S_k\}
>$$
>

## Isomorphicity

>[!DEFINITION] Definition: Isomorphic Vector Spaces
>
>Two [vector spaces](./Vector%20Spaces.md) $V$ and $W$ are **isomorphic** if there exists a [bijective](../../Analysis/Functions/Injections,%20Surjections%20and%20Bijections.md) [linear transformation](../../Analysis/Functional%20Analysis/Linearity/Linearity%20(Functions).md) $f: V \to W$ between them.
>

>[!THEOREM] Theorem: Isomorphicity of Finite Dimensional Spaces
>
>Two [finite dimensional](./Hamel%20Bases.md) [vector spaces](./Vector%20Spaces.md) are [isomorphic](./Vector%20Spaces.md) if and only if they have the same [dimension](./Hamel%20Bases.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>