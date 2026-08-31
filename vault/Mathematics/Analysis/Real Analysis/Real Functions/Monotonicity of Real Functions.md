---
tags:
  - real-mathematical-analysis
  - mathematical-analysis
  - mathematics
---

# Monotonicity of Real Functions

>[!DEFINITION] Definition: Monotonicity
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $S \subseteq \mathcal{D}$.
>
>We say that $f$ is:
>- **increasing** on $S$ if $x_1 \lt x_2 \implies f(x_1) \le f(x_2)$ for all $x_1, x_2 \in S$;
>- **strictly increasing** on $S$ if $x_1 \lt x_2 \implies f(x_1) \lt f(x_2)$ for all $x_1, x_2 \in S$;
>- **decreasing** on $S$ if $x_1 \lt x_2 \implies f(x_1) \ge f(x_2)$ for all $x_1, x_2 \in S$;
>- **strictly decreasing** on $S$ if $x_1 \lt x_2 \implies f(x_1) \gt f(x_2)$ for all $x_1, x_2 \in S$.
>
>In any of the above four cases, we also say that $f$ is **monotone**.
>
>If $S = \mathcal{D}$, then we can omit the "on $S$" part.
>

>[!THEOREM] Theorem: Monotonicity Criteria
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $[a;b] \subseteq \mathcal{D}$ be a [closed interval](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line).
>
>If $f$ is [continuous](./Continuity%20(Real%20Functions).md) on $[a;b]$ and [differentiable](./Differentiability%20(Real%20Functions).md) on the [open interval](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) $(a;b)$, then:
>
>- $f$ is [increasing](./Monotonicity%20of%20Real%20Functions.md) on $[a;b]$ if and only if $f'(x) \ge 0$ for all $x \in (a;b)$;
>- $f$ is [decreasing](./Monotonicity%20of%20Real%20Functions.md) on $[a;b]$ if and only if $f'(x) \le 0$ for all $x \in (a;b)$;
>- $f$ is [strictly increasing](./Monotonicity%20of%20Real%20Functions.md) on $[a;b]$ if $f'(x) \gt 0$ for all $x \in (a;b)$;
>- $f$ is [strictly decreasing](./Monotonicity%20of%20Real%20Functions.md) on $[a;b]$ if $f'(x) \lt 0$ for all $x \in (a;b)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Invertibility of Strictly Monotone Functions
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
>
>If $f$ is [strictly monotone](./Monotonicity%20of%20Real%20Functions.md), then $f$ is [injective](../../Functions/Injections,%20Surjections%20and%20Bijections.md#Injections). Moreover:
>- If $f$ is [strictly increasing](./Monotonicity%20of%20Real%20Functions.md), then its [inverse](../../Functions/Injections,%20Surjections%20and%20Bijections.md#Injections) $f^{-1}: f(\mathcal{D}) \to \mathcal{D}$ is also [strictly increasing](./Monotonicity%20of%20Real%20Functions.md).
>- If $f$ is [strictly decreasing](./Monotonicity%20of%20Real%20Functions.md), then its [inverse](../../Functions/Injections,%20Surjections%20and%20Bijections.md#Injections) $f^{-1}: f(\mathcal{D}) \to \mathcal{D}$ is also [strictly decreasing](./Monotonicity%20of%20Real%20Functions.md).
>- If $f$ is [continuous](./Continuity%20(Real%20Functions).md) and $\mathcal{D}$ is an [interval](../Euclidean%20Space/Euclidean%20Space.md), then its [inverse](../../Functions/Injections,%20Surjections%20and%20Bijections.md#Injections) $f^{-1}: f(\mathcal{D}) \to \mathcal{D}$ is also [continuous](./Continuity%20(Real%20Functions).md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Riemann-Integrability of Monotone Functions
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
>
>If $f$ is [monotone](./Monotonicity%20of%20Real%20Functions.md) on a [closed interval](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) $[a,b] \subseteq \mathcal{D}$, then $f$ is also [Riemann-integrable](./Integration/Riemann%20Integrals%20(Real%20Functions).md) on $[a, b]$.
>
>>[!PROOF]-
>>
>>TODO
>>
>