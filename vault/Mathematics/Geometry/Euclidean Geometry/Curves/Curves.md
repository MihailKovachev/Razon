---
title: Simple Curve
tags:
  - curves
  - euclidean-geometry
  - geometry
  - mathematics
---

# Curves

>[!DEFINITION] Definition: Curve
>
>A **curve** $\mathcal{C}$ in $\mathbb{R}^n$ is a [geometric figure](../Geometric%20Shapes.md) which is the [image](../../../Analysis/Functions/Functions.md) of a nonconstant [parametric curve](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Parametric%20Curves/Parametric%20Curve.md) $\gamma$.
>

## Parametrizations

>[!DEFINITION] Definition: Curve Parametrization
>
>A **parametrization** of a [curve](Curves.md#Curves) $\mathcal{C}$ in $\mathbb{R}^n$ is a [continuous](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Continuity%20of%20Real%20Vector%20Functions.md) [function](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Real%20Vector%20Function.md) $\gamma: I \subseteq \mathbb{R} \to \mathbb{R}^n$ on an [interval](../../../Analysis/Real%20Analysis/The%20Topology%20of%20Euclidean%20Space.md) $I$ whose [image](../../../Analysis/Functions/Functions.md) is $\mathcal{C}$.
>
>$$
>\gamma(I) = \mathcal{C}
>$$
>

The same [curve](Curves.md#Curves) can have many different [parametrizations](Curves.md#Parametrizations).

>[!EXAMPLE]- Example: Different Parametrizations of the Same Curve
>
>TODO
>

More over, not all parametrizations are created equal. A single curve can have multiple parametrizations but some of them will be more useful than others because they have certain properties. 

### Equivalence of Parametrizations

>[!DEFINITION] Definition: Reparametrization
>
>Let $\mathcal{C}$ be a [curve](Curves.md#Curves) in $\mathbb{R}^n$ and let $\gamma: I_{\gamma} \subseteq \mathbb{R} \to \mathbb{R}^n$ and $\varphi: I_{\varphi} \subseteq \mathbb{R} \to \mathbb{R}^n$ be [parametrizations](Parametric%20Curve.md) of $\mathcal{C}$.
>
>A **reparametrization** between $\gamma$ and $\varphi$ is a [bijective](../../../Analysis/Functions/Types%20of%20Functions/Bijection.md) [function](../../../Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) $h_{I_{\gamma} \to I_{\varphi}}: I_{\gamma} \to I_{\varphi}$ with [inverse](../../../Analysis/Functions/Types%20of%20Functions/Injection.md) $h_{I_{\varphi} \to I_{\gamma}}: I_{\varphi} \to I_{\gamma}$ such that
>
>$$
>\begin{align*}
>\gamma(t) = \varphi(h_{I_{\gamma} \to I_{\varphi}}(t)) \qquad \forall t \in I_{\gamma} \\
>\varphi(t) = \gamma(h_{I_{\varphi} \to I_{\gamma}}(t)) \qquad \forall t \in I_{\varphi}
>\end{align*}
>$$
>
>>[!NOTE]
>>
>>This is the most general definition for reparametrization. However, it is quite common to require that both $h_{I_{\gamma} \to I_{\varphi}}$ and $h_{I_{\varphi} \to I_{\gamma}}$ have additional properties such as [continuity](../../../Analysis/Real%20Analysis/Real%20Functions/Continuity.md), [continuous differentiability](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md) or [smoothness](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md). In this case, when we say that a reparametrization has some property, we mean that both $h_{I_{\gamma} \to I_{\varphi}}$ and $h_{I_{\varphi} \to I_{\gamma}}$ have this property.
>>
>

>[!DEFINITION] Definition: Equivalence of Parametrizations
>
>Let $\mathcal{C}$ be a [curve](Curves.md#Curves) in $\mathbb{R}^n$.
>
>Two [parametrizations](Parametric%20Curve.md) $\gamma: I_{\gamma} \subseteq \mathbb{R} \to \mathbb{R}^n$ and $\varphi: I_{\varphi} \subseteq \mathbb{R} \to \mathbb{R}^n$ of $\mathcal{C}$ are **equivalent** if and only if there exists a [reparametrization](Curves.md#Equivalence%20of%20Parametrizations) between them.
>
>>[!NOTE] Note
>>
>>This is the most general definition of equivalence for parametrizations. However, sometimes we require that such a [reparametrization](Curves.md#Equivalence%20of%20Parametrizations) also has additional properties such as [continuity](../../../Analysis/Real%20Analysis/Real%20Functions/Continuity.md), [continuous differentiability](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md) or [smoothness](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md). In this case, we say that $\gamma$ and $\varphi$ are "equivalent up to a PROPERTY reparametrization" such as "equivalent up to a continuous reparametrization" or "equivalent up to a smooth reparametrization".
>>
>

>[!THEOREM] Theorem: Equivalence of Regular Injective Parametrizations
>
>Let $\gamma: I_{\gamma} \subseteq \mathbb{R} \to \mathbb{R}^n$ and $\varphi: I_{\varphi} \subseteq \mathbb{R} \to \mathbb{R}^n$ be [parametrizations](Curves.md#Parametrizations) of the same [curve](Curves.md#Curves) $\mathcal{C}$.
>
>If $\gamma$ and $\varphi$ are $C^1$-[regular](TODO) (i.e. [continuously differentiable](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) with a non-vanishing [derivative](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md)) and [injective](../../../Analysis/Functions/Types%20of%20Functions/Injection.md), then they are [equivalent](Curves.md#Equivalence%20of%20Parametrizations) up to a [continuously differentiable](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md) [reparametrization](Curves.md#Equivalence%20of%20Parametrizations).
>
>>[!PROOF]-
>>
>>TODO
>>
>

#### Orientation of Equivalent Parametrizations

[Continuously differentiable](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) [parametrizations](Curves.md#Parametrizations) which are [equivalent](Curves.md#Equivalence%20of%20Parametrizations) up to a [continuously differentiable](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md) [reparametrization](Curves.md#Equivalence%20of%20Parametrizations) with a non-vanishing [derivative](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md) exhibit a nice property which allows us to define orientations for them.

>[!THEOREM] Theorem: Unit Tangent Vectors of Equivalent Parametrizations
>
>Let $\gamma: I_{\gamma} \subseteq \mathbb{R} \to \mathbb{R}^n$ and $\gamma: I_{\gamma} \subseteq \mathbb{R} \to \mathbb{R}^n$ be two [parametrizations](Curves.md#Parametrizations) of the same [curve](Curves.md#Curve) $\mathcal{C}$.
>
>If $\gamma$ and $\varphi$ are [differentiable](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) with non-vanishing [derivatives](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) and are also [equivalent](Curves.md#Equivalence%20of%20Parametrizations) up to a [continuously differentiable](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md) [reparametrization](Curves.md#Equivalence%20of%20Parametrizations) $\{h_{I_{\gamma} \to I_{\varphi}}, h_{I_{\varphi} \to I_{\gamma}}\}$ with a non-vanishing [derivative](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md), then exactly one of the following is true for their [unit tangent vectors](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Tangent%20Vector.md):
>
>- Case (I): $\mathbf{T}_{\varphi}(t) = \mathbf{T}_{\gamma}(h_{I_{\varphi} \to I_{\gamma}}(t))$ for all $t \in I_{\varphi}$
>- Case (II): $\mathbf{T}_{\varphi}(t) = -\mathbf{T}_{\gamma}(h_{I_{\varphi} \to I_{\gamma}}(t))$ for all $t \in I_{\varphi}$
>
>>[!PROOF]-
>>
>>By definition, we have $\varphi(t) = \gamma(h_{I_{\varphi} \to I_{\gamma}}(t))$. The [chain rule](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiation%20Rules%20for%20Curve%20Parameterisations.md) gives us
>>
>>$$
>>\varphi'(t) = \gamma'(h_{I_{\varphi} \to I_{\gamma}}(t)) \cdot h_{I_{\varphi} \to I_{\gamma}}'(t).
>>$$
>>
>>The [unit tangent vector](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Tangent%20Vector.md) $\mathbf{T}_{\varphi}$ of $\varphi$ is given by $\frac{\varphi'}{||\varphi'||}$ which combined with the above yields
>>
>>$$
>>\mathbf{T}_{\varphi}(t) = \frac{\varphi'(t)}{||\varphi'(t)||} = \frac{\gamma'(h_{I_{\varphi} \to I_{\gamma}}(t)) \cdot h_{I_{\varphi} \to I_{\gamma}}'(t)}{||\gamma'(h_{I_{\varphi} \to I_{\gamma}}(t)) \cdot h_{I_{\varphi} \to I_{\gamma}}'(t)||}.
>>$$
>>
>>We can use the property of the norm to transform the above expression into the following:
>>
>>$$
>>\mathbf{T}_{\varphi}(t) = \frac{h_{I_{\varphi} \to I_{\gamma}}'(t)}{|h_{I_{\varphi} \to I_{\gamma}}'(t)|} \frac{\gamma'(h_{I_{\varphi} \to I_{\gamma}}(t))}{||\gamma'(h_{I_{\varphi} \to I_{\gamma}}(t))||} = \frac{h_{I_{\varphi} \to I_{\gamma}}'(t)}{|h_{I_{\varphi} \to I_{\gamma}}'(t)|} \mathbf{T}_{\gamma}(h_{I_{\varphi} \to I_{\gamma}}(t)).
>>$$
>>
>>Since $h_{I_{\varphi} \to I_{\gamma}}'(t)$ is [continuously differentiable](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md) with a non-vanishing [derivative](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md), it must be the case that either $h_{I_{\varphi} \to I_{\gamma}}'(t) \gt 0$ or $h_{I_{\varphi} \to I_{\gamma}}'(t) \lt 0$ for all $t \in I_{\varphi}$. Moreover, we notice that $\frac{h_{I_{\varphi} \to I_{\gamma}}'(t)}{|h_{I_{\varphi} \to I_{\gamma}}'(t)|}$ is $1$ if and only if $h_{I_{\varphi} \to I_{\gamma}}'(t) \gt 0$ and $\frac{h_{I_{\varphi} \to I_{\gamma}}'(t)}{|h_{I_{\varphi} \to I_{\gamma}}'(t)|}$ is $-1$ if and only if $h_{I_{\varphi} \to I_{\gamma}}'(t) \lt 0$ and so either $\frac{h_{I_{\varphi} \to I_{\gamma}}'(t)}{|h_{I_{\varphi} \to I_{\gamma}}'(t)|} = 1$ for all $t \in I_{\varphi}$ or $\frac{h_{I_{\varphi} \to I_{\gamma}}'(t)}{|h_{I_{\varphi} \to I_{\gamma}}'(t)|} = -1$ or $t \in I_{\varphi}$.
>>
>
>>[!DEFINITION] Definition: Orientation of Parametrizations
>>
>>We say that $\gamma$ and $\varphi$ have
>>- the **same orientation** in the first case;
>>- **opposite orientations** in the second case.
>>
>>>[!NOTE] Note: Preserving and Reversing Orientation
>>>
>>>We might also say that $\gamma$ and $\varphi$ are equivalent up to an
>>>- **orientation-preserving** reparametrization in the first case;
>>>- **orientation-reversing** reparametrization in the second case;
>>>
>>
>

Intuitively, the above theorem tells us that, under the specified conditions, the unit tangent of one parametrization at each point on the curve is always either equal or exactly opposite to the unit tangent vector of the other parametrization at the same point.

![](res/Unit%20Tangent%20Vectors%20of%20Equivalent%20Parametrizations.svg)

## Types of Curves

### Curves with Endpoints

>[!DEFINITION] Definition: Endpoints
>
>TODO
>

### Closed Curves

>[!DEFINITION] Definition: Closed Curves
>
>A [curve](Curves.md) is **closed** iff it is [compact](../../../Analysis/Real%20Analysis/The%20Topology%20of%20Euclidean%20Space.md) and without [manifold boundary](../../Manifolds/Manifolds.md).
>

### Simple Curves

>[!DEFINITION] Definition: Simple Curve
>
>A **simple curve** is a [curve](Curves.md#Curves) $\mathcal{C}$ for which there exists an [injective](../../../Analysis/Functions/Types%20of%20Functions/Injection.md) [parametrization](Curves.md#Parametrizations) $\gamma: I \subset \mathbb{R} \to \mathbb{R}^n$ on a closed interval $I = [a;b]$ with a [continuous](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Scalar%20Fields/Continuity%20of%20Real%20Scalar%20Fields.md) [inverse](../../../Analysis/Functions/Types%20of%20Functions/Injection.md).
>
>>[!NOTE]
>>
>>Simples curves are also known as **Jordan arcs**.
>>
>

A [simple curve](Curves.md#Simple%20Curves) is just a [curve with endpoints](Curves.md#Curves%20with%20Endpoints) which does not intersect itself. The existence of a continuous inverse also guarantees that curve is not [space-filling](TODO).


# Length

>[!DEFINITION] Definition: Length of Curves
>
>>[!NOTE] Note: Generalization to Non-Simple Curves
>>
>>If a [curve](Curves.md#Curves) $\mathcal{C}$ is not [simple](Curves.md#Simple%20Curves) but can be represented as the [union](../../../Set%20Theory/Collections/Operations%20with%20Collections.md) $\mathcal{C} = \mathcal{C}_1 \cup \mathcal{C}_2 \cup \cdots \cup \mathcal{C}_{n-1} \cup \mathcal{C}_n$ of finitely many [simple curves](Curves.md#Simple%20Curves) $\mathcal{C}_1, \dotsc, \mathcal{C}_n$ such that $\mathcal{C}_{k}$ and $\mathcal{C}_{k+1}$ share exactly one point and this point lies on their [manifold boundary](../../Manifolds/Manifolds.md), then we define the length of $\mathcal{C}$ as the sum of the lengths of $\mathcal{C}_1, \dotsc, \mathcal{C}_n$:
>>
>>$$
>>\mathcal{L}(\mathcal{C}) \overset{\text{def}}{=} \sum_{i = 1}^n \mathcal{L}(\mathcal{C}_i)
>>$$
>>
>

>[!THEOREM] Theorem: Length via Line Integral
>
>The [length](Curves.md#Length) of a [curve](Curves.md) $\mathcal{C} \subset \mathbb{R}^n$ is given by the [line integral](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Scalar%20Fields/Integration/Scalar%20Line%20Integrals.md#Scalar%20Line%20Integrals%20over%20Geometric%20Curves) of $1$ over $\mathcal{C}$.
>
>$$
>\int_{\mathcal{C}} 1 \mathop{\mathrm{d}s}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

