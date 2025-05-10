---
title: Functions of the Real Numbers
tags:
  - real-analysis
  - mathematics
  - real-functions
  - analysis
  - vector-analysis
---

# Real-Valued Functions

>[!DEFINITION] Definition: Real-Valued Function
>
>A **real-valued function** is a [function](../Functions/Functions.md) whose [codomain](../Functions/Functions.md) are the [real numbers](../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md).
>

>[!DEFINITION] Definition: Operations with Real-Valued Functions
>
>Let $f: \mathcal{D}_f \to \mathbb{R}$ and $g: \mathcal{D}_g \to \mathbb{R}$ be [real-valued functions](Functions%20of%20the%20Real%20Numbers.md).
>
>We define
>- the **sum** of $f$ and $g$ as $f + g: \mathcal{D}_f \cap \mathcal{D}_g \to \mathbb{R}$ with $(f+g)(x) = f(x) + g(x)$;
>- the **difference** $f - g: \mathcal{D}_f \cap \mathcal{D}_g \to \mathbb{R}$ with $(f-g)(x) = f(x) - g(x)$;
>- the **product** of $f$ and $g$ as $fg: \mathcal{D}_f \cap \mathcal{D}_g \to \mathbb{R}$ with $(fg)(x) = f(x) g(x)$;
>- the **quotient** $f/g: \mathcal{D} \to \mathbb{R}$ with $\mathcal{D} = \{x \in \mathcal{D}_f \cap \mathcal{D}_g \mid g(x) \ne 0\}$ and $(f/g)(x) = \frac{f(x)}{g(x)}$.
>

## Real Functions

>[!DEFINITION] Definition: Real Function
>
>A **real function** is a [real-valued function](Functions%20of%20the%20Real%20Numbers.md) whose [domain](../Functions/Functions.md) is a [subset](../../../Set%20Theory/Subsets.md) of the [real numbers](../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md):
>
>$$
>f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}
>$$
>

# Real Vector-Valued Functions

>[!DEFINITION] Definition: Real Vector-Valued Function
>
>A **real vector-valued function** $f: D \to \mathbb{R}^n$ is a [function](../Functions/Functions.md) from an arbitrary [set](../../Set%20Theory/Sets.md) $D$ to the [real vector space](../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Vector.md) $\mathbb{R}^n$.
>
>>[!NOTE] Note: Component Functions
>>
>>Every **real vector-valued function** $f: D \to \mathbb{R}^n$ can be described by $n$ [real-valued functions](Functions%20of%20the%20Real%20Numbers.md) $f_1, \dotsc, f_n: \mathcal{D} \to \mathbb{R}^n$, where $f_k$ is responsible for the $k$-th component of the resulting [vector](../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Vector.md):
>>
>>$$
>>f(x) = \begin{bmatrix}f_1(x) \\ \vdots \\ f_n(x) \end{bmatrix}
>>$$
>>
>>Hence, $f_1, \dotsc, f_n$ are called the **component functions** of $f$.
>>
>

## Real Vector Functions

>[!DEFINITION] Definition: Vector Function
>
>A **vector function** $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ is a [real vector-valued function](Functions%20of%20the%20Real%20Numbers.md) whose [domain](../Functions/Functions.md) $\mathcal{D}$ is a [subset](../../../Set%20Theory/Sets.md) of a [real vector space](../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Structure%20of%20the%20Real%20Vector%20Space.md) $\mathbb{R}^m$.
>
>>[!NOTATION]- Notation: Multivariate Notation and Coordinate Representations
>>
>>Strictly speaking, a [real vector function](Real%20Vector%20Function.md) $f$ takes a [vector](../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Vector.md) $\mathbf{p} \in \mathcal{D} \subseteq \mathbb{R}^m$ and outputs another vector $f(\mathbf{p}) \in \mathbb{R}^n$. However, since vectors live as a [points](../../Geometry/Euclidean%20Geometry/Euclidean%20Geometry.md) in [Euclidean space](../The%20Topology%20of%20Euclidean%20Space.md), they can be uniquely represented by [coordinates](../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Coordinate%20Systems/index.md).
>>
>>Although the action of $f$ is independent of the choice of [coordinate systems](../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Coordinate%20Systems/index.md) for $\mathbb{R}^m$ and $\mathbb{R}^n$ ($\mathbf{p}$ and $f(\mathbf{p})$ are the same vectors, regardless of how we choose to represent them), many definitions involving $f$, such as differentiability and integrability, *do* depend on the choice of a [coordinate system](../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Coordinate%20Systems/index.md) for the input space $\mathbb{R}^m$. Indeed, it would be more appropriate to formulate such definitions about the [coordinate representations](../../Analysis%20on%20Manifolds/Coordinate%20Representation%20of%20Functions.md) of $f$ in the chosen coordinate systems. However, this formality gets very cumbersome very quickly.
>>
>>Hence, if the coordinates of $\mathbf{p}$ in a given coordinate system $\phi$ are $p^1, \dotsc, p^n$, then instead of writing ${}_{(\mathbb{R}^m, \phi)}f(p^1,\dotsc,p^m)$ for the coordinate representation of $f$, we can just write $f(p^1,\dotsc,p^m)$, as long as it is clear which coordinate system we are using. If there is no particular coordinate system specified, then we usually assume that those are [Cartesian coordinates](../../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Coordinate%20Systems/Cartesian%20Coordinate%20System.md).
>>
>>This is why vector functions are often called **multivariate functions**.
>>
>
>>[!NOTE] Note: Component Functions
>>
>>The [component functions](../Functions%20of%20the%20Real%20Numbers.md) of $f$ are [real scalar fields](Scalar%20Fields/Real%20Scalar%20Field.md).
>>
>

