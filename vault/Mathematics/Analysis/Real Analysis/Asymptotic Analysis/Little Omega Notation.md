---
tags:
    - real-analysis
    - asymptotic-analysis
    - analysis
    - mathematics
---

# Little Omega Notation

>[!DEFINITION] Definition: Little Omega Notation (Real Functions)
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../Real%20Functions/Real%20Functions.md) and let $p \in \mathbb{R} \cup \{-\infty, +\infty\}$ be an [extended real number](../../../Algebra/Extended%20Real%20Numbers.md) which is an [accumulation point](../../../Topology/Accumulation%20Points.md) of the [intersection](../../../Set%20Theory/Intersections.md) $\mathcal{D}_f \cap \mathcal{D}_g$.
>
>We say that $f$ is **little omega** of $g$ around $p$ if, for every $M \in \mathbb{R}_{\gt 0}$, there exists some [deleted neighborhood](../../../Topology/Topological%20Spaces/Neighborhoods.md) $N$ of $p$ such that
>
>$$|f(x)| \ge M |g(x)|$$
>
>for all $x \in N \cap \mathcal{D}_f \cap \mathcal{D}_g$.
>
>>[!NOTATION]
>>
>>$$f(x) = \omega(g(x)) \qquad \text{for} \qquad x\to p$$
>>
>>When $p$ can be inferred from context, we can omit $x \to p$. 
>>
>>We also use $\omega(g(x))$ to denote *any* [function](../Real%20Functions/Real%20Functions.md) $h$ for which $h(x) = \omega(g(x))$ holds.
>>
>

>[!THEOREM] Theorem: Little Omega Notation via Limits
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../Real%20Functions/Real%20Functions.md) and let $p$ be a [limit point](../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) of $\mathcal{D}_f \cap \mathcal{D}_g$ or $p = \pm \infty$.
>
>If there exists a [deleted neighborhood](../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) $\mathcal{N}(p)$ such that $g(x) \ne 0$ on $\mathcal{N}(p) \cap \mathcal{D}_f \cap \mathcal{D}_g$, then $f$ is [little omega](#Little%20omega%20Notation) of $g$ around $p$ if and only if the [limit](../Real%20Functions/Limits%20(Real%20Functions).md) of the absolute value of their ratio at $p$ is $\infty$:
>
>$$f(x) = \omega(g(x)) \text{ for } x\to p \iff \lim_{x \to p} \left| \frac{f(x)}{g(x)} \right| = \infty$$
>
>>[!PROOF]-
>>
>>TODO
>>
>