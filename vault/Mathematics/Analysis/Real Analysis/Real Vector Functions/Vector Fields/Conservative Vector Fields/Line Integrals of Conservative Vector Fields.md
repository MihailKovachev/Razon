>[!THEOREM] Gradient Theorem (Fundamental Theorem of Analysis for Line Integrals)
>
>If $\boldsymbol{v}: D \to \mathbb{R}^n$ is the  [gradient field](Conservative%20Vector%20Field.md) of a [scalar field](../../../Real%20Vector%20Functions/Scalar%20Fields/Real%20Scalar%20Field.md) $f: D\to\mathbb{R}$ on an [open subset](../../../../../Topology/Metric%20Spaces/index.md#^opensets) $D \subseteq \mathbb{R}^n$, then its [line integral](../Integration/Vector%20Line%20Integral.md) over a [piecewise continuously differentiable](../../../Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) [curve parameterisation](../../../Real%20Vector%20Functions/Parametric%20Curves/Parametric%20Curve.md) $\gamma: [a;b] \to D$ can be calculated as
>
>$$
>\int_\gamma \boldsymbol{v} \cdot \mathop{\mathrm{d}\boldsymbol{s}} = f(\gamma (b)) - f(\gamma (a))
>$$
>
>>[!PROOF]-
>>
>>By definition
>>
>>$$
>>\int_\gamma \boldsymbol{v} \cdot \mathop{\mathrm{d}\boldsymbol{s}} = \int_a^b \boldsymbol{v}(\gamma(t)) \cdot \gamma'(t) \mathop{\mathrm{d}t} = \int_a^b \nabla  f(\gamma(t)) \cdot \gamma'(t) \mathop{\mathrm{d}t}
>>$$
>>
>>The [chain rule for scalar fields](../../../Real%20Vector%20Functions/Scalar%20Fields/Differentiation/Differentiation%20Rules%20for%20Scalar%20Fields.md#^chainrule) tells us that the integrand is the derivative of $f(\gamma (t))$:
>>
>>$$
>>\frac{\mathrm{d}}{\mathrm{d}t} f(\gamma (t)) = \nabla  f(\gamma(t)) \cdot \gamma'(t)
>>$$
>>
>>$$
>>\int_a^b \nabla  f(\gamma(t)) \cdot \gamma'(t) \mathop{\mathrm{d}t} = \int_a^b \frac{\mathrm{d}}{\mathrm{d}t} f(\gamma (t)) \mathop{\mathrm{d}t}
>>$$
>>
>>The [fundamental theorem of real analysis](../../../Real%20Functions/Integration/The%20Fundamental%20Theorem%20of%20Real%20Analysis.md) then gives us
>>
>>$$
>>\int_a^b \frac{\mathrm{d}}{\mathrm{d}t} f(\gamma (t)) \mathop{\mathrm{d}t} = f(\gamma(t))\Big|_a^b = f(\gamma(b)) - f(\gamma(a))
>>$$
>>
>

>[!THEOREM] Theorem: Path Independence of Line Integrals of Conservative Vector Fields
>
>A [real vector field](../Real%20Vector%20Field.md) $\boldsymbol{v}: D\subseteq \mathbb{R}^n \to \mathbb{R}^n$ is [conservative](Conservative%20Vector%20Field.md) if and only if its [line integrals](../Integration/Vector%20Line%20Integral.md) over all [simple curves](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md) with [piecewise continuously differentiable](../../../Real%20Vector%20Functions/Differentiation/Partial%20Derivatives%20of%20Real%20Vector%20Functions.md) [reparameterisations](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md) $\gamma_1: [a;b] \to \mathbb{R}^n$ and $\gamma_2: [a;b] \to \mathbb{R}^n$ (i.e. $\gamma_1(a) = \gamma_2(a)$ and $\gamma_1(b) = \gamma_2(b)$) are equal.
>
>$$
>\int_{\gamma_1} \boldsymbol{v}\cdot \mathop{\mathrm{d}\boldsymbol{s}} = \int_{\gamma_2} \boldsymbol{v}\cdot \mathop{\mathrm{d}\boldsymbol{s}}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Line Integrals of Conservative Vector Fields over Closed Curves
>
>A [continuous](../../../Real%20Vector%20Functions/Continuity%20of%20Real%20Vector%20Functions.md) [vector field](../Real%20Vector%20Field.md) $\boldsymbol{v}: D\subseteq \mathbb{R}^n \to \mathbb{R}^n$ is [conservative](Conservative%20Vector%20Field.md) if and only if its [line integral](../Integration/Vector%20Line%20Integral.md) over every [closed curve](../../../../../Geometry/Euclidean%20Geometry/Curves/Curves.md) $\mathcal{C} \subseteq D$ is always zero.
>
>$$
>\oint_\mathcal{C} \boldsymbol{v} \cdot \mathop{\mathrm{d}\boldsymbol{s}} = 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>