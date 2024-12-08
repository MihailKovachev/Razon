>[!DEFINITION] Definitiom: Base for a Topological Space
>
>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces/Topological%20Space.md).
>
>A **base** for $(X,\tau)$ is a [collection](../../Set%20Theory/Collections/Collection.md) $\mathcal{B}$ of [open subsets](../Topological%20Spaces/Open%20Subset.md) of $X$ such that every open set can be represented as a [union](../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) of a [subset](../../Set%20Theory/Subset.md) of $\mathcal{B}$.
>
>>[!WARNING]
>>
>>This representation is not necessarily unique.
>>
>
>>[!THEOREM]- Theorem: Equivalent Definition
>>
>>Let $(X, \tau)$ be a [topological space](../Topological%20Spaces/Topological%20Space.md).
>>
>>A [collection](../../Set%20Theory/Collections/Collection.md) $\mathcal{B}$ of [open sets](../Topological%20Spaces/Open%20Subset.md) is a [base](.md) for $(X, \tau)$ if and only if for each [open set](../Topological%20Spaces/Open%20Subset.md) $U$ and each $u \in U$, there exists some $B \in \mathcal{B}$ such that $B \subseteq U$ and $u \in B$.
>>
>>>[!PROOF]-
>>>
>>>We need to prove two things:
>>>- (I) If $\mathcal{B}$ is a [base](.md) for $(X, \tau)$, then for each [open set](../Topological%20Spaces/Open%20Subset.md) $U$ and each $u \in U$, there exists some $B \in \mathcal{B}$ such that $B \subseteq U$ and $u \in B$.
>>>- (II) If for each [open set](../Topological%20Spaces/Open%20Subset.md) $U$ and each $u \in U$, there exists some $B \in \mathcal{B}$ such that $B \subseteq U$ and $u \in B$, then $\mathcal{B}$ is a  [base](.md) for $(X, \tau)$.
>>>
>>>**Part I:**
>>>
>>>Suppose $\mathcal{B}$ is a [base](.md) for $(X, \tau)$. Let $U$ be [open](../Topological%20Spaces/Open%20Subset.md) and let $u \in U$. Since $\mathcal{B}$ is a [base](.md), $U$ can be represented as a [union](../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) of some [subset](../../Set%20Theory/Subset.md) $\mathcal{B}_U \subseteq \mathcal{B}$, i.e. $U = \bigcup \mathcal{B}_U$. This implies that every $B \in \mathcal{B}_U$ is a [subset](../../Set%20Theory/Subset.md) of $U$. Moreover, since $u \in U$, there must exist at least one $B \in \mathcal{B}_U$ which contains $u$.
>>>
>>>**Part II:**
>>>
>>>Suppose that for each [open set](../Topological%20Spaces/Open%20Subset.md) $U \in \tau$ and each $u \in U$, there exists a $B(u) \in \mathcal{B}$ such that $B(u) \subseteq U$ and $u \in B(u)$. Since $B(u) \subseteq U$ for each $u \in U$, it holds that $\bigcup_{u \in U} B(u) \subseteq U$. Since this [union](../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) contains every $u \in U$, it follows that $\bigcup_{u \in U} B(u) = U$. Therefore, $U$ is a [union](../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) of a [subset](../../Set%20Theory/Subset.md) of $\mathcal{B}$, Q.E.D.
>>>
>>
>
