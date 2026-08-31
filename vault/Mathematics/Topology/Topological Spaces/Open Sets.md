---
tags:
    - topology
    - mathematics
---

# Open Sets

>[!DEFINITION] Definition: Open Set
>
>A [subset](../../Set%20Theory/Subsets.md) $U \subseteq X$ of a [topological space](./Topological%20Space.md) $X$ is **open** if it is a [neighborhood](./Neighborhoods.md) of each of its own elements.
>

>[!THEOREM] Theorem: The Fundamental Properties of Open Sets
>
>If $X$ is a [topological space](./Topological%20Space.md), then:
>
>    - The [empty set](../../Set%20Theory/Sets.md) $\varnothing$ and $X$ itself are [open](#Open%20Sets).
>    - If $\mathcal{S}$ is a [collection](../../Set%20Theory/Collections.md) of [open sets](#Open%20Sets), then its [union](../../Set%20Theory/Unions.md) is also [open](#Open%20Sets).
>    - If $\mathcal{S}$ is a [finite](../../Set%20Theory/Cardinality.md) [collection](../../Set%20Theory/Collections.md) of [open sets](#Open%20Sets), then its [intersection](../../Set%20Theory/Intersections.md) is also [open](#Open%20Sets).
>
>>[!PROOF]-
>>
>>We need to prove three things:
>>
>>- (I) The [empty set](../../Set%20Theory/Sets.md) $\varnothing$ and $X$ itself are [open](#Open%20Sets).
>>- (II) If $\mathcal{S}$ is a [collection](../../Set%20Theory/Collections.md) of [open sets](#Open%20Sets), then its [union](../../Set%20Theory/Unions.md) is also [open](#Open%20Sets).
>>- (III) If $\mathcal{S}$ is a [finite](../../Set%20Theory/Cardinality.md) [collection](../../Set%20Theory/Collections.md) of [open sets](#Open%20Sets), then its [intersection](../../Set%20Theory/Intersections.md) is also [open](#Open%20Sets).
>>
>>We assume that the [topological space](./Topological%20Space.md) is characterized by a [neighborhood system](./Neighborhoods.md) $\mathcal{N}$.
>>
>>**Proof of (I):**
>>
>>To prove that $\varnothing$ is [open](#Open%20Sets), we must show that $\varnothing \in \mathcal{N}(x)$ for all $x \in \varnothing$. This is vacuously true because $\varnothing$ contains no elements. Thus, $\varnothing$ is [open](#Open%20Sets).
>>
>>To prove $X$ is [open](#Open%20Sets), let $x \in X$. By definition, the [neighborhood system](./Neighborhoods.md) $\mathcal{N}(x)$ has at least one [neighborhood](./Neighborhoods.md) $N \in \mathcal{N}(x)$. Since $N$ is a [subset](../../Set%20Theory/Subsets.md) of $X$, one of the defining properties of a [neighborhood system](./Neighborhoods.md) tells us that $X$ is also a [neighborhood](./Neighborhoods.md) of $x$. Since this holds for all $x \in X$, we know that $X$ is [open](#Open%20Sets).
>>
>>**Proof of (II):**
>>
>>To show that $\bigcup \mathcal{S}$ is [open](#Open%20Sets), we need to show that $\bigcup \mathcal{S} \in \mathcal{N}(x)$ for each $x \in \bigcup \mathcal{S}$. 
>>
>>Let $x \in \bigcup \mathcal{S}$. By the definition of a [union](../../Set%20Theory/Unions.md), there exists at least one $V \in \mathcal{S}$ such that $x \in V$. Since $\mathcal{S}$ is a [collection](../../Set%20Theory/Collections.md) of [open sets](#Open%20Sets), then $V$ must be [open](#Open%20Sets). Since $x \in V$, the definition of an [open set](#Open%20Sets) tells us that $V$ is a [neighborhood](./Neighborhoods.md) of $x$. Since $V \subseteq \bigcup \mathcal{S}$ and $V \in \mathcal{N}(x)$, one of the defining properties of a [neighborhood system](./Neighborhoods.md) tells us that $\bigcup \mathcal{S}$ is also a [neighborhood](./Neighborhoods.md) of $x$. 
>>
>>This holds for all $x \in \bigcup \mathcal{S}$, so $\bigcup \mathcal{S}$ is [open](./Open%20Sets.md).
>>
>>**Proof of (III):**
>>
>>If $\mathcal{S}$ is [empty](../../Set%20Theory/Sets.md) ($|\mathcal{S}| = 0$), its [intersection](../../Set%20Theory/Intersections.md) $\bigcap \mathcal{S}$ is $X$ itself, which is an [open set](./Open%20Sets.md).
>>
>>If $\mathcal{S}$ is [non-empty](../../Set%20Theory/Sets.md), then let $\mathcal{S} = \{U_1, U_2, \dots, U_n\}$ and let $x \in \bigcap \mathcal{S}$. By the definition of an [intersection](../../Set%20Theory/Intersections.md), we know that $x \in U_i$ for every $i \in \{1, 2, \dots, n\}$. 
>>
>>Since $\mathcal{S}$ is a [collection](../../Set%20Theory/Collections.md) of [open sets](./Open%20Sets.md), we know that each $U_i$ is [open](./Open%20Sets.md). Since $x \in U_i$ for every $i \in \{1, 2, \dots, n\}$, it follows that $U_1, \dotsc, U_n$ are [neighborhoods](./Neighborhoods.md) of $x$. Therefore, one of the defining properties of a [neighborhood system](./Neighborhoods.md) tells us that $\bigcap \mathcal{S} = U_1 \cap U_2 \cap \dots \cap U_n$ is a [neighborhood](./Neighborhoods.md) of $x$. 
>>
>>Since this is true for all $x \in \bigcap \mathcal{S}$, it follows that $\bigcap \mathcal{S}$ is [open](./Open%20Sets.md).
>>
>

>[!THEOREM] Theorem: Neighborhoods via Open Sets
>
>Let $X$ be a [topological space](./Topological%20Space.md) and let $x \in X$.
>
>A [subset](../../Set%20Theory/Subsets.md) $N \subseteq X$ is a [neighborhood](./Neighborhoods.md) of $x$ if and only if there exists some [open set](./Open%20Sets.md) $U$ with $x \in U$ and $U \subseteq N$.
>
>>[!PROOF]-
>>
>>We need to prove two things:
>>
>>- (I) If $N$ is a [neighborhood](./Neighborhoods.md) of $x$, then there exists some [open set](./Open%20Sets.md) $U$ with $x \in U$ and $U \subseteq N$.
>>- (II) If there exists some [open set](./Open%20Sets.md) $U$ with $x \in U$ and $U \subseteq N$, then $N$ is a [neighborhood](./Neighborhoods.md) of $x$.
>>
>>**Proof of (I):**
>>
>>Let $U$ be the [subset](../../Set%20Theory/Subsets.md) of $X$ containing all points which have $N$ as a [neighborhood](./Neighborhoods.md):
>>
>>$$U = \{p \in X \mid N \in \mathcal{N}(p)\}$$
>>
>>Since $N$ is a [neighborhood](./Neighborhoods.md) of $x$ by assumption, it immediately follows that $x \in U$. Furthermore, one of the defining properties of a [neighborhood system](./Neighborhoods.md) tells us that if $p \in X$, then $p$ is contained in all of its [neighborhoods](./Neighborhoods.md), i.e. if $N \in \mathcal{N}(p)$, then $p \in N$. Therefore, $U \subseteq N$.
>>
>>We have thus shown that $x \in U$ and $U \subseteq N$. Finally, we must show that $U$ is [open](./Open%20Sets.md). 
>>
>>Let $p \in U$. By the definition of $U$, we know that $N \in \mathcal{N}(p)$. The defining property of a [neighborhood system](./Neighborhoods.md) tells us that there exists some $M \in \mathcal{N}(p)$ with $M \subseteq N$ such that $N \in \mathcal{N}(p')$ for all $p' \in M$. The condition $N \in \mathcal{N}(p')$ is the defining property of $U$ and so $p' \in U$ for all $p' \in M$. Therefore, $M \subseteq U$. Since $M$ is a [neighborhood](./Neighborhoods.md) of $p$ and since $M \subseteq U$, one of the defining properties of a [neighborhood system](./Neighborhoods.md) tells us that $U$ is also a [neighborhood](./Neighborhoods.md) of $p$. Since this holds for all $p \in U$, it follows that $U$ is [open](./Open%20Sets.md).
>>
>>**Proof of (II):**
>>
>>The definition of an [open set](./Open%20Sets.md) tells us that $U$ is a [neighborhood](./Neighborhoods.md) of $x$. Therefore, one of the defining properties of a [neighborhood system](./Neighborhoods.md) tells us that $N$ must also be a [neighborhood](./Neighborhoods.md) of $x$, since $U \subseteq N$.
>>
>

>[!THEOREM] Theorem: Topology from Open Sets
>
>Let $X$ be a [set](../../Set%20Theory/Sets.md) and let $\mathcal{U}$ be a [collection](../../Set%20Theory/Collections.md) of [subsets](../../Set%20Theory/Subsets.md) of $X$ with the following properties:
>
>- The [empty set](../../Set%20Theory/Sets.md) $\varnothing$ and $X$ itself are in $\mathcal{U}$.
>
>$$\varnothing \in \mathcal{U} \qquad X \in \mathcal{U}$$
>
>- If $\mathcal{S}$ is a [subcollection](../../Set%20Theory/Collections.md) of $\mathcal{U}$, then its [union](../../Set%20Theory/Unions.md) is in $\mathcal{U}$.
>
>$$\mathcal{S} \subseteq \mathcal{U} \implies \bigcup \mathcal{S} \in \mathcal{U}$$
>
>- If $\mathcal{S}$ is a [finite](../../Set%20Theory/Cardinality.md) [subcollection](../../Set%20Theory/Collections.md) of $\mathcal{U}$, then its [intersection](../../Set%20Theory/Intersections.md) is in $\mathcal{U}$.
>
>$$\mathcal{S} \subseteq \mathcal{U} \qquad \text{and} \qquad |\mathcal{S}| \in \mathbb{N}_0 \implies \bigcap \mathcal{S} \in \mathcal{U}$$
>
>Then there exists a unique [neighborhood system](./Neighborhoods.md) $\mathcal{N}$ on $X$ whose [open sets](./Open%20Sets.md) are precisely the elements of $\mathcal{U}$.
>
>>[!DEFINITION] Definition: Topology via Open Sets
>>
>>Any [collection](../../Set%20Theory/Collections.md) of [subsets](../../Set%20Theory/Subsets.md) of $X$ with the aforementioned properties is known as a **topology** on $X$.
>>
>>>[!IMPORTANT]
>>>
>>>This is the standard definition of "topology" as a mathematical object.
>>>
>>
>
>>[!PROOF]-
>>
>>Let $\mathcal{N}: X \to \mathcal{P}(\mathcal{P}(X))$ be defined according to the theorem which identifies [neighborhoods](./Neighborhoods.md) and [open sets](./Open%20Sets.md):
>>
>>$$\mathcal{N}(x) = \{N \subseteq X \mid \exists U \in \mathcal{U} \text{ such that } x \in U \subseteq N\}$$
>>
>>We need to prove three things: 
>>
>>- (I) $\mathcal{N}$ is a [neighborhood system](./Neighborhoods.md) on $X$.
>>- (II) The [open sets](./Open%20Sets.md) w.r.t. $\mathcal{N}$ are precisely the elements of $\mathcal{U}$.
>>- (III) $\mathcal{N}$ is unique.
>>
>>**Proof of (I):**
>>
>>We need to prove the four defining properties of a [neighborhood system](./Neighborhoods.md):
>>
>>    - If $N \in \mathcal{N}(x)$, then $x \in N$: Let $x \in X$ and let $N \in \mathcal{N}(x)$. By the definition of $\mathcal{N}$, there exists some $U \in \mathcal{U}$ with $x \in U \subseteq N$. Therefore, $x \in N$.
>>    - If $N \in \mathcal{N}(x)$ and $N \subseteq M \subseteq X$, then $M \in \mathcal{N}(x)$: Let $x \in X$ and let $N \in \mathcal{N}(x)$. By the definition of $\mathcal{N}$, there exists some $U \in \mathcal{U}$ such that $x \in U \subseteq N$. Since $N \subseteq M$, we have $U \subseteq M$ and so $x \in U \subseteq M$. Therefore, $M \in \mathcal{N}(x)$.
>>    - If $N_1, \dotsc, N_p \in \mathcal{N}(x)$, then $N_1 \cap \cdots \cap N_p \in \mathcal{N}(x)$. Let $x \in X$ and let $N_1, \dotsc, N_p \in \mathcal{N}(x)$. By the definition of $\mathcal{N}$, there exist some $U_1, \dotsc, U_p \in \mathcal{U}$ such that $x \in U_1 \subseteq N_1, \dotsc, x \in U_p \subseteq N_p$. Consequently, $x \in U_1 \cap \cdots \cap U_p \subseteq N_1 \cap \cdots \cap N_p$. From the third assumption for $\mathcal{U}$, it follows that $U_1 \cap \cdots \cap U_p \in \mathcal{U}$. Therefore, $N_1 \cap \cdots \cap N_p \in \mathcal{N}(x)$.
>>    - If $N \in \mathcal{N}(x)$, then there exists some $M \in \mathcal{N}(x)$ with $M \subseteq N$ and $N \in \mathcal{N}(y)$ for each $y \in M$: Let $x \in X$ and let $N \in \mathcal{N}(x)$. By the definition of $\mathcal{N}$, there exists some $U \in \mathcal{U}$ such that $x \in U \subseteq N$. Let $M = U$. We have $x \in U \subseteq M$ and so $M \in \mathcal{N}(x)$. For each $y \in M$ (i.e. $y \in U$), we have $y \in U \subseteq N$ and so $N \in \mathcal{N}(y)$.
>>
>>**Proof of (II):**
>>
>>Let $\mathcal{U}_{\mathcal{N}}$ be the [collection](../../Set%20Theory/Collections.md) of [open sets](./Open%20Sets.md) w.r.t. the [neighborhood system](./Neighborhoods.md) $\mathcal{N}$. By definition, $O \in \mathcal{U}_{\mathcal{N}}$ if and only if $O \in \mathcal{N}(x)$ for each $x \in O$. We need to show that $\mathcal{U}_{\mathcal{N}} = \mathcal{U}$.
>>
>>Let $U \in \mathcal{U}$ and let $x \in U$. We have $x \in U \subseteq U$ and so the definition of $\mathcal{N}$ tells us that $U \in \mathcal{N}(x)$. This holds for every $x \in U$ and so $U \in \mathcal{U}_{\mathcal{N}}$, i.e. $\mathcal{U} \subseteq \mathcal{U}_{\mathcal{N}}$.
>>
>>Let $O \in \mathcal{U}_{\mathcal{N}}$. By the definition of $\mathcal{U}_{\mathcal{N}}$, for each $x \in O$, we have $O \in \mathcal{N}(x)$. Therefore, using the definition of $\mathcal{N}$, we get that for each $x \in O$, there exists some $U_x \in \mathcal{U}$ such that $x \in U_x \subseteq O$. We can express $O$ as the [union](../../Set%20Theory/Unions.md) $O = \bigcup_{x \in O} \{x\}$. Since $\{x\} \subseteq U_x \subseteq O$ for each $x \in O$, we have $O = \bigcup_{x \in O} U_x$. The second assumption for $\mathcal{U}$ implies that $\bigcup_{x \in O} U_x \in \mathcal{U}$ and so $O \in \mathcal{U}$, i.e. $\mathcal{U}_{\mathcal{N}} \subseteq \mathcal{U}$.
>>
>>Since $\mathcal{U} \subseteq \mathcal{U}_{\mathcal{N}}$ and $\mathcal{U}_{\mathcal{N}} \subseteq \mathcal{U}$, we have $\mathcal{U} = \mathcal{U}_{\mathcal{N}}$.
>>
>>**Proof of (III):**
>>
>>Suppose $\mathcal{N}'$ is another [neighborhood system](./Neighborhoods.md) on $X$ which generates the exact same [open sets](./Open%20Sets.md) $\mathcal{U}$ as $\mathcal{N}$. We need to show that $\mathcal{N}(x) = \mathcal{N}'(x)$ for all $x \in X$.
>>
>>Let $N \in \mathcal{N}(x)$. By the definition of $\mathcal{N}$, there exists some $U \in \mathcal{U}$ such that $x \in U \subseteq N$. By assumption, $U$ must be [open](./Open%20Sets.md) w.r.t. $\mathcal{N}'$. Therefore, $U$ is considered a [neighborhood](./Neighborhoods.md) of $x$ under $\mathcal{N}'$, i.e. $U \in \mathcal{N}'(x)$. Since $U \subseteq N$ and $U \in \mathcal{N}'(x)$, one of the defining properties of [neighborhood systems](./Neighborhoods.md) tells us that $N \in \mathcal{N}'(x)$. Thus, $\mathcal{N}(x) \subseteq \mathcal{N}'(x)$.
>>
>>Let $N \in \mathcal{N}'(x)$. Let $V = \{y \in X \mid N \in \mathcal{N}'(y)\}$. Let $z \in V$. By the definition of $V$, we know that $N \in \mathcal{N}'(z)$. One of the defining properties of [neighborhood system](./Neighborhoods.md) tells us that there exists some $M \in \mathcal{N}'(z)$ with $M \subseteq N$ such that $N \in \mathcal{N}'(w)$ for all $w \in M$. However, this is the defining condition for being an element of $V$. Therefore, $w \in V$ for all $w \in M$ and so $M \subseteq V$. Since $M$ is a [neighborhood](./Neighborhoods.md) of $z$ and since $M \subseteq V$, another of the defining properties of [neighborhood systems](./Neighborhoods.md) tells us that $V$ must be a [neighborhood](./Neighborhoods.md) of $z$ w.r.t. $\mathcal{N}'$. This holds for all $z \in V$ and so $V$ is [open](./Open%20Sets.md) w.r.t. $\mathcal{N}'$, i.e. $V \in \mathcal{U}$. We see that $x \in V$, i.e. $x \in V \subseteq N$, and since $V \in \mathcal{U}$, it follows that $N \in \mathcal{N}(x)$ by the definition of $\mathcal{N}$. Therefore, $\mathcal{N}'(x) \subseteq \mathcal{N}(x)$.
>>
>>Since $\mathcal{N}(x) \subseteq \mathcal{N}'(x)$ and $\mathcal{N}'(x) \subseteq \mathcal{N}(x)$, we get that $\mathcal{N}'(x) = \mathcal{N}(x)$.
>>
>>The above holds for all $x \in X$ and so $\mathcal{N} = \mathcal{N}'$.
>>
>

>[!THEOREM] Theorem: Open Sets via Closed Sets
>
>Let $X$ be a [topological space](./Topological%20Space.md).
>
>A [subset](../../Set%20Theory/Subsets.md) $S \subseteq X$ is [open](./Open%20Sets.md) if and only if its [complement](../../Set%20Theory/Set%20Difference.md) $X \setminus S$ is [closed](./Closed%20Sets.md).
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Open Set via Interior
>
>A [subset](../../Set%20Theory/Subsets.md) $S \subseteq X$ of a [topological space](./Topological%20Space.md) $X$ is [open](./Open%20Sets.md) if and only if it is equal to its own [interior](./Interior%20(Topology).md).
>
>$$S = \operatorname{int} S$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Open Set via Boundary
>
>A [subset](../../Set%20Theory/Subsets.md) $S \subseteq X$ of a [topological space](./Topological%20Space.md) $X$ is [open](./Open%20Sets.md) if and only if it contains none of its [boundary points](./Boundary%20(Topology).md):
>
>$$S \text{ is open } \iff S \cap \partial S = \varnothing$$
>
>>[!PROOF]-
>>
>>TODO
>>
>