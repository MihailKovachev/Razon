>[!TIP] Tip: Differentiability of Real Scalar Fields
>
>Let $f: \mathcal{D} \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) on an [open subset](../../../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Open%20Sets%20in%20Euclidean%20Space.md) $\mathcal{D} \subseteq \mathbb{R}^n$ and let $\mathbf{a} = \begin{bmatrix}a_1 & \cdots & a_n\end{bmatrix}^\mathsf{T} \in \mathcal{D}$.
>
>Then $f$ is [differentiable](../../Real%20Vector%20Functions/Differentiation/Differentiability%20of%20Real%20Vector%20Functions.md) at $\mathbf{a}$ if and only if it is [partially differentiable](Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md) there and the following [limit](../Limits%20of%20Real%20Scalar%20Fields.md) is zero.
>
>$$
>\lim_{\mathbf{x} \to \mathbf{a}} \frac{f(\mathbf{x}) - [f(\mathbf{a}) + \nabla f(\mathbf{a}) \cdot (\mathbf{x} - \mathbf{a})]}{||\mathbf{x} - \mathbf{a}||} = 0,
>$$
>
>where $\nabla f(\mathbf{a}) \cdot (\mathbf{x} - \mathbf{a})$ is the [dot product](../../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Dot%20Product.md) between the [gradient](Gradient.md) of $f$ at $\mathbf{a}$ and $(\mathbf{x} - \mathbf{a})$.
>
>>[!PROOF]-
>>
>>TODO
>>
>