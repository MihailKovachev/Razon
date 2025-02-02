>[!THEOREM] Theorem: Arithmetic Differentiation Rules
>
>If $f,g: D \subseteq \mathbb{R} \to \mathbb{R}$ are [differentiable](Differentiability%20of%20Real%20Functions.md) at $x \in D$, then the following hold:
>
>- Linearity: $[\alpha\, f(x) + \beta\, g(x)]' = \alpha\, f'(x) + \beta\, g'(x)$ for all $\alpha, \beta \in \mathbb{R}$
>- Product Rule: $[f(x)g(x)]' = f'(x)g(x) + f(x)g'(x)$
>- Quotient Rule: $\left[\frac{f(x)}{g(x)}\right]' = \frac{f'(x)g(x)-f(x)g'(x)}{g(x)^2}$ provided that $g(x) \ne 0$
>- General Power Rule: $\left[f(x)^{g(x)}\right]' = f(x)^{g(x)}\left[f'(x)\frac{g(x)}{f(x)} + g'(x)\ln(f(x))\right]$
>
>>[!PROOF]-
>>
>>**Proof of linearity:**
>>
>>$$
>>\begin{align*}[\lambda\, f(x) + \mu\, g(x)]' &= \operatorname*{lim}_{\Delta x\rightarrow0}\frac{\lambda f(x_{0}+\Delta x)+\mu g(x_{0}+\Delta x) - \lambda f(x_{0})-\mu g(x_{0})}{\Delta x}\\ &= \lim_{\Delta x\to 0}\frac{\lambda[f(x_{0}+\Delta x)-f(x_{0})] + \mu[g(x_{0}+\Delta x)-g(x_{0})]}{\Delta x} \\ &= \lim_{\Delta x\to 0}\lambda\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x} + \lim_{\Delta x\to 0}\mu\frac{g(x_0+\Delta x)-g(x_0)}{\Delta x} \\ &= \lambda\lim_{\Delta x\to 0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x} + \mu\lim_{\Delta x\to 0}\frac{g(x_0+\Delta x)-g(x_0)}{\Delta x} \\ &= \lambda f'(x_0) + \mu g'(x_0)\end{align*}
>>$$
>>
>

>[!THEOREM] Theorem: Chain Rule
>
>If $g: D \subseteq \mathbb{R} \to \mathbb{R}$ is [differentiable](Differentiability%20of%20Real%20Functions.md) at $x \in D$ and $f: g(D) \to \mathbb{R}$ is [differentiable](Differentiability%20of%20Real%20Functions.md) at $g(x)$, then
>
>$$
>[f(g(x))]' = f'(g(x)) \cdot g'(x)
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Derivative of the Inverse Function
>
>Let $f: D \subseteq \mathbb{R} \to \mathbb{R}$ be [invertible](../../../Functions/Types%20of%20Functions/Inverse%20Function.md).
>
>If $f$ is [differentiable](Differentiability%20of%20Real%20Functions.md) at $f^{-1}(y), y \in f(D)$ and $f'(f^{-1}(y)) \ne 0$, then
>
>$$
>[f^{-1}(y)]' = \frac{1}{f'(f^{-1}(y))}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>
