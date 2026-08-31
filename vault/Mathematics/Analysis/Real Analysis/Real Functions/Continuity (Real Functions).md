---
tags:
    - real-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Continuity (Real Functions)

>[!DEFINITION] Definition: Continuity of Real Functions
>
>A [real function](./Real%20Functions.md) $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ is [continuous](../../Continuity/Continuity.md) at $c \in \mathbb{R}$ if and only if $f$'s [limit](./Limits%20(Real%20Functions.md#Real%20Limits) at $c$ is equal to $f(c)$:
>
>$$
>\lim_{x \to c} f(x) = f(c)
>$$
>
>If $f$ is [continuous](./Continuity%20(Real%20Functions).md) at every $c \in S \subseteq \mathcal{D}$, then we say that $f$ is **continuous on** $S$. If $S = \mathcal{D}$, then we simply say that $f$ is **continuous**.
>
>>[!EXAMPLE]- Example: $\frac{(x-1)(x+3)}{x - 2}$
>>
>>The [function](./Real%20Functions.md) $f: \mathbb{R} \setminus \{2\} \to \mathbb{R}$ defined as
>>
>>$$
>>f(x) = \frac{(x-1)(x+3)}{x - 2}
>>$$
>>
>>*is* [continuous](./Continuity%20(Real%20Functions).md). We do not require that $\lim_{x \to 2} f(x) = f(2)$, since $f$ is not defined for $x = 2$.
>>
>
>>[!EXAMPLE]- Example: Polynomial Functions
>>
>>All [real polynomial functions](./Real%20Polynomial%20Functions.md) are [continuous](./Continuity%20(Real%20Functions).md) on all of $\mathbb{R}$.
>>
>
>>[!EXAMPLE]- Example: Exponential Function
>>
>>The [real exponential function](./Real%20Exponentiation.md#The%20Real%20Exponential%20Function) is [continuous](./Continuity%20(Real%20Functions).md) on all of $\mathbb{R}$..
>>
>
>>[!EXAMPLE]- Example: Trigonometric Functions
>>
>>All [real trigonometric functions](./Real%20Trigonometric%20Functions/Real%20Trigonometric%20Functions.md) are [continuous](./Continuity%20(Real%20Functions).md) (of course, only where they are defined).
>>
>

>[!THEOREM] Theorem: Operations with Continuous Functions
>
>Let $f: \mathcal{D}_f \subseteq \mathbb{R} \to \mathbb{R}$ and $g: \mathcal{D}_g \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](./Real%20Functions.md) and let $c \in \mathbb{R}$.
>
>If $f$ and $g$ are [continuous](./Continuity%20(Real%20Functions).md) at $c$, then so are:
>- $\alpha f + \beta g$ for all $\alpha,\beta \in \mathbb{R}$;
>- $f \cdot g$;
>- $f / g$ provided that $g(c) \ne 0$;
>- $f \circ g$ provided that $g(\mathcal{D}_g) \subseteq \mathcal{D}_f$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] The Extreme Value Theorem
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $[a;b] \subseteq \mathcal{D}$ be a [closed interval](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line).
>
>If $f$ is [continuous](./Continuity%20(Real%20Functions).md) on $[a;b]$, then there exist at least one $x_{\text{of min}} \in [a;b]$ and at least one $x_{\text{of max}} \in [a;b]$ such that
>
>$$
>f(x_{\text{of min}}) \le f(x) \le f(x_{\text{of max}}) \qquad \forall x \in [a;b]
>$$
>
>>[!INTUITION]
>>
>>This theorem says that if a function is continuous on a closed interval, then it has a minimum and a maximum value on it.
>>
>
>TODO: Add diagram
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] The Intermediate Value Theorem
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $[a;b] \subseteq \mathcal{D}$ be a [closed interval](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line).
>
>If $f$ is [continuous](./Continuity%20(Real%20Functions).md) on $[a;b]$, then for each $y \in (\min\{f(a), f(b)\}; \max\{f(a), f(b)\})$, there exists at least one $x \in [a;b]$ such that $f(x) = y$.
>
>>[!INTUITION]
>>
>>The theorem says that if a function is continuous on a closed interval, then it must generate all values between its minimum and maximum value on said interval.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Bolzano's Theorem
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $[a;b] \subseteq \mathcal{D}$ be a [closed interval](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line).
>
>If $f$ is [continuous](./Continuity%20(Real%20Functions).md) on $[a;b]$ and $f(a) \cdot f(b) \lt 0$, then there exists at least one $x \in (a;b)$ such that $f(x) = 0$.
>
>>[!PROOF]-
>>
>>This is just a special case of the intermediate value theorem.
>>
>

>[!THEOREM] Theorem: Fixed-Point Theorem
>
>Let $[a;b] \subset \mathbb{R}$ be a [closed interval](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) and let $f: [a; b] \to [a;b]$ be a [real function](./Real%20Functions.md).
>
>If $f$ is [continuous](./Continuity%20(Real%20Functions).md), then there exists at least one $\xi \in [a;b]$ with $f(\xi) = \xi$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Riemann Integrability of Continuous Functions
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md), let $[a, b] \subseteq \mathcal{D}$ be a [closed interval](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) and let $X \subseteq [a,b]$ be the [set](../../../Set%20Theory/Sets.md) of all $x \in [a;b]$ at which $f$ is [discontinuous](./Continuity%20(Real%20Functions).md).
>
>If $f$ is [bounded](./Boundedness%20of%20Real%20Functions.md) on $[a,b]$ and $X$ has [Lebesgue measure](../Lebesgue%20Integral.md#Lebesgue%20Measure) zero, then $f$ is [Riemann-integrable](./Integration/Riemann%20Integrals%20(Real%20Functions).md) on $[a,b]$.
>
>>[!TIP] Tip: Continuity $\implies$ Riemann-Integrability
>>
>>A direct consequence of this is that if $f$ is [continuous](./Continuity%20(Real%20Functions).md) on $[a,b]$, then it is also [Riemann-integrable](./Integration/Riemann%20Integrals%20(Real%20Functions).md) on $[a,b]$.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antidifferentiability of Continuous Function
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
>
>If $f$ is [continuous](./Continuity%20(Real%20Functions).md) on $S \subseteq \mathcal{D}$, then it is also [antidifferentiable](./Antidifferentiability%20(Real%20Functions).md) on $S$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Continuous Extension

>[!DEFINITION] Definition: Continuous Extension
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and $p \in \mathbb{R}$ be a [limit point](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of $\mathcal{D}$.
>
>A **continuous extension** of $f$ at $p$ is any [real function](./Real%20Functions.md) $\tilde{f}: \mathcal{D} \cup \{p\} \to \mathbb{R}$ which is [continuous](./Continuity%20(Real%20Functions).md) at $p$ with $\tilde{f}(x) = f(x)$ for all $x \in \mathcal{D} \setminus \{p\}$.
>