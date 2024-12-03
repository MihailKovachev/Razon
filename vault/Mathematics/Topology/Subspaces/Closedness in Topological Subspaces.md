>[!THEOREM] Theorem: Closedness in Topological Subspaces
>
>Let $(S, \tau_S)$ be a [subspace](Topological%20Subspace.md) of a [topological space](../Topological%20Spaces/Topological%20Space.md) $(X, \tau_X)$.
>
>A [set](../../Set%20Theory/Set.md) $A$ is [closed](../Topological%20Spaces/Closed%20Subset.md) in $(S, \tau_S)$ if and only if it is the [intersection](../../Set%20Theory/Operations%20with%20Sets/Intersection.md) of a [closed set](../Topological%20Spaces/Closed%20Subset.md) of $(X, \tau_X)$ with $S$.
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>- (I) If $A$ is a [closed set](../Topological%20Spaces/Closed%20Subset.md) of $(S, \tau_S)$, then there exists a [closed set](../Topological%20Spaces/Closed%20Subset.md) $C$ of $(X, \tau_X)$ such that $A = C \cap S$.
>>- (II) If there exists a [closed set](../Topological%20Spaces/Closed%20Subset.md) $C$ of $(X, \tau_X)$ such that $A = C \cap S$, then $A$ is [closed](../Topological%20Spaces/Closed%20Subset.md) in $(S, \tau_S)$.
>>
>>**Proof of (I):**
>>
>>Suppose that $A$ is [closed](../Topological%20Spaces/Closed%20Subset.md) in $(S, \tau_S)$. Then its [complement](../../Set%20Theory/Complement.md) $S \setminus A$ is [open](../Topological%20Spaces/Open%20Subset.md) in $(S, \tau_S)$ and, by definition, there exists an [open set](../Topological%20Spaces/Open%20Subset.md) $O_A$ of $(X, \tau_X)$ such that $S \setminus A = O_A \cap S$. Furthermore, $X \setminus O_A$ is [closed](../Topological%20Spaces/Closed%20Subset.md) in $(X, \tau_X)$, since $O_A$ is [open](../Topological%20Spaces/Open%20Subset.md) in $(X, \tau_X)$.
>>
>>**Proof of (II):**
>>
>>TODO
>>
>

>[!THEOREM] Theorem
>
>Let $(S, \tau_S)$ be a [subspace](Topological%20Subspace.md) of a [topological space](../Topological%20Spaces/Topological%20Space.md) $(X, \tau_X)$ and let $C$ be a [subset](../../Set%20Theory/Subset.md) of $S$.
>
>If $C$ is [closed](../Topological%20Spaces/Closed%20Subset.md) in $(S, \tau_S)$ and $S$ is [closed](../Topological%20Spaces/Closed%20Subset.md) $(X, \tau_X)$, then $C$ is also [closed](../Topological%20Spaces/Closed%20Subset.md) in $(X, \tau_X)$.
>
>>[!PROOF]-
>>
>>TODO
>>
>