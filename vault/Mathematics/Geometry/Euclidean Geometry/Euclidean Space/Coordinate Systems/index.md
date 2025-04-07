---
title: Coordinate Systems for Euclidean Space
tags:
    - coordinate-systems
    - euclidean-geometry
    - geometry
    - mathematics
---

# Coordinate Systems for Euclidean Space

Each [vector](../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Vector.md) $\mathbf{p}$ in the [Euclidean space](../../../../Analysis/Real%20Analysis/The%20Topology%20of%20Euclidean%20Space.md) $\mathbb{R}^n$ is completely specified by its $n$ components. However, many problems are very difficult or outright impossible to solve if we are doing calculations based on vectors' components. Hence, it is often convenient to specify each $\mathbf{p}$ in some other a way known as a **coordinate system**.

>[!DEFINITION] Definition: Coordinate System for Euclidean Space
>
>A [coordinate system](../../../Manifolds/Coordinate%20Systems/index.md) $\phi: \mathbb{R}^n \to \mathbb{R}^n$ for the [Euclidean space](../../../../Analysis/Real%20Analysis/The%20Topology%20of%20Euclidean%20Space.md) $\mathbb{R}^n$ is a [continuous](../../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Continuity%20of%20Real%20Vector%20Functions.md) [function](../../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Vector%20Fields/Real%20Vector%20Field.md) which is [bijective](../../../../Analysis/Functions/Injections,%20Surjections%20and%20Bijections.md) onto its [image](../../../../Analysis/Functions/Functions.md) and has a continuous [continuous](../../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Continuity%20of%20Real%20Vector%20Functions.md) [inverse](../../../../Analysis/Functions/Injections,%20Surjections%20and%20Bijections.md). The [component functions](../../../../Analysis/Real%20Analysis/Functions%20of%20the%20Real%20Numbers.md) of $\phi$ are $n$ [functions](../../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Scalar%20Fields/Real%20Scalar%20Field.md) $\phi^1, \dotsc, \phi^n: \mathbb{R}^n \to \mathbb{R}$. These functions are known as **coordinates** ***on*** $\mathbb{R}^n$. Given a specific $\mathbf{p} \in \mathbb{R}^n$, the value $p^i = \phi^i (\mathbf{p})$ is known as the $i$-th **coordinate** ***of*** $\mathbf{p}$.
>
>>[!NOTATION]
>>
>>Coordinates are usually denotes using superscripts instead of subscripts: $\phi^1, \dotsc, \phi^n$ and $p^1, \dotsc, p^n$ instead of $\phi_1, \dotsc, \phi_n$ and $p_1, \dotsc, p_n$.
>>
>

>[!INTUITION]
>
>The requirements in the definition of a coordinate system mean that each [vector](../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Vector.md) is identified by a unique combination of coordinates but also ensure that [vector](../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Vector.md) which are closed to each other have coordinates which are close to each other. Essentially, if $\mathbf{p} \ne \mathbf{p}'$, then at least one of $\phi^1(\mathbf{p}), \dotsc, \phi^n(\mathbf{p})$ must be different from $\phi^1(\mathbf{p}'), \dotsc, \phi^n(\mathbf{p}')$. Furthermore, if the [Euclidean distance](../../../../Algebra/Linear%20Algebra/Vector%20Spaces/Inner%20Product%20Spaces/Euclidean%20Distance.md) between $\mathbf{p}$ and $\mathbf{p}'$ is small, then the differences between $\phi^1(\mathbf{p}), \dotsc, \phi^n(\mathbf{p})$ and $\phi^1(\mathbf{p}'), \dotsc, \phi^n(\mathbf{p}')$, respectively, should be small.
>

## Coordinate Tuples

Although $\phi$ takes in a [vector](../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Vector.md) $\mathbf{p} \in \mathbb{R}^n$ and outputs the [vector](../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Vector.md) $\begin{bmatrix} \phi^1(\mathbf{p}) & \cdots & \phi^n(\mathbf{p}) \end{bmatrix}^{\mathsf{T}}$, we rarely treat its output as such. It is much more common to treat its output as the $n$-[tuple](../../../../Set%20Theory/Tuples.md) $(\phi^1 (\mathbf{p}), \dotsc, \phi^n (\mathbf{p}))$. We just define $\phi$ as a [vector function](../../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Vector%20Fields/Real%20Vector%20Field.md) only because it makes formulating the necessary requirements easier. This is, nevertheless, a very important point to make as treating the coordinates a vector falsely lead one to believe that the coordinates of $\mathbf{p} + \mathbf{p}$ are just $\phi^1(\mathbf{p}) + \phi^1 (\mathbf{p}')$, $\dotsc$, $\phi^n (\mathbf{p}) + \phi^n (\mathbf{p}')$. Whilst this might be true in certain coordinate system, it is the exception rather than the rule.

