---
tags:
  - real-analysis
  - mathematical-analysis
  - mathematics
---

# Extrema of Real Functions

## Local Extrema

>[!DEFINITION] Definition: Local Minimum
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
> 
>We say that $f$ **has a local minimum at** $p \in \mathcal{D}$ if there exists some [open neighborhood](../Euclidean%20Space/Euclidean%20Space.md) $N(p)$ such that
>
>$$f(p) \le f(x) \qquad \forall x \in N(p)$$
>
>This **local minimum** is $f(p)$.

>[!DEFINITION] Definition: Local Maximum
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
> 
>We say that $f$ **has a local maximum at** $p \in \mathcal{D}$ if there exists some [open neighborhood](../Euclidean%20Space/Euclidean%20Space.md) $N(p)$ such that
>
>$$
>f(p) \ge f(x) \qquad \forall x \in N(p)
>$$
>
>This **local maximum** is $f(p)$.
>

>[!DEFINITION] Definition: Local Extremum
>
>The local minima and maxima of a function are known as its **local extrema**.
>
>TODO: Add Diagram
>

## Global Extrema

>[!DEFINITION] Definition: Global Minimum
>
>Let $f: \mathcal{D} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
>
>We say that $f$ **has a global minimum at** $p \in \mathcal{D}$ if
>
>$$
>f(p) \le f(x) \qquad \forall x \in \mathcal{D}
>$$
>
>This **global minimum** is $f(p)$.
>
>>[!NOTE]
>>
>>There cannot be more than one value for the global minimum, but there may be multiple places in the domain of the function where said minimum occurs.
>>
>

>[!DEFINITION] Definition: Global Maximum
>
>Let $f: \mathcal{D} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
>
>We say that $f$ **has a global maximum at** $p \in \mathcal{D}$ if
>
>$$
>f(p) \ge f(x) \qquad \forall x \in \mathcal{D}
>$$
>
>This **global maximum** is $f(p)$.
>
>>[!NOTE]
>>
>>There cannot be more than one value for the global maximum, but there may be multiple places in the domain of the function where said maximum occurs.
>>
>

>[!DEFINITION] Definition: Global Extremum
>
>The global minimum and maximum of a function are known as its **global extrema**.
>

>[!THEOREM] Theorem: Global Extremum $\implies$ Local Extremum
>
>Every [global minimum](#Global%20Extrema) is a [local minimum](#Local%20Extrema) and every [global maximum](#Global%20Extrema) is a [local maximum](#Local%20Extrema).
>
>>[!PROOF]-
>>
>>TODO
>>
>

## Finding Extrema

>[!THEOREM] Theorem: Critical Points and Local Extrema
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
>
>If $f$ has a [local extremum](#Local%20Extrema) at $p \in \mathcal{D}$, then $f$ has a [critical point](./Differentiability%20(Real%20Functions).md) at $p$.
>
>>[!PROOF]-
>>
>>If $f$ is not [differentiable](./Differentiability%20(Real%20Functions).md) at $p$, then it trivially has a [critical point](./Differentiability%20(Real%20Functions).md) at $p$.
>>
>>We need to prove two additional things:
>>- (I) If $f$ is [differentiable](./Differentiability%20(Real%20Functions).md) at $p$ and has a [local minimum](#Local%20Extrema) there, then $f'(p) = 0$.
>>- (II) If $f$ is [differentiable](./Differentiability%20(Real%20Functions).md) at $p$ and has a [local maximum](#Local%20Extrema) there, then $f'(p) = 0$.
>>
>>**Proof of (I):**
>>
>>Since $f$ is [differentiable](./Differentiability%20(Real%20Functions).md) at $p$, for each $\varepsilon \gt 0$, there exists some $\delta \gt 0$ such that
>>
>>$$
>>0 \lt |h - p| \lt \delta \implies \left\vert\frac{f(p + h) - f(p)}{h} - f'(p)\right\vert \lt \varepsilon.
>>$$
>>
>>Since $f$ has a [local minimum](#Local%20Extrema) at $p$, there exists some $\delta' \le \delta$ such that
>>
>>$$
>>f(p) \le f(x)
>>$$
>>
>>for all $x$ with $0 \lt |x - p| \lt \delta'$. TODO
>>
>
>>[!THEOREM] Theorem: Criteria of the First Derivative
>>
>>If $f$ is [differentiable](./Differentiability%20(Real%20Functions).md) at a [critical point](./Differentiability%20(Real%20Functions).md)  $x_0$, then:
>>- $f$ has a [local minimum](#Local%20Extrema) at $x_0$ if there is some $\varepsilon \gt 0$ such that
>>
>>$$
>>f'(x) \lt 0 \qquad \forall x \in (x_0 - \varepsilon; x_0) \qquad \text{ and } \qquad f'(x) \gt 0 \qquad \forall x \in (x_0; x_0 + \varepsilon)
>>$$
>>
>>- $f$ has a [local maximum](#Local%20Extrema) at $x_0$ if there is some $\varepsilon \gt 0$ such that
>>
>>$$
>>f'(x) \gt 0 \quad \forall x \in (x_0-\varepsilon; x_0)\qquad \text{ and } \qquad f'(x) \lt 0 \quad \forall x\in (x_0; x_0+\varepsilon)
>>$$
>>
>>>[!PROOF]-
>>>
>>>TODO
>>
>
>>[!THEOREM] Theorem: Criteria of the Second Derivative
>>
>>If $f$ is [differentiable](./Differentiability%20(Real%20Functions).md) at a [critical point](./Differentiability%20(Real%20Functions).md) $x_0$, then:
>>
>>- $f$ has a [local minimum](#Local%20Extrema) at $x_0$ if $f''(x_0) \gt 0$;
>>- $f$ has a [local maximum](#Local%20Extrema) at $x_0$ if $f''(x_0) \lt 0$.
>>
>>>[!WARNING]
>>>
>>>If $f''(x_0) = 0$ or $f$ is not [twice differentiable](./Differentiability%20(Real%20Functions).md) at $x_0$, then $f$ may or may not have a [local extremum](#Local%20Extrema) at $x_0$, but we cannot use the second derivative to verify this.
>>>
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

>[!ALGORITHM] Algorithm: Finding the Extrema of a Function
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md).
>
>1. Determine the [critical points](./Differentiability%20(Real%20Functions).md) $x_1, x_2, \cdots, x_n \in \mathcal{D}$ of $f$ by solving $f'(x) = 0$ and also seeing where $f$ is not [differentiable](./Differentiability%20(Real%20Functions).md).
>2. Use the above criteria to check at which [critical point](./Differentiability%20(Real%20Functions).md) $f$ has [local extrema](#Local%20Extrema).
>3. Evaluate $f$ at the places of its [local extrema](#Local%20Extrema) to obtain the values of the [local minima](#Local%20Extrema) and [local maxima](#Local%20Extrema).
>4. Evaluate $f$ at the following locations:
>	- If $D = [a;b]$ where $a,b \in \mathbb{R}$, evaluate $f(a)$ and $f(b)$;
>	-  If $D = [a;b)$ where $a \in \mathbb{R}$ and $b \in \mathbb{R} \cup \{\infty\}$, evaluate $f(a)$ and $\lim_{x\to b} f(x)$;
>	- If $D = (a;b]$ where $a \in \mathbb{R} \cup \{-\infty \}$ and $b \in \mathbb{R}$, evaluate $\lim_{x\to a} f(x)$ and $f(b)$;
>	- If $D = (a;b)$ where $a \in \mathbb{R} \cup \{-\infty \}$ and $b \in \mathbb{R} \cup \{\infty\}$, evaluate $\lim_{x\to a} f(x)$ and $\lim_{x\to b} f(x)$;
>	- If $D = D_1 \cup \cdots \cup D_n$ is a [union](../../../Set%20Theory/Collections.md) of [disjoint](../../../Set%20Theory/Sets.md) [intervals](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) $D_1, \cdots, D_n$, then perform Step 4 separately for each interval.
>5. Compare the [local extrema](#Local%20Extrema) of $f$ with the values from Step 4:
>	- If there is a greatest value, then it is the [global maximum](#Global%20Extrema) of $f$;
>	- If there is a smallest value, then it is the [global minimum](#Global%20Extrema) of $f$;