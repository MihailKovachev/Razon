---
tags:
    - theoretical-computer-science
    - computer-science
---

# Deterministic Finite State Machines

>[!DEFINITION] Definition: Deterministic Finite State Machine
>
>A **deterministic finite state machine** (**DFSM**) or **deterministic finite automaton** (**DFA**) is a [tuple](../../Mathematics/Set%20Theory/Tuples.md) $(\Sigma, S, s_0, \delta, F)$, where:
>- $\Sigma$ is a [finite](../../Mathematics/Set%20Theory/Cardinality.md), [non-empty](../../Mathematics/Set%20Theory/Sets.md) [set](../../Mathematics/Set%20Theory/Sets.md) known as the **input alphabet**;
>- $S$ is a [finite](../../Mathematics/Set%20Theory/Cardinality.md), [non-empty](../../Mathematics/Set%20Theory/Sets.md) [set](../../Mathematics/Set%20Theory/Sets.md) known as the **set of states**;
>- $s_0 \in S$ is known as the **initial state**;
>- $\delta$ is a [function](../../Mathematics/Analysis/Functions/Functions.md) $\delta: S \times \Sigma \to S$ known as the **state-transition function**;
>- $F \subseteq S$ is known as the **set of accepted states** or the **set of final states**.
>

>[!DEFINITION] Definition: Extended Transition Function
>
>Let $\mathcal{S} = (\Sigma, S, s_0, \delta, F)$ be a [finite state machine](./Finite%20State%20Machines.md):
>
>The **extended transition function** of $\mathcal{S}$ is the [function](../../Mathematics/Analysis/Functions/Functions.md) $\hat{\delta}: S \times \Sigma^{\ast} \to S$ defined in the following way:
>- *Base case:* For each [state](./Finite%20State%20Machines.md) $s \in S$, we have $\hat{\delta}(s, \varepsilon) = s$ where $\varepsilon$ is the empty string;
>- *Recursive case:* For each [state](./Finite%20State%20Machines.md) $s \in S$, each string $w \in \Sigma^{\ast}$ and each symbol $a \in \Sigma$, we have $\hat{\delta}(s, wa) = \delta(\hat{\delta}(s, w), a)$.
>

>[!DEFINITION] Definition: Acceptance and Rejection
>
>Let $\text{DFSM} = (\Sigma, S, s_0, \delta, F)$ be a [deterministic finite state machine](./Finite%20State%20Machines.md) and let $w \in \Sigma^{\ast}$.
>
>We say that $\text{DFSM}$ **accepts** $w$ if the [extended transition function](./Finite%20State%20Machines.md) yields an [accepted state](./Finite%20State%20Machines.md) on $(s_0, w)$:
>
>$$
>\hat{\delta}(s_0, w) \in F
>$$
>
>We say that $\text{DFSM}$ **rejects** $w$ if the [extended transition function](./Finite%20State%20Machines.md) does *not* yield an [accepted state](./Finite%20State%20Machines.md) on $(s_0, w)$:
>
>$$
>\hat{\delta}(s_0, w) \notin F
>$$
>