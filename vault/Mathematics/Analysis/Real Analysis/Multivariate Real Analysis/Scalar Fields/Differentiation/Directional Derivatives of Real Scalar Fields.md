>[!DEFINITION] Definition: Directional Derivative of a Real Scalar Field
>
>Let $f: \mathcal{D} \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) on an [open subset](../../../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Open%20Sets%20in%20Euclidean%20Space.md) $\mathcal{D} \subseteq \mathbb{R}^n$.
>
>The **directional derivative** of $f$ at $\mathbf{x}_0 \in \mathcal{D}$ along the [unit vector](../../../../../Algebra/Linear%20Algebra/Vector%20Spaces/Normed%20Vector%20Spaces/Unit%20Vector.md) $\mathbf{\hat{r}}$ is the [limit](../../../Univariate%20Real%20Analysis/Real%20Functions/Limits%20of%20Functions/Limit%20of%20a%20Real%20Function.md)
>
>$$
>\lim_{h\to 0}\frac{f(\mathbf{x}_0 + h \cdot \mathbf{\hat{r}} ) - f(\mathbf{x}_0)}{h}
>$$
>
>(if it exists).
>
>>[!NOTATION]-
>>
>>$$
>>\frac{\partial f}{\partial \mathbf{\hat{r}}}(\mathbf{x}_0) \qquad \partial_{\mathbf{\hat{r}}}f(\mathbf{x}_0) \qquad f_{\mathbf{\hat{r}}}(\mathbf{x}_0) \qquad D_{\mathbf{\hat{r}}} f(\mathbf{x}_0)
>>$$
>>
>

>[!THEOREM] Theorem: Directional Derivative in an Arbitrary Direction
>
>Let $f: \mathcal{D} \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) on an [open subset](../../../../../Geometry/Euclidean%20Geometry/Euclidean%20Space/Open%20Sets%20in%20Euclidean%20Space.md) $\mathcal{D} \subseteq \mathbb{R}^n$. 
>
>If $f$ is [differentiable](Differentiability%20of%20Real%20Scalar%20Fields.md) at $\mathbf{a} \in \mathcal{D}$, then it [directional derivative](Directional%20Derivatives%20of%20Real%20Scalar%20Fields.md) at $\mathbf{a}$ exists along every [unit vector](../../../../../Algebra/Linear%20Algebra/Vector%20Spaces/Normed%20Vector%20Spaces/Unit%20Vector.md) $\mathbf{\hat{r}}$ and is the [dot product](../../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Dot%20Product.md) of $f$'s [gradient](Gradient.md) with $\mathbf{\hat{r}}$:
>
>$$
>\partial_{\mathbf{\hat{r}}}(\mathbf{a}) f = \nabla f(\mathbf{a}) \cdot \mathbf{\hat{r}}(\mathbf{a})
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!TIP]
>>
>>This theorem directly implies that the greatest directional derivative at $\mathbf{a}$ is $|| \nabla f(\mathbf{a}) ||$ and is in the direction of $\nabla f(\mathbf{a})$. Conversely, the smallest directional derivative at $\mathbf{a}$ is $- || \nabla f(\mathbf{a}) ||$ and is in the direction of $-\nabla f(\mathbf{a})$.
>>
>