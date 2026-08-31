---
tags:
    - real-mathematical-analysis
    - mathematical-analysis
    - electrical-engineering
---

# Taylor Series

>[!DEFINITION] Definition: Taylor Polynomial
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) which is $m$-times [differentiable](./Differentiability%20(Real%20Functions).md) at $p \in \mathcal{D}$.
>
>The $m$**-th Taylor polynomial** of $f$ at $p$ is the following [function](./Real%20Functions.md):
>
>$$\sum_{k = 0}^m \frac{f^{(k)}(p)}{k!}(x-p)^k$$
>
>>[!NOTATION]
>>
>>$$T_m(p; x)$$
>>
>

The [Taylor polynomial](./Taylor%20Series.md) $T_m(p, x)$ has the following [polynomial](./Real%20Polynomial%20Functions.md) expansion:

$$T_m(p; x) = f(p) + f'(p)(x-p)+\frac{f''(p)}{2!}(x-p)^2 + \cdots + \frac{f^{(m)}(p)}{m!}(x-p)^m$$

>[!THEOREM] Taylor's Theorem
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md), let $(a,b) \subseteq \mathcal{D}$ and let $p \in (a,b)$. Let $R_{m+1}(p;x)$ denote the [remainder](TODO) of $f$ and its $m$-th [Taylor polynomial](./Taylor%20Series.md) at $p$:
>
>$$R_{m+1}(p; x) = f(x) - T_m (p; x)$$
>
>If $f$ is $(m+1)$-times [continuously differentiable](./Differentiability%20(Real%20Functions).md) on $(a,b)$, then $R_{m+1}(p;x)$ can be obtained by the following [integral](./Integration/Riemann%20Integrals%20(Real%20Functions).md) from $p$ to $x$ :
>
>$$R_{m+1}(p; x) = \frac{1}{m!}\int_p^x (x-t)^m f^{(m+1)}(t) \,\mathrm{d}t$$
>
>Moreover, for each $x \in (a, b)$, there exists some $\xi_x \in (p, x)$ or $\xi_x \in (x,p)$ such that
>
>$$R_{m+1}(p; x) = \frac{f^{(m+1)}(\xi_x)}{(m+1)!}(x-p)^{m+1}.$$
>
>>[!NOTATION]
>>
>>Sometimes, we substitute $h = x - p$:
>>
>>$$R_{m+1}(p; p + h) = f(p + h) - T_m (p; p + h)$$
>>
>>$$R_{m+1}(p; p + h) = \frac{f^{(m+1)}(\xi_x)}{(m+1)!}h^{m+1}$$
>>
>
>>[!EXAMPLE]- Example: $\mathrm{e}^x$
>>
>>For the [exponential function](./Real%20Exponentiation.md#The%20Real%20Exponential%20Function) $f(x) = \mathrm{e}^x$ we have $f^{(m)}(x) = \mathrm{e}^x$. For its $m$-th [Taylor polynomial](./Taylor%20Series.md) at $0$:
>>
>>$$\begin{aligned}f(x) & = T_m(0; x) + R_{m+1}(0; x) \\ \mathrm{e}^x & = \sum_{k=0}^m \frac{x^k}{k!} + R_{m+1}(0; x)\end{aligned}$$
>>
>>The theorem tells us that there is some $\xi_x \in (0, x)$ with
>>
>>$$R_{m+1}(0; x) = \frac{\mathrm{e}^{\xi_x}}{(m+1)!}x^{m+1}.$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Remainder and Bachmann-Landau
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md), let $(a,b) \subseteq \mathcal{D}$ and let $p \in (a,b)$. Let $R_{m+1}(p;p + h)$ denote the [remainder](TODO) of $f$ and its $m$-th [Taylor polynomial](./Taylor%20Series.md) at $p$:
>
>$$R_{m+1}(p; p + h) = f(p + h) - T_m (p; p + h)$$
>
>If $f$ is $m$-times [differentiable](./Differentiability%20(Real%20Functions).md) at $p$, then $R_{m+1}(p; p+h)$ is [little O](../Asymptotic%20Analysis/Bachmann-Landau%20Notation.md) of $h^m$:
>
>$$R_{m+1}(p; p + h) = o(h^m) \qquad \text{for} \qquad h \to 0$$
>
>If $f$ is $(m+1)$-times [differentiable](./Differentiability%20(Real%20Functions).md) at $p$, then $R_{m+1}(p; p+h)$ is [big O](../Asymptotic%20Analysis/Bachmann-Landau%20Notation.md) of $h^{m+1}$:
>
>$$R_{m+1}(p; p + h) = O(h^{m+1}) \qquad \text{for} \qquad h \to 0$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!DEFINITION] Definition: Taylor Series
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) which is [infinitely differentiable](./Differentiability%20(Real%20Functions).md) at $p \in \mathcal{D}$.
>
>The **Taylor series** of $f$ at $p$ is the following [power series](../Real%20Power%20Series.md)
>
>$$\sum_{k = 0}^{\infty} \frac{f^{(k)}(p)}{k!}(x-p)^k$$
>
>>[!NOTATION]
>>
>>$$T(p; x)$$
>>
>

The [Taylor series](./Taylor%20Series.md) of a [function](./Real%20Functions.md) $f$ is useful because it can sometimes allow us to express $f$ as a [power series](../Real%20Power%20Series.md).

>[!THEOREM] Theorem: Taylor Series-Function Equality
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) which is [infinitely differentiable](./Differentiability%20(Real%20Functions).md) at $p \in \mathcal{D}$ and let $x \in \mathcal{D}$.
>
>The [Taylor series](./Taylor%20Series.md) $T_{f}(p; x)$ [converges](../Real%20Power%20Series.md) to $f(x)$ if and only if the [sequence](../../Functional%20Analysis/Sequences/Sequences.md) of the [remainders](./Taylor%20Series.md) of its [Taylor polynomials](./Taylor%20Series.md) at $p$ [converges](../../Functional%20Analysis/Sequences/Sequences.md#Convergence) to $0$.
>
>$$f(x) = T_{f}(p; x) \iff \lim_{n \to \infty} R_n(p; x) = 0$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Taylor Series-Function Equality via Derivatives
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md), let $p, x \in \mathcal{D}$ and let $I \subset \mathcal{D}$ be the [compact interval](../Euclidean%20Space/Euclidean%20Space.md) whose endpoints are $p$ and $x$.
>
>If $f$ is [infinitely differentiable](./Differentiability%20(Real%20Functions).md) on an [open interval](../Euclidean%20Space/Euclidean%20Space.md) containing $I$ and there exist $A, B \in \mathbb{R}$ such that
>
>$$|f^{(n)}(t)| \le A\cdot B^n$$
>
>for all $n \in \mathbb{N}$ and all $t \in I$, then $f(x)$ is equal to the [Taylor series](./Taylor%20Series.md) $T_{f}(p; x)$:
>
>$$f(x) = T_f (p; x)$$
>
>>[!PROOF]-
>>
>>From [Taylor's theorem](./Taylor%20Series.md), we know that there exists some $\xi_x$ in the [open interval](../Euclidean%20Space/Euclidean%20Space.md) whose endpoints are $x$ and $p$ such that
>>
>>$$R_n (p; x) = \frac{f^{(n)}(\xi_x)}{(n)!}(x-p)^n.$$
>>
>>We have
>>
>>$$|R_n (p; x)| = \left\vert \frac{f^{(n)}(\xi_x)}{(n)!}(x-p)^n \right\vert \le \frac{AB^n}{n!}|x-p|^n$$
>>
>>for all $n \in \mathbb{N}$. Since $\frac{AB^n}{n!}|x-p|^n$ [converges](./Limits%20(Real%20Functions.md) to $0$ for $n \to \infty$ and since
>>
>>$$0 \le |R_n (p; x)| \le \frac{AB^n}{n!}|x-p|^n,$$
>>
>>the [sandwich theorem](./Limits%20(Real%20Functions.md) tells us that
>>
>>$$\lim_{n \to \infty} |R_n (p; x)| = 0$$
>>
>>and so
>>
>>$$\lim_{n \to \infty} R_n (p; x) = 0.$$
>>
>