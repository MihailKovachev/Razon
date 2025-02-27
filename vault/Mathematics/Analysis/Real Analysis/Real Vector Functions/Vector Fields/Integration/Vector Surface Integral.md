>[!DEFINITION] Definition: Vector Surface Integral
>
>Let $\mathbf{F}: \mathcal{D}_{\mathbf{F}} \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [real vector field](../Real%20Vector%20Field.md) and let $S: \mathcal{D}_S \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ be a [differentiable](../../../Real%20Vector%20Functions/Differentiation/Differentiability%20of%20Real%20Vector%20Functions.md) [parametric surface](../../../Real%20Vector%20Functions/Parametric%20Surfaces/Parametric%20Surface.md) whose [image](../../../../Functions/Functions.md) $S(\mathcal{D}_S)$ is a [subset](../../../../../Set%20Theory/Sets.md) of $\mathcal{D}_{\mathbf{F}}$.
>
>The **(vector) surface integral** of $f$ over $S$ is the [double integral](../../../Real%20Vector%20Functions/Scalar%20Fields/Integration/Double%20Integrals.md)
>
>$$
>\iint_{\mathcal{D}_S} \mathbf{F}(S(x,y)) \cdot \mathbf{N}(x,y) \mathop{\mathrm{d}\mathcal{D}_S},
>$$
>
>where $\mathbf{N}$ is the [normal vector](../../../Real%20Vector%20Functions/Parametric%20Surfaces/Surface%20Normal%20Vector.md) of $S$ and $\cdot$ denotes the [dot product](../../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Dot%20Product.md).
>
>>[!NOTATION]-
>>
>>$$
>>\iint_S \mathbf{F} \qquad \iint_S \mathbf{F} \cdot \mathrm{d}\mathbf{S}
>>$$
>>
>>If $S(\mathcal{D}_S)$ is a [closed surface](../../../../../Geometry/Euclidean%20Geometry/Surfaces/Closed%20Surfaces.md), then a circle can be put through the two integral signs.
>

>[!THEOREM] Theorem: Vector Surface Integral to Scalar Surface Integral
>
>Let $\mathbf{F}: \mathcal{D}_{\mathbf{F}} \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [real vector field](../Real%20Vector%20Field.md) and let $S: \mathcal{D}_S \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ be a [differentiable](../../../Real%20Vector%20Functions/Differentiation/Differentiability%20of%20Real%20Vector%20Functions.md) [parametric surface](../../../Real%20Vector%20Functions/Parametric%20Surfaces/Parametric%20Surface.md) whose [image](../../../../Functions/Functions.md) $S(\mathcal{D}_S)$ is a [subset](../../../../../Set%20Theory/Sets.md) of $\mathcal{D}_{\mathbf{F}}$.
>
>The [vector surface integral](Vector%20Surface%20Integral.md) of $\mathbf{F}$ over $S$ is equal to the [scalar surface integral](../../../Real%20Vector%20Functions/Scalar%20Fields/Integration/Scalar%20Surface%20Integral.md) of the [dot product](../../../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Dot%20Product.md) between $\mathbf{F}$ and the [unit surface normal](../../../Real%20Vector%20Functions/Parametric%20Surfaces/Surface%20Normal%20Vector.md) of $S$.
>
>$$
>\iint_S \mathbf{F} \cdot \mathop{\mathrm{d}\mathbf{S}} = \iint_S \mathbf{F} \cdot \mathbf{n} \mathop{\mathrm{d}S}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Vector Surface Integrals of Reparameterisations
>
>Let $\mathbf{F}: \mathcal{D}_{\mathbf{F}} \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ be a [real vector field](../Real%20Vector%20Field.md) and let $\phi: \mathcal{D}_{\phi} \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ and $\psi: \mathcal{D}_{\psi} \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ be [equivalent](../../../Real%20Vector%20Functions/Parametric%20Surfaces/Equivalence%20of%20Parametric%20Surfaces.md) [parametric surfaces](../../../Real%20Vector%20Functions/Parametric%20Surfaces/Parametric%20Surface.md) whose [image](../../../../Functions/Functions.md) is a [subset](../../../../../Set%20Theory/Sets.md) of $\mathcal{D}_{\mathbf{F}}$.
>
>If $\phi$ and $\psi$ have the [same orientation](../../../Real%20Vector%20Functions/Parametric%20Surfaces/Equivalence%20of%20Parametric%20Surfaces.md), then the [surface integrals](Vector%20Surface%20Integral.md) of $\mathbf{F}$ over $\phi$ and $\psi$ are equal:
>
>$$
>\iint_{\phi} \mathbf{F} = \iint_{\psi} \mathbf{F}
>$$
>
>If $\phi$ and $\psi$ have [opposite orientations](../../../Real%20Vector%20Functions/Parametric%20Surfaces/Equivalence%20of%20Parametric%20Surfaces.md), then the [surface integrals](Vector%20Surface%20Integral.md) of $\mathbf{F}$ over $\phi$ and $\psi$ are equal in magnitude but differ in algebraic sign:
>
>$$
>\iint_{\phi} \mathbf{F} = -\iint_{\psi} \mathbf{F}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>


