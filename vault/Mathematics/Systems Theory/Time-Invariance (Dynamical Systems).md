---
tags:
    - systems-theory
    - mathematics
---

# Time-Invariance (Dynamical Systems)

>[!DEFINITION] Definition: Time-Invariant Dynamical System
>
>A [dynamical system](./Dynamical%20Systems.md) $(\mathbb{T}, \mathbb{W}, \mathfrak{B})$ is **time-invariant** if for each $\tau \in \mathbb{R}$ and each [trajectory](./Dynamical%20Systems.md) $w: \mathbb{T} \to \mathbb{W}$ with [$\tau$-shift](./Time%20Shift.md) $\sigma^{\tau} w: \mathcal{D}_{\sigma^{\tau}w} \to \mathbb{R}$, there exists some [trajectory](./Dynamical%20Systems.md) $v: \mathbb{T} \to \mathbb{W}$ whose [restriction](../Analysis/Functions/Restriction%20(Functions).md) on $\mathcal{D}_{\sigma^{\tau}w}$ is $\sigma^{\tau}w$:
>
>$$v(t) = \sigma^{\tau}w(t) \qquad \forall t \in \mathcal{D}_{\sigma^{\tau}w}$$
>
