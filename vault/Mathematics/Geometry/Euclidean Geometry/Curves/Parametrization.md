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

# Parametrizations

>[!DEFINITION] Definition: Curve Parametrization
>
>A **parametrization** of a [curve](Curves.md#Curves) $\mathcal{C}$ in $\mathbb{R}^n$ is a [continuous](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Continuity%20of%20Real%20Vector%20Functions.md) [function](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Real%20Vector%20Function.md) $\gamma: I \subseteq \mathbb{R} \to \mathbb{R}^n$ on an [interval](../../../Analysis/Real%20Analysis/The%20Topology%20of%20Euclidean%20Space.md) $I$ whose [image](../../../Analysis/Functions/Functions.md) is $\mathcal{C}$.
>
>$$
>\gamma(I) = \mathcal{C}
>$$
>
>>[!NOTE] Note: Parametric Curves
>>
>>Parametrizations are often called **parametric curves**.
>>
>

The same [curve](Curves.md#Curves) can have many different [parametrizations](Curves.md#Parametrizations).

>[!EXAMPLE]- Example: Different Parametrizations of the Same Curve
>
>TODO
>

More over, not all parametrizations are created equal. A single curve can have multiple parametrizations but some of them will be more useful than others because they have certain properties. 

## Tangent Vectors

[Differentiable](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) [parametrizations](Parametrization.md#Parametrizations) allows us to define the notion of "tangentiality" for [curves](Curves.md).

>[!DEFINITION] Definition: Tangent Vector
>
>Let $\gamma: I \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [curve parametrization](Parametrization.md) which is [differentiable](Differentiability%20of%20Parametric%20Curves.md) at $t \in I$.
>
>The **tangent vector** of $\gamma$ at $t$ is the [derivative](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) $\dot{\gamma}(t)$ of $\gamma$ there.
>
>>[!NOTE]
>>
>>The tangent vector is also known as $\gamma$'s **velocity** and its magnitude as $\gamma$'s **speed**.
>>
>
>>[!DEFINITION] Definition: Unit Tangent Vector
>>
>>The **unit tangent vector** is the [unit vector](../../../../../Algebra/Linear%20Algebra/Vector%20Spaces/Normed%20Vector%20Spaces/Unit%20Vector.md) obtained from the [tangent vector](Parametrization.md#Tangent%20Vectors):
>>
>>$$
>>\frac{1}{||\dot{\gamma}(t)||}\dot{\gamma}(t)
>>$$
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\mathbf{T}(t)
>>>$$
>>>
>>
>

It is apparent from the above definition that there is no unique [tangent vector](Parametrization.md#Tangent%20Vectors) which is intrinsic to a [curve](Curves.md)'s geometry. Instead, tangent vectors depend on the [parametrization](Parametrization.md#Parametrizations) in question. However, it turns out that the [tangent vectors](Parametrization.md#Tangent%20Vectors) of all [parametrizations](Parametrization.md#Parametrizations) at the same point, if they exist, are collinear.

>[!THEOREM] Theorem: Collinearity of Tangent Vectors
>
>Let $\mathcal{C}$ be a [curve](Curves.md) in $\mathbb{R}^n$ and let $\gamma: I_{\gamma} \subseteq \mathbb{R} \to \mathbb{R}^n$ and $\varphi: I_{\varphi} \subseteq \mathbb{R} \to \mathbb{R}^n$ be [parametrizations](Parametrization.md#Parametrizations) of $\mathcal{C}$. Let $\mathbf{p} \in \mathcal{C}$ and let $t \in I_{\gamma}$ and $s \in I_{\varphi}$ be such that $\gamma(t) = \mathbf{p}$ and $\varphi(s) = \mathbf{p}$.
>
>If $\gamma$ is [differentiable](Differentiability%20of%20Parametric%20Curves.md) at $t$ and $\varphi$ is [differentiable](Differentiability%20of%20Parametric%20Curves.md) at $s$, then there exists some $\lambda \in \mathbb{R}$ such that
>
>$$
>\dot{\gamma}(t) = \lambda \, \dot{\varphi}(s)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

The above theorem tells us that all [tangent vectors](Parametrization.md#Tangent%20Vectors) at a point of a [curve](Curves.md) line on a [straight line](Straight%20Lines/Straight%20Line.md)

>[!DEFINITION] Definition: Tangent Line
>
>The **tangent line** to a [curve](Curves.md) $\mathcal{C}$ at $\mathbf{p} \in \mathcal{C}$ is the [straight line](Straight%20Lines/Straight%20Line.md)
>
>$$
>\{ \mathbf{p} + k \mathbf{t} \mid k \in \mathbb{R} \},
>$$
>
>where $\mathbf{t}$ is any non-zero [tangent vector](Parametrization.md#Tangent%20Vectors) of a [parametrization](Parametrization.md#Parametrizations) of $\mathcal{C}$ at $\mathbf{p}$.
>

## Normal Vectors

>[!DEFINITION] Definition: Normal Vector
>
>Let $\gamma: I \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [curve parametrization](Parametrization.md) which is twice [differentiable](Differentiability%20of%20Parametric%20Curves.md) at $t \in I$.
>
>The **normal vector** of $\gamma$ at $t$ is the [derivative](Differentiability%20of%20Parametric%20Curves.md) of its [tangent vector](Parametrization.md#Tangent%20Vectors) there, i.e. $\gamma$'s second [derivative](Differentiability%20of%20Parametric%20Curves.md) $\ddot{\gamma}(t)$.
>
>>[!DEFINITION] Definition: Unit Normal Vector
>>
>>The **unit normal vector** is the [unit vector](../../../../../Algebra/Linear%20Algebra/Vector%20Spaces/Normed%20Vector%20Spaces/Unit%20Vector.md) obtained from $\gamma$'s [normal vector](Parametrization.md#Normal%20Vectors):
>>
>>$$
>>\frac{1}{||\dot{\mathbf{T}}(t)||}\dot{\mathbf{T}}(t)
>>$$
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\mathbf{N}(t)
>>>$$
>>>
>>
>

## Binormal Vectors

>[!DEFINITION] Definition: Binormal Vector
>
>Let $\gamma: I \subseteq \mathbb{R} \to \mathbb{R}^3$ be a [curve parametrization](Parametrization.md) which is twice [differentiable](Differentiability%20of%20Parametric%20Curves.md) at $t \in I$.
>
>
>The **binormal vector** of $\gamma$ at $t$ is the [cross product](../../../Algebra/Linear%20Algebra/Matrices/Row%20and%20Column%20Vectors/Real%20Vectors/Real%20Cross%20Product.md) of its [unit tangent vector](Parametrization.md#Tangent%20Vectors) and its [unit normal vector](Parametrization.md#Normal%20Vectors) at $t$:
>
>$$
>\mathbf{T}(t) \times \mathbf{N}(t)
>$$
>
>>[!NOTATION]
>>
>>$$
>>\mathbf{B}(t)
>>$$
>>
>

# Equivalence of Parametrizations

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
>Two [parametrizations](Parametric%20Curve.md) $\gamma: I_{\gamma} \subseteq \mathbb{R} \to \mathbb{R}^n$ and $\varphi: I_{\varphi} \subseteq \mathbb{R} \to \mathbb{R}^n$ of $\mathcal{C}$ are **equivalent** if and only if there exists a [reparametrization](Parametrization.md#Equivalence%20of%20Parametrizations) between them.
>
>>[!NOTE] Note
>>
>>This is the most general definition of equivalence for parametrizations. However, sometimes we require that such a [reparametrization](Parametrization.md#Equivalence%20of%20Parametrizations) also has additional properties such as [continuity](../../../Analysis/Real%20Analysis/Real%20Functions/Continuity.md), [continuous differentiability](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md) or [smoothness](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md). In this case, we say that $\gamma$ and $\varphi$ are "equivalent up to a PROPERTY reparametrization" such as "equivalent up to a continuous reparametrization" or "equivalent up to a smooth reparametrization".
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

### Orientation

[Continuously differentiable](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) [parametrizations](Curves.md#Parametrizations) which are [equivalent](Curves.md#Equivalence%20of%20Parametrizations) up to a [continuously differentiable](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md) [reparametrization](Curves.md#Equivalence%20of%20Parametrizations) with a non-vanishing [derivative](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md) exhibit a nice property which allows us to define orientations for them.

>[!THEOREM] Theorem: Unit Tangent Vectors of Equivalent Parametrizations
>
>Let $\gamma: I_{\gamma} \subseteq \mathbb{R} \to \mathbb{R}^n$ and $\gamma: I_{\gamma} \subseteq \mathbb{R} \to \mathbb{R}^n$ be two [parametrizations](Curves.md#Parametrizations) of the same [curve](Curves.md#Curve) $\mathcal{C}$.
>
>If $\gamma$ and $\varphi$ are [differentiable](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) with non-vanishing [derivatives](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Parametric%20Curves/Differentiation/Differentiability%20of%20Parametric%20Curves.md) and are also [equivalent](Curves.md#Equivalence%20of%20Parametrizations) up to a [continuously differentiable](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md) [reparametrization](Curves.md#Equivalence%20of%20Parametrizations) $\{h_{I_{\gamma} \to I_{\varphi}}, h_{I_{\varphi} \to I_{\gamma}}\}$ with a non-vanishing [derivative](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md), then exactly one of the following is true for their [unit tangent vectors](Parametrization.md):
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
>>The [unit tangent vector](Parametrization.md) $\mathbf{T}_{\varphi}$ of $\varphi$ is given by $\frac{\varphi'}{||\varphi'||}$ which combined with the above yields
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



Intuitively, the above theorem tells us that, under the specified conditions, the unit tangent vectorof one parametrization at each point on the curve is always either equal or exactly opposite to the unit tangent vector of the other parametrization at the same point.

![](res/Unit%20Tangent%20Vectors%20of%20Equivalent%20Parametrizations.svg)

# Bibliography

