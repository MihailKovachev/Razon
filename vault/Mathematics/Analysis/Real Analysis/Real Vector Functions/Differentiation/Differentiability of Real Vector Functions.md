>[!DEFINITION] Definition: Differentiability of Real Vector Functions
>
>Let $f: \mathcal{D} \to \mathbb{R}^n$ be a [real vector function](../Real%20Vector%20Function.md) on an [open set](../../The%20Topology%20of%20Euclidean%20Space.md) $\mathcal{D} \subseteq \mathbb{R}^m$ and let $\mathbf{a}$ be an [accumulation point](../../../../Topology/Interior,%20Boundary,%20Exterior/Accumulation%20Point.md) of $\mathcal{D}$.
>
>We say that $f$ is **(totally) differentiable at** $\mathbf{a}$ iff there exists some [linear transformation](../../../../../Algebra/Linear%20Algebra/Linear%20Transformations/Linear%20Transformation.md) $L_a: \mathcal{D} \to \mathbb{R}^n$ (which usually depends on $\mathbf{a}$) such that the following [limit](../Scalar%20Fields/Limits%20of%20Real%20Scalar%20Fields.md) is zero.
>
>$$
>\lim_{\mathbf{x} \to \mathbf{a}} \frac{||f(\mathbf{x}) - f(\mathbf{a}) - L_a(\mathbf{x} - \mathbf{a})||}{||\mathbf{x} - \mathbf{a}||} = 0
>$$
>
>In this case, the transformation $L_a$ is known as the **(total) derivative** or **(total) differential** of $f$ at $\mathbf{a}$.
>
>If $f$ is [differentiable](Differentiability%20of%20Real%20Vector%20Functions.md) at every $\mathbf{a}$ in some $S \subseteq \mathbb{R}^m$, then we say that $f$ is **(totally) differentiable on** $S$. If $S = \mathcal{D}$, we can also just say that $f$ is **(totally) differentiable**. 
>
>>[!NOTATION]-
>>
>>We usually denote $L_{\mathbf{a}}$ as $\mathrm{d}f_{\mathbf{a}}$. If it is clear what $\mathbf{a}$ is, then we can also drop it and write just $\mathrm{d}f$.
>>
>
>>[!THEOREM] Theorem: Uniqueness of the Derivative
>>
>>If $f$ is [differentiable](Differentiability%20of%20Real%20Vector%20Functions.md) at $\mathbf{a}$, then its [derivative](Differentiability%20of%20Real%20Vector%20Functions.md) $\mathrm{d}f_{\mathbf{a}}$ is unique.
>>
>>>[!PROOF]-
>>>
>>>
>>>TODO
>>
>

>[!THEOREM] Theorem: Differentiability via Component Functions
>
>A [real vector function](../Real%20Vector%20Function.md) $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ is [differentiable](Differentiability%20of%20Real%20Vector%20Functions.md) at $\mathbf{a} \in \mathcal{D}$ if and only if its [component functions](../Real%20Vector%20Function.md) are [differentiable](../Scalar%20Fields/Differentiation/Differentiability%20of%20Real%20Scalar%20Fields.md) there.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Total Derivative and the Jacobian
>
>Let $f: \mathcal{D} \to \mathbb{R}^n$ be a [real vector function](../Real%20Vector%20Function.md) on an [open subset](../../The%20Topology%20of%20Euclidean%20Space.md) $\mathcal{D} \subseteq \mathbb{R}^m$ and let $\mathbf{a}$ be an [accumulation point](../../../../Topology/Interior,%20Boundary,%20Exterior/Accumulation%20Point.md) of $\mathcal{D}$.
>
>If $f$ is [differentiable](Differentiability%20of%20Real%20Vector%20Functions.md) at $\mathbf{a}$, then it is [partially differentiable](Partial%20Derivatives%20of%20Real%20Vector%20Functions.md) there with respect to [Cartesian coordinates](../../../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Coordinate%20Systems/Cartesian%20Coordinate%20System.md) and the [matrix representation](../../../../../Algebra/Linear%20Algebra/Linear%20Transformations/Matrix%20Representations%20of%20Linear%20Transformations.md) of its [derivative](Differentiability%20of%20Real%20Vector%20Functions.md) $\mathrm{d}f_{\mathbf{a}}$ (with respect to the [standard bases](../../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Standard%20Basis.md) of $\mathbb{R}^m$ and $\mathbb{R}^n$) is the [Jacobian matrix](Jacobian%20Matrix.md) $Df(\mathbf{a})$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuous Differentiability
>
>Let $f: \mathcal{D} \to \mathbb{R}^n$ be a [real vector function](../Real%20Vector%20Function.md) on an [open subset](../../The%20Topology%20of%20Euclidean%20Space.md) $\mathcal{D} \subseteq \mathbb{R}^m$ and let $\mathbf{a}$ be an [accumulation point](../../../../Topology/Interior,%20Boundary,%20Exterior/Accumulation%20Point.md) of $\mathbf{a}$.
>
>If there exists an [open](../../The%20Topology%20of%20Euclidean%20Space.md) [neighbourhood](../../../../Topology/Topological%20Spaces/Neighborhoods.md) $N$ of $\mathbf{a}$ on which the [restriction](../../../Functions/Restriction.md) $f\big|_{N}$ is [continuously partially differentiable](Partial%20Derivatives%20of%20Real%20Vector%20Functions.md) in [Cartesian coordinates](../../../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Coordinate%20Systems/Cartesian%20Coordinate%20System.md), then $f$ is [totally differentiable](Differentiability%20of%20Real%20Vector%20Functions.md) at $\mathbf{a}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Continuous Differentiability
>>
>>In this case, we say that $f$ is **continuously differentiable** at $\mathbf{a}$.
>>
>