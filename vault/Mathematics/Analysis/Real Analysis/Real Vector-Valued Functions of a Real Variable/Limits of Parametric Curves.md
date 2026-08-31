---
title: Limits of Parametric Curves
tags:
    - real-analysis
    - vector-analysis
    - mathematical-analysis
    - mathematics
---

# Limits of Parametric Curves

In the case of [vector-valued functions](./Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) $\gamma: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}^n$, the definition of a [limit](../Real%20Vector%20Functions/Limits%20(Real%20Vector%20Functions).md) reduces to the following.

>[!DEFINITION] Definition: Limits of Parametric Curves
>
>Let $\gamma: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}^n$ be a [vector-valued functions](./Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable.md) let $t_0$ be an [accumulation point](../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}$.
>
>We say that $\mathbf{L} \in \mathbb{R}^n$ is the [limit](../Real%20Vector%20Functions/Limits%20(Real%20Vector%20Functions).md) of $\gamma$ for $t \to t_0$ if and only if for each $\varepsilon \gt 0$, there exists some $\delta \gt 0$ such that for all $t \in I$ we have
>
>$$
>0 \lt ||t - t_0|| \lt \delta \implies ||\gamma(t) - \mathbf{L}|| \lt \varepsilon
>$$ 
>
