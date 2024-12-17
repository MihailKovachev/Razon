>[!DEFINITION] Definition: Differentiability of Real Vector Functions
>
>Let $f: \mathcal{D} \to \mathbb{R}^n$ be a [real vector function](../Real%20Vector%20Function.md) on an [open set](../../../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Open%20Sets%20in%20Euclidean%20Space.md) $\mathcal{D} \subseteq \mathbb{R}^m$ and let $\mathbf{a} \in \mathcal{D}$ be an [accumulation point](../../../../../Topology/Interior,%20Exterior,%20Boundary/Accumulation%20Point.md) of $\mathcal{D}$.
>
>We say that $f$ is **(totally) differentiable at** $\mathbf{a}$ iff there exists some [linear transformation](../../../../../Algebra/Linear%20Algebra/Linear%20Transformations/Linear%20Transformation.md) $L_a: \mathcal{D} \to \mathbb{R}^n$ (which usually depends on $\mathbf{a}$) such that the following [limit](../../Scalar%20Fields/Limits%20of%20Real%20Scalar%20Fields.md) is zero.
>
>$$
>\lim_{\mathbf{x} \to \mathbf{a}} \frac{||f(\mathbf{x}) - f(\mathbf{a}) - L_a(\mathbf{x} - \mathbf{a})||}{||\mathbf{x} - \mathbf{a}||} = 0
>$$
>
>In this case, the transformation $L_a$ is known as the **derivative** or **differential** of $f$ at $\mathbf{a}$.
>
>>[!NOTE]
>>
>>Sometimes, $f$ is also called **totally differentiable at** $\mathbf{a}$ and $L_a$ is called the **total derivative** or **total differential** of $f$ at $\mathbf{a}$.
>>
>

>[!THEOREM] Theorem: Differentiability via Component Functions
>
>A [real vector function](../Real%20Vector%20Function.md) $f: \mathcal{D} \subseteq \mathbb{R}^m \to \mathbb{R}^n$ is [differentiable](Differentiability%20of%20Real%20Vector%20Functions.md) at $\mathbf{a} \in \mathcal{D}$ if and only if its [component functions](../Real%20Vector%20Function.md) are [differentiable](../../Scalar%20Fields/Differentiation/Differentiability%20of%20Real%20Scalar%20Fields.md) there.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Total Derivative and the Jacobian
>
>Let $f: \mathcal{D} \to \mathbb{R}^n$ be a [real vector function](../Real%20Vector%20Function.md) on an [open subset](../../../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Open%20Sets%20in%20Euclidean%20Space.md) $\mathcal{D} \subseteq \mathbb{R}^m$ and let $\mathbf{x}_0 \in \mathcal{D}$.
>
>If there exists an [open](../../../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Open%20Sets%20in%20Euclidean%20Space.md) [neighbourhood](../../../../../Topology/Topological%20Spaces/Neighbourhoods.md) $N$ of $\mathbf{x}_0$ on which the [restriction](../../../../Functions/Restriction.md) $f\big|_{N}$ is [continuously partially differentiable](Partial%20Derivatives%20of%20Real%20Vector%20Functions.md), then $f$ is [totally differentiable](Differentiability%20of%20Real%20Vector%20Functions.md) at $\mathbf{x}_0$ and the [matrix representation](../../../../../Algebra/Linear%20Algebra/Linear%20Transformations/Matrix%20Representations%20of%20Linear%20Transformations.md) of $f$'s [derivative](Differentiability%20of%20Real%20Vector%20Functions.md) at $\mathbf{x}_0$ (with respect to the [standard bases](../../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Standard%20Basis.md) of $\mathbb{R}^m$ and $\mathbb{R}^n$) is the [Jacobian matrix](Jacobian%20Matrix.md) $Df(\mathbf{x}_0)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>