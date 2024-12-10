>[!DEFINITION] Definition: Closed Set
>
>Let $(S, \tau)$ be a [topological space](Topological%20Space.md).
>
>A [subset](../../Set%20Theory/Subset.md) $U$ of $S$ is **closed** if its [complement](../../Set%20Theory/Complement.md) $S \setminus U$ is an [open set](Open%20Subset.md).
>
>>[!THEOREM]
>>
>>Let $(S, \tau)$ be a [topological space](Topological%20Space.md).
>>
>>A [subset](../../Set%20Theory/Subset.md) $C \subseteq S$ is [closed](Closed%20Subset.md) if and only if for each $x$ in its [complement](../../Set%20Theory/Complement.md) $S \setminus C$ there exists a [neighbourhood](Neighbourhoods.md) $N$ of $x$ such that $N \subseteq S \setminus C$.
>>
>>>[!PROOF]-
>>>
>>>TODO
>>>
>>
>

>[!THEOREM] Theorem: Intersection of Closed Sets
>
>Let $(S, \tau)$ be a [topological space](Topological%20Space.md).
>
>The [intersection](../../Set%20Theory/Collections/Intersection%20of%20a%20Collection.md) of any [collection](../../Set%20Theory/Collections/Collection.md) of [closed subsets](Closed%20Subset.md.md) is also closed.
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Union of Closed Sets
>
>Let $(S, \tau)$ be a [topological space](Topological%20Space.md).
>
>The [union](../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) of any finite [collection](../../Set%20Theory/Collections/Collection.md) of [closed subsets](Closed%20Subset.md.md) is also closed.
>
>>[!PROOF]-
>>
>>Let $S_1,\cdots,S_n$ be closed sets. We need to show that $\bigcup \{S_1,\cdots, S_n\} = S_1 \cup \cdots \cup S_n$ is closed. According to the definition of a closed set, this means we must show that $S \setminus (S_1 \cup \cdots \cup S_n)$ is [open](Open%20Subset.md).
>>
>>By the [distributive law](../../Set%20Theory/Operations%20with%20Sets/Distributive%20Laws%20for%20Set%20Operations.md)
>>
>>$$
>>S \setminus (S_1 \cup \cdots \cup S_n) = (S\setminus S_1) \cap \cdots \cap (S \setminus S_n)
>>$$
>>
>>The sets $S_1,\cdots,S_n$ are closed and by definition their [complements](../../Set%20Theory/Complement.md) $S\setminus S_1,\cdots, S \setminus S_n$ are open. The right-hand side is thus an intersection of open sets and is, therefore, open itself. This means that the complement $S \setminus S_1 \cup \cdots \cup S_n$ is open and so $S_1 \cup \cdots \cup S_n$ is closed.
>>
>