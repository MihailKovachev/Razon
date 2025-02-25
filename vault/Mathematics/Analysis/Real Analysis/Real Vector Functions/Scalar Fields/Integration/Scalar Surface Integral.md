>[!DEFINITION] Definition: Scalar Surface Integral
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^3 \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) and let $S: \mathcal{D}_S \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ be a [differentiable](../../../Real%20Vector%20Functions/Differentiation/Differentiability%20of%20Real%20Vector%20Functions.md) [parametric surface](../../../Real%20Vector%20Functions/Parametric%20Surfaces/Parametric%20Surface.md) whose [image](../../../../Functions/index.md) $S(\mathcal{D}_S)$ is a [subset](../../../../../Set%20Theory/Sets.md) of $\mathcal{D}_f$.
>
>The **(scalar) line integral** of $f$ over $S$ is the [double integral](Double%20Integral%20of%20a%20Real%20Scalar%20Field.md)
>
>$$
>\iint_{\mathcal{D}_S} f(S(x,y)) \, ||\mathbf{N}(x,y)|| \mathop{\mathrm{d}\mathcal{D}_S},
>$$
>
>where $\mathbf{N}$ is the [normal vector](../../../Real%20Vector%20Functions/Parametric%20Surfaces/Surface%20Normal%20Vector.md) of $S$.
>
>>[!NOTATION]-
>>
>>$$
>>\iint_S f \qquad \iint_S f \mathop{\mathrm{d}S}
>>$$
>>
>>If $S(\mathcal{D}_S)$ is a [closed surface](../../../../../Geometry/Euclidean%20Geometry/Surfaces/Closed%20Surfaces.md), then a circle can be put through the two integral signs.
>>
>

>[!THEOREM] Theorem: Surface Integrals of Scalar Fields
>
>Let $f: \mathcal{D} \subseteq \mathbb{R}^3 \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) and let $\phi: \mathcal{D}_{\phi} \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ and $\psi: \mathcal{D}_{\psi} \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ be [differentiable](../../../Real%20Vector%20Functions/Differentiation/Differentiability%20of%20Real%20Vector%20Functions.md) [parametric surfaces](../../../Real%20Vector%20Functions/Parametric%20Surfaces/Parametric%20Surface.md) whose [images](../../../../Functions/index.md) are [subsets](../../../../../Set%20Theory/Sets.md) of $\mathcal{D}$.
>
>If $\phi$ and $\psi$ are [smooth reparameterisations](../../../Real%20Vector%20Functions/Parametric%20Surfaces/Equivalence%20of%20Parametric%20Surfaces.md) and $f$ is [continuous](../Continuity%20of%20Real%20Scalar%20Fields.md), then the [surface integrals](Scalar%20Surface%20Integral.md) of $f$ over $\phi$ and $\psi$ are equal.
>
>$$
>\iint_{\phi} f = \iint_{\psi} f
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>