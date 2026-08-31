---
tags:
    - real-mathematical-analysis
    - vector-mathematical-analysis
    - mathematical-analysis
    - mathematics
---

# Curvature

TODO

>[!DEFINITION] Definition: Curvature
>
>$$\kappa(t) = \frac{1}{s'(t)} ||\mathbf{T}'(t)||$$
>
>$s$ is [arclength function](./Arclength.md)
>
>$\mathbf{T}$ is [unit tangent vector](./Differentiation/Differentiability%20(Real%20Parametric%20Curves).md)
>
>>[!EXAMPLE] Example: Circle Curvature
>>
>>$$\frac{1}{r}$$
>>
>

>[!THEOREM] Theorem: Curvature in $\mathbb{R}^2$
>
>$$\kappa(t) = \frac{|x'(t)y''(t)-y'(t)x''(t)|}{(x'(t)^2+y'(t)^2)^{\frac{3}{2}}}$$
>
>>[!DEFINITION] Definition: Signed Curvature
>>
>>$$\tilde{\kappa}(t) = \frac{x'(t)y''(t)-y'(t)x''(t)}{(x'(t)^2+y'(t)^2)^{\frac{3}{2}}}$$
>>
>>If [arclength parametrization](./Arclength.md), then
>>
>>$$\tilde{\kappa}(t) = x'(t)y''(t)-y'(t)x''(t)$$
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem
>
>$$\tilde{\kappa}(t) = \frac{f''(t)}{(1+f'(t)^2)^{\frac{3}{2}}}$$
>
>>[!PROOF]-
>>
>>TODO
>>
>