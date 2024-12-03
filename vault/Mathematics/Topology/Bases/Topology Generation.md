>[!THEOREM] Theorem: Topology Generation
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces/Topological%20Space.md) and let $\mathcal{B}$ be a [base](Base%20for%20a%20Topological%20Space.md) for $(X, \tau)$.
>
>A [subset](../../Set%20Theory/Subset.md) $U \subseteq X$ is [open](../Topological%20Spaces/Open%20Subset.md) if and only if for each $u \in U$ there exists some $B \in \mathcal{B}$ such that $B \subseteq U$ and $u \in B$.
>
>>[!PROOF]-
>>
>>We need to prove two things separately:
>>- (I) If $U$ is [open](../Topological%20Spaces/Open%20Subset.md), then for each $u \in U$ there exists some $B_u \in \mathcal{B}$ such that $B_u \subseteq U$ and $u \in B_u$.
>>- (II) If for each $u \in U$ there exists some $B \in \mathcal{B}$ such that $B \subseteq U$ and $u \in B$, then $U$ is [open](../Topological%20Spaces/Open%20Subset.md).
>>
>>**Proof of (I):**
>>
>>Suppose $U$ is [open](../Topological%20Spaces/Open%20Subset.md). The fact that for each $u \in U$ there exists some $B_u \in \mathcal{B}$ such that $B_u \subseteq U$ and $u \in B_u$ follows immediately from the [base criterion](Base%20for%20a%20Topological%20Space.md).
>>
>>**Proof of (II):**
>>
>>Suppose that for each $u \in U$ there exists some $B \in \mathcal{B}$ such that $B \subseteq U$ and $u \in B$. Since $u$ is contained in $B_u$ and $B_u \subseteq U$, we know that $U = \bigcup_{u \in U} B_u$, i.e. $U$ is a [union](../../Set%20Theory/Operations%20with%20Sets/Union.md) of [open subsets](../Topological%20Spaces/Open%20Subset.md) and is thus [open](../Topological%20Spaces/Open%20Subset.md).
>>
>
>>[!INTUITION]
>>
>>This theorems allows us to determine the [topology](../Topological%20Spaces/Topology.md) $\tau$ given only a [base](Base%20for%20a%20Topological%20Space.md) for it.
>>
>
>^topology-generation
>
