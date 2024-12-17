>[!THEOREM]+
>
>Let $(X, \tau)$ be a [topological space](Topological%20Space.md).
>
>A [subset](../../Set%20Theory/Subset.md) $S \subseteq X$ is [closed](Closed%20Subset.md) if and only if it is equal to its own [closure](../Interior,%20Exterior,%20Boundary/Closure.md).
>
>>[!PROOF]-
>>
>>We have to prove two things:
>>- (I) If $S$ is [closed](Closed%20Subset.md), then $S = \overline{S}$.
>>- (II) If $S = \overline{S}$, then $S$ is [closed](Closed%20Subset.md).
>>
>>**Proof of (I):**
>>
>>TODO
>>
>>**Proof of (II):**
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Limit Points of Closed Subsets
>
>Let $(X, \tau)$ be a [topological space](Topological%20Space.md).
>
>A [subset](../../Set%20Theory/Subset.md) $S \subseteq X$ is [closed](Closed%20Subset.md) if and only if it contains all of its [limit points](../Interior,%20Exterior,%20Boundary/Accumulation%20Point.md).
>
>>[!PROOF]-
>>
>>We need to prove two things separately:
>>- (I) If $S$ is [closed](Closed%20Subset.md), then every [limit point](../Interior,%20Exterior,%20Boundary/Accumulation%20Point.md) of $S$ lies in $S$.
>>- (II) If $S$ contains all of its [limit points](../Interior,%20Exterior,%20Boundary/Accumulation%20Point.md), then it is [closed](Closed%20Subset.md).
>>
>>**Proof of (I):**
>>
>>We prove this by contradiction. Suppose that $S$ is [closed](Closed%20Subset.md) and there exists a [limit point](../Interior,%20Exterior,%20Boundary/Accumulation%20Point.md) $p$ of $S$ which lies outside of $S$, i.e. $p \in X \setminus S$. We know that $X \setminus S$ is [open](Open%20Subset.md) because it is the [complement](../../Set%20Theory/Complement.md) of a [closed set](Closed%20Subset.md). However, since $p$ is a [limit point](../Interior,%20Exterior,%20Boundary/Accumulation%20Point.md) of $S$, every [open set](Open%20Subset.md) which contains $p$ must also contain an element of $S$. This implies that $X \setminus S$ contains an element of $S$ which is a contradiction.
>>
>>**Proof of (II):**
>>
>>Suppose that $S$ contains all of its [limit points](../Interior,%20Exterior,%20Boundary/Accumulation%20Point.md). This means that there are no points $p \in X\setminus S$ such that every [open set](Open%20Subset.md) $U$ which contains $p$ also contains another element of $S$. Alternatively, this means that each $p \in X \setminus S$ is contained in some [open set](Open%20Subset.md) $U_p$ such that $U_p \cap S = \varnothing$, i.e. $U_p \subseteq X \setminus S$. Therefore, the [union](../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) $\bigcup_{p \in X \setminus S} U_p$ is a [subset](../../Set%20Theory/Subset.md) of $X \setminus S$ and, since it contains every $p \in X \setminus S$, it means that $\bigcup_{p \in X \setminus S} U_p = X \setminus$. Since $X \setminus S$ is a [union](../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) of [open sets](Open%20Subset.md), it is itself [open](Open%20Subset.md) and so $S$ is [closed](Closed%20Subset.md).
>>
>

