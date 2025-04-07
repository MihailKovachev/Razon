---
title: Curves
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
>A **simple curve** is a [curve](Curves.md#Curves) $\mathcal{C}$ for which there exists an [injective](../../../Analysis/Functions/Injections,%20Surjections%20and%20Bijections.md) [parametrization](Curves.md#Parametrizations) $\gamma: I \subset \mathbb{R} \to \mathbb{R}^n$ on a closed interval $I = [a;b]$ with a [continuous](../../../Analysis/Real%20Analysis/Real%20Vector%20Functions/Scalar%20Fields/Continuity%20of%20Real%20Scalar%20Fields.md) [inverse](../../../Analysis/Functions/Injections,%20Surjections%20and%20Bijections.md).
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

