---
tags:
    - real-analysis
    - vector-analysis
    - mathematical-analysis
    - analysis
---

# Real Vector Functions

>[!DEFINITION] Definition: Real Vector-Valued Function
>
>A **real vector-valued function** $f: \mathcal{D} \to \mathbb{R}^n$ is a [function](../../Functions/Functions.md) from an arbitrary [set](../../../Set%20Theory/Sets.md) $\mathcal{D}$ to the [Euclidean space](../Euclidean%20Space/Euclidean%20Space.md) $\mathbb{R}^n$.
>
>>[!NOTE] Note: Component Functions
>>
>>Every **real vector-valued function** $f: \mathcal{D} \to \mathbb{R}^n$ can be described by $n$ [real-valued functions](../Real%20Functions/Real%20Functions.md) $f_1, \dotsc, f_n: \mathcal{D} \to \mathbb{R}$, where $f_i(x)$ gives the $i$-th component of the [vector](../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $f(x)$:
>>
>>$$
>>f(x) = \begin{bmatrix}f_1(x) \\ \vdots \\ f_n(x) \end{bmatrix}
>>$$
>>
>>Hence, $f_1, \dotsc, f_n$ are called the **component functions** of $f$.
>>
>

>[!DEFINITION] Definition: Vector Function
>
>A **real vector function** $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ is a [real vector-valued function](./Real%20Vector%20Functions.md) whose [domain](../../Functions/Functions.md) a [subset](../../../Set%20Theory/Sets.md) $\mathcal{D}$ is a [subset](../../../Set%20Theory/Sets.md#Subsets) of a [Euclidean space](../Euclidean%20Space/Euclidean%20Space.md) $\mathbb{R}^m$.
>
>>[!NOTE] Note: Component Functions
>>
>>Every **real vector function** $f: \mathcal{D} \to \mathbb{R}^n$ can be described by $n$ [real scalar fields](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f_1, \dotsc, f_n: \mathcal{D} \to \mathbb{R}$ such that for each [vector](../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $\mathbb{x} \in \mathcal{D}$, the [function](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) $f_k$ gives the the $k$-th component of $f(\mathbf{x})$, which is a [vector](../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) in $\mathbb{R}^n$. 
>>
>>$$
>>f(\mathbf{x}) = \begin{bmatrix}f_1(\mathbf{x}) \\ \vdots \\ f_n(\mathbf{x}) \end{bmatrix}
>>$$
>>
>>Hence, $f_1, \dotsc, f_n$ are called the **component functions** of $f$.
>>
>
>
>>[!NOTATION] Notation: Multivariate Notation and Coordinate Representations
>>
>>Strictly speaking, a [real vector function](./Real%20Vector%20Functions.md) $f$ takes a [real vector](../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $\mathbf{p} \in \mathcal{D} \subseteq \mathbb{R}^m$ and outputs another [real vector](../../../Algebra/Linear%20Algebra/Real%20Vectors/Real%20Vectors.md) $f(\mathbf{p}) \in \mathbb{R}^n$. However, since [real vectors](../../Algebra/Linear%20Algebra/Matrices/Real%20Vectors.md) live in a [Euclidean space](../Euclidean%20Space/Euclidean%20Space.md), they can be uniquely represented by [coordinates](../../../Geometry/Manifolds/Coordinate%20Systems/Charts.md).
>>
>>If $(p^1, \dotsc, p^m)$ are the [coordinates](../../../Geometry/Manifolds/Coordinate%20Systems/Charts.md) of $\mathbf{p}$ with respect to some chosen [coordinate system](../../../Geometry/Manifolds/Coordinate%20Systems/Charts.md), then we can write $f(p^1, \dotsc, p^m)$ instead of $f(\mathbf{p})$ as long as it is which [coordinate system](../../../Geometry/Manifolds/Coordinate%20Systems/Charts.md) we are working in. Unless otherwise indicated, always assume [Cartesian coordinates](../Euclidean%20Space/Cartesian%20Coordinate%20System.md)
>>
>>This is why vector functions are often called **multivariate functions**.
>>
>