---
tags:
    - real-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Real Rational Functions

>[!DEFINITION] Definition: Real Rational Functions
>
>A **real rational function** is a [real function](./Real%20Functions.md) $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ for which there exist [real polynomials](../../../Algebra/Fields/The%20Real%20Numbers/Real%20Polynomials.md) $P$ and $Q$ such that
>
>$$
>f(x) = \frac{P(x)}{Q(x)}
>$$
>
>for all $x \in \mathcal{D}$.
>

>[!THEOREM] Theorem: Limits at Infinity
>
>Let $f$ be a [real rational function](./Real%20Rational%20Functions.md) given by
>
>$$
>f(x) = \frac{P(x)}{Q(x)} = \frac{\displaystyle{\sum_{k=0}^m p_k x^k}}{\displaystyle{\sum_{k=0}^n q_k x^k}}.
>$$
>
>If $m \lt n$, then $f$ has a [horizontal asymptote](./Limits%20(Real%20Functions.md) at $y = 0$:
>
>$$
>m \lt n \implies \lim_{x \to \pm \infty} f(x) = 0
>$$
>
>If $m = n$, then $f$ has a [horizontal asymptote](./Limits%20(Real%20Functions.md) at $y = \frac{p_m}{q_n}$:
>
>$$
>m = n \implies \lim_{x \to \pm \infty} f(x) = \frac{p_m}{q_n} 
>$$
>
>If $m \gt n$, then the [limits](./Limits%20(Real%20Functions.md) of $f$ at $\pm_{\infty}$ depend on $(n-m)$ and $\frac{p_m}{q_n}$:
>
>$$
>\begin{aligned}
>&\lim_{x \to +\infty}  f(x) = 
>\begin{cases}
>+\infty \qquad \text{when } \frac{p_m}{q_n} \gt 0 \\
>-\infty \qquad \text{when } \frac{p_m}{q_n} \lt 0
>\end{cases} \\
>&\lim_{x \to -\infty} f(x) =
>\begin{cases}
>+\infty \qquad \text{when } (n-m) \text{ is even and } \frac{p_m}{q_n} \gt 0 \text{ or } (n - m) \text{ is odd and } \frac{p_m}{q_n} \lt 0 \\
>-\infty \qquad \text{when } (n-m) \text{ is even and } \frac{p_m}{q_n} \lt 0 \text{ or } (n - m) \text{ is odd and } \frac{p_m}{q_n} \gt 0
>\end{cases}
>\end{aligned}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Vertical Asymptotes
>
>Let $f$ be a [real rational function](./Real%20Rational%20Functions.md) given by
>
>$$
>f(x) = \frac{P(x)}{Q(x)} = \frac{\displaystyle{\sum_{k=0}^m p_k x^k}}{\displaystyle{\sum_{k=0}^n q_k x^k}}.
>$$
>
>If $r \in \mathbb{R}$ is a [root](../../../Algebra/Equations/Polynomial%20Equations/Polynomial%20Equations.md) of $Q$ but not of $P$, then $f$ has a [vertical asymptote](./Limits%20(Real%20Functions.md#Asymptotes) at $x = r$.
>
>If $r \in \mathbb{R}$ is a [root](../../../Algebra/Equations/Polynomial%20Equations/Polynomial%20Equations.md) of both $P$ and $Q$ but its [multiplicity](../../../Algebra/Fields/The%20Real%20Numbers/Real%20Polynomials.md) for $P$ is lower than its [multiplicity](../../../Algebra/Fields/The%20Real%20Numbers/Real%20Polynomials.md) for $Q$, then $f$ again has a [vertical asymptote](./Limits%20(Real%20Functions.md#Asymptotes) at $x = r$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Partial Fraction Decomposition
>
>Every [real rational function](./Real%20Rational%20Functions.md) $f(x) = \frac{P(x)}{Q(x)}$ with $\deg P \lt \deg Q$ can be represented as a sum of [real rational functions](./Real%20Rational%20Functions.md)
>
>$$f(x) = \sum_{i = 1}\sum_{j = 1}^{m_{l_i}} \frac{A_{ji}}{l_i(x)^j} + \sum_{i=1}\sum_{j = 1}^{m_{q_i}} \frac{B_{ji}x + C_{ji}}{q_i(x)^j},$$
>
>where:
>
>- $l_i(x)$ are the distinct [linear factors](../../../Algebra/Fields/The%20Real%20Numbers/Real%20Polynomials.md) of $Q(x)$ and $m_{l_i}$ are their respective [multiplicities](../../../Algebra/Fields/The%20Real%20Numbers/Real%20Polynomials.md);
>- $q_i(x)$ are the distinct [irreducible quadratic factors](../../../Algebra/Fields/The%20Real%20Numbers/Real%20Polynomials.md) of $Q(x)$ and $m_{q_i}$ are their respective [multiplicities](../../../Algebra/Fields/The%20Real%20Numbers/Real%20Polynomials.md);
>- $A_{ji}, B_{ji}, C_{ji} \in \mathbb{R}$.
>
>>[!EXAMPLE]- Example: $\frac{x^4 + 3x^2 - 2x}{x^6 + x^4 -x^2 -1}$
>>
>>We want to find the [partial fraction decomposition](./Real%20Rational%20Functions.md) of the following [rational function](./Real%20Rational%20Functions.md):
>>
>>$$f(x) = \frac{x^4 + 3x^2 - 2x}{x^6 + x^4 -x^2 - 1}$$
>>
>>The denominator can be factored as $x^6 + x^4 -x^2 -1 = (x-1)(x+1)(x^2+1)^2$:
>>
>>$$\frac{x^4 + 3x^2 - 2x}{x^6 + x^4 -x^2 -1} = \frac{x^4 + 3x^2 - 2x}{(x-1)(x+1)(x^2+1)^2}$$
>>
>>The theorem tells us that 
>>
>>$$\frac{x^4 + 3x^2 - 2x}{x^6 + x^4 -x^2 -1} = \frac{A}{x-1} + \frac{B}{x+1} + \frac{Cx + D}{x^2 + 1} + \frac{Ex + F}{(x^2 +1)^2}$$
>>
>>for some $A, B, C, D, E, F \in \mathbb{R}$. We bring the right-hand side to a single denominator:
>>
>>$$\begin{aligned}& \frac{A}{x-1} + \frac{B}{x+1} + \frac{Cx + D}{x^2 + 1} + \frac{Ex + F}{x^2 +1} = \\ & = \frac{A(x+1)(x^2+1)^2 + B(x-1)(x^2+1)^2 + (Cx+D)(x-1)(x+1)(x^2+1) + (Ex+F)(x-1)(x+1)}{(x-1)(x+1)(x^2+1)^2}\end{aligned}$$
>>
>>We multiply the numerator out and group according to the powers of $x$:
>>
>>$$(A + B + C)x^5 + (A - B + D)x^4 + (2A + 2B + E)x^3 + (2A - 2B + F)x^2 + (A + B - C - E)x + (A - B - D - F)$$
>>
>>We want this to be equal to the numerator of the original expression. By comparing the coefficients in front of the respective powers of $x$, we obtain the following [system of linear equations](../../../Algebra/Linear%20Algebra/Systems%20of%20Linear%20Equations/Systems%20of%20Linear%20Equations.md):
>>
>>$$\left\vert\begin{array}{cccccccc}+A & +B & +C & & & & = & 0 \\ +A & -B & & +D & & & = & 1 \\ +2A & +2B & & & +E & & = & 0 \\ +2A & -2B & & & & +F & = & 3 \\ +A & +B & -C & & -E & & = & -2 \\ +A & -B & & -D & & -F & = & 0\end{array}\right.$$
>>
>>Solving it, we obtain:
>>
>>$$\left\vert\begin{aligned}A & = \frac{1}{4} \\ B & = -\frac{3}{4} \\ C & = \frac{1}{2} \\ D & = 0 \\ E & = 1 \\ F & = 1\end{aligned}\right.$$
>>
>>We can now substitute these values back to obtain the [partial fraction decomposition](./Real%20Rational%20Functions.md):
>>
>>$$\begin{aligned}\frac{x^4 + 3x^2 - 2x}{x^6 + x^4 -x^2 - 1} & = \frac{A}{x-1} + \frac{B}{x+1} + \frac{Cx + D}{x^2 + 1} + \frac{Ex + F}{(x^2 +1)^2} \\ & = \frac{1}{4(x-1)}-\frac{3}{4(x+1)}+\frac{x}{2(x^2+1)}+\frac{x+1}{(x^2+1)^2}\end{aligned}$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Antidifferentiation of Rational Functions
>
>Let $f: \mathcal{D} \subseteq \mathbb{R} \to \mathbb{R}$ be a [real function](./Real%20Functions.md) and let $I \subseteq \mathcal{D}$ be an [interval](../Euclidean%20Space/Euclidean%20Space.md#The%20Real%20Number%20Line).
>
>If $f$ is [rational](./Real%20Rational%20Functions.md) on $I$ with $f(x) = \frac{1}{(x-a)^m}$, where $m \in \mathbb{N}$, then $f$ is [antidifferentiable](./Antidifferentiability%20(Real%20Functions).md) on $I$:
>
>$$\int \frac{\mathrm{d}x}{(x-a)^m} = \begin{cases} \ln |x - a| + C & \text{if } m = 1 \\ \\ -\frac{1}{(m-1)(x-a)^{m-1}} + C & \text{if } m \ge 2 \end{cases}$$
>
>If $f$ is [rational](./Real%20Rational%20Functions.md) on $I$ with $f(x) = \frac{1}{(x-a)^2+b^2}$, where $b \gt 0$, then $f$ is [antidifferentiable](./Antidifferentiability%20(Real%20Functions).md) on $I$:
>
>$$\int \frac{1}{(x-a)^2+b^2} \,\mathrm{d}x = \frac{1}{b} \arctan \frac{x-a}{b} + C, \qquad b \gt 0$$
>
>If $f$ is [rational](./Real%20Rational%20Functions.md) on $I$ with $f(x) = \frac{x-a}{(x-a)^2+b^2}$, where $b \gt 0$, then $f$ is [antidifferentiable](./Antidifferentiability%20(Real%20Functions).md) on $I$:
>
>$$\int \frac{x-a}{(x-a)^2+b^2} \,\mathrm{d}x = \frac{1}{2}\ln((x-a)^2 + b^2)+C$$
>
>If $f$ is [rational](./Real%20Rational%20Functions.md) on $I$ with $f(x) = \frac{1}{(x^2 + px + q)^m}$, where $m \in \mathbb{N}$ and $p, q \in \mathbb{R}$ with $p^2 - 4q \lt 0$, then $f$ is [antidifferentiable](./Antidifferentiability%20(Real%20Functions).md) on $I$:
>
>$$\int \frac{\mathrm{d}x}{(x^2+px+q)^m} = \begin{cases} \frac{2}{\sqrt{4q-p^2}} \arctan \left(\frac{2x+p}{\sqrt{4q-p^2}}\right) + C & \text{if } m = 1 \\ \frac{2x+p}{(m-1)(4q-p^2)(x^2+px+q)^{m-1}} + \frac{4m-6}{(m-1)(4q-p^2)}\int \frac{1}{(x^2+px+q)^{m-1}} + C & \text{if } m \ge 2\end{cases}$$
>
>If $f$ is [rational](./Real%20Rational%20Functions.md) on $I$ with $f(x) = \frac{Ax + B}{(x^2 + px + q)^m}$, where $m \in \mathbb{N}$ and $A, B, p, q, \in \mathbb{R}$ with $p^2 - 4q \lt 0$, then $f$ is [antidifferentiable](./Antidifferentiability%20(Real%20Functions).md) on $I$:
>
>$$\int \frac{Ax + B}{(x^2+px+q)^m} \mathop{\mathrm{d}x} = \begin{cases}\frac{A}{2}\ln (x^2+px+q) + \left(B - \frac{Ap}{2}\right)\int \frac{\mathop{\mathrm{d}x}}{x^2+px+q} + C & \text{if } m = 1 \\ -\frac{A}{2(m-1)(x^2+px+q)} + \left(B - \frac{Ap}{2}\right)\int \frac{\mathop{\mathrm{d}x}}{(x^2+px+q)^{m-1}} + C & \text{if } m \ge 2 \end{cases}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!ALGORITHM] Algorithm: Antidifferentiation of Rational Functions
>
>We are given the following [real rational function](./Real%20Rational%20Functions.md):
>
>$$f(x) = \frac{N(x)}{D(x)}$$
>
>If $\deg N \lt \deg D$, then find the [partial fraction decomposition](./Real%20Rational%20Functions.md) of $f$ and use the [antiderivatives of the elementary rational functions](./Antidifferentiability%20(Real%20Functions).md):
>
>$$\int f(x) \mathop{\mathrm{d}x} = \sum_{i}\sum_{j = 1}^{m_{l_i}} \int \frac{A_{ji}}{l_i(x)^j} \mathop{\mathrm{d}x} + \sum_{i}\sum_{j = 1}^{m_{q_i}}\int \frac{B_{ji}x + C_{ji}}{q_i(x)^j} \mathop{\mathrm{d}x}$$
>
>If $\deg N \ge \deg D$, then [divide](../../../Algebra/Fields/The%20Real%20Numbers/Real%20Polynomials.md) $N$ by $D$ to find $f(x) = Q(x) + \frac{R(x)}{D(x)}$. Find the [partial fraction decomposition](./Real%20Rational%20Functions.md) of $\frac{R(x)}{D(x)}$ and use the [antiderivatives](./Antidifferentiability%20(Real%20Functions).md):
>
>$$\int f(x) \mathop{\mathrm{d}x} = \int Q(x) + \frac{R(x)}{D(x)} \mathop{\mathrm{d}x} = \int Q(x) \mathop{\mathrm{d}x} + \int \frac{R(x)}{D(x)} \mathop{\mathrm{d}x}$$
>
>>[!EXAMPLE]- Example: $\int \frac{x^4+3x^2-2x}{x^4-1} \,\mathrm{d}x$
>>
>>We want to determine the [antiderivatives](./Antidifferentiability%20(Real%20Functions).md) of
>>
>>$$f(x) = \frac{x^4+3x^2-2x}{x^4-1}.$$
>>
>>[Polynomial division](../../../Algebra/Fields/The%20Real%20Numbers/Real%20Polynomials.md) gives us the following:
>>
>>$$f(x) = \frac{3x^2-2x+1}{x^4 - 1} + 1$$
>>
>>We have:
>>
>>$$\begin{aligned}\int f(x) \,\mathrm{d}x & = \int \frac{3x^2-2x+1}{x^4 - 1} + 1\,\mathrm{d}x \\ & = \int 1 \,\mathrm{d}x + \int \frac{3x^2-2x+1}{x^4 - 1} \,\mathrm{d}x \\ & = x + \int \frac{3x^2-2x+1}{x^4 - 1} \,\mathrm{d}x\end{aligned}$$
>>
>>To find $\int \frac{3x^2-2x+1}{x^4 - 1} \,\mathrm{d}x$, we need to find the [partial fraction decomposition](./Real%20Rational%20Functions.md) of $\frac{3x^2-2x+1}{x^4 - 1}$:
>>
>>$$\frac{3x^2-2x+1}{x^4 - 1} = \frac{1}{2(x-1)}-\frac{3}{2(x+1)}+\frac{x+1}{x^2+1}$$
>>
>>We have:
>>
>>$$\begin{aligned}\int \frac{3x^2-2x+1}{x^4 - 1} \,\mathrm{d}x & = \int \frac{1}{2(x-1)}-\frac{3}{2(x+1)}+\frac{x+1}{x^2+1}\,\mathrm{d}x \\ & = \int \frac{1}{2(x-1)} \,\mathrm{d}x + \int -\frac{3}{2(x+1)} \,\mathrm{d}x + \int \frac{x+1}{x^2+1} \,\mathrm{d}x \\ & = \frac{1}{2} \int \frac{1}{x-1} \,\mathrm{d}x - \frac{3}{2}\int \frac{1}{x+1}\,\mathrm{d}x + \int \frac{x+1}{x^2+1} \,\mathrm{d}x \\ & = \frac{1}{2} \int \frac{1}{x-1} \,\mathrm{d}x - \frac{3}{2}\int \frac{1}{x+1}\,\mathrm{d}x + \int \frac{x}{x^2 + 1} \,\mathrm{d}x + \int \frac{1}{x^2 + 1} \,\mathrm{d}x\end{aligned}$$
>>
>>By using the [antiderivatives](./Antidifferentiability%20(Real%20Functions).md) of the [elementary rational functions](./Real%20Rational%20Functions.md):
>>
>>$$\begin{aligned}\int \frac{3x^2-2x+1}{x^4 - 1} \,\mathrm{d}x & = \frac{1}{2} \int \frac{1}{x-1} \,\mathrm{d}x - \frac{3}{2}\int \frac{1}{x+1}\,\mathrm{d}x + \int \frac{x}{x^2 + 1} \,\mathrm{d}x + \int \frac{1}{x^2 + 1} \,\mathrm{d}x \\ & = \frac{1}{2}\ln|x-1| - \frac{3}{2}\ln|x+1| + \frac{1}{2}\ln(x^2 + 1) + \arctan x + C\end{aligned}$$
>>
>>Finally:
>>
>>$$\begin{aligned}\int f(x) \,\mathrm{d}x & = x + \int \frac{3x^2-2x+1}{x^4 - 1} \,\mathrm{d}x \\ & = x + \frac{1}{2}\ln|x-1| - \frac{3}{2}\ln|x+1| + \frac{1}{2}\ln(x^2 + 1) + \arctan x + C\end{aligned}$$
>>
>