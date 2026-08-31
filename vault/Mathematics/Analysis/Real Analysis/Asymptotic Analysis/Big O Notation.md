---
tags:
    - real-analysis
    - asymptotic-analysis
    - analysis
    - mathematics
---

# Big O Notation

>[!DEFINITION] Definition: Big O Notation
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../Real%20Functions/Real%20Functions.md) and let $p \in \mathbb{R} \cup \{-\infty, +\infty\}$ be an [extended real number](../../../Algebra/Extended%20Real%20Numbers.md) which is an [accumulation point](../../../Topology/Accumulation%20Points.md) of the [intersection](../../../Set%20Theory/Intersections.md) $\mathcal{D}_f \cap \mathcal{D}_g$.
>
>We say that $f$ is **big O** of $g$ around $p$ if there exists some $C \in \mathbb{R}_{\gt 0}$ and some [deleted neighborhood](../../../Topology/Topological%20Spaces/Neighborhoods.md) $N$ of $p$ such that
>
>$$|f(x)| \le C |g(x)|$$
>
>for all $x \in N \cap \mathcal{D}_f \cap \mathcal{D}_g$.
>
>>[!NOTATION]
>>
>>$$f(x) = O(g(x)) \qquad \text{for} \qquad x\to p$$
>>
>>When $p$ can be inferred from context, we can omit $x \to p$. 
>>
>>We also use $O(g(x))$ to denote *any* [function](../Real%20Functions/Real%20Functions.md) $h$ for which $h(x) = O(g(x))$ holds.
>>
>
>>[!EXAMPLE]- Example: $x^3 + 3x^2  = O(x)$ for $x \to 0$
>>
>>Consider $f(x) = x^3 + 3x^2$ and $g(x) = x$. To show that
>>
>>$$f(x) = O(g(x))$$
>>
>>for $x \to 0$, we need to show that there exist some $C, \delta \gt 0$ such that
>>
>>$$|f(x)| \le C |g(x)|$$
>>
>>for all $x$ with $0 \lt |x| \lt \delta$. In other words, we need to show that there exist some $C, \delta \gt 0$ such that
>>
>>$$|x^3 + 3x^2| \le C |x|$$
>>
>>for all $x$ with $0 \lt |x| \lt \delta$. We have:
>>
>>$$|x^3 + 3x^2| = |x|\cdot|x^2 + 3x|$$
>>
>>We use the [triangle inequality](../../../Algebra/Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) for $|x^2 + 3x|$:
>>
>>$$|x^3 + 3x^2| = |x|\cdot|x^2 + 3x| \le |x| \cdot (|x^2| + |3x|) = |x| \cdot (|x|^2 + 3|x|)$$
>>
>>Let's see what happens for $\delta = 1$. We have $0 \lt |x| \lt 1$ and so $|x|^2 \lt 1$. From this, we get the following:
>>
>>$$|x|^2 + 3|x| \lt 1 + 3 = 4$$
>>
>>From $|x^3 + 3x^2| \le |x| \cdot (|x|^2 + 3|x|)$, we get:
>>
>>$$|x^3 + 3x^2| \le 4 \cdot |x|$$
>>
>>We have thus found $\delta = 1$ and $C = 4$.
>>
>

Intuitively, this means that, around $p$, the magnitude of $f$ is bounded by a constant multiple of the magnitude of $g$.

>[!THEOREM] Theorem: Big O Notation via Limit Superior
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../Real%20Functions/Real%20Functions.md) and let $p$ be a [limit point](../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) of $\mathcal{D}_f \cap \mathcal{D}_g$ or $p = \pm \infty$.
>
>If there exists a [deleted neighborhood](../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) $\mathcal{N}(p)$ such that $g(x) \ne 0$ on $\mathcal{N}(p) \cap \mathcal{D}_f \cap \mathcal{D}_g$, then $f$ is [Big O](#Big%20O%20Notation) of $g$ around $p$ if and only if the [limit superior](../Real%20Functions/Limits%20(Real%20Functions).md) of the absolute value of their ratio at $p$ is finite:
>
>$$f(x) = O(g(x)) \text{ for } x\to p \iff \limsup_{x \to p} \left|\frac{f(x)}{g(x)}\right| < \infty$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Big O Notation via Limits
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../Real%20Functions/Real%20Functions.md) and let $p$ be a [limit point](../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) of $\mathcal{D}_f \cap \mathcal{D}_g$ or $p = \pm \infty$.
>
>If there exists a [deleted neighborhood](../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) $\mathcal{N}(p)$ such that $g(x) \ne 0$ on $\mathcal{N}(p) \cap \mathcal{D}_f \cap \mathcal{D}_g$ and the [limit](../Real%20Functions/Limits%20(Real%20Functions).md) of the ratio of $f$ and $g$ is finite, then $f$ is [Big O](#Big%20O%20Notation) of $g$ around $p$:
>
>$$\lim_{x \to p} \frac{f(x)}{g(x)} \in \mathbb{R} \implies f(x) = O(g(x)) \text{ for } x\to p$$
>
>If $f$ is [big O](#Big%20O%20Notation) of $g$ around $p$, then the [limit](../Real%20Functions/Limits%20(Real%20Functions).md) of $f / g$ at $p$ cannot be [infinite](../Real%20Functions/Limits%20(Real%20Functions).md).
>
>>[!EXAMPLE]- Example: $x^m = O(x^n)$ for $x \to 0$ and all $n \le m$
>>
>>We want to prove the following:
>>
>>$$x^m = O(x^n)\qquad \text{for} \qquad x \to 0\qquad \forall n \le m$$
>>
>>For $n \lt m$, we have:
>>
>>$$\lim_{x \to 0} \frac{x^m}{x^n} = \lim_{x \to 0} x^{m-n} = 0$$
>>
>>For $n = m$, we have $x^m = O(x^m)$.
>>
>>
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: $f$ is Big O of $f$
>
>Every [function](../Real%20Functions/Real%20Functions.md) $f$ is [big O](./Bachmann-Landau%20Notation.md) of itself around every $p$:
>
>$$f = O(f)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Sums in Big O
>
>If $f_1$ is [big O](#Big%20O%20Notation) of $g_1$ around $p$ and $f_2$ is [big O](#Big%20O%20Notation) of $g_2$, then $f_1 + f_2$ is [big O](#Big%20O%20Notation) of $|g_1| + |g_2|$ around $p$:
>
>$$f_1 = O(g_1) \text{ and } f_2 = O(g_2) \implies f_1 + f_2 = O(|g_1| + |g_2|)$$
>
>If $f_1$ is [big O](#Big%20O%20Notation) of $g_1$ around $p$ and $f_2$ is [big O](#Big%20O%20Notation) of $g_2$, then $f_1 + f_2$ is [big O](#Big%20O%20Notation) of $\max\{|g_1|, |g_2|\}$ around $p$:
>
>$$f_1 = O(g_1) \text{ and } f_2 = O(g_2) \implies f_1 + f_2 = O(\max\{|g_1|, |g_2|\})$$
>
>If $f_1$ and $f_2$ are [big O](#Big%20O%20Notation) of $g$ around $p$, then so is $f_1 + f_2$:
>
>$$f_1 = O(g) \text{ and } f_2 = O(g) \implies f_1 + f_2 = O(g)$$
>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Arithmetic in Bachmann-Landau
>
>If $f_1$ and $f_2$ are [little O](./Bachmann-Landau%20Notation.md) of $g$ for $x \to p$, then so is $f_1 + f_2$:
>
>$$f_1 = o(g) \text{ and } f_2 = o(g) \implies f_1 + f_2 = o(g)$$
>
>If $f_1$ and $f_2$ are [big O](./Bachmann-Landau%20Notation.md) of $g$ for $x \to p$, then so is $f_1 + f_2$:
>
>$$f_1 = O(g) \text{ and } f_2 = O(g) \implies f_1 + f_2 = O(g)$$
>
>If $f_1$ is [big O](./Bachmann-Landau%20Notation.md) of $g_1$ for $x \to p$ and $f_2$ is [big O](./Bachmann-Landau%20Notation.md) of $g_2$ for $x \to p$, then $f_1 f_2$ is [big O](./Bachmann-Landau%20Notation.md) of $g_1g_2$:
>
>$$f_1 = O(g_1) \text{ and } f_2 = O(g_2) \implies f_1 f_2 = O(g_1 g_2)$$
>
>If $f_1$ is [big O](./Bachmann-Landau%20Notation.md) of $g_1$ for $x \to p$ and $f_2$ is [little O](./Bachmann-Landau%20Notation.md) of $g_2$ for $x \to p$, then $f_1 f_2$ is [little O](./Bachmann-Landau%20Notation.md) of $g_1 g_2$:
>
>$$f_1 = O(g_1) \text{ and } f_2 = o(g_2) \implies f_1f_2 = o(g_1g_2)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
