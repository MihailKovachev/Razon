---
tags:
  - real-mathematical-analysis
  - mathematical-analysis
  - mathematics
---

# Concavity and Convexity of Real Functions

## Concavity

>[!DEFINITION] Definition: Concave
>
>A [real function](./Real%20Functions.md) $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ is **concave** on an [interval](../Euclidean%20Space/Euclidean%20Space.md) $I \subseteq \mathcal{D}$ if
>
>$$
>f(\lambda c + (1-\lambda)d) \ge \lambda f(c) + (1-\lambda)f(d) 
>$$
>
>for all $\lambda \in [0; 1]$ and all $c, d \in I$.
>
>We say that $f$ is **strictly concave** if we can replace $\ge$ with $\gt$.
>

Geometrically, the [graph](./Real%20Functions.md) of a [concave](#Concavity) [function](./Real%20Functions.md) always lies above any secant line:

![Concave Function Graph](./res/Concave%20Function%20Graph.svg)

>[!THEOREM] Theorem: Concavity via Differentiation
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
>
>If $f$ is [continuous](./Continuity%20(Real%20Functions).md) on a [closed interval](../Euclidean%20Space/Euclidean%20Space.md) $[a;b]$ and [twice continuously differentiable](./Differentiability%20(Real%20Functions).md) on the [open interval](../Euclidean%20Space/Euclidean%20Space.md) $(a;b)$, then it is [concave](#Concave) on $[a;b]$ if and only if
>
>$$
>f''(x) \le 0 \qquad \forall x \in (a;b)
>$$
>
>and it is [strictly concave](#Concave) if
>
>$$
>f''(x) \lt 0 \qquad \forall x \in (a;b).
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Convexity

>[!DEFINITION] Definition: Convexity
>
>A [real function](./Real%20Functions.md) $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ is **convex** on a [closed interval](../Euclidean%20Space/Euclidean%20Space.md) $[a;b] \subseteq \mathcal{D}$ if
>
>$$
>f(\lambda c + (1-\lambda)d) \le \lambda f(c) + (1-\lambda)f(d) 
>$$
>
>for all $\lambda \in [0;1]$ and all $c, d \in I$.
>
>We say that $f$ is **strictly convex** if we can replace $\le$ with $\lt$.
>

Geometrically, the [graph](./Real%20Functions.md) of a [convex](#Convexity) [function](./Real%20Functions.md) always lies below any secant line:

![Convex Function Graph](./res/Convex%20Function%20Graph.svg)

>[!THEOREM] Theorem: Convexity via Differentiation
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
>
>If $f$ is [continuous](./Continuity%20(Real%20Functions).md) on a [closed interval](../Euclidean%20Space/Euclidean%20Space.md) $[a;b]$ and [twice continuously differentiable](./Differentiability%20(Real%20Functions).md) on the [open interval](../Euclidean%20Space/Euclidean%20Space.md) $(a;b)$, then it is [convex](#Convexity) on $[a;b]$ if and only if
>
>$$
>f''(x) \ge 0 \qquad x \in (a;b)
>$$
>
>and it is [strictly convex](#Convexity) if
>
>$$
>f''(x) \gt 0 \qquad x \in (a;b)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!EXAMPLE]- Example: $x^2$
>>
>>The [function](./Real%20Functions.md) $f: \mathbb{R} \to \mathbb{R}$ defined as
>>
>>$$
>>f(x) = x^2
>>$$
>>
>>is [strictly convex](#Convexity) on all [closed intervals](../Euclidean%20Space/Euclidean%20Space.md) $[a;b]$ because
>>
>>$$
>>f''(x) = 2
>>$$
>>
>>and so
>>
>>$$
>>f''(x) \gt 0
>>$$
>>
>>for all $x \in (a;b)$.
>>
>
>>[!EXAMPLE]- Example: $\mathrm{e}^x$
>>
>>The [real exponential function](./Real%20Exponentiation.md#The%20Real%20Exponential%20Function) is [strictly convex](#Convexity) on all [closed intervals](../Euclidean%20Space/Euclidean%20Space.md) $[a;b]$ because
>>
>>$$
>>(\mathrm{e}^x)'' = \mathrm{e}^x
>>$$
>>
>>and $\mathrm{e}^x \gt 0$ for all $x \in \mathbb{R}$.
>>
>

## Inflection Points

>[!DEFINITION] Definition: Inflection Point
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ and let $p \in \mathcal{D}$.
>
>We say that $(p, f(p))$ is an **inflection point** of $f$ if there exists some $\varepsilon \gt 0$ such that $f$ is [convex](#Convexity) on $(p-\varepsilon; p)$ and [concave](#Concavity) on $(p; p + \varepsilon)$ or vice versa.
>

>[!THEOREM] Theorem: Inflection Points and Second Derivative
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $p \in \mathcal{D}$.
>
>If $f$ has an [inflection point](#Inflection%20Points) at $p$, is [differentiable](./Differentiability%20(Real%20Functions).md) on some [open neighborhood](../Euclidean%20Space/Euclidean%20Space.md) of $p$ and is [twice differentiable](./Differentiability%20(Real%20Functions).md) at $p$, then $f''(p) = 0$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Second-Order Derivative Test for Inflection Points
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $p \in \mathcal{D}$.
>
>If $f$ is [twice continuously differentiable](./Differentiability%20(Real%20Functions).md) on some [open neighborhood](../Euclidean%20Space/Euclidean%20Space.md) of $p$ with $f''(p) = 0$ and there exists some $\varepsilon \gt 0$ such that $f''(x_1) \cdot f''(x_2) \lt 0$ for all $x_1 \in (p - \varepsilon; p)$ and all $x_2 \in (p; p + \varepsilon)$, then $f$ has an [inflection point](#Inflection%20Points) at $p$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Higher-Order Derivative Test for Inflection Points
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md), let $p \in \mathcal{D}$.
>
>Suppose $f$ is $(n-1)$[-times differentiable](./Differentiability%20(Real%20Functions).md) $(n \ge 3)$ on some [open neighborhood](../Euclidean%20Space/Euclidean%20Space.md) of $p$ and is $n$[-times differentiable](./Differentiability%20(Real%20Functions).md) at $p$.
>
>If $f^{(k)}(p) = 0$ for all $2 \leq k < n$ and $f^{(n)}(p) \neq 0$, and if $n$ is odd, then $f$ has an [inflection point](#Inflection%20Points) at $p$.
>
>>[!PROOF]-
>>
>>TODO
>>
>