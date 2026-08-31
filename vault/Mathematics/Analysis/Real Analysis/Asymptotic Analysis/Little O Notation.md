---
tags:
    - real-analysis
    - asymptotic-analysis
    - analysis
    - mathematics
---

# Little O Notation

>[!DEFINITION] Definition: Little O Notation
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../Real%20Functions/Real%20Functions.md) and let $p \in \mathbb{R} \cup \{-\infty, +\infty\}$ be an [extended real number](../../../Algebra/Extended%20Real%20Numbers.md) which is an [accumulation point](../../../Topology/Accumulation%20Points.md) of the [intersection](../../../Set%20Theory/Intersections.md) $\mathcal{D}_f \cap \mathcal{D}_g$.
>
>We say that $f$ is **little o** of $g$ around $p$ if, for every $\epsilon \in \mathbb{R}_{\gt 0}$, there exists some [deleted neighborhood](../../../Topology/Topological%20Spaces/Neighborhoods.md) $N$ of $p$ such that
>
>$$|f(x)| \le \epsilon |g(x)|$$
>
>for all $x \in N \cap \mathcal{D}_f \cap \mathcal{D}_g$.
>
>>[!NOTATION]
>>
>>$$f(x) = o(g(x)) \qquad \text{for} \qquad  x\to p$$
>>
>>When $p$ can be inferred from context, we can omit $x \to p$. 
>>
>>We also use $o(g(x))$ to denote *any* [function](../Real%20Functions/Real%20Functions.md) $h$ for which $h(x) = o(g(x))$ holds.
>>
>

Intuitively, this means that, around $p$, $f$ becomes insignificant in comparison to $g$.

>[!THEOREM] Theorem: Little O Notation via Limits
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../Real%20Functions/Real%20Functions.md) and let $p$ be a [limit point](../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) of $\mathcal{D}_f \cap \mathcal{D}_g$ or $p = \pm \infty$.
>
>If there exists a [deleted neighborhood](../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) $\mathcal{N}(p)$ such that $g(x) \ne 0$ on $\mathcal{N}(p) \cap \mathcal{D}_f \cap \mathcal{D}_g$, then $f$ is [little o](#Little%20o%20Notation) of $g$ around $p$ if and only if the [limit](../Real%20Functions/Limits%20(Real%20Functions).md) of their ratio at $p$ is zero:
>
>$$f(x) = o(g(x)) \text{ for } x\to p \iff \lim_{x \to p} \frac{f(x)}{g(x)} = 0$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Algebraic Manipulations in Little o Notation
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$, $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ and $h: \mathcal{D}_h \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../Real%20Functions/Real%20Functions.md) and let $p$ be a [limit point](../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) of $\mathcal{D}_f \cap \mathcal{D}_g \cap \mathcal{D}_h$ or $p = \pm \infty$.
>
>Then $f(x) + g(x)$ is [little o](#Little%20o%20Notation) of $h(x)$ for $x \to p$ if and only if there exists some [real function](../Real%20Functions/Real%20Functions.md) which is [little o](#Little%20o%20Notation) of $h(x)$ for $x \to p$ and whose sum with $-g$ is $f$:
>
>$$f(x) + g(x) = o(h(x)) \text{ for } x \to p \iff f(x) = -g(x) + o(h(x)) \text{ for } x \to p$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Little O $\implies$ Big O
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../Real%20Functions/Real%20Functions.md) and let $p \in \mathbb{R}$ be a [limit point](../../../Topology/Accumulation%20Points.md) of $\mathcal{D}_f \cap \mathcal{D}_g$ or $p \in \{-\infty, +\infty\}$.
>
>If $f$ is [little o](#Little%20O%20Notation) of $g$ around $p$, then $f$ is also [big O](./Big%20O%20Notation.md) of $g$ around $p$:
>
>$$f = o(g) \text{ around } p \implies f = O(g) \text{ around } p$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!DEFINITION] Definition: Little O Notation (Real Scalar Fields)
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R}^n \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R}^n \to \mathbb{R}$ be [real scalar fields](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) and let $\boldsymbol{p} \in \mathbb{R}^n$ be a [limit point](../../../Topology/Accumulation%20Points.md) of $\mathcal{D}_f \cap \mathcal{D}_g$.
>
>We say that $f$ is **little o** of $g$ around $\boldsymbol{p}$ if for each $\varepsilon \gt 0$, there exists a [deleted neighborhood](../Euclidean%20Space/Euclidean%20Space.md#The%20Topology%20of%20the%20Real%20Number%20Line) $\mathcal{N}(\boldsymbol{p})$ such that
>
>$$|f(\boldsymbol{x})| \le \varepsilon |g(\boldsymbol{x})|$$
>
>for all $\boldsymbol{x} \in \mathcal{N}(\boldsymbol{p}) \cap \mathcal{D}_f \cap \mathcal{D}_g$.
>
>>[!NOTATION]
>>
>>$$f(\boldsymbol{x}) = o(g(\boldsymbol{x})) \qquad \text{for} \qquad  \boldsymbol{x}\to \boldsymbol{p}$$
>>
>>When $\boldsymbol{p}$ can be inferred from context, we can omit $\boldsymbol{x} \to \boldsymbol{p}$. 
>>
>>We also use $o(g(\boldsymbol{x}))$ to denote *any* [real scalar field](../Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md)$h$ for which $h(\boldsymbol{x}) = o(g(\boldsymbol{x}))$ holds.
>>
>