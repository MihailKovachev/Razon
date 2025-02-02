>[!DEFINITION] Definition: Equivalence of Parametric Surfaces
>
>Let $\phi: \mathcal{D}_{\phi} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ and $\psi: \mathcal{D}_{\psi} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ be [parametric surfaces](Parametric%20Surface.md).
>
>We say that $\phi$ and $\psi$ are **equivalent** if they have the same [image](../../../Functions/Image%20of%20a%20Function.md) and there exists a [differentiable](../Real%20Vector%20Functions/Differentiation/Differentiability%20of%20Real%20Vector%20Functions.md), [bijective](../../../Functions/Types%20of%20Functions/Bijection.md) [real vector field](../Vector%20Fields/Real%20Vector%20Field.md) $h: \mathcal{D}_{\phi} \to \mathcal{D}_{\psi}$ with a [differentiable](../Real%20Vector%20Functions/Differentiation/Differentiability%20of%20Real%20Vector%20Functions.md) [inverse](../../../Functions/Types%20of%20Functions/Inverse%20Function.md) such that
>
>$$
>\psi \circ h = \phi 
>$$
>
>>[!DEFINITION] Definition: Reparameterisation
>>
>>Equivalent parametric surfaces are also known as **reparameterisations**.
>>
>>>[!DEFINITION] Definition: Smooth Reparameterisation
>>>
>>>We say that $\phi$ and $\psi$ are **smooth reparameterisations** if they are both [smooth](Smoothness.md) and $h$ and $h^{-1}$ are [continuously differentiable](../Real%20Vector%20Functions/Differentiation/Differentiability%20of%20Real%20Vector%20Functions.md).
>>>
>>
>

>[!THEOREM] Theorem: Surface Normals of Smooth Parameterisations
>
>If $\phi: \mathcal{D}_{\phi} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ and $\psi: \mathcal{D}_{\psi} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ are [smooth reparameterisations](Equivalence%20of%20Parametric%20Surfaces.md), then their [surface normal vectors](Surface%20Normal%20Vector.md) $\mathbf{N}_{\psi}$ and $\mathbf{N}_{\phi}$ at each $\mathbf{p} \in \phi(\mathcal{D}_{\phi})$ (or equivalently $\mathbf{p} \in \psi(\mathcal{D}_{\psi})$) are related by
>
>$$
>\mathbf{N}_{\phi} = k(\mathbf{p}) \mathbf{N}_{\psi},
>$$
>
>where $k(\mathbf{p}) \in \mathbb{R}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>