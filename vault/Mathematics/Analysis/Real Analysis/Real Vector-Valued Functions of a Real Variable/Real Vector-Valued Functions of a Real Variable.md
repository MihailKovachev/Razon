---
tags:
    - real-analysis
    - vector-analysis
    - analysis
    - mathematics
---

# Real Vector-Valued Functions of a Real Variable

>[!DEFINITION] Definition: Real Vector-Valued Functions of a Real Variable
>
>A **real vector-valued function of a real variable** is a [real vector-valued function](../Real%20Vector-Valued%20Functions.md) whose [domain](../../Functions/Functions.md) is a [subset](../../../Set%20Theory/Subsets.md) of the [real numbers](../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md):
>
>$$f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}^n$$
>

Some people require more stringent conditions in the definition such as [continuity](./Continuity%20(Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable).md) or [differentiability](./Differentiation/Differentiability%20(Real%20Parametric%20Curves).md).

>[!DEFINITION] Definition: Endpoints
>
>Let $\gamma: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [vector-valued function](./Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md).
>
>If $\mathcal{D}$ is a [compact interval](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) $[a;b]$, then we call $\gamma(a)$ and $\gamma(b)$ the **endpoints** of $\gamma$.
>

>[!DEFINITION] Definition: Closed Parametric Curve
>
>A [parametric curve](./Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\gamma: \mathcal{D} \subset \mathbb{R} \to \mathbb{R}^n$ is **closed** if $\mathcal{D}$ is a [compact interval](../Euclidean%20Space/Euclidean%20Space.md) $[a,b]$ and $\gamma$'s [endpoints](./Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) are equal:
>
>$$\gamma(a) = \gamma(b)$$
>

>[!DEFINITION] Definition: Simple Curve
>
>A [parametric curve](./Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\gamma: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}^n$ is **simple** if $\mathcal{D}$ is a [compact interval](../Euclidean%20Space/Euclidean%20Space.md) $[a,b]$ and $\gamma$ is [injective](../../Functions/Injections.md), except possibly for $\gamma (a) = \gamma(b)$.
>

>[!EXAMPLE]- Example: Curve through Points
>
>Given two [points](../Euclidean%20Space/Euclidean%20Space.md) $\mathbf{p}, \mathbf{q} \in \mathbb{R}$, the [image](../../Functions/Functions.md) of the [function](./Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $f: [0,1] \to \mathbb{R}$ defined as
>
>$$f(t) = t\mathbf{q} + (1-t)\mathbf{p}$$
>
>for all $t \in [0,1]$ is the [line](TODO) connecting $\boldsymbol{p}$ and $\boldsymbol{q}$.
>
