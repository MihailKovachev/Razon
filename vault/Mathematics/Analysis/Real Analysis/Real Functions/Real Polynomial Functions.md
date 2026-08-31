---
tags:
    - real-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Real Polynomial Functions

>[!DEFINITION] Definition: Real Polynomial Functions
>
>A **real polynomial function** is a [real function](./Real%20Functions.md) $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ for which there exists a [real polynomial](../../../Algebra/Fields/The%20Real%20Numbers/Real%20Polynomials.md) $\sum_{k = 0}^n a_k x^k$ such that
>
>$$
>f(x) = \sum_{k = 0}^n a_k x^k = a_n x^n + a_{n-1}x^{n-1} + \cdots + a_1 x + a_0
>$$
>
>for every $x \in \mathcal{D}$.
>

>[!THEOREM] Theorem: Parity of Real Polynomial Functions
>
>A [real polynomial function](./Real%20Polynomial%20Functions.md) $f(x) = \sum_{k=0}^n a_k x^k$ is:
>- [even](./Parity.md) if and only if only the coefficients $a_k$ in front of even numbers $k$ are non-zero;
>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity of Real Polynomial Functions
>
>Every [real polynomial function](./Real%20Polynomial%20Functions.md) is [continuous](./Continuity%20(Real%20Functions).md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Differentiability of Real Polynomial Functions
>
>Every [real polynomial function](./Real%20Polynomial%20Functions.md) 
>
>$$
>f(x) = \sum_{k=0}^n a_k x^k = a_n x^n + a_{n-1}x^{n-1} + \cdots + a_1 x + a_0
>$$
>
>is [differentiable](./Differentiability%20(Real%20Functions).md) and its [derivative](./Differentiability%20(Real%20Functions).md) $f'$ is also a [real polynomial function](./Real%20Polynomial%20Functions.md):
>
>$$
>f'(x) = \sum_{k = 1}^n k a_k x^{k-1} = n a_n x^{n-1} + (n-1)a_{n-1}x^{n - 2} + \cdots + 2a_2 x + a_1
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antidifferentiability of Real Polynomial Functions
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $I \subseteq \mathcal{D}$ be an [interval](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line).
>
>If $f$ is [polynomial](./Real%20Polynomial%20Functions.md) on $I$ with $f(x) = \sum_{k=0}^n a_k x^k$, then $f$ is [antidifferentiable](./Antidifferentiability%20(Real%20Functions).md) on $I$ with
>
>$$
>\int f(x) \mathop{\mathrm{d}x} = C + \sum_{k=0}^n \frac{1}{k+1}a_k x^{k+1}.
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>