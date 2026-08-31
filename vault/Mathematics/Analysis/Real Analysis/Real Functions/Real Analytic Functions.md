---
tags:
  - real-mathematical-analysis
  - mathematical-analysis
  - mathematics
---

# Real Analytic Functions

>[!DEFINITION] Definition: Real Analytic Function
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $O$ be an [open subset](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of $\mathbb{R}$ which is contained in $\mathcal{D}$.
>
>We say that $f$ is **analytic** on $O$ if there exists a [real power series](../Real%20Power%20Series.md) $\displaystyle \sum_{n=0}^\infty a_n (x - c)^n$ which [converges](../Real%20Power%20Series.md#Convergence) on $O$ such that
>
>$$
>f(x) = \displaystyle \sum_{n=0}^\infty a_n (x - c)^n \qquad \forall x \in O
>$$
>

>[!THEOREM] Theorem: Differentiation of Real Analytic Functions
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $O$ be an [open subset](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of $\mathbb{R}$ which is contained in $\mathcal{D}$.
>
>If $f$ is [analytic](./Real%20Analytic%20Functions.md) on $O$ with $f(x) = \sum_{n=0}^\infty a_n (x - c)^n$, then $f$ is [differentiable](./Differentiability%20(Real%20Functions).md) on $O$ and its [derivative](./Differentiability%20(Real%20Functions).md) is also [analytic](./Real%20Analytic%20Functions.md) on $O$ with
>
>$$
>f'(x) = \sum_{n=1}^\infty n a_n (x - c)^{n-1}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antidifferentiation of Real Analytic Functions
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $O$ be an [open subset](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line) of $\mathbb{R}$ which is contained in $\mathcal{D}$.
>
>If $f$ is [analytic](./Real%20Analytic%20Functions.md) on $O$ with $f(x) = \sum_{n=0}^\infty a_n (x - c)^n$, then its [antiderivatives](./Antidifferentiability%20(Real%20Functions).md) are also [analytic](./Real%20Analytic%20Functions.md) on $O$ with
>
>$$
>\int f(x) \mathop{\mathrm{d}x} = \text{const} + \sum_{n = 0}^\infty a_n \frac{(x - c)^{n+1}}{n+1}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Automatic Differentiation via Dual Numbers
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real analytic function](./Real%20Analytic%20Functions.md) and let $a + b\varepsilon$ be a [dual number](../../../Algebra/Dual%20Numbers.md).
>
>If $a \in \mathcal{D}$, then
>
>$$
>f(a + b\varepsilon) = f(a) + b f'(a)\varepsilon
>$$
>
>>[!TIP] Tip: Automatic Differentiation
>>
>>This theorem allows us to find the [derivative](./Differentiability%20(Real%20Functions).md) of $f$ at any $a \in \mathcal{D}$ without the need to find an expression for $f'$, so long as we have a closed-form expression for $f$. All we have to do is set $b = 1$ and then use this expression to evaluate $f(a + b \varepsilon)$. In the end, the value of the derivative $f'(a)$ will be the coefficient before $\varepsilon$.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>