---
tags:
  - complex-analysis
  - analysis
  - mathematics
---

# Limits (Complex Functions)

>[!DEFINITION] Definition: Limit (Complex Function)
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](./Complex%20Functions.md) and let $p \in \mathbb{C}$ be an [accumulation point](../../../Topology/Accumulation%20Points.md) of $\mathcal{D}$.
>
>A **limit** of $f$ at $p$ is any [complex number](../../../Algebra/Fields/The%20Complex%20Numbers/Complex%20Numbers.md) $L \in \mathbb{C}$ such that for each $\varepsilon \gt 0$, there exists some $\delta \gt 0$ with
>
>$$0 \lt |z - p| \lt \delta \implies |f(z) - L| \lt \varepsilon$$
>
>for all $z \in \mathcal{D}$.
>
>>[!NOTATION]
>>
>>$$f(z) \overset{z \to p}{\to} L \qquad \lim_{z \to p} f(z) = L$$
>>
>

>[!DEFINITION] Definition: Limit of a Complex Function
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](./Complex%20Functions.md) and let $c \in \mathbb{C}$ be an [accumulation point](../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}$.
>
>We say that $L$ is the **limit** of $f$ as $z$ approaches $c$ if for each $\varepsilon \gt 0$ there exists some $\delta \gt 0$ such that
>
>$$
>0 \lt |z - c| \lt \delta \implies |f(z) - L| \lt \varepsilon
>$$
>
>for all $z \in \mathcal{D}$.
>
>>[!NOTATION]
>>
>>Most commonly, the limit is denoted by
>>
>>$$
>>\lim_{z \to c} f(z) = L \qquad 
>>$$
>>
>>In text, one also writes "$f(z) \to L$ as $z \to c$". Sometimes, one might also encounter $f(z) \underset{z \to c}{\longrightarrow} L$ and $f(z) \overset{z \to c}{\longrightarrow} L$.
>>
>
>>[!DEFINITION] Definition: Limit at Infinity
>>
>>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](./Complex%20Functions.md) such that $\mathcal{D}$ is the [complement](../../../Set%20Theory/Sets.md#Operations) of some [open ball](../Complex%20Euclidean%20Topology.md) in $\mathbb{C}$ centered at zero.
>>
>>We say that $L \in \mathbb{C}$ is the **limit** of $f$ for $z \to \infty$ if for each $\varepsilon \gt 0$ there exists some $R \gt 0$ such that
>>
>>$$
>>|z| \gt R \implies |f(z) - L| \lt \varepsilon 
>>$$
>>
>>for all $z \in \mathcal{D}$.
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\lim_{z \to \infty} f(z) = L
>>>$$
>>>
>>
>

>[!THEOREM] Theorem: Uniqueness of the Limit
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](./Complex%20Functions.md) and let $c \in \mathbb{C}$ be an [accumulation point](../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}$ or $c = \infty$.
>
>If the [limit](#Complex%20Limits) of $f$ exists at $c$, then it is unique:
>
>$$
>\lim_{z \to c} f(z) = L \in \mathbb{C} \qquad \text{ and } \qquad \lim_{z \to c} f(z) = M \in \mathbb{C} \implies L = M
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Complex Limits via Absolute Value
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](./Complex%20Functions.md) and let $c \in \mathbb{C}$ be an [accumulation point](../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}$.
>
>A number $L \in \mathbb{C}$ is the [limit](./Limits%20(Complex%20Functions.md) of $f$ for $z \to c$ if and only if
>
>$$
>\lim_{z \to c} |f(z) - L| = 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Component-wise Limits
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](./Complex%20Functions.md) and let $c \in \mathbb{C}$ be an [accumulation point](../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}$.
>
>The [limit](./Limits%20(Complex%20Functions.md) of $f$ at $c$ is $L \in \mathbb{C}$ if and only if the [limit](../../Real%20Analysis/Real%20Functions/Limits%20(Real%20Functions.md) of $f$'s [real part](../Complex-Valued%20Functions.md) is $\operatorname{Re} (L)$ and the [limit](../../Real%20Analysis/Real%20Functions/Limits%20(Real%20Functions.md) of its [imaginary part](../Complex-Valued%20Functions.md) if $\operatorname{Im} (L)$:
>
>$$
>\lim_{z \to c} f(z) = L \iff \lim_{z \to c} \operatorname{Re} f (z) = \operatorname{Re} (L) \qquad \text{and} \qquad \lim_{z \to c}\operatorname{Im} f (z) = \operatorname{Im} (L)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Operations with Limits
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{C} \to \mathbb{C}$ and $g: \mathcal{D}_g \subseteq \mathbb{C} \to \mathbb{C}$ be [complex functions](./Complex%20Functions.md) and let $c \in \mathbb{C}$ be an [accumulation point](../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}_f \cap \mathcal{D}_g$.
>
>If the [limits](#Complex%20Limits) of $f$ and $g$ exist at $c$, then
>
>$$
>\lim_{z\to c} \left( \alpha f(z) + \beta g(z) \right) = \alpha \lim_{z \to c} f(z) + \beta \lim_{z \to c} g(z) \qquad \forall \alpha, \beta \in \mathbb{C}
>$$
>
>Moreover, if there also exists some [open ball](../Complex%20Euclidean%20Topology.md) around $c$ on which $f$ and $g$ are [bounded](../Boundedness%20of%20Complex%20Functions.md), then
>
>$$
>\begin{aligned}
>
>&\lim_{z \to c} \left(f(z) g(z)\right) = \left(\lim_{z \to c} f(z)\right) \cdot \left(\lim_{z \to c} g(z)\right) \\
>
>\\
>
>&\lim_{z \to c} \frac{f(z)}{g(z)} = \frac{\displaystyle \lim_{z \to c} f(z)}{\displaystyle \lim_{z \to c} g(z)}, \qquad \text{ provided that } \lim_{z \to c} g(z) \ne 0
>
>\end{aligned}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Squeeze Theorem
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{C} \to \mathbb{C}$ and $g: \mathcal{D}_g \subseteq \mathbb{C} \to \mathbb{C}$ be [complex functions](./Complex%20Functions.md) and let $c \in \mathbb{C}$ be an [accumulation point](../../../Topology/Interior,%20Boundary,%20Exterior.md) of $\mathcal{D}_f \cap \mathcal{D}_g$.
>
>If there exists some [deleted neighborhood](../Complex%20Euclidean%20Topology.md) $N$ of $c$ such that $|g(z)| \le |f(z)|$ for all $z \in N$ and $\lim_{z \to c} f(z) = 0$, then $\lim_{z \to c} g(z) = 0$.
>
>If there exists some [deleted neighborhood](../Complex%20Euclidean%20Topology.md) $N$ of $c$ on which $g$ is [bounded](../Boundedness%20of%20Complex%20Functions.md) and $\lim_{z \to c} f(z) = 0$, then $\lim_{z \to c} (f(z) \cdot g(z)) = 0$.
>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](./Complex%20Functions.md) such that $\mathcal{D}$ is the [complement](../../../Set%20Theory/Sets.md#Operations) of some [open ball](../Complex%20Euclidean%20Topology.md) in $\mathbb{C}$ centered at zero.
>
>The [limit](#Complex%20Limits) of $f$ for $z \to \infty$ is $L \in \mathbb{C}$ if and only if the [limit](#Complex%20Limits) of $|f(z) - L|$ for $|z| \to \infty$ is zero.
>
>$$
>\lim_{z \to \infty} f(z) = L \iff \lim_{|z| \to \infty} |f(z) - L| = 0
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Limit $\leftrightarrow$ Limit at Infinity
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](./Complex%20Functions.md) such that $\mathcal{D}$ is the [complement](../../../Set%20Theory/Sets.md#Operations) of some [open ball](../Complex%20Euclidean%20Topology.md) in $\mathbb{C}$ centered at zero.
>
>The [limit](#Complex%20Limits) of $f$ for $z \to \infty$ is equal to $L \in \mathbb{C}$ if and only if the [limit](#Complex%20Limits) of $f\left(\frac{1}{z}\right)$ for $z \to 0$ is $L$.
>
>$$
>\lim_{z \to \infty} f(z) = L \iff \lim_{z \to 0} f \left( \frac{1}{z} \right) = L
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Infinite Limits

>[!DEFINITION] Definition: Infinite Limits
>
>Let $c \in \mathbb{C}$ and let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](./Complex%20Functions.md) defined on some [deleted neighborhood](../Complex%20Euclidean%20Topology.md) $\mathcal{D}$ of $c$.
>
>We say that $f$ has an **infinite limit** at $c$ if for each $M \gt 0$, there exists some $\delta \gt 0$ such that
>
>$$
>0 \lt |z - c| \lt \delta \implies |f(z)| \gt M
>$$
>
>for all $z \in \mathcal{D}$.
>
>>[!NOTATION]
>>
>>$$
>>\lim_{z \to c} f(z) = \infty
>>$$
>>
>
>>[!DEFINITION] Definition: Infinite Limits at Infinity
>>
>>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](./Complex%20Functions.md) such that $\mathcal{D}$ is the [complement](../../../Set%20Theory/Sets.md#Operations) of some [open ball](../Complex%20Euclidean%20Topology.md) in $\mathbb{C}$ centered at zero.
>>
>>We say that $f$ has an **infinite limit** for $z \to \infty$ if for each $M \gt 0$ there exists some $R \gt 0$ such that
>>
>>$$
>>|z| \gt R \implies |f(z)| \gt M
>>$$
>>
>>for all $z \in \mathcal{D}$.
>>
>>>[!NOTATION]
>>>
>>>$$
>>>\lim_{z \to \infty} f(z) = \infty
>>>$$
>>>
>>
>

>[!WARNING]
>
>Even though we use limit notation for infinite limits and infinite limits at infinity, we never say that these limits *exist*, since they are not complex numbers.
>

>[!THEOREM] Theorem
>
>Let $c \in \mathbb{C}$ and let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](./Complex%20Functions.md) defined on some [deleted neighborhood](../Complex%20Euclidean%20Topology.md) $\mathcal{D}$ of $c$.
>
>The [limit](#Infinite%20Limits) of $f$ for $z \to c$ is $\infty$ if and only if the [limit](../../Real%20Analysis/Real%20Functions/Limits%20(Real%20Functions.md#Infinite%20Limits) of $|f|$ for $z \to c$ is $\infty$.
>
>$$
>\lim_{z \to c} f(z) = \infty \iff \lim_{z \to c} |f(z)| = \infty
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](./Complex%20Functions.md) such that $\mathcal{D}$ is the [complement](../../../Set%20Theory/Sets.md#Operations) of some [open ball](../Complex%20Euclidean%20Topology.md) in $\mathbb{C}$ centered at zero.
>
>The [limit](#Infinite%20Limits) of $f$ for $z \to \infty$ is $\infty$ if and only if the [limit](#Infinite%20Limits) of $|f|$ for $|z| \to \infty$ is $\infty$.
>
>$$
>\lim_{z \to \infty} f(z) = \infty \iff \lim_{|z| \to \infty } |f(z)| = \infty
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Infinite Limit $\leftrightarrow$ Infinite Limit at Infinity
>
>Let $f: \mathcal{D} \subseteq \mathbb{C} \to \mathbb{C}$ be a [complex function](./Complex%20Functions.md) such that $\mathcal{D}$ is the [complement](../../../Set%20Theory/Sets.md#Operations) of some [open ball](../Complex%20Euclidean%20Topology.md) in $\mathbb{C}$ centered at zero.
>
>The [limit](#Infinite%20Limits) of $f$ for $z \to \infty$ is $\infty$ if and only if the [limit](#Infinite%20Limits) of $f\left( \frac{1}{z} \right)$ for $z \to 0$ is $\infty$.
>
>$$
>\lim_{z \to \infty} f(z) = \infty \iff \lim_{z \to 0} f\left( \frac{1}{z} \right) = \infty
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Common Limits
>
>Following are some [limits](./Limits%20(Complex%20Functions.md) for [complex functions](./Complex%20Functions.md):
>
>$$
>\begin{aligned}
>
>&\lim_{z \to c} \lambda = \lambda \qquad \lambda, c \in \mathbb{C} \\
>
>&\lim_{z \to \infty} \frac{1}{z^n} = 0 \qquad \forall n \in \mathbb{N}
>
>\end{aligned}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

# Sources

1. N. H. Asmar, L. Grafakos, "Analytic Functions," in *Complex Analysis with Applications*, Columbia, USA: Springer, 2018