>[!THEOREM] Theorem: Existence of a Topology with a Base
>
>Let $X$ be a [non-empty](../../Set%20Theory/The%20Empty%20Set.md) [set](../../Set%20Theory/Set.md) and let $\mathcal{B}$ be a [collection](../../Set%20Theory/Collections/Collection.md) of [subsets](../../Set%20Theory/Subset.md) of $X$.
>
>There exists a [topology](../Topological%20Spaces/Topology.md) $\tau_\mathcal{B}$ on $X$ such that $\mathcal{B}$ is a [base](Base%20for%20a%20Topological%20Space.md) for the [topological space](../Topological%20Spaces/Topological%20Space.md) $(X, \tau_\mathcal{B})$ if and only if
>- $X$ is the [union](../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) of $\mathcal{B}$, i.e. $X = \bigcup \mathcal{B}$, and
>- for each $B_1, B_2 \in \mathcal{B}$, the [intersection](../../Set%20Theory/Operations%20with%20Sets/Intersection.md) $B_1 \cap B_2$ is a union of a subset of $\mathcal{B}$.
>
>>[!PROOF]-
>>
>>We need to prove the following things separately:
>>- If there exists a [topology](../Topological%20Spaces/Topology.md) $\tau_\mathcal{B}$ on $X$ such that $\mathcal{B}$ is a [base](Base%20for%20a%20Topological%20Space.md) for the [topological space](../Topological%20Spaces/Topological%20Space.md) $(X, \tau_\mathcal{B})$, then $X = \bigcup \mathcal{B}$ and for each $B_1, B_2 \in \mathcal{B}$, the [intersection](../../Set%20Theory/Operations%20with%20Sets/Intersection.md) $B_1 \cap B_2$ is a [union](../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) of a subset of $\mathcal{B}$.
>>- If $\mathcal{B}$ is such that $X = \bigcup \mathcal{B}$ and for each $B_1, B_2 \in \mathcal{B}$, the [intersection](../../Set%20Theory/Operations%20with%20Sets/Intersection.md) $B_1 \cap B_2$ is a union of a [subset](../../Set%20Theory/Subset.md) of $\mathcal{B}$, then there exists a [topology](../Topological%20Spaces/Topology.md) $\tau_\mathcal{B}$ on $X$ such that $\mathcal{B}$ is a [base](Base%20for%20a%20Topological%20Space.md) for the [topological space](../Topological%20Spaces/Topological%20Space.md) $(X, \tau_\mathcal{B})$.
>>
>>**Part 1**: 
>>
>>Suppose that there exists a [topology](../Topological%20Spaces/Topology.md) $\tau_\mathcal{B}$ on $X$ such that $\mathcal{B}$ is a [base](Base%20for%20a%20Topological%20Space.md) for the [topological space](../Topological%20Spaces/Topological%20Space.md) $(X, \tau_\mathcal{B})$.
>>
>>By the definition of a [topology](../Topological%20Spaces/Topology.md), we have that $X$ is an [open set](../Topological%20Spaces/Open%20Subset.md). Since $\mathcal{B}$ is a [base](Base%20for%20a%20Topological%20Space.md) for $\tau_\mathcal{B}$, the [set](../../Set%20Theory/Set.md) $X$ can be expressed as a [union](../../Set%20Theory/Operations%20with%20Sets/Union.md) of a [subset](../../Set%20Theory/Subset.md) of $\mathcal{B}$. In particular, since $\mathcal{B}$ is comprised only of [subsets](../../Set%20Theory/Subset.md) of $X$, then $X = \bigcup \mathcal{B}$. Similarly, since $\mathcal{B}$ contains only [open sets](../Topological%20Spaces/Open%20Subset.md) by definition, the [intersection](../../Set%20Theory/Operations%20with%20Sets/Intersection.md) $B_1 \cap B_2$ is in $\tau_\mathcal{B}$, which completes the proof, since every [open set](../Topological%20Spaces/Open%20Subset.md) can be expressed as a [union](../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) of elements of $\mathcal{B}$ by definition.
>>
>>**Part 2:** 
>>
>>Suppose $\mathcal{B}$ is such that $X = \bigcup \mathcal{B}$ and for each $B_1, B_2 \in \mathcal{B}$, the [intersection](../../Set%20Theory/Operations%20with%20Sets/Intersection.md) $B_1 \cap B_2$ is a union of a [subset](../../Set%20Theory/Subset.md) of $\mathcal{B}$. Define $\tau_\mathcal{B}$ as the [collection](../../Set%20Theory/Collections/Collection.md) of all [subsets](../../Set%20Theory/Subset.md) of $X$ which are [unions](../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) of [subsets](../../Set%20Theory/Subset.md) of $\mathcal{B}$. 
>>
>>We need to show that $\tau_\mathcal{B}$ is a [topology](../Topological%20Spaces/Topology.md) on $X$. To do this we need to show the following three things:
>>- $X \in \tau_\mathcal{B}$ and $\varnothing \in \tau_\mathcal{B}$;
>>- $\tau_\mathcal{B}$ is closed under arbitrary [unions](../../Set%20Theory/Collections/Union%20of%20a%20Collection.md);
>>- The [intersection](../../Set%20Theory/Operations%20with%20Sets/Intersection.md) $U_1 \cap U_2$ of each $U_1, U_2 \in \tau_\mathcal{B}$ is in $\tau_\mathcal{B}$.
>>
>>The assumption that $X = \bigcup\mathcal{B}$ entails that $X \in \tau_\mathcal{B}$. The [empty set](../../Set%20Theory/The%20Empty%20Set.md) is a [subset](../../Set%20Theory/Subset.md) of $\mathcal{B}$ and since $\varnothing = \bigcup \varnothing$, we have that $\varnothing \in \tau_\mathcal{B}$.
>>
>>Consider now an arbitrary [subset](../../Set%20Theory/Subset.md) $T$ of $\tau_\mathcal{B}$. Since each $U \in T$ is a [union](../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) of a [subset](../../Set%20Theory/Subset.md) of $\mathcal{B}$, then $\bigcup T$ is also a [union](../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) of a [subset](../../Set%20Theory/Subset.md) $\mathcal{B}$, meaning that $\bigcup T \in \tau_\mathcal{B}$.
>>
>>Finally, we consider two [sets](../../Set%20Theory/Set.md) $U_1, U_2 \in \tau_\mathcal{B}$. By definition of $\tau_\mathcal{B}$, there exists some [subset](../../Set%20Theory/Subset.md) $\{B_i\}_{i \in I} \subseteq \mathcal{B}$ such that $U_1 = \bigcup_{i \in I} B_i$. Similarly, $U_2 = \bigcup_{j \in J} B_j$. We thus have
>>
>>$$U_1 \cap U_2 = \left(\bigcup_{i \in I} B_i\right) \cap \left(\bigcup_{j \in J} B_j\right) = \bigcup_{i \in i, j \in J} (B_i \cap B_j)$$
>>
>>By assumption, for all $i \in I$ and $j \in J$, the [intersection](../../Set%20Theory/Operations%20with%20Sets/Intersection.md) $(B_i \cap B_j)$ is a [union](../../Set%20Theory/Operations%20with%20Sets/Union.md) of a [subset](../../Set%20Theory/Subset.md) of $\mathcal{B}$. Therefore, the [union](../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) $\bigcup_{i \in i, j \in J} (B_i \cap B_j)$ is also a [union](../../Set%20Theory/Collections/Union%20of%20a%20Collection.md) of a [subset](../../Set%20Theory/Subset.md) of $\mathcal{B}$ and is thus in $\tau_\mathcal{B}$, Q.E.D.
>>
>