---
tags:
    - measure-theory
    - mathematics
---

# Measures

>[!DEFINITION] Definition: Measure
>
>Let $(X, \Sigma)$ be a [measurable space](./Measures.md).
>
>A **measure** on $(X, \Sigma)$ is a [function](../Analysis/Functions/Functions.md) $\mu: \Sigma \to [0,\infty]$ from $\Sigma$ to the [subspace](../Topology/Topological%20Subspaces.md) of the non-negative [extended real number line](../Analysis/Real%20Analysis/Extended%20Real%20Number%20Line.md) with the following properties:
>
>    - $\mu(\varnothing) = 0$
>    - If $(S_i)_{i \in \mathbb{N}}$ is a [sequence](../Analysis/Functional%20Analysis/Sequences/Sequences.md) of [pairwise disjoint](../Set%20Theory/Intersections.md) [measurable sets](./σ-Algebras.md), then $\mu$ of their [union](../Set%20Theory/Unions.md) is the [sum](../Analysis/Real%20Analysis/Real%20Series.md) of $\mu(S_i)$.
>
>$$\mu\left(\bigcup_{i =1}^{\infty} S_i \right) = \sum_{i =1}^{\infty} \mu(S_i)$$
>

>[!THEOREM] Theorem: Monotonicity of Measures
>
>Let $(X, \Sigma)$ be a [measurable space](./Measures.md) and let $\mu: \Sigma \to [0,\infty]$ be a [measure](./Measures.md).
>
>For all [measurable sets](./Measurable%20Space.md) $A, B \in \Sigma$, if $A$ is a [subset](../Set%20Theory/Subsets.md) of $B$, then $\mu(A) \le \mu (B)$.
>
>$$A \subseteq B \implies \mu(A) \le \mu(B)$$
>
>>[!PROOF]-
>>
>>Let $A, B \in \Sigma$ with $A \subseteq B$. We can express $B$ as the [union](../Set%20Theory/Unions.md) of $A$ and $A$'s [complement](../Set%20Theory/Set%20Difference.md) $B \setminus A$ in $B$:
>>
>>$$B = A \cup (B \setminus A)$$
>>
>>We can express $B \setminus A$ as the [intersection](../Set%20Theory/Intersections.md) $B \cap (X \setminus A)$. Since $\Sigma$ is a [σ-algebra](./σ-Algebras.md) and $A \in \Sigma$, we know that $X \setminus A \in \Sigma$. Similarly, since both $B$ and $X \setminus A$ are [measurable](./Measurable%20Space.md), so is $B \setminus A = B \cap (X \setminus A)$. 
>>
>>Since $A$ and $B \setminus A$ are [disjoint](../Set%20Theory/Intersections.md), we have:
>>
>>$$\mu(B) = \mu(A \cup (B \setminus A)) = \mu(A) + \mu(B \setminus A)$$
>>
>>By definition, $\mu(B \setminus A) \ge 0$ and so $\mu(A) + \mu(B \setminus A) \ge \mu(A)$, i.e. $\mu(B) \ge \mu(A)$.
>>
>

>[!THEOREM] Theorem: Subadditivity
>
>Let $(X, \Sigma, \mu)$ be a [measure space](./Measure%20Space.md) and let $(S_k)_{k \in \mathcal{I}}$ be a [sequence](../Analysis/Functional%20Analysis/Sequences/Sequences.md) of [measurable sets](./Measurable%20Space.md).
>
>If $S$ is a [subset](../Set%20Theory/Subsets.md) of the [union](../Set%20Theory/Unions.md) of $(S_k)_{k \in \mathcal{I}}$ and is [measurable](./Measurable%20Space.md), then its [measure](./Measures.md) is less than or equal to the [series](../Analysis/Real%20Analysis/Extended%20Real%20Series.md) of the [measures](./Measures.md) of $(S_k)_{k \in \mathcal{I}}$:
>
>$$S \subseteq \bigcup_{k \in \mathcal{I}} S_k \text{ and } S \in \Sigma \implies \mu(S) \le \sum_{k \in \mathcal{I}} \mu(S_k)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity from Below
>
>Let $(X, \Sigma, \mu)$ be a [measure space](./Measure%20Space.md) and let $(S_k)_{k \in \mathcal{I}}$ be a [sequence](../Analysis/Functional%20Analysis/Sequences/Sequences.md) of [measurable sets](./Measurable%20Space.md).
>
>If $S_k \subseteq S_{k+1}$ for all $k \in [\min \mathcal{I}, \max \mathcal{I} - 1]$, then the [limit](../Analysis/Real%20Analysis/Limits%20(Extended%20Real%20Sequences).md) of the [sequence](../Analysis/Real%20Analysis/Extended%20Real%20Sequence.md) $(\mu (S_k))_{k \in \mathcal{I}}$ of the [measures](./Measures.md) of $(S_k)_{k \in \mathcal{I}}$ is the [measure](./Measures.md) of the [union](../Set%20Theory/Unions.md) $\bigcup_{k\in\mathcal{I}} S_k$:
>
>$$\lim_{k \to \infty} \mu(S_k) = \mu\left( \bigcup_{k \in \mathcal{I}} S_k \right)$$
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Continuity from Above
>
>Let $(X, \Sigma, \mu)$ be a [measure space](./Measure%20Space.md) and let $(S_k)_{k \in \mathcal{I}}$ be a [sequence](../Analysis/Functional%20Analysis/Sequences/Sequences.md) of [measurable sets](./Measurable%20Space.md).
>
>If $S_k \supseteq S_{k+1}$ for all $k \in [\min \mathcal{I}, \max \mathcal{I} - 1]$ and $\mu(S_n) < \infty$ for some $n \in \mathcal{I}$, then the [limit](../Analysis/Real%20Analysis/Limits%20(Extended%20Real%20Sequences).md) of the [sequence](../Analysis/Real%20Analysis/Extended%20Real%20Sequence.md) $(\mu (S_k))_{k \in \mathcal{I}}$ of the [measures](./Measures.md) of $(S_k)_{k \in \mathcal{I}}$ is the [measure](./Measures.md) of the [intersection](../Set%20Theory/Intersections.md) $\bigcap_{k\in\mathcal{I}} S_k$:
>
>$$\lim_{k \to \infty} \mu(S_k) = \mu\left( \bigcap_{k \in \mathcal{I}} S_k \right)$$
>
>>[!PROOF]-
>>
>>TODO
>>