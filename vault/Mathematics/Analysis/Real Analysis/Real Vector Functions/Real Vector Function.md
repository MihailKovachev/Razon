>[!DEFINITION] Definition: Vector Function
>
>A **vector function** $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ is a [real vector-valued function](../Real%20Vector-Valued%20Function.md) whose [domain](../../Functions/index.md) $\mathcal{D}$ is a [subset](../../../Set%20Theory/index.md) of a [real vector space](../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Structure%20of%20the%20Real%20Vector%20Space.md) $\mathbb{R}^m$.
>
>>[!NOTATION]- Notation: Multivariate Notation and Coordinate Representations
>>
>>Strictly speaking, a [real vector function](Real%20Vector%20Function.md) $f$ takes a [vector](../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Vector.md) $\mathbf{p} \in \mathcal{D} \subseteq \mathbb{R}^m$ and outputs another vector $f(\mathbf{p}) \in \mathbb{R}^n$. However, since vectors live as a [points](../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Points%20vs%20Vectors/index.md) in [Euclidean space](../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/index.md), they can be uniquely represented by [coordinates](../../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Coordinate%20Systems/index.md).
>>
>>Although the action of $f$ is independent of the choice of [coordinate systems](../../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Coordinate%20Systems/index.md) for $\mathbb{R}^m$ and $\mathbb{R}^n$ ($\mathbf{p}$ and $f(\mathbf{p})$ are the same vectors, regardless of how we choose to represent them), many definitions involving $f$, such as differentiability and integrability, *do* depend on the choice of a [coordinate system](../../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Coordinate%20Systems/index.md) for the input space $\mathbb{R}^m$. Indeed, it would be more appropriate to formulate such definitions about the [coordinate representations](../../Analysis%20on%20Manifolds/Coordinate%20Representation%20of%20Functions.md) of $f$ in the chosen coordinate systems. However, this formality gets very cumbersome very quickly.
>>
>>Hence, if the coordinates of $\mathbf{p}$ in a given coordinate system $\phi$ are $p^1, \dotsc, p^n$, then instead of writing ${}_{(\mathbb{R}^m, \phi)}f(p^1,\dotsc,p^m)$ for the coordinate representation of $f$, we can just write $f(p^1,\dotsc,p^m)$, as long as it is clear which coordinate system we are using. If there is no particular coordinate system specified, then we usually assume that those are [Cartesian coordinates](../../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Coordinate%20Systems/Cartesian%20Coordinate%20System.md).
>>
>>This is why vector functions are often called **multivariate functions**.
>>
>
>>[!NOTE] Note: Component Functions
>>
>>The [component functions](../Real%20Vector-Valued%20Function.md) of $f$ are [real scalar fields](Scalar%20Fields/Real%20Scalar%20Field.md).
>>
>

