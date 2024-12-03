>[!THEOREM] Theorem: Continuity at a Point
>
>Let $(X, d_X)$ and $(Y, d_Y)$ be [metric spaces](Metric%20Space.md).
>
>A [function](../../Analysis/Functions/Function.md) $f: X \to Y$ is [](../Continuity/Continuity.md#^continuity-at-a-point) at $x_0 \in X$ if and only if for each [open ball](Open%20Ball.md) $B_\varepsilon(f(x_0))$ around $f(x_0)$ there exists some [open ball](Open%20Ball.md) $B_\delta(x_0)$ around $x_0$ such that if $x$ is inside $B_\delta(x_0)$, then $f(x)$ is inside $B_\varepsilon(f(x_0))$.
>
>$$
>\forall \varepsilon \gt 0, \exists \delta \gt 0: x \in B_\delta(x_0) \implies f(x) \in B_\varepsilon(f(x_0))
>$$
>
>>[!PROOF]-
>>
>>
>>
>