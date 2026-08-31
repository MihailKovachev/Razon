---
tags:
    - real-analysis
    - asymptotic-analysis
    - analysis
    - mathematics
---

# Master Theorem

>[!THEOREM] Master Theorem
>
>Let $f, T: [s, \infty) \subseteq \mathbb{R} \to \mathbb{R}$ be [real functions](../Real%20Functions/Real%20Functions.md) such that there exist some $a \ge 1$ and $b \gt 1$ with
>
>$$T(x) = a T\left( \frac{x}{b}\right) + f(x)$$
>
>for all $x \in [s, \infty)$.
>
>If there exists some $\varepsilon \gt 0$ such that $f(x)$ is [Big O](./Big%20O%20Notation.md) $x^{\log_b(a) - \varepsilon}$ for $x \to \infty$, then $T(x)$ is [big Theta](./Big%20Theta%20Notation.md) of $(x^{\log_b a})$ for $x \to \infty$:
>
>$$f(x) = O(x^{\log_b(a) - \varepsilon}) \qquad \text{for} \qquad x \to \infty \implies T(x) = \Theta (x^{\log_b a}) \qquad \text{for} \qquad x \to \infty$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
