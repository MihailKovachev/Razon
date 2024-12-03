>[!THEOREM] Theorem: Continuity of Composition
>
>Let $(X, \tau_X)$, $(Y, \tau_Y)$ and $(Z, \tau_Z)$ be [topological spaces](../Topological%20Spaces/Topological%20Space.md).
>
>If $f: X \to Y$ and $g: Y \to Z$ are [](Continuity.md#^continuity), then their [composition](../../Analysis/Functions/Composition.md) $g \circ f: X \to Z$ is also [](Continuity.md#^continuity).
>
>>[!PROOF]-
>>
>>Recall the following theorem:
>>
>>![](Continuity%20of%20Restrictions.md#^continuity-via-openness)
>>
>>Hence, we need to prove only that if $U$ is [open](../Topological%20Spaces/Open%20Subset.md) in $(Z, \tau_Z)$, then its [inverse image](../../Analysis/Functions/Inverse%20Image.md)  $(g\circ f)^{-1}(U)$ is [open](../Topological%20Spaces/Open%20Subset.md) in $(X, \tau_X)$.
>>
>>
>>
>>Let $U$ be [open](../Topological%20Spaces/Open%20Subset.md) in $(Z, \tau_Z)$. We know that $(g\circ f)^{-1}(U) = f^{-1}(g^{-1}(U))$. Since $g$ is [](Continuity.md#^continuity) and $U$ is [open](../Topological%20Spaces/Open%20Subset.md) in $(Z, \tau_Z)$, the aforementioned theorem tells us that $g^{-1}(U)$ is [open](../Topological%20Spaces/Open%20Subset.md) in $(Y, \tau_Y)$. Analogously, since $f$ is [](Continuity.md#^continuity) and $g^{-1}(U)$ is [open](../Topological%20Spaces/Open%20Subset.md) in $(Y, \tau_Y)$, the theorem tells us that $f^{-1}(g^{-1}(U))$ is [](Continuity.md#^continuity) in $(X,\tau_X)$.
>>
>