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

>[!DEFINITION] Definition: Equivalence of Parametric Curves
>
>Let $\mathcal{C} \subseteq \mathbb{R}^n$ be a [curve](Curves.md#Curves) in $\mathbb{R}^n$.
>
>Two [parametrizations](Parametric%20Curve.md) $\gamma_1: I_1 \subseteq \mathbb{R} \to \mathcal{C}$ and $\gamma_2: I_2 \subseteq \mathbb{R} \to \mathcal{C}$ are **equivalent** iff there exists a [differentiable](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md), [bijective](../../../Analysis/Functions/Types%20of%20Functions/Bijection.md) [function](../../../Analysis/Real%20Analysis/Real%20Functions/Real%20Functions.md) $\varphi: I_1 \to I_2$ with a [differentiable](../../../Analysis/Real%20Analysis/Real%20Functions/Differentiation/Derivatives.md) [inverse](../../../Analysis/Functions/Types%20of%20Functions/Injection.md) such that $\varphi'(t) \ne 0$ and $\gamma_2(\varphi(t)) = \gamma_1(t)$ for all $t \in I_1$.
>
>>[!DEFINITION] Definition: Reparametrizations
>>
>>Equivalent parametric curves are also called **reparametrizations**.
>>
>

>[!THEOREM] Theorem: Equivalence of Regular Injective Parametrizations
>
>All [regular](TODO) [injective](../../../Analysis/Functions/Types%20of%20Functions/Injection.md) [parametrizations](Curves.md#Parametrizations) of the same [curve](Curves.md#Curves) are [equivalent](Curves.md#Equivalence%20of%20Parametrizations).
>
>>[!PROOF]-
>>
>>TODO
>>
>

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

>[!DEFINITION] Definition: Length of Simple Curves
>
>
>

>[!THEOREM] Theorem: Length via Line Integral
>
>Let $\mathcal{C} \subset \mathbb{R}^n$ be a [simple curve](Curves.md#Simple%20Curves).
>
>If $\gamma: [a;b] \subset \mathbb{R} \to \mathbb{R}^n$ is a [regular](TODO) and [injective](../../../Analysis/Functions/Types%20of%20Functions/Injection.md) [parametrization](Curves.md#Parametrization) of $\mathcal{C}$, then the [length](Curves.md#Length) of $\mathcal{C}$ is given by the following [line integral](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Scalar%20Fields/Integration/Scalar%20Line%20Integrals.md):
>
>$$
>\int_{\gamma} 1 = \int_a^b ||\gamma'(t)|| \mathop{\mathrm{d}t}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

If a [curve](Curves.md#Curves) $\mathcal{C}$ is not [simple](Curves.md#Simple%20Curves) but can be represented as the [union](../../../Set%20Theory/Collections/Operations%20with%20Collections.md) $\mathcal{C} = \mathcal{C}_1 \cup \mathcal{C}_2 \cup \cdots \cup \mathcal{C}_{n-1} \cup \mathcal{C}_n$ of finitely many [simple curves](Curves.md#Simple%20Curves) $\mathcal{C}_1, \dotsc, \mathcal{C}_n$ such that $\mathcal{C}_{k}$ and $\mathcal{C}_{k+1}$ share exactly one point and this point lies on their [manifold boundary](../../Manifolds/Manifolds.md), then we define the length of $\mathcal{C}$ as the sum of the lengths of $\mathcal{C}_1, \dotsc, \mathcal{C}_n$:

$$
\mathcal{L}(\mathcal{C}) \overset{\text{def}}{=} \sum_{i = 1}^n \mathcal{L}(\mathcal{C}_i)
$$