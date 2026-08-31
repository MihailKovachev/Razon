---
tags:
    - classical-mechanics
    - mathematics
---

# Lagrangian Formalism

The **Lagrangian formalism** of [classical mechanics](./Classical%20Mechanics.md) is a framework which can be used to predict how a [system](../Physical%20Systems.md) of [point particles](./Point%20Particles.md) evolves over time. It is based on an empirically derived principle stating that for each set of [generalized coordinates](./Generalized%20Coordinates.md) and their [generalized velocities](./Generalized%20Coordinates.md) there is a special [function](../../Mathematics/Analysis/Real%20Analysis/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md) such that the  [system](../Physical%20Systems.md) evolves in such a way so as to either [minimize](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Extrema%20of%20Real%20Functions.md) or [maximize](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Extrema%20of%20Real%20Functions.md) a particular [integral](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md).

>[!DEFINITION] Definition: Lagrangian
>
>Let $q_1, \dotsc, q_s$ and $\dot{q}_1, \dotsc, \dot{q}_s$ are any [generalized coordinates](./Generalized%20Coordinates.md) and their [generalized velocities](./Generalized%20Coordinates.md) for a [system](../Physical%20Systems.md) $\mathcal{S}$ of [point particles](./Point%20Particles.md).
>
>A **Lagrangian** of $\mathcal{S}$ is [function](../../Mathematics/Analysis/Real%20Analysis/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables/Real-Valued%20Functions%20of%20Multiple%20Real%20Variables.md)
>
>$$
>\mathcal{L}(q_1, \dotsc, q_s, \dot{q}_1, \dotsc, \dot{q}_s, t)
>$$
>
>of $q_1, \dotsc, q_s$, $\dot{q}_1, \dotsc, \dot{q}_s$ and the time $t$.
>
>>[!DEFINITION] Definition: Action
>>
>>Let $t_1$ and $t_2$ be two [moments in time](./Classical%20Mechanics.md).
>>
>>The **action** of a [path](./Generalized%20Coordinates.md) $\boldsymbol{q}: [t_1; t_2] \to \mathbb{R}^s$ in [configuration space](./Generalized%20Coordinates.md) is defined via the following [integral](../../Mathematics/Analysis/Real%20Analysis/Real%20Functions/Integration/Riemann%20Integrals%20(Real%20Functions).md):
>>
>>$$
>>S[\boldsymbol{q}] \overset{\text{def}}{=} \int_{t_1}^{t_2} \mathcal{L}(q_1(t), \dotsc, q_s(t), \dot{q}_1(t), \dotsc, \dot{q}_s(t), t) \mathop{\mathrm{d}t}
>>$$
>>
>

The [Lagrangian formalism](./Lagrangian%20Formalism.md) is based on the principle that for each set of [generalized coordinates](./Generalized%20Coordinates.md) and their [generalized velocities](./Generalized%20Coordinates.md) there is a [Lagrangian](./Lagrangian%20Formalism.md), usually called *the* [Lagrangian](./Lagrangian%20Formalism.md) of the [system](../Physical%20Systems.md), which can be used to accurately predict the evolution of the [system](../Physical%20Systems.md) through time.

>[!AXIOM] Axiom: Principle of Stationary Action
>
>For each set of [generalized coordinates](./Generalized%20Coordinates.md) and their [generalized velocities](./Generalized%20Coordinates.md) for a [system](../Physical%20Systems.md) of [point particles](./Point%20Particles.md) there exists a [Lagrangian](./Lagrangian%20Formalism.md) $\mathcal{L}$ such that, between any moments $t_1$ and $t_2$, the [path](./Generalized%20Coordinates.md) of the [system](../Physical%20Systems.md) in [configuration space](./Generalized%20Coordinates.md) is the one whose [action](./Lagrangian%20Formalism.md) is either the lowest or highest possible out of all [paths](./Generalized%20Coordinates.md).
>