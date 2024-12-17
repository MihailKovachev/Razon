>[!THEOREM] Theorem: Chain Rule for Scalar Fields
>
>Let $f: D \subseteq \mathbb{R}^n \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) and let $\mathbf{r}: [a;b] \to D$ be a [curve parameterisation](../../Curve%20Parameterisations/Curve%20Parameterisation.md). 
>
>If $\mathbf{r}$ is [differentiable](../../Curve%20Parameterisations/Differentiation/Differentiability%20of%20Curve%20Parameterisations.md) and $f$ is [partially differentiable](Partial%20Derivatives%20of%20Real%20Scalar%20Fields.md), then the [derivative](../../../Univariate%20Real%20Analysis/Differentiation/Differentiability%20of%20Real%20Functions.md) of the [composition](../../../../Functions/Composition.md) $f \circ \mathbf{r}$ is the [dot product](../../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Dot%20Product.md) of $f$'s [gradient](Gradient.md) and $\mathbf{r}$'s derivative.
>
>$$\frac{\mathrm{d}}{\mathrm{d}t} f(\mathbf{r}(t)) = \nabla f(\mathbf{r}(t))\cdot \mathbf{r}'(t)$$
>
>>[!NOTE]
>>
>>The composition $f\circ\mathbf{r}$ is a [real function](../../../Univariate%20Real%20Analysis/Real%20Functions/Real%20Function.md).
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>
>^chainrule
>

>[!THEOREM] Theorem: Product Rule
>
>Let $f, g: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be [real scalar fields](../Real%20Scalar%20Field.md).
>
>If $f$ and $g$ are [differentiable](../../../Univariate%20Real%20Analysis/Differentiation/Differentiability%20of%20Real%20Functions.md) at $\mathbf{a} \in \mathcal{D}$, then the product $fg: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ is also [differentiable](../../../Univariate%20Real%20Analysis/Differentiation/Differentiability%20of%20Real%20Functions.md) at $\mathbf{a} \in \mathcal{D}$ with
>
>$$
>\mathop{\mathrm{d}(fg)_{\mathcal{a}}} = g(\mathcal{a})\mathop{\mathrm{d}f_{\mathcal{a}}} + f(\mathcal{a})\mathop{\mathrm{d}g_{\mathcal{a}}}
>$$
>
>>[!IMPORTANT]
>>
>>You should remember that $\mathrm{d}(fg)_{\mathcal{a}}$ is a *function* and so are $\mathop{\mathrm{d}f_{\mathcal{a}}}$ and $\mathop{\mathrm{d}g_{\mathcal{a}}}$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Quotient Rule
>
>Let $f, g: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ be [real scalar fields](../Real%20Scalar%20Field.md).
>
>If $f$ and $g$ are [differentiable](../../../Univariate%20Real%20Analysis/Differentiation/Differentiability%20of%20Real%20Functions.md) at $\mathbf{a} \in \mathcal{D}$ and $g(\mathcal{a}) \ne 0$, then the quotient $f/g: \mathcal{D} \subseteq \mathbb{R}^n \to \mathbb{R}$ is also [differentiable](../../../Univariate%20Real%20Analysis/Differentiation/Differentiability%20of%20Real%20Functions.md) at $\mathbf{a} \in \mathcal{D}$ with
>
>$$
>\mathop{\mathrm{d}(f/g)_{\mathcal{a}}} = \frac{g(\mathcal{a})\mathop{\mathrm{d}f_{\mathcal{a}}} - f(\mathcal{a})\mathop{\mathrm{d}g_{\mathcal{a}}}}{g(\mathcal{a})^2}
>$$
>
>>[!IMPORTANT]
>>
>>You should remember that $\mathrm{d}(f/g)_{\mathcal{a}}$ is a *function* and so are $\mathop{\mathrm{d}f_{\mathcal{a}}}$ and $\mathop{\mathrm{d}g_{\mathcal{a}}}$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>