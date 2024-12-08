>[!DEFINITION] Definition: Directional Derivative of a Real Scalar Field
>
>Let $f: D \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md).
>
>The **directional derivative** of $f$ at $\vec{x} \in D$ along the [unit vector](../../../../../Algebra/Linear%20Algebra/Vector%20Spaces/Normed%20Vector%20Spaces/Unit%20Vector.md) $\hat{r}$ is the [limit](../../../Univariate%20Real%20Analysis/Real%20Functions/Limits%20of%20Functions/Limit%20of%20a%20Function.md)
>
>$$\lim_{h\to 0}\frac{f(\vec{x}+h\cdot \hat{r})-f(\vec{x})}{h},$$
>
>if it exists.
>
>>[!NOTATION]-
>>
>>$$
>>\frac{\partial f}{\partial \hat{r}}(\vec{x}) \qquad \partial_{\hat{r}}f(\vec{x}) \qquad f_{\hat{r}}(\vec{x})
>>$$
>>
>

>[!THEOREM] Theorem: Directional Derivative in an Arbitrary Direction
>
>Let $f: D \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md). 
>
>If $f$ is [continuously partially differentiable](Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md), then its [directional derivatives](Directional%20Derivatives%20of%20Real%20Scalar%20Fields.md) along an arbitrary [unit vector](../../../../../Algebra/Linear%20Algebra/Vector%20Spaces/Normed%20Vector%20Spaces/Unit%20Vector.md) $\hat{r}$ is the [dot product](../../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Dot%20Product.md) of its [gradient](Gradient.md) with $\hat{r}$:
>
>$$
>\partial_{\hat{r}} f = \langle \nabla f, \hat{r}\rangle
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>