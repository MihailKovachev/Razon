>[!THEOREM] Theorem: Surface Integrals of Scalar Fields
>
>Let $f: D \subseteq \mathbb{R}^3 \to \mathbb{R}$ be a [real scalar field](../Real%20Scalar%20Field.md) and $\mathcal{S} \subseteq D$ be a [surface](../../../../../Geometry/Euclidean%20Geometry/Surfaces/Surface.md).
>
>If $f$ is [continuous](../Continuity%20of%20Real%20Scalar%20Fields.md), then for all [smooth surface parameterisations](../../Parametric%20Surfaces/Smoothness%20of%20Surface%20Parameterisations.md) $\phi: D_\phi \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ and $\psi: D_\psi \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ of $\mathcal{S}$ the following [double integrals](Double%20Integral%20of%20a%20Real%20Scalar%20Field.md) are equal:
>
>$$
>\iint\limits_{D_{\phi}} f(\phi(u,v)) \, \left|\left|\frac{\partial\phi}{\partial u}(u, v) \times \frac{\partial \phi}{\partial v}(u,v)\right|\right| \mathop{\mathrm{d}D_{\phi}} = \iint\limits_{D_{\psi}} f(\psi(u,v)) \, \left|\left|\frac{\partial\psi}{\partial u}(u, v) \times \frac{\partial \psi}{\partial v}(u,v)\right|\right| \mathop{\mathrm{d}D_{\psi}}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!DEFINITION] Definition: Surface Integral of a Scalar Field
>>
>>Let $f: D \subseteq \mathbb{R}^3 \to \mathbb{R}$ be a [continuous](../Continuity%20of%20Real%20Scalar%20Fields.md) [real scalar field](../Real%20Scalar%20Field.md) and $\mathcal{S} \subseteq D$ be a [surface](../../../../../Geometry/Euclidean%20Geometry/Surfaces/Surface.md) with a [smooth parameterisation](../../Parametric%20Surfaces/Smoothness%20of%20Surface%20Parameterisations.md) $\phi: D_\phi \subseteq \mathbb{R}^2 \to \mathbb{R}^3$.
>>
>>The **surface integral** of $f$ over $\mathcal{S}$ is the [double integral](Double%20Integral%20of%20a%20Real%20Scalar%20Field.md)
>>
>>$$
>>\iint\limits_{D_{\phi}} f(\phi(u,v)) \, ||\mathbf{N}(u,v)|| \mathop{\mathrm{d}D_{\phi}}
>>$$
>>
>>>[!NOTATION]-
>>>
>>>Since the surface integral is independent of the parameterisation, we denote it as
>>>
>>>$$\int_\mathcal{S} f \mathop{\mathrm{d}S}$$
>>>
>>
>