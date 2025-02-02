>[!TIP] Tip: Partial Derivatives in Cartesian Coordinates
>
>Let $f: \mathcal{D} \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) on an [open subset](../../../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Open%20Sets%20in%20Euclidean%20Space.md) $\mathcal{D} \subseteq \mathbb{R}^n$.
>
>The [partial derivative](Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md) of $f$ at $\mathbf{a}$ with respect to the $i$-th [Cartesian coordinate](../../../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Coordinate%20Systems/Cartesian%20Coordinate%20System.md) $x^i$ coincides with the [directional derivative](Directional%20Derivatives%20of%20Real%20Scalar%20Fields.md) of $f$ there along the $i$-th [standard basis vector](../../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Standard%20Basis%20of%20the%20Real%20Vector%20Space.md) $\mathbf{e}_i$:
>
>$$
>\frac{\partial f}{\partial x^i}(\mathbf{a}) = \lim_{h\to 0} \frac{f(\mathbf{a} + h \cdot \mathbf{e}_i) - f(\mathbf{a})}{h}
>$$
>
>>[!NOTATION]-
>>
>>Cartesian coordinates in partial derivatives can be denoted using either subscripts and superscripts, i.e.
>>
>>$$
>>\frac{\partial}{\partial x^i} (\mathbf{a}) \qquad  \frac{\partial f}{\partial x^i} f(\mathbf{a}) \qquad \left. \frac{\partial f}{\partial x^i}\right|_{\mathbf{a}} \qquad f_{x^i}(\mathbf{a})
>>$$
>>
>>$$
>>\frac{\partial}{\partial x_i} (\mathbf{a}) \qquad  \frac{\partial f}{\partial x_i} f(\mathbf{a}) \qquad \left. \frac{\partial f}{\partial x_i}\right|_{\mathbf{a}} \qquad f_{x_i}(\mathbf{a})
>>$$
>>
>>are equivalent. Writing the coordinates using subscripts is cleaner when partial derivatives of higher orders are involved.
>>
>