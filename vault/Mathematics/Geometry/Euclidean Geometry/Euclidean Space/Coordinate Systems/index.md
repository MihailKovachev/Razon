---
title: Coordinate Systems of Euclidean Space
---

# Coordinate Systems for Euclidean Space

A [coordinate system](../../../Manifolds/Coordinates/Coordinate%20System.md) for the [Euclidean space](../Euclidean%20Space.md) $\mathbb{R}^n$ is simply a way to uniquely identify each [point (vector)](../../Points%20and%20Vectors/Points%20vs%20Vectors.md) $\mathbf{p} \in \mathbb{R}^n$. More specifically, each coordinate system $\phi$ consists of $n$ [functions](../../../../Analysis/Real%20Analysis/Multivariate%20Real%20Analysis/Scalar%20Fields/Real%20Scalar%20Field.md) $\phi^1, \dotsc, \phi^n: \mathbb{R}^n \to \mathbb{R}$. These functions are known as coordinates *on* $\mathbb{R}^n$. Given a specific $\mathbf{p} \in \mathbb{R}^n$, the value $p^i = \phi^i (\mathbf{p})$ is known as the $i$-th coordinate *of* $\mathbf{p}$.

>[!NOTATION]
>
>Coordinates are usually denotes using superscripts instead of subscripts: $\phi^1, \dotsc, \phi^n$ and $p^1, \dotsc, p^n$ instead of $\phi_1, \dotsc, \phi_n$ and $p_1, \dotsc, p_n$.
>

>[!NOTE] Note: Uniqueness of Coordinates
>
>The term "unique" refers to the fact that different points in $\mathbf{R}^n$ must have different coordinates under the same coordinate system and different coordinates must always refer to different points.
>

One might ask why coordinate systems are even needed when each $\mathbf{p}$ is a [vector](../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Vector.md) and can be uniquely identified using its components. And indeed, there exists a coordinate system which just uses $\mathbf{p}$'s components as coordinates, namely the [Cartesian coordinate system](Cartesian%20Coordinate%20System.md). However, many problems are either easier to solve in other coordinate systems or are outright impossible to solve in Cartesian coordinates, but can be solved using different coordinates. Additionally, many concepts which initially appear to be coordinate-independent actually turn out to be quite dependent on the choice of coordinate system - we were just implicitly working using Cartesian coordinates.