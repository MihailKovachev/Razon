# Lagrange Multipliers

Lagrange multipliers allow us to determine if a [function](../Real%20Scalar%20Field.md) subject to some [constraints](Constraints.md) has [local extrema](Local%20Extrema.md).

>[!THEOREM] Theorem: Lagrange Multipliers
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [continuously partially differentiable](../Differentiation/Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md) [real scalar field](../Real%20Scalar%20Field.md) and let
>
>$$
>\begin{align*}
>
>g_1(\mathbf{x}) &= c_1 \\
>
>&\vdots \\
>
>g_k(\mathbf{x}) &= c_k
>
>\end{align*}
>$$
>
>be some [constraints](Constraints.md#^equality-constraint), where $g_1, \dotsc, g_k: \mathcal{D} \to \mathbb{R}$ are also [continuously partially differentiable](../Differentiation/Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md), and let $S \{\mathbf{x} \mid g_1(\mathbf{x}) = c_1 \text{ and } \cdots \text{ and } g_k(\mathbf{x}) = c_k\}$.
>
>If $f\big|_S$ has a [local extremum](../../../Univariate%20Real%20Analysis/Real%20Functions/Extrema/Local%20Extrema.md) at $\mathbf{a}$ and the [gradients](../Differentiation/Gradient.md) $\nabla g_1(\mathbf{a}), \dotsc, \nabla g_k(\mathbf{a})$ are [linearly independent](../../../../../Algebra/Linear%20Algebra/Vector%20Spaces/Linear%20Independence.md), then $\nabla f(\mathbf{a})$ is a [linear combination](../../../../../Algebra/Linear%20Algebra/Vector%20Spaces/Linear%20Combination.md) of $\nabla g_1(\mathbf{a}), \dotsc, \nabla g_k(\mathbf{a})$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Lagrange Multipliers
>>
>>The coefficients $\lambda_1, \dotsc, \lambda_k$ in the representation 
>>
>>$$
>>\nabla f(\mathbf{a}) = \lambda_1 \nabla g_1(\mathbf{a}) + \cdots + \lambda_k \nabla g_k(\mathbf{a})
>>$$
>>
>>of $\nabla f(\mathbf{a})$ as a [linear combination](../../../../../Algebra/Linear%20Algebra/Vector%20Spaces/Linear%20Combination.md) of $\nabla g_1(\mathbf{a}), \dotsc, \nabla g_k(\mathbf{a})$ are known as **Lagrange multipliers**.
>>
>

>[!EXAMPLE]-
>
>TODO
>