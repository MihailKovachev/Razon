---
tags:
    - real-analysis
    - analysis
    - mathematics
---

# Big Theta Notation

>[!DEFINITION] Definition: Big Theta Notation
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../Real%20Functions/Real%20Functions.md) and let $p \in \mathbb{R} \cup \{-\infty, +\infty\}$ be an [extended real number](../../../Algebra/Extended%20Real%20Numbers.md) which is an [accumulation point](../../../Topology/Accumulation%20Points.md) of the [intersection](../../../Set%20Theory/Intersections.md) $\mathcal{D}_f \cap \mathcal{D}_g$.
>
>We say that $f$ is **big Theta** of $g$ around $p$ if there exist some $C_1, C_2 \in \mathbb{R}_{\gt 0}$ and a [deleted neighborhood](../../../Topology/Topological%20Spaces/Neighborhoods.md) $N$ of $p$ such that
>
>$$C_1 |g(x)| \le |f(x)| \le C_2 |g(x)|$$
>
>for all $x \in N \cap \mathcal{D}_f \cap \mathcal{D}_g$.
>
>>[!NOTATION]
>>
>>$$f(x) = \Theta(g(x)) \qquad \text{for} \qquad x\to p$$
>>
>>When $p$ can be inferred from context, we can omit $x \to p$. 
>>
>>We also use $\Theta(g(x))$ to denote *any* [function](../Real%20Functions/Real%20Functions.md) $h$ for which $h(x) = \Theta(g(x))$ holds.
>>
>

>[!THEOREM] Theorem: Big Theta via Big O
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../Real%20Functions/Real%20Functions.md) and let $p \in \mathbb{R} \cup \{-\infty, +\infty\}$ be an [extended real number](../../../Algebra/Extended%20Real%20Numbers.md) which is an [accumulation point](../../../Topology/Accumulation%20Points.md) of the [intersection](../../../Set%20Theory/Intersections.md) $\mathcal{D}_f \cap \mathcal{D}_g$.
>
>Then $f$ is [big Theta](./Big%20Theta%20Notation.md) of $g$ around $p$ if and only if $f$ is [big O](./Big%20O%20Notation.md) of $g$ and $g$ is [big O](./Big%20O%20Notation.md) of $f$ around $p$:
>
>$$f = \Theta(g) \iff f = O(g) \text{ and } g = O(f)$$
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>
>>- (1) If $f = \Theta (g)$, then $f = O(g)$ and $g = O(f)$.
>>- (2) $f = O(g)$ and $g = O(f)$, then $f = \Theta (g)$.
>>
>>
>>
>

>[!THEOREM] Theorem: Big Theta Notation via Limits
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../Real%20Functions/Real%20Functions.md) and let $p$ be a [limit point](../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) of $\mathcal{D}_f \cap \mathcal{D}_g$ or $p = \pm \infty$.
>
>If there exists a [deleted neighborhood](../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) $\mathcal{N}(p)$ such that $g(x) \ne 0$ on $\mathcal{N}(p) \cap \mathcal{D}_f \cap \mathcal{D}_g$ and the [limit](../Real%20Functions/Limits%20(Real%20Functions).md) of the absolute value of the ratio of $f$ and $g$ is strictly positive, then $f$ is [big Theta](#Big%20Theta%20Notation) of $g$ around $p$:
>
>$$\lim_{x \to p} \left|\frac{f(x)}{g(x)}\right| \in \mathbb{R}_{\gt 0} \implies f(x) = \Theta(g(x)) \text{ for } x\to p$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Sums in Big Theta Notation
>
>If $f_1$ and $f_2$ share the same sign around $p$ and $f_1$ is [Big Theta](#Big%20Theta%20Notation) of $g_1$ around $p$ and $f_2$ is [Big Theta](#Big%20Theta%20Notation) of $g_2$ around $p$, then $f_1 + f_2$ is [Big Theta](#Big%20Theta%20Notation) of $|g_1| + |g_2|$ around $p$:
>
>$$f_1 = \Theta(g_1) \text{ and } f_2 = \Theta(g_2) \implies f_1 + f_2 = \Theta(|g_1| + |g_2|)$$
>
>If $f_1$ and $f_2$ share the same sign around $p$, and $f_1$ is [Big Theta](#Big%20Theta%20Notation) of $g_1$ around $p$ and $f_2$ is [Big Theta](#Big%20Theta%20Notation) of $g_2$ around $p$, then $f_1 + f_2$ is [Big Theta](#Big%20Theta%20Notation) of $\max\{|g_1|, |g_2|\}$ around $p$:
>
>$$f_1 = \Theta(g_1) \text{ and } f_2 = \Theta(g_2) \implies f_1 + f_2 = \Theta(\max\{|g_1|, |g_2|\})$$
>
>If $f_1$ and $f_2$ share the same sign around $p$, and both are [Big Theta](#Big%20Theta%20Notation) of $g$ around $p$, then so is $f_1 + f_2$:
>
>$$f_1 = \Theta(g) \text{ and } f_2 = \Theta(g) \implies f_1 + f_2 = \Theta(g)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
