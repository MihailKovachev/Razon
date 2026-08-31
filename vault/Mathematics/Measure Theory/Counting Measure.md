---
tags:
    - measure-theory
    - mathematics
---

# Counting Measure

>[!DEFINITION] Definition: Counting Measure
>
>Let $(X, \Sigma)$ be a [measurable space](./Measurable%20Space.md).
>
>The **counting measure** on $(X, \Sigma)$ is the [function](../Analysis/Functions/Functions.md) $\mu: \Sigma \to [0,\infty]$ from $\Sigma$ to the [subspace](../Topology/Topological%20Subspaces.md) of the non-negative [extended real number line](../Analysis/Real%20Analysis/Extended%20Real%20Number%20Line.md) defined using [cardinality](../Set%20Theory/Cardinality.md) as follows:
>
>$$\mu(S) \overset{\text{def}}{=} \begin{cases}|S|, & \text{if } S \text{ is finite} \\ \infty, & \text{if } S \text{ is infinite}\end{cases}$$
>