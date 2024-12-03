>[!DEFINITION] Definition: Connectedness of a Topological Space
>
>A [topological space](../Topological%20Spaces/Topological%20Space.md) is **connected** iff it cannot be represented as the [union](../../Set%20Theory/Operations%20with%20Sets/Union.md) of two [disjoint](../../Set%20Theory/Disjoint%20Sets.md), [nonempty](../../Set%20Theory/The%20Empty%20Set.md) [open sets](../Topological%20Spaces/Open%20Subset.md).
>
>>[!THEOREM]- Theorem: Equivalent Definition
>>
>>A [topological space](../Topological%20Spaces/Topological%20Space.md) $(X, \tau)$ is [#^connected-space](#^connected-space) if and only if its only [clopen subsets](../Topological%20Spaces/Clopen%20Set.md) are $\varnothing$ and $X$.
>>
>>>[!PROOF]-
>>>
>>>We need to prove two things:
>>>- (I) If $(X, \tau)$ is [#^connected-space](#^connected-space), then its only [clopen subsets](../Topological%20Spaces/Clopen%20Set.md) are $\varnothing$ and $X$.
>>>- (II) If the only [clopen subsets](../Topological%20Spaces/Clopen%20Set.md) of $(X, \tau)$ are $\varnothing$ and $X$, then $(X, \tau)$ is [#^connected-space](#^connected-space).
>>>
>>>**Proof of (I):**
>>>
>>>We prove this by contradiction.
>>>
>>>Suppose that $(X, \tau)$ is [#^connected-space](#^connected-space) and let $U \subset X$ be [clopen](../Topological%20Spaces/Clopen%20Set.md). If $U$ is [nonempty](../../Set%20Theory/The%20Empty%20Set.md), then so is $X \setminus U$. Since $U$ is [clopen](../Topological%20Spaces/Clopen%20Set.md), so is its [complement](../../Set%20Theory/Complement.md) $X \setminus U$.  More importantly, this implies that both $U$ and $X \setminus U$ are [open](../Topological%20Spaces/Open%20Subset.md). However, since $X = U \cup X\setminus U$, this means that $X$ can be represented as the [union](../../Set%20Theory/Operations%20with%20Sets/Union.md) of two [disjoint](../../Set%20Theory/Disjoint%20Sets.md), [nonempty](../../Set%20Theory/The%20Empty%20Set.md) [open sets](../Topological%20Spaces/Open%20Subset.md) and is thus not [disconnected](Disconnectedness.md), which is a contradiction.
>>>
>>>**Proof of (II):**
>>>
>>>We prove this by contradiction.
>>>
>>>Suppose that the only [clopen subsets](../Topological%20Spaces/Clopen%20Set.md) of $(X, \tau)$ are $\varnothing$ and $X$. Assume that $(X, \tau)$ is [disconnected](Disconnectedness.md), i.e. there exists two [disjoint](../../Set%20Theory/Disjoint%20Sets.md), [nonempty](../../Set%20Theory/The%20Empty%20Set.md) [open sets](../Topological%20Spaces/Open%20Subset.md) $U$ and $V$ such that $X = U \cup V$.
>>>
>>>
>>
>>
>
>^connected-space
>

>[!DEFINITION] Definition: Connectedness of a Subset
>
>Let $(X, \tau_X)$ be a [topological space](../Topological%20Spaces/Topological%20Space.md).
>
>A [subset](../../Set%20Theory/Subset.md) $S \subseteq X$ is **connected** iff the [subspace](../Subspaces/Topological%20Subspace.md) $(S, \tau_S)$ is [#^connected-space](#^connected-space).
>
>^connected-subset
>