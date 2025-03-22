---
title: Continuity of Real Functions
tags:
  - continuity
  - real-functions
  - real-analysis
  - analysis
  - mathematics
---

# Continuity

>[!DEFINITION] Definition: Continuity of Real Functions
>
>A [real function](Real%20Functions.md) $f: D \subseteq \mathbb{R} \to \mathbb{R}$ is **continuous at** $c \in D$ if its [limit](Limits/Limits%20of%20Real%20Functions.md) as $x$ approaches $c$ is exists and is equal to its value for $c$:
>
>$$
>\lim_{x \to c} f(x) = f(c)
>$$
>
>If $f$ is continuous at every $c \in S \subseteq D$, then we say that $f$ is **continuous on** $S$. If $S = D$, then we simply say that $f$ is **continuous**.
>

# Properties

>[!THEOREM] Theorem: Operations with Continuous Functions
>
>If $f,g: D \subseteq\mathbb{R} \to \mathbb{R}$ are two [continuous functions](Continuity.md), then so are
>- $\alpha f + \beta g$ for all $\alpha,\beta \in \mathbb{R}$;
>- $f \cdot g$;
>- $f / g$ provided that $g(x) \ne 0$ for all $x \in D$;
>- $f \circ g$ provided that $g(D) \subseteq D$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] The Extreme Value Theorem
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be a [real-valued function](../Real-Valued%20Function.md) on a closed interval $D = [a;b]$.
>
>If $f$ is [continuous](Real%20Functions.md) on $D$, then there exist at least one $x_{\text{of min}} \in D$ and at least one $x_{\text{of max}} \in D$ such that
>
>$$
>f(x_{\text{of min}}) \le f(x) \le f(x_{\text{of max}}) \qquad \forall x \in D
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
>Let $f: D \subset \mathbb{R} \to \mathbb{R}$ be a [real function](Real%20Functions.md) on a closed interval $D = [a;b]$.
>
>If $f$ is [continuous](Real%20Functions.md) on $D$, then for every $y$ between $f(a)$ and $f(b)$, i.e. $\min\{f(a), f(b)\} \le y \le \max\{f(a), f(b)\}$, there exists an $x \in D$ such that $f(x) = y$.
>
>>[!INTUITION]
>>
>>The theorem says that if a function is continuous on a closed interval, then it must generate all values between the values on the interval's endpoints.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Bolzano's Theorem
>
>Let $f: D \subset \mathbb{R} \to \mathbb{R}$ be a [real function](Real%20Functions.md) on a closed interval $D = [a;b]$.
>
>If $f$ is [continuous](Real%20Functions.md) on $D$ and $f(a) \lt 0$ and $f(b) \gt 0$ (or vice-versa), then there exists at least one $x \in D$ such that $f(x) = 0$.
>
>>[!PROOF]-
>>
>>This is just a special case of the intermediate value theorem.
>>
>

>[!THEOREM] Theorem: Integrability of Continuous Functions
>
>Let $f$ be a [real function](Real%20Functions.md) on a [closed interval](../../../../../Set%20Theory/Ordering/Intervals.md).
>
>If $f$ is [continuous](Real%20Functions.md), then it is also [Riemann-integrable](Integration/Definite%20Integrals.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

