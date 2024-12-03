>[!DEFINITION] Definition: Continuity at a Point
>
>Let $(X,\tau_X)$ and $(Y,\tau_Y)$ be [topological spaces](../Topological%20Spaces/Topological%20Space.md).
>
>A [function](../../Analysis/Functions/Function.md) $f: X \to Y$ is **continuous at** $x \in X$ iff for each [neighbourhood](../Topological%20Spaces/Neighbourhoods.md) $V$ of $f(x)$ there exists a neighbourhood $U$ of $x$ such that $f(U) \subset V$.
>
>^continuity-at-a-point
>

>[!DEFINITION] Definition: Continuity
>
>Let $(X,\tau_X)$ and $(Y,\tau_Y)$ be [topological spaces](../Topological%20Spaces/Topological%20Space.md).
>
>A [function](../../Analysis/Functions/Function.md) $f: X \to Y$ is **continuous on** $X$ or simply **continuous** iff it is [#^continuity-at-a-point](#^continuity-at-a-point) at each $x \in X$.
>
>>[!THEOREM]- Theorem: Equivalent Definition - Continuity via Openness
>>
>>Let $(X,\tau_X)$ and $(Y,\tau_Y)$ be [topological spaces](../Topological%20Spaces/Topological%20Space.md).
>>
>>A [function](../../Analysis/Functions/Function.md) $f: X \to Y$ is [#^continuity](#^continuity) if and only if the [inverse image](../../Analysis/Functions/Inverse%20Image.md) of each [open subset](../Topological%20Spaces/Open%20Subset.md) of $Y$ is an open subset of $X$.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>
>
>>[!THEOREM]- Theorem: Equivalent Definition  - Continuity via Closedness
>>
>>Let $(X,\tau_X)$ and $(Y,\tau_Y)$ be [topological spaces](../Topological%20Spaces/Topological%20Space.md).
>>
>>A [function](../../Analysis/Functions/Function.md) $f: X \to Y$ is [#^continuity](#^continuity) if and only if the [inverse image](../../Analysis/Functions/Inverse%20Image.md) of each [closed subset](../Topological%20Spaces/Closed%20Subset.md) of $Y$ is a [closed subset](../Topological%20Spaces/Closed%20Subset.md) of $X$.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>
>>[!THEOREM]- Theorem: Local Criterion
>>
>>Let $(X,\tau_X)$ and $(Y,\tau_Y)$ be [topological spaces](../Topological%20Spaces/Topological%20Space.md).
>>
>>A [function](../../Analysis/Functions/Function.md) $f: X \to Y$ is [#^continuity](#^continuity) if and only if each point $x \in X$ has a [neighbourhood](../Topological%20Spaces/Neighbourhoods.md) $N$ such that the [restriction](../../Analysis/Functions/Restriction.md) $f\big|_N$ is [#^continuity](#^continuity).
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>
>^continuity
>