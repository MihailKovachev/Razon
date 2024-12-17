>[!DEFINITION] Definition: Hessian Matrix
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [twice partially differentiable](Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md) [real scalar field](../Real%20Scalar%20Field.md).
>
>The **Hessian matrix** of $f$ is the $n \times n$-[matrix](../../../../../Algebra/Linear%20Algebra/Matrices/Square%20Matrices/Square%20Matrix.md) $H_f$ whose columns are the [gradients](Gradient.md) of $f$'s first order [partial derivatives](Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md):
>
>$$
>H_f(\mathbf{x}) \overset{\text{def}}{=} \begin{bmatrix}\vert & \vert & \vert \\ \nabla(\partial_1 f) & \cdots & \nabla(\partial_n f) \\ \vert & \vert & \vert \end{bmatrix} = \begin{bmatrix}\partial_1 \partial_1 f & \cdots & \partial_1\partial_n f \\ \vdots & \ddots & \vdots \\ \partial_n\partial_1 f & \cdots & \partial_n\partial_n f\end{bmatrix}
>$$
>
>>[!NOTATION]-
>>
>>The [Hessian matrix](Hessian%20Matrix.md) $H_f$ is different for different $\mathbf{x} \in \mathcal{D}$, since the [partial derivatives](Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md) of $f$ depend on $\mathbf{x}$. The [Hessian matrix](Hessian%20Matrix.md) at a given $\mathbf{x}_0$ is thus denoted as $H_f(\mathbf{x}_0)$ to make this dependency apparent.
>>
>

>[!THEOREM] Theorem: Symmetry of the Hessian Matrix
>
>Let $f: D \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [twice partially differentiable](Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md) [real scalar field](../Real%20Scalar%20Field.md).
>
>If all [second partial derivatives](Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md) of $f$ are also [continuous](../Continuity%20of%20Real%20Scalar%20Fields.md), then the [Hessian matrix](Hessian%20Matrix.md) of $f$ is [symmetric](../../../../../Algebra/Linear%20Algebra/Matrices/Square%20Matrices/Symmetric%20Matrices/Symmetric%20Matrix.md) for every $\mathbf{x} \in D$.
>
>>[!PROOF]-
>>
>>This follows directly from [Schwarz's theorem](Symmetry%20of%20Second%20Derivatives.md).
>>
>