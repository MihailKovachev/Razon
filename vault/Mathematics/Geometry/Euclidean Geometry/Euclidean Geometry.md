---
title: Euclidean Geometry
tags:
  - euclidean-geometry
  - geometry
  - mathematics
---

# Euclidean Geometry

>[!DEFINITION] Definition: Euclidean Geometry
>
>**Euclidean geometry** is the study of [topological spaces](../../Topology/Topological%20Spaces.md) which are [homeomorphic](../../Topology/Continuity/Homeomorphisms/Homeomorphic%20Spaces.md) to some [Euclidean space](../../Analysis/Real%20Analysis/The%20Topology%20of%20Euclidean%20Space.md).
>

Euclidean geometry considers space as an abstract object, known as a [topological space](../../Topology/Topological%20Spaces.md). This object is just a [set](../../Set%20Theory/Sets.md) with some special mathematical properties which allow us to rigorously define the notions of distance and "closeness" so that they match with our observations of the physical world.

The "[homeomorphic](../../Topology/Continuity/Homeomorphisms/Homeomorphic%20Spaces.md) to some [Euclidean space](../../Analysis/Real%20Analysis/The%20Topology%20of%20Euclidean%20Space.md)" part means that there is a [bijection](../../Analysis/Functions/Injections,%20Surjections%20and%20Bijections.md) between this [set](../../Set%20Theory/Sets.md) and some [Euclidean space](../../Analysis/Real%20Analysis/The%20Topology%20of%20Euclidean%20Space.md) $\mathbb{R}^n$ - in other words, each element (**point**) of the [set](../../Set%20Theory/Sets.md) can be uniquely associated with an $n$-dimensional [real column vector](../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Vector.md) $\mathbb{R}^n$. This is very useful because it allows us to apply [real analysis](../../Analysis/Real%20Analysis/index.md) to study geometry.

>[!NOTATION]
>
>Points are usually denoted with uppercase Latin letters: $P,Q,K,L,$ etc.
>
>The fact that points can be associated with vectors is so fundamental that we often think of the point and its associated vector as the same thing and write $P = \begin{bmatrix}p_1 & \cdots & p_n\end{bmatrix}^\mathsf{T}$ or more commonly $P = (p_1, \cdots, p_n)$.
>
>

>[!DEFINITION] Definition: Locus of Points
>
>A **locus of points** is any [set](../../Set%20Theory/Sets.md) of [points](Euclidean%20Geometry.md).
>

Once again, points and vectors are so closely related in geometry that we introduce the notion of a vector "pointing" from one point to another.

>[!DEFINITION] Definition: Vector between Points
>
>The vector which "points" from point $P$ to point $Q$, denoted by $\overrightarrow{PQ}$ is the [difference](../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Vector.md) between the [vector](../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Vector.md) associated with $P$ and the [vector](../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Vector.md) associated with $Q$:
>
>$$
>\overrightarrow{PQ} = Q - P
>$$
>

>[!DEFINITION] Definition: Distance between Points
>
>The **distance** between two [points](Euclidean%20Geometry.md) $P$ and $Q$ is the norm of the [vector](Euclidean%20Geometry.md) $\overrightarrow{PQ}$ or $\overrightarrow{QP}$:
>
>$$
>d(P, Q) \overset{\text{def}}{=} |\overrightarrow{PQ}| = |\overrightarrow{QP}|
>$$
>