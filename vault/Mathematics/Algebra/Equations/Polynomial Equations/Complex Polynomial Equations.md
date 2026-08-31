---
title: Complex Polynomial Equations
tags:
     - algebra
     - mathematics
---

# Complex Polynomial Equations

>[!THEOREM] Theorem:
>
>Every [complex polynomial equation](./Complex%20Polynomial%20Equations.md)
>
>$$\sum_{k = 0}^n a_k z^k = 0,$$
>
>where $\sum_{k = 0}^n a_k z^k$ is not constant, has at least one solution $z \in \mathbb{C}$.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Complex Conjugate Root Theorem
>
>If $z \in \mathbb{C}$ is a root of the [complex polynomial equation](./Complex%20Polynomial%20Equations.md)
>
>$$
>\sum_{k = 0}^n a_k z^k = 0
>$$
>
>and $a_k$ are all [real numbers](../../Fields/The%20Real%20Numbers/The%20Real%20Numbers.md), then the [complex conjugate](../../Fields/The%20Complex%20Numbers/Complex%20Numbers.md) $\bar{z}$ is also a root of the equation.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Cauchy's Bound
>
>If $r \in \mathbb{C}$ is a root of the [complex polynomial equation](./Complex%20Polynomial%20Equations.md)
>
>$$
>\sum_{k = 0}^n a_k z^k = 0,
>$$
>
>then
>
>$$
>|r| \le 1 + \max \left\{\left|\frac{a_{n-1}}{a_n}\right|, \left|\frac{a_{n-2}}{a_n}\right|, \dotsc, \left|\frac{a_{0}}{a_n}\right|\right\}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Second-Degree Polynomial Equations
>
>The solutions to the [complex polynomial equation](./Complex%20Polynomial%20Equations.md)
>
>$$
>az^2 + bz + c = 0
>$$
>
>are given by
>
>$$
>z = \frac{-b \pm \left(\sqrt{\frac{\sqrt{\delta_x^2 + \delta_y^2} + \delta_x}{2}}+ \mathrm{i} \mathop{\operatorname{sgn}}(\delta_y) \sqrt{\frac{\sqrt{\delta_x^2 + \delta_y^2}-\delta_x}{2}}\right)}{2a},
>$$
>
>where $\delta_x = \Re (b^2 - 4ac)$ and $\delta_y = \Im (b^2 - 4ac)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>
>>[!TIP] Tip: Complex Roots of Polynomial Equations
>>
>>If $a, b, c$ are [real numbers](../../Fields/The%20Real%20Numbers/The%20Real%20Numbers.md) and $b^2 - 4ac \lt 0$, then the above formula reduces to
>>
>>$$
>>x = -\frac{b}{2a} \pm \frac{\mathrm{i}}{2a}\sqrt{-b^2 + 4ac}
>>$$
>>
>