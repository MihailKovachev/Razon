---
tags:
    - real-analysis
    - asymptotic-analysis
    - analysis
    - mathematics
---

# Big Omega Notation

>[!DEFINITION] Definition: Big Omega Notation
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../Real%20Functions/Real%20Functions.md) and let $p \in \mathbb{R} \cup \{-\infty, +\infty\}$ be an [extended real number](../../../Algebra/Extended%20Real%20Numbers.md) which is an [accumulation point](../../../Topology/Accumulation%20Points.md) of the [intersection](../../../Set%20Theory/Intersections.md) $\mathcal{D}_f \cap \mathcal{D}_g$.
>
>We say that $f$ is **big Omega** of $g$ around $p$ if there exist some $C \in \mathbb{R}_{\gt 0}$ and some [deleted neighborhood](../../../Topology/Topological%20Spaces/Neighborhoods.md) $N$ of $p$ such that
>
>$$|f(x)| \ge C |g(x)|$$
>
>for all $x \in N \cap \mathcal{D}_f \cap \mathcal{D}_g$.
>
>>[!NOTATION]
>>
>>$$f(x) = \Omega(g(x)) \qquad \text{for} \qquad x\to p$$
>>
>>When $p$ can be inferred from context, we can omit $x \to p$. 
>>
>>We also use $\Omega(g(x))$ to denote *any* [function](../Real%20Functions/Real%20Functions.md) $h$ for which $h(x) = \Omega(g(x))$ holds.
>>
>

>[!THEOREM] Theorem: Big Omega Notation via Limits
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../Real%20Functions/Real%20Functions.md) and let $p$ be a [limit point](../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) of $\mathcal{D}_f \cap \mathcal{D}_g$ or $p = \pm \infty$.
>
>If there exists a [deleted neighborhood](../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) $\mathcal{N}(p)$ such that $g(x) \ne 0$ on $\mathcal{N}(p) \cap \mathcal{D}_f \cap \mathcal{D}_g$ and the [limit](../Real%20Functions/Limits%20(Real%20Functions).md) of the absolute value of the ratio of $f$ and $g$ is strictly positive or $\infty$, then $f$ is [Big Omega](#Big%20Omega%20Notation) of $g$ around $p$:
>
>$$\lim_{x \to p} \left|\frac{f(x)}{g(x)}\right| \in \mathbb{R}_{\gt 0} \cup \{\infty \} \implies f(x) = \Omega(g(x)) \text{ for } x\to p$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Sums in Big Omega Notation
>
>If $f_1$ and $f_2$ share the same sign around $p$ and $f_1$ is [Big Omega](#Big%20Omega%20Notation) of $g_1$ around $p$ and $f_2$ is [Big Omega](#Big%20Omega%20Notation) of $g_2$ around $p$, then $f_1 + f_2$ is [Big Omega](#Big%20Omega%20Notation) of $|g_1| + |g_2|$ around $p$:
>
>$$f_1 = \Omega(g_1) \text{ and } f_2 = \Omega(g_2) \implies f_1 + f_2 = \Omega(|g_1| + |g_2|)$$
>
>If $f_1$ and $f_2$ share the same sign around $p$, and $f_1$ is [Big Omega](#Big%20Omega%20Notation) of $g_1$ around $p$ and $f_2$ is [Big Omega](#Big%20Omega%20Notation) of $g_2$ around $p$, then $f_1 + f_2$ is [Big Omega](#Big%20Omega%20Notation) of $\max\{|g_1|, |g_2|\}$ around $p$:
>
>$$f_1 = \Omega(g_1) \text{ and } f_2 = \Omega(g_2) \implies f_1 + f_2 = \Omega(\max\{|g_1|, |g_2|\})$$
>
>If $f_1$ and $f_2$ share the same sign around $p$, and both are [Big Omega](#Big%20Omega%20Notation) of $g$ around $p$, then so is $f_1 + f_2$:
>
>$$f_1 = \Omega(g) \text{ and } f_2 = \Omega(g) \implies f_1 + f_2 = \Omega(g)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>