---
title: Parametrization
tags:
  - vector-analysis
  - real-analysis
  - analysis
  - euclidean-geometry
  - geometry
  - mathematics
---

# Parametrization

>[!DEFINITION] Definition: Surface Parametrization
>
>Let $\mathcal{S}$ be a [surface](Surfaces.md) in $\mathbb{R}^n$.
>
>A **parametrization** of $\mathcal{S}$ is a [continuous](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Continuity%20of%20Real%20Vector%20Functions.md) [function](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Real%20Vector%20Function.md) $\varphi: \mathcal{D} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ on a [connected set](../../../Analysis/Real%20Analysis/The%20Topology%20of%20Euclidean%20Space.md#Connectedness) $\mathcal{D}$ which is [injective](../../../Analysis/Functions/Types%20of%20Functions/Injection.md) on $\mathcal{D}$ except possibly at the [boundary](../../../Topology/Interior,%20Boundary,%20Exterior/Boundary.md) $\partial \mathcal{D}$ and whose [image](../../../Analysis/Functions/Functions.md) is $\mathcal{S}$.
>

## Equivalence of Parametrizations

>[!DEFINITION] Definition: Reparametrization
>
>Let $\psi: \mathcal{D}_{\psi} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ and $\phi: \mathcal{D}_{\phi} \subseteq \mathbb{R}^2 \to \mathbb{R}^n$ be [parametrizations](Surfaces.md#Parametrizations) of the same [surface](surfaces.md#Surfaces) $\mathcal{S} \subset \mathbb{R}^n$.
>
>A **reparametrization** between $\psi$ and $\phi$ is a [bijective](../../../Analysis/Functions/Types%20of%20Functions/Bijection.md) [function](../../../Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) $h_{\mathcal{D}_{\psi} \to \mathcal{D}_{\phi}}: \mathcal{D}_{\psi} \to \mathcal{D}_{\phi}$ with [inverse](../../../Analysis/Functions/Types%20of%20Functions/Injection.md) $h_{\mathcal{D}_{\phi} \to \mathcal{D}_{\psi}}: \mathcal{D}_{\phi} \to \mathcal{D}_{\psi}$ such that
>
>$$
>\begin{align*}
>\psi(\mathbf{x}) = \phi(h_{\mathcal{D}_{\psi} \to \mathcal{D}_{\phi}}(\mathbf{x})) \qquad \forall \mathbf{x} \in \mathcal{D}_{\psi} \\
>\phi(\mathbf{x}) = \psi(h_{\mathcal{D}_{\phi} \to \mathcal{D}_{\psi}}(\mathbf{x})) \qquad \forall \mathbf{x} \in \mathcal{D}_{\phi}
>\end{align*}
>$$
>
>>[!NOTE]
>>
>>This is the most general definition for reparametrization. However, it is quite common to require that both $h_{I_{\psi} \to I_{\phi}}$ and $h_{I_{\phi} \to I_{\psi}}$ have additional properties such as [continuity](../../../Analysis/Real%20Analysis/Real%20Functions/Continuity.md), [continuous differentiability](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md) or [smoothness](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md). In this case, when we say that a reparametrization has some property, we mean that both $h_{I_{\psi} \to I_{\phi}}$ and $h_{I_{\phi} \to I_{\psi}}$ have this property.
>>
>

>[!DEFINITION] Definition: Equivalence of Parametrizations
>
>Two [parametrizations](Surfaces.md#Parametrizations) of a [surface](Surfaces.md#Parametrizations) $\mathcal{S}$ are **equivalent** if and only if there exists a [reparametrization](Surfaces.md#Equivalence%20of%20Parametrizations) between them.
>
>>[!NOTE] Note
>>
>>This is the most general definition of equivalence for parametrizations. However, sometimes we require that such a [reparametrization](Surfaces.md#Equivalence%20of%20Parametrizations) also has additional properties such as [continuity](../../../Analysis/Real%20Analysis/Real%20Functions/Continuity.md), [continuous differentiability](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md) or [smoothness](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md). In this case, we say that $\psi$ and $\phi$ are "equivalent up to a PROPERTY reparametrization" such as "equivalent up to a continuous reparametrization" or "equivalent up to a smooth reparametrization".
>>
>