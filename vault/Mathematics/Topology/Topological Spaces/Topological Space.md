---
tags:
    - topology
    - mathematics
---

# Topological Space

A **topological space** is a [set](../../Set%20Theory/Sets.md) $X$ for which a notion of [closeness](../Topology.md) has been defined. This is typically done using either a [neighborhood system](./Neighborhoods.md) or a [collection](../../Set%20Theory/Collections.md) of [subsets](../../Set%20Theory/Subsets.md) of $X$ with specific properties whose elements are either called [open sets](./Open%20Sets.md) or [closed sets](./Closed%20Sets.md), depending on precisely which properties we are talking about. 

The standard is to use a [collection](../../Set%20Theory/Collections.md) $\tau$ of [open sets](./Open%20Sets.md), call it a **topology** on $X$ and define the corresponding [topological space](./Topological%20Space.md) as the [ordered pair](../../Set%20Theory/Tuples.md) $(X, \tau)$. However, since using either one of the three approaches uniquely identifies the other two in a consistent way, it is in many cases better to think of all three being used at the same time. The [topological space](./Topological%20Space.md) would then be a [tuple](../../Set%20Theory/Tuples.md) $(X, \mathcal{N}, \tau_O, \tau_C)$, where $\mathcal{N}$ is a [neighborhood system](./Neighborhoods.md), $\tau_O$ is a **topology** in the sense of a [collection](../../Set%20Theory/Collections.md) of [open sets](./Open%20Sets.md) and $\tau_C$ is a **topology** in the sense of a [collection](../../Set%20Theory/Collections.md) of [closed sets](./Closed%20Sets.md) which are consistent with one another.

The important thing: specifying one of these defines a specific notion of [closeness](../Topology.md) on $X$. This is why $X$ itself is often called a [topological space](./Topological%20Space.md) as long as it is clear what notion of [closeness](../Topology.md) we mean. When multiple possible concepts of [closeness](../Topology.md) on $X$ are present within a given context, then we can explicitly say which one is meant by using either one of the three aforementioned approaches. Based on the terminology used, we can also infer which approach was originally used.
