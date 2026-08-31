---
tags:
    - analysis
    - mathematics
---

# Metric

>[!DEFINITION] Definition: Metric
>
>A **metric** on a [set](../Set%20Theory/Sets.md) $M$ is a [real-valued function](./Real%20Analysis/Real-Valued%20Functions.md) $d: M \times M \to \mathbb{R}$ with the following properties:
>
>- Identity of indiscernibles: $d(x, y) \ge 0$ with $d(x, y) = 0 \iff x = y$ for all $x, y \in M$;
>- Symmetry: $d(x,y) = d(y,x)$ for all $x, y \in M$;
>- Triangle inequality: $d(x,z) \le d(x,y) + d(y,z)$ for all $x, y, z \in M$.
>