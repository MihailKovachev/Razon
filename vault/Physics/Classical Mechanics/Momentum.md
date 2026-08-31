---
title: Momentum
tags:
    - classical-mechanics
    - physics
---

# Momentum

>[!DEFINITION] Definition: Momentum
>
>The **momentum** of a [point mass](./Point%20Mass.md) $m$ at time $t$ is the product of $m$ with its [velocity](../Kinematics/Velocity.md) $\mathbf{v}$:
>
>$$m \mathbf{v}$$
>
>>[!NOTATION]
>>
>>$$
>>\boldsymbol{p} \qquad \mathbf{p} \qquad \vec{p} \qquad \boldsymbol{P} \qquad \mathbf{P} \qquad \vec{P}
>>$$
>>
>

>[!DEFINITION] Definition: Impulse
>
>The **impulse** of a [physical system](./Classical%20Mechanics.md) between two [moments](./Classical%20Mechanics.md) $t_1$ and $t_2 \gt t_1$ is the change in the [momentum](./Momentum.md):
>
>$$
>\boldsymbol{p}(t_2) - \boldsymbol{p}(t_1)
>$$
>
>>[!NOTATION]
>>
>>$$
>>\mathbf{J} \qquad \boldsymbol{J} \qquad \vec{J}
>>$$
>>
>

>[!THEOREM] Theorem: Momentum and Force
>
>The [derivative](../../Mathematics/Analysis/Real%20Analysis/Real%20Vector-Valued%20Functions%20of%20a%20Real%20Variable/Differentiation/Differentiability%20(Real%20Parametric%20Curves).md) of the [momentum](./Momentum.md) of a [point mass](./Inertia.md#Point%20Masses) $m$ with respect to [time](./Classical%20Mechanics.md) is the sum $\sum_i {}_{\text{on }m}\boldsymbol{F}_i(t^{\ast})$ of all [forces](./Newtonian%20Formalism.md) currently acting on $m$:
>
>$$
>\frac{\mathrm{d}\boldsymbol{P}}{\mathrm{d}t}(t^{\ast}) = \sum_i {}_{\text{on }m}\boldsymbol{F}_i(t^{\ast})
>$$
>
>>[!NOTE] Note: Non-Inertial Frames
>>
>>When working in a [non-inertial reference frame](./Newtonian%20Formalism.md), the [inertial force](./Newtonian%20Formalism.md) must be included in $\sum_i {}_{\text{on }m}\boldsymbol{F}_i(t)$.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Impulse and Force
>
>The [impulse](./Momentum.md) of a [point mass](./Inertia.md#Point%20Masses) $m$ between two [moments](./Classical%20Mechanics.md) $t_1$ and $t_2 \gt t_1$ is given by the [integral](../../Mathematics/Analysis/Real%20Analysis/Real%20Parametric%20Curves/Integration%20of%20Parametric%20Curves.md) of the sum $\sum_i {}_{\text{on }m}\boldsymbol{F}_i(t)$ of all [forces](./Newtonian%20Formalism.md) acting on $m$ from $t_1$ to $t_2$:
>
>$$
>\boldsymbol{J} = \int_{t_1}^{t_2} \sum_i {}_{\text{on }m}\boldsymbol{F}_i(t) \mathop{\mathrm{d}t}
>$$
>
>>[!NOTE] Note: Non-Inertial Frames
>>
>>When working in a [non-inertial reference frame](./Newtonian%20Formalism.md), the [inertial force](./Newtonian%20Formalism.md) must be included in $\sum_i {}_{\text{on }m}\boldsymbol{F}_i(t)$.
>>
>
>>[!PROOF]-
>>
>>TODO
>>
>

>[!THEOREM] Theorem: Conservation of Momentum
>
>In an [inertial reference frame](./Newtonian%20Formalism.md), the total [momentum](./Momentum.md) of an [isolated physical system](./Classical%20Mechanics.md) remains constant.
>
>$$
>\boldsymbol{P} = \text{const} \qquad \boldsymbol{J} = \boldsymbol{0}
>$$
>
>>[!PROOF]-
>>
>>TODO
>>
>