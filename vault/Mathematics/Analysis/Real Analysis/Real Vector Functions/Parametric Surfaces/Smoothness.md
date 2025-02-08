---
title: Smoothness of Parametric Surfaces
---


>[!DEFINITION] Definition: Smoothness of Parametric Surfaces
>
>Let $s: \mathcal{D} \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ be a [parametric surface](Parametric%20Surface.md).
>
>We say that $s$ is **smooth at** $\mathbf{a}$ iff it is [differentiable](../../Real%20Vector%20Functions/Differentiation/Differentiability%20of%20Real%20Vector%20Functions.md) there and its [normal vector](Surface%20Normal%20Vector.md) at $\mathbf{a}$ is nonzero.
>
>If $s$ is smooth at every $\mathbf{x}$ in some $S \subseteq \mathbb{R}^2$, then we say that $s$ is **smooth on** $S$. If $S = \mathcal{D}$, then we just say that $s$ is **smooth**.
>

>[!DEFINITION] Definition: Piecewise Smoothness
>
>A **piecewise smooth parametric surface** is a [function](../../Real%20Vector%20Functions/Real%20Vector%20Function.md) $\phi: \mathcal{D} \subseteq \mathbb{R}^2 \to \mathbb{R}^3$ such that $\mathcal{D}$ can be represented as the [union](../../../../Set%20Theory/Collections/Operations%20with%20Collections.md) of finitely many [disjoint sets](../../../../Set%20Theory/Disjoint%20Sets.md) $\mathcal{D}_1, \dotsc, \mathcal{D}_k$ and $\phi$ can be represented as
>
>$$
>\phi (\mathbf{x}) = 
>\begin{cases}
>
>s_1(\mathbf{x}) \qquad \text{ if } \mathbf{x} \in \mathcal{D}_1 \\
>
>\vdots \\
>
>s_k(\mathbf{x}) \qquad \text{ if } \mathbf{x} \in \mathcal{D}_k
>
>\end{cases}
>$$
>
>where $s_1: \mathcal{D}_1 \to \mathbb{R}^3, \dotsc, s_k: \mathcal{D}_k \to \mathbb{R}^3$ are [parametric surfaces](Parametric%20Surface.md) which are [smooth](Smoothness.md) except at possibly finitely many places.
>