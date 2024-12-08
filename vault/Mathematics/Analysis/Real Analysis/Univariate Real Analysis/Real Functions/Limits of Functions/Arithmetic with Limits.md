>[!THEOREM] Theorem: Arithmetic with Real Limits
>
>Let $f,g: D\subseteq\mathbb{R} \to \mathbb{R}$ be [real functions](../Real%20Function.md).
>
>If both [limits](Real%20Limits%20of%20a%20Function.md) $\displaystyle \lim_{x \to c} f(x)$ and $\displaystyle \lim_{x \to c} g(x)$ exist for $c \in D \cup \{-\infty, +\infty\}$, then
>
>$$\lim_{x\to c} \alpha f(x) + \beta g(x) = \alpha \lim_{x \to c} f(x) + \beta \lim_{x \to c} g(x) \qquad \forall \alpha, \beta \in \mathbb{R}$$
>
>$$\lim_{x \to c} \left(f(x) g(x)\right) = \left(\lim_{x\to c} f(x)\right) \cdot \left(\lim_{x\to c} g(x)\right)$$
>
>$$\lim_{x \to c} \frac{f(x)}{g(x)} = \frac{\displaystyle \lim_{x \to c} f(x)}{\displaystyle \lim_{x \to c} g(x)}, \qquad \lim_{x \to c} g(x) \ne 0$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!WARNING]
>>
>>These do *not* apply to [infinite limits](Infinite%20Limits.md).
>>
>

>[!THEOREM] Theorem: Arithmetic with Infinite Limits
>Let $f,g: D\subseteq\mathbb{R} \to \mathbb{R}$ be two [functions](../Real%20Function.md).
>
>The following rules apply for the [limits](Real%20Limits%20of%20a%20Function.md) of $f$ and $g$ for $c \in D \cup \{-\infty, +\infty\}$, no matter if they are [real](Real%20Limits%20of%20a%20Function.md) or [infinite](Infinite%20Limits.md):
>
>||$\displaystyle \lim_{x\to c} f(x) = L \lt 0$|$\displaystyle \lim_{x\to c} f(x) = L \gt 0$|
>|:--:|:--:|:--:|
>|$\displaystyle \lim_{x\to c} g(x) = -\infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = -\infty$ </br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = +\infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = -\infty$ </br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = -\infty$|
>|$\displaystyle \lim_{x\to c} g(x) = + \infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = +\infty$ </br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = -\infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = +\infty$ </br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = +\infty$|
> 
>||$\displaystyle \lim_{x\to c} f(x) = -\infty$|$\displaystyle \lim_{x\to c} f(x) = +\infty$|
>|:--:|:--:|:--:|
>|$\displaystyle \lim_{x\to c} g(x) = -\infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = -\infty$ </br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = +\infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = \, ?$ </br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = -\infty$|
>|$\displaystyle \lim_{x\to c} g(x) = + \infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = \, ?$ </br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = -\infty$|$\displaystyle \lim_{x\to c} (f(x) + g(x)) = +\infty$ </br> $\displaystyle\lim_{x\to c} (f(x)g(x)) = +\infty$|
>
>>[!NOTE]
>>A question mark ("?") indicates that we cannot compute the limit directly, but we can try to transform the expression via algebraic manipulations in such a way, so as to make the limit computable.
>
>>[!PROOF]-
>>TODO